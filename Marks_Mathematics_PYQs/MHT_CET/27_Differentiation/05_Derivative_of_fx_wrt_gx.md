# MHT CET Mathematics - Differentiation

## Topic 5: Derivative of f(x) wrt g(x)

**Total Questions:** 27

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $f(\cos x)$ with respect to $g(\tan x)$ at $x = \dfrac{\pi}{6}$, given that $f'\left(\dfrac{\sqrt{3}}{2}\right) = 4$ and $g'\left(\dfrac{1}{\sqrt{3}}\right) = 2$ is:

**Options:**

- **(A)** $\sqrt{3}$
- **(B)** $2$
- **(C)** $-\dfrac{3}{4}$
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\dfrac{3}{4}$**

**Detailed Solution:**

Let $u = f(\cos x)$ and $v = g(\tan x)$

Differentiating $u$ and $v$ with respect to $x$:

$\dfrac{du}{dx} = f'(\cos x) \cdot (-\sin x)$

$\dfrac{dv}{dx} = g'(\tan x) \cdot (\sec^2 x)$

The derivative of $u$ with respect to $v$ is:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}} = \dfrac{-f'(\cos x) \sin x}{g'(\tan x) \sec^2 x}$

At $x = \dfrac{\pi}{6}$:

$\cos\left(\dfrac{\pi}{6}\right) = \dfrac{\sqrt{3}}{2}$, $\sin\left(\dfrac{\pi}{6}\right) = \dfrac{1}{2}$

$\tan\left(\dfrac{\pi}{6}\right) = \dfrac{1}{\sqrt{3}}$, $\sec^2\left(\dfrac{\pi}{6}\right) = \dfrac{4}{3}$

Substituting these values:

$\dfrac{du}{dv} = \dfrac{-f'\left(\dfrac{\sqrt{3}}{2}\right) \cdot \dfrac{1}{2}}{g'\left(\dfrac{1}{\sqrt{3}}\right) \cdot \dfrac{4}{3}}$

Given $f'\left(\dfrac{\sqrt{3}}{2}\right) = 4$ and $g'\left(\dfrac{1}{\sqrt{3}}\right) = 2$:

$\dfrac{du}{dv} = \dfrac{-4 \cdot \dfrac{1}{2}}{2 \cdot \dfrac{4}{3}} = \dfrac{-2}{\dfrac{8}{3}} = -\dfrac{3}{4}$

Answer: $-\dfrac{3}{4}$

</details>

---

### Q2. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\log_{10} x$ with respect to $\log_x 10$ is

**Options:**

- **(A)** $-\log_{10} x^2$
- **(B)** $-(\log_{10} x)^2$
- **(C)** $(\log_x 10)^2$
- **(D)** $\dfrac{x^2}{100}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-(\log_{10} x)^2$**

**Detailed Solution:**

Let $u = \log_{10} x$ and $v = \log_x 10$.

Using the base change property of logarithms, $v = \dfrac{1}{\log_{10} x} = \dfrac{1}{u}$.

Differentiating $v$ with respect to $u$, we get $\dfrac{dv}{du} = -\dfrac{1}{u^2}$.

The derivative of $u$ with respect to $v$ is given by $\dfrac{du}{dv} = \dfrac{1}{\dfrac{dv}{du}}$.

Substituting the value of $\dfrac{dv}{du}$, we get $\dfrac{du}{dv} = -u^2$.

Replacing $u$ with $\log_{10} x$, we obtain $\dfrac{du}{dv} = -(\log_{10} x)^2$.

Answer: $-(\log_{10} x)^2$

</details>

---

### Q3. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\tan^{-1}\left(\dfrac{\sqrt{1 + x^2} - 1}{x}\right)$ with respect to $\tan^{-1}\left(\dfrac{x}{\sqrt{1 - x^2}}\right)$ at $x = \dfrac{1}{2}$ is

**Options:**

- **(A)** $\dfrac{\sqrt{3}}{2}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{\sqrt{3}}{5}$
- **(D)** $\dfrac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\sqrt{3}}{5}$**

**Detailed Solution:**

Let $u = \tan^{-1}\left(\dfrac{\sqrt{1 + x^2} - 1}{x}\right)$ and $v = \tan^{-1}\left(\dfrac{x}{\sqrt{1 - x^2}}\right)$.

Substituting $x = \tan \theta$ in $u$:

$u = \tan^{-1}\left(\dfrac{\sec \theta - 1}{\tan \theta}\right) = \tan^{-1}\left(\dfrac{1 - \cos \theta}{\sin \theta}\right)$

$u = \tan^{-1}\left(\dfrac{2 \sin^2(\theta/2)}{2 \sin(\theta/2) \cos(\theta/2)}\right) = \tan^{-1}\left(\tan \dfrac{\theta}{2}\right) = \dfrac{\theta}{2} = \dfrac{1}{2} \tan^{-1} x$

Differentiating $u$ with respect to $x$:

$\dfrac{du}{dx} = \dfrac{1}{2(1 + x^2)}$

Substituting $x = \sin \phi$ in $v$:

$v = \tan^{-1}\left(\dfrac{\sin \phi}{\cos \phi}\right) = \tan^{-1}(\tan \phi) = \phi = \sin^{-1} x$

Differentiating $v$ with respect to $x$:

$\dfrac{dv}{dx} = \dfrac{1}{\sqrt{1 - x^2}}$

The derivative of $u$ with respect to $v$ is:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}} = \dfrac{\dfrac{1}{2(1 + x^2)}}{\dfrac{1}{\sqrt{1 - x^2}}} = \dfrac{\sqrt{1 - x^2}}{2(1 + x^2)}$

Substituting $x = \dfrac{1}{2}$:

$\dfrac{du}{dv} = \dfrac{\sqrt{1 - \left(\dfrac{1}{2}\right)^2}}{2\left(1 + \left(\dfrac{1}{2}\right)^2\right)} = \dfrac{\sqrt{\dfrac{3}{4}}}{2\left(\dfrac{5}{4}\right)} = \dfrac{\dfrac{\sqrt{3}}{2}}{\dfrac{5}{2}} = \dfrac{\sqrt{3}}{5}$

Answer: $\dfrac{\sqrt{3}}{5}$

</details>

---

### Q4. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cot[f(x)] = \dfrac{3x - x^3}{1 - 3x^2}$ and $\sin[g(x)] = \dfrac{1 - x^2}{1 + x^2}$, then $\lim\limits_{x \to t}\dfrac{f(x) - f(t)}{g(x) - g(t)} = \ldots$

**Options:**

