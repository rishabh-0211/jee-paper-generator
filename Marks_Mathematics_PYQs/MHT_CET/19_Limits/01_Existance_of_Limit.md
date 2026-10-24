# MHT CET Mathematics - Limits

## Topic 1: Existance of Limit

**Total Questions:** 16

---

### Q1. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider the function: $f(x) = \begin{cases} x^2 + 1 & \text{if } x < 2 \\ 5 & \text{if } x = 2 \\ 3x - 1 & \text{if } x > 2 \end{cases}$
Which of the following statements is correct ?

**Options:**

- **(A)** $\lim_{x \to 2} f(x)$ exists and is equal to $5$
- **(B)** $\lim_{x \to 2} f(x)$ exists but is not equal to $5$
- **(C)** $\lim_{x \to 2} f(x)$ does not exist because $f(2)$ is defined
- **(D)** $\lim_{x \to 2} f(x)$ does not exist because left-hand and right-hand limits are not equal

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\lim_{x \to 2} f(x)$ exists and is equal to $5$**

**Detailed Solution:**

To find the limit of $f(x)$ as $x \to 2$, we evaluate the left-hand limit (LHL) and the right-hand limit (RHL).

LHL $= \lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} (x^2 + 1) = 2^2 + 1 = 5$

RHL $= \lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} (3x - 1) = 3(2) - 1 = 5$

Since LHL $=$ RHL $= 5$, the limit $\lim_{x \to 2} f(x)$ exists and is equal to $5$.

Answer: $\lim_{x \to 2} f(x)$ exists and is equal to $5$

</details>

---

### Q2. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim_{x \to 1} \dfrac{x^3 + ax^2 + bx + c}{x^2 - 2x + 1} = 2026$ then the value of $a - c$ is...

**Options:**

- **(A)** $2$
- **(B)** $1$
- **(C)** $-1$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-2$**

**Detailed Solution:**

Let $f(x) = x^3 + ax^2 + bx + c$.

For the limit to exist and be finite, the denominator $(x-1)^2$ must be a factor of the numerator $f(x)$.

Let $f(x) = (x-1)^2(x-k)$.

Expanding this, we get $f(x) = (x^2-2x+1)(x-k) = x^3 - (k+2)x^2 + (2k+1)x - k$.

Comparing the coefficients, we have $a = -(k+2)$ and $c = -k$.

The limit is given by $\lim_{x \to 1} \dfrac{(x-1)^2(x-k)}{(x-1)^2} = \lim_{x \to 1} (x-k) = 1-k$.

Given that the limit is $2026$, we have $1-k = 2026 \Rightarrow k = -2025$.

We need to find the value of $a-c$.

$a-c = -(k+2) - (-k) = -k - 2 + k = -2$.

Answer: $-2$

</details>

---

### Q3. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim_{x \to 3} \dfrac{[x] - 3}{x - 3}$, where $[\cdot]$ denotes the greatest integer function, is.....

**Options:**

- **(A)** $\infty$
- **(B)** $1$
- **(C)** $0$
- **(D)** does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) does not exist**

**Detailed Solution:**

Evaluate the left-hand limit (LHL) and right-hand limit (RHL) at $x = 3$.

For LHL, let $x \to 3^{-}$. Then $[x] = 2$.

LHL $= \lim_{x \to 3^{-}} \dfrac{[x] - 3}{x - 3} = \lim_{x \to 3^{-}} \dfrac{2 - 3}{x - 3} = \lim_{x \to 3^{-}} \dfrac{-1}{x - 3} = \infty$

For RHL, let $x \to 3^{+}$. Then $[x] = 3$.

RHL $= \lim_{x \to 3^{+}} \dfrac{[x] - 3}{x - 3} = \lim_{x \to 3^{+}} \dfrac{3 - 3}{x - 3} = \lim_{x \to 3^{+}} 0 = 0$

Since LHL $\neq$ RHL, the limit does not exist.

Answer: does not exist

</details>

---

### Q4. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Define $\mathrm{f}(x)=\left\{\begin{array}{cl}\mathrm{b}-\mathrm{a} x & , \text { if } x < 2 \\ 3 & , \text { if } x=2 \\ \mathrm{a}+2 \mathrm{~b} x & , \text { if } x>2\end{array}\right.$ and if $\lim _{x \rightarrow 2} \mathrm{f}(x)$ exists, then $\frac{\mathrm{a}}{\mathrm{b}}=$

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -1**

