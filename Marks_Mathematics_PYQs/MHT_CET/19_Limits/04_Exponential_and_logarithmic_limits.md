# MHT CET Mathematics - Limits

## Topic 4: Exponential and logarithmic limits

**Total Questions:** 13

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim\limits_{h \to 0} \dfrac{\log_e(1 + 2h) - 2\log_e(1 + h)}{h^2}$

**Options:**

- **(A)** $-1$
- **(B)** $\infty$
- **(C)** $e$
- **(D)** $\dfrac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1$**

**Detailed Solution:**

The given limit is of the form $\dfrac{0}{0}$.

Applying L'Hospital's rule by differentiating the numerator and the denominator with respect to $h$:

$\lim\limits_{h \to 0} \dfrac{\dfrac{2}{1 + 2h} - \dfrac{2}{1 + h}}{2h}$

Simplifying the numerator:

$\dfrac{2}{1 + 2h} - \dfrac{2}{1 + h} = \dfrac{2(1 + h) - 2(1 + 2h)}{(1 + 2h)(1 + h)} = \dfrac{-2h}{(1 + 2h)(1 + h)}$

Substituting this back into the limit:

$\lim\limits_{h \to 0} \dfrac{-2h}{2h(1 + 2h)(1 + h)}$

Canceling $2h$ from the numerator and the denominator:

$\lim\limits_{h \to 0} \dfrac{-1}{(1 + 2h)(1 + h)}$

Substituting $h = 0$:

$\dfrac{-1}{(1 + 0)(1 + 0)} = -1$

Answer: $-1$

</details>

---

### Q2. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x)$ is defined as below
$f(x) = \begin{cases} \dfrac{(3^x + 3^{-x} - 2)\log(1 + 4x)}{(1 - \cos 4x)\tan(2x)}, & x \neq 0 \\ \dfrac{(\log p)^r}{q}, & x = 0 \end{cases}$
is continuous at $x = 0$ then $p + q - r = \ldots$

**Options:**

- **(A)** $0$
- **(B)** $3$
- **(C)** $5$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

For $f(x)$ to be continuous at $x = 0$, we must have $\lim_{x \to 0} f(x) = f(0)$.

$\lim_{x \to 0} \dfrac{(3^x + 3^{-x} - 2)\log(1 + 4x)}{(1 - \cos 4x)\tan(2x)}$

$= \lim_{x \to 0} \dfrac{3^{-x}(3^x - 1)^2 \log(1 + 4x)}{2\sin^2(2x)\tan(2x)}$

Dividing and multiplying by appropriate powers of $x$ to use standard limits:

$= \lim_{x \to 0} 3^{-x} \left(\dfrac{3^x - 1}{x}\right)^2 \cdot \dfrac{\log(1 + 4x)}{4x} \cdot \dfrac{(2x)^2}{\sin^2(2x)} \cdot \dfrac{2x}{\tan(2x)} \cdot \dfrac{4x^3}{2(2x)^2(2x)}$

Using the standard limits $\lim_{x \to 0} \dfrac{a^x - 1}{x} = \log a$, $\lim_{x \to 0} \dfrac{\log(1+x)}{x} = 1$, $\lim_{x \to 0} \dfrac{\sin x}{x} = 1$, and $\lim_{x \to 0} \dfrac{\tan x}{x} = 1$:

$= 1 \cdot (\log 3)^2 \cdot 1 \cdot 1^2 \cdot 1 \cdot \dfrac{4}{16}$

$= \dfrac{(\log 3)^2}{4}$

Given $f(0) = \dfrac{(\log p)^r}{q}$, we equate the two values:

$\dfrac{(\log 3)^2}{4} = \dfrac{(\log p)^r}{q}$

Comparing the terms, we get $p = 3$, $q = 4$, and $r = 2$.

Therefore, $p + q - r = 3 + 4 - 2 = 5$.

Answer: $5$

</details>

---

### Q3. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim\limits_{x \to 0}\left[\dfrac{x \cdot \log(1 + 4x)}{\left(e^{4x} - 1\right)^2}\right] = \cdots$