- **(A)** $\dfrac{3}{2(1 + t^2)}$
- **(B)** $\dfrac{3}{2}$
- **(C)** $\dfrac{5}{2}$
- **(D)** $-\dfrac{5}{2(1 + t^2)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{2}$**

**Detailed Solution:**

Given $\cot[f(x)] = \dfrac{3x - x^3}{1 - 3x^2}$

Substituting $x = \tan\theta$, we get:

$\cot[f(x)] = \dfrac{3\tan\theta - \tan^3\theta}{1 - 3\tan^2\theta} = \tan(3\theta)$

$\cot[f(x)] = \cot\left(\dfrac{\pi}{2} - 3\theta\right)$

$\Rightarrow f(x) = \dfrac{\pi}{2} - 3\theta = \dfrac{\pi}{2} - 3\tan^{-1}x$

Differentiating with respect to $x$, we get:

$f'(x) = \dfrac{-3}{1 + x^2}$

Similarly, given $\sin[g(x)] = \dfrac{1 - x^2}{1 + x^2}$

Substituting $x = \tan\theta$, we get:

$\sin[g(x)] = \dfrac{1 - \tan^2\theta}{1 + \tan^2\theta} = \cos(2\theta)$

$\sin[g(x)] = \sin\left(\dfrac{\pi}{2} - 2\theta\right)$

$\Rightarrow g(x) = \dfrac{\pi}{2} - 2\theta = \dfrac{\pi}{2} - 2\tan^{-1}x$

Differentiating with respect to $x$, we get:

$g'(x) = \dfrac{-2}{1 + x^2}$

The given limit is in the form of the definition of the derivative (or can be evaluated using L'Hospital's Rule):

$\lim\limits_{x \to t}\dfrac{f(x) - f(t)}{g(x) - g(t)} = \dfrac{f'(t)}{g'(t)}$

Substituting the derivatives at $x = t$:

$\dfrac{f'(t)}{g'(t)} = \dfrac{\dfrac{-3}{1 + t^2}}{\dfrac{-2}{1 + t^2}} = \dfrac{3}{2}$

Answer: $\dfrac{3}{2}$

</details>

---

### Q5. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\tan^{-1}\left(\dfrac{\sqrt{1+x^2} - 1}{x}\right)$ with respect to $\sin^{-1}\left(\dfrac{2x}{1+x^2}\right)$ is...

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $\dfrac{1}{4}$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{4}$**

**Detailed Solution:**

Let $u = \tan^{-1}\left(\dfrac{\sqrt{1+x^2} - 1}{x}\right)$ and $v = \sin^{-1}\left(\dfrac{2x}{1+x^2}\right)$.

Substituting $x = \tan \theta$, we get:

$u = \tan^{-1}\left(\dfrac{\sqrt{1+\tan^2\theta} - 1}{\tan\theta}\right)$

$u = \tan^{-1}\left(\dfrac{\sec\theta - 1}{\tan\theta}\right) = \tan^{-1}\left(\dfrac{1 - \cos\theta}{\sin\theta}\right)$

$u = \tan^{-1}\left(\dfrac{2\sin^2(\theta/2)}{2\sin(\theta/2)\cos(\theta/2)}\right) = \tan^{-1}\left(\tan\dfrac{\theta}{2}\right) = \dfrac{\theta}{2} = \dfrac{1}{2}\tan^{-1}x$

Now, for $v$:

$v = \sin^{-1}\left(\dfrac{2\tan\theta}{1+\tan^2\theta}\right) = \sin^{-1}(\sin 2\theta) = 2\theta = 2\tan^{-1}x$

Differentiating $u$ and $v$ with respect to $x$:

$\dfrac{du}{dx} = \dfrac{1}{2(1+x^2)}$

$\dfrac{dv}{dx} = \dfrac{2}{1+x^2}$

The derivative of $u$ with respect to $v$ is given by:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}} = \dfrac{\dfrac{1}{2(1+x^2)}}{\dfrac{2}{1+x^2}} = \dfrac{1}{4}$

Answer: $\dfrac{1}{4}$

</details>

---

### Q6. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\sin ^{-1}\left(2 x \sqrt{1-x^2}\right)$ w.r.t. $\sin ^{-1}\left(3 x-4 x^3\right)$ for $-\frac{1}{2} < x < \frac{1}{2}$ is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{3}{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{3}$**

**Detailed Solution:**

Let $u = \sin^{-1}\left(2 x \sqrt{1-x^2}\right)$ and $v = \sin^{-1}\left(3 x-4 x^3\right)$.

Substitute $x = \sin \theta$. Since $-\dfrac{1}{2} < x < \dfrac{1}{2}$, we have $-\dfrac{\pi}{6} < \theta < \dfrac{\pi}{6}$.

For $u$:
$u = \sin^{-1}(2 \sin \theta \cos \theta) = \sin^{-1}(\sin 2\theta)$
Since $-\dfrac{\pi}{3} < 2\theta < \dfrac{\pi}{3}$, which lies in the principal value branch $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$, we get $u = 2\theta$.

For $v$:
$v = \sin^{-1}(3 \sin \theta - 4 \sin^3 \theta) = \sin^{-1}(\sin 3\theta)$
Since $-\dfrac{\pi}{2} < 3\theta < \dfrac{\pi}{2}$, which also lies in the principal value branch, we get $v = 3\theta$.

We need to find the derivative of $u$ with respect to $v$, which is $\dfrac{du}{dv}$.

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{d\theta}}{\dfrac{dv}{d\theta}} = \dfrac{2}{3}$

Answer: $\frac{2}{3}$

</details>

---

### Q7. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\dfrac{\sin x}{1+\dfrac{\cos x}{1+\dfrac{\sin x}{1+\dfrac{\cos x}{\ldots \ldots}}}}$, then $\dfrac{\mathrm{dy}}{\mathrm{dx}}$ is given by

**Options:**