**Detailed Solution:**

For $\lim_{x \rightarrow 2} \mathrm{f}(x)$ to exist, the left-hand limit (LHL) and right-hand limit (RHL) at $x = 2$ must be equal.

$\text{LHL} = \lim_{x \rightarrow 2^-} \mathrm{f}(x) = \lim_{x \rightarrow 2^-} (\mathrm{b} - \mathrm{a}x) = \mathrm{b} - 2\mathrm{a}$

$\text{RHL} = \lim_{x \rightarrow 2^+} \mathrm{f}(x) = \lim_{x \rightarrow 2^+} (\mathrm{a} + 2\mathrm{b}x) = \mathrm{a} + 4\mathrm{b}$

Equating LHL and RHL:

$\mathrm{b} - 2\mathrm{a} = \mathrm{a} + 4\mathrm{b}$

$-3\mathrm{a} = 3\mathrm{b}$

$\mathrm{a} = -\mathrm{b}$

$\dfrac{\mathrm{a}}{\mathrm{b}} = -1$

Answer: -1

</details>

---

### Q5. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $\mathrm{f}(x)=\left\{\begin{array}{cl}\frac{\cos a x-\cos b x}{\cos c x-\cos b x} & , \text { if } x \neq 0 \\ -1 & , \text { if } x=0\end{array}\right.$ is continuous at $x=0$, then $a^2, b^2, c^2$ are in

**Options:**

- **(A)** Geometric progression
- **(B)** Arithmetic progression
- **(C)** Harmonic progression
- **(D)** Arithmetico-Geometric progression

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Arithmetic progression**

**Detailed Solution:**

For the function to be continuous at $x=0$, we must have $\lim_{x \to 0} \mathrm{f}(x) = \mathrm{f}(0)$.

$\lim_{x \to 0} \dfrac{\cos ax - \cos bx}{\cos cx - \cos bx} = -1$

Dividing the numerator and the denominator by $x^2$, we get:

$\lim_{x \to 0} \dfrac{\dfrac{1 - \cos bx}{x^2} - \dfrac{1 - \cos ax}{x^2}}{\dfrac{1 - \cos bx}{x^2} - \dfrac{1 - \cos cx}{x^2}} = -1$

Using the standard limit $\lim_{x \to 0} \dfrac{1 - \cos kx}{x^2} = \dfrac{k^2}{2}$, we can evaluate the limit as:

$\dfrac{\dfrac{b^2}{2} - \dfrac{a^2}{2}}{\dfrac{b^2}{2} - \dfrac{c^2}{2}} = -1$

$\dfrac{b^2 - a^2}{b^2 - c^2} = -1$

$b^2 - a^2 = -b^2 + c^2$

$2b^2 = a^2 + c^2$

This is the condition for an Arithmetic Progression. Therefore, $a^2, b^2, c^2$ are in Arithmetic Progression.

Answer: Arithmetic progression

</details>

---

### Q6. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\quad \mathbf{f}(x)=\left\{\begin{array}{cl}\frac{1-\cos 4 x}{x^2} & \text { if } x < 0 \\ a & \text { if } x=0 \\ \frac{\sqrt{x}}{(16+\sqrt{x})^{\frac{1}{2}}-4} & \text { if } x>0\end{array}\right.$ is continuous at $x=0$ Then $a=$

**Options:**

- **(A)** $4$
- **(B)** $8$
- **(C)** $-4$
- **(D)** $-8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $8$**

**Detailed Solution:**

For the function to be continuous at $x=0$, the left-hand limit (LHL), right-hand limit (RHL), and the value of the function at $x=0$ must be equal.

Evaluating the left-hand limit (LHL) at $x=0$:
$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} \dfrac{1 - \cos 4x}{x^2}$

Using the trigonometric identity $1 - \cos \theta = 2 \sin^2 \left(\dfrac{\theta}{2}\right)$:
$\lim_{x \to 0^-} \dfrac{2 \sin^2 2x}{x^2} = 2 \lim_{x \to 0^-} \left( \dfrac{\sin 2x}{x} \right)^2$

Multiplying and dividing by $4$ inside the limit:
$2 \lim_{x \to 0^-} \left( \dfrac{\sin 2x}{2x} \times 2 \right)^2 = 2 \times (1 \times 2)^2 = 2 \times 4 = 8$

