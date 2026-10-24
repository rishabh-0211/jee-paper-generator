# BITSAT Mathematics - Definite Integration

## Topic 2: Definite Integration by Substitution

**Total Questions:** 5

---

### Q1. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_0^{\pi / 4} \cos x e^{\sin x} d x$ is equal to

**Options:**

- **(A)** $e+1$
- **(B)** $e-1$
- **(C)** $e$
- **(D)** $-e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e-1$**

**Detailed Solution:**

Suppose, $I=\int_0^{\pi / 2} \cos x e^{\sin x} d x$
Let $\sin x=t \Rightarrow \cos x d x=d t$
$x \rightarrow 0 \Rightarrow t \rightarrow 0$
and $x \rightarrow \frac{\pi}{2} \Rightarrow t \rightarrow 1$
So $I=\int_0^1 e^t d t=\left[e^t\right]_0^1=e-1$

</details>

---

### Q2. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `2`

$\int_{0}^{\infty} \frac{\mathrm{dx}}{\left(\mathrm{x}^{2}+\mathrm{a}^{2}\right)\left(\mathrm{x}^{2}+\mathrm{b}^{2}\right)}$ is

**Options:**

- **(A)** $\frac{\pi a b}{a+b}$
- **(B)** $\frac{\pi}{2(a+b)}$
- **(C)** $\frac{\pi}{2 a b(a+b)}$
- **(D)** $\frac{\pi(a+b)}{2 a b}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{2 a b(a+b)}$**

**Detailed Solution:**

$\int_{0}^{\infty} \frac{d x}{\left(x^{2}+a^{2}\right)\left(x^{2}+b^{2}\right)}=\frac{1}{b^{2}-a^{2}}$

$\int_{0}^{\infty} \frac{\left(x^{2}+b^{2}\right)-\left(x^{2}+a^{2}\right)}{\left(x^{2}+a^{2}\right)\left(x^{2}+b^{2}\right)}$

$=\frac{1}{b^{2}-a^{2}} \int_{0}^{\infty}\left[\frac{1}{x^{2}+a^{2}}-\frac{1}{x^{2}+b^{2}}\right] d x$

$=\frac{1}{b^{2}-a^{2}}\left[\frac{1}{a} \tan ^{-1} \frac{x}{a}-\frac{1}{b} \tan ^{-1} \frac{x}{b}\right]_{0}^{\infty}$

$=\frac{1}{b^{2}-a^{2}}\left[\frac{\pi}{2 a}-\frac{\pi}{2 b}\right]=\frac{\pi}{2 a b(a+b)}$

</details>

---

### Q3. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `2`

Elvaluate $\int_{0}^{\pi / 2} \frac{\sin x}{1+\cos ^{2} x} d x$

**Options:**

- **(A)** $\pi / 2$
- **(B)** $\pi / 4$
- **(C)** $\pi / 3$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pi / 4$**

**Detailed Solution:**

Let $\mathrm{I}=\int_{0}^{\pi / 2} \frac{\sin \mathrm{x}}{1+\cos ^{2} \mathrm{x}} \mathrm{dx}$

Let $\cos \mathrm{x}=\mathrm{t}$ and $-\sin \mathrm{x} \mathrm{d} \mathrm{x}=\mathrm{dt}$

Now, $\mathrm{x}=0 \Rightarrow \mathrm{t}=\cos 0=1$ and

$\mathrm{x}=\frac{\pi}{2} \Rightarrow \mathrm{t}=\cos \frac{\pi}{2}=0$

$\therefore \quad \mathrm{I}=\int_{1}^{0} \frac{\sin \mathrm{x}}{1+\mathrm{t}^{2}}\left(\frac{-\mathrm{dt}}{\sin \mathrm{x}}\right)=-\int_{1}^{0} \frac{\mathrm{dt}}{1+\mathrm{t}^{2}}$

$=\left[\tan ^{-1} \mathrm{t}\right]_{1}^{0}=-\left[0-\frac{\pi}{4}\right]=\frac{\pi}{4}$

</details>

---

### Q4. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `2`

Evaluate : \(\int_0^1 \frac{\mathrm{dx}}{\sqrt{2-\mathrm{x}^2}}\).

**Options:**

- **(A)** \(\pi / 4\)
- **(B)** \(\pi\)
- **(C)** \(\pi / 2\)
- **(D)** \(\pi / 3\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \(\pi / 4\)**

**Detailed Solution:**

\(\begin{aligned}
& \int \frac{\mathrm{dx}}{\sqrt{2-\mathrm{x}^2}}=\sin ^{-1} \frac{\mathrm{x}}{\sqrt{2}}+\mathrm{c} \\
& \text {So } \int_0^1 \frac{\mathrm{dx}}{\sqrt{2-\mathrm{x}^2}}=\left.\sin ^{-1} \frac{\mathrm{x}}{\sqrt{2}}\right|_0 ^1 \\
= & \sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)+c-\sin ^{-1}(0)-c=\frac{\pi}{4}-0=\frac{\pi}{4}
\end{aligned}\)

</details>

---

### Q5. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `1`

Evaluate: \(\int x \tan ^{-1} x d x\)

**Options:**

- **(A)** \(\frac{1}{2}\left(x^2+1\right) \tan ^{-1} x-\frac{1}{2} x+c\)
- **(B)** \(\frac{1}{2}\left(x^2+1\right) \tan ^{-1} x+\frac{1}{2} x+c\)
- **(C)** \(\frac{1}{2}\left(\mathrm{x}^2-1\right) \tan ^{-1} \mathrm{x}-\frac{1}{2} \mathrm{x}+\mathrm{c}\)
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \(\frac{1}{2}\left(x^2+1\right) \tan ^{-1} x-\frac{1}{2} x+c\)**

**Detailed Solution:**

\(\begin{aligned}
& \int x \tan ^{-1} x d x=\frac{x^2}{2} \tan ^{-1} x-\frac{1}{2} \int \frac{x^2}{1+x^2} d x \\
& =\frac{x^2}{2} \tan ^{-1} x-\frac{1}{2} \int\left[1-\frac{1}{1+x^2}\right] d x \\
& =\frac{1}{2}\left(x^2+1\right) \tan ^{-1} x-\frac{1}{2} x+c
\end{aligned}\)

</details>

---

