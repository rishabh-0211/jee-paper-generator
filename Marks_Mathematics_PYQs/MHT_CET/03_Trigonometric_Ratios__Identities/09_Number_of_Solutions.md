# MHT CET Mathematics - Trigonometric Ratios & Identities

## Topic 9: Number of Solutions

**Total Questions:** 9

---

### Q1. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions of $\tan x+\sec x=2 \cos x$ in $[0,2 \pi]$ is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 0
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

The given equation is $\tan x + \sec x = 2 \cos x$.

Rewriting in terms of sine and cosine, we get:

$\dfrac{\sin x}{\cos x} + \dfrac{1}{\cos x} = 2 \cos x$

For the equation to be defined, $\cos x \neq 0$. Multiplying both sides by $\cos x$, we get:

$\sin x + 1 = 2 \cos^2 x$

Using the identity $\cos^2 x = 1 - \sin^2 x$:

$\sin x + 1 = 2(1 - \sin^2 x)$

$\Rightarrow 2 \sin^2 x + \sin x - 1 = 0$

$\Rightarrow (2 \sin x - 1)(\sin x + 1) = 0$

This gives $\sin x = \dfrac{1}{2}$ or $\sin x = -1$.

For $\sin x = \dfrac{1}{2}$, the solutions in $[0, 2\pi]$ are $x = \dfrac{\pi}{6}$ and $x = \dfrac{5\pi}{6}$. For both values, $\cos x \neq 0$, so they are valid solutions.

For $\sin x = -1$, the solution in $[0, 2\pi]$ is $x = \dfrac{3\pi}{2}$. However, at $x = \dfrac{3\pi}{2}$, $\cos x = 0$, which makes $\tan x$ and $\sec x$ undefined. Thus, this solution is rejected.

Therefore, there are exactly $2$ valid solutions.

Answer: 2

</details>

---

### Q2. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions, of $2^{1+|\cos x|+|\cos x|^2+\ldots \ldots \ldots \cdots}=4$ in $(-\pi, \pi)$, is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

The given equation is $2^{1+|\cos x|+|\cos x|^2+\ldots} = 4$.

The exponent is an infinite geometric progression with first term $a=1$ and common ratio $r=|\cos x|$. For the sum to be finite, we must have $|\cos x| < 1$.

The sum of the infinite geometric progression is $S = \dfrac{1}{1 - |\cos x|}$.

Substituting this into the equation gives $2^{\dfrac{1}{1 - |\cos x|}} = 2^2$.

Equating the exponents, we get $\dfrac{1}{1 - |\cos x|} = 2$.

$1 - |\cos x| = \dfrac{1}{2}$

$|\cos x| = \dfrac{1}{2}$

This gives $\cos x = \dfrac{1}{2}$ or $\cos x = -\dfrac{1}{2}$.

In the interval $(-\pi, \pi)$, the solutions for $\cos x = \dfrac{1}{2}$ are $x = \dfrac{\pi}{3}, -\dfrac{\pi}{3}$.

The solutions for $\cos x = -\dfrac{1}{2}$ are $x = \dfrac{2\pi}{3}, -\dfrac{2\pi}{3}$.

Thus, there are $4$ solutions in the given interval.

Answer: 4

</details>

---

### Q3. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In $(0,2 \pi)$, the number of solutions of $\tan \theta+\sec \theta=2 \cos \theta$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

The given equation is $\tan \theta + \sec \theta = 2 \cos \theta$.

Rewriting in terms of sine and cosine:

$\dfrac{\sin \theta}{\cos \theta} + \dfrac{1}{\cos \theta} = 2 \cos \theta$

For the equation to be defined, $\cos \theta \neq 0$, which implies $\theta \neq \dfrac{\pi}{2}, \dfrac{3\pi}{2}$.

Multiplying both sides by $\cos \theta$:

$\sin \theta + 1 = 2 \cos^2 \theta$

Using the identity $\cos^2 \theta = 1 - \sin^2 \theta$:

$\sin \theta + 1 = 2(1 - \sin^2 \theta)$

$2 \sin^2 \theta + \sin \theta - 1 = 0$

Factorizing the quadratic equation:

$(2 \sin \theta - 1)(\sin \theta + 1) = 0$

This gives $\sin \theta = \dfrac{1}{2}$ or $\sin \theta = -1$.

If $\sin \theta = -1$, then $\theta = \dfrac{3\pi}{2}$, which is rejected since $\cos \theta \neq 0$.

If $\sin \theta = \dfrac{1}{2}$, the solutions in the interval $(0, 2\pi)$ are $\theta = \dfrac{\pi}{6}$ and $\theta = \dfrac{5\pi}{6}$.

Thus, there are exactly $2$ solutions.

Answer: 2

</details>

---

### Q4. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{S}=\left\{x \in(-\pi, \pi) \mid x \neq 0, \pm \dfrac{\pi}{2}\right\}$. The sum of all distinct solutions of the equation $\sqrt{3} \sec x+\operatorname{cosec} x+2(\tan x-\cot x)=0$ in the set S is equal to