Evaluating the right-hand limit (RHL) at $x=0$:
$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \dfrac{\sqrt{x}}{\sqrt{16 + \sqrt{x}} - 4}$

Rationalizing the denominator by multiplying the numerator and denominator by $\sqrt{16 + \sqrt{x}} + 4$:
$\lim_{x \to 0^+} \dfrac{\sqrt{x} (\sqrt{16 + \sqrt{x}} + 4)}{(\sqrt{16 + \sqrt{x}})^2 - 4^2}$

$\Rightarrow \lim_{x \to 0^+} \dfrac{\sqrt{x} (\sqrt{16 + \sqrt{x}} + 4)}{16 + \sqrt{x} - 16}$

$\Rightarrow \lim_{x \to 0^+} \dfrac{\sqrt{x} (\sqrt{16 + \sqrt{x}} + 4)}{\sqrt{x}}$

Canceling $\sqrt{x}$ and substituting $x = 0$:
$\lim_{x \to 0^+} (\sqrt{16 + \sqrt{x}} + 4) = \sqrt{16 + 0} + 4 = 4 + 4 = 8$

Since the function is continuous at $x=0$, we have:
$f(0) = \lim_{x \to 0} f(x)$

$a = 8$

Answer: $8$

</details>

---

### Q7. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)= \begin{cases}\frac{8^x-4^x-2^x+1}{x^2}, & \text { if } x>0 \\ \mathrm{e}^x \sin x+x+\lambda \log 4, & \text { if } x \leqslant 0\end{cases}$ is continuous at $x=0$ then the value of $1000 \mathrm{e}^\lambda=$

**Options:**

- **(A)** $1000$
- **(B)** $3000$
- **(C)** $2000$
- **(D)** $4000$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2000$**

**Detailed Solution:**

For the function to be continuous at $x=0$, the right-hand limit (RHL) must equal the left-hand limit (LHL) at $x=0$.

First, evaluating the right-hand limit:
$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \dfrac{8^x - 4^x - 2^x + 1}{x^2}$

Factorizing the numerator:
$8^x - 4^x - 2^x + 1 = 4^x(2^x - 1) - 1(2^x - 1) = (4^x - 1)(2^x - 1)$

So, the limit becomes:
$\lim_{x \to 0^+} \left( \dfrac{4^x - 1}{x} \right) \left( \dfrac{2^x - 1}{x} \right)$

Using the standard limit $\lim_{x \to 0} \dfrac{a^x - 1}{x} = \log a$, we get:
$\lim_{x \to 0^+} f(x) = (\log 4)(\log 2)$

Now, evaluating the left-hand limit:
$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (\mathrm{e}^x \sin x + x + \lambda \log 4)$

Substituting $x = 0$:
$\lim_{x \to 0^-} f(x) = \mathrm{e}^0 \sin 0 + 0 + \lambda \log 4 = \lambda \log 4$

Equating the LHL and RHL for continuity:
$\lambda \log 4 = (\log 4)(\log 2)$

$\lambda = \log 2$

We need to find the value of $1000 \mathrm{e}^\lambda$:
$1000 \mathrm{e}^\lambda = 1000 \mathrm{e}^{\log 2} = 1000 \times 2 = 2000$

Answer: $2000$

</details>

---

### Q8. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{|x|}{|x|+x^2}=$

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $-1$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

Given limit is $\lim_{x \rightarrow 0} \dfrac{|x|}{|x|+x^2}$

Since $x^2 = |x|^2$, the expression can be written as $\dfrac{|x|}{|x|+|x|^2}$

For $x \neq 0$, we can divide the numerator and denominator by $|x|$:

$\dfrac{|x|}{|x|(1+|x|)} = \dfrac{1}{1+|x|}$

Taking the limit as $x \rightarrow 0$:

$\lim_{x \rightarrow 0} \dfrac{1}{1+|x|} = \dfrac{1}{1+0} = 1$

Answer: $1$

</details>

---

### Q9. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For each $x \in \mathbb{R}$, Let $[x]$ represent greatest integer function, then $\lim _{x \rightarrow 0^{-}} \dfrac{x([x]+|x|) \sin [x]}{|x|}$ is equal to

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $\sin 1$
- **(D)** $-\sin 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\sin 1$**