**Options:**

- **(A)** $\dfrac{1}{4}$
- **(B)** $\dfrac{1}{16}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{1}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{4}$**

**Detailed Solution:**

$\lim\limits_{x \to 0} \left[ \dfrac{x \cdot \log(1 + 4x)}{\left(e^{4x} - 1\right)^2} \right]$

Multiplying and dividing by appropriate powers of $4x$:

$= \lim\limits_{x \to 0} \left[ \dfrac{x \cdot \dfrac{\log(1 + 4x)}{4x} \cdot 4x}{\left(\dfrac{e^{4x} - 1}{4x} \cdot 4x\right)^2} \right]$

$= \lim\limits_{x \to 0} \left[ \dfrac{4x^2 \cdot \dfrac{\log(1 + 4x)}{4x}}{16x^2 \cdot \left(\dfrac{e^{4x} - 1}{4x}\right)^2} \right]$

$= \dfrac{4}{16} \cdot \dfrac{\lim\limits_{x \to 0} \dfrac{\log(1 + 4x)}{4x}}{\left(\lim\limits_{x \to 0} \dfrac{e^{4x} - 1}{4x}\right)^2}$

Using the standard limits $\lim\limits_{u \to 0} \dfrac{\log(1 + u)}{u} = 1$ and $\lim\limits_{u \to 0} \dfrac{e^u - 1}{u} = 1$:

$= \dfrac{1}{4} \cdot \dfrac{1}{(1)^2} = \dfrac{1}{4}$

Answer: $\dfrac{1}{4}$

</details>

---

### Q4. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim\limits_{x \to 0}\dfrac{45^x - 9^x - 5^x + 1}{(k^x - 1)(3^x - 1)} = 2$, then the value of $k$ is ...

**Options:**

- **(A)** $45$
- **(B)** $9$
- **(C)** $5$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

The given limit is $\lim\limits_{x \to 0}\dfrac{45^x - 9^x - 5^x + 1}{(k^x - 1)(3^x - 1)} = 2$

Factorizing the numerator:

$45^x - 9^x - 5^x + 1 = 9^x(5^x - 1) - 1(5^x - 1) = (9^x - 1)(5^x - 1)$

Substituting this back into the limit:

$\lim\limits_{x \to 0}\dfrac{(9^x - 1)(5^x - 1)}{(k^x - 1)(3^x - 1)} = 2$

Dividing the numerator and the denominator by $x^2$:

$\lim\limits_{x \to 0}\dfrac{\dfrac{9^x - 1}{x} \cdot \dfrac{5^x - 1}{x}}{\dfrac{k^x - 1}{x} \cdot \dfrac{3^x - 1}{x}} = 2$

Using the standard limit $\lim\limits_{x \to 0}\dfrac{a^x - 1}{x} = \ln a$, we get:

$\dfrac{\ln 9 \cdot \ln 5}{\ln k \cdot \ln 3} = 2$

Since $\ln 9 = \ln(3^2) = 2 \ln 3$, the equation becomes:

$\dfrac{2 \ln 3 \cdot \ln 5}{\ln k \cdot \ln 3} = 2$

$\dfrac{2 \ln 5}{\ln k} = 2$

$\ln k = \ln 5$

$k = 5$

Answer: $5$

</details>

---

### Q5. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\lim\limits_{x \to 0} \dfrac{(4^x - 1)^3}{\tan\left(\dfrac{x}{4}\right)\log\left(1 + \dfrac{x^2}{3}\right)} = 96(\log a)^b$, then $(a + b) = $

**Options:**

- **(A)** $5$
- **(B)** $7$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5$**

**Detailed Solution:**

The given limit is $\lim\limits_{x \to 0} \dfrac{(4^x - 1)^3}{\tan\left(\dfrac{x}{4}\right)\log\left(1 + \dfrac{x^2}{3}\right)}$.

Dividing the numerator and the denominator by $x^3$, we get:

$\lim\limits_{x \to 0} \dfrac{\left(\dfrac{4^x - 1}{x}\right)^3}{\dfrac{\tan\left(\dfrac{x}{4}\right)}{x} \cdot \dfrac{\log\left(1 + \dfrac{x^2}{3}\right)}{x^2}}$

Using the standard limits $\lim\limits_{x \to 0} \dfrac{a^x - 1}{x} = \log a$, $\lim\limits_{x \to 0} \dfrac{\tan x}{x} = 1$, and $\lim\limits_{x \to 0} \dfrac{\log(1 + x)}{x} = 1$, we can rewrite the limit as:

$\lim\limits_{x \to 0} \dfrac{\left(\dfrac{4^x - 1}{x}\right)^3}{\dfrac{\tan\left(\dfrac{x}{4}\right)}{\dfrac{x}{4}} \cdot \dfrac{1}{4} \cdot \dfrac{\log\left(1 + \dfrac{x^2}{3}\right)}{\dfrac{x^2}{3}} \cdot \dfrac{1}{3}}$

Evaluating the limits, we get:

$\dfrac{(\log 4)^3}{1 \cdot \dfrac{1}{4} \cdot 1 \cdot \dfrac{1}{3}} = 12(\log 4)^3$

Since $\log 4 = \log(2^2) = 2\log 2$, we have:

$12(2\log 2)^3 = 12 \cdot 8(\log 2)^3 = 96(\log 2)^3$

Comparing this with the given expression $96(\log a)^b$, we get $a = 2$ and $b = 3$.

Therefore, $a + b = 2 + 3 = 5$.

Answer: $5$

</details>

---

### Q6. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha(a)$ and $\beta(a)$ be the roots of the equation $(\sqrt[3]{1+a}-1) x^2+(\sqrt{1+a}-1) x+(\sqrt[6]{1+a}-1)=0$ where $a\gt-1$ then $\lim _{a \rightarrow 0^{+}} \alpha(a)$ and $\lim _{a \rightarrow 0^{+}} \beta(a)$ respectively are

**Options:**

- **(A)** 1 and $-\dfrac{5}{2}$
- **(B)** -1 and $-\dfrac{1}{2}$
- **(C)** 2 and $-\dfrac{7}{2}$
- **(D)** 3 and $-\dfrac{9}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -1 and $-\dfrac{1}{2}$**

**Detailed Solution:**

Let $1+a = t^6$. As $a \rightarrow 0^{+}$, $t \rightarrow 1$.

Substituting this in the given equation, we get:

$(t^2-1) x^2+(t^3-1) x+(t-1)=0$

Since $t \rightarrow 1$, $t \neq 1$. Dividing the entire equation by $t-1$, we get:

$(t+1) x^2+(t^2+t+1) x+1=0$

Taking the limit as $t \rightarrow 1$, the equation becomes:

$(1+1) x^2+(1^2+1+1) x+1=0$

$2x^2+3x+1=0$

Factorizing the quadratic equation:

$2x^2+2x+x+1=0$

$(2x+1)(x+1)=0$

The roots are $x=-1$ and $x=-\dfrac{1}{2}$.

Thus, $\lim _{a \rightarrow 0^{+}} \alpha(a)$ and $\lim _{a \rightarrow 0^{+}} \beta(a)$ are $-1$ and $-\dfrac{1}{2}$.

Answer: -1 and $-\dfrac{1}{2}$

</details>

---

### Q7. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow \infty} x^3\left\{\sqrt{x^2+\sqrt{1+x^4}}-x \sqrt{2}\right\}=$

**Options:**

