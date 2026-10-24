# JEE Main Mathematics - Indefinite Integration

## Topic 1: Integration by Substitution

**Total Questions:** 75

---

### Q1. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x) = \int \left(\dfrac{16x + 24}{x^2 + 2x - 15}\right) dx$. If $f(4) = 14 \log_e(3)$ and $f(7) = \log_e(2^{\alpha} \cdot 3^{\beta})$, $\alpha, \beta \in \mathbb{N}$, then $\alpha + \beta$ is equal to:

**Options:**

- **(A)** $31$
- **(B)** $37$
- **(C)** $39$
- **(D)** $41$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $39$**

**Detailed Solution:**

The given integral is $f(x) = \int \left(\dfrac{16x + 24}{x^2 + 2x - 15}\right) dx$.

Factorizing the denominator, we get $x^2 + 2x - 15 = (x + 5)(x - 3)$.

Using partial fractions, we can write:

$\dfrac{16x + 24}{(x + 5)(x - 3)} = \dfrac{A}{x + 5} + \dfrac{B}{x - 3}$

$16x + 24 = A(x - 3) + B(x + 5)$

Substituting $x = 3$, we get $72 = 8B \Rightarrow B = 9$.

Substituting $x = -5$, we get $-56 = -8A \Rightarrow A = 7$.

Therefore, the integral becomes:

$f(x) = \int \left(\dfrac{7}{x + 5} + \dfrac{9}{x - 3}\right) dx$

$f(x) = 7 \log_e|x + 5| + 9 \log_e|x - 3| + C$

Given $f(4) = 14 \log_e(3)$, we substitute $x = 4$:

$f(4) = 7 \log_e(9) + 9 \log_e(1) + C = 14 \log_e(3) + C$

Since $f(4) = 14 \log_e(3)$, we get $C = 0$.

Thus, $f(x) = 7 \log_e|x + 5| + 9 \log_e|x - 3|$.

Now, substituting $x = 7$:

$f(7) = 7 \log_e(12) + 9 \log_e(4)$

$f(7) = 7 \log_e(2^2 \cdot 3) + 9 \log_e(2^2)$

$f(7) = 7(2 \log_e(2) + \log_e(3)) + 18 \log_e(2)$

$f(7) = 14 \log_e(2) + 7 \log_e(3) + 18 \log_e(2)$

$f(7) = 32 \log_e(2) + 7 \log_e(3)$

$f(7) = \log_e(2^{32} \cdot 3^7)$

Comparing this with $f(7) = \log_e(2^{\alpha} \cdot 3^{\beta})$, we get $\alpha = 32$ and $\beta = 7$.

Therefore, $\alpha + \beta = 32 + 7 = 39$.

Answer: $39$

</details>

---

### Q2. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=\int \frac{\mathrm{d} x}{x^{\left(\frac{2}{3}\right)}+2 x^{\left(\frac{1}{2}\right)}}$ be such that $f(0)=-26+24 \log _{\mathrm{e}}(2)$. If $f(1)=\mathrm{a}+\mathrm{b} \log _{\mathrm{e}}(3)$, where $\mathrm{a}, \mathrm{b} \in \mathbf{Z}$, then $\mathrm{a}+\mathrm{b}$ is equal to :

**Options:**

- **(A)** -26
- **(B)** -11
- **(C)** -5
- **(D)** -18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -11**

**Detailed Solution:**

Let $u = x^{1/6}$, so $x = u^6$ and $dx = 6u^5 du$. Then $x^{2/3} = u^4$, $x^{1/2} = u^3$. 
$f(x) = \int \frac{6u^5 du}{u^4 + 2u^3} = \int \frac{6u^2 du}{u+2}$. 
By polynomial division: $\frac{u^2}{u+2} = u - 2 + \frac{4}{u+2}$. 
$f(x) = 6\left(\frac{u^2}{2} - 2u + 4\ln|u+2|\right) + C = 3u^2 - 12u + 24\ln(u+2) + C$. 
Substituting back: $f(x) = 3x^{1/3} - 12x^{1/6} + 24\ln(x^{1/6}+2) + C$. 
From $f(0) = -26 + 24\ln(2)$: $24\ln(2) + C = -26 + 24\ln(2)$, so $C = -26$. 
At $x = 1$: $f(1) = 3 - 12 + 24\ln(3) - 26 = -35 + 24\ln(3)$. 
Thus $a = -35$, $b = 24$, and $a + b = -11$.

</details>

---

### Q3. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{I}(x)=\int \frac{3 d x}{(4 x+6)\left(\sqrt{4 x^{2}+8 x+3}\right)}$ and $\mathrm{I}(0)=\frac{\sqrt{3}}{4}+20$. If $\mathrm{I}\left(\frac{1}{2}\right)=\frac{a \sqrt{2}}{b}+\mathrm{c}$, where $a, b, \mathrm{c} \in \mathrm{N}, \operatorname{gcd}(a, b)=1$, then $a+b+c$ is equal to

**Options:**

- **(A)** 30
- **(B)** 31
- **(C)** 29
- **(D)** 28

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 31**

**Detailed Solution:**

$4x^2+8x+3 = (2x+1)(2x+3)$ and $4x+6 = 2(2x+3)$.
$I(x) = \frac{3}{4}\int \frac{du}{u^{3/2}\sqrt{u-2}}$ where $u = 2x+3$.
Substituting $u = 2\sec^2\phi$: $I(x) = \frac{3}{4}\sin\phi + C = \frac{3}{4}\sqrt{\frac{2x+1}{2x+3}} + C$.
$I(0) = \frac{3}{4}\sqrt{\frac{1}{3}} + C = \frac{\sqrt{3}}{4} + C = \frac{\sqrt{3}}{4} + 20 \Rightarrow C = 20$.
$I\left(\frac{1}{2}\right) = \frac{3}{4}\sqrt{\frac{2}{4}} + 20 = \frac{3}{4\sqrt{2}} + 20 = \frac{3\sqrt{2}}{8} + 20$.
$a = 3, b = 8, c = 20$, $\gcd(3,8) = 1$. $a+b+c = 31$.

</details>

---

### Q4. JEE Main 2026 (22 January Shift 1)

*Type:* `numerical` | *Level:* `3`

If $\int(\sin x)^{\frac{-11}{2}}(\cos x)^{\frac{-5}{2}} d x=$ $-\frac{p_{1}}{q_{1}}(\cot x)^{\frac{9}{2}}-\frac{p_{2}}{q_{2}}(\cot x)^{\frac{5}{2}}-\frac{p_{3}}{q_{3}}(\cot x)^{\frac{1}{2}}+\frac{p_{4}}{q_{4}}(\cot x)^{\frac{-3}{2}}+\mathrm{C}$, where $p_{i}$ and $q_{i}$ are positive integers with $\operatorname{gcd}\left(p_{i}, q_{i}\right)=1$ for $i=1,2,3,4$ and C is the constant of integration, then $\frac{15 p_{1} p_{2} p_{3} p_{4}}{q_{1} q_{2} q_{3} q_{4}}$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

$\int \sin^{-11/2}x\cos^{-5/2}x\,dx$.
Since $m+n = -8$ (negative even), substitute $t = \cot x$, $dx = \frac{-dt}{1+t^2}$.
Integral becomes $-\int \frac{(1+t^2)^3}{t^{5/2}}dt = -\int(t^{-5/2}+3t^{-1/2}+3t^{3/2}+t^{7/2})dt$.
$= \frac{2}{3}t^{-3/2} - 6t^{1/2} - \frac{6}{5}t^{5/2} - \frac{2}{9}t^{9/2} + C$.
Comparing: $\frac{p_1}{q_1} = \frac{2}{9}$, $\frac{p_2}{q_2} = \frac{6}{5}$, $\frac{p_3}{q_3} = \frac{6}{1}$, $\frac{p_4}{q_4} = \frac{2}{3}$.
$\frac{15p_1p_2p_3p_4}{q_1q_2q_3q_4} = \frac{15 \cdot 2 \cdot 6 \cdot 6 \cdot 2}{9 \cdot 5 \cdot 1 \cdot 3} = \frac{2160}{135} = 16$.

</details>

---

### Q5. JEE Main 2025 (7 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If $\begin{aligned} \int\left(\frac{1}{x}+\frac{1}{x^3}\right) & \left(\sqrt[23]{3 x^{-24}+x^{-26}}\right) d x \\ & =-\frac{\alpha}{3(\alpha+1)}\left(3 x^\beta+x^\gamma\right)^{\frac{\alpha+1}{\alpha}}+C, x \gt 0,\end{aligned}$ $(\alpha, \beta, \gamma \in Z)$, where $C$ is the constant of integration, then $\alpha+\beta+\gamma$ is equal to ________ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

$\begin{aligned} & \int\left(\frac{1}{\mathrm{x}^2}+\frac{1}{\mathrm{x}^4}\right)\left(\frac{3}{\mathrm{x}}+\frac{1}{\mathrm{x}^3}\right)^{\frac{1}{23}} \mathrm{dx} \\ & \text { using } \mathrm{t}=\frac{3}{\mathrm{x}}+\frac{1}{\mathrm{x}^3} \Rightarrow \mathrm{dt}=-3\left(\frac{1}{\mathrm{x}^2}+\frac{1}{\mathrm{x}^4}\right) \mathrm{dx} \\ & \int \frac{\mathrm{t}^{1 / 23} \mathrm{dt}}{-3}=\frac{\mathrm{t}^{24 / 23}}{\left(\frac{24}{23}\right)(-3)}+C \\ & \Rightarrow \alpha=23 \beta=-1 \gamma=-3 \\ & \alpha+\beta+\gamma=19\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (4 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\int \frac{\left(\sqrt{1+x^2}+x\right)^{10}}{\left(\sqrt{1+x^2}-x\right)^9} d x=$
$\frac{1}{m}\left(\left(\sqrt{1+x^2}+x\right)^n\left(n \sqrt{1+x^2}-x\right)\right)+C \text { where } C$
is the constant of integration and $m, n \in N$, then $\mathrm{m}+\mathrm{n}$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **379**

**Detailed Solution:**

rationalise
$\begin{aligned}
& \Rightarrow \int \frac{\left(\sqrt{1+x^2}+x\right)^{10}}{\left(\sqrt{1+x^2}-x\right)^9} \times \frac{\left(\sqrt{1+x^2}+x\right)^9}{\left(\sqrt{1+x^2}+x\right)^9} d x \\
& \Rightarrow \int \frac{\left(\sqrt{1+x^2}+x\right)^{19}}{1} d x
\end{aligned}$
Put $\sqrt{1+\mathrm{x}^2}+\mathrm{x}=\mathrm{t}$
$\left(\frac{\mathrm{x}}{\sqrt{1+\mathrm{x}^2}}+1\right) \mathrm{dx}=\mathrm{dt}$
$\mathrm{dx}=\frac{\mathrm{dt}}{\mathrm{t}} \sqrt{1+\mathrm{x}^2}$
Now as $\sqrt{1+\mathrm{x}^2}+\mathrm{x}=\mathrm{t}$
$\begin{aligned}
& \text { so } \sqrt{1+\mathrm{x}^2}-\mathrm{x}=\frac{1}{\mathrm{t}} \\
& \therefore \sqrt{1+\mathrm{x}^2}=\frac{1}{2}\left(\mathrm{t}+\frac{1}{\mathrm{t}}\right)
\end{aligned}$
Thus $I=\int \mathrm{t}^{19} \cdot \frac{\mathrm{dt}}{\mathrm{t}} \cdot \frac{1}{2}\left(\mathrm{t}+\frac{1}{\mathrm{t}}\right)$
$\begin{aligned}
& \Rightarrow \frac{1}{2} \int\left(\mathrm{t}^{19}+\mathrm{t}^{17}\right) \mathrm{dt} \\
& =\frac{1}{2}\left(\frac{\mathrm{t}^{20}}{20}+\frac{\mathrm{t}^{18}}{18}\right)+\mathrm{C} \\
& =\frac{\mathrm{t}^{19}}{360}\left[9 \mathrm{t}+\frac{10}{\mathrm{t}}\right]+\mathrm{C} \\
& =\frac{\mathrm{t}^{19}}{360}\left[9\left(\mathrm{t}+\frac{1}{\mathrm{t}}\right)+\frac{1}{\mathrm{t}}\right]+\mathrm{C} \\
& \Rightarrow \frac{\left(\sqrt{1+\mathrm{x}^2}+\mathrm{x}\right)^{19}}{360}\left[9\left(2 \sqrt{1+\mathrm{x}^2}\right)+\left(\sqrt{1+\mathrm{x}^2}-\mathrm{x}\right)\right]+\mathrm{C} \\
& \Rightarrow \frac{\left(\sqrt{1+\mathrm{x}^2}+\mathrm{x}\right)^{19}}{360}\left[19 \sqrt{1+\mathrm{x}^2}-\mathrm{x}\right]+\mathrm{C} \\
& \therefore \mathrm{~m}=360, \mathrm{n}=19 \\
& \therefore \mathrm{~m}+\mathrm{n}=379
\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\int x^3 \sqrt{3-x^2} d x$. If $5 f(\sqrt{2})=-4$, then $f(1)$ is equal to

**Options:**

- **(A)** $-\frac{2 \sqrt{2}}{5}$
- **(B)** $-\frac{8 \sqrt{2}}{5}$
- **(C)** $-\frac{4 \sqrt{2}}{5}$
- **(D)** $-\frac{6 \sqrt{2}}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{6 \sqrt{2}}{5}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } 3-x^2=t^2 \\ & +x d x=-t d t \\ & f(x)=\int\left(3-t^2\right) \cdot t(-t d t)+c \\ & =\int\left(\mathrm{t}^4-3 \mathrm{t}^2\right) \mathrm{dt}+\mathrm{c} \\ & =\frac{\mathrm{t}^5}{5}-\mathrm{t}^3+\mathrm{c} \\ & \mathrm{f}(\mathrm{x})=\frac{\left(3-\mathrm{x}^2\right)^{5 / 2}}{5}-\left(3-\mathrm{x}^2\right)^{3 / 2}+\mathrm{c} \\ & \mathrm{f}(\sqrt{2})=\frac{1}{5}-1+\mathrm{c}=-\frac{4}{5}\end{aligned}$
$\begin{aligned} & \mathrm{c}=0 \\ & \mathrm{f}(1)=\frac{2^{5 / 2}}{5}-2^{3 / 2} \\ & =2^{1 / 2}\left(\frac{4}{5}-2\right) \\ & \mathrm{f}(1)-\frac{-6 \sqrt{2}}{5}\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\int \frac{2 x^2+5 x+9}{\sqrt{x^2+x+1}} \mathrm{~d} x=x \sqrt{x^2+x+1}+\alpha \sqrt{x^2+x+1}+\beta \log _e\left|x+\frac{1}{2}+\sqrt{x^2+x+1}\right|+\mathrm{C}$, where $C$ is the constant of integration, then $\alpha+2 \beta$ is equal to $\qquad$ _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