- **(A)** $\dfrac{y \sin x+(1+y) \cos x}{1+2 y+\cos x-\sin x}$
- **(B)** $\dfrac{y \cos x+(1+y) \sin x}{1+2 y+\cos x-\sin x}$
- **(C)** $\dfrac{y \sin x-(1+y) \cos x}{1+2 y+\cos x-\sin x}$
- **(D)** $\dfrac{y \cos x-(1+y) \sin x}{1+2 y+\cos x-\sin x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{y \sin x+(1+y) \cos x}{1+2 y+\cos x-\sin x}$**

**Detailed Solution:**

The given expression is an infinite continued fraction. We can observe that the expression repeats itself, so we can substitute $y$ into the denominator:

$y = \dfrac{\sin x}{1 + \dfrac{\cos x}{1 + y}}$

Simplifying the right side:

$y = \dfrac{\sin x (1 + y)}{1 + y + \cos x}$

Cross-multiplying to remove the denominator:

$y(1 + y + \cos x) = \sin x (1 + y)$

$y + y^2 + y \cos x = \sin x + y \sin x$

Differentiating both sides with respect to $x$:

$\dfrac{dy}{dx} + 2y \dfrac{dy}{dx} + \dfrac{dy}{dx} \cos x - y \sin x = \cos x + \dfrac{dy}{dx} \sin x + y \cos x$

Grouping the terms containing $\dfrac{dy}{dx}$ on one side:

$\dfrac{dy}{dx} (1 + 2y + \cos x - \sin x) = y \sin x + \cos x + y \cos x$

$\dfrac{dy}{dx} = \dfrac{y \sin x + (1 + y) \cos x}{1 + 2y + \cos x - \sin x}$

Answer: $\dfrac{y \sin x+(1+y) \cos x}{1+2 y+\cos x-\sin x}$

</details>

---

### Q8. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Derivative of $\mathrm{e}^x$ w.r.t. $\sqrt{x}$ is

**Options:**

- **(A)** $\sqrt{x} e^x$
- **(B)** $-2 \sqrt{x}$
- **(C)** $2 \sqrt{x} \mathrm{e}^x$
- **(D)** $\dfrac{1}{2} \sqrt{x} \mathrm{e}^x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \sqrt{x} \mathrm{e}^x$**

**Detailed Solution:**

Let $u = \mathrm{e}^x$ and $v = \sqrt{x}$.

Differentiating $u$ and $v$ with respect to $x$:

$\dfrac{du}{dx} = \mathrm{e}^x$

$\dfrac{dv}{dx} = \dfrac{1}{2\sqrt{x}}$

The derivative of $u$ with respect to $v$ is given by:

$\dfrac{du}{dv} = \dfrac{\dfrac{du}{dx}}{\dfrac{dv}{dx}}$

$\dfrac{du}{dv} = \dfrac{\mathrm{e}^x}{\dfrac{1}{2\sqrt{x}}} = 2\sqrt{x}\mathrm{e}^x$

Answer: $2 \sqrt{x} \mathrm{e}^x$

</details>

---

### Q9. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $x=\log _e\left(\frac{\cos \frac{y}{2}-\sin \frac{y}{2}}{\cos \frac{y}{2}+\sin \frac{y}{2}}\right), \tan \frac{y}{2}=\sqrt{\frac{1-t}{1+t}}$. Then $\left(y_1\right)_{t=\frac{1}{2}}$ has the value

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $-\frac{1}{2}$
- **(C)** $\frac{1}{4}$
- **(D)** $-\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & x=\log _{\mathrm{e}}\left(\frac{\cos \frac{y}{2}-\sin \frac{y}{2}}{\cos \frac{y}{2}+\sin \frac{y}{2}}\right) \\ & \Rightarrow \mathrm{e}^x=\frac{1-\tan \frac{y}{2}}{1+\tan \frac{y}{2}}\end{aligned}$
$\Rightarrow \mathrm{e}^x=\tan \left(\frac{\pi}{4}-\frac{y}{2}\right) \quad$....(i) $\left[\because \tan \frac{\pi}{4}=1\right]$
Differentiating w.r.t. $x$, we get
$\mathrm{e}^x=\sec ^2\left(\frac{\pi}{4}-\frac{y}{2}\right) \cdot\left(\frac{-1}{2}\right) \frac{\mathrm{d} y}{\mathrm{~d} x}$
$\Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=-2 \mathrm{e}^x \cos ^2\left(\frac{\pi}{4}-\frac{y}{2}\right)$
$\begin{aligned} & \text { When } \mathrm{t}=\frac{1}{2}, \\ & \tan \frac{y}{2}=\sqrt{\frac{1-\frac{1}{2}}{1+\frac{1}{2}}} \\ & \Rightarrow \tan \frac{y}{2}=\frac{1}{\sqrt{3}} \\ & \Rightarrow \frac{y}{2}=\frac{\pi}{6}\end{aligned}$
Substituting $\frac{y}{2}=\frac{\pi}{6}$ in (i), we get
$\mathrm{e}^x=\tan \frac{\pi}{12}=2-\sqrt{3}$
$\therefore \quad\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{\mathrm{t}=\frac{1}{2}}=-2(2-\sqrt{3}) \cos ^2 \frac{\pi}{12}$
$\begin{aligned} & =-2(2-\sqrt{3})\left(\frac{\sqrt{3}+1}{2 \sqrt{2}}\right)^2 \\ & =\frac{-1}{2}(2-\sqrt{3})(2+\sqrt{3}) \\ & =-\frac{1}{2}\end{aligned}$

</details>

---

### Q10. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Differentiation of $\tan ^{-1}\left(\frac{\sqrt{1+x^2}-1}{x}\right)$ w.r.t. $\cos ^{-1}\left(\sqrt{\frac{1+\sqrt{1+x^2}}{2 \sqrt{1+x^2}}}\right)$, is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 1
- **(C)** 2
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let $\mathrm{u}=\tan ^{-1}\left[\frac{\sqrt{1+x^2}-1}{x}\right]$
and $v=\cos ^{-1}\left[\sqrt{\frac{1+\sqrt{1+x^2}}{2 \sqrt{1+x^2}}}\right]$
Put $x=\tan \theta$, then $\theta=\tan ^{-1} x$
$$
\begin{aligned}
\therefore \mathrm{u} & =\tan ^{-1}\left[\frac{\sqrt{1+\tan ^2 \theta}-1}{\tan \theta}\right]-\tan ^{-1}\left[\frac{\sec \theta-1}{\tan \theta}\right] \\
& =\tan ^{-1}\left[\frac{\frac{1}{\cos \theta}-1}{\frac{\sin \theta}{\cos \theta}}\right]=\tan ^{-1}\left[\frac{1-\cos \theta}{\sin \theta}\right] \\
& =\tan ^{-1}\left[\frac{2 \sin ^2 \frac{\theta}{2}}{2 \sin \frac{\theta}{2} \cos \frac{\theta}{2}}\right]-\tan ^{-1}\left(\tan \frac{\theta}{2}\right)=\frac{\theta}{2}
\end{aligned}
$$
$$
\therefore \quad \mathrm{u}=\frac{\tan ^{-1} x}{2}
$$
$$
\begin{aligned}
v & =\cos ^{-1}\left[\sqrt{\frac{1+\sqrt{1+\tan ^2 \theta}}{2 \sqrt{1+\tan ^2 \theta}}}\right] \\
& =\cos ^{-1}\left[\sqrt{\frac{1+\sec \theta}{2 \sec \theta}}\right] \\
& =\cos ^{-1}\left[\sqrt{\frac{1+\frac{1}{\cos \theta}}{\frac{2}{\cos \theta}}}\right] \\
& =\cos ^{-1}\left[\sqrt{\frac{1+\cos \theta}{2}}\right] \\
& =\cos ^{-1}\left(\sqrt{\frac{2 \cos ^2\left(\frac{\theta}{2}\right)}{2}}\right) \\
& =\cos ^{-1}\left(\cos \frac{\theta}{2}\right)-\frac{0}{2}
\end{aligned}
$$
$$
\therefore \quad v=\frac{\tan ^{-1} x}{2}
$$
From (i) and (ii), we get $\mathrm{u}=\mathrm{v}$
$$
\therefore \quad \frac{d u}{d v}=1
$$

</details>

---

### Q11. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\mathrm{f}(\tan x)$ w.r.t. $\mathrm{g}(\sec x)$ at $x=\frac{\pi}{4}$ where $\mathrm{f}^{\prime}(1)=2$ and $\mathrm{g}^{\prime}(\sqrt{2})=4$ is
(A) 
(B)

**Options:**

- **(A)** $\frac{1}{\sqrt{2}}$
- **(B)** $\sqrt{2}$
- **(C)** $1$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{2}}$**