- **(A)** $\frac{1}{\sqrt{2}}$
- **(B)** $\frac{1}{4 \sqrt{2}}$
- **(C)** $\frac{-1}{4 \sqrt{2}}$
- **(D)** $\frac{-1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{4 \sqrt{2}}$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow \infty} x^3\left(\sqrt{x^2+\sqrt{1+x^4}}-x \sqrt{2}\right) \\ & =\lim _{x \rightarrow \infty} \frac{x^3\left(x^2+\sqrt{1+x^4}-2 x^2\right)}{\sqrt{x^2+\sqrt{1+x^4}}+x \sqrt{2}} \\ & =\lim _{x \rightarrow \infty} \frac{x^3\left(\sqrt{1+x^4}-x^2\right)}{\sqrt{x^2+\sqrt{1+x^4}}+x \sqrt{2}} \\ & =\lim _{x \rightarrow \infty} \frac{x^3\left(1+x^4-x^4\right)}{\left(\sqrt{x^2+\sqrt{1+x^4}}+x \sqrt{2}\right)\left(\sqrt{1+x^4}+x^2\right)}\end{aligned}$
$\begin{aligned} & =\lim _{x \rightarrow \infty} \frac{x^3}{x^3\left(\sqrt{1+\sqrt{\frac{1}{x^4}+1}+\sqrt{2}}\right)\left(\sqrt{\frac{1}{x^4}+1}+1\right)} \\ & =\lim _{x \rightarrow \infty} \frac{1}{\left(\sqrt{1+\sqrt{\frac{1}{x^4}+1}+\sqrt{2}}\right)\left(\sqrt{\frac{1}{x^4}+1}+1\right)} \\ & =\frac{1}{(\sqrt{1+1}+\sqrt{2})(1+1)} \\ & =\frac{1}{4 \sqrt{2}}\end{aligned}$

</details>

---

### Q8. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 1} \frac{2^{2 x-2}-2^x+1}{\sin ^2(x-1)}=$

**Options:**

- **(A)** $\frac{1}{2}(\log 2)^2$
- **(B)** $(\log 2)^2$
- **(C)** $2 \log 2$
- **(D)** $2(\log 2)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\log 2)^2$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 1} \frac{2^{2 x-2}-2^x+1}{\sin ^2(x-1)}=\lim _{x \rightarrow 1} \frac{\left(2^{x-1}-1\right)^2}{\sin ^2(x-1)}=\lim _{x \rightarrow 1} \frac{\frac{\left(2^{x-1}-1\right)^2}{(x-1)^2}}{\frac{\sin ^2(x-1)}{(x-1)^2}} \\ & =\frac{(\log 2)^2}{1^2}=(\log 2)^2\end{aligned}$

</details>

---

### Q9. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\lim _{x \rightarrow 0} \frac{27^x-9^x-3^x+1}{\sqrt{5}-\sqrt{4+\cos x}}=$

**Options:**

- **(A)** $8 \sqrt{5} \log 3$
- **(B)** $16 \sqrt{5} \log 3$
- **(C)** $8 \sqrt{5}(\log 3)^2$
- **(D)** $\sqrt{5}(\log 3)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8 \sqrt{5}(\log 3)^2$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0} \frac{27^x-9^x-3^x+1}{\sqrt{5}-\sqrt{4+\cos x}}=\lim _{x \rightarrow 0} \frac{\left(9^x-1\right)\left(3^x-1\right)}{5-(4+\cos x)}\{\sqrt{5}+\sqrt{4+\cos x}\} \\ & =\lim _{x \rightarrow 0} \frac{\left(9^x-1\right)\left(3^x+1\right)}{1-\cos x} \cdot\{\sqrt{5}+\sqrt{4+\cos x}\} \\ & =\lim _{x \rightarrow 0} \frac{\left(9^x-1\right)\left(3^x-1\right)}{2 \sin ^2\left(\frac{x}{2}\right)} \cdot\{\sqrt{5}+\sqrt{4+\cos x}\} \\ & =\lim _{x \rightarrow 0} \frac{\left(\frac{9^x-1}{x}\right)\left(\frac{3^x-1}{x}\right)}{2 \times \frac{\sin ^2 \frac{x}{2}}{\frac{x^2}{4}} \times \frac{1}{4}} \cdot\{\sqrt{5}+\sqrt{4+\cos x}\}\end{aligned}$
$\begin{aligned} & =\frac{\log 9 \cdot \log 3}{\frac{1}{2}}\{\sqrt{5}+\sqrt{5}\} \\ & =2 \log 9 \cdot \log 3 \cdot(2 \sqrt{5}) \\ & =8 \sqrt{5}(\log 3)^2\end{aligned}$