$\begin{aligned} & 2 \mathrm{x}^2+5 \mathrm{x}+9=\mathrm{A}\left(\mathrm{x}^2+\mathrm{x}+1\right)+\mathrm{B}(2 \mathrm{x}+1)+\mathrm{C} \\ & \mathrm{A}=2 \quad \mathrm{~B}=\frac{3}{2} \quad \mathrm{C}=\frac{11}{2} \\ & 2 \int \sqrt{\mathrm{x}^2+\mathrm{x}+1} \mathrm{dx}+\frac{3}{2} \int \frac{2 \mathrm{x}+1}{\sqrt{\mathrm{x}^2+\mathrm{x}+1}} \mathrm{dx}+\frac{11}{2} \int \frac{\mathrm{dx}}{\sqrt{\mathrm{x}^2+\mathrm{x}+1}} \\ & 2 \int \sqrt{\left(\mathrm{x}+\frac{1}{2}\right)^2+\left(\frac{\sqrt{3}}{2}\right)^2} \mathrm{dx}+3 \sqrt{\mathrm{x}^2+\mathrm{x}+1}+\frac{11}{2} \int \frac{\mathrm{dx}}{\sqrt{\left(\mathrm{x}+\frac{1}{2}\right)^2+\left(\frac{\sqrt{3}}{2}\right)^2}} \\ & 2\left(\frac{\mathrm{x}+\frac{1}{2}}{2} \sqrt{\mathrm{x}^2+\mathrm{x}+1}+\frac{3}{8} \ln \left(\mathrm{x}+\frac{1}{2}+\sqrt{\mathrm{x}^2+\mathrm{x}+1}\right)\right)+3 \sqrt{\mathrm{x}^2+\mathrm{x}+1} \\ & +\frac{11}{2} \ell \mathrm{n}\left(\mathrm{x}+\frac{1}{2}+\sqrt{\mathrm{x}^2+\mathrm{x}+1}\right)+\mathrm{C} \\ & \alpha=\frac{7}{2} \quad\beta=\frac{25}{4} \\& \alpha+2 \beta=16 \\ &  \end{aligned}$

</details>

---

### Q9. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\int \frac{2-\tan x}{3+\tan x} \mathrm{~d} x=\frac{1}{2}\left(\alpha x+\log _{\mathrm{e}}|\beta \sin x+\gamma \cos x|\right)+C$, where $C$ is the constant of integration. Then $\alpha+\frac{\gamma}{\beta}$ is equal to :

**Options:**

- **(A)** 7
- **(B)** 4
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4**

**Detailed Solution:**

$\begin{aligned} & \int \frac{2-\tan x}{3+\tan x} d x=\int \frac{2 \cos x-\sin x}{3 \cos x+\sin x} d x \\ & 2 \cos x-\sin x=A(3 \cos x+\sin x)+B(\cos x-3 \sin x) \\ & 3 A+B=2 \\ & A-3 B=-1\end{aligned}$
$\begin{aligned} & \Rightarrow A=\frac{1}{2}, B=\frac{1}{2} \\ & \therefore \int \frac{2 \cos x-\sin x}{3 \cos x+\sin x} d x \\ & =\frac{x}{2}+\frac{1}{2} \ln |3 \cos x+\sin x|+C \\ & =\frac{1}{2}(x+\ln |3 \cos x+\sin x|)+C \\ & =\frac{1}{2}(\alpha x+\ln |\beta \sin x+\gamma \cos x|)+C \\ & \alpha=1, \beta=1, \gamma=3 \\ & \therefore \alpha+\frac{\gamma}{\beta}=1+\frac{3}{1}=4\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\int \frac{1}{\sqrt[5]{(x-1)^4(x+3)^6}} \mathrm{~d} x=\mathrm{A}\left(\frac{\alpha x-1}{\beta x+3}\right)^B+\mathrm{C}$, where $\mathrm{C}$ is the constant of integration, then the value of $\alpha+\beta+20 \mathrm{AB}$ is__________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

$\begin{aligned} & \int \frac{1}{\sqrt[5]{(x-1)^4(x+3)^6}} d x=A\left(\frac{\alpha x-1}{\beta x+3}\right)^B+C \\ & I=\int \frac{1}{(x-1)^{4 / 5}(x+3)^{6 / 5}} d x \\ & I=\int \frac{1}{\left(\frac{x-1}{x+3}\right)^{4 / 5}(x+3)^2} d x \\ & \left(\frac{x-1}{x+3}\right)=t \Rightarrow \frac{4}{(x+3)^2} d x=d t \quad t^{-4 / 5+1} \\ & I=\frac{1}{4} \int \frac{1}{t^{4 / 5}} d t=\frac{1}{4} \frac{t^{1 / 5}}{1 / 5}+c \\ & I=\frac{5}{4}\left(\frac{x-1}{x+3}\right)^{1 / 5}+C \\ & A=\frac{5}{4} \quad \alpha=\beta=1 \quad B=\frac{1}{5} \\ & \alpha+\beta+20 A B=2+20 \times \frac{5}{4} \times \frac{1}{5}=7\end{aligned}$

</details>

---

### Q11. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $I(x)=\int \frac{6}{\sin ^2 x(1-\cot x)^2} d x$. If $I(0)=3$, then $I\left(\frac{\pi}{12}\right)$ is equal to

**Options:**

- **(A)** $2 \sqrt{3}$
- **(B)** $\sqrt{3}$
- **(C)** $3 \sqrt{3}$
- **(D)** $6 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3 \sqrt{3}$**

**Detailed Solution:**

$I(x)=\int \frac{6 d x}{\sin ^2 x(1-\cot x)^2}=\int \frac{6 \operatorname{cosec}^2 x d x}{(1-\cot x)^2}$
Put $1-\cot x=t$
$\operatorname{cosec}^2 \mathrm{xdx}=\mathrm{dt}$
$\begin{aligned} & I=\int \frac{6 d t}{t^2}=\frac{-6}{t}+c \\ & I(x)=\frac{-6}{1-\cot x} c, c=3 \\ & I(x)=3-\frac{6}{1-\cot x}, I\left(\frac{\pi}{12}\right)=3-\frac{6}{1-(2+\sqrt{3})} \\ & I\left(\frac{\pi}{12}\right)=3+\frac{6}{\sqrt{3}+1}=3+\frac{6(\sqrt{3}-1)}{2}=3 \sqrt{3}\end{aligned}$

</details>

---

### Q12. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{1}{\mathrm{a}^2 \sin ^2 x+\mathrm{b}^2 \cos ^2 x} \mathrm{~d} x=\frac{1}{12} \tan ^{-1}(3 \tan x)+$ constant, then the maximum value of $\mathrm{a} \sin x+\mathrm{b} \cos x$, is :

**Options:**

- **(A)** $\sqrt{40}$
- **(B)** $\sqrt{41}$
- **(C)** $\sqrt{39}$
- **(D)** $\sqrt{42}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{40}$**

**Detailed Solution:**

$\begin{aligned}
& \int \frac{\sec ^2 x d x}{a^2 \tan ^2 x+b^2} \\
& \text { let } \tan x=t \\
& \sec ^2 d x=d t \\
& \int \frac{d t}{a^2 t^2+b^2} \\
& \frac{1}{a^2} \int \frac{d t}{t^2+\left(\frac{b}{a}\right)^2} \\
& \frac{1}{a^2} \frac{1}{\frac{b}{a}} \tan ^{-1}\left(\frac{t}{b} a\right)+c \\
& \frac{1}{a b} \tan ^{-1}\left(\frac{\alpha}{b} \tan x\right)+c
\end{aligned}$
on comparing $\frac{\mathrm{a}}{\mathrm{b}}=3$
$\begin{aligned}
& a b=12 \\
& a=6, b=2
\end{aligned}$
maximum value of
$6 \sin x+2 \cos x \text { is } \sqrt{40}$

</details>

---

### Q13. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\int \operatorname{cosec}^5 x d x=\alpha \cot x \operatorname{cosec} x\left(\operatorname{cossc}^2 x+\frac{3}{2}\right)+\beta \log _\epsilon\left|\tan \frac{x}{2}\right|+C$
where $\alpha, \beta \in \mathbb{R}$ and $\mathrm{C}$ is the constant of integration, then the value of $8(\alpha+\beta)$ equals _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