**Detailed Solution:**

$\begin{array}{ll} & \text { Let } \mathrm{p}=\mathrm{f}(\tan x) \text { and } \mathrm{q}=\mathrm{g}(\sec x) \\ \therefore \quad & \frac{\mathrm{dp}}{\mathrm{d} x}=\mathrm{f}^{\prime}(\tan x) \times \sec ^2 x \text { and } \\ & \frac{\mathrm{dq}}{\mathrm{d} x}=\mathrm{g}^{\prime}(\sec x) \times \sec x \tan x \\ \therefore \quad & \left.\frac{\mathrm{dp}}{\mathrm{d} x}\right|_{x=\frac{\pi}{4}}=\mathrm{f}^{\prime}(1) \times 2=4, \\ & \left.\frac{\mathrm{dq}}{\mathrm{d} x}\right|_{x=\frac{\pi}{4}}=\mathrm{g}^{\prime}(\sqrt{2}) \times \sqrt{2}=4 \sqrt{2} \\ \therefore \quad & \text { Required Derivative }=\left(\left.\frac{\mathrm{dp}}{\left.\mathrm{dx}\right|_{x=\frac{\pi}{4}} ^{\mathrm{dq}}}\right|_{s=\frac{\pi}{4}} ^{\mathrm{d}}\right)=\frac{4}{4 \sqrt{2}}=\frac{1}{\sqrt{2}}\end{array}$

</details>

---

### Q12. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Derivative of $\tan ^{-1}\left(\frac{\sqrt{1+x^2}-\sqrt{1-x^2}}{\sqrt{1+x^2}+\sqrt{1-x^2}}\right)$ w.r.t. $\cos ^{-1} x^2$ is

**Options:**

- **(A)** $-\frac{1}{2}$
- **(B)** $-1$
- **(C)** $\frac{1}{2}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{1}{2}$**

**Detailed Solution:**

Let $y=\tan ^{-1}\left(\frac{\sqrt{1+x^2}-\sqrt{1-x^2}}{\sqrt{1+x^2}+\sqrt{1-x^2}}\right)$ and $\mathrm{z}=\cos ^{-1}\left(x^2\right)$
Put $x^2=\cos 2 \theta \Rightarrow \theta=\frac{1}{2} \cos ^{-1} x^2$
$$
\begin{aligned}
\therefore \quad y & =\tan ^{-1}\left(\frac{\sqrt{1+\cos 2 \theta}-\sqrt{1-\cos 2 \theta}}{\sqrt{1+\cos 2 \theta}+\sqrt{1-\cos 2 \theta}}\right) \\
\Rightarrow y & =\tan ^{-1}\left(\frac{\cos \theta-\sin \theta}{\cos \theta+\sin \theta}\right) \\
\Rightarrow y & =\tan ^{-1}\left(\frac{1-\tan \theta}{1+\tan \theta}\right) \\
\Rightarrow y & =\tan ^{-1}\left(\tan \left(\frac{\pi}{4}-\theta\right)\right) \\
\Rightarrow y & =\frac{\pi}{4}-\frac{1}{2} \cos ^{-1} x^2 \\
\Rightarrow y & =\frac{\pi}{4}-\frac{1}{2} \mathrm{z} \\
\therefore \quad \frac{\mathrm{dy}}{\mathrm{dz}} & =-\frac{1}{2}
\end{aligned}
$$

</details>

---

### Q13. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x=3 \tan \mathrm{t}$ and $y=3 \sec \mathrm{t}$, then the value of $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}$ at $\mathrm{t}=\frac{\pi}{4}$ is

**Options:**

- **(A)** $\frac{-1}{6 \sqrt{2}}$
- **(B)** $\frac{1}{6 \sqrt{2}}$
- **(C)** $\frac{1}{3 \sqrt{2}}$
- **(D)** $\frac{3}{2 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{6 \sqrt{2}}$**

**Detailed Solution:**

$\begin{aligned} & x=3 \tan \mathrm{t} \\ & \therefore \quad \frac{\mathrm{d} x}{\mathrm{dt}}=3 \sec ^2 \mathrm{t} \\ & y=3 \sec \mathrm{t} \\ & \therefore \quad \frac{\mathrm{d} y}{\mathrm{dt}}=3 \sec \mathrm{t} \tan \mathrm{t} \\ & \text { Now, } \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\frac{\mathrm{d} y}{\mathrm{dt}}}{\frac{\mathrm{d} x}{\mathrm{dt}}}=\frac{3 \sec \mathrm{tan} t}{3 \sec ^2 \mathrm{t}}=\sin \mathrm{t} \\ & \therefore \quad \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=\frac{\mathrm{d}}{\mathrm{dt}}(\sin \mathrm{t}) \cdot \frac{\mathrm{dt}}{\mathrm{d} x} \\ & =\cos t \times \frac{1}{3 \sec ^2 t} \\ & \therefore \quad \frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}=\frac{\cos ^3 \mathrm{t}}{3} \\ & \therefore \quad\left(\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}\right)_{\left(\mathrm{t}=\frac{\pi}{4}\right)}=\frac{\left(\cos \frac{\pi}{4}\right)^3}{3}=\frac{1}{6 \sqrt{2}} \\ & \end{aligned}$

</details>

---

### Q14. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The derivative of $\mathrm{f}(\sec x)$ with respect to $\mathrm{g}(\tan x)$ at $x=\frac{\pi}{4}$, where $\mathrm{f}^{\prime}(\sqrt{2})=4$ and $\mathrm{g}^{\prime}(1)=2$, is

**Options:**

- **(A)** $2$
- **(B)** $\frac {1}{\sqrt 2}$
- **(C)** $\sqrt 2$
- **(D)** $\frac {1}{2\sqrt 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt 2$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } y=\mathrm{f}(\sec x) \text { and } \mathrm{z}=\mathrm{g}(\tan x) \\ & \frac{\mathrm{d} y}{\mathrm{~d} x}=\mathrm{f}^{\prime}(\sec x) \cdot \sec x \tan x \\ & \frac{\mathrm{dz}}{\mathrm{d} x}=\mathrm{g}^{\prime}(\tan x) \cdot \sec ^2 x \\ & \text { Now, } \frac{\mathrm{d} y}{\mathrm{dz}}=\frac{\mathrm{f}^{\prime}(\sec x) \sec x \tan x}{\mathrm{~g}^{\prime}(\tan x) \sec ^2 x} \\ & \frac{\mathrm{d} y}{\mathrm{dz}}=\frac{\mathrm{f}^{\prime}(\sec x) \tan x}{\mathrm{~g}^{\prime}(\tan x) \cdot \sec x} \\ & \left.\frac{d y}{d z}\right|_{x=\frac{\pi}{4}}=\frac{f^{\prime}\left(\sec \frac{\pi}{4}\right) \tan \frac{\pi}{4}}{g^{\prime}\left(\tan \frac{\pi}{4}\right) \sec \frac{\pi}{4}} \\ & =\frac{\mathrm{f}^{\prime}(\sqrt{2}) \cdot(1)}{\mathrm{g}^{\prime}(1) \cdot \sqrt{2}} \Rightarrow \frac{4 \times 1}{2 \sqrt{2}} \\ & =\sqrt{2} \\ & \end{aligned}$

