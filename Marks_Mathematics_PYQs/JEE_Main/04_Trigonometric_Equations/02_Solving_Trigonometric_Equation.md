# JEE Main Mathematics - Trigonometric Equations

## Topic 2: Solving Trigonometric Equation

**Total Questions:** 75

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $S = \{\theta \in (-2\pi, 2\pi) : \cos\theta + 1 = \sqrt{3}\sin\theta\}$. Then $\sum_{\theta \in S}\theta$ is equal to:

**Options:**

- **(A)** $-\dfrac{2\pi}{3}$
- **(B)** $-\dfrac{4\pi}{3}$
- **(C)** $\dfrac{2\pi}{3}$
- **(D)** $\dfrac{4\pi}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\dfrac{4\pi}{3}$**

**Detailed Solution:**

Given equation: $\cos\theta + 1 = \sqrt{3}\sin\theta$

Using half-angle formulas, we get:

$2\cos^2\dfrac{\theta}{2} = 2\sqrt{3}\sin\dfrac{\theta}{2}\cos\dfrac{\theta}{2}$

$2\cos\dfrac{\theta}{2} \left( \cos\dfrac{\theta}{2} - \sqrt{3}\sin\dfrac{\theta}{2} \right) = 0$

This gives two cases:

Case 1: $\cos\dfrac{\theta}{2} = 0$

$\Rightarrow \dfrac{\theta}{2} = (2k+1)\dfrac{\pi}{2} \Rightarrow \theta = (2k+1)\pi$

Since $\theta \in (-2\pi, 2\pi)$, the possible values are $\theta = -\pi, \pi$.

Case 2: $\cos\dfrac{\theta}{2} - \sqrt{3}\sin\dfrac{\theta}{2} = 0$

$\Rightarrow \tan\dfrac{\theta}{2} = \dfrac{1}{\sqrt{3}}$

$\Rightarrow \dfrac{\theta}{2} = k\pi + \dfrac{\pi}{6} \Rightarrow \theta = 2k\pi + \dfrac{\pi}{3}$

Since $\theta \in (-2\pi, 2\pi)$, the possible values are:

For $k = 0$, $\theta = \dfrac{\pi}{3}$

For $k = -1$, $\theta = -2\pi + \dfrac{\pi}{3} = -\dfrac{5\pi}{3}$

Thus, the set of solutions is $S = \left\{-\pi, \pi, \dfrac{\pi}{3}, -\dfrac{5\pi}{3}\right\}$.

Sum of all solutions in $S$:

$\sum_{\theta \in S}\theta = -\pi + \pi + \dfrac{\pi}{3} - \dfrac{5\pi}{3} = -\dfrac{4\pi}{3}$

Answer: $-\dfrac{4\pi}{3}$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `numerical` | *Level:* `3`

If $S = \left\{\theta \in [-\pi, \pi] : \cos\theta \cos\dfrac{5\theta}{2} = \cos 7\theta \cos\dfrac{7\theta}{2}\right\}$, then $n(S)$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

Given equation: $\cos\theta \cos\dfrac{5\theta}{2} = \cos 7\theta \cos\dfrac{7\theta}{2}$

Multiplying both sides by $2$:

$2\cos\theta \cos\dfrac{5\theta}{2} = 2\cos 7\theta \cos\dfrac{7\theta}{2}$

Using the identity $2\cos A \cos B = \cos(A+B) + \cos(A-B)$:

$\cos\left(\theta + \dfrac{5\theta}{2}\right) + \cos\left(\theta - \dfrac{5\theta}{2}\right) = \cos\left(7\theta + \dfrac{7\theta}{2}\right) + \cos\left(7\theta - \dfrac{7\theta}{2}\right)$

$\cos\left(\dfrac{7\theta}{2}\right) + \cos\left(\dfrac{-3\theta}{2}\right) = \cos\left(\dfrac{21\theta}{2}\right) + \cos\left(\dfrac{7\theta}{2}\right)$

Since $\cos(-x) = \cos x$, we get:

$\cos\left(\dfrac{7\theta}{2}\right) + \cos\left(\dfrac{3\theta}{2}\right) = \cos\left(\dfrac{21\theta}{2}\right) + \cos\left(\dfrac{7\theta}{2}\right)$

$\cos\left(\dfrac{3\theta}{2}\right) = \cos\left(\dfrac{21\theta}{2}\right)$

$\cos\left(\dfrac{21\theta}{2}\right) - \cos\left(\dfrac{3\theta}{2}\right) = 0$

Using the identity $\cos C - \cos D = -2\sin\left(\dfrac{C+D}{2}\right)\sin\left(\dfrac{C-D}{2}\right)$:

$-2\sin\left(\dfrac{\dfrac{21\theta}{2} + \dfrac{3\theta}{2}}{2}\right)\sin\left(\dfrac{\dfrac{21\theta}{2} - \dfrac{3\theta}{2}}{2}\right) = 0$

$-2\sin(6\theta)\sin\left(\dfrac{9\theta}{2}\right) = 0$

This gives $\sin(6\theta) = 0$ or $\sin\left(\dfrac{9\theta}{2}\right) = 0$.

Case 1: $\sin(6\theta) = 0$

$6\theta = n\pi \Rightarrow \theta = \dfrac{n\pi}{6}$ for $n \in \mathbb{Z}$.

Since $\theta \in [-\pi, \pi]$, we have $-\pi \le \dfrac{n\pi}{6} \le \pi \Rightarrow -6 \le n \le 6$.

The possible values for $n$ are $\{-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6\}$.

This gives $13$ solutions.

Case 2: $\sin\left(\dfrac{9\theta}{2}\right) = 0$

$\dfrac{9\theta}{2} = m\pi \Rightarrow \theta = \dfrac{2m\pi}{9}$ for $m \in \mathbb{Z}$.

Since $\theta \in [-\pi, \pi]$, we have $-\pi \le \dfrac{2m\pi}{9} \le \pi \Rightarrow -4.5 \le m \le 4.5$.

The possible values for $m$ are $\{-4, -3, -2, -1, 0, 1, 2, 3, 4\}$.

This gives $9$ solutions.

To find common solutions, we equate the two sets of solutions:

$\dfrac{n\pi}{6} = \dfrac{2m\pi}{9} \Rightarrow 3n = 4m$

For $m \in \{-4, -3, -2, -1, 0, 1, 2, 3, 4\}$, $m$ must be a multiple of $3$. The valid values for $m$ are $-3, 0, 3$, which correspond to $n = -4, 0, 4$.

Thus, there are $3$ common solutions.

Total number of unique solutions $n(S) = 13 + 9 - 3 = 19$.

Answer: $19$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $S = \{x \in [-\pi, \pi] : \sin x (\sin x + \cos x) = a, a \in \mathbb{Z}\}$. Then $n(S)$ is equal to :

**Options:**

- **(A)** $3$
- **(B)** $6$
- **(C)** $7$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $9$**

**Detailed Solution:**

Given the equation: $\sin x (\sin x + \cos x) = a$

$\Rightarrow \sin^2 x + \sin x \cos x = a$

Using the double angle formulas $\sin^2 x = \dfrac{1 - \cos 2x}{2}$ and $\sin x \cos x = \dfrac{\sin 2x}{2}$, we get:

$\dfrac{1 - \cos 2x}{2} + \dfrac{\sin 2x}{2} = a$

$\Rightarrow \sin 2x - \cos 2x = 2a - 1$

We know that the range of $A\sin \theta + B\cos \theta$ is $[-\sqrt{A^2+B^2}, \sqrt{A^2+B^2}]$. Thus, the range of $\sin 2x - \cos 2x$ is $[-\sqrt{2}, \sqrt{2}]$.

$\Rightarrow -\sqrt{2} \le 2a - 1 \le \sqrt{2}$

$\Rightarrow 1 - 1.414 \le 2a \le 1 + 1.414$

$\Rightarrow -0.414 \le 2a \le 2.414$

$\Rightarrow -0.207 \le a \le 1.207$

Since $a \in \mathbb{Z}$, the possible values for $a$ are $0$ and $1$.

Case 1: $a = 0$
$\sin x (\sin x + \cos x) = 0$
$\Rightarrow \sin x = 0$ or $\sin x + \cos x = 0$
For $x \in [-\pi, \pi]$, $\sin x = 0 \Rightarrow x \in \{-\pi, 0, \pi\}$ (3 solutions)
$\sin x + \cos x = 0 \Rightarrow \tan x = -1 \Rightarrow x \in \{-\dfrac{\pi}{4}, \dfrac{3\pi}{4}\}$ (2 solutions)
Total solutions for $a = 0$ is $5$.

Case 2: $a = 1$
$\sin^2 x + \sin x \cos x = 1$
$\Rightarrow \sin x \cos x = 1 - \sin^2 x$
$\Rightarrow \sin x \cos x = \cos^2 x$
$\Rightarrow \cos x (\sin x - \cos x) = 0$
$\Rightarrow \cos x = 0$ or $\sin x - \cos x = 0$
For $x \in [-\pi, \pi]$, $\cos x = 0 \Rightarrow x \in \{-\dfrac{\pi}{2}, \dfrac{\pi}{2}\}$ (2 solutions)
$\sin x - \cos x = 0 \Rightarrow \tan x = 1 \Rightarrow x \in \{-\dfrac{3\pi}{4}, \dfrac{\pi}{4}\}$ (2 solutions)
Total solutions for $a = 1$ is $4$.

The total number of elements in the set $S$ is $n(S) = 5 + 4 = 9$.

Answer: $9$

</details>

---

### Q4. JEE Main 2026 (24 January Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of elements in the set $\left\{x \in\left[0,180^{\circ}\right]: \tan \left(x+100^{\circ}\right)=\tan \left(x+50^{\circ}\right) \tan x \tan \left(x-50^{\circ}\right)\right\}$ is $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

$\frac{\tan(x+100°)}{\tan x} = \tan(x+50°)\tan(x-50°)$
$\frac{\sin(x+100°)\cos x}{\cos(x+100°)\sin x} = \frac{\sin(x+50°)\sin(x-50°)}{\cos(x+50°)\cos(x-50°)}$
Applying Componendo & Dividendo:
$\frac{\sin(2x+100°)}{\sin 100°} = \frac{\cos 100°}{-\cos 2x}$
$2\sin(2x+100°)\cos 2x + \sin 200° = 0$
$\sin(4x+100°) + \sin 100° + \sin 200° = 0$
$\sin(4x+100°) = -2\sin 150° \cos 50°$
$\sin(4x+100°) = -\cos 50° = \sin(-40°)$
$\therefore 4x + 100° = n\pi + (-1)^n(-40°)$
$x = \frac{n\pi + (-1)^{n+1}(40°) - 100°}{4}$
$\therefore x = 30°, 55°, 120°, 145°$ in $(0, \pi)$
$\therefore$ Number of solutions $= 4$

</details>

---

### Q5. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Number of solutions of $\sqrt{3} \cos 2 \theta+8 \cos \theta+3 \sqrt{3}=0, \theta \in[-3 \pi, 2 \pi]$ is:

**Options:**

- **(A)** 0
- **(B)** 5
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

Using $\cos 2\theta = 2\cos^2\theta - 1$:
$2\sqrt{3}\cos^2\theta + 8\cos\theta + 2\sqrt{3} = 0 \Rightarrow \sqrt{3}\cos^2\theta + 4\cos\theta + \sqrt{3} = 0$.
$\cos\theta = \frac{-4 \pm 2}{2\sqrt{3}}$, giving $\cos\theta = -\frac{1}{\sqrt{3}}$ or $\cos\theta = -\sqrt{3}$ (rejected).
Let $\alpha = \cos^{-1}(-1/\sqrt{3}) \approx 2.186$ rad. General solution: $\theta = 2n\pi \pm \alpha$.
In $[-3\pi, 2\pi]$: $\theta = \alpha, -\alpha, 2\pi-\alpha, -2\pi+\alpha, -2\pi-\alpha$.
Total $= 5$ solutions.