**Options:**

- **(A)** $-\dfrac{7 \pi}{9}$
- **(B)** $-\dfrac{2 \pi}{9}$
- **(C)** 0
- **(D)** $\dfrac{5 \pi}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

The given equation is:

$\sqrt{3} \sec x + \operatorname{cosec} x + 2(\tan x - \cot x) = 0$

Converting the terms to sine and cosine:

$\dfrac{\sqrt{3}}{\cos x} + \dfrac{1}{\sin x} + 2\left(\dfrac{\sin x}{\cos x} - \dfrac{\cos x}{\sin x}\right) = 0$

Multiplying the entire equation by $\sin x \cos x$ (which is non-zero for $x \in S$):

$\sqrt{3} \sin x + \cos x + 2(\sin^2 x - \cos^2 x) = 0$

Using the double angle identity $\cos 2x = \cos^2 x - \sin^2 x$:

$\sqrt{3} \sin x + \cos x - 2 \cos 2x = 0$

$\sqrt{3} \sin x + \cos x = 2 \cos 2x$

Dividing both sides by 2:

$\dfrac{\sqrt{3}}{2} \sin x + \dfrac{1}{2} \cos x = \cos 2x$

$\cos x \cos \dfrac{\pi}{3} + \sin x \sin \dfrac{\pi}{3} = \cos 2x$

$\cos\left(x - \dfrac{\pi}{3}\right) = \cos 2x$

The general solution is given by:

$2x = 2n\pi \pm \left(x - \dfrac{\pi}{3}\right)$, where $n \in \mathbb{Z}$

Taking the positive sign:

$2x = 2n\pi + x - \dfrac{\pi}{3}$

$x = 2n\pi - \dfrac{\pi}{3}$

For $x \in (-\pi, \pi)$, the only valid solution is for $n = 0$:

$x_1 = -\dfrac{\pi}{3}$

Taking the negative sign:

$2x = 2n\pi - x + \dfrac{\pi}{3}$

$3x = 2n\pi + \dfrac{\pi}{3}$

$x = \dfrac{2n\pi}{3} + \dfrac{\pi}{9}$

For $x \in (-\pi, \pi)$, the valid solutions are:

For $n = 0$, $x_2 = \dfrac{\pi}{9}$

For $n = 1$, $x_3 = \dfrac{2\pi}{3} + \dfrac{\pi}{9} = \dfrac{7\pi}{9}$

For $n = -1$, $x_4 = -\dfrac{2\pi}{3} + \dfrac{\pi}{9} = -\dfrac{5\pi}{9}$

All these solutions are distinct and belong to the set $S$ since none of them are $0$ or $\pm \dfrac{\pi}{2}$.

The sum of all distinct solutions is:

$x_1 + x_2 + x_3 + x_4 = -\dfrac{\pi}{3} + \dfrac{\pi}{9} + \dfrac{7\pi}{9} - \dfrac{5\pi}{9}$

$= \dfrac{-3\pi + \pi + 7\pi - 5\pi}{9} = 0$

Answer: 0

</details>

---

### Q5. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The principal solutions, of the equation $\sqrt{3} \sec x+2=0$, are

**Options:**