</details>

---

### Q15. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The rate of change of $\sqrt{x^2+16}$ with respect to $\frac{x}{x-1}$ at $x=5$ is

**Options:**

- **(A)** $\frac{-80}{\sqrt{41}}$
- **(B)** $\frac{80}{\sqrt{41}}$
- **(C)** $\frac {12}{5}$
- **(D)** $\frac {-12}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-80}{\sqrt{41}}$**

**Detailed Solution:**

$\begin{aligned} & y=\sqrt{x^2+16} \\ & \therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{2 x}{2 \sqrt{x^2+16}} \\ & \therefore \quad \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{x}{\sqrt{x^2+16}}... (i) \\ & \text { Let } \mathrm{z}=\frac{x}{x-1} \\ & \therefore \quad \frac{\mathrm{dz}}{\mathrm{d} x}=\frac{(x-1)-x}{(x-1)^2} \\ & \therefore \quad \frac{\mathrm{dz}}{\mathrm{d} x}=\frac{-1}{(x-1)^2}... (ii) \\ & \therefore \quad\left(\frac{d y}{d z}\right)_{x=5}=\frac{\frac{x}{\sqrt{x^2+16}}}{\frac{-1}{(x-1)^2}} \\ & =\frac{-5}{\sqrt{25+16}} \times 16=\frac{-80}{\sqrt{41}} \\ & \end{aligned}$

</details>

---

### Q16. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Derivative of $\sin ^{-1}\left(\frac{2 x}{1+x^2}\right)$ w.r.t. $\tan ^{-1} x,-1 < x < 1$ is

**Options:**

- **(A)** 2
- **(B)** $\frac{1}{1+x^2}$
- **(C)** $\frac{2}{1+x^2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

$\begin{aligned} & \sin ^{-1}\left(\frac{2 x}{1+x^2}\right) \text { let } x=\tan \theta \\ & =\sin ^{-1}\left(\frac{2 \tan \theta}{1+\tan ^2 \theta}\right)=\sin ^{-1}(\sin 2 \theta)=2 \theta=2 \tan ^{-1} x \\ & \text { Now } \frac{d\left(\sin ^{-1} \frac{2 x}{1+x^2}\right)}{d\left(\tan ^{-1} x\right)}=\frac{d\left(2 \tan ^{-1} x\right)}{d\left(\tan ^{-1} x\right)}=2\end{aligned}$

</details>

---

### Q17. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The second derivative of a $\sin ^3 t$ w.r.t $a \cos ^3 t$ at $t=\frac{\pi}{4}$ is

**Options:**

- **(A)** $\frac{-4 \sqrt{2}}{3 a}$
- **(B)** $\frac{4 \sqrt{2}}{3 a}$
- **(C)** $\frac{4 \sqrt{2}}{3 a}$
- **(D)** $\frac{1}{12 a}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4 \sqrt{2}}{3 a}$**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{d}^2\left(a \sin ^3 t\right)}{\alpha\left(a \cos ^3 t\right)^2}=\frac{d\left(\frac{\mathrm{d}\left(a \sin ^3 t\right)}{\mathrm{d}\left(a \cos ^3 t\right)}\right)}{\mathrm{d}\left(a \cos ^3 t\right)}=\frac{\mathrm{d}\left\{\frac{\mathrm{d}\left(a \sin ^3 t\right) / \mathrm{d} t}{\mathrm{~d}\left(a \cos ^3 t / \mathrm{d} t\right)}\right\}}{\mathrm{d}\left(a \cos ^3 t\right)} \\ & =\frac{\mathrm{d}\left\{\frac{3 a \sin ^2 t \cdot \cos t}{-a \cdot 3 \cdot \cos ^2 t \cdot \sin t}\right\}}{\mathrm{d}\left(a \cos ^3 t\right)}=\frac{\mathrm{d}\{-\tan t\}}{\mathrm{d}\left(a \cos ^3 t\right)} \\ & =\frac{\frac{\mathrm{d}(-\tan t)}{\mathrm{d} t}}{\frac{\mathrm{d}\left(a \cos ^3 t\right)}{\mathrm{d} t}}=\frac{-\sec ^2 t}{-3 a \cos ^2 t \sin t}=\frac{1}{3 a \cos ^4 t \cdot \sin t} \\ & \text { at, } t=\frac{\pi}{4} ; \frac{1}{3 a \cos ^4 \frac{\pi}{4} \cdot \sin \frac{\pi}{4}}=\frac{1}{3 a\left(\frac{1}{\sqrt{2}}\right)^4 \frac{1}{\sqrt{2}}}=\frac{4 \sqrt{2}}{3 a}\end{aligned}$

</details>

---

### Q18. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $(\log \mathrm{x})^{\mathrm{x}}$ with respect to $\log \mathrm{x}$ is

**Options:**