</details>

---

### Q10. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}(x)=\left(\frac{2^{x}-1}{1-3^{x}}\right)$, for $\mathrm{x} \neq 0$ is continuous at $x=0$, then $\mathrm{f}(0)=$

**Options:**

- **(A)** $\cdot \log 3$
- **(B)** $\frac{-(\log 2)}{(\log 3)}$
- **(C)** $\frac{(\log 2)}{(\log 3)}$
- **(D)** $-\log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-(\log 2)}{(\log 3)}$**

**Detailed Solution:**

$f(0)=\lim _{x \rightarrow 0} \frac{2^{x}-1}{-\left(3^{x}-1\right)}=-\frac{\lim _{x \rightarrow 0} \frac{2^{x}-1}{x}}{\lim _{x \rightarrow 0} \frac{3^{x}-1}{x}}=\frac{-\log 2}{\log 3}$

$$
f(0)=\lim _{x \rightarrow 0} \frac{2^{x}-1}{-\left(3^{x}-1\right)}=-\frac{\lim _{x \rightarrow 0} \frac{2^{x}-1}{x}}{\lim _{x \rightarrow 0} \frac{3^{x}-1}{x}}=\frac{-\log 2}{\log 3}
$$

</details>

---

### Q11. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

$\lim _{x \rightarrow 0}\left(\frac{3^{x}-1}{x}\right)$ is equal to

**Options:**

- **(A)** $2 \log 3$
- **(B)** $3 \log 3$
- **(C)** $\log 3$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log 3$**

**Detailed Solution:**

$\lim _{x \rightarrow 0}\left(\frac{3^{x}-1}{x}\right) \quad\left(\frac{0}{0}\right.$ form $)$
Using L' Hospital's rule, $=\lim _{x \rightarrow 0} \frac{3^{x} \log 3-0}{1}=3^{0} \log 3$

</details>

---

### Q12. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim _{x \rightarrow 0} \frac{15^{x}-5^{x}-3^{x}+1}{1-\cos 2 x}$ is

**Options:**

- **(A)** $\frac{(\log 3)(\log 5)}{2}$
- **(B)** $2(\log 3)(\log 5)$
- **(C)** $\frac{\log 3+\log 5}{2}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{(\log 3)(\log 5)}{2}$**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{15^{x}-5^{x}-3^{x}+1}{1-\cos 2 x}$
$=\lim _{x \rightarrow 0} \frac{\left(3^{x}-1\right)\left(5^{x}-1\right)}{1-1+2 \sin ^{2} x}$
$\quad=\lim _{x \rightarrow 0}\left(\frac{3^{x}-1}{x}\right)\left(\frac{5^{x}-1}{x}\right)\left(\frac{x^{2}}{2 \sin ^{2} x}\right)$
$=\frac{1}{2}(\log 3)(\log 5) \cdot 1$
$\quad\left[\because \lim _{x \rightarrow 0}\left(\frac{a^{x}-b^{x}}{x}\right)=\log \left(\frac{a}{b}\right)\right]$

</details>

---

### Q13. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 1}(\log e x)^{1 / \log x}$ is equal to

**Options:**

- **(A)** $e^{-1}$
- **(B)** $e$
- **(C)** $e^{2}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e$**

**Detailed Solution:**

$\begin{aligned} \lim _{x \rightarrow 1}(\log e x)^{1 / \log x} &=\lim _{x \rightarrow 1}[\log e+\log x]^{1 / \log x} \\ &=\lim _{x \rightarrow 1}[1+\log x]^{1 / \log x} \\ &=e^{\lim _{x \rightarrow 1} \frac{\log x}{\log x}}=e \end{aligned}$

</details>

---