</details>

---

### Q6. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of the equation
$\cos 2 \theta \cos \frac{\theta}{2}+\cos \frac{5 \theta}{2}=2 \cos ^3 \frac{5 \theta}{2}$
in $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ is :

**Options:**

- **(A)** 7
- **(B)** 5
- **(C)** 6
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 7**

**Detailed Solution:**

$\begin{aligned}
& \cos 2 \theta \cos \frac{\theta}{2}+\cos \frac{5 \theta}{2}=2 \cos ^3 \frac{5 \theta}{2} \\
& \frac{1}{2}\left(2 \cos 2 \theta \cos \frac{\theta}{2}\right)+\cos \frac{50}{2} \\
& =\frac{1}{2}\left(\cos \frac{15 \theta}{2}+3 \cos \frac{5 \theta}{2}\right)
\end{aligned}$
or solving
$\begin{aligned}
& \cos \frac{3 \theta}{2}=\cos \frac{15 \theta}{2} \\
& \cos \frac{15 \theta}{2}-\cos \frac{3 \theta}{2}=0 \\
& 2 \sin 30 \sin \frac{9 \theta}{2}=0
\end{aligned}$
$3 \theta=\mathrm{n} \pi \text { or } \frac{9 \theta}{2}=\mathrm{m} \pi$
$\begin{aligned}
& \theta=\frac{\mathrm{n} \pi}{3} \quad \theta=\frac{2 \mathrm{~m} \pi}{9} \\
& \theta=\left\{-\frac{\pi}{2}, \frac{\pi}{3}, 0\right\} \\
& \theta=\left\{-\frac{4 \pi}{9}, \frac{-2 \pi}{9}, \frac{4 \pi}{9}, \frac{2 \pi}{9}\right\}
\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If for $\theta \in\left[-\frac{\pi}{3}, 0\right]$, the points $(x, y)=\left(3 \tan \left(\theta+\frac{\pi}{3}\right), 2 \tan \left(\theta+\frac{\pi}{6}\right)\right)$ lie on $x y+\alpha x+\beta y+\gamma=0$, then $\alpha^2+\beta^2+\gamma^2$ is equal to :

**Options:**

- **(A)** 80
- **(B)** 72
- **(C)** 96
- **(D)** 75

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 75**

**Detailed Solution:**

$\begin{aligned}
& x=3\left(\frac{\tan \theta+\sqrt{3}}{1-\sqrt{3} \tan \theta}\right) \\
& x-\sqrt{3} \tan \theta=3 \tan \theta+3 \sqrt{3} \\
& \tan \theta=\frac{x-3 \sqrt{3}}{3+\sqrt{3} x} \ldots(1) \\
& 2\left(\frac{\tan \theta+\frac{1}{\sqrt{3}}}{1-\frac{\tan \theta}{\sqrt{3}}}=y\right) \\
& 2(\sqrt{3} \tan \theta+1)=y(\sqrt{3}-\tan \theta) \ldots .
\end{aligned}$
using (1) and (2)
$\begin{aligned}
& 2\left(\frac{x-3 \sqrt{3}}{\sqrt{3}+x}+1\right)=y\left(\sqrt{3}-\frac{(x-3 \sqrt{3})}{\sqrt{3}(\sqrt{3}+x)}\right) \\
& 2 \sqrt{3}(x-3 \sqrt{3}+x+\sqrt{3})=y(3(\sqrt{3}+x)-x+3 \sqrt{3}) \\
& 4 \sqrt{3} x-12=y(2 x+6 \sqrt{3}) \\
& x y-2 \sqrt{3} x+3 \sqrt{3} y-6=0 \\
& \Rightarrow \alpha=-2 \sqrt{3}, \beta=3 \sqrt{3}, \gamma=-6 \\
& \alpha^2+\beta^2+\gamma^2=12+27+36=75
\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $10 \sin ^4 \theta+15 \cos ^4 \theta=6$, then the value of $\frac{27 \operatorname{cosec}^6 \theta+8 \sec ^6 \theta}{16 \sec ^8 \theta}$ is:

**Options:**

- **(A)** $\frac{2}{5}$
- **(B)** $\frac{3}{4}$
- **(C)** $\frac{3}{5}$
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{5}$**

**Detailed Solution:**

$\begin{aligned} & 10\left(\sin ^2 \theta\right)^2+15\left(1-\sin ^2 \theta\right)^2=6 \\ & \text { Let } \sin ^2 \theta=\mathrm{t} \Rightarrow 10 \mathrm{t}^2+15(1-\mathrm{t})^2=16 \\ & 10 \mathrm{t}^2+15-30 \mathrm{t}+15 \mathrm{t}^2=6 \\ & 25 \mathrm{t}^2-30 \mathrm{t}+9=0 \\ & (5 \mathrm{t}-3)^2=0 \\ & \sin ^2 \theta=\frac{3}{5} \text { and } \cos ^2 \theta=\frac{2}{5} \\ & \frac{27 \times \frac{125}{27}+8+\frac{125}{8}}{16\left(\frac{5}{2}\right)^4}=\frac{250}{125 \times 5}=\frac{2}{5}\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of equation $(4-\sqrt{3}) \sin x$ $-2 \sqrt{3} \cos ^2 x=-\frac{4}{1+\sqrt{3}}, x \in\left[-2 \pi, \frac{5 \pi}{2}\right]$ is

**Options:**

- **(A)** $4$
- **(B)** $3$
- **(C)** $6$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5$**

**Detailed Solution:**

$\begin{aligned} & (4-\sqrt{3}) \sin x-2 \sqrt{3} \cos ^2 x=\frac{-4}{1+\sqrt{3}}, x \in\left[-2 \pi, \frac{5 \pi}{2}\right] \\ & \Rightarrow(4-\sqrt{3}) \sin x-2 \sqrt{3}\left(1-\sin ^2 x\right)=2(1-\sqrt{3}) \\ & \Rightarrow 2 \sqrt{3} \sin ^2 x+4 \sin x-\sqrt{3} \sin x-2=0 \\ & \Rightarrow(2 \sin x-1)(\sqrt{3} \sin x+2)=0 \\ & \Rightarrow \sin x=\frac{1}{2} \\ & \therefore \text { Number of solution }=5\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions of the equation $2 x+3 \tan x=\pi, x \in[-2 \pi, 2 \pi]-\left\{ \pm \frac{\pi}{2}, \pm \frac{3 \pi}{2}\right\}$ is

**Options:**

- **(A)** $6$
- **(B)** $5$
- **(C)** $4$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5$**

**Detailed Solution:**

$\tan \mathrm{x}=\frac{\pi}{3}-\frac{2 \mathrm{x}}{3}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Ecn5zcYEeQbU5AdH6_RtcgfX9aCyPfSNonrQ2PtRKXI.original.fullsize.png"/>
5 solutions

</details>

---

### Q11. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\theta \in\left[-\frac{7 \pi}{6}, \frac{4 \pi}{3}\right]$, then the number of solutions of $\sqrt{3} \operatorname{cosec}^2 \theta-2(\sqrt{3}-1) \operatorname{cosec} \theta-4=0$, is equal to

**Options:**

- **(A)** $6$
- **(B)** $8$
- **(C)** $10$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6$**

**Detailed Solution:**

$\begin{aligned} & \operatorname{cosec} \theta=\frac{2(\sqrt{3}-1) \pm \sqrt{4(3+1-2 \sqrt{3})+16 \sqrt{3}}}{2 \sqrt{3}} \\ & =\frac{2(\sqrt{3-1}) \pm \sqrt{16+8 \sqrt{3}}}{2 \sqrt{3}} \\ & =\frac{2(\sqrt{3}-1) \pm(2+2 \sqrt{3})}{2 \sqrt{3}}\end{aligned}$
$\operatorname{cosec} \theta=2$ or $\frac{-2}{\sqrt{3}}$
$\therefore \sin \theta=\frac{1}{2}$ or $\frac{-\sqrt{3}}{2}$
$\therefore \sin \theta=\frac{1}{2}$ has 3 solutions \& also $\sin \theta=\frac{-\sqrt{3}}{2}$
has 3 solutions in $\left[\frac{-7 \pi}{6}, \frac{4 \pi}{3}\right]$

</details>

---

### Q12. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\theta \in[-2 \pi, 2 \pi]$, then the number of solutions of $2 \sqrt{2} \cos ^2 \theta+(2-\sqrt{6}) \cos \theta-\sqrt{3}=0$, is equal to:

**Options:**

- **(A)** 12
- **(B)** 6
- **(C)** 8
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8**

**Detailed Solution:**

$\begin{aligned} & 2 \sqrt{2} \cos ^2 \theta+2 \cos \theta-\sqrt{6} \cos \theta-\sqrt{3}=0 \\ & (2 \cos \theta-\sqrt{3})(\sqrt{2} \cos \theta+1)=0 \\ & \cos \theta=\frac{\sqrt{3}}{2}, \frac{-1}{\sqrt{2}}\end{aligned}$
Number of solution $=8$

</details>

---

### Q13. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The sum of all values of $\theta \in[0,2 \pi]$ satisfying $2 \sin ^2 \theta=\cos 2 \theta$ and $2 \cos ^2 \theta=3 \sin \theta$ is

**Options:**

- **(A)** $4 \pi$
- **(B)** $\frac{5 \pi}{6}$
- **(C)** $\pi$
- **(D)** $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\pi$**

**Detailed Solution:**

$\begin{aligned}
& 2 \sin ^2 \theta=\cos 2 \theta \\
& 2 \sin ^2 \theta=1-2 \sin ^2 \theta \\
& 4 \sin ^2 \theta=1 \\
& \sin ^2 \theta=\frac{1}{4} \\
& \sin \theta= \pm \frac{1}{2} \\
& 2 \cos ^2 \theta=3 \sin \theta \\
& 2-2 \sin ^2 \theta+3 \sin \theta-2=0 \\
& (2 \sin \theta-1)(2 \sin \theta-2)=0 \\
& \sin \theta=\frac{1}{2}
\end{aligned}$
so common equation which satisfy both equations is $\sin \theta=\frac{1}{2}$
$\theta=\frac{\pi}{6}, \frac{5 \pi}{6} \quad(\theta \in[0,2 \pi])$

Sum $=\pi$

</details>

---

### Q14. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of solutions of $\sin ^2 x+\left(2+2 x-x^2\right) \sin x-3(x-1)^2=0$, where $-\pi \leq x \leq \pi$, is________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

$\sin ^2 x-\left(x^2-2 x-2\right) \sin x-3(x-1)^2=0$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Te7nat8bKp7y0w3Ngaw26uy0jG0Oypp4WBXaXS8nvEs.original.fullsize.png">
$\begin{aligned} & \sin x=-3(\text { reject }) \text { or }(x-1)^2 \\ & \sin x=(x-1)^2\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uxid6risaV7wIu3L0RbfRs7LBdcoRYLk__zVKKQmswo.original.fullsize.png">

</details>

---

### Q15. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Suppose $\theta \epsilon\left[0, \frac{\pi}{4}\right]$ is a solution of $4 \cos \theta-3 \sin \theta=1$. Then $\cos \theta$ is equal to :

**Options:**