- **(A)** $\dfrac{2 \pi}{3}, \dfrac{4 \pi}{3}$
- **(B)** $\dfrac{4 \pi}{3}, \dfrac{5 \pi}{3}$
- **(C)** $\dfrac{5 \pi}{6}, \dfrac{7 \pi}{6}$
- **(D)** $\dfrac{7 \pi}{6}, \dfrac{11 \pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{5 \pi}{6}, \dfrac{7 \pi}{6}$**

**Detailed Solution:**

Given equation is $\sqrt{3} \sec x + 2 = 0$

$\Rightarrow \sec x = -\dfrac{2}{\sqrt{3}}$

$\Rightarrow \cos x = -\dfrac{\sqrt{3}}{2}$

Since $\cos x$ is negative, $x$ lies in the second or third quadrant.

We know that $\cos \left( \dfrac{\pi}{6} \right) = \dfrac{\sqrt{3}}{2}$

In the second quadrant, $x = \pi - \dfrac{\pi}{6} = \dfrac{5\pi}{6}$

In the third quadrant, $x = \pi + \dfrac{\pi}{6} = \dfrac{7\pi}{6}$

The principal solutions are $\dfrac{5\pi}{6}$ and $\dfrac{7\pi}{6}$.

Answer: $\dfrac{5 \pi}{6}, \dfrac{7 \pi}{6}$

</details>

---

### Q6. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of solutions in $[0,2 \pi]$ of the equation $16^{\sin ^2 x}+16^{\cos ^2 x}=10$ is

**Options:**

- **(A)** 2
- **(B)** 4
- **(C)** 6
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8**

**Detailed Solution:**

$\begin{aligned} & 16^{\sin ^2 x}+16^{\cos ^2 x}=10 \\ & 16^{\sin ^2 x}+16^{1-\sin ^2 x}=10 \\ & 16^{\sin ^2 x}+\frac{16}{16^{\sin ^2 x}}=10\end{aligned}$
Let $16^{\sin ^2 x}=\mathrm{t}$
$\begin{array}{ll}
\therefore & \mathrm{t}+\frac{16}{\mathrm{t}}=10 \\
\therefore & \mathrm{t}^2-10 \mathrm{t}+16=0 \\
& \Rightarrow \mathrm{t}=2 \text { and } \mathrm{t}=8
\end{array}$
Now, $16^{\sin ^2 x}=2$ and $16^{\sin ^2 x}=8$
$\begin{aligned}
& 2^{4 \sin ^2 x}=2^1 \text { and } 2^{4 \sin ^2 x}=2^3 \\
\therefore \quad & 4 \sin ^2 x=1 \text { and } 4 \sin ^2 x=3 \\
\therefore \quad & \sin ^2 x=\frac{1}{4} \text { and } \sin ^2 x=\frac{3}{4} \\
& \sin x= \pm \frac{1}{2} \text { and } \sin x= \pm \frac{\sqrt{3}}{2} \\
\therefore \quad & x=\frac{\pi}{6}, \frac{5 \pi}{6}, \frac{7 \pi}{6}, \frac{11 \pi}{6} \text { and } x=\frac{\pi}{3}, \frac{2 \pi}{3}, \frac{4 \pi}{3}, \frac{5 \pi}{3}
\end{aligned}$
$\therefore \quad$ number of solutions $=8$.

</details>

---

### Q7. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of values of $\mathrm{x}$ in the interval $[0,3 \pi]$ satisfying $2 \sin ^2 x+5 \sin ^2 x-3=0$ is

**Options:**

- **(A)** 1
- **(B)** 6
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

$\begin{aligned} & 2 \sin ^2 x+5 \sin x-3=0 \\ & \Rightarrow(\sin x+3)(2 \sin x-1)=0 \\ & \Rightarrow \sin x=-3 \text { or } \sin x=\frac{1}{2} \\ & \Rightarrow \text { no solution or } \sin x=\sin \frac{\pi}{6} \\ & \Rightarrow x=n \pi+(-1) n \frac{\pi}{6}\end{aligned}$
But $x \in[0,3 \pi]$
$$
\Rightarrow x=\frac{\pi}{6}, \frac{5 \pi}{6}, \frac{13 \pi}{6}, \frac{17 \pi}{6}
$$
four solution

</details>

---

### Q8. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of $\tan 3 x=1$ is

**Options:**

- **(A)** $x=n \pi, n \in Z$
- **(B)** $x=n\left(\frac{\pi}{3}\right)+\frac{\pi}{12}, n \in Z$
- **(C)** $x=n \pi+\frac{\pi}{4}, n \in Z$
- **(D)** $x=n \pi \pm \frac{\pi}{4}, n \in Z$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x=n\left(\frac{\pi}{3}\right)+\frac{\pi}{12}, n \in Z$**

**Detailed Solution:**

We know that $\tan \theta=\tan \alpha$ implies
$\theta=n \pi+\alpha$, where $n \in Z$
Given $\tan 3 x=1$
$\therefore \tan 3 x=\tan \frac{\pi}{4} \Rightarrow 3 x=n \pi+\frac{\pi}{4}$
$\therefore \quad \mathrm{x}=\frac{\mathrm{n} \pi}{3}+\frac{\pi}{12}, \quad \mathrm{n} \in Z$

</details>

---

### Q9. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\cos 2 \theta=\sin \propto, \quad$ then $\theta=$

**Options:**

- **(A)** $2 n \pi \pm\left(\frac{\pi}{2}-\alpha\right), n \in z$
- **(B)** $n \pi \pm\left(\frac{\pi}{4}+\frac{\alpha}{2}\right), n \in z$
- **(C)** $\frac{1}{2}\left[n \pi+(-1)^{n} \propto\right], n \in z$
- **(D)** $n \pi \pm\left(\frac{\pi}{4}-\frac{\alpha}{2}\right), n \in z$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $n \pi \pm\left(\frac{\pi}{4}-\frac{\alpha}{2}\right), n \in z$**

**Detailed Solution:**

We have $\cos 2 \theta=\sin \alpha \Rightarrow \cos 2 \theta=\cos (90-\alpha)$ When $\cos \theta=\cos \alpha$, we get $\theta=2 n \pi \pm \alpha, n \in Z$ $\therefore \quad 2 \theta=2 \mathrm{n} \pi \pm(90-\alpha)$
$\theta=\frac{2 n \pi}{2} \pm\left(\frac{90-\alpha}{2}\right) \Rightarrow \theta=n \pi \pm\left(\frac{\pi}{4}-\frac{\alpha}{2}\right)$

</details>

---