**Detailed Solution:**

For $x \rightarrow 0^{-}$, $-1 < x < 0$.

In this interval, $[x] = -1$ and $|x| = -x$.

Substituting these values into the given limit:

$\lim _{x \rightarrow 0^{-}} \dfrac{x(-1 - x) \sin(-1)}{-x}$

Using $\sin(-1) = -\sin 1$, the expression becomes:

$\lim _{x \rightarrow 0^{-}} \dfrac{x(1 + x) \sin 1}{-x}$

Canceling $x$ from the numerator and denominator:

$\lim _{x \rightarrow 0^{-}} -(1 + x) \sin 1$

Evaluating the limit as $x \rightarrow 0^{-}$:

$-(1 + 0) \sin 1 = -\sin 1$

Answer: $-\sin 1$

</details>

---

### Q10. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=3 x^{10}-7 x^8+5 x^6-21 x^3+3 x^2-7$, then $\lim _{\alpha \rightarrow 0} \frac{f(1-\alpha)-f(1)}{\alpha^3+3 \alpha}=$

**Options:**

- **(A)** $\frac{53}{3}$
- **(B)** $\frac{-53}{3}$
- **(C)** $\frac{52}{3}$
- **(D)** $\frac{-52}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{53}{3}$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{f}(x)=3 x^{10}-7 x^8+5 x^6-21 x^3+3 x^2-7 \\
\therefore \quad & \mathrm{f}^{\prime}(x)=30 x^9-56 x^7+30 x^5-63 x^2+6 x \\
& \Rightarrow \mathrm{f}^{\prime}(1)=30-56+30-63+6=-53
\end{aligned}
$$
Now, $\lim _{\alpha \rightarrow 0} \frac{f(1-\alpha)-f(1)}{\alpha^3+3 \alpha}$
$$
\begin{aligned}
& =-\lim _{\alpha \rightarrow 0} \frac{f(1-\alpha)-f(1)}{(1-\alpha)-1} \times \frac{1}{\alpha^2+3} \\
& =-f^{\prime}(1) \times \frac{1}{3}=\frac{53}{3}
\end{aligned}
$$

</details>

---

### Q11. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The left-hand derivative of $\mathrm{f}(x)=[x] \sin (\pi x)$, at $x=\mathrm{k}, \mathrm{k}$ is an integer and $[\cdot]$ is the greatest integer function, is

**Options:**

- **(A)** $(-1)^{\mathrm{k}}(\mathrm{k}-1) \pi$
- **(B)** $(-1)^{\mathrm{k}-1}(\mathrm{k}-1) \pi$
- **(C)** $(-1)^{\mathrm{k}} \mathrm{k} \pi$
- **(D)** $(-1)^{\mathrm{k}-1} \mathrm{k} \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-1)^{\mathrm{k}}(\mathrm{k}-1) \pi$**

**Detailed Solution:**

$\begin{aligned} f(x)= & {[x] \sin (\pi x) } \\ \text { LHD } & =\lim _{h \rightarrow 0} \frac{f(k-h)-f(k)}{-h} \\ & =\lim _{h \rightarrow 0} \frac{[k-h] \sin \pi(k-h)-[k] \sin k \pi}{-h} \\ & =\lim _{h \rightarrow 0} \frac{(k-1) \sin (k \pi-\pi h)-k \sin k \pi}{-h} \\ & =\lim _{h \rightarrow 0} \frac{(-1)^{k+1}(k-1) \sinh \pi-0}{-h} \quad \ldots[\because k \in I] \\ & =(-1)^k(k-1) \pi\end{aligned}$

</details>

---

### Q12. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 3} \frac{(1-\cos 2 x) \cdot \sin 5 x}{x^2 \sin 3 x}$ is

**Options:**

