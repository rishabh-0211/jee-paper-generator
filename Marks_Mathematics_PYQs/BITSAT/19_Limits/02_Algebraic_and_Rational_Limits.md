# BITSAT Mathematics - Limits

## Topic 2: Algebraic and Rational Limits

**Total Questions:** 6

---

### Q1. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \sqrt{\frac{x-\sin x}{x+\sin ^{2} x}}$ is equal to

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** $\infty$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \sqrt{\frac{x-\sin x}{x+\sin ^{2} x}=\lim _{x \rightarrow 0} \sqrt{\frac{1-\frac{\sin x}{x}}{1+\frac{\sin ^{2} x}{x}}}}$

$=\lim _{x \rightarrow 0} \sqrt{\frac{1-\frac{\sin x}{x}}{1+\left(\frac{\sin x}{x}\right) \sin x}}=\sqrt{\frac{1-1}{1+1 \times 0}}=0$

</details>

---

### Q2. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0} \frac{2 \sin ^{2} 3 x}{x^{2}}$ is equal to

**Options:**

- **(A)** 12
- **(B)** 18
- **(C)** 0
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 18**

**Detailed Solution:**

Consider $\lim _{x \rightarrow 0} \frac{2 \sin ^{2} 3 x}{x^{2}}$

$\begin{array}{l}

=2 \cdot \lim _{x \rightarrow 0}\left[\frac{\sin 3 x}{x}\right]^{2}=2 \cdot \lim _{x \rightarrow 0}\left[3 \frac{\sin 3 x}{3 x}\right]^{2} \\

=2.9 \lim _{x \rightarrow 0}\left(\frac{\sin 3 x}{3 x}\right)^{2}=18 \times 1=18

\end{array}$

</details>

---

### Q3. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

Value of $\lim _{x \rightarrow 0} \frac{a^{\sin x}-1}{\sin x}$ is

**Options:**

- **(A)** $\log \mathrm{a}$
- **(B)** $\sin x$
- **(C)** $\log (\sin x)$
- **(D)** $\cos x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log \mathrm{a}$**

**Detailed Solution:**

We have, $\lim _{x \rightarrow 0} \frac{a^{\sin x}-1}{\sin x}=\lim _{y \rightarrow 0} \frac{a^{y}-1}{y}$ $=\log \mathrm{a}$, where $\mathrm{y}=\sin \mathrm{x}$

$\because \mathrm{x} \rightarrow 0 \Rightarrow \mathrm{y}=\sin \mathrm{x} \rightarrow 0$

</details>

---

### Q4. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{n \rightarrow \infty} \frac{a^{n}+b^{n}}{a^{n}-b^{n}},$ where $a>b>1,$ is equal to

**Options:**

- **(A)** -1
- **(B)** 1
- **(C)** 0
- **(D)** None

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

limit $=\lim _{n \rightarrow \infty} \frac{1+\left(\frac{b}{a}\right)^{n}}{1-\left(\frac{b}{a}\right)^{n}}=1,$

because $0<\frac{b}{a}<1$ implies

$\left(\frac{b}{a}\right)^{n} \rightarrow 0$ as $n \rightarrow \infty$

</details>

---

### Q5. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\left\{\begin{array}{cl}\frac{x^{2}+3 x-10}{x^{2}+2 x-15} & \text { , when } x \neq-5 \\ \text { a }, & \text { when } x=-5\end{array}\right.$

is continuous at $x=-5$, then the value of 'a' will be

**Options:**

- **(A)** $3 / 2$
- **(B)** $7 / 8$
- **(C)** $8 / 7$
- **(D)** $2 / 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $7 / 8$**

**Detailed Solution:**

$\lim _{x \rightarrow-5} f(x)=\frac{(x-2)(x+5)}{(x+5)(x-3)}=\frac{-7}{-8}=\frac{7}{8}$

</details>

---

### Q6. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `1`

$\quad \operatorname{Let} f(x)=\left(x^{5}-1\right)\left(x^{3}+1\right), g(x)=\left(x^{2}-1\right)\left(x^{2}-x+1\right)$

and let $\mathrm{h}(\mathrm{x})$ be such that $\mathrm{f}(\mathrm{x})=\mathrm{g}(\mathrm{x}) \mathrm{h}(\mathrm{x})$. Then

$\operatorname{limh}_{x \rightarrow 1} \mathrm{~h}(\mathrm{x})$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 3
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

Given $f(x)=g(x) h(x)$

$\Rightarrow h(x)=\frac{f(x)}{g(x)}$

$\Rightarrow \lim _{x \rightarrow 1} h(x)=\lim _{x \rightarrow 1} \frac{f(x)}{g(x)}$

$\Rightarrow \lim _{x \rightarrow 1} \frac{\left(x^{5}-1\right)\left(x^{3}+1\right)}{\left(x^{2}-1\right)\left(x^{2}-x+1\right)}$

$=\lim _{x \rightarrow 1} \frac{x^{5}-1^{5}}{x-1}=5 \times 1^{4}=5$

</details>

---