- **(A)** $(\log x)^x\left[\frac{1}{\log x} \log (\log x)\right]$
- **(B)** $(\log )^x\left[\log x+\frac{1}{\log (\log x)}\right]$
- **(C)** $x(\log )^x\left[\frac{1}{\log x}+\log (\log x)\right]$
- **(D)** $x(\log )^x\left[\log x+\frac{1}{\log (\log x)}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x(\log )^x\left[\frac{1}{\log x}+\log (\log x)\right]$**

**Detailed Solution:**

Let $\mathrm{u}=(\log \mathrm{x})^{\mathrm{x}}$
$$
\begin{aligned}
& \therefore \log \mathrm{u}=\mathrm{x} \log \left[\log (\mathrm{x})^{\mathrm{x}}\right] \\
& \therefore \frac{1}{\mathrm{u}} \frac{\mathrm{du}}{\mathrm{dx}}=\frac{\mathrm{x}}{\log (\mathrm{x})} \times \frac{1}{\mathrm{x}}+\log (\log \mathrm{x})=\log (\log \mathrm{x})+\frac{1}{\log \mathrm{x}} \\
& \therefore \frac{\mathrm{du}}{\mathrm{dx}}=(\log \mathrm{x})^{\mathrm{x}}\left[\frac{1}{\log \mathrm{x}}+\log (\log \mathrm{x})\right]
\end{aligned}
$$
Let $v=\log x \Rightarrow \frac{d v}{d x}=\frac{1}{x}$
$$
\therefore \frac{d u}{d v}=(\log x)^x(x)\left[\frac{1}{\log x}+\log (\log x)\right]
$$

</details>

---

### Q19. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\sin ^{-1}\left(\frac{\sqrt{1+x}+\sqrt{1-x}}{2}\right)$ w.r.t. $\cos ^{-1} x$ is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $-\frac{1}{2}$
- **(C)** $-1$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

(B)
Put $x=\cos \theta$, Then $\theta=\cos ^{-1} x$ 
$\begin{aligned}\left[\frac{\sqrt{1+x}+\sqrt{1-x}}{2}\right] &=\left[\frac{\sqrt{1+\cos \theta}+\sqrt{1-\cos \theta}}{2}\right]=\left[\frac{\sqrt{2 \cos ^{2} \frac{\theta}{2}}+\sqrt{2 \sin ^{2} \frac{\theta}{2}}}{2}\right] \\ &=\frac{\sqrt{2} \cos \frac{\theta}{2}}{2}+\frac{\sqrt{2} \sin \frac{\theta}{2}}{2}=\frac{1}{\sqrt{2}} \cdot \frac{\cos \theta}{2}+\frac{1}{\sqrt{2}} \frac{\sin \theta}{2} \\ &=\frac{\sin \pi}{4} \cdot \frac{\cos \theta}{2}+\frac{\cos \pi}{4} \cdot \frac{\sin \theta}{2}=\sin \left(\frac{\pi}{4}+\frac{\theta}{2}\right) \end{aligned}$ 
$\therefore y=\sin ^{-1}\left(\sin \left(\frac{\pi}{4}+\frac{\theta}{2}\right)\right)=\frac{\pi}{4}+\frac{\theta}{2}=\frac{\pi}{4}+\frac{\cos ^{-1} x}{2}$ $\therefore \frac{d y}{d x}=\frac{1}{2} \times \frac{-1}{\sqrt{1-x^{2}}}=\frac{-1}{2 \sqrt{1-x^{2}}}$

</details>

---

### Q20. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The derivative of $\cot ^{-1} x$ w.r.t $\log \left(1+x^{2}\right)$ is

**Options:**

- **(A)** $-2 x$
- **(B)** $-\frac{1}{2 x}$
- **(C)** $\frac{1}{2 x}$
- **(D)** $2 x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{1}{2 x}$**

**Detailed Solution:**

(C)
Let $u=\cot ^{-1} x$ and $v=\log \left(1+x^{2}\right)$
$\begin{array}{l}\frac{d u}{d x}=\frac{-1}{1+x^{2}} \text { and } \frac{d v}{d x}=\frac{2 x}{1+x^{2}} \\ \therefore \frac{d u}{d v}=\frac{\left(\frac{d u}{d x}\right)}{\left(\frac{d v}{d x}\right)}=\frac{\left(\frac{-1}{1+x^{2}}\right)}{\left(\frac{2 x}{1+x^{2}}\right)}=\frac{-1}{2 x}\end{array}$

</details>

---

### Q21. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The derivative of $f(\tan x)$ w.r.t. $g(\sec x)$ at $x=\frac{\pi}{4}$, where $f^{\prime}(1)=2$ and $g^{\prime}(\sqrt{2})=4$ is

**Options:**

- **(A)** $\frac{1}{\sqrt{2}}$
- **(B)** 2
- **(C)** $\sqrt{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{2}}$**

**Detailed Solution:**

$$
\begin{array}{l}
\frac{\frac{d}{d x} f(\tan x)}{\frac{d}{d x} g(\sec x)}=\frac{f^{\prime}(\tan x) \cdot \sec ^{2} x}{g^{\prime}(\sec x) \cdot \sec x \tan x} \\
\text { At } x=\frac{\pi}{4} \text { we get } \\
=\frac{f^{\prime}\left(\tan \frac{\pi}{4}\right)\left(\sec ^{2} \frac{\pi}{4}\right)}{g^{\prime}\left(\sec \frac{\pi}{4}\right) \sec \frac{\pi}{4} \tan \frac{\pi}{4}}=\frac{f^{\prime}(1)(2)}{g^{\prime}(\sqrt{2})(\sqrt{2})(1)}=\frac{2 \times 2}{4 \sqrt{2}}=\frac{1}{\sqrt{2}}
\end{array}
$$

</details>

---

### Q22. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $x=\log t, y+1=\frac{1}{t}, \quad$ then $e^{-x} \frac{d^{2} x}{d y^{2}}+\frac{d x}{d y}=$

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** $-1$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Given $x=\log t$ and $y+1=\frac{1}{t}$
$\therefore \frac{d x}{d t}=\frac{1}{t}$ and $\frac{d y}{d t}=\frac{-1}{t^{2}}$
$\therefore \frac{d x}{d y}=\frac{1}{t} \times\left(-t^{2}\right)=-t$
$\therefore \frac{d^{2} x}{d y^{2}}=\frac{d}{d t}\left(\frac{d x}{d y}\right) \times \frac{d t}{d y}=\frac{d}{d t}(-t) \times \frac{1}{\left(\frac{d y}{d t}\right)}=\frac{(-1)}{\left(\frac{-1}{t^{2}}\right)}=t^{2}$
$e^{-x}=e^{-\log t}=e^{\log (t)^{-1}}=\frac{1}{t}$
Thus $e^{-x} \frac{d^{2} y}{d x^{2}}+\frac{d x}{d y}$
$=\left(\frac{1}{t}\right)\left(t^{2}\right)+(-t)=t-t=0$

</details>

---

### Q23. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>x</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo></math> and <math><mi>y</mi><mo>=</mo><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo></math> are differentiable functions of <math><mi>t</mi></math> then <math><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mi> </mi><mo>⋅</mo><mi> </mi><msup> <mi>g</mi> <mo>″</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mo>−</mo><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mi> </mi><mo>⋅</mo><mi> </mi><msup> <mi>f</mi> <mo>″</mo> </msup> <mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo> </mrow> <mrow> <msup> <mrow> <mrow><mo>[</mo> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> <mo>]</mo></mrow> </mrow> <mn>3</mn> </msup> <mi> </mi><mi> </mi> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mi> </mi><mo>⋅</mo><mi> </mi><msup> <mi>g</mi> <mo>″</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mo>−</mo><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mi> </mi><mo>⋅</mo><mi> </mi><msup> <mi>f</mi> <mo>″</mo> </msup> <mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo> </mrow> <mrow> <msup> <mrow> <mrow><mo>[</mo> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> <mo>]</mo></mrow> </mrow> <mn>2</mn> </msup> <mi> </mi><mi> </mi> </mrow> </mfrac> </mrow> </math>
- **(C)** <math > <mfrac>  <mrow>   <msup>    <mi>g</mi>    <mo>&#x2032;</mo>   </msup>   <mrow><mo>(</mo>    <mi>t</mi>   <mo>)</mo></mrow><mi>&#x00A0;</mi><mo>&#x22C5;</mo><mi>&#x00A0;</mi><msup>    <mi>f</mi>    <mo>&#x2033;</mo>   </msup>   <mrow><mo>(</mo>    <mi>t</mi>   <mo>)</mo></mrow><mo>&#x2212;</mo><msup>    <mi>f</mi>    <mo>&#x2032;</mo>   </msup>   <mrow><mo>(</mo>    <mi>t</mi>   <mo>)</mo></mrow><mi>&#x00A0;</mi><mo>&#x22C5;</mo><mi>&#x00A0;</mi><msup>    <mi>g</mi>    <mo>&#x2033;</mo>   </msup>   <mo stretchy='false'>(</mo><mi>t</mi><mo stretchy='false'>)</mo>  </mrow>  <mrow>   <msup>    <mrow>     <mrow><mo>[</mo> <mrow>      <msup>       <mi>f</mi>       <mo>&#x2032;</mo>      </msup>      <mrow><mo>(</mo>       <mi>t</mi>      <mo>)</mo></mrow>     </mrow> <mo>]</mo></mrow>    </mrow>    <mn>3</mn>   </msup>   <mi>&#x00A0;</mi><mi>&#x00A0;</mi>  </mrow> </mfrac> </math>
- **(D)** <math > <mfrac>  <mrow>   <msup>    <mi>g</mi>    <mo>&#x2032;</mo>   </msup>   <mrow><mo>(</mo>    <mi>t</mi>   <mo>)</mo></mrow><mi>&#x00A0;</mi><mo>&#x22C5;</mo><mi>&#x00A0;</mi><msup>    <mi>f</mi>    <mo>&#x2033;</mo>   </msup>   <mrow><mo>(</mo>    <mi>t</mi>   <mo>)</mo></mrow><mo>+</mo><msup>    <mi>f</mi>    <mo>&#x2032;</mo>   </msup>   <mrow><mo>(</mo>    <mi>t</mi>   <mo>)</mo></mrow><mi>&#x00A0;</mi><mo>&#x22C5;</mo><mi>&#x00A0;</mi><msup>    <mi>g</mi>    <mo>&#x2033;</mo>   </msup>   <mrow><mo>(</mo>    <mi>t</mi>   <mo>)</mo></mrow>  </mrow>  <mrow>   <msup>    <mrow>     <mrow><mo>[</mo> <mrow>      <msup>       <mi>f</mi>       <mo>&#x2032;</mo>      </msup>      <mrow><mo>(</mo>       <mi>t</mi>      <mo>)</mo></mrow>     </mrow> <mo>]</mo></mrow>    </mrow>    <mn>3</mn>   </msup>   <mi>&#x00A0;</mi><mi>&#x00A0;</mi>  </mrow> </mfrac> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mfrac> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mi> </mi><mo>⋅</mo><mi> </mi><msup> <mi>g</mi> <mo>″</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mo>−</mo><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow><mi> </mi><mo>⋅</mo><mi> </mi><msup> <mi>f</mi> <mo>″</mo> </msup> <mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo> </mrow> <mrow> <msup> <mrow> <mrow><mo>[</mo> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> <mo>]</mo></mrow> </mrow> <mn>3</mn> </msup> <mi> </mi><mi> </mi> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<math><mi>X</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo></math>
<math><mi>Y</mi><mo>=</mo><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo></math>
<math> <mrow> <mfrac> <mrow> <mi>d</mi><mi>x</mi> </mrow> <mrow> <mi>d</mi><mi>t</mi> </mrow> </mfrac> <mo>=</mo><msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mi>d</mi><mi>x</mi> </mrow> <mrow> <mi>d</mi><mi>t</mi> </mrow> </mfrac> <mo>=</mo><msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mi>d</mi><mi>y</mi> </mrow> <mrow> <mi>d</mi><mi>x</mi> </mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mfrac> <mrow> <mi>d</mi><mi>y</mi> </mrow> <mrow> <mi>d</mi><mi>t</mi> </mrow> </mfrac> </mrow> <mrow> <mfrac> <mrow> <mi>d</mi><mi>x</mi> </mrow> <mrow> <mi>d</mi><mi>t</mi> </mrow> </mfrac> </mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <msup> <mi>d</mi> <mn>2</mn> </msup> <mi>y</mi> </mrow> <mrow> <mi>d</mi><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo><mfrac> <mi>d</mi> <mrow> <mi>d</mi><mi>x</mi> </mrow> </mfrac> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <msup> <mi>g</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> <mrow> <msup> <mi>f</mi> <mo>′</mo> </msup> <mrow><mo>(</mo> <mi>t</mi> <mo>)</mo></mrow> </mrow> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mi>d</mi> <mrow> <mi>d</mi><mi>t</mi> </mrow> </mfrac> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <msup> <mi>g</mi> <mo>′</mo> </msup> <mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo> </mrow> <mrow> <msup> <mi>g</mi> <mo>′</mo> </msup> <mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo> </mrow> </mfrac> </mrow> <mo>)</mo></mrow><mo>.</mo><mfrac> <mrow> <mi>d</mi><mi>t</mi> </mrow> <mrow> <mi>d</mi><mi>x</mi> </mrow> </mfrac> </mrow> </math>
<math > <mrow>  <mo>=</mo><mfrac>   <mrow>    <msup>     <mi>f</mi>     <mo>&#x2032;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow><mo>&#x22C5;</mo><msup>     <mi>g</mi>     <mo>&#x2033;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow><mo>&#x2212;</mo><msup>     <mi>g</mi>     <mo>&#x2032;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow><mo>&#x22C5;</mo><msup>     <mi>f</mi>     <mo>&#x2033;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow>   </mrow>   <mrow>    <msup>     <mrow>      <mrow><mo>(</mo>       <mrow>        <msup>         <mi>f</mi>         <mo>&#x2032;</mo>        </msup>        <mrow><mo>(</mo>         <mi>t</mi>        <mo>)</mo></mrow>       </mrow>      <mo>)</mo></mrow>     </mrow>     <mn>2</mn>    </msup>    <mi>&#x00A0;</mi><mi>&#x00A0;</mi><mi>&#x00A0;</mi>   </mrow>  </mfrac>  <mo>&#x22C5;</mo><mfrac>   <mn>1</mn>   <mrow>    <msup>     <mi>f</mi>     <mo>&#x2032;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow>   </mrow>  </mfrac>   </mrow></math>
<math > <mrow>  <mo>=</mo><mfrac>   <mrow>    <msup>     <mi>f</mi>     <mo>&#x2032;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow><mo>&#x22C5;</mo><msup>     <mi>g</mi>     <mo>&#x2033;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow><mo>&#x2212;</mo><msup>     <mi>g</mi>     <mo>&#x2032;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow><mo>&#x22C5;</mo><msup>     <mi>f</mi>     <mo>&#x2033;</mo>    </msup>    <mrow><mo>(</mo>     <mi>t</mi>    <mo>)</mo></mrow>   </mrow>   <mrow>    <msup>     <mrow>      <mrow><mo>(</mo>       <mrow>        <msup>         <mi>f</mi>         <mo>&#x2032;</mo>        </msup>        <mrow><mo>(</mo>         <mi>t</mi>        <mo>)</mo></mrow>       </mrow>      <mo>)</mo></mrow>     </mrow>     <mn>3</mn>    </msup>    <mi>&#x00A0;</mi><mi>&#x00A0;</mi><mi>&#x00A0;</mi>   </mrow>  </mfrac>   </mrow></math>