- **(A)** $\frac{4}{(3 \sqrt{6}+2)}$
- **(B)** $\frac{6+\sqrt{6}}{(3 \sqrt{6}+2)}$
- **(C)** $\frac{4}{(3 \sqrt{6}-2)}$
- **(D)** $\frac{6-\sqrt{6}}{(3 \sqrt{6}-2)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{(3 \sqrt{6}-2)}$**

**Detailed Solution:**

$4\left(\frac{1-\tan ^2 \theta / 2}{1+\tan ^2 \theta / 2}\right)-3\left(\frac{2 \tan \frac{\theta}{2}}{1+\tan ^2 \frac{\theta}{2}}\right)=1$
let $\tan \frac{\theta}{2}=\mathrm{t}$
$\begin{aligned}
& \frac{4-4 t^2-6 t}{1+t^2}=1 \\
& 4-4 t^2-6 t=1+t^2
\end{aligned}$
$\begin{aligned} & \Rightarrow 5 t^2+6 t-3=0 \\ & \Rightarrow t=\frac{-6 \pm \sqrt{36-4(5)(-3)}}{2(5)} \\ & =\frac{-6 \pm \sqrt{96}}{10} \\ & =\frac{-6 \pm 4 \sqrt{6}}{10} \\ & t=\frac{-3+2 \sqrt{6}}{5} \\ & \cos \theta=\frac{1-t^2}{1+t^2}=\frac{1-\left(\frac{2 \sqrt{6}-3}{5}\right)^2}{1+\left(\frac{2 \sqrt{6}-3}{5}\right)^2}=\frac{1-\left(\frac{24+9-12 \sqrt{6}}{25}\right)}{1+\left(\frac{24+9-12 \sqrt{6}}{25}\right)} \\ & =\frac{25-33+12 \sqrt{6}}{25+33-12 \sqrt{6}}=\frac{12 \sqrt{6}-8}{58-12 \sqrt{6}}=\frac{6 \sqrt{6}-4}{29-6 \sqrt{6}} \times \frac{29+6 \sqrt{6}}{29+6 \sqrt{6}} \\ & =\frac{100+150 \sqrt{6}}{625}=\frac{4+6 \sqrt{6}}{25} \times \frac{4-6 \sqrt{6}}{4-6 \sqrt{6}} \\ & =\frac{-200}{25(4-6 \sqrt{6})}=\frac{-8}{4-6 \sqrt{6}}=\frac{4}{3 \sqrt{6}-2}\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $S=\left\{\sin ^2 2 \theta:\left(\sin ^4 \theta+\cos ^4 \theta\right) x^2+(\sin 2 \theta) x+\left(\sin ^6 \theta+\cos ^6 \theta\right)=0\right.$ has real roots $\}$. If $\alpha$ and $\beta$ be the smallest and largest elements of the set $S$, respectively, then $3\left((\alpha-2)^2+(\beta-1)^2\right)$ equals _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

$\begin{aligned} & D=(\sin 2 \theta)^2-4\left(1-\frac{\sin ^2 2 \theta}{2}\right)\left(1-\frac{3}{4} \sin ^2 2 \theta\right) \\ & =(\sin 2 \theta)^2-4\left(1-\frac{5}{4} \sin ^2 2 \theta+\frac{3}{8} \sin ^4 2 \theta\right) \\ & D=-\frac{3}{2} \sin ^4 2 \theta+6 \sin ^2 2 \theta-4>0 \\ & 3 \sin ^4 2 \theta-12 \sin ^2 2 \theta+8 < 0 \\ & \sin ^2 2 \theta=\frac{12 \pm \sqrt{12^2-12.8}}{6}=\frac{12 \pm 4 \sqrt{3}}{6}=\frac{6 \pm 2 \sqrt{3}}{3} \\ & \sin ^2 2 \theta=2 \pm \frac{2}{\sqrt{3}}, \text { but } \sin ^2 2 \theta \in[0,1] \\ & \therefore \alpha=2-\frac{2}{\sqrt{3}}, \beta=1 \rightarrow(\alpha-2)^2=\frac{4}{3},(\beta-1)^2=0 \\ & 3(\alpha-2)^2+(\beta-1)^2=4\end{aligned}$

</details>

---

### Q17. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>−</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>9</mn><mo>−</mo><mn>4</mn><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>;</mo><mi>x</mi><mo>∈</mo><mfenced close="]" open="["><mrow><mo>−</mo><mn>2</mn><mi>π</mi><mo>,</mo><mn>2</mn><mi>π</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>9</mn><mo>-</mo><mn>4</mn><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>9</mn><mo>-</mo><mn>4</mn><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>4</mn><mi>cos</mi><mi>x</mi><mo>-</mo><mn>13</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>4</mn><mi>cos</mi><mi>x</mi><mo>=</mo><mn>13</mn></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>≤</mo><mi>cos</mi><mi>x</mi><mo>≤</mo><mn>1</mn></math></p><p>So, the maximum value of LHS is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>12</mn></math></p><p>But, RHS is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>.</p><p>So, no solutions are possible for the given equation.</p>

</details>

---

### Q18. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>4</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math> has exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> solutions in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="⌉" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mi mathvariant="normal">n</mi><mi>π</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo><mi mathvariant="normal">n</mi><mo>∈</mo><mi mathvariant="normal">N</mi></math>, then the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mi>x</mi><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn></math> belong to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>∞</mo><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mn>0</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><msqrt><mn>17</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mfrac><msqrt><mn>17</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mn>0</mn><mo>)</mo></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>4</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>·</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>4</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>·</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>+</mo><mn>4</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>4</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>6</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Now, for exactly three solution we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><mn>5</mn></math> (in the given interval)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>5</mn><mo>±</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>So, the required interval is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mn>0</mn><mo>)</mo></math>.</p>

</details>

---

### Q19. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mi>R</mi></math> of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mn>2</mn><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mn>2</mn><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>x</mi><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>-</mo><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>x</mi><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mrow><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mn>4</mn></mfrac></mstyle></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mfenced><mfrac><mrow><mn>3</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow><mrow><mn>4</mn><mo>-</mo><mstyle displaystyle="true"><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mstyle></mrow></mfrac></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mfenced><mfrac><mrow><mn>3</mn><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow><mrow><mn>4</mn><mo>-</mo><mstyle displaystyle="true"><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mstyle></mrow></mfrac></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, the sum of real roots is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>.</p>

</details>

---

### Q20. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mo>-</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>&lt;</mo><mi>α</mi><mo>&lt;</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></math> is the solution of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>cos</mi><mi>θ</mi><mo>+</mo><mn>5</mn><mi>sin</mi><mi>θ</mi><mo>=</mo><mn>1</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>α</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mo>-</mo><msqrt><mn>10</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mo>-</mo><msqrt><mn>10</mn></msqrt></mrow><mn>12</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>10</mn></msqrt><mo>-</mo><mn>10</mn></mrow><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>10</mn></msqrt><mo>-</mo><mn>10</mn></mrow><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>10</mn></msqrt><mo>-</mo><mn>10</mn></mrow><mn>12</mn></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>cos</mi><mi>θ</mi><mo>+</mo><mn>5</mn><mi>sin</mi><mi>θ</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>θ</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>θ</mi><mn>2</mn></mfrac></mrow></mfrac></mfenced><mo>+</mo><mn>5</mn><mfenced><mfrac><mrow><mn>2</mn><mi>tan</mi><mfrac><mi>θ</mi><mn>2</mn></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>θ</mi><mn>2</mn></mfrac></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>θ</mi><mn>2</mn></mfrac><mo>-</mo><mn>10</mn><mi>tan</mi><mfrac><mi>θ</mi><mn>2</mn></mfrac><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfrac><mi>θ</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><mo>±</mo><msqrt><mn>100</mn><mo>-</mo><mn>4</mn><mfenced><mn>5</mn></mfenced><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></msqrt></mrow><mrow><mn>2</mn><mo>×</mo><mn>5</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfrac><mi>θ</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><mo>±</mo><msqrt><mn>160</mn></msqrt></mrow><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfrac><mi>θ</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>±</mo><msqrt><mn>40</mn></msqrt></mrow><mn>5</mn></mfrac></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>∈</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mi>π</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>α</mi><mn>2</mn></mfrac><mo>∈</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mi>π</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>π</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfrac><mi>α</mi><mn>2</mn></mfrac><mo>∈</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mfrac><mi>α</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>40</mn></msqrt></mrow><mn>5</mn></mfrac></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>θ</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>θ</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>θ</mi><mn>2</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mi>α</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>40</mn></msqrt></mrow><mn>5</mn></mfrac></mstyle></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>40</mn></msqrt></mrow><mn>5</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mi>α</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>40</mn></msqrt></mrow><mn>5</mn></mfrac></mstyle></mfenced></mrow><mrow><mn>2</mn><mfenced><mstyle displaystyle="true"><mfrac><msqrt><mn>40</mn></msqrt><mn>5</mn></mfrac></mstyle></mfenced><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>5</mn></mfrac></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mi>α</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>40</mn></msqrt></mrow><mrow><msqrt><mn>40</mn></msqrt><mo>-</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mi>α</mi><mo>=</mo><mfrac><mrow><msqrt><mn>40</mn></msqrt><mo>-</mo><mn>20</mn></mrow><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>tan</mi><mi>α</mi><mo>=</mo><mfrac><mrow><msqrt><mn>10</mn></msqrt><mo>-</mo><mn>10</mn></mrow><mn>12</mn></mfrac></math></p>

</details>

---

### Q21. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mn>2</mn></msup><mi>θ</mi><mo>-</mo><mn>5</mn><mi>sec</mi><mi>θ</mi><mo>=</mo><mn>1</mn></math> has exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> solutions in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mi mathvariant="normal">n</mi><mi>π</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math>, for the least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>∈</mo><mi mathvariant="normal">N</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi mathvariant="normal">k</mi><mo>=</mo><mn>1</mn></mrow><mi mathvariant="normal">n</mi></munderover><mfrac><mi mathvariant="normal">k</mi><msup><mn>2</mn><mi mathvariant="normal">k</mi></msup></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mn>2</mn><mn>15</mn></msup></mfrac><mfenced><mrow><msup><mn>2</mn><mn>14</mn></msup><mo>-</mo><mn>14</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mn>2</mn><mn>14</mn></msup></mfrac><mfenced><mrow><msup><mn>2</mn><mn>15</mn></msup><mo>-</mo><mn>15</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><mn>15</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac><mfenced><mrow><msup><mn>2</mn><mn>14</mn></msup><mo>-</mo><mn>15</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac><mfenced><mrow><msup><mn>2</mn><mn>14</mn></msup><mo>-</mo><mn>15</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mn>2</mn></msup><mi mathvariant="normal">θ</mi><mo>-</mo><mn>5</mn><mi>secθ</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mfenced><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">θ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>5</mn><mi>secθ</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">θ</mi><mo>-</mo><mn>5</mn><mi>secθ</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mi>sec</mi><mn>2</mn></msup><mi mathvariant="normal">θ</mi><mo>-</mo><mn>6</mn><mi>secθ</mi><mo>+</mo><mi>secθ</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>secθ</mi><mfenced><mrow><mi>sec</mi><mi>θ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mi>secθ</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>(</mo><mn>2</mn><mi>secθ</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>secθ</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>secθ</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cosθ</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo> </mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>≤</mo><mi>cosθ</mi><mo>≤1</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cosθ</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>=</mo><mn>13</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi mathvariant="normal">k</mi><mo>=</mo><mn>1</mn></mrow><mn>13</mn></munderover><mfrac><mi mathvariant="normal">k</mi><msup><mn>2</mn><mi mathvariant="normal">k</mi></msup></mfrac><mo>=</mo><mi mathvariant="normal">S</mi></math> (say)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>…</mo><mo>.</mo><mo>+</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo> </mo><mi mathvariant="normal">S</mi><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>…</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>12</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac><mo>+</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>14</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>-</mo><mfrac><mi mathvariant="normal">S</mi><mn>2</mn></mfrac><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>…</mo><mo>.</mo><mo>+</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>…</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>12</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac><mo>+</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>14</mn></msup></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi mathvariant="normal">S</mi><mn>2</mn></mfrac><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></mrow></mfenced><mo>-</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>14</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi mathvariant="normal">S</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>·</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfrac><mo>-</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>14</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi mathvariant="normal">S</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>·</mo><mfrac><mfrac><mrow><msup><mn>2</mn><mn>13</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mn>13</mn></msup></mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac></mfrac><mo>-</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>14</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><mn>2</mn><mo>·</mo><mfenced><mfrac><mrow><msup><mn>2</mn><mn>13</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mn>13</mn></msup></mfrac></mfenced><mo>-</mo><mfrac><mn>13</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><mfenced><mfrac><mrow><msup><mn>2</mn><mn>14</mn></msup><mo>-</mo><mn>2</mn><mo>-</mo><mn>13</mn></mrow><msup><mn>2</mn><mn>13</mn></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">S</mi><mo>=</mo><mfenced><mfrac><mrow><msup><mn>2</mn><mn>14</mn></msup><mo>-</mo><mn>15</mn></mrow><msup><mn>2</mn><mn>13</mn></msup></mfrac></mfenced></math></p>

</details>

---

### Q22. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let the set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>∈</mo><mi>R</mi></math> such that the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>a</mi><mi>sin</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>a</mi><mo>-</mo><mn>7</mn></math> has a solution be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>p</mi><mo>,</mo><mo> </mo><mi>q</mi><mo>]</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mi>tan</mi><mn>9</mn><mo>°</mo><mo>-</mo><mi>tan</mi><mn>27</mn><mo>°</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mi>cot</mi><mn>63</mn><mo>°</mo></mrow></mfrac><mo>+</mo><mi>tan</mi><mn>81</mn><mo>°</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mi>q</mi><mi>r</mi></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **48**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>a</mi><mo>·</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>a</mi><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>a</mi><mo>×</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>a</mi><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>×</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>a</mi><mo>=</mo><mo>-</mo><mn>8</mn><mo>+</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>(</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo>(</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>2</mn><mo> </mo><mfenced close="]" open="["><mtext>Not possible</mtext></mfenced><mo>,</mo><mo> </mo><mi>a</mi><mo>=</mo><mn>2</mn><mo>(</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>≤</mo><mi>sin</mi><mi>x</mi><mo>≤</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">a</mi><mo>∈</mo><mo>[</mo><mn>2</mn><mo>,</mo><mn>6</mn><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>p</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>q</mi><mo>=</mo><mn>6</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mi>tan</mi><msup><mn>9</mn><mo>°</mo></msup><mo>+</mo><mi>cot</mi><msup><mn>9</mn><mo>°</mo></msup><mo>-</mo><mi>tan</mi><msup><mn>27</mn><mo>°</mo></msup><mo>-</mo><mi>cot</mi><msup><mn>27</mn><mo>°</mo></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><msup><mn>9</mn><mo>°</mo></msup><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><msup><mn>9</mn><mo>°</mo></msup></mrow><mrow><mi>sin</mi><msup><mn>9</mn><mo>°</mo></msup><mo>·</mo><mi>cos</mi><msup><mn>9</mn><mo>°</mo></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><msup><mn>27</mn><mo>°</mo></msup><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><msup><mn>27</mn><mo>°</mo></msup></mrow><mrow><mi>sin</mi><msup><mn>27</mn><mo>°</mo></msup><mo>·</mo><mi>cos</mi><msup><mn>27</mn><mo>°</mo></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><msup><mn>9</mn><mo>°</mo></msup><mo>·</mo><mi>cos</mi><msup><mn>9</mn><mo>°</mo></msup></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><msup><mn>27</mn><mo>°</mo></msup><mo>·</mo><mi>cos</mi><msup><mn>27</mn><mo>°</mo></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mn>2</mn><mo>×</mo><mi>sin</mi><msup><mn>9</mn><mo>°</mo></msup><mo>·</mo><mi>cos</mi><msup><mn>9</mn><mo>°</mo></msup></mrow></mfrac><mo>-</mo><mfrac><mn>2</mn><mrow><mn>2</mn><mo>×</mo><mi>sin</mi><msup><mn>27</mn><mo>°</mo></msup><mo>·</mo><mi>cos</mi><msup><mn>27</mn><mo>°</mo></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mi>sin</mi><msup><mn>18</mn><mo>°</mo></msup></mrow></mfrac><mo>-</mo><mfrac><mn>2</mn><mrow><mi>sin</mi><msup><mn>54</mn><mo>°</mo></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfrac><mn>4</mn><mrow><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>4</mn><mrow><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mn>8</mn><mfenced close="]" open="["><mfrac><mrow><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn><mo>-</mo><msqrt><mn>5</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><mn>5</mn><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mn>8</mn><mfenced><mfrac><mn>2</mn><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>p</mi><mo>·</mo><mi>q</mi><mo>·</mo><mi>r</mi><mo>=</mo><mn>2</mn><mo>×</mo><mn>6</mn><mo>×</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>p</mi><mo>·</mo><mi>q</mi><mo>·</mo><mi>r</mi><mo>=</mo><mn>48</mn></math></p>

</details>

---

### Q23. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>]</mo><mo>:</mo><mn>3</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mn>5</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mn>5</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mfenced close="]" open="["><mrow><mn>3</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>-</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>-</mo><mn>2</mn><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>3</mn></msup><mo>-</mo><msup><mi>b</mi><mn>3</mn></msup><mo>=</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>)</mo><mfenced close="]" open="["><mrow><mn>3</mn><mi>t</mi><mo>+</mo><mn>2</mn><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>)</mo><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#960;</mi><mo>,</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>11</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total solution <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q24. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>:</mo><msup><mn>9</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>9</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>10</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><munder><mo>&#8721;</mo><mrow><mi>x</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mfrac><mi>x</mi><mn>3</mn></mfrac></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>(</mo><mi>&#946;</mi><mo>-</mo><mn>14</mn><msup><mo>)</mo><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><msup><mn>9</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>10</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mi>t</mi></math>, then above equation will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mi>t</mi></mfrac><mo>+</mo><mi>t</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>t</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>t</mi><mo>=</mo><mn>1</mn></math></p><p>So, when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>9</mn><mo>&#8658;</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>, as given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mstyle displaystyle="false"><munder><mo>&#8721;</mo><mrow><mi>x</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder></mstyle><mfenced><mfrac><mi>x</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mfrac><mn>0</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>12</mn></mfrac></mfenced><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mo>-</mo><mi mathvariant="normal">&#960;</mi></mrow><mn>12</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>+</mo><mn>2</mn><msup><mfenced><mrow><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14</mn><mo>-</mo><mn>8</mn><msqrt><mn>3</mn></msqrt></math></p><p>So, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><msup><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mn>14</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>64</mn><mo>&#215;</mo><mn>3</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>32</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q25. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> for which the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>&#955;</mi></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><msup><mfenced><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>4</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn><mfenced open="[" close="]"><mrow><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>2</mn><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mi>max</mi></msub><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>  (max Value)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#955;</mi><mi>min</mi></msub><mo>=</mo><mn>2</mn><mfenced><mrow><mn>0</mn><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>  (Minimum Value)</p><p>So, range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q26. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mo>(</mo><mn>3</mn><mi>&#960;</mi><mo>+</mo><mi>&#952;</mi><mo>)</mo></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mi>&#960;</mi><mo>]</mo><mo>:</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math>.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#946;</mi><mo>=</mo><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>&#952;</mi></math>  then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>&#946;</mi><mo>)</mo></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mo>(</mo><mn>3</mn><mi mathvariant="normal">&#960;</mi><mo>+</mo><mi>&#952;</mi><mo>)</mo></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mi>&#960;</mi><mo>]</mo><mo>:</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>&#952;</mi></mrow></mfenced><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mo>(</mo><mn>3</mn><mi mathvariant="normal">&#960;</mi><mo>+</mo><mi>&#952;</mi><mo>)</mo></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mn>3</mn><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mn>4</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mrow><mi>cos</mi><mo>&#160;</mo><mn>4</mn><mi>&#952;</mi></mrow><mn>4</mn></mfrac></math></p><p>Now on differentiating we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mi>sin</mi><mo>&#160;</mo><mn>4</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mi>sin</mi><mo>&#160;</mo><mn>4</mn><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#952;</mi><mo>=</mo><mi mathvariant="normal">n</mi><mi>&#960;</mi><mo>+</mo><mo>(</mo><mo>-</mo><mn>1</mn><msup><mo>)</mo><mi mathvariant="normal">n</mi></msup><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">n</mi><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mo>(</mo><mo>-</mo><mn>1</mn><msup><mo>)</mo><mi mathvariant="normal">n</mi></msup><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>,</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mrow></mfenced><mo>,</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mrow></mfenced><mo>,</mo><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#946;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>&#946;</mi><mo>)</mo><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mrow><mi>cos</mi><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q27. JEE Main 2023 (25 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> respectively are the numbers of positive and negative value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mi>&#960;</mi><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> that satisfy the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mi>cos</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>=</mo><mi>cos</mi><mn>3</mn><mi>&#952;</mi><mi>cos</mi><mfrac><mrow><mn>9</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>n</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>&#183;</mo><mi>cos</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>=</mo><mi>cos</mi><mn>3</mn><mi>&#952;</mi><mo>&#183;</mo><mi>cos</mi><mfrac><mrow><mn>9</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mi>cos</mi><mfenced><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><mn>9</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mfenced><mi>cos</mi><mn>3</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>5</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>3</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>15</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>3</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>15</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>5</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>15</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>2</mn><mi mathvariant="normal">k</mi><mi>&#960;</mi><mo>&#177;</mo><mfrac><mrow><mn>5</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac><mo>;</mo><mo>&#160;</mo><mi>k</mi><mo>&#8712;</mo><mi>Z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">k</mi><mi>&#960;</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">k</mi><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mi>k</mi><mi>&#960;</mi></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#952;</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mi>&#960;</mi><mo>,</mo><mo>-</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>5</mn></mfrac><mo>,</mo><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>5</mn><mo>,</mo><mi>n</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>m</mi><mi>n</mi><mo>=</mo><mn>25</mn></math>.</p>

</details>

---

### Q28. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>)</mo><mo>:</mo><mo>&#160;</mo><mi>tan</mi><mfenced><mi>&#960;cos&#952;</mi></mfenced><mo>+</mo><mi>tan</mi><mfenced><mi>&#960;sin&#952;</mi></mfenced><mo>=</mo><mn>0</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mo>)</mo><mo>:</mo><mo>&#160;</mo><mi>tan</mi><mfenced><mi>&#960;cos&#952;</mi></mfenced><mo>+</mo><mi>tan</mi><mfenced><mi>&#960;sin&#952;</mi></mfenced><mo>=</mo><mn>0</mn></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mi>&#960;cos&#952;</mi></mfenced><mo>+</mo><mi>tan</mi><mfenced><mi>&#960;sin&#952;</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mfenced><mi>&#960;cos&#952;</mi></mfenced><mo>=</mo><mo>-</mo><mi>tan</mi><mfenced><mi>&#960;sin&#952;</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mfenced><mi>&#960;cos&#952;</mi></mfenced><mo>=</mo><mi>tan</mi><mfenced><mrow><mo>-</mo><mi>&#960;sin&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#960;cos&#952;</mi><mo>=</mo><mi>n</mi><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi>&#960;sin&#952;</mi><mo>;</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>Z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin&#952;</mi><mo>+</mo><mi>cos&#952;</mi><mo>=</mo><mi>n</mi></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>&#8804;</mo><mi>sin&#952;</mi><mo>+</mo><mi>cos&#952;</mi><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>&#8804;</mo><mi>n</mi><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>Z</mi></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q29. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The number of elements in the set</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>:</mo><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><mn>6</mn></mfrac></mfenced><mo>=</mo><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><msup><mn>4</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** infinite

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><mn>6</mn></mfrac></mfenced><mo>=</mo><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><msup><mn>4</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></math></p><p>Now we know that maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi></math> function is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><mn>6</mn></mfrac></mfenced><mo>&#8804;</mo><mn>2</mn></math> and using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>M</mi><mo>&#8805;</mo><mi>G</mi><mo>.</mo><mi>M</mi></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><msup><mn>4</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>&#8805;</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">S</mi><mo>.</mo><mo>&#8804;</mo><mn>2</mn><mo>.</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">s</mi><mo>&#160;</mo><mo>&#8805;</mo><mn>2</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">S</mi><mo>.</mo><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">S</mi><mo>.</mo><mo>=</mo><mn>2</mn></math></p><p>Now equating both to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><msup><mn>4</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mn>2</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><mn>6</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mi>x</mi></msup><mo>+</mo><msup><mn>4</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mn>2</mn></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math> </p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we can see common solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> </p><p>Hence, possible solution is only one.</p></blockquote>

</details>

---

### Q30. JEE Main 2022 (29 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>)</mo><mo>:</mo><mn>7</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn></mrow></mfenced></math>. Then, the sum of roots of all the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cot</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mn>6</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi>&#952;</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi></math>, is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>5</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mfenced><mrow><mn>2</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mfenced close="}" open="{"><mtext>which&#160;is&#160;not&#160;possible</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p>For all four values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>co</mi><msup><mtext>t</mtext><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mtext>will&#160;become&#160;</mtext><mn>1</mn><mo>&#160;</mo><mtext>and&#160;</mtext><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mtext>will&#160;become</mtext><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cot</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mn>6</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p>Sum of roots of all four equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>16</mn></math>.</p></blockquote>

</details>

---

### Q31. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="["><mrow><mo>-</mo><mi>&#960;</mi><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math>. Then the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi><mo>:</mo><mi>tan</mi><mi>&#952;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msqrt><mn>5</mn></msqrt><mo>-</mo><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="["><mrow><mo>-</mo><mi>&#960;</mi><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> and the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi><mo>:</mo><mi>tan</mi><mi>&#952;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msqrt><mn>5</mn></msqrt><mo>-</mo><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#945;</mi><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msqrt><mn>5</mn></msqrt><mo>-</mo><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math> becomes,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#945;</mi><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>tan</mi><mi>&#945;</mi><mo>-</mo><mi>tan</mi><mfenced><mrow><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p><p>On rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>&#945;</mi><mo>-</mo><mi>tan</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#945;</mi><mi>tan</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac></math></p><p>On using formula <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mi>A</mi><mo>-</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>A</mi><mo>-</mo><mi>tan</mi><mi>B</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>A</mi><mi>tan</mi><mi>B</mi></mrow></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mi>tan</mi><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#952;</mi><mo>=</mo><mi>n</mi><mi>&#960;</mi><mo>+</mo><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>3</mn><mi>&#952;</mi><mo>=</mo><mi>&#945;</mi><mo>-</mo><mi>n</mi><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#945;</mi><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mi>n</mi><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>;</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>Z</mi></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mi>&#960;</mi><mo>,</mo><mi>&#960;</mi><mo>/</mo><mn>2</mn><mo>)</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></math> are acceptable solution</p><p>So, total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> solutions are possible.</p></blockquote>

</details>

---

### Q32. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

If the sum of solutions of the system of equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>&#960;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p>So, the common solution is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p>Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi><mo>+</mo><mn>11</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>=</mo><mn>3</mn><mi>&#960;</mi><mo>=</mo><mi mathvariant="normal">k</mi><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>K</mi><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q33. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>:</mo><msup><mn>8</mn><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></msup><mo>+</mo><msup><mn>8</mn><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></msup><mo>=</mo><mn>16</mn></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>S</mi></mfenced><mo>+</mo><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi></mrow></munder><mfenced><mrow><mi>sec</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>cosec</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></msup><mo>+</mo><msup><mn>8</mn><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></msup><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>8</mn><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></msup><mo>+</mo><msup><mn>8</mn><mrow><mn>2</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></msup><mo>=</mo><mn>16</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></msup><mo>=</mo><mi>y</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>+</mo><mfrac><mn>64</mn><mi>y</mi></mfrac><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>8</mn><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></msup><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>S</mi></mfenced><mo>+</mo><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi></mrow></munder><mfenced><mrow><mi>sec</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>cosec</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">n</mi><mfenced><mi mathvariant="normal">S</mi></mfenced><mo>+</mo><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi></mrow></munder><mfrac><mn>1</mn><mrow><mi>cos</mi><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle><mo>+</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mstyle><mo>+</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi></mrow></munder><mfrac><mn>2</mn><mrow><mn>2</mn><mi>cos</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>&#952;</mi></mstyle></mfenced><mi>sin</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>&#952;</mi></mstyle></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi></mrow></munder><mn>2</mn><mi>cos</mi><mtext>ec</mtext><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>4</mn><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mtext>ec</mtext><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced><mtext>+</mtext><mn>2</mn><mi>cos</mi><mtext>ec</mtext><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced><mtext>+</mtext><mn>2</mn><mi>cos</mi><mtext>ec</mtext><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced><mtext>+</mtext><mn>2</mn><mi>cos</mi><mtext>ec</mtext><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>7</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mn>2</mn><mfenced close="]" open="["><mrow><mo>-</mo><mi>cos</mi><mtext>ec</mtext><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mtext>ec</mtext><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mtext>ec</mtext><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mtext>ec</mtext><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#215;</mo><mn>4</mn><mo>=</mo><mo>-</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q34. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>sin</mi><mi>x</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><mi>&#960;</mi><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn><mi>&#960;</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<blockquote><p>The number of solutions will be the number of points of intersection of the graphs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>sin</mi><mi>x</mi></math></p><p>Plotting the two curves on the same axis, we get, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/59811bf7-4463-4c2a-91b5-85f4660f9c5d-image.png" style="width: 456px; height: 200px;" /></p><p>the number of intersection as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></p></blockquote>

</details>

---

### Q35. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mo>&#160;</mo><mi>x</mi></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn></mrow></mfenced></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><mfenced><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>5</mn></msqrt></mrow></mfenced><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><mfenced><mrow><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></mfrac></math></p><p>Now plotting the graph we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fb839449-bb1d-4fcf-8b19-c9bcdc42fb84-image.png" style="width: 415px; height: 130px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo></math>Now by graph number of solutions in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q36. JEE Main 2022 (29 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#952;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>=</mo><mn>0</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#952;</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>&#952;</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6323fce3-4237-419a-a9ef-36d49cf5b116-image.png" style="width: 300px; height: 178px;" /></p><p>As per the graph drawn there is only one point of intersection, so only one solution of the given equation.</p>

</details>

---

### Q37. JEE Main 2022 (29 Jun Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mn>4</mn><mi>&#960;</mi><mo>,</mo><mn>4</mn><mi>&#960;</mi></mrow></mfenced><mo>:</mo><mo>&#160;</mo><mn>3</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>+</mo><mn>6</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>10</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>+</mo><mn>6</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>10</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>+</mo><mn>6</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>5</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>5</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mfenced><mrow><mn>3</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mn>4</mn><mi>&#960;</mi><mo>,</mo><mn>4</mn><mi>&#960;</mi></mrow></mfenced><mo>&#8658;</mo><mn>2</mn><mi>&#952;</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mn>8</mn><mi>&#960;</mi><mo>,</mo><mn>8</mn><mi>&#960;</mi></mrow></mfenced></math></p><p>So for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mo>&#177;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mo>&#177;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#177;</mo><mn>15</mn><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> gives <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math> solution</p><p>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math> gives <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math> solution</p><p>hence, total elements in set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math></p>

</details>

---

### Q38. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>21</mn><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math> holds, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>21</mn><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>21</mn><mo>-</mo><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>17</mn><mo>+</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>-</mo><mn>6</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>17</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mi>p</mi></mfrac><mo>-</mo><mn>6</mn><mi>p</mi><mo>=</mo><mn>17</mn><mo>&#8658;</mo><mn>14</mn><mo>-</mo><mn>6</mn><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>17</mn><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mn>17</mn><mi>p</mi><mo>-</mo><mn>14</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mo>&#177;</mo><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3e0502d1-dc6c-4eb1-a809-776593d891fa-image.png" style="width: 220px; height: 250px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  There are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> solutions</p>

</details>

---

### Q39. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mi>cos</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mi>&#960;</mi><mo>,</mo><mn>3</mn><mi>&#960;</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>cos</mi><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>&#160;</mo></math>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>=</mo><mo>-</mo><mn>6</mn><mi>&#960;</mi><mo>,</mo><mo>-</mo><mn>4</mn><mi>&#960;</mi><mo>,</mo><mo>-</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mn>4</mn><mi>&#960;</mi><mo>,</mo><mn>6</mn><mi>&#960;</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>3</mn><mi>&#960;</mi><mo>,</mo><mo>-</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mo>-</mo><mi>&#960;</mi><mo>,</mo><mn>0</mn><mo>,</mo><mi>&#960;</mi><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mn>3</mn><mi>&#960;</mi></mrow></mfenced></math></p><p>So total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> solutions.</p>

</details>

---

### Q40. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mi>&#960;</mi><mo>,</mo><mi>&#960;</mi><mo>]</mo><mo>-</mo><mfenced close="}" open="{"><mrow><mo>&#177;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>:</mo><mi>sin</mi><mi>&#952;</mi><mi>tan</mi><mi>&#952;</mi><mo>+</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><munder><mo>&#8721;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>cos</mi><mn>2</mn><mi>&#952;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>+</mo><mi>n</mi><mfenced><mi>S</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi><mo>&#160;</mo><mi>tan</mi><mo>&#160;</mo><mi>&#952;</mi><mo>+</mo><mi>tan</mi><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mi>sin</mi><mo>&#160;</mo><mn>2</mn><mi>&#952;</mi><mo>;</mo><mo>&#160;</mo><mi>&#952;</mi><mo>&#8800;</mo><mo>&#177;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow><mrow><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow><mrow><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi></mrow><mrow><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">&#960;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mi mathvariant="normal">&#960;</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mi>&#960;</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi>&#952;</mi><mo>&#160;</mo><mo>+</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mi>&#960;</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#952;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mi>&#960;</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math> (rejected)</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced><mi>S</mi></mfenced><mo>=</mo><mn>5</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mi>&#931;</mi><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>cos</mi><mo>&#160;</mo><mn>0</mn><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>&#960;</mi><mo>+</mo><mi>cos</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>+</mo><mi>cos</mi><mfenced><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>4</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>+</mo><mi>n</mi><mfenced><mi>S</mi></mfenced><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q41. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>4</mn><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is the sum of all these solutions, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>,</mo><mi>S</mi></mrow></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mfrac><mrow><mn>8</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mfrac><mrow><mn>13</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>9</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mfrac><mrow><mn>13</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>9</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>4</mn><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mi>sin</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>2</mn><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mi>cos</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>2</mn><mo>.</mo><mfenced><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>cos</mi><mn>3</mn><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>3</mn><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></math></p><p>No. of solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p><p>Sum of solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>S</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>+</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>=</mo><mfrac><mrow><mn>13</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></math></p>

</details>

---

### Q42. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the sum of all solutions (in radians) of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>4</mn><mi>&#960;</mi><mo>]</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>8</mn><mi>S</mi></mrow><mi>&#960;</mi></mfrac></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **56**

**Detailed Solution:**

<p>Given that: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>4</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mo>&#8722;</mo><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><mi>cos</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><mn>0</mn><mo>&#8197;&#8197;</mo><mo>;</mo><mo>&#8197;&#8197;</mo><mrow><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>4</mn><mi>&#960;</mi><mo>]</mo></mrow></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mn>1</mn><mo>&#8722;</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mo>&#8722;</mo><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><mi>cos</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mn>2</mn><mo>&#8722;</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi><mo>&#8722;</mo><mi>sin</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi><mo>&#8722;</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>sin</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>;</mo><mn>2</mn><mi>&#952;</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mn>8</mn><mi>&#960;</mi><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>9</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>13</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Sum of the solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>S</mi><mo>=</mo><mfrac><mrow><mn>28</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>
Then value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">S</mi></mrow><mi>&#960;</mi></mfrac><mo>=</mo><mn>8</mn><mo>&#215;</mo><mfenced><mfrac><mrow><mn>28</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac></mfenced><mo>=</mo><mn>56</mn></math></p>

</details>

---

### Q43. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The sum of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced open="|" close="|"><mrow><mi>tan</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>10</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>30</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>15</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>30</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>30</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced close="|" open="|"><mrow><mi>tan</mi><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p>Case-<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo></math> When <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>tan</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mfenced><mrow><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> (Not possible, since <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>)</p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#177;</mo><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>5</mn></msqrt></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>10</mn></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>&#960;</mi></mrow><mn>10</mn></mfrac></math></p><p>Case-<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo></math> When <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>0</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mi>tan</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mi>cos</mi><mi>x</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mo>(</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mi>&#981;</mi></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math></p><p>Sum of solutions</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>10</mn></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>10</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>11</mn><mi>&#960;</mi></mrow><mn>30</mn></mfrac></math></p>

</details>

---

### Q44. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of distinct real roots of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>Apply: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mi>cos</mi><mi>x</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>tan</mi><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>Hence, number of roots is one.</p>

</details>

---

### Q45. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>]</mo></math>, for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mn>3</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mn>4</mn><mi>x</mi><mo>=</mo><mn>0</mn></math>, is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>&#960;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>&#960;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>&#960;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#960;</mi></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mn>3</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mn>4</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>4</mn><mi>x</mi><mo>)</mo><mo>+</mo><mo>(</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mn>3</mn><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>sin</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mi>cos</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>sin</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>sin</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mfenced open="{" close="}"><mrow><mi>cos</mi><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>sin</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mfenced close="}" open="{"><mrow><mn>2</mn><mi>cos</mi><mi>x</mi><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>sin</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#960;</mi><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mn>3</mn><mi>&#960;</mi><mo>,</mo><mn>4</mn><mi>&#960;</mi><mo>,</mo><mn>5</mn><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>6</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>8</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mn>2</mn><mi>&#960;</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>&#960;</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math></p><p>So sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mi>&#960;</mi><mo>+</mo><mi>&#960;</mi><mo>+</mo><mn>2</mn><mi>&#960;</mi><mo>=</mo><mn>9</mn><mi>&#960;</mi></math></p>

</details>

---

### Q46. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of solutions of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>7</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>7</mn></msup><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mi>&#960;</mi><mo>]</mo></math>  is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math></p><p>Also, we know for a number which lie between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo></math> higher the power of the number the less is its value.  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>7</mn></msup><mi>x</mi><mo>&#8804;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>7</mn></msup><mi>x</mi><mo>&#8804;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>&#8804;</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Also, we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>This means the equality must hold for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>7</mn></msup><mi>x</mi><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>7</mn></msup><mi>x</mi><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><msup><mi>sin</mi><mn>5</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><msup><mi>cos</mi><mn>5</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mn>1</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>.</mo></math></p><p>Thus, there are total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> solutions.</p>

</details>

---

### Q47. JEE Main 2021 (18 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>cot</mi><mi>x</mi><mo>|</mo><mo>=</mo><mi>cot</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#960;</mi><mo>]</mo></math> is<gwmw style="display:none;"></gwmw>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> (Not possible)</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>x</mi><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><mi>cot</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></math> (reject as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cot</mi><mi>x</mi><mo>&#60;</mo><mn>0</mn></math>)</p><p>So, number of solutions is one.</p>

</details>

---

### Q48. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd></mtr><mtr><mtd><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mfenced><mrow><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mi>&#960;</mi></mrow></mfenced><mo>,</mo></math> are

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>,</mo><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>,</mo><mfrac><mrow><mn>11</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd></mtr><mtr><mtd><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>use <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub><mo>+</mo><msub><mi>R</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>2</mn><mpadded lspace="-3px"><mi>x</mi></mpadded></mrow></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd></mtr><mtr><mtd><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>use <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>1</mn></msub><mo>-</mo><msub><mi>C</mi><mrow><mn>3</mn><mo>&#160;</mo></mrow></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><msub><mi>C</mi><mrow><mn>3</mn><mo>&#160;</mo></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>2</mn><mpadded lspace="-3px"><mi>x</mi></mpadded></mrow></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mi>sin</mi><mn>2</mn><mpadded lspace="-3px"><mi>x</mi></mpadded></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>=</mo><mi>&#960;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>,</mo><mi>&#960;</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p>

</details>

---

### Q49. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>tan</mi><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math> is<gwmw style="display:none;"></gwmw></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>tan</mi><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math><gwmw style="display:none;"></gwmw></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>tan</mi><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>The graph of the two functions is given as</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dc9c8849-d705-4da6-a308-ee6bf8a16e7e-image.png" style="width: 393px; height: 340px;" /></p><p>It is clear from the graph that the number of solutions of the given equation is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>3</mn><mo>.</mo></math></p>

</details>

---

### Q50. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>30</mn></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>+</mo><mfrac><msup><mfenced><mn>81</mn></mfenced><mn>1</mn></msup><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup></mfrac><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>+</mo><mfrac><mn>81</mn><mi>t</mi></mfrac><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>30</mn><mi>t</mi><mo>+</mo><mn>81</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>-</mo><mn>27</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><msup><mn>3</mn><mn>1</mn></msup></math> or  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>81</mn></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><msup><mn>3</mn><mn>1</mn></msup></math>  or   <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>  or  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4d74cd18-9d96-4d27-8234-8dbf50118c7c-image.png" style="width: 248px; height: 114px;" />  </p><p>Hence, total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> solution.</p>

</details>

---

### Q51. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mi>x</mi><mo>+</mo><mn>1</mn></math>, then number of solutions of the given equation when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><msup><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msqrt><mn>3</mn></msqrt><mi>cos</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>cos</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math> (reject)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math> only</p><p>Hence, only one solution.</p>

</details>

---

### Q52. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#60;</mo><mi>&#960;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>y</mi><mo>-</mo><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>y</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>y</mi><mo>-</mo><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mfenced open="[" close="]"><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>4</mn><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>2</mn><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>cos</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p>option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math></p>

</details>

---

### Q53. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>S</mi></math> be the set of all <math><mi>&#945;</mi><mtext>&#8201;</mtext><mo>&#8712;</mo><mtext>&#8201;</mtext><mi>R</mi></math> such that the equation, <math><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>7</mn></math> has a solution. Then <math><mi>S</mi></math> is equal to:

**Options:**

- **(A)** <math><mfenced open="[" close="]" separators="|"><mrow><mn>3</mn><mo>,</mo><mi> </mi><mn>7</mn></mrow></mfenced></math>
- **(B)** <math><mfenced open="[" close="]" separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mn>6</mn></mrow></mfenced></math>
- **(C)** <math><mfenced open="[" close="]" separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced></math>
- **(D)** R

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfenced open="[" close="]" separators="|"><mrow><mn>2</mn><mo>,</mo><mi> </mi><mn>6</mn></mrow></mfenced></math>**

**Detailed Solution:**

The given equation can be written as:  
<math><mn>1</mn><mo>-</mo><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="italic">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mi> </mi><mi>α</mi><mi> </mi><mi>s</mi><mi>i</mi><mi>n</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>α</mi><mo>-</mo><mn>7</mn></math>  
<math><mo>⇒</mo><mn>2</mn><mrow><mrow><msup><mrow><mi mathvariant="italic">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mi>α</mi><mrow><mrow><mi mathvariant="italic">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mn>2</mn><mi>α</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>  
<math><mo>⇒</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>α</mi><mo>-</mo><mn>4</mn><mi> </mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mi> </mi><mn>2</mn><mi> </mi><mfenced separators="|"><mrow><mi>s</mi><mi>i</mi><mi>n</mi><mi>x</mi><mi> </mi><mo>≠</mo><mn>2</mn></mrow></mfenced></math>  
For at least one solution 
<math><mo>-</mo><mn>1</mn><mo>≤</mo><mfrac><mrow><mi mathvariant="normal">α</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi mathvariant="normal"> </mi><mo>≤</mo><mn>1</mn></math>  
<math><mo>⇒</mo><mi mathvariant="normal">α</mi><mo>∈</mo><mo>[</mo><mn>2,6</mn><mo>]</mo></math>

</details>

---

### Q54. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>3</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math> is:

**Options:**

- **(A)** <math><mn>5</mn></math>
- **(B)** <math><mn>7</mn></math>
- **(C)** <math><mn>3</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>5</mn></math>**

**Detailed Solution:**

<p>The given trigonometric equation can be written as
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mn>2</mn></msup><mn>3</mn><mi>x</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>4</mn></msup><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>2</mn></msup><mn>3</mn><mi>x</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>4</mn></msup><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mi>&#160;</mi></math></p><p>In given interval <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> at <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mi>&#160;</mi><mo>-</mo><mi>&#960;</mi><mo>,</mo><mtext>&#8201;</mtext><mn>0</mn><mo>,</mo><mtext>&#8201;</mtext><mi>&#960;</mi><mo>,</mo><mi>&#160;</mi><mn>2</mn><mi>&#960;</mi></math> and these values are also satisfied by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>0</mn><mo>.</mo></math>
Hence total number of solutions is <math><mn>5</mn><mo>.</mo></math></p>

</details>

---

### Q55. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>:</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>.</mo></math> Then the sum of the elements of <math><mi>S</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>
- **(B)** <math><mfrac><mrow><mn>13</mn><mi>&#960;</mi></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mn>2</mn><mi>&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>2</mn><mi>&#960;</mi></math>**

**Detailed Solution:**

<p>The given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></math> can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>3</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mi>sin</mi><mi>&#952;</mi><mo>&#8800;</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Hence, solutions in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo><mi>&#160;</mi><mn>2</mn><mi>&#960;</mi></mrow></mfenced></math> are
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>&#960;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mi>&#160;</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mi>&#160;</mi><mn>2</mn><mi>&#960;</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p>Sum of the elements is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#960;</mi><mo>.</mo></math></p>

</details>

---

### Q56. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all values of <math><mi>&#160;</mi><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mi>&#960;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>&#952;</mi><mo>=</mo><mi>t</mi></mrow></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>&#952;</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></mrow></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>A</mi><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>A</mi><mo>-</mo><mn>1</mn><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mrow><mn>4</mn><mi>&#952;</mi><mo>=</mo><mn>0</mn></mrow></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>Z</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#952;</mi><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>8</mn></mfrac><mo>&#160;</mo><mo>&#8712;</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Hence, the sum of the values of <math><mi>&#952;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>8</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q57. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo></math> then the number of values of <math><mi>x</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> is:

**Options:**

- **(A)** <math><mn>4</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>3</mn><mi>x</mi><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#160;</mi><mi>x</mi><mi>&#160;</mi><mo>.</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn></math> or <math><mi>x</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math> or <math><mi>&#160;</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math><mo>&#8756;</mo></math> Number of solutions <math><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q58. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

Consider the following two statements.
Statement $\boldsymbol{p}$ :
The value of $\sin 120^{\circ}$ can be divided by taking $\theta=240^{\circ}$ in the equation
$$
2 \sin \frac{\theta}{2}=\sqrt{1+\sin \theta}-\sqrt{1-\sin \theta} .
$$
Statement $\boldsymbol{q}$ :
The angles $A, B, C$ and $D$ of any quadrilateral $A B C D$ satisfy the equation
$$
\cos \left(\frac{1}{2}(A+C)\right)+\cos \left(\frac{1}{2}(B+D)\right)=0
$$
Then the truth values of $p$ and $q$ are respectively.

**Options:**

- **(A)** $\mathrm{F}, \mathrm{T}$
- **(B)** $\mathrm{T}, \mathrm{T}$
- **(C)** F, F
- **(D)** T, F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{F}, \mathrm{T}$**

**Detailed Solution:**

Statement $p$ :
$$
\sin 120^{\circ}=\cos 30^{\circ}=\frac{\sqrt{3}}{2} \Rightarrow 2 \sin 120^{\circ}=\sqrt{3}
$$
So, $\sqrt{1+\sin 240^{\circ}}-\sqrt{1-\sin 240^{\circ}}=$
$$
\sqrt{\frac{1-\sqrt{3}}{2}}-\sqrt{\frac{1+\sqrt{3}}{2}} \neq \sqrt{3}
$$
Statement $\mathbf{q}$ :
So, $A+B+C+D=2 \pi$
$$
\begin{aligned}
&\Rightarrow \frac{A+C}{2}+\frac{B+D}{2}=\pi \\
&\Rightarrow \cos \left(\frac{A+C}{2}\right)+\cos \left(\frac{B+D}{2}\right) \\
&=\cos \left(\frac{A+C}{2}\right)-\cos \left(\frac{A+C}{2}\right)=0
\end{aligned}
$$
Therefore, statement $p$ is false and statement $q$ is true.

</details>

---

### Q59. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of $\sin 3 x=\cos 2 x$, in the interval $\left(\frac{\pi}{2}, \pi\right)$ is

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$\sin 3 x=\cos 2 x$
$$
\begin{aligned}
&\Rightarrow 3 \sin x-4 \sin ^3 x=1-2 \sin ^2 x \\
&\Rightarrow 4 \sin ^3 x-2 \sin ^2 x-3 \sin x+1=0 \\
&\Rightarrow \sin x=1, \frac{-2 \pm 2 \sqrt{5}}{8}
\end{aligned}
$$
In the interval $\left(\frac{\pi}{2}, \pi\right), \sin x=\frac{-2+2 \sqrt{5}}{8}$
So, there is only one solution.

</details>

---

### Q60. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan A$ and $\tan B$ are the roots of the quadratic equation, $3 x^2-10 x-25=0$ then the value of $3 \sin ^2(A+B)-10 \sin (A+B) \cdot \cos (A+B)-25 \cos ^2$ $(A+B)$ is

**Options:**

- **(A)** 25
- **(B)** $-25$
- **(C)** $-10$
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-25$**

**Detailed Solution:**

As $\tan A$ and $\tan B$ are the roots of $3 x^2-10 x-25=0$
So, $\tan (A+B)=\frac{\tan A+\tan B}{1-\tan A \tan B}=\frac{\frac{10}{3}}{1+\frac{25}{3}}$ $=\frac{10 / 3}{28 / 3}=\frac{5}{14}$
Now, $\cos ^2(A+B)=-1+2 \cos ^2(A+B)$
$=\frac{1-\tan ^2(A+B)}{1+\tan ^2(A+B)} \Rightarrow \cos ^2(A+B)=\frac{196}{221}$
$\therefore 3 \sin ^2(A+B)-10 \sin (A+B)$
$=\cos ^2(A+B)\left[3 \tan ^2(A+B)-10 \tan (A+B)-25\right]$
$=\frac{75-700-4900}{196} \times \frac{196}{221}=-\frac{5525}{196} \times \frac{196}{221}=-25$

</details>

---

### Q61. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If sum of all the solutions of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>cos</mi><mi>x</mi><mo>&#183;</mo><mfenced separators="|"><mrow><mi>cos</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi></mrow></mfenced></math> is <math><mi>k</mi><mi>&#960;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>20</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mi> </mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>cos</mi><mi>x</mi><mo>.</mo><mfenced separators="|"><mrow><mi>cos</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>.</mo><mi>cos</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p>We would use the formula</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>.</mo><mi>cos</mi><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mi>B</mi></mrow></mfenced><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>A</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>B</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced><mo>.</mo><mi>cos</mi><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>cos</mi><mi>x</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>cos</mi><mi>x</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>cos</mi><mi>x</mi><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mi>cos</mi><mi>x</mi><mfenced separators="|"><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mn>6</mn><mi>cos</mi><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced separators="|"><mrow><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>cos</mi><mn>3</mn><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mn>3</mn><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>General Solution <math><mn>3</mn><mi>x</mi><mo>=</mo><mn>2</mn><mi>n</mi><mi>&#960;</mi><mo>&#177;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math></p><p><math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>n</mi><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>&#177;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>9</mn></mfrac><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Sum</mi><mo>=</mo><mfrac><mrow><mn>13</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>,</mo><mi>&#160;</mi><mi>k</mi><mo>=</mo><mfrac><mn>13</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q62. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mi>&#952;</mi><mo>:</mo><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mi>&#952;</mi><mo>:</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>,</mo></math> be two sets. Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8834;</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>-</mo><mi>P</mi><mi>&#160;</mi><mo>&#8800;</mo><mi>&#160;</mi><mi>&#981;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>&#8836;</mo><mi>P</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>Q</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8836;</mo><mi>Q</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>Q</mi></math>**

**Detailed Solution:**

<p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>:</mo><mo>&#160;</mo><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>&#952;</mi></math></strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></math></p><p><strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>:</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>&#952;</mi><mo>&#8658;</mo><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mi>cos</mi><mi>&#952;</mi><mi>&#160;</mi><mi>&#160;</mi></math></strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mi>&#160;</mi><mfrac><mn>1</mn><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></math></p>

</details>

---

### Q63. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mn>0</mn><mi>&#160;</mi><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn><mi>&#960;</mi><mo>,</mo></math> then the number of real values of <math><mi>x</mi><mo>,</mo></math> which satisfy the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mn>3</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mn>4</mn><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mn>3</mn><mi>x</mi><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mi>x</mi><mfenced separators="|"><mrow><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>cos</mi><mi>x</mi><mn>2</mn><mi>cos</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi><mo>,</mo><mfrac><mi>&#960;</mi><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac><mo>,</mo><mfrac><mrow><mn>9</mn><mi>&#960;</mi></mrow><mn>5</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#160;</mo></math>Solutions.

</details>

---

### Q64. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#945;</mi><mo>+</mo><mi>cos</mi><mi>&#946;</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>&#160;</mi><mtext>and</mtext><mi>&#160;</mi><mi>sin</mi><mi>&#945;</mi><mo>+</mo><mi>sin</mi><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#160;</mi></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is the arithmetic mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#160;</mi><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

Given 
<mo><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mo>&#160;</mo><mi>&#945;</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>&#946;</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></mo>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mi>&#945;</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>&#946;</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
<math><mo>&#8658;</mo><mn>2</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mo>(</mo><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>)</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mo>(</mo><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>)</mo><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> ......(i) and

<math><mn>2</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mo>(</mo><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>)</mo></mrow></mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mo>&#8289;</mo><mo>(</mo><mfrac><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>)=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> ....(ii)

Dividing (ii) and (i)

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#160;</mo><mfenced><mfrac><mfenced><mrow><mi>&#945;</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></mfrac></mfenced></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi><mi>&#160;</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mrow></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi mathvariant="normal">&#952;</mi><mo>+</mo><mi>cos</mi><mo>&#8289;</mo><mn>2</mn><mi mathvariant="normal">&#952;</mi><mi>&#160;</mi><mo>=</mo></math> <math><mfrac><mrow><mn>2</mn><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow></mfrac><mo>+</mo><mi>&#160;</mi><mfrac><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfrac></math>

<math><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>10</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

</details>

---

### Q65. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $2 \cos \theta+\sin \theta=1\left(\theta \neq \frac{\pi}{2}\right)$, then $7 \cos \theta+6 \sin \theta$ is equal to:

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 2
- **(C)** $\frac{11}{2}$
- **(D)** $\frac{46}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{46}{5}$**

**Detailed Solution:**

Given $2 \cos \theta+\sin \theta=1$
Squaring both sides, we get
$$
\begin{aligned}
&(2 \cos \theta+\sin \theta)^2=1^2 \\
&\Rightarrow 4 \cos ^2 \theta+\sin ^2 \theta+4 \sin \theta \cos \theta=1 \\
&\Rightarrow 3 \cos ^2 \theta+\left(\cos ^2 \theta+\sin ^2 \theta\right)+4 \sin \theta \cos \theta \\
&=1 \\
&\Rightarrow 3 \cos ^2 \theta+\not \lambda+4 \sin \theta \cos \theta=1 \\
&\Rightarrow 3 \cos ^2 \theta+4 \sin \theta \cos \theta=0 \\
&\Rightarrow \cos \theta(3 \cos \theta+4 \sin \theta)=0 \\
&\Rightarrow 3 \cos \theta+4 \sin \theta=0 \\
&\Rightarrow 3 \cos \theta=-4 \sin \theta \\
&\Rightarrow \frac{-3}{4}=\tan \theta=\sqrt{\sec ^2 \theta-1}=\frac{-3}{4} \\
&\left(\because \tan ^2 \theta=\sqrt{\sec ^2 \theta-1}\right) \\
&\Rightarrow \sec ^2 \theta-1=\left(\frac{-3}{4}\right)^2=\frac{9}{16} \\
&\Rightarrow \sec 2 \theta=\frac{9}{16}+1=\frac{25}{16} \Rightarrow \sec \theta=\frac{5}{4}
\end{aligned}
$$
or $\cos \theta=\frac{4}{5}$
Now, $\sin ^2 \theta+\cos ^2 \theta=1$
$$
\begin{aligned}
&\Rightarrow \sin ^2 \theta+\left(\frac{4}{5}\right)^2=1 \\
&\sin ^2 \theta+\frac{4}{5}=1 \Rightarrow \sin ^2 \theta=1-\frac{16}{25}=\frac{9}{25} \\
&\sin \theta=\pm \frac{3}{5}
\end{aligned}
$$
Taking $\quad\left(\sin \theta=+\frac{3}{5}\right) \quad$ because $\left(\sin \theta=-\frac{3}{5}\right)$ cannot satisfy the given equation.
Therefore; $7 \cos \theta+6 \sin \theta$
$$
=7 \times \frac{4}{5}+6 \times \frac{3}{5}=\frac{28}{5}+\frac{18}{5}=\frac{46}{5}
$$

</details>

---

### Q66. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

<p>The number of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#945;</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mn>3</mn></msup><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>7</mn><msup><mi>sin</mi><mn>2</mn></msup><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>7</mn><mi>sin&#945;</mi><mo>=</mo><mn>2</mn></math>, is :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>sin</mi><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>7</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>7</mn><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>=</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><msup><mi>sin</mi><mn>3</mn></msup><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>7</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>&#160;</mo><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced open="[" close="]"><mrow><mn>2</mn><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>+</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>7</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><msup><mi>a</mi><mn>3</mn></msup><mo>-</mo><msup><mi>b</mi><mn>3</mn></msup><mo>=</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>&#160;</mo><msup><mi>sin</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>5</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>=1,</mo><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>&#8800;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>&#8757;</mo><mi>sinx</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> 
Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>=1&#160;&#8658;&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mi mathvariant="normal">0</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;&#8658;&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mo>&#160;&#160;</mo><mfrac><mrow><mn>5</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>6</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi mathvariant="normal">&#945;</mi><mo>&#160;</mo><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mi mathvariant="normal">0</mi><mo>,</mo><mo>&#160;&#160;</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfenced></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> values of <math> <mrow> <mi>&#945;</mi> </mrow> </math> in <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mn>0</mn> <mtext>,&#160;</mtext> <mn>2</mn> <mi>&#960;</mi> </mrow> </mfenced> </mrow> </math>.</p>

</details>

---

### Q67. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{A}=\{\theta: \sin (\theta)=\tan (\theta)\}$ and $\mathrm{B}=(\theta: \cos (\theta)=$ 1\} be two sets. Then:

**Options:**

- **(A)** $\mathrm{A}=\mathrm{B}$
- **(B)** $A \not \subset B$
- **(C)** $B \not \subset A$
- **(D)** $A \subset B$ and $B-A \neq \phi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $A \not \subset B$**

**Detailed Solution:**

Let $\mathrm{A}=\{\theta: \sin \theta=\tan \theta\}$ and $\mathrm{B}=\{\theta: \cos \theta=1\}$
Now, $A=\left\{\theta: \sin \theta=\frac{\sin \theta}{\cos \theta}\right\}$ $=\{\theta: \sin \theta(\cos \theta-1)=0\}$ $=\{\theta=0, \pi, 2 \pi, 3 \pi, \ldots \ldots\}$
For $\mathrm{B}: \cos \theta=1 \Rightarrow \theta=\pi, 2 \pi, 4 \pi, \ldots \ldots$
This shows that $\mathrm{A}$ is not contained in B. i.e. $\mathrm{A} \not \subset \mathrm{B}$. but $\mathrm{B} \subset \mathrm{A}$.

</details>

---

### Q68. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The number of solutions of the equation $\sin 2 x-2 \cos x+4 \sin x=4$ in the interval $[0,5 \pi]$ is :

**Options:**

- **(A)** 3
- **(B)** 5
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

$$
\text { } \begin{aligned}
& \sin 2 x-2 \cos x+4 \sin x=4 \\
& \Rightarrow 2 \sin x \cdot \cos x-2 \cos x+4 \sin x-4=0 \\
& \Rightarrow(\sin x-1)(\cos x-2)=0
\end{aligned}
$$

$$
\begin{aligned}
& \because \cos x-2 \neq 0, \therefore \sin x=1 \\
& \therefore \quad x=\frac{\pi}{2}, \frac{5 \pi}{2}, \frac{9 \pi}{2}
\end{aligned}
$$

</details>

---

### Q69. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Statement-1: The number of common solutions of the trigonometric equations $2 \sin ^2 \theta$ $-\cos 2 \theta=0$ and $2 \cos ^2 \theta-3 \sin \theta=0$ in the interval $[0,2 \pi]$ is two.
Statement-2: The number of solutions of the equation, $2 \cos ^2 \theta-3 \sin \theta=0$ in the interval $[0, \pi]$ is two.

**Options:**

- **(A)** Statement-1 is true; Statement-2 is true; Statement-2 is a correct explanation for statement-1.
- **(B)** Statement-1 is true; Statement-2 is true; Statement-2 is not a correct explanation for statement-1.
- **(C)** Statement-1 is false; Statement-2 is true.
- **(D)** Statement-1 is true; Statement-2 is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement-1 is true; Statement-2 is true; Statement-2 is not a correct explanation for statement-1.**

**Detailed Solution:**

$2 \sin ^2 \theta-\cos 2 \theta=0$
$\Rightarrow 2 \sin ^2 \theta-\left(1-2 \sin ^2 \theta\right)=0$
$\Rightarrow 2 \sin ^2 \theta-1+2 \sin ^2 \theta=0$
$\Rightarrow 4 \sin ^2 \theta=1 \Rightarrow \sin \theta=\pm \frac{1}{2}$
$\therefore \theta=\frac{\pi}{4}, \frac{3 \pi}{4}, \frac{5 \pi}{4}, \frac{7 \pi}{4}, \theta \in[0,2 \pi]$
$\therefore \theta=\frac{\pi}{6}, \frac{5 \pi}{6}, \frac{7 \pi}{6}, \frac{11 \pi}{6}$
$$
\begin{aligned}
& \text { Now } 2 \cos ^2 \theta-3 \sin \theta=0 \\
\Rightarrow & 2\left(1-\sin ^2 \theta\right)-3 \sin \theta=0 \\
\Rightarrow & -2 \sin ^2 \theta-3 \sin \theta+2=0 \\
\Rightarrow & -2 \sin ^2 \theta-4 \sin \theta+\sin \theta+2=0 \\
\Rightarrow & 2 \sin ^2 \theta-\sin \theta+4 \sin \theta-2=0 \\
\Rightarrow & \sin \theta(2 \sin \theta-1)+2(2 \sin \theta-1)=0 \\
\Rightarrow & \sin \theta=\frac{1}{2},-2
\end{aligned}
$$
But $\sin \theta=-2$, is not possible
$$
\therefore \quad \sin \theta=\frac{1}{2}, \Rightarrow \theta=\frac{\pi}{6}, \frac{5 \pi}{6}
$$
Hence, there are two common solution, there each of the statement-1 and 2 are true but statement- 2 is not a correct explanation for statement-1.

</details>

---

### Q70. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of the equation, $\sin ^{-1} x=2 \tan ^{-1} x$ (in principal values) is :

**Options:**

- **(A)** 1
- **(B)** 4
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Given equation is
$$
\sin ^{-1} x=2 \tan ^{-1} x
$$
Now, this equation has only one solution.
$$
\begin{aligned}
& \therefore \quad \text { LHS }=\sin ^{-1} 1=\frac{\pi}{2} \\
& \text { and } \text { RHS }=2 \tan ^{-1} 1=2 \times \frac{\pi}{4}=\frac{\pi}{2}
\end{aligned}
$$
Also, $x=1$ gives angle value as $\frac{\pi}{4}$ and $\frac{5 \pi}{4}$ $\frac{5 \pi}{4}$ is outside the principal value.

</details>

---

### Q71. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A value of $x$ for which $\sin \left(\cot ^{-1}(1+x)\right)=\cos$ $\left(\tan ^{-1} x\right)$, is :

**Options:**

- **(A)** $-\frac{1}{2}$
- **(B)** 1
- **(C)** 0
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{1}{2}$**

**Detailed Solution:**

$\sin \left(\cot ^{-1}(1+x)\right)=\cos \left(\tan ^{-1} x\right)$
$\begin{aligned} & \Rightarrow \operatorname{cosec}^2\left(\cot ^{-1}(1+x)\right)=\sec ^2\left(\tan ^{-1} x\right) \\ & \Rightarrow 1+\left[\cot \left(\cot ^{-1}(1+x)\right)\right]^2 \\ & \Rightarrow=1+\left[\sec \left(\tan ^{-1} x\right)\right]^2 \\ & \Rightarrow(1+x)^2=x^2 \Rightarrow x=-\frac{1}{2}\end{aligned}$

</details>

---

### Q72. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `3`

The equation $e^{\sin x}-e^{-\sin x}-4=0$ has

**Options:**

- **(A)** infinite number of real roots
- **(B)** no real roots
- **(C)** exactly one real root
- **(D)** exactly four real roots

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) no real roots**