- **(A)** $\frac{10}{3}$
- **(B)** $\frac{5}{3}$
- **(C)** $\frac{5}{6}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{10}{3}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} \frac{(1-\cos 2 x) \sin 5 x}{x^2 \sin 3 x} \\ & \lim _{x \rightarrow 0} \frac{(1-\cos 2 x) \sin 5 x \cdot x}{x^3 \cdot \sin 3 x} \\ & \lim _{x \rightarrow 0} \frac{2 \sin ^2 x}{x^2} \cdot \frac{\sin 5 x}{x} \cdot \frac{x}{\sin 3 x} \\ & =2\left(\lim _{x \rightarrow 0} \frac{\sin x}{x}\right)^2 \cdot 5\left(\lim _{x \rightarrow 0} \frac{\sin 5 x}{5 x}\right) \cdot \frac{1}{3}\left(\frac{1}{\lim _{x \rightarrow 0} \frac{\sin 3 x}{3 x}}\right) \\ & =2 \times 1 \times 5 \times 1 \times \frac{1}{3} \times 1=\frac{10}{3}\end{aligned}$

</details>

---

### Q13. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=[x]-\left[\frac{x}{4}\right], x \in R$
Where $[x]$ denotes the greatest integer less than or equal to $x$, then

**Options:**

- **(A)** $\lim _{x \rightarrow 4^{-}} f(x)$ exists, but $\lim _{x \rightarrow 4^{+}} f(x)$ does not exist.
- **(B)** $f(x)$ is continuous at $x=4$.
- **(C)** $\lim _{x \rightarrow 4^{+}} f(x)$ exists, but $\lim _{x \rightarrow 4^{-}} f(x)$ does not exist.
- **(D)** Both $\lim _{x \rightarrow 4^{-}} f(x)$ and $\lim _{x \rightarrow 4^{+}} f(x)$ exist, but are not equal.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $f(x)$ is continuous at $x=4$.**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 4^{-}} f(x)=\left[4^{-}\right]-\left[\frac{4^{-}}{4}\right]=3-0=3 \text { and } \\ & \lim _{x \rightarrow 4^{+}} f(x)=\left[4^{+}\right]-\left[\frac{4^{+}}{4}\right]=4-1=3 \\ & f(4)=[4]-\left[\frac{4}{4}\right]=4-1=3 \\ & \because \lim _{x \rightarrow 4^{-}} f(x)=\lim _{x \rightarrow 4^{+}} f(x)=f(4) \\ & \Rightarrow f(x) ; \text { continuous at } x=4\end{aligned}$

</details>

---

### Q14. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Mrs. Rajni deposited Rs. 10,0000 in a bank that pays $4 \%$ interest compounded continuously then the amount she gets after 10 years is Rs. approximately.
(given $e^{(0.4)}=1.49182$ )

**Options:**

- **(A)** $15150$
- **(B)** $16000$
- **(C)** $14918$
- **(D)** $13000$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $14918$**

**Detailed Solution:**

$\begin{aligned} & \because A=P\left(1+\frac{R}{100}\right) \\ & \Rightarrow A=10000\left(1+\frac{4}{100}\right)^{10}=10000 \times e^{\frac{4}{100} \times 10} \\ & \Rightarrow A=10000 \times e^{0.4}=14918 \quad\left[\because \lim _{x \rightarrow 0}(1+x)^{\frac{1}{x}}=e\right]\end{aligned}$

</details>

---

### Q15. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{2 x}{|x|+x^2}=$

**Options:**

- **(A)** Limit exists
- **(B)** Limit does not exists
- **(C)** $2$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Limit does not exists**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{2 x}{|x|+x^2}$
L.H.L $\lim _{x \rightarrow 0^{-}} \frac{2 x}{-x+x^2}=\lim _{x \rightarrow 0^{-}} \frac{2}{-1+x}=-\infty$
R.H.L $\lim _{x \rightarrow 0^{+}} \frac{2 x}{x+x^2}=\lim _{x \rightarrow 0^{+}} \frac{2}{1+x}=\infty$
$\because$ L.H.L $\neq$ R.H.L $\Rightarrow$ limit does not exist

</details>

---

### Q16. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\lim _{x \rightarrow 1} \frac{x^2-a x+b}{(x-1)}=5$, then $(a+b)$ is equal to

**Options:**

- **(A)** $-3$
- **(B)** $-4$
- **(C)** $7$
- **(D)** $-7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-7$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/sCr7eNemBVHhIbn8bvG_ejsXqExDhRTsk57uq9DZsT4.original.fullsize.png">
Applying $\Rightarrow a=-3$ Hospital's rule
$\begin{aligned} & \Rightarrow 2 \times 1-a=5 \\ & \Rightarrow a=-3\end{aligned}$
from (1) $b=-4$
$\Rightarrow a+b=-7$

</details>

---