</details>

---

### Q24. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

Derivative of <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi></mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow></mrow></mrow></mrow></mfenced></mrow></mrow></math> with respect to <math><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow></math> at <math><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math> is _______

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>1</mn></math>**

**Detailed Solution:**

Let <math><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mo>(</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow></mrow></mrow><mo>)</mo></mrow></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mfrac><mrow><mi>d</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi><mi> </mi></mrow></mrow></mrow></mfrac><mo>⋅</mo><mo>(</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>a</mi></mrow></mrow><mo>)</mo></math>
<math><mo>⇒</mo><mi> </mi><mfrac><mrow><mi>d</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow><mo>[</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow><mo>]</mo></mrow><mrow><mo>[</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow></mrow></mrow><mo>]</mo></mrow></mfrac></math>
<math><mo>⇒</mo><mi> </mi><mfrac><mrow><mi>d</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac><mo>=</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow></math> ..... (i)
Now,
Let <math><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mfrac><mrow><mi>d</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac><mo>=</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow><mo>.</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow><mi> </mi></math> ..... (ii)
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mfrac><mrow><mi>d</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mi>d</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow><mo>.</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow></mrow></mfrac><mo>=</mo><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>θ</mi></mrow></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><msub><mrow><mfenced close="|" open="" separators="|"><mrow><mfrac><mrow><mi>d</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mi>d</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msub><mo>=</mo><mrow><mrow> <mrow> <mfrac> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <msub> <mo>dy</mo> <mn>1</mn> </msub> </mrow> <mrow> <mtext>d</mtext> <mi>θ</mi> </mrow> </mfrac> </mrow> </mfenced> </mrow> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <msub> <mo>dy</mo> <mn>2</mn> </msub> </mrow> <mrow> <mtext>d</mtext> <mi>θ</mi> </mrow> </mfrac> </mrow> </mfenced> </mrow> </mfrac> <mo>=</mo> </mrow>  <mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>1</mn></mrow></mrow></math>