$\int \operatorname{cosec}^3 x \cdot \operatorname{cosec}^2 x d x=I$
By applying integration by parts
$\begin{aligned}
& I=-\cot x \operatorname{cosec}^3 x+\int \cot x\left(-3 \operatorname{cosec}^2 x \cot x \operatorname{cosec} x\right) d x \\
& I=-\cot x \operatorname{cosec}^3 x-3 \int \operatorname{cosec}^3 x\left(\operatorname{cosec}^2 x-1\right) d x \\
& I=-\cot x \operatorname{cosec}^3 x-3 I+3 \int \operatorname{cosec}^3 x d x
\end{aligned}$
let
$\begin{aligned}
& I_1=\int \operatorname{cosec}^3 x d x=-\operatorname{cosec} x \cot x-\int \cot ^2 x \operatorname{cosec} x d x \\
& I_1=-\operatorname{cosec} x \cot x-\int\left(\operatorname{cosec}^2 x-1\right) \operatorname{cosec} x d x
\end{aligned}$
$\begin{aligned} & 2 I_1=-\operatorname{cosec} x \cot x+\ln \left|\tan \frac{x}{2}\right| \\ & I_1=-\frac{1}{2} \operatorname{cosec} x \cot x+\frac{1}{2} \ln \left|\tan \frac{x}{2}\right| \\ & 4 I=-\cot x \operatorname{cosec}^3 x-\frac{3}{2} \operatorname{cosec} x \cot x+\frac{3}{2} \ln \left|\tan \frac{x}{2}\right|+4 c \\ & I=-\frac{1}{4} \operatorname{cosec} x \cot x\left(\operatorname{cosec}^2 x+\frac{3}{2}\right)+\frac{3}{8} \ln \left|\tan \frac{x}{2}\right|+c \\ & \therefore \alpha=\frac{-1}{4}, \beta=\frac{3}{8} \rightarrow 8(\alpha+\beta)=1\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∫</mo><mfrac><mrow><msup><mi>sin</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi></mrow><msqrt><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>sin</mi><mo>(</mo><mi>x</mi><mo>-</mo><mi>θ</mi><mo>)</mo></msqrt></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>A</mi><msqrt><mi>cos</mi><mi>θ</mi><mi>tan</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>θ</mi></msqrt><mo>+</mo><mi>B</mi><msqrt><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>sin</mi><mi>θ</mi><mi>cot</mi><mi>x</mi></msqrt><mo>+</mo><mi>C</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the integration constant, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>cosec</mo><mo>(</mo><mn>2</mn><mi>θ</mi><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>sec</mi><mi>θ</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>sec</mi><mi>θ</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>cosec</mo><mo>(</mo><mn>2</mn><mi>θ</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>cosec</mo><mo>(</mo><mn>2</mn><mi>θ</mi><mo>)</mo></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><msup><mi>sin</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi></mrow><msqrt><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>sin</mi><mo>(</mo><mi>x</mi><mo>-</mo><mi>θ</mi><mo>)</mo></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><msup><mi>sin</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi></mrow><msqrt><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>(</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>cos</mi><mi>x</mi><mi>sin</mi><mi>θ</mi><mo>)</mo></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><msup><mi>sin</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi></mrow><msqrt><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>(</mo><mi>tan</mi><mi>x</mi><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>sin</mi><mi>θ</mi><mo>)</mo></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><msup><mi>sin</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><msqrt><mi>tan</mi><mi>x</mi><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>sin</mi><mi>θ</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mo>∫</mo><mfrac><mrow><msup><mi>cos</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mi>x</mi><msqrt><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>cot</mi><mi>x</mi><mi>sin</mi><mi>θ</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mn>1</mn><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><msqrt><mi>tan</mi><mi>x</mi><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>sin</mi><mi>θ</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mo>∫</mo><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msqrt><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>cot</mi><mi>x</mi><mi>sin</mi><mi>θ</mi></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><msqrt><mi>tan</mi><mi>x</mi><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>sin</mi><mi>θ</mi></msqrt></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mo>∫</mo><mfrac><mrow><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi></mrow><msqrt><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>cot</mi><mi>x</mi><mi>sin</mi><mi>θ</mi></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced close="}" open="{"><mi>let</mi></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>sin</mi><mi>θ</mi><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>θ</mi><mo>×</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mrow><mi>cos</mi><mi>θ</mi></mrow></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>cot</mi><mi>x</mi><mi>sin</mi><mi>θ</mi><mo>=</mo><msup><mi>z</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>cosec</mi><mn>2</mn></msup><mi>x</mi><mo>×</mo><mi>sin</mi><mi>θ</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>z</mi><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>z</mi><mi>d</mi><mi>z</mi></mrow><mrow><mi>sin</mi><mi>θ</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mrow><mi>cos</mi><mi>θ</mi><mo>×</mo><mi>t</mi></mrow></mfrac><mo>+</mo><mo>∫</mo><mfrac><mrow><mn>2</mn><mi>z</mi><mi>d</mi><mi>z</mi></mrow><mrow><mi>sin</mi><mi>θ</mi><mo>×</mo><mi>z</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfenced><mrow><mi>sec</mi><mi>θ</mi></mrow></mfenced><mo>∫</mo><mfenced><mn>1</mn></mfenced><mi>d</mi><mi>t</mi><mo>+</mo><mi>cosec</mi><mi>θ</mi><mo>∫</mo><mfenced><mn>1</mn></mfenced><mi>d</mi><mi>z</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>=</mo><mn>2</mn><mi>sec</mi><mi>θ</mi><msqrt><mi>tan</mi><mi>x</mi><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>sin</mi><mi>θ</mi></msqrt><mo>+</mo><mn>2</mn><mo>cosec</mo><mi>θ</mi><msqrt><mi>cos</mi><mi>θ</mi><mo>-</mo><mi>cot</mi><mi>x</mi><mi>sin</mi><mi>θ</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>×</mo><mi>B</mi><mo>=</mo><mn>4</mn><mi>sec</mi><mi>θ</mi><mi>cosec</mi><mi>θ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>×</mo><mi>B</mi><mo>=</mo><mfrac><mn>2</mn><mn>2</mn></mfrac><mo>×</mo><mfrac><mn>4</mn><mrow><mi>sin</mi><mi>θ</mi><mi>cos</mi><mi>θ</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>×</mo><mi>B</mi><mo>=</mo><mn>8</mn><mo>cosec</mo><mn>2</mn><mi>θ</mi></math></p>

</details>

---

### Q15. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∫</mo><mfrac><mrow><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>8</mn></msup><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mi>dx</mi></mrow><mrow><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>12</mn></msup><mo>+</mo><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><msup><mfenced close="|" open="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi mathvariant="normal">C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><msup><mfenced><mfenced close="|" open="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfenced></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi mathvariant="normal">C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfenced close="|" open="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfenced></mfenced><mo>+</mo><mi mathvariant="normal">C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><msup><mfenced><mfenced close="|" open="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfenced></mfenced><mn>3</mn></msup><mo>+</mo><mi mathvariant="normal">C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><msup><mfenced close="|" open="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi mathvariant="normal">C</mi></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><msup><mi mathvariant="normal">x</mi><mn>8</mn></msup><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow><mrow><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>12</mn></msup><mo>+</mo><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfrac><mi>dx</mi></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>·</mo><mfenced><mrow><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>4</mn></msup></mfrac></mrow></mfenced><mi>dx</mi><mo>=</mo><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>6</mn></msup><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>x</mi><mn>6</mn></msup></mfrac></mstyle><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>·</mo><mfenced><mrow><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>4</mn></msup></mfrac></mrow></mfenced><mi>dx</mi><mo>=</mo><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msup><mi mathvariant="normal">x</mi><mn>6</mn></msup><mrow><msup><mi mathvariant="normal">x</mi><mn>12</mn></msup><mo>+</mo><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>·</mo><mfrac><mrow><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>6</mn></msup><mo>-</mo><mn>3</mn></mrow><msup><mi mathvariant="normal">x</mi><mn>4</mn></msup></mfrac><mi>dx</mi><mo>=</mo><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>8</mn></msup><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>12</mn></msup><mo>+</mo><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>dx</mi><mo>=</mo><mfrac><mi>dt</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>∫</mo><mfrac><mn>1</mn><mi mathvariant="normal">t</mi></mfrac><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>log</mi><mo>|</mo><mi mathvariant="normal">t</mi><mo>|</mo><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfenced><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>=</mo><mi>log</mi><msup><mfenced close="|" open="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfrac></mrow></mfenced></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p>Hence optin <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">A</mi></mfenced></math> is correct</p>

</details>

---

### Q16. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>3</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msqrt><mn>4</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>&#60;</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **28**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mn>3</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msqrt><mn>4</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>,</mo><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mfenced><mrow><mn>3</mn><mo>+</mo><mfrac><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow></mfenced><msqrt><mn>4</mn><mo>-</mo><mfrac><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></msqrt></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>t</mi><mo>&#160;</mo><mi>d</mi><mi>t</mi></mrow><mrow><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><msqrt><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></msqrt></mrow></mfrac></math></p><p>Now let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mo>=</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>&#8658;</mo><mn>8</mn><mi>t</mi><mo>&#160;</mo><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>&#955;</mi><mo>&#160;</mo><mi>d</mi><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>&#955;</mi><mo>&#160;</mo><mi>d</mi><mi>&#955;</mi></mrow><mrow><mn>4</mn><mo>&#183;</mo><mfenced><mrow><mn>3</mn><mfenced><mfrac><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow><mn>4</mn></mfrac></mfenced><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#183;</mo><mi>&#955;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>&#955;</mi></mrow><mrow><mn>3</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mo>+</mo><mn>16</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>&#955;</mi></mrow><mrow><mn>3</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mn>25</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>&#955;</mi></mrow><mrow><msup><mi>&#955;</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>25</mn><mn>3</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>5</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>&#955;</mi></mrow><mn>5</mn></mfrac></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>15</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><msqrt><mfenced><mrow><mn>4</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></msqrt></mrow><mrow><mn>5</mn><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>&#960;</mi></mrow><mn>30</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>15</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>5</mn></mfrac></mfenced><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>15</mn></mfrac><mo>&#215;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>15</mn></mfrac><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>5</mn></mfrac></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>15</mn></mfrac><mfenced><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>5</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>15</mn></mfrac><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>5</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>15</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>5</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>5</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced></math></p><p>Now comparing with given value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>28</mn></math></p></blockquote>

</details>

---

### Q17. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><msqrt><mfrac><mrow><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mi>x</mi></mfrac></msqrt><mo>&#160;</mo><mi>d</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mn>9</mn></mfenced><mo>=</mo><mn>12</mn><mo>+</mo><mn>7</mn><msub><mi>log</mi><mi>e</mi></msub><mn>7</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>&#945;</mi><mo>+</mo><mn>7</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>4</mn></msup></math> is equal to _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **64**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><msqrt><mfrac><mrow><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mi>x</mi></mfrac></msqrt><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p>Now let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>7</mn></mrow><mi>x</mi></mfrac><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>&#8658;</mo><mo>-</mo><mfrac><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>t</mi><mo>&#160;</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>14</mn><mi>t</mi></mrow><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>14</mn><mo>&#8747;</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>14</mn><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mstyle><mo>-</mo><mn>2</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>14</mn></mrow><mn>2</mn></mfrac><mo>&#8747;</mo><mfenced close="]" open="["><mrow><mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mstyle></mrow></mfenced><mrow><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>t</mi></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mstyle></mrow></mfenced><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>t</mi></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>7</mn><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>ln</mi><mfenced open="|" close="|"><mfrac><mrow><mi>t</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>t</mi></mfrac></mstyle><mo>-</mo><mn>2</mn></mrow><mrow><mi>t</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>t</mi></mfrac></mstyle><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mrow><mi>t</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>t</mi></mfrac></mstyle></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mi>t</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mn>9</mn></mfenced><mo>=</mo><mo>&#160;</mo><mn>12</mn><mo>+</mo><mn>7</mn><mo>&#215;</mo><mi>ln</mi><mn>7</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>7</mn></mrow><mn>4</mn></mfrac><mi>ln</mi><msup><mfenced><mfrac><mn>1</mn><mn>7</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mn>7</mn><mo>&#215;</mo><mfrac><mn>12</mn><mn>7</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mi>ln</mi><mn>7</mn></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>t</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>I</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac><mi>ln</mi><msup><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mn>7</mn><mo>&#215;</mo><mfrac><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mi>ln</mi><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mfrac><msup><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mn>7</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mi>ln</mi><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>7</mn><mo>&#160;</mo><mi>ln</mi><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mi>ln</mi><mn>7</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mi>ln</mi><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>=</mo><mn>64</mn></math></p>

</details>

---

### Q18. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>,</mo><mi>&#948;</mi><mo>&#8712;</mo><mi>&#8469;</mi></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mo>&#8747;</mo><mfenced><mrow><msup><mfenced><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mfenced><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><msup><mfenced><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mi>&#946;</mi><mi>x</mi></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mi>&#947;</mi></mfrac><msup><mfenced><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mrow><mi>&#948;</mi><mi>x</mi></mrow></msup><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mi>n</mi><mo>!</mo></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is constant of integration, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn><mi>&#947;</mi><mo>-</mo><mn>4</mn><mi>&#948;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><msup><mfenced><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mfenced><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>ln</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><msup><mfenced><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mi>&#946;</mi><mi>x</mi></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mi>&#947;</mi></mfrac><msup><mfenced><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mrow><mi>&#948;</mi><mi>x</mi></mrow></msup><mo>+</mo><mi>C</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mfenced><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><msup><mfenced><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>ln</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mi>ln</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfenced><mrow><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><msup><mfenced><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><msup><mfenced><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><msup><mfenced><mfrac><mi>x</mi><mi>e</mi></mfrac></mfenced><mrow><mi>&#946;</mi><mi>x</mi></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mi>&#947;</mi></mfrac><msup><mfenced><mfrac><mi>e</mi><mi>x</mi></mfrac></mfenced><mrow><mi>&#948;</mi><mi>x</mi></mrow></msup><mo>+</mo><mi>C</mi></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#947;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#948;</mi><mo>=</mo><mn>2</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mn>2</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn><mi>&#947;</mi><mo>-</mo><mn>4</mn><mi>&#948;</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn><mo>-</mo><mn>8</mn><mo>=</mo><mn>4</mn></math></p><p>Hence this is the required option. </p></blockquote>

</details>

---

### Q19. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>x</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mi>x</mi></msup></mrow></mfenced><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>x</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mi>x</mi></msup><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>x</mi></msup><mo>-</mo><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mi>x</mi></msup><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>x</mi></msup><msub><mi>log</mi><mn>2</mn></msub><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>x</mi></msup><msub><mi>log</mi><mn>2</mn></msub><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>x</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mi>x</mi></msup><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>x</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mi>x</mi></msup></mrow></mfenced><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p>Now, Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>x</mi></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><msub><mi>log</mi><mn>2</mn></msub><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>&#183;</mo><msub><mi>log</mi><mn>2</mn></msub><mi>e</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mi>t</mi><mo>&#183;</mo><msub><mi>log</mi><mn>2</mn></msub><mi>e</mi></math></p><p>On differentiating both sides we get :
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>x</mi><mo>&#183;</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p>Then solution is not possible as there is no proper substitution.</p><p>Note: This question was bonus in Jee Mains 2023 April session.</p></blockquote>

</details>

---

### Q20. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mn>1</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>e</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>e</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mi>ln</mi><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>+</mo><mi>ln</mi><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>ln</mi><mfenced><mfrac><mrow><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p>Also given,<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced close="]" open="["><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>C</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>I</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mn>0</mn><mo>+</mo><mi>C</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>ln</mi><mfenced><mfrac><mi>e</mi><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mi>ln</mi><mo>(</mo><mi>e</mi><mo>+</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mrow><mi>e</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mi>ln</mi><mfenced><mrow><mi>e</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p></blockquote>

</details>

---

### Q21. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msqrt><mi>sec</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><msqrt><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mfrac><mn>1</mn><mi>&#946;</mi></mfrac><mi>x</mi></mrow></mfenced></msqrt></mrow></mfenced></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math> constant, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msqrt><mi>sec</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><msqrt><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mfrac><mn>1</mn><mi>&#946;</mi></mfrac><mi>x</mi></mrow></mfenced></msqrt></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>.</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">S</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msqrt><mi>sec</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><msqrt><mi>sec</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mo>&#160;</mo><mi>x</mi></mrow><msqrt><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#160;</mo><mo>&#8658;</mo><mo>-</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><msqrt><mi>sec</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msqrt><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><msqrt><mi>sec</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mo>|</mo><msqrt><mn>2</mn></msqrt><mi>cos</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><msqrt><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></msqrt><mo>|</mo><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><mn>2</mn><mo>&#160;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><msqrt><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></msqrt><mo>&#183;</mo><msqrt><mn>2</mn><mo>&#160;</mo></msqrt><mi>cos</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><msqrt><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></msqrt><mo>&#183;</mo><msqrt><mn>1</mn><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></msqrt></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msqrt><mi>sec</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mrow><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><msqrt><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mfrac><mn>1</mn><mi>&#946;</mi></mfrac><mi>x</mi></mrow></mfenced></msqrt></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q22. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mfrac><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mrow></mfenced></mrow><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mfrac></mfenced><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mfrac><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></mfrac></mfenced><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mfrac><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></mfrac></mfenced><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mfrac><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mrow></mfenced></mrow><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mfrac><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mrow></mfenced></mrow><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mfrac></mfenced><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p>Multiplying by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math> in numerator and denominator, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mfenced><mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mstyle><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mfenced><mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>cos</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><mi>x</mi><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>sin</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mi>x</mi></mrow></mfenced><mrow><mn>2</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mfenced><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mo>-</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfenced><mrow><mn>2</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfrac><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mo>&#8747;</mo><mi>cosec</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mi>sec</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>tan</mi><mfrac><mrow><mi>x</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mstyle></mrow><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mfenced><mrow><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>tan</mi><mfrac><mstyle displaystyle="true"><mi>x</mi><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mstyle><mn>2</mn></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mi mathvariant="normal">&#960;</mi></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></mrow></mfenced></mrow><mrow><mi>tan</mi><mfenced><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p></blockquote>

</details>

---

### Q23. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi><mo>,</mo><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>&#183;</mo><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac><mi>tan</mi><mi>&#952;</mi><mfenced><mrow><mo>-</mo><mn>4</mn><mi>sin</mi><mi>&#952;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac><mfenced><mrow><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#8747;</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mi>tan</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mi>&#952;</mi><mo>+</mo><mi mathvariant="normal">c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mn>2</mn><mi>&#952;</mi><mo>-</mo><mi>tan</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mi>&#952;</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><munder><mrow><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><msqrt><mn>1</mn><mo>&#8722;</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow><mi>x</mi></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mi>c</mi></mrow><mo>&#9183;</mo></munder><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>g</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow><mi>x</mi></mfrac></mfenced><mo>+</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p>

</details>

---

### Q24. JEE Main 2021 (31 Aug Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mo>|</mo><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi><mo>|</mo><mo>+</mo><mi>&#946;</mi><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced open="|" close="|"><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>+</mo><mi>&#947;</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>tan</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi><mo>,</mo></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is constant of integration, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup></mrow></mfenced></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mo>|</mo><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi><mo>|</mo><mo>+</mo><mi>&#946;</mi><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced close="|" open="|"><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>x</mi><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>+</mo><mi>&#947;</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>tan</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>tan</mi><mi>x</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><msup><mi>tan</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>t</mi><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mi>t</mi><mrow><mo>(</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>)</mo><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi></math>
Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>t</mi><mrow><mo>(</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>)</mo><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mi>A</mi><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>B</mi><mi>t</mi><mo>+</mo><mi>C</mi></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mi>A</mi><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mo>(</mo><mi>B</mi><mi>t</mi><mo>+</mo><mi>C</mi><mo>)</mo><mo>(</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>-</mo><mi>t</mi><mfenced><mrow><mi>A</mi><mo>-</mo><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced><mo>+</mo><mi>A</mi><mo>+</mo><mi>C</mi></math></p><p>Comparing on both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mi>A</mi><mo>+</mo><mi>B</mi><mo>+</mo><mi>C</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>A</mi><mo>+</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p>Solving these equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced close="}" open="{"><mrow><mfrac><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mfrac><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8747;</mo><mfrac><mn>1</mn><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mi>d</mi><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8747;</mo><mfrac><mn>1</mn><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mi>d</mi><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>1</mn></mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>1</mn></mrow><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>tan</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, Comparing from both sides
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>
So <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><msup><mi>&#947;</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q25. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mn>1</mn><mroot><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>3</mn></msup><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mo>)</mo><mn>5</mn></msup></mrow><mn>4</mn></mroot></mfrac><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>x</mi></math> is equal to : (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mn>5</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>5</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi mathvariant="normal">C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi mathvariant="normal">C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mroot><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>3</mn></msup><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mo>)</mo><mn>5</mn></msup></mrow><mn>4</mn></mroot></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>4</mn></mfrac></mstyle></msup><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mo>)</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>4</mn></mfrac></mstyle></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><msup><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>4</mn></mfrac></mstyle></msup></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#160;</mo><mo>=</mo><mi>t</mi></math></p><p>Differentiate on both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>.</mo><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mfenced><mi>t</mi></mfenced><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>4</mn></mfrac></mstyle></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mfrac><msup><mi>t</mi><mrow><mstyle displaystyle="true"><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>4</mn></mfrac></mstyle><mo>+</mo><mn>1</mn></mrow></msup><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>4</mn></mfrac></mstyle></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mi>t</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mfenced><mfrac><mn>1</mn><mi>t</mi></mfrac></mfenced><mfrac bevelled="true"><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac bevelled="true"><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>C</mi></math></p>

</details>

---

### Q26. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>3</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>7</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>14</mn></mfrac><mfenced><mrow><mi>u</mi><mi>x</mi><mo>+</mo><mi>v</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>7</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>+</mo><mi>v</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>3</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mrow><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>7</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>3</mn></mrow><mrow><mn>4</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>7</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math>
Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>3</mn><mo>=</mo><mi>A</mi><mfenced><mrow><mn>8</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>+</mo><mi>B</mi><mfenced><mrow><mn>4</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>7</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>3</mn><mo>=</mo><mo>(</mo><mn>8</mn><mi>A</mi><mo>+</mo><mn>4</mn><mi>B</mi><mo>)</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>7</mn><mi>B</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>28</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfrac><mn>1</mn><mn>28</mn></mfrac><mfenced><mrow><mn>8</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mo>+</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mfenced><mrow><mn>4</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>7</mn></mrow></mfenced></mrow><mrow><mn>4</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>7</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>28</mn></mfrac><mi>ln</mi><mfenced open="|" close="|"><mrow><mn>4</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mi>x</mi><mo>+</mo><mi>C</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>28</mn></mfrac><mi>ln</mi><mo>&#8739;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced close=""><mrow><mn>4</mn><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>7</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>&#8739;</mo><mo>+</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mi>x</mi><mo>+</mo><mi>C</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>u</mi><mo>=</mo><mfrac><mn>13</mn><mn>2</mn></mfrac><mo>&#38;</mo><mi>v</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>u</mi><mo>+</mo><mi>v</mi><mo>=</mo><mfrac><mn>13</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>7</mn></math>

</details>

---

### Q27. JEE Main 2021 (27 Aug Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mi>a</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mi>b</mi><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the constant of integration, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>(</mo><msqrt><mn>3</mn></msqrt><mi>a</mi><mo>+</mo><mi>b</mi><mo>)</mo></math> is equal to _________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>4</mn></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>4</mn></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mi>P</mi><mi>u</mi><mi>t</mi><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">t</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>tan</mi><mo>&#160;</mo><mi>&#952;</mi></mrow></mfenced><mspace linebreak="newline"/><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mi>d</mi><mi>&#952;</mi></mrow><mrow><mstyle displaystyle="true"><mfrac><mn>9</mn><mn>16</mn></mfrac></mstyle><msup><mi>sec</mi><mn>4</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow><mn>9</mn></mfrac><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow><mn>9</mn></mfrac><mfenced close="]" open="["><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mi>sin</mi><mo>&#160;</mo><mn>2</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow><mn>9</mn></mfrac><mfenced close="]" open="["><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mn>3</mn></mfrac></mfenced><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>3</mn><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow><mn>9</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>15</mn></math></p>

</details>

---

### Q28. JEE Main 2021 (18 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>8</mn></msup><mo>+</mo><mn>7</mn><msup><mi>x</mi><mn>6</mn></msup></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>7</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>K</mi></mfrac><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>5</mn><msup><mi>x</mi><mn>8</mn></msup><mo>+</mo><mn>7</mn><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>14</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo>+</mo><mn>2</mn><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>5</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>-</mo><mn>7</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>8</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>7</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>7</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q29. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>cos</mi><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt></mrow><msqrt><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>6</mn></msqrt></mfrac><mi>d</mi><mi>x</mi></math> is equal to (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is a constant of integration)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>cos</mi><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt></mrow><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mn>2</mn><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></msqrt><mi>cos</mi><mi>t</mi></mrow><mrow><mn>2</mn><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn></msqrt></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mi>t</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><msqrt><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>5</mn></msqrt><mo>+</mo><mi>c</mi></math></p>

</details>

---

### Q30. JEE Main 2021 (16 Mar Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>For real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#948;</mi><mo>,</mo></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mi>x</mi></mfrac></mfenced></mrow><mrow><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mi>x</mi></mfrac></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>&#945;</mi><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mi mathvariant="normal">x</mi></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>&#946;</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>&#947;</mi><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mi mathvariant="normal">x</mi></mfrac></mfenced><mo>+</mo><mi>&#948;</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mi mathvariant="normal">x</mi></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">C</mi></math>  where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math> is an arbitrary constant, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi><mo>)</mo></math> is equal to ______ .<gwmw style="display:none;"></gwmw></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced></mrow></mfrac><mo>+</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><mi>y</mi><mo>,</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>t</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>z</mi></mrow><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mtext>e</mtext></msub><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>5</mn></msqrt><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac><mo>,</mo><mi>&#947;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mi>&#948;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac><mo>,</mo><mi>&#947;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msqrt><mn>5</mn></msqrt></mfrac><mo>,</mo><mi>&#948;</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mi>&#947;</mi><mo>+</mo><mi>&#948;</mi><mo>)</mo><mo>=</mo><mn>10</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q31. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi>e</mi><mrow><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>5</mn><msup><mi>e</mi><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mi>x</mi></mrow></msup></mrow><mrow><msup><mi>e</mi><mrow><mn>4</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup><mo>+</mo><mn>5</mn><msup><mi>e</mi><mrow><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup><mo>-</mo><mn>7</mn><msup><mi>e</mi><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup></mrow></mfrac><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, is equal to
(where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is a constant of integration)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mi mathvariant="normal">c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mi mathvariant="normal">c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mi mathvariant="normal">c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></msqrt><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mi mathvariant="normal">c</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi mathvariant="normal">e</mi><mrow><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>5</mn><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mi>x</mi></mrow></msup></mrow><mrow><msup><mi mathvariant="normal">e</mi><mrow><mn>4</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup><mo>+</mo><mn>5</mn><msup><mi mathvariant="normal">e</mi><mrow><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup><mo>-</mo><mn>7</mn><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>5</mn><msup><mfenced><mrow><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>7</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced></mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced></mfrac><mo>=</mo><mn>4</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>x</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p>

</details>

---

### Q32. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mi>&#952;</mi><mo>&#183;</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mfenced><mrow><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><msqrt><mn>2</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>6</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac><mi>d</mi><mi>&#952;</mi></math> is (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is a constant of integration)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>18</mn></mfrac><msup><mfenced open="[" close="]"><mrow><mn>11</mn><mo>-</mo><mn>18</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>9</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>18</mn></mfrac><msup><mfenced open="[" close="]"><mrow><mn>9</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi><mo>-</mo><mn>3</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mn>6</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>18</mn></mfrac><msup><mfenced open="[" close="]"><mrow><mn>11</mn><mo>-</mo><mn>18</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>9</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>6</mn></msup><mi>&#952;</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>18</mn></mfrac><msup><mfenced open="[" close="]"><mrow><mn>9</mn><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>6</mn></msup><mi>&#952;</mi><mo>-</mo><mn>3</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mn>6</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></msup><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>18</mn></mfrac><msup><mfenced open="[" close="]"><mrow><mn>11</mn><mo>-</mo><mn>18</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>9</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>6</mn></msup><mi>&#952;</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mi>&#952;</mi><mo>&#183;</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mfenced><mrow><msup><mi>sin</mi><mn>6</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><msqrt><mn>2</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>6</mn></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac><mi>d</mi><mi>&#952;</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mi>&#952;</mi><mo>.</mo><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi><mo>&#183;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#952;</mi><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mfenced><mrow><mn>2</mn><msup><mi>sin</mi><mn>4</mn></msup><mi>&#952;</mi><mo>+</mo><mn>3</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi>d</mi><mi>&#952;</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>t</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>t</mi><mn>5</mn></msup><mo>+</mo><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mi>t</mi></mrow></mfenced><mi>t</mi><msup><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>t</mi><mn>5</mn></msup><mo>+</mo><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mi>t</mi></mrow></mfenced><msup><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>t</mi><mn>5</mn></msup><mo>+</mo><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mi>t</mi></mrow></mfenced><msup><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>6</mn></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mi>d</mi><mi>t</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>t</mi><mn>6</mn></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup><mo>=</mo><msup><mi>u</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>12</mn><mfenced><mrow><msup><mi>t</mi><mn>5</mn></msup><mo>+</mo><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mi>t</mi></mrow></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>u</mi><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mfenced><msup><mi>u</mi><mn>2</mn></msup></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#183;</mo><mfrac><mrow><mn>2</mn><mi>u</mi><mi>d</mi><mi>u</mi></mrow><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><msup><mi>u</mi><mn>2</mn></msup><mn>6</mn></mfrac><mo>&#160;</mo><mi>d</mi><mi>u</mi><mo>=</mo><mfrac><msup><mi>u</mi><mn>3</mn></msup><mn>18</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>6</mn></msup><mo>+</mo><mn>3</mn><msup><mi>t</mi><mn>4</mn></msup><mo>+</mo><mn>6</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mn>18</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mi>sin</mi><mi>&#952;</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></math> will give</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>18</mn></mfrac><msup><mfenced open="[" close="]"><mrow><mn>11</mn><mo>-</mo><mn>18</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>9</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>6</mn></msup><mi>&#952;</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi>c</mi></math></p>

</details>

---

### Q33. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><msqrt><mn>8</mn><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></msqrt></mfrac><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mi>a</mi><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mo>&#160;</mo><mi>b</mi></mrow></mfrac></mfenced><mo>+</mo><mi>c</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is a constant of integration, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><msqrt><mn>8</mn><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></msqrt></mfrac><mi>d</mi><mi>x</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><msqrt><mn>9</mn><mo>-</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msqrt><mn>9</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>t</mi><mn>3</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow><mn>3</mn></mfrac></mfenced><mo>+</mo><mi>c</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q34. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>cos</mi><mi>&#952;</mi></mrow><mrow><mn>5</mn><mo>+</mo><mn>7</mn><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mi>d</mi><mi>&#952;</mi><mo>=</mo><msub><mo>Alog</mo><mi>e</mi></msub><mo>|</mo><mi>B</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>|</mo><mo>+</mo><mi>C</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>B</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo></mrow><mi>A</mi></mfrac></math> can be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>5</mn><mo>(</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>(</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn><mo>)</mo></mrow><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>(</mo><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>(</mo><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>cos</mi><mi>&#952;</mi></mrow><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>7</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mi>t</mi><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mi>t</mi><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mfrac><mn>5</mn><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mn>2</mn><mi>t</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>t</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>+</mo><mi>c</mi><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>+</mo><mi>c</mi></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>(</mo><mi>&#952;</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>5</mn><mo>(</mo><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>3</mn></mrow></mfrac></math></p>

</details>

---

### Q35. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><msqrt><mi>x</mi></msqrt><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><msqrt><mi>x</mi></msqrt><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>tan</mi><mi>&#952;</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>tan</mi><mi>&#952;</mi></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>.</mo><mn>2</mn><mi>tan</mi><mi>&#952;</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>tan</mi><mi>&#952;</mi></mrow><mrow><msup><mi>sec</mi><mn>4</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>.</mo><mn>2</mn><mi>tan</mi><mi>&#952;</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mn>2</mn><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi><mo>.</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mo>&#160;</mo><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#952;</mi><mo>&#8722;</mo><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mi>C</mi><mo>=</mo><mi>&#952;</mi><mo>&#8722;</mo><mfrac><mrow><mi>tan</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi></msqrt><mo>&#8722;</mo><mfrac><msqrt><mi>x</mi></msqrt><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>&#8722;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi>tan</mi><mo>&#8722;</mo></msup><msqrt><mn>3</mn></msqrt><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mrow><mn>1</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>&#8722;</mo><msup><mi>tan</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><msqrt><mn>1</mn></msqrt><mo>+</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>&#8722;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8722;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math></p>

</details>

---

### Q36. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mfenced><mfrac><mi>x</mi><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></mfenced><mn>2</mn></msup><mi>d</mi><mi>x</mi></math> is equal to, (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration):

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>-</mo><mfrac><mrow><mi>x</mi><mi>sec</mi><mi>x</mi></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mi>x</mi><mi>tan</mi><mi>x</mi></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>x</mi><mo>-</mo><mfrac><mrow><mi>x</mi><mi>tan</mi><mi>x</mi></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mi>x</mi><mi>sec</mi><mi>x</mi></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>-</mo><mfrac><mrow><mi>x</mi><mi>sec</mi><mi>x</mi></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mi>x</mi><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>&#8901;</mo><mfrac><mrow><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mtext>&#8201;</mtext><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>x</mi><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>&#8722;</mo><mo>&#8747;</mo><mfenced close="]" open="["><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mi>x</mi><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mtext>&#8201;</mtext><mi>d</mi><mi>x</mi></mrow></mfenced><mtext>&#8201;</mtext><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>x</mi><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mo>&#8722;</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mo>&#8747;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mtext>&#8201;&#8201;</mtext><mi>d</mi><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8757;&#8201;&#8201;&#8201;&#8201;</mtext><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mi>cos</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mo>&#8722;</mo><mn>1</mn></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mi>x</mi><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>sec</mi><mi>x</mi><mo>+</mo><mi>x</mi><mi>sec</mi><mi>x</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>sec</mi><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>x</mi><mi>sin</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8722;</mo><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mi>x</mi><mo>&#8722;</mo><mfrac><mrow><mi>x</mi><mi>sec</mi><mi>x</mi></mrow><mrow><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math></p>

</details>

---

### Q37. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msqrt><mi>x</mi></msqrt><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>A</mi><mfenced><mi>x</mi></mfenced><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced><mo>+</mo><mi>B</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">A</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced></math> can be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msqrt><mi>x</mi></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msqrt><mi>x</mi></msqrt></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><msqrt><mi>x</mi></msqrt><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><munder><munder><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced></mrow><mo>&#9183;</mo></munder><mi>I</mi></munder><munder><munder><mfenced><mn>1</mn></mfenced><mo>&#9183;</mo></munder><mrow><mi>I</mi><mi>I</mi></mrow></munder><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi></msqrt><mo>-</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>.</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mi>x</mi></msqrt></mrow></mfrac><mo>.</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi></msqrt><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>t</mi><mo>.</mo><mn>2</mn><mi>t</mi><mo>.</mo><mi>d</mi><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>C</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo></math>putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi></msqrt><mo>-</mo><mo>&#8747;</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi></msqrt><mo>-</mo><mi>t</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi></msqrt><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mi>x</mi></msqrt><mo>-</mo><msqrt><mi>x</mi></msqrt><mo>+</mo><mi>C</mi></math></p><p>Comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mi>x</mi></mfenced><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced><mo>+</mo><mi>B</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>C</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">A</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><msqrt><mi>x</mi></msqrt></mrow></mfenced></math></p>

</details>

---

### Q38. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>&#952;</mi></mrow><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mfenced separators="|"><mrow><mi>tan</mi><mn>2</mn><mi>&#952;</mi><mo>+</mo><mi>sec</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced></mrow></mfrac><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mi>tan</mi><mi>&#952;</mi><mo>+</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mi>f</mi><mfenced separators="|"><mi>&#952;</mi></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math> where <math><mi>C</mi></math> is a constant of integration, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>&#955;</mi><mo>,</mo><mi>f</mi><mfenced separators="|"><mi>&#952;</mi></mfenced></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>-</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>-</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>tan</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></mrow></mfrac><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi><mi>a</mi><mi>n</mi><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfrac><mi>d</mi><mi>&#952;</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>&#952;</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>t</mi><mo>+</mo><mn>2</mn><mi>ln</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mi>tan</mi><mi>&#952;</mi><mo>+</mo><mn>2</mn><mi>ln</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mo>&#160;</mo><mi>f</mi><mfenced separators="|"><mi>&#952;</mi></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mi>tan</mi><mi>&#952;</mi></math></p>

</details>

---

### Q39. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>7</mn></mfrac></mstyle></msup><msup><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow><mstyle displaystyle="true"><mfrac><mn>6</mn><mn>7</mn></mfrac></mstyle></msup></mrow></mfrac></math> is equal to: (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>7</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>7</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced><mfrac><mn>3</mn><mn>7</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>13</mn></mfrac><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced><mfrac><mrow><mo>-</mo><mn>13</mn></mrow><mn>7</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>7</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced><mfrac><mrow><mo>-</mo><mn>6</mn></mrow><mn>7</mn></mfrac></msup><mfrac><mn>1</mn><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Let <math><mfrac><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>7</mn></mrow></msup></math> ,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mn>7</mn><msup><mi>t</mi><mn>6</mn></msup><mi>d</mi><mi>t</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>t</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup><msup><mi>t</mi><mn>6</mn></msup><mi>d</mi><mi>t</mi><mo>=</mo><mi>t</mi><mo>+</mo><mi>C</mi></math></p>

</details>

---

### Q40. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mrow></mfrac><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mi>&#955;</mi></mfrac></msup><mo>+</mo><mi>c</mi></math>, where <math><mi>c</mi></math> is a constant of integration, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mi>f</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>9</mn><mn>8</mn></mfrac></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<p>Let, <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>=</mo><mi>t</mi></math> </p><p><math><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>t</mi><mn>3</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>6</mn></msup></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>t</mi><mn>7</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>6</mn></msup></mfrac></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>6</mn></msup></mfrac><mo>=</mo><msup><mi>r</mi><mn>3</mn></msup></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mn>7</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><msup><mi>r</mi><mn>2</mn></msup><mi>d</mi><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><msup><mi>r</mi><mn>2</mn></msup><mi>d</mi><mi>r</mi></mrow><msup><mi>r</mi><mn>2</mn></msup></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>r</mi><mo>+</mo><mi>c</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced separators="|"><mfrac><mrow><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>6</mn></msup><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi>c</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mi mathvariant="normal">c</mi><mn>2</mn></msup><mi>x</mi></math> and <math><mi>&#955;</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mi>f</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q41. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>)</mo><mi>&#160;</mi></math>, be constant.If the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>&#945;</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi>tan</mi><mi>&#945;</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>A</mi><mfenced separators="|"><mi>x</mi></mfenced><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>B</mi><mfenced separators="|"><mi>x</mi></mfenced><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>C</mi></math>, where C is a constant of integration, then the functions <math><mi>A</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> and <math><mi>B</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> are respectively

**Options:**

- **(A)** <math><mi>x</mi><mo>-</mo><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfenced></math>
- **(B)** <math><mi>x</mi><mo>+</mo><mi>α</mi></math> and <math><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mfenced open="|" close="|" separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>α</mi></mrow></mfenced></mrow></mfenced><mi> </mi></math>
- **(C)** <math><mi>x</mi><mo>+</mo><mi>α</mi></math> and <math><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mfenced open="|" close="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>α</mi></mrow></mfenced></mrow></mfenced></math>
- **(D)** <math><mi>x</mi><mo>-</mo><mi>α</mi></math> and <math><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mfenced open="|" close="|" separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>α</mi></mrow></mfenced></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>x</mi><mo>-</mo><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mi>tan</mi><mi>&#945;</mi></mrow><mrow><mi>tan</mi><mi>x</mi><mo>-</mo><mi>tan</mi><mi>&#945;</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mi>&#945;</mi></mrow><mrow><mi>cos</mi><mi>&#945;</mi></mrow></mfrac></mrow><mrow><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>sin</mi><mi>&#945;</mi></mrow><mrow><mi>cos</mi><mi>&#945;</mi></mrow></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#945;</mi><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#945;</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#945;</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#945;</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mi>&#945;</mi></mrow></mfenced></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>x</mi><mo>-</mo><mi>&#945;</mi><mo>)</mo></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi>cos</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>&#945;</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mo>(</mo><mi>x</mi><mo>-</mo><mi>&#945;</mi><mo>)</mo></mrow></mfrac><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>&#945;</mi><mi>cot</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>&#945;</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mi>sin</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mi>x</mi><mo>-</mo><mi>&#945;</mi><mo>)</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>&#945;</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mi>sin</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>
Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></mrow></mfenced></math>

</details>

---

### Q42. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mi>e</mi></msub><mfrac><msup><mrow><mo>(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></msup><mrow><mo>|</mo><msup><mi>x</mi><mn>3</mn></msup><mo>|</mo></mrow></mfrac><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mi>e</mi></msub><mfrac><mrow><mo>|</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn><mo>|</mo></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mfrac><mfenced separators="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mi>e</mi></msub><mfrac><mrow><mo>|</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn><mo>|</mo></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mfrac><mfenced separators="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Put, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><mi>t</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi>e</mi></msub><mfenced separators="|"><mi>t</mi></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi>e</mi></msub><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><msub><mi mathvariant="normal">g</mi><mi>e</mi></msub><mfenced close="|" open="|" separators="|"><mfrac><mfenced separators="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p></blockquote>

</details>

---

### Q43. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></mfenced><mo>+</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math>, then (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration)

**Options:**

- **(A)** <math><mi>A</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>27</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>9</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math><mi>A</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>81</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math><mi>A</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>54</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>9</mn><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math>
- **(D)** <math><mi>A</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>54</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>A</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>54</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced close="]" open="[" separators="|"><mrow><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>&#160;</mi><mo>&#8211;</mo><mn>1</mn><mo>=</mo><mn>3</mn><mi>tan</mi><mi>&#952;</mi><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>3</mn><msup><mi>sec</mi><mn>2</mn></msup><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mi mathvariant="normal">c</mi><mn>2</mn></msup><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></mrow><mrow><mn>81</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mi mathvariant="normal">c</mi><mn>4</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>27</mn></mfrac><mo>&#8747;</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>54</mn></mfrac><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mi>d</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>54</mn></mfrac><mfenced><mrow><mi>&#952;</mi><mo>+</mo><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>54</mn></mfrac><mfenced separators="|"><mrow><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the constant of integration.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>54</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></mfenced><mo>+</mo><mfrac><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></mfenced><mrow><mn>1</mn><mo>+</mo><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>54</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>3</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>10</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>54</mn></mfrac><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></math></p>

</details>

---

### Q44. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mi mathvariant="normal">c</mi><mn>2</mn></msup><mi>x</mi><mo>&#183;</mo><msup><mi>cot</mi><mfrac><mn>4</mn><mn>3</mn></mfrac></msup><mi>x</mi><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup><mi>x</mi><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></msup><mi>x</mi><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup><mi>x</mi><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><msup><mi mathvariant="normal">t</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup><mi>x</mi><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">n</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup><mi>x</mi><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<blockquote><p>Given integral can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></msup></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>t</mi><mrow><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></msup><mi>&#160;</mi><mi>d</mi><mi>t</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>C</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><msup><mi>t</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup><mfenced><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></mrow></mfenced></mfrac><mo>+</mo><mi>&#160;</mi><mi>C</mi></math></p><p>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><msup><mi>t</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mfrac><mo>+</mo><mi>&#160;</mi><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mn>3</mn><msup><mi>tan</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup><mi>x</mi><mo>+</mo><mi>C</mi><mo>.</mo></math></p></blockquote>

</details>

---

### Q45. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mi>&#160;</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration, then the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mrow></mfrac><mo>=</mo><mi>x</mi><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi>C</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>7</mn></msup><msup><mfenced separators="|"><mrow><mfrac><mn>1</mn><msup><mi>x</mi><mn>6</mn></msup></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mrow></mfrac></math></p><p>Put, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>6</mn></msup></mfrac><mo>+</mo><mn>1</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>t</mi><mo>=</mo><mo>-</mo><mfrac><mn>6</mn><msup><mi>x</mi><mn>7</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>t</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the constant of integration<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced separators="|"><mrow><mfrac><mn>1</mn><msup><mi>x</mi><mn>6</mn></msup></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mi>C</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></math></p>

</details>

---

### Q46. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mn>5</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi></math>  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced><mrow><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mfrac><mi mathvariant="normal">x</mi><mn>2</mn></mfrac></mrow></mfenced></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>sin</mi><mi>A</mi><mi>cos</mi><mi>B</mi><mo>+</mo><mi>cos</mi><mi>A</mi><mi>sin</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><mfrac><mrow><mfenced><mrow><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>2</mn><mi>sin</mi><mstyle displaystyle="true"><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced></mstyle><mi>cos</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow></mfenced><mi>cos</mi><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mrow><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mo>+</mo><mi>cos</mi><mo>&#160;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>4</mn><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mi>cos</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Using  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>cos</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>x</mi><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.</p>

</details>

---

### Q47. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>13</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>11</mn></msup></mrow><msup><mfenced separators="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></mfrac><mi>d</mi><mi>x</mi></math>, is equal to

**Options:**

- **(A)** <math><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>6</mn><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><mi>C</mi></math>
- **(B)** <math><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>12</mn></msup><msup><mfenced separators="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>12</mn></msup><mrow><mn>6</mn><msup><mfenced separators="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>12</mn></msup><mrow><mn>6</mn><msup><mfenced separators="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p>The given integral can be written as

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><mo>.</mo><mi>&#160;</mi><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup></mrow><msup><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>3</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfenced><mn>4</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p> (Dividing  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>16</mn></msup></math> to both numerator and denominator),</p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mn>2</mn><mo>+</mo><mn>3</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mo>-</mo><mn>6</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>-</mo><mn>4</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mn>3</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mn>4</mn></msup></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mfrac><msup><mi>t</mi><mrow><mo>-</mo><mn>4</mn><mo>+</mo><mn>1</mn></mrow></msup><mrow><mo>-</mo><mn>4</mn><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced><mfrac><mn>1</mn><msup><mi>t</mi><mn>3</mn></msup></mfrac></mfenced><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the constant of integration.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mn>6</mn><msup><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mn>3</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfenced><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mi>C</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>12</mn></msup><mrow><mn>6</mn><msup><mfenced separators="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mi>C</mi></math></p>

</details>

---

### Q48. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced><mi>lnx</mi></mfenced><mi>d</mi><mi>x</mi></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>2</mn></mfrac><mfenced separators="|"><mrow><mi>cos</mi><mfenced separators="|"><mi>lnx</mi></mfenced><mo>-</mo><mi>sin</mi><mfenced separators="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced separators="|"><mrow><mi>cos</mi><mfenced separators="|"><mi>lnx</mi></mfenced><mo>-</mo><mi>sin</mi><mfenced separators="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced separators="|"><mrow><mi>cos</mi><mfenced separators="|"><mi>lnx</mi></mfenced><mo>+</mo><mi>sin</mi><mfenced separators="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>2</mn></mfrac><mfenced separators="|"><mrow><mi>cos</mi><mfenced separators="|"><mi>lnx</mi></mfenced><mo>+</mo><mi>sin</mi><mfenced separators="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>2</mn></mfrac><mfenced separators="|"><mrow><mi>cos</mi><mfenced separators="|"><mi>lnx</mi></mfenced><mo>+</mo><mi>sin</mi><mfenced separators="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mfenced separators="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>

Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mi>e</mi><mi>t</mi></msup><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><msup><mi>e</mi><mi>t</mi></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>t</mi><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mi>cos</mi><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>t</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>t</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>t</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>t</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mi>cos</mi><mi>t</mi><mo>&#160;</mo><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mi>t</mi></msup><mfenced separators="|"><mrow><mi>cost</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>t</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the constant of integration.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mfenced separators="|"><mrow><mi>cos</mi><mfenced separators="|"><mi>lnx</mi></mfenced><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math>. 
 </p>

</details>

---

### Q49. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{x+1}{\sqrt{2 x-1}} \mathrm{~d} x=f(x) \sqrt{2 x-1}+\mathrm{C},$ where $\mathrm{C}$ is a constant

of integration, then $f(x)$ is equal to:

**Options:**

- **(A)** $\frac{1}{3}(x+1)$
- **(B)** $\frac{2}{3}(x+2)$
- **(C)** $\frac{2}{3}(x-4)$
- **(D)** $\frac{1}{3}(x+4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{3}(x+4)$**

**Detailed Solution:**

Let $I=\int \frac{x+1}{\sqrt{2 x-1}} d x$

Put $\sqrt{2 x-1}=t$

$\begin{array}{l}

\therefore \quad 2 x-1=t^{2} \Rightarrow d x=t d t \\

I=\int \frac{\left(t^{2}+3\right)}{2} d t=\frac{t^{3}}{6}+\frac{3 t}{2}+C \\

=\frac{(2 x-1)^{\frac{3}{2}}}{6}+\frac{3}{2}(2 x-1)^{\frac{1}{2}}+C \\

=\sqrt{2 x-1}\left(\frac{x+4}{3}\right)+C \\

=f(x) \cdot \sqrt{2 x-1}+C

\end{array}$

Hence, $f(x)=\frac{x+4}{3}$

</details>

---

### Q50. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{\sqrt{1-x^{2}}}{x^{4}} d x=A(\mathrm{x})\left(\sqrt{1-x^{2}}\right)^{m}+C,$ for a suitable chosen integer $\mathrm{m}$ and a function $\mathrm{A}(\mathrm{x})$, where $\mathrm{C}$ is a constant of integration, then $(\mathrm{A}(\mathrm{x}))^{\mathrm{m}}$ equals :

**Options:**

- **(A)** $\frac{-1}{27 x^{9}}$
- **(B)** $\frac{-1}{3 x^{3}}$
- **(C)** $\frac{1}{27 x^{6}}$
- **(D)** $\frac{1}{9 x^{4}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-1}{27 x^{9}}$**

**Detailed Solution:**

$A(x)\left(\sqrt{1-x^{2}}\right)^{m}+C=\int \frac{\sqrt{1-x^{2}}}{x^{4}} d x$

$=\int \frac{\sqrt{\frac{1}{x^{2}}-1}}{x^{3}} d x$

Let $\frac{1}{x^{2}}-1=u^{2}$

$\Rightarrow-\frac{2}{x^{3}}=\frac{2 u d u}{d x}$

$\frac{d x}{x^{3}}=-u d u$

$A(x)\left(\sqrt{1-x^{2}}\right)^{m}+C=\int\left(-u^{2}\right) d u=-\frac{u^{3}}{3}+C$

$\begin{array}{l}

=-\frac{1}{3}\left(\frac{1}{x^{2}}-1\right)^{\frac{3}{2}}+C \\

=-\frac{1}{3} \cdot \frac{1}{x^{3}} \cdot\left(1-x^{2}\right)^{\frac{3}{2}}+C \\

=\frac{-1}{3 x^{3}}\left(\sqrt{1-x^{2}}\right)^{3}+C

\end{array}$

Compare both sides,

$\begin{array}{l}

\Rightarrow A(x)=-\frac{1}{3 x^{3}} \text { and } m=3 \\

\Rightarrow(A(x))^{3}=\frac{-1}{27 x^{9}}

\end{array}$

</details>

---

### Q51. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let, <math><mi>n</mi><mo>&#8805;</mo><mn>2</mn></math> be a natural number and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>&#952;</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mi>n</mi></msup><mi>&#952;</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></mrow></mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></msup><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mi>&#952;</mi></mrow></mfrac><mi>d</mi><mi>&#952;</mi><mo>,</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mi>&#952;</mi></mrow></mfrac></mrow></mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>&#952;</mi></mrow></mfrac></mrow></mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>&#952;</mi></mrow></mfrac></mrow></mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>&#952;</mi></mrow></mfrac></mrow></mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></mfrac></msup><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><msup><mi mathvariant="normal">n</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>&#952;</mi></mrow></mfrac></mrow></mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></mfrac></msup><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mfenced separators="|"><mrow><msup><mi>sin</mi><mi>n</mi></msup><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></msup><mi>cos</mi><mi>&#952;</mi></mrow><mrow><msup><mi>sin</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mi>&#952;</mi></mrow></mfrac><mi>d</mi><mi>&#952;</mi></math></p><p>Put, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>&#952;</mi><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mi>d</mi><mi>&#952;</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mo>=</mo><mtable><mtr><mtd><mo>&#8747;</mo><mfrac><mrow><msup><mfenced separators="|"><mrow><msup><mi>t</mi><mi>n</mi></msup><mo>-</mo><mi>t</mi></mrow></mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></msup><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac></mtd><mtd></mtd></mtr></mtable></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>t</mi><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mfrac></mrow></mfenced><mfrac><mn>1</mn><mi>n</mi></mfrac></msup></mrow><msup><mi>t</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mi>d</mi><mi>t</mi></math>

<math><mo>=</mo><mi>&#160;</mi><mrow><mo stretchy="false">&#8747;</mo><mrow><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>t</mi></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>n</mi></mrow></mfrac></mrow></msup></mrow><mrow><msup><mrow><mi>t</mi></mrow><mrow><mi>n</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>t</mi></mrow></mrow></math>

Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>t</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mfrac><mo>=</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>t</mi><mi>n</mi></msup></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>z</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#8747;</mo><msup><mi>z</mi><mfrac><mn>1</mn><mi>n</mi></mfrac></msup><mi>d</mi><mi>z</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><msup><mi>z</mi><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mn>1</mn></mrow></msup><mrow><mfenced separators="|"><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mi>n</mi><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mrow><mn>1</mn><mo>-</mo><mi>n</mi></mrow></msup></mrow></mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mn>1</mn></mrow></msup></mrow><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>c</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mi>n</mi><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>&#952;</mi></mrow></mfrac></mrow></mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mi>n</mi></mfrac></msup><mo>+</mo><mi>c</mi><mo>.</mo></math></p>

</details>

---

### Q52. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>8</mn></msup><mo>+</mo><mn>7</mn><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>7</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math>, <math><mfenced separators="|"><mrow><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mrow></mfenced><mo>,</mo></math> and <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then the value of <math><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>8</mn></msup><mo>+</mo><mn>7</mn><msup><mi>x</mi><mn>6</mn></msup></mrow><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>7</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>8</mn></msup><mo>+</mo><mn>7</mn><msup><mi>x</mi><mn>6</mn></msup></mrow><mrow><msup><mi>x</mi><mn>14</mn></msup><msup><mfenced separators="|"><mrow><mfrac><mn>1</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>7</mn></msup></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math>

<math><mo>=</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mfrac><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>7</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow></mfrac></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>7</mn></mrow></msup></mrow></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math>

Put, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>7</mn></msup></mfrac><mo>+</mo><mn>2</mn><mo>=</mo><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>5</mn><msup><mi>x</mi><mn>6</mn></msup></mfrac><mo>-</mo><mfrac><mn>7</mn><msup><mi>x</mi><mn>8</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>x</mi><mn>7</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>7</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math>

Now,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>c</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mo>+</mo><msup><mrow><mn>2.1</mn></mrow><mrow><mn>7</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

</details>

---

### Q53. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&#8800;</mo><mi>n</mi><mi>&#960;</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> (the set of natural numbers), the integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>x</mi><msqrt><mfrac><mrow><mn>2</mn><mi>sin</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>sin</mi><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mrow><mrow><mn>2</mn><mi>sin</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>sin</mi><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi></math>, is equal to
(where <math><mi>c</mi></math> is a constant of integration).

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mi>sec</mi><mfenced separators="|"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sec</mi><mn>2</mn></msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><mi>sec</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfenced separators="|"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfenced separators="|"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mi>x</mi><msqrt><mfrac><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi></math>

Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mi>&#952;</mi><mo>&#8658;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>d</mi><mi>&#952;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><msqrt><mfrac><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>&#952;</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>+</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>&#952;</mi></mrow></mfrac></msqrt><mi>d</mi><mi>&#952;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><msqrt><mfrac><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mrow></mfrac></msqrt><mi>d</mi><mi>&#952;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><msqrt><mfrac><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>&#952;</mi></mrow></mfrac></msqrt><mi>d</mi><mi>&#952;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mi>d</mi><mi>&#952;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced separators="|"><mrow><mi>sec</mi><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mrow></mfenced></mrow><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mfrac><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|" separators="|"><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfenced separators="|"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>c</mi></math>

</details>

---

### Q54. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><msup><mi>sin</mi><mn>5</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>5</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math>, is equal to

(where <mi><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mi> is the constant of integration).

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cot</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>3</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>cot</mi><mn>3</mn></msup><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><msup><mi>sin</mi><mn>5</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>5</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mfenced separators="|"><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><msup><mi>sin</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><msup><mfenced separators="|"><mrow><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup><msup><mfenced separators="|"><mrow><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math>
Put, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mi>t</mi><mo>=</mo><mn>3</mn><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mn>3</mn><msup><mfenced separators="|"><mi>t</mi></mfenced><mn>2</mn></msup></mrow></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mi>t</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the constant of integration.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#160;</mi><mi>&#160;</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mfenced separators="|"><mrow><msup><mi>tan</mi><mn>3</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mi>C</mi></math>

</details>

---

### Q55. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msqrt><mn>1</mn><mo>+</mo><mn>2</mn><mi>cot</mi><mi>x</mi><mfenced separators="|"><mrow><mi>cosec</mi><mi>x</mi><mo>+</mo><mi>cot</mi><mi>x</mi></mrow></mfenced></msqrt><mi>d</mi><mi>x</mi><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>&#160;</mo></math>is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>log</mi><mfenced open="|" close="|"><mrow><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>log</mi><mfenced open="|" close="|"><mrow><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>log</mi><mfenced open="|" close="|"><mrow><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>log</mi><mfenced open="|" close="|"><mrow><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>log</mi><mfenced open="|" close="|"><mrow><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msqrt><mn>1</mn><mo>+</mo><mn>2</mn><mi>cot</mi><mi>x</mi><mfenced separators="|"><mrow><mi>cosec</mi><mi>&#160;</mi><mi>x</mi><mo>+</mo><mi>cot</mi><mi>x</mi></mrow></mfenced></msqrt><mi>d</mi><mi>x</mi><mi>&#160;</mi><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><msqrt><mn>2</mn><mi>cot</mi><mi>x</mi><mi>cosec</mi><mi>x</mi><mo>+</mo><msup><mi>cosec</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cot</mi><mn>2</mn></msup><mi>x</mi></msqrt></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><msqrt><msup><mfenced><mrow><mi>cosec</mi><mi>&#160;</mi><mi>x</mi><mo>+</mo><mi>cot</mi><mi>&#160;</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></msqrt><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced close="|" open="|" separators="|"><mrow><mi>cosec</mi><mi>&#160;</mi><mi>x</mi><mo>+</mo><mi>cot</mi><mi>&#160;</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><mi>cosec</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>cot</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>tan</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mi>log</mi><mfenced><mrow><mfrac><mrow><mi>sin</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mi>cos</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac><mo>&#183;</mo><mn>2</mn><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mn>2</mn><mi>log</mi><mfenced open="|" close="|"><mrow><mi>sin</mi><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math></p>

</details>

---

### Q56. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>12</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>9</mn></msup></mrow><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>5</mn></msup><mrow><mn>2</mn><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>10</mn></msup></mrow><mrow><mn>2</mn><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>5</mn></msup></mrow><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>10</mn></msup><mrow><mn>2</mn><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>10</mn></msup><mrow><mn>2</mn><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>12</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>9</mn></msup></mrow><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>12</mn></msup><mo>+</mo><mn>5</mn><msup><mi>x</mi><mn>9</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>15</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced separators="|"><mrow><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>5</mn><msup><mi>x</mi><mn>6</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac></mrow></mfenced><mn>3</mn></msup></mfrac></math>

Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac><mo>=</mo><mi>t</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>-</mo><mfrac><mn>5</mn><msup><mi>x</mi><mn>6</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>5</mn><msup><mi>x</mi><mn>6</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mn>1</mn><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>5</mn></msup></mfrac></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mi>c</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><msup><mi>x</mi><mn>10</mn></msup><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mi>c</mi></math>
Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>x</mi><mn>10</mn></msup><mrow><mn>2</mn><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math>

</details>

---

### Q57. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></msup><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfrac><mn>5</mn><mn>4</mn></mfrac></msup></mrow></mfrac></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#160;</mi><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#160;</mi><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></msup><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfrac><mn>5</mn><mn>4</mn></mfrac></msup></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mn>5</mn><mn>4</mn></mfrac></msup></mrow></mfrac></math>

Put, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>t</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>3</mn><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mn>3</mn></mfrac><mfrac><mn>1</mn><msup><mi>t</mi><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mfrac><mo>+</mo><mi>c</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mn>3</mn></mfrac><msup><mfenced separators="|"><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> being the constant of integration.

</details>

---

### Q58. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<p>The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></mrow></mfrac></math> equals to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>4</mn></msup></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></mrow></mfrac></math>

  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>5</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac></mrow></mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></mrow></mfrac></math>

Put,   <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac><mo>=</mo><mi>t</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><msup><mi>x</mi><mn>5</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;&#160;</mo><mi>I</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></mfrac></math>

<math> <mrow> <mo>=</mo> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mo>&#215;</mo> <mo>&#8747;</mo> <msup> <mtext>t</mtext> <mfrac> <mrow> <mo>-</mo> <mn>3</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </msup> <mtext>dt</mtext> </mrow> </math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mfenced><mfrac><msup><mi>t</mi><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mfrac><mn>1</mn><mn>4</mn></mfrac></mfrac></mfenced><mo>+</mo><mi>c</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac></mrow></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.

</details>

---

### Q59. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is a non-zero number and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi>x</mi><mrow><mn>5</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mrow><mn>4</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced><mrow><msup><mi>x</mi><mrow><mn>5</mn><mi>m</mi></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>4</mn><mi>m</mi></mrow></msup></mrow></mfenced><mrow><mn>2</mn><mi>m</mi><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mi>m</mi></mrow></mfrac><mfrac><msup><mi>x</mi><mrow><mn>4</mn><mi>m</mi></mrow></msup><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mrow><mn>5</mn><mi>m</mi></mrow></msup><mrow><mn>2</mn><mi>m</mi><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>m</mi><mfenced><mrow><msup><mi>x</mi><mrow><mn>5</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mn>4</mn><mi>m</mi></mrow></msup></mrow></mfenced></mrow><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mi>m</mi></mrow></mfrac><mfrac><msup><mi>x</mi><mrow><mn>4</mn><mi>m</mi></mrow></msup><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi>x</mi><mrow><mn>5</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mrow><mn>4</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>x</mi><mrow><mn>5</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mrow><mn>4</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><mrow><msup><mi>x</mi><mrow><mn>6</mn><mi>m</mi></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>m</mi></mrow></msup></mrow></mfenced><mn>3</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>x</mi><mrow><mo>-</mo><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>m</mi></mrow></msup></mrow></mfenced><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math>.</p><p>If, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>m</mi></mrow></msup><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>m</mi><mfenced><mrow><msup><mi>x</mi><mrow><mo>-</mo><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>d</mi><mi>t</mi></mrow><mrow><mi>m</mi><msup><mi>t</mi><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mn>1</mn><mi>m</mi></mfrac><mo>&#8747;</mo><msup><mi>t</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi>d</mi><mi>t</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mn>1</mn><mi>m</mi></mfrac><mfenced><mfrac><msup><mi>t</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mrow><mo>-</mo><mn>2</mn></mrow></mfrac></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>m</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>m</mi></mrow></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>m</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>x</mi><mi>m</mi></msup></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>m</mi></mrow></mfrac><mfrac><msup><mi>x</mi><mrow><mn>4</mn><mi>m</mi></mrow></msup><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mi>m</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>.</mo></math></p>

</details>

---

### Q60. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

$$
\text { The integral } \int \frac{\sin ^2 x \cos ^2 x}{\left(\sin ^3 x+\cos ^3 x\right)^2} d x \text { is equal to: }
$$

**Options:**

- **(A)** $\frac{1}{\left(1+\cot ^3 x\right.}+c$
- **(B)** $\left.-\frac{1}{3\left(1+\tan ^3 x\right.}+c\right)$
- **(C)** $\frac{\sin ^3 x}{\left(1+\cos ^3 x\right.}+c$
- **(D)** $-\frac{\cos ^3 x}{3\left(1+\sin ^3 x\right.}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left.-\frac{1}{3\left(1+\tan ^3 x\right.}+c\right)$**

**Detailed Solution:**

Let $I=\int \frac{\sin ^2 x \cos ^2 x}{\left(\sin ^3 x+\cos ^3 x\right)^2} d x$
$$
\begin{aligned}
&\mathrm{I}=\int\left(\frac{\sin x \cdot \cos x}{\sin ^3 x+\cos ^3 x}\right)^2 d x \\
&\mathrm{I}=\int\left(\frac{\sin x \cdot \cos x}{\cos ^3 x\left(1+\tan ^3 x\right)}\right)^2 d x \\
&=\int\left(\frac{\sin x \cdot \sec ^2 x}{\left(1+\tan ^3 x\right)}\right)^2 d x \\
&\text { Put } 1+\tan ^3 x=\mathrm{t} \\
&d t=3 \tan ^2 x \sec ^2 x d x \text { or } d x \\
&=\frac{d t}{3 \tan ^2 x \sec ^2 x} \\
&\therefore \mathrm{I}=\int \frac{\sin ^2 x \cdot \sec ^4 x}{t^2} \times \frac{d t}{3 \tan ^2 x \sec ^2 x}
\end{aligned}
$$

$$
\begin{aligned}
&\mathrm{I}=\frac{1}{3} \int \frac{\sin ^2 x \cdot \sec ^4 x}{t^2} \times \frac{d t}{\frac{\sin ^2 x}{\cos ^2 x} \times \sec ^2 x} \\
&=\frac{1}{3} \int \frac{\sin ^2 x \cdot \sec ^4 x}{t^2} \times \frac{d t}{\sin ^2 x \sec ^4 x} \\
&\therefore \mathrm{I}=\frac{1}{3} \int \frac{d t}{t^2}=\frac{1}{3} \int t^{-2} d t \\
&\mathrm{I}=\frac{1}{3}\left[\frac{t^{-2+1}}{-2+1}\right]+c=\frac{-1}{3}\left[\frac{1}{t}\right]+c \\
&\text { or } \mathrm{I}=-\frac{1}{3\left(1+\tan ^3 x\right)}+c
\end{aligned}
$$

</details>

---

### Q61. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int x \cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right) d x(x>0)$ is equal to:

**Options:**

- **(A)** $-x+\left(1+x^2\right) \tan ^{-1} x+c$
- **(B)** $x-\left(1+x^2\right) \cot ^{-1} x+c$
- **(C)** $-x+\left(1+x^2\right) \cot ^{-1} x+c$
- **(D)** $x-\left(1+x^2\right) \tan ^{-1} x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-x+\left(1+x^2\right) \tan ^{-1} x+c$**

**Detailed Solution:**

Let $\mathrm{I}=\int x \cos ^{-1}\left(\frac{1-x^2}{1+x^2}\right) d x$
$$
\therefore \mathrm{I}=2 \int_{\text {II }} x \cdot \tan ^{-1} x d x
$$
Applying Integration by parts
$$
\begin{array}{r}
\mathrm{I}=2\left[\tan ^{-1} x \int x d x-\int\left(\frac{d}{d x}\left(\tan ^{-1} x\right) \int x d x\right) d x\right] \\
\mathrm{I}=2\left[\frac{x^2}{2} \tan ^{-1} x-\int \frac{1}{1+x^2} \times \frac{x^2}{2} d x\right]+c \\
\mathrm{I}=2\left[\frac{x^2}{2} \tan ^{-1} x-\frac{1}{2} \int \frac{x^2+1-1}{x^2+1} d x\right]+c \\
\mathrm{I}=2\left[\frac{x^2}{2} \tan ^{-1} x-\frac{1}{2} \int \frac{x^2+1}{x^2+1} d x+\frac{1}{2} \int \frac{1}{1+x^2} d x\right]+c
\end{array}
$$

$$
\begin{aligned}
\mathrm{I} &=2\left[\frac{x^2}{2} \tan ^{-1} x-\frac{1}{2} \int 1 . d x+\frac{1}{2} \tan ^{-1} x\right]+c \\
\mathrm{I} &=2\left[\frac{x^2}{2} \tan ^{-1} x-\frac{x}{2}+\frac{1}{2} \tan ^{-1} x\right]+c \\
\mathrm{I} &=x^2 \tan ^{-1} x+\tan ^{-1} x-x+c \\
& \text { or } I=-x+\left(x^2+1\right) \tan ^{-1} x+c
\end{aligned}
$$

</details>

---

### Q62. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mi>sin</mi><mn>8</mn></msup><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mn>8</mn></msup><mi>x</mi></mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>8</mn></msup><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mn>8</mn></msup><mi>x</mi><mo>=</mo><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>=</mo><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sin</mi><mn>8</mn></msup><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mn>8</mn></msup><mi>x</mi></mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><msup><mo>sin</mo><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mrow><mfenced><mrow><msup><mi>sin</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></math> 

  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.  </p></blockquote>

</details>

---

### Q63. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `3`

The integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>c</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>c</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>c</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>c</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><msup><mi>x</mi><mspace/></msup><mo>+</mo><mo>&#8747;</mo><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi></math></p><p>Integrating <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><munder><munder><mi>x</mi><mo>&#9183;</mo></munder><mi>I</mi></munder><mo>.</mo><munder><munder><mrow><mrow><mo>(</mo><mn>1</mn><mo>&#8722;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>)</mo></mrow><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup></mrow><mo>&#9183;</mo></munder><mrow><mi>I</mi><mi>I</mi></mrow></munder><mi>d</mi><mi>x</mi></math>, by parts</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>-</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>-</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>c</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.  </p>

</details>

---

### Q64. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the integral
$$
\int \frac{\cos 8 x+1}{\cot 2 x-\tan 2 x} d x=A \cos 8 x+k
$$
where $k$ is an arbitrary constant, then $\mathrm{A}$ is equal to:

**Options:**

- **(A)** $-\frac{1}{16}$
- **(B)** $\frac{1}{16}$
- **(C)** $\frac{1}{8}$
- **(D)** $-\frac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{1}{16}$**

**Detailed Solution:**

Let $\mathrm{I}=\int \frac{\cos 8 x+1}{\cot 2 x-\tan 2 x} d x$
Now, $\mathrm{D}^r=\cot 2 x-\tan 2 x=\frac{\cos 2 x}{\sin 2 x}-\frac{\sin 2 x}{\cos 2 x}$
$$
=\frac{\cos ^2 2 x-\sin ^2 2 x}{\sin 2 x \cos 2 x}=\frac{2 \cos 4 x}{\sin 4 x}
$$
$\begin{aligned} \therefore \mathrm{I} &=\int \frac{2 \cos ^2 4 x}{\frac{2 \cos 4 x}{\sin 4 x}} d x=\int \frac{2 \cos ^2 4 x \cdot \sin 4 x}{2 \cos 4 x} d x \\ &=\frac{1}{2} \int \sin 8 x d x=-\frac{1}{2} \frac{\cos 8 x}{8}+k \\ &=-\frac{1}{16} \cdot \cos 8 x+k \\ & \text { Now },-\frac{1}{16} \cdot \cos 8 x+k=\mathrm{A} \cos 8 x+k \\ & \Rightarrow \mathrm{A}=-\frac{1}{16} \end{aligned}$

</details>

---

### Q65. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The integral $\int \frac{x d x}{2-x^2+\sqrt{2-x^2}}$ equals :

**Options:**

- **(A)** $\log \left|1+\sqrt{2+x^2}\right|+c$
- **(B)** $-\log \left|1+\sqrt{2-x^2}\right|+c$
- **(C)** $-x \log \left|1-\sqrt{2-x^2}\right|+c$
- **(D)** $x \log \left|1-\sqrt{2+x^2}\right|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\log \left|1+\sqrt{2-x^2}\right|+c$**

**Detailed Solution:**

$\quad \mathrm{I}=\int \frac{x d x}{2-x^2+\sqrt{2-x^2}}$
$$
\begin{aligned}
& \text { Put } t=\sqrt{2-x^2}, \frac{d t}{d x}=\frac{1}{2 \sqrt{2-x^2}} \cdot(-2 x) \\
& \begin{aligned}
& \Rightarrow-t d t=x d x \\
& \therefore \\
& \mathrm{I}=\int \frac{(-t) d t}{t^2+t}=-\int \frac{1}{t+1} d t=-\log |t+1| \\
&=-\log \left|\sqrt{2-x^2}+1\right|+c
\end{aligned}
\end{aligned}
$$

</details>

---

### Q66. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{d x}{x+x^7}=p(x)$ then, $\int \frac{x^6}{x+x^7} d x$ is equal to:

**Options:**

- **(A)** $\ln |x|-p(x)+c$
- **(B)** $\ln |x|+p(x)+c$
- **(C)** $x-p(x)+c$
- **(D)** $x+p(x)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\ln |x|-p(x)+c$**

**Detailed Solution:**

$\int \frac{x^6}{x+x^7} d x=\int \frac{x^6}{x\left(1+x^6\right)} d x$
$=\int \frac{\left(1+x^6\right)-1}{x\left(1+x^6\right)} d x$
$=\int \frac{1}{x} d x-\int \frac{1}{x+x^7} d x$
$=\ln |x|-p(x)+c$

</details>

---

### Q67. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `3`

$f(x)=\int \frac{d x}{\sin ^6 x}$ is a polynomial of degree

**Options:**

- **(A)** 5 in $\cot x$
- **(B)** 5 in $\tan x$
- **(C)** 3 in $\tan x$
- **(D)** 3 in $\cot x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5 in $\cot x$**

**Detailed Solution:**

Let $f(x)=\int \frac{d x}{\sin ^6 x}$
$$
f(x)=\int \operatorname{cosec}^6 x d x
$$
From reduction formula, we have
$$
\begin{aligned}
& \mathrm{I}_{\mathrm{n}}=\int \operatorname{cosec}^n x d x \\
& =-\frac{\operatorname{cosec}^{n-2} x \cot x}{n-1}+\frac{n-2}{n-1} \mathrm{I}_{n-2}
\end{aligned}
$$

$$
\begin{gathered}
\therefore f(x)=-\frac{\operatorname{cosec}^4 x \cot x}{5}+\frac{4}{5}\left[\frac{-\operatorname{cosec}^2 x \cot x}{3}+\frac{2}{3} \mathrm{I}_2\right] \\
=-\frac{\operatorname{cosec}^4 x \cot x}{5}-\frac{4}{15} \operatorname{cosec}^2 x \cdot \cot x+\frac{8}{15}[-\cot x] \\
=\frac{-\left(1+\cot ^2 x\right)^2 \cdot \cot x}{5}-\frac{4}{15}\left(1+\cot ^2 x\right) \cot x \\
=\frac{-1}{5}\left[1+\cot ^4 x+2 \cot ^2 x\right] \cot x-\frac{4}{15}[-\cot x)\left(\because \operatorname{cosec}^2 x=1+\cot ^2 x\right) \\
=\frac{-1}{5}\left[\cot x+\cot ^3 x\right] \\
\frac{-4}{15} \cot ^3 x-\frac{4}{15} \cot ^3 x-\frac{8}{15} \cot x \\
\cot x]
\end{gathered}
$$

$$
\begin{aligned}
& =\frac{-15}{15} \cot x-\frac{\cot ^5 x}{5}-\frac{10}{15} \cot ^3 x \\
& =\frac{-\cot ^5 x}{5}-\frac{2}{3} \cot ^3 x-\cot x
\end{aligned}
$$
It is a polynomial of degree 5 in $\cot x$.

</details>

---

### Q68. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `3`

If $f(x)=\int\left(\frac{x^2+\sin ^2 x}{1+x^2}\right) \sec ^2 x d x$ and $f(0)=0$, then $f(1)$ equals

**Options:**

- **(A)** $\tan 1-\frac{\pi}{4}$
- **(B)** $\tan 1+1$
- **(C)** $\frac{\pi}{4}$
- **(D)** $1-\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan 1-\frac{\pi}{4}$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { Let } f(x)=\int\left(\frac{x^2+\sin ^2 x}{1+x^2}\right) \sec ^2 x d x \\
& =\int \frac{x^2 \sec ^2 x+\frac{\sin ^2 x}{\cos ^2 x}}{1+x^2} d x
\end{aligned}
$$

$$
\begin{aligned}
& =\int \frac{x^2 \sec ^2 x+\tan ^2 x}{1+x^2} d x \\
& =\int \frac{x^2\left(1+\tan ^2 x\right)+\tan ^2 x}{1+x^2} d x \\
& =\int \frac{x^2+\tan ^2 x\left(1+x^2\right)}{1+x^2} d x \\
& =\int \frac{x^2}{1+x^2} d x+\int \tan ^2 x d x \\
& =\int \frac{x^2+1-1}{1+x^2} \mathrm{dx}+\int\left(\sec ^2 \mathrm{x}-1 \mathrm{dx}\right. \\
& =\int 1 d x-\int \frac{d x}{1+x^2}+\int \sec ^2 x d x-\int d x \\
& =-\tan -1 x+\tan ^{-1} x+\mathrm{c} \\
& \text { Given: } f(0)=0 \\
& \Rightarrow f(0)=-\tan ^{-1} 0+\tan ^2+c \\
& \Rightarrow c=0 \\
& \therefore f(x)=-\tan ^{-1} x+\tan ^2 x
\end{aligned}
$$
Now,
$$
f(1)=-\tan ^{-1}(1)+\tan 1=\tan 1-\frac{\pi}{4}
$$

</details>

---

### Q69. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The integral of $\frac{x^2-x}{x^3-x^2+x-1}$ w.r.t. $x$ is

**Options:**

- **(A)** $\frac{1}{2} \log \left(x^2+1+c\right)$
- **(B)** $\frac{1}{2} \log \left|x^2-1\right|+c$
- **(C)** $\log \left(x^2+1+c\right)$
- **(D)** $\log \left|x^2-1\right|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2} \log \left(x^2+1+c\right)$**

**Detailed Solution:**

Let $I=\int \frac{x^2-x}{x^3-x^2+x-1} d x$
$$
=\int \frac{x(x-1)}{x^2(x-1)+(x-1)} d x=\int \frac{x d x}{x^2+1}
$$

$$
\left.=\frac{1}{2} \int \frac{2 x d x}{\left(x^2+1\right.}\right)
$$
Let $x^2+1=t \Rightarrow 2 x d x=d t$
$$
\begin{aligned}
& \therefore I=\frac{1}{2} \int \frac{d t}{t}=\frac{1}{2} \log t+c \\
& =\frac{1}{2} \log \left(x^2+1\right)+c
\end{aligned}
$$
where ' $c$ ' is the constant of integration.

</details>

---

### Q70. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

If the integral $\int \frac{5 \tan x}{\tan x-2} d x=x+a \ln |\sin x-2 \cos x|+k$, then $a$ is equal to

**Options:**

- **(A)** $-1$
- **(B)** $-2$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2$**

**Detailed Solution:**

$\int \frac{5 \tan x}{\tan x-2} d x=\int \frac{5 \sin x}{\sin x-2 \cos x} d x$
$\Rightarrow \int\left[\frac{2(\cos x+2 \sin x)+(\sin x-2 \cos x)}{\sin x-2 \cos x}\right] d x$
$=2 \int\left(\frac{\cos x+2 \sin x}{\sin x-2 \cos x}\right) d x+\int d x+k$
$=2 \log |\sin x-2 \cos x|+x+k \quad \therefore a=2$

</details>

---

### Q71. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

The value of $\sqrt{2} \int \frac{\sin x d x}{\sin \left(x-\frac{\pi}{4}\right)}$ is

**Options:**

- **(A)** $x+\log \left|\cos \left(x-\frac{\pi}{4}\right)\right|+c$
- **(B)** $x-\log \left|\sin \left(x-\frac{\pi}{4}\right)\right|+c$
- **(C)** $x+\log \left|\sin \left(x-\frac{\pi}{4}\right)\right|+c$
- **(D)** $x-\log \left|\cos \left(x-\frac{\pi}{4}\right)\right|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x+\log \left|\sin \left(x-\frac{\pi}{4}\right)\right|+c$**

**Detailed Solution:**

$$
\begin{aligned}
& \sqrt{2} \int \frac{\sin x d x}{\sin \left(x-\frac{\pi}{4}\right)}=\sqrt{2} \int \frac{\sin \left(x-\frac{\pi}{4}+\frac{\pi}{4}\right) d x}{\sin \left(x-\frac{\pi}{4}\right)} \\
& =\sqrt{2} \int\left(\cos \frac{\pi}{4}+\cot \left(x-\frac{\pi}{4}\right) \sin \frac{\pi}{4}\right) d x \\
& =\int d x+\int \cot \left(x-\frac{\pi}{4}\right) d x \\
& =x+\ln \left|\sin \left(x-\frac{\pi}{4}\right)\right|+c .
\end{aligned}
$$

</details>

---

### Q72. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{\cos x+\sqrt{3} \sin x}$ equals

**Options:**

- **(A)** $\frac{1}{2} \log \tan \left(\frac{x}{2}+\frac{\pi}{12}\right)+c$
- **(B)** $\frac{1}{2} \log \tan \left(\frac{x}{2}-\frac{\pi}{12}\right)+c$
- **(C)** $\log \tan \left(\frac{\mathrm{x}}{2}+\frac{\pi}{12}\right)+\mathrm{c}$
- **(D)** $\log \tan \left(\frac{\mathrm{x}}{2}-\frac{\pi}{12}\right)+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2} \log \tan \left(\frac{x}{2}+\frac{\pi}{12}\right)+c$**

**Detailed Solution:**

$\int \frac{d x}{\cos x+\sqrt{3} \sin x}$
$=\frac{1}{2} \int \sec \left(x-\frac{\pi}{3}\right) d x$
$=\frac{1}{2} \log \tan \left(\frac{x}{2}-\frac{\pi}{6}+\frac{\pi}{4}\right)+c$
$=\frac{1}{2} \log \tan \left(\frac{x}{2}+\frac{\pi}{12}\right)+c$.

</details>

---

### Q73. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

$\int\left\{\frac{(\log x-1)}{\left(1+(\log x)^2\right.}\right\}^2 d x$ is equal to

**Options:**

- **(A)** $\frac{\log x}{(\log x)^2+1}+C$
- **(B)** $\frac{x}{x^2+1}+C$
- **(C)** $\frac{x e^x}{1+x^2}+C$
- **(D)** $\frac{x}{(\log x)^2+1}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{x}{(\log x)^2+1}+C$**

**Detailed Solution:**

$$
\begin{aligned}
& \int \frac{(\log x-1)^2}{\left(1+(\log x)^2\right)^2} d x \\
& =\int\left[\frac{1}{\left(1+(\log x)^2\right)}-\frac{2 \log x}{\left(1+(\log x)^2\right)^2}\right] d x \\
& =\int\left[\frac{e^t}{1+t^2}-\frac{2 t e^t}{\left(1+t^2\right)^2}\right] d t \text { put } \log x=t \Rightarrow d x=e^t d t \\
& \int e^t\left[\frac{1}{1+t^2}-\frac{2 t}{\left(1+t^2\right)^2}\right] d t \\
& =\frac{e^t}{1+t^2}+c=\frac{x}{1+(\log x)^2}+c
\end{aligned}
$$

</details>

---

### Q74. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{d x}{\cos x-\sin x}$ is equal to

**Options:**

- **(A)** $\frac{1}{\sqrt{2}} \log \left|\tan \left(\frac{x}{2}-\frac{\pi}{8}\right)\right|+C$
- **(B)** $\frac{1}{\sqrt{2}} \log \left|\cot \left(\frac{x}{2}\right)\right|+C$
- **(C)** $\frac{1}{\sqrt{2}} \log \left|\tan \left(\frac{x}{2}-\frac{3 \pi}{8}\right)\right|+C$
- **(D)** $\frac{1}{\sqrt{2}} \log \left|\tan \left(\frac{x}{2}+\frac{3 \pi}{8}\right)\right|+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\sqrt{2}} \log \left|\tan \left(\frac{x}{2}+\frac{3 \pi}{8}\right)\right|+C$**

**Detailed Solution:**

$\int \frac{d x}{\cos x-\sin x}=\frac{1}{\sqrt{2}} \int \frac{1}{\cos \left(x+\frac{\pi}{4}\right)} d x=\frac{1}{\sqrt{2}} \int \sec \left(x+\frac{\pi}{4}\right) d x=\frac{1}{\sqrt{2}} \log \left|\tan \left(\frac{x}{2}+\frac{3 \pi}{8}\right)\right|+C$

</details>

---

### Q75. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $\int \frac{\sin x}{\sin (x-\alpha)} d x=A x+B \log \sin (x-\alpha)+C$, then value of $(A, B)$ is

**Options:**

- **(A)** $(\sin \alpha, \cos \alpha)$
- **(B)** $(\cos \alpha, \sin \alpha)$
- **(C)** $(-\sin \alpha, \cos \alpha)$
- **(D)** $(-\cos \alpha, \sin \alpha)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\cos \alpha, \sin \alpha)$**

**Detailed Solution:**

Put $x-\alpha=t$
$\Rightarrow \int \frac{\sin (\alpha+t)}{\sin t} d t=\sin \alpha \int \cot t d t+\cos \alpha \int d t$
$=\cos \alpha(x-\alpha)+\sin \alpha \ln |\sin t|+c$
$A=\cos \alpha, B=\sin \alpha$

</details>

---