**Detailed Solution:**

$e^{\sin x}-e^{-\sin x}=4 \quad \Rightarrow e^{\sin x}=t$
$t-\frac{1}{t}=4$
$\begin{array}{ll}t^2-4 t-1=0 & \Rightarrow t=\frac{4 \pm \sqrt{16+4}}{2} \\ \Rightarrow t=\frac{4 \pm 2 \sqrt{5}}{2} & \Rightarrow t=2 \pm \sqrt{5}\end{array}$
$e^{\sin x}=2 \pm \sqrt{5} \quad \quad-1 \leq \sin x \leq 1 \quad \quad \frac{1}{e} \leq e^{\sin x} \leq e$
$e^{\sin x}=2+\sqrt{5}$ not possible 
$e^{\sin x}=2-\sqrt{5}$ not possible
$\therefore$ hence no solution

</details>

---

### Q73. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

If $0 < x < \pi$ and $\cos x+\sin x=\frac{1}{2}$, then $\tan x$ is

**Options:**

- **(A)** $\frac{(1-\sqrt{7})}{4}$
- **(B)** $\frac{(4-\sqrt{7})}{3}$
- **(C)** $-\frac{(4+\sqrt{7})}{3}$
- **(D)** $\frac{(1+\sqrt{7})}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{(4+\sqrt{7})}{3}$**