</details>

---

### Q25. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

Differentiation of <math><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></mrow></mfenced></mrow></mrow></math> with respect to <math><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mo>(</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>)</mo></mrow></mrow></math> is .....

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></math>
- **(C)** <math><mn>3</mn></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>L</mi><mi>e</mi><mi>t</mi><mi> </mi><mi>x</mi><mo>=</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>θ</mi></math>

then <math><mi>f</mi><mfenced separators="|"><mrow><mi>θ</mi></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow></mrow><mrow><mn>1</mn><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>θ</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mo>=</mo><mi> </mi><mi>θ</mi></mrow></mrow></math>
and <math><mi>g</mi><mfenced separators="|"><mrow><mi>θ</mi></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mo>(</mo><mn>3</mn><mi> </mi><mi>s</mi><mi>i</mi><mi>n</mi><mi>θ</mi><mo>-</mo><mn>4</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>θ</mi><mo>)</mo></mrow></mrow></mrow></mrow><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mo>(</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mn>3</mn><mi>θ</mi><mo>)</mo><mo>=</mo><mn>3</mn><mi>θ</mi></mrow></mrow></mrow></mrow></math>
Differentiating f w.r.t to g
 <math><mo>⟹</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mi>d</mi><mfenced separators="|"><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>θ</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>d</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>θ</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q26. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

If $x=f(t)$ and $y=g(t)$, then the value of $\frac{d^{2} y}{d x^{2}}$ is

**Options:**

- **(A)** $\frac{f^{\prime}(t) g^{\prime \prime}(t) g^{\prime}(t) f^{\prime \prime}(t)}{\left\{f^{\prime}(t)\right\}^{3}}$
- **(B)** $\frac{f^{\prime}(t) g^{\prime \prime}(t)-g^{\prime}(t) f^{\prime \prime}(t)}{\left\{f^{\prime}(t)\right\}^{2}}$
- **(C)** $\frac{g^{\prime}(t) f^{\prime \prime}(t) g^{\prime \prime}(t) f^{\prime}(t)}{\left\{f^{\prime}(t)\right\}^{2}}$
- **(D)** $\frac{g^{\prime}(t) f^{\prime \prime}(t)-g^{\prime \prime}(t) f^{\prime}(t)}{\left\{f^{\prime}(t)\right\}^{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{f^{\prime}(t) g^{\prime \prime}(t) g^{\prime}(t) f^{\prime \prime}(t)}{\left\{f^{\prime}(t)\right\}^{3}}$**

**Detailed Solution:**

Given, $x=f(t), y=g(t)$
$$
\begin{array}{c}
\frac{d x}{d t}=f^{\prime}(t), \frac{d y}{d t}=g^{\prime}(t) \\
\therefore \quad \frac{d y}{d x}=\frac{g^{\prime}(t)}{f^{\prime}(t)}
\end{array}
$$
Now, $\frac{d^{2} y}{d x^{2}}=\frac{d}{d x}\left(\frac{d y}{d x}\right)$
$$
\begin{aligned}
&=\frac{d}{d t}\left(\frac{g^{\prime}(t)}{f^{\prime}(t)}\right) \frac{d t}{d x} \\
=&\left[\frac{f^{\prime}(t) \cdot g^{\prime \prime}(t)-g^{\prime}(t) f^{\prime \prime}(t)}{\left[f^{\prime}(t)\right]^{2}}\right] \cdot \frac{1}{f^{\prime}(t)} \\
=& \frac{f^{\prime}(t) \cdot g^{\prime \prime}(t)-g^{\prime}(t) f^{\prime \prime}(t)}{\left\{f^{\prime}(t)\right\}^{3}}
\end{aligned}
$$

</details>

---

### Q27. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

The derivative of $\cos ^{3} x$ w.r.t. $\sin ^{3} x$ is

**Options:**

- **(A)** $-\cot x$
- **(B)** $\cot x$
- **(C)** $\tan x$
- **(D)** $-\tan x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\cot x$**

**Detailed Solution:**

Let $\begin{aligned} u=\cos ^{3} x, v=\sin ^{3} x \\ \frac{d u}{d x}=-3 & \cos ^{2} x \sin x, \frac{d v}{d x}=3 \sin ^{2} x \cos x \\ \text { Now, } \frac{d u}{d v} &=\frac{-3 \cos ^{2} x \sin x}{3 \sin ^{2} x \cos x} \\ &=-\frac{\cos x}{\sin x} \\ &=-\cot x \end{aligned}$

</details>

---