**Detailed Solution:**

$\cos x+\sin x=\frac{1}{2} \Rightarrow 1+\sin 2 x=\frac{1}{4} \Rightarrow \sin 2 x=-\frac{3}{4}$, so $x$ is obtuse and $\frac{2 \tan x}{1+\tan ^2 x}=-\frac{3}{4} \Rightarrow 3 \tan ^2 x+8 \tan x+3=0$
$\therefore \tan x=\frac{-8 \pm \sqrt{64-36}}{6}=\frac{-4 \pm \sqrt{7}}{3}$
$\because \tan x < 0 \quad \therefore \tan x=\frac{-4-\sqrt{7}}{3}$

</details>

---

### Q74. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

The number of values of $x$ in the interval $[0,3 \pi]$ satisfying the equation $2 \sin ^2 x+5 \sin x-3=0$ is

**Options:**

- **(A)** 4
- **(B)** 6
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 4**

**Detailed Solution:**

<p><strong>Solving $2\sin^2x + 5\sin x - 3 = 0$</strong></p><p>The equation is quadratic in $\sin x$. Substitute $y = \sin x$, yielding $2y^2 + 5y - 3 = 0$.</p><p>Factoring gives $(2y - 1)(y + 3) = 0$. Solutions are $y = \frac{1}{2}$ and $y = -3$.</p><p>Since the range of sine is $[-1, 1]$, $\sin x = -3$ has no solution.</p><p>For $\sin x = \frac{1}{2}$, the general solution is $x = n\pi + (-1)^n\frac{\pi}{6}$, where $n \in \mathbb{Z}$.</p><p>Within $[0, 3\pi]$, valid values occur for $n = 0, 1, 2, 3$, giving $x = \frac{\pi}{6}, \frac{5\pi}{6}, \frac{13\pi}{6}, \frac{17\pi}{6}$.</p><p>Thus, there are exactly four solutions.</p><p>$\boxed{4}$</p>

</details>

---

### Q75. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

The number of solution of $\tan x+\sec x=2 \cos x$ in $[0,2 \pi)$ is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 0
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

The given equation is $\tan x+\sec x=2 \cos x \Rightarrow \sin x+1=2 \cos ^2 x$
$$
\begin{aligned}
& \Rightarrow \sin x+1=2\left(1-\sin ^2 x\right) \Rightarrow 2 \sin ^2 x+\sin x-1=0 \\
& \Rightarrow(2 \sin x-1)(\sin x+1)=0 \Rightarrow \sin x=\frac{1}{2},-1 \Rightarrow x=30^{\circ}, 150^{\circ}, 270^{\circ}
\end{aligned}
$$

</details>

---

