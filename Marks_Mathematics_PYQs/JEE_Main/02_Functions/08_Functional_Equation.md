# JEE Main Mathematics - Functions

## Topic 8: Functional Equation

**Total Questions:** 42

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $f$ be a polynomial function such that $\log_2(f(x)) = \left(\log_2\left(2+\dfrac{2}{3}+\dfrac{2}{9}+\ldots\infty\right)\right)\cdot\log_3\left(1+\dfrac{f(x)}{f(1/x)}\right)$, $x>0$ and $f(6)=37$. Then $\displaystyle\sum_{n=1}^{10}f(n)$ is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **395**

**Detailed Solution:**

The sum of the infinite geometric progression is given by:

$S = 2 + \dfrac{2}{3} + \dfrac{2}{9} + \ldots \infty = \dfrac{2}{1 - \dfrac{1}{3}} = 3$

Substituting this into the given equation:

$\log_2(f(x)) = \log_2(3) \cdot \log_3\left(1 + \dfrac{f(x)}{f(1/x)}\right)$

Using the base change property $\log_a(b) \cdot \log_b(c) = \log_a(c)$:

$\log_2(f(x)) = \log_2\left(1 + \dfrac{f(x)}{f(1/x)}\right)$

Equating the arguments:

$f(x) = 1 + \dfrac{f(x)}{f(1/x)}$

$f(x)f(1/x) - f(1/x) = f(x)$

$f(x)f(1/x) = f(x) + f(1/x)$

The only polynomial functions satisfying this relation are of the form $f(x) = 1 \pm x^n$.

Given $f(6) = 37$:

$1 \pm 6^n = 37$

Taking the positive sign, $6^n = 36 \Rightarrow n = 2$.

Thus, the polynomial is $f(x) = x^2 + 1$.

The required sum is:

$\sum_{n=1}^{10} f(n) = \sum_{n=1}^{10} (n^2 + 1)$

$\sum_{n=1}^{10} f(n) = \sum_{n=1}^{10} n^2 + \sum_{n=1}^{10} 1$

$\sum_{n=1}^{10} f(n) = \dfrac{10 \times 11 \times 21}{6} + 10$

$\sum_{n=1}^{10} f(n) = 385 + 10 = 395$

Answer: $395$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be a function such that $f(x) + 3f\left(\dfrac{\pi}{2} - x\right) = \sin x$, $x \in \mathbf{R}$. Let the maximum value of $f$ on $\mathbf{R}$ be $\alpha$. If the area of the region bounded by the curves $g(x) = x^2$ and $h(x) = \beta x^3$, $\beta > 0$, is $\alpha^2$, then $30\beta^3$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

Given $f(x) + 3f\left(\dfrac{\pi}{2} - x\right) = \sin x$

Replacing $x$ with $\dfrac{\pi}{2} - x$, we get:

$f\left(\dfrac{\pi}{2} - x\right) + 3f(x) = \sin\left(\dfrac{\pi}{2} - x\right) = \cos x$

Multiplying this equation by $3$ and subtracting the first equation gives:

$9f(x) - f(x) = 3\cos x - \sin x$

$8f(x) = 3\cos x - \sin x$

$f(x) = \dfrac{3\cos x - \sin x}{8}$

The maximum value of $f(x)$ is $\alpha = \dfrac{\sqrt{3^2 + (-1)^2}}{8} = \dfrac{\sqrt{10}}{8}$.

Thus, $\alpha^2 = \dfrac{10}{64} = \dfrac{5}{32}$.

The points of intersection of the curves $g(x) = x^2$ and $h(x) = \beta x^3$ are given by:

$x^2 = \beta x^3 \Rightarrow x^2(1 - \beta x) = 0 \Rightarrow x = 0, x = \dfrac{1}{\beta}$

The area of the region bounded by the curves is:

$\int_{0}^{1/\beta} (x^2 - \beta x^3) dx = \left[ \dfrac{x^3}{3} - \dfrac{\beta x^4}{4} \right]_{0}^{1/\beta}$

$= \dfrac{1}{3\beta^3} - \dfrac{1}{4\beta^3} = \dfrac{1}{12\beta^3}$

Given that the area is $\alpha^2$, we have:

$\dfrac{1}{12\beta^3} = \dfrac{5}{32}$

$\beta^3 = \dfrac{32}{60} = \dfrac{8}{15}$

Therefore, $30\beta^3 = 30 \times \dfrac{8}{15} = 16$.

Answer: $16$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let for some $\alpha \in \mathbb{R}$, $f:\mathbb{R}\rightarrow\mathbb{R}$ be a function satisfying $f(x+y)=f(x)+2y^2+y+\alpha xy$ for all $x,y \in \mathbb{R}$. If $f(0)=-1$ and $f(1)=2$, then the value of $\sum_{n=1}^{5}(\alpha+f(n))$ is:

**Options:**

- **(A)** $110$
- **(B)** $140$
- **(C)** $150$
- **(D)** $170$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $140$**

**Detailed Solution:**

Given $f(x+y) = f(x) + 2y^2 + y + \alpha xy$

Substituting $x = 0$ and replacing $y$ with $x$, we get:

$f(x) = f(0) + 2x^2 + x + \alpha(0)x$

Since $f(0) = -1$, we have:

$f(x) = 2x^2 + x - 1$

To find $\alpha$, substitute $f(x)$ into the original functional equation:

$2(x+y)^2 + (x+y) - 1 = (2x^2 + x - 1) + 2y^2 + y + \alpha xy$

$2x^2 + 4xy + 2y^2 + x + y - 1 = 2x^2 + x - 1 + 2y^2 + y + \alpha xy$

Comparing both sides, we get $\alpha = 4$.

We need to find the value of $\sum_{n=1}^{5}(\alpha+f(n))$:

$\sum_{n=1}^{5}(4 + 2n^2 + n - 1) = \sum_{n=1}^{5}(2n^2 + n + 3)$

$= 2\sum_{n=1}^{5}n^2 + \sum_{n=1}^{5}n + \sum_{n=1}^{5}3$

$= 2\left(\dfrac{5 \times 6 \times 11}{6}\right) + \dfrac{5 \times 6}{2} + 3 \times 5$

$= 2(55) + 15 + 15$

$= 110 + 30 = 140$

Answer: $140$

</details>

---

### Q4. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ be a function such that $3 f(x)+2 f\left(\frac{m}{19 x}\right)=5 x, x \neq 0$, where $m=\sum_{i=1}^{9}(i)^{2}$. Then $f(5)-f(2)$ is equal to

**Options:**

- **(A)** 18
- **(B)** 36
- **(C)** 9
- **(D)** -9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 18**

**Detailed Solution:**

$m = \sum_{i=1}^{9} i^2 = \frac{9 \cdot 10 \cdot 19}{6} = 285$, so $\frac{m}{19} = 15$.
The equation becomes $3f(x) + 2f\left(\frac{15}{x}\right) = 5x$ ...(i)
Replace $x$ by $\frac{15}{x}$: $3f\left(\frac{15}{x}\right) + 2f(x) = \frac{75}{x}$ ...(ii)
From $3 \times (i) - 2 \times (ii)$: $5f(x) = 15x - \frac{150}{x}$, so $f(x) = 3x - \frac{30}{x}$.
$f(5) = 15 - 6 = 9$, $f(2) = 6 - 15 = -9$.
$f(5) - f(2) = 9 - (-9) = 18$.

</details>

---

### Q5. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ and $g$ be functions satisfying $f(x+y)=f(x) f(y), f(1)=7$ and $g(x+y)=g(x y), g(1)=1$, for all $x, y \in \mathbf{N}$. If $\sum_{x=1}^{\mathrm{n}}\left(\frac{f(x)}{\mathrm{g}(x)}\right)=19607$, then n is equal to:

**Options:**

- **(A)** 7
- **(B)** 6
- **(C)** 4
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

$f(x+y)=f(x)f(y)$ with $f(1)=7$ gives $f(x)=7^x$.
For $g$: put $y=1$ in $g(x+y)=g(xy)$ to get $g(x+1)=g(x)$. 
So $g(x)=g(1)=1$ for all $x \in \mathbb{N}$.
$\sum_{x=1}^{n}\frac{f(x)}{g(x)}=\sum_{x=1}^{n}7^x=\frac{7(7^n-1)}{6}=19607$
$7^{n+1}-7=117642$
$ \Rightarrow 7^{n+1}=117649=7^6$
$n+1=6 \Rightarrow n=5$

</details>

---

### Q6. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)+2 f\left(\frac{1}{x}\right)=x^2+5$ and $2 g(x)-3 g\left(\frac{1}{2}\right)=x, x \gt 0$. If $\alpha=\int_1^2 f(x) d x$, and $\beta=\int_1^2 g(x) d x$, then the value of $9 \alpha+\beta$ is:

**Options:**

- **(A)** $1$
- **(B)** $0$
- **(C)** $10$
- **(D)** $11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $11$**

**Detailed Solution:**

$\begin{aligned}
& f(x)+2 f\left(\frac{1}{x}\right)=x^2+5 \\
& f\left(\frac{1}{x}\right)+2 f(x)=\frac{1}{x^2}+5 \\
& f(x)=\frac{2}{3 x^2}-\frac{x^2}{3}+\frac{5}{3} \\
& \alpha=\int_1^2\left(\frac{2}{3 x^2}-\frac{x^2}{3}+\frac{5}{3}\right) \mathrm{dx} \\
& \left(-\frac{2}{3 x}-\frac{x^3}{9}+\frac{5 x}{3}\right)_1^2 \\
& -\frac{1}{3}-\frac{8}{9}+\frac{10}{3}+\frac{2}{3}+\frac{1}{9}-\frac{5}{3} \\
& \alpha=2-\frac{7}{9}=\frac{11}{9} \\
& 2 g(x)-3 g\left(\frac{1}{2}\right)=x \\
& \mathrm{~g}\left(\frac{1}{2}\right)=-\frac{1}{2} \\
& \mathrm{~g}(\mathrm{x})=\frac{\mathrm{x}}{2}-\frac{3}{4} \\
& \beta=\int_1^2\left(\frac{x}{2}-\frac{3}{4}\right) d x \\
& \left(\frac{x^2}{4}-\frac{3 x}{4}\right)_1^2=1-\frac{3}{2}-\frac{1}{4}+\frac{3}{4}=0 \\
& 9 \alpha+\beta=11 \\
& \text { option (4) }
\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be a continuous function satisfying $f(0)=1$ and $f(2 \mathrm{x})-f(\mathrm{x})=\mathrm{x}$ for all $\mathrm{x} \in \mathbb{R}$. If $\lim _{n \rightarrow \infty}\left\{f(x)-f\left(\frac{x}{2^n}\right)\right\}=G(x)$, then $\sum_{r=1}^{10} G\left(r^2\right)$ is equal to

**Options:**

- **(A)** 540
- **(B)** 385
- **(C)** 420
- **(D)** 215

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 385**

**Detailed Solution:**

$\begin{aligned}
& f(2 x)-f(x)=x \\
& f(x)-f\left(\frac{x}{2}\right)=\frac{x}{2} \\
& \mathrm{f}\left(\frac{\mathrm{x}}{2}\right)-\mathrm{f}\left(\frac{\mathrm{x}}{4}\right)=\frac{\mathrm{x}}{4} \\
& \mathrm{f}\left(\frac{\mathrm{x}}{4}\right)-\mathrm{f}\left(\frac{\mathrm{x}}{8}\right)=\frac{\mathrm{x}}{8} \\
& f\left(\frac{x}{2^{n-1}}\right)-f\left(\frac{x}{2^n}\right)=\frac{x}{2^n} \\
& f(2 x)-f\left(\frac{x}{2^n}\right)=x\left\{\frac{1-\left(\frac{1}{2}\right)^{n-1}}{1-\frac{1}{2}}\right\} \\
& f(x)-f\left(\frac{x}{2^n}\right)=2 x\left(1-\left(\frac{1}{2}\right)^{n+1}\right) \\
& \mathrm{f}(\mathrm{x})+\mathrm{x}-\mathrm{f}\left(\frac{\mathrm{x}}{2^{\mathrm{n}}}\right)=2 \mathrm{x}\left(1-\left(\frac{1}{2}\right)^{\mathrm{n}+1}\right) \\
& \lim _{n \rightarrow \infty}\left(f(x)-f\left(\frac{x}{2^n}\right)\right)=\lim _{n \rightarrow \infty}\left(2 x\left(1-\left(\frac{1}{2}\right)^{n+1}\right)-x\right) \\
& G(x)=x \\
& \sum_{r=1}^{10} G\left(r^2\right)=\sum_{r=1}^{10} r^2=385
\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $f$ be a function such that $f(x)+3 f\left(\frac{24}{x}\right)$ $=4 x, x \neq 0$. Then $f(3)+f(8)$ is equal to

**Options:**

- **(A)** $11$
- **(B)** $10$
- **(C)** $12$
- **(D)** $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $11$**

**Detailed Solution:**

$f(x)+3 f\left(\frac{24}{x}\right)=4 x$
Put $x=3 \quad f(3)+3 f(8)=12$
Put $x=8 \quad f(8)+3 f(3)=32$
Add both $\quad 4(\mathrm{f}(3)+\mathrm{f}(8))=44$
$f(3)+f(8)=11$

</details>

---

### Q9. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: \mathbf{R}-\{0\} \rightarrow(-\infty, 1)$ be a polynomial of degree 2, satisfying $f(x) f\left(\frac{1}{x}\right)=f(x)+f\left(\frac{1}{x}\right)$. If $f(K)=-2 K$, then the sum of squares of all possible values of $K$ is :

**Options:**

- **(A)** $7$
- **(B)** $6$
- **(C)** $1$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6$**

**Detailed Solution:**

as $f(x)$ is a polynomial of degree two let it be
$f(x)=a x^2+b x+c \quad(a \neq 0)$
on satisfying given conditions we get
$C=1 \& a= \pm 1$
hence $f(x)=1 \pm x^2$
also range $\in(-\infty, 1]$ hence
$f(x)=1-x^2$
now $f(k)=-2 k$
$1-\mathrm{k}^2=-2 \mathrm{k} \rightarrow \mathrm{k}^2-2 \mathrm{k}-1=0$
let roots of this equation be $\alpha \& \beta$ then $\alpha^2+\beta^2=(\alpha+\beta)^2-2 \alpha \beta$
$=4-2(-1)=6$

</details>

---

### Q10. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=\frac{2^{x+2}+16}{2^{2 x+1}+2^{x+4}+32}$. Then the value of $8\left(f\left(\frac{1}{15}\right)+f\left(\frac{2}{15}\right)+\ldots+f\left(\frac{59}{15}\right)\right)$ is equal to

**Options:**

- **(A)** $92$
- **(B)** $118$
- **(C)** $102$
- **(D)** $108$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $118$**

**Detailed Solution:**

$\begin{aligned}
& f(x)=\frac{42^x+16}{2.2^{2 x}+16.2^x+32} \\
& f(x)=\frac{2\left(2^x+4\right)}{2^{2 x}+8.2^x+16} \\
& f(x)=\frac{2}{2^x+4} \\
& f(4-x)=\frac{2^x}{2\left(2^x+4\right)} \\
& f(x)+f(4-x)=\frac{1}{2}
\end{aligned}$

So, $\quad \mathrm{f}\left(\frac{1}{15}\right)+\mathrm{f}\left(\frac{59}{15}\right)=\frac{1}{2}$
$\begin{aligned}
& \text { Similarly }=f\left(\frac{29}{15}\right)+f\left(\frac{31}{15}\right)=\frac{1}{2} \\
& f\left(\frac{30}{15}\right)=f(2)=\frac{2}{2^2+4}=\frac{2}{8}=\frac{1}{4} \\
& \Rightarrow 8\left(29 \times \frac{1}{2}+\frac{1}{4}\right)
\end{aligned}$

Ans. 118

</details>

---

### Q11. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

If a function $f$ satisfies $f(\mathrm{~m}+\mathrm{n})=f(\mathrm{~m})+f(\mathrm{n})$ for all $\mathrm{m}, \mathrm{n} \in \mathbf{N}$ and $f(1)=1$, then the largest natural number $\lambda$ such that $\sum_{k=1}^{2022} f(\lambda+k) \leq(2022)^2$ is equal to _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1010**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(\mathrm{m}+\mathrm{n})=\mathrm{f}(\mathrm{m})+\mathrm{f}(\mathrm{n}) \\
& \Rightarrow \mathrm{f}(\mathrm{x})=\mathrm{kx} \\
& \Rightarrow \mathrm{f}(1)=1 \\
& \Rightarrow \mathrm{k}=1 \\
& \mathrm{f}(\mathrm{x})=\mathrm{x}
\end{aligned}$
Now
$\sum_{\mathrm{k}=1}^{2022} \mathrm{f}(\lambda+\mathrm{k}) \leq(2022)^2$
$\begin{aligned} & \Rightarrow \sum_{\mathrm{k}=1}^{2022}(\lambda+\mathrm{k}) \leq(2022)^2 \\ & \Rightarrow 2022 \lambda+\frac{2022 \times 2023}{2} \leq(2022)^2\end{aligned}$
$\begin{aligned}
& \Rightarrow \lambda \leq 2022-\frac{2023}{2} \\
& \Rightarrow \lambda \leq 1010.5
\end{aligned}$
$\therefore$ largest natural no. $\lambda$ is 1010 .

</details>

---

### Q12. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the differentiable function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mo>{</mo><mn>0</mn><mo>}</mo><mo>-</mo><mi mathvariant="normal">&#8477;</mi><mo>,</mo></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mn>10</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>29</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>-</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Eliminating <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mi>x</mi></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>10</mn></math></p><p>Let us replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>3</mn></mfrac><mo>-</mo><mn>2</mn><mfenced><mn>3</mn></mfenced><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>48</mn><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>+</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mn>13</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q13. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>4</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>+</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>+</mo><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>-</mo><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>-</mo><mn>6</mn></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>4</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mn>4</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Eliminating <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>5</mn><mi>x</mi></mfrac><mo>+</mo><mn>15</mn><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>5</mn><mi>x</mi></mfrac><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>18</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>10</mn><mi>x</mi></mfrac><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>18</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mfenced><mrow><mfrac><mn>10</mn><mi>x</mi></mfrac><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>18</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mn>10</mn><mi>log</mi><mi>x</mi><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>18</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mn>10</mn><mi>log</mi><mn>2</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>10</mn><mi>log</mi><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>18</mn><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>10</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><mn>6</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q14. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mi>x</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>3</mn></mfenced></math></p><p>On subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> and equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>-</mo><mi>f</mi><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>4</mn><mo>)</mo></math></p><p>On adding equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q15. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math>, If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>320</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mn>5</mn></munderover><mi>f</mi><mfenced><mi>n</mi></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6875</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6575</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6825</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6528</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6825</mn></math>**

**Detailed Solution:**

<p>Given, equation is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>f</mi><msup><mfenced><mn>0</mn></mfenced><mn>2</mn></msup><mo>&#8658;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>5</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, then we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced></mrow><mrow><mi>f</mi><mfenced><mn>0</mn></mfenced></mrow></mfrac><mo>&#183;</mo><mfrac><mrow><mi>f</mi><mfenced><mn>2</mn></mfenced></mrow><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced></mrow></mfrac><mo>&#183;</mo><mfrac><mrow><mi>f</mi><mfenced><mn>3</mn></mfenced></mrow><mrow><mi>f</mi><mfenced><mn>2</mn></mfenced></mrow></mfrac><mo>=</mo><msup><mfenced><mfrac><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced></mrow><mn>5</mn></mfrac></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>320</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><msup><mfenced><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced><mn>3</mn></msup><msup><mn>5</mn><mn>3</mn></msup></mfrac><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>5</mn><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>20</mn><mo>&#183;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>4</mn><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>4</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>4</mn><mo>&#183;</mo><mn>5</mn><mspace linebreak="newline"/><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>4</mn><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mn>4</mn><mn>2</mn></msup><mo>&#183;</mo><mn>5</mn><mspace linebreak="newline"/><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>4</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><msup><mn>4</mn><mn>3</mn></msup><mo>&#183;</mo><mn>5</mn><mspace linebreak="newline"/><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>4</mn><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><msup><mn>4</mn><mn>4</mn></msup><mo>&#183;</mo><mn>5</mn><mspace linebreak="newline"/><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>=</mo><mn>4</mn><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><msup><mn>4</mn><mn>5</mn></msup><mo>&#183;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mn>5</mn></munderover><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mn>5</mn><mo>+</mo><mn>5</mn><mo>&#183;</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>&#183;</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><mn>5</mn><mo>&#183;</mo><msup><mn>4</mn><mn>3</mn></msup><mo>+</mo><mn>5</mn><mo>&#183;</mo><msup><mn>4</mn><mn>4</mn></msup><mo>+</mo><mn>5</mn><mo>&#183;</mo><msup><mn>4</mn><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mn>5</mn></munderover><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfrac><mrow><mn>5</mn><mfenced><mrow><msup><mn>4</mn><mn>6</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>3</mn></mfrac><mo>=</mo><mn>6825</mn></math></p>

</details>

---

### Q16. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>:</mo><mi mathvariant="normal">&#8469;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math>, satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>3</mn><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>;</mo><mi>x</mi><mo>&#8805;</mo><mn>2</mn></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>f</mi><mfenced><mn>2022</mn></mfenced></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mi>f</mi><mfenced><mn>2028</mn></mfenced></mstyle></mfrac></math> is equal to</p><p> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8200</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8000</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8400</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8100</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8100</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>3</mn><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>3</mn><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>f</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>f</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>6</mn><mi>f</mi><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><mn>4</mn><mi>f</mi><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>9</mn><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>3</mn><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>16</mn><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p>Hence, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>f</mi><mfenced><mn>2022</mn></mfenced></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>f</mi><mfenced><mn>2028</mn></mfenced></mrow></mfrac><mo>=</mo><mn>4044</mn><mo>+</mo><mn>4056</mn><mo>=</mo><mn>8100</mn></math></p>

</details>

---

### Q17. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a differentiable function that satisfies the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>f</mi><mo>(</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>|</mo></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Given,</p><p>Functional equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>-</mo><mn>1</mn></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math> in above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>0</mn><mo>+</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p>Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>h</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mi>h</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>h</mi></mfenced><mo>-</mo><mn>1</mn><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mi>h</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>h</mi></mfenced><mo>-</mo><mn>1</mn></mrow><mi>h</mi></mfrac></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>h</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>h</mi></mfenced><mo>-</mo><mn>1</mn></mrow><mi>h</mi></mfrac><mo>=</mo><mi>k</mi></math></p><p>So, the equation becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>k</mi></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> in above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>k</mi><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>2</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as&#160;given&#160;</mtext><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now integrate both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Now again taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>+</mo><mi>c</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as&#160;</mtext><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q18. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The number of functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo><mo>&#8594;</mo><mo>{</mo><mi mathvariant="normal">a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi><mo>:</mo><mo>|</mo><mi mathvariant="normal">a</mi><mo>|</mo><mo>&#8804;</mo><mn>8</mn><mo>}</mo></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi mathvariant="normal">n</mi><mo>)</mo><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">n</mi></mfrac><mi>f</mi><mo>(</mo><mi mathvariant="normal">n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#8704;</mo><mo>&#160;</mo><mi mathvariant="normal">n</mi><mo>&#8712;</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>}</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi mathvariant="normal">n</mi><mo>)</mo><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">n</mi></mfrac><mi>f</mi><mo>(</mo><mi mathvariant="normal">n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#8704;</mo><mo>&#160;</mo><mi mathvariant="normal">n</mi><mo>&#8712;</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mi>f</mi><mo>(</mo><mi mathvariant="normal">n</mi><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mi mathvariant="normal">n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>n</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>1</mn></math>    ....(1)</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>2</mn></math>    ....(2)</p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>3</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mn>3</mn></math>      ....(3)</p><p>Put the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo></math> from equation (1) in equation (2),</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>(</mo><mn>1</mn><mo>-</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>2</mn><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math>       ....(4)</p><p>Put the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo></math> from equation (4) in equation (3),</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>(</mo><mn>2</mn><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mn>3</mn><mo>-</mo><mn>6</mn><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math>    </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>f</mi><mo>:</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo><mo>&#8594;</mo><mo>{</mo><mi mathvariant="normal">a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi><mo>:</mo><mo>|</mo><mi mathvariant="normal">a</mi><mo>|</mo><mo>&#8804;</mo><mn>8</mn><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>8</mn><mo>&#8804;</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>&#8804;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>8</mn><mo>&#8804;</mo><mn>3</mn><mo>-</mo><mn>6</mn><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#8804;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>11</mn><mo>&#8804;</mo><mo>-</mo><mn>6</mn><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#8804;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mn>6</mn></mfrac><mo>&#8804;</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#8804;</mo><mfrac><mn>11</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math></p><p>Case I: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mn>3</mn></math></p><p>Case II: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>Therefore, two such functions are possible.</p>

</details>

---

### Q19. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced><mo>-</mo><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mn>3</mn></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>3</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>0</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math>**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>-</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>6</mn></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>-</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>a</mi><mo>=</mo><mi>b</mi><mo>+</mo><mn>3</mn></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>12</mn><mo>-</mo><mn>2</mn><mi>a</mi><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mo>-</mo><mn>2</mn><mi>a</mi><mo>=</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>a</mi><mo>=</mo><mn>15</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>6</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>c</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>6</mn></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>6</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>27</mn><mo>-</mo><mn>27</mn><mo>+</mo><mn>18</mn><mo>-</mo><mn>6</mn><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>8</mn><mo>-</mo><mn>12</mn><mo>+</mo><mn>12</mn><mo>-</mo><mn>6</mn><mo>+</mo><mn>1</mn><mo>-</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math></p>

</details>

---

### Q20. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#8712;</mo><mi mathvariant="normal">N</mi></math>, If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><mi>k</mi></mfenced><mo>=</mo><mn>3279</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math> </p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><msup><mn>3</mn><mn>2</mn></msup></math></p><p>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><msup><mn>3</mn><mn>2</mn></msup><mo>&#215;</mo><mn>3</mn><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup></math></p><p>And so on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><msup><mn>3</mn><mi>n</mi></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><mi>r</mi></mfenced><mo>=</mo><mn>3279</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mn>3279</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>3</mn><mi>n</mi></msup><mo>=</mo><mn>3279</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>&#215;</mo><mfrac><mrow><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>3279</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>1093</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>2186</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mi>n</mi></msup><mo>=</mo><mn>2187</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mi>n</mi></msup><mo>=</mo><msup><mn>3</mn><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q21. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mrow><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn></mrow></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math>,  then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>3</mn><mn>2023</mn></mfrac></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>f</mi><mfenced><mfrac><mn>2022</mn><mn>2023</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2011</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1010</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2010</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1011</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1011</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mrow><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn></mrow></mfrac></math>,</p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><msup><mn>2</mn><mrow><mn>2</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mrow><msup><mn>2</mn><mrow><mn>2</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mrow><mn>2</mn><mo>+</mo><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mrow><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>2</mn><mo>+</mo><msup><mn>2</mn><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>So by using the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math> we will solve the given equation </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>3</mn><mn>2023</mn></mfrac></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>f</mi><mfenced><mfrac><mn>2022</mn><mn>2023</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2022</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2021</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>3</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2020</mn><mn>2023</mn></mfrac></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>f</mi><mfenced><mfrac><mn>1011</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1012</mn><mn>2023</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><munder><mrow><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2022</mn><mn>2023</mn></mfrac></mfenced></mrow><mo>&#9183;</mo></munder><mn>1</mn></munder><mo>+</mo><munder><munder><mrow><mi>f</mi><mfenced><mfrac><mn>2</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2021</mn><mn>2023</mn></mfrac></mfenced></mrow><mo>&#9183;</mo></munder><mn>1</mn></munder><mo>+</mo><munder><munder><mrow><mi>f</mi><mfenced><mfrac><mn>3</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2020</mn><mn>2023</mn></mfrac></mfenced></mrow><mo>&#9183;</mo></munder><mn>1</mn></munder><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><munder><munder><mrow><mi>f</mi><mfenced><mfrac><mn>1011</mn><mn>2023</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1012</mn><mn>2023</mn></mfrac></mfenced></mrow><mo>&#9183;</mo></munder><mn>1</mn></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>1011</mn><mo>&#160;</mo><mtext>times</mtext><mo>=</mo><mn>1011</mn></math></p>

</details>

---

### Q22. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>4</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>14</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>23</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>4</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>14</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is equal to</p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mn>3</mn><mo>+</mo><mi>&#955;</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>7</mn><mo>-</mo><mi>&#955;</mi><mo>=</mo><mi>c</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>4</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mi>&#955;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>iii</mi></mfenced></math></p><p>Now subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced><mo>-</mo><mfenced><mi>iii</mi></mfenced></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mo>-</mo><mi>&#955;</mi></mrow><mn>5</mn></mfrac></math>, now putting  in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mo>-</mo><mi>&#955;</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mn>7</mn><mo>-</mo><mi>&#955;</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>&#955;</mi><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q23. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a continuous function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mn>7</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>14</mn></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math></p><p>Now replance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mtext>by&#160;</mtext><mfrac><mi>x</mi><mn>3</mn></mfrac></math>  infinite times,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mfrac><mi>x</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>x</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>x</mi><mn>3</mn></mfrac></mfenced><mo>-</mo><mi>f</mi><mfenced><mfrac><mi>x</mi><msup><mn>3</mn><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mfrac><mi>x</mi><msup><mn>3</mn><mn>2</mn></msup></mfrac><mspace linebreak="newline"></mspace><mo>.</mo><mspace linebreak="newline"></mspace><mo>.</mo></math></p><p>On adding, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>f</mi><mfenced><mfrac><mi>x</mi><msup><mn>3</mn><mi>n</mi></msup></mfrac></mfenced><mo>=</mo><mi>x</mi><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo><mo>+</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><munder><mi>lim</mi><mrow><mi>n</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>f</mi><mfenced><mfrac><mi>x</mi><msup><mn>3</mn><mi>n</mi></msup></mfrac></mfenced><mo>=</mo><mi>x</mi><mfenced><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></mrow></mfrac></mfenced><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mn>7</mn></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>8</mn></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>4</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>+</mo><mn>3</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>14</mn></mfenced><mo>=</mo><mn>10</mn></math></p></blockquote>

</details>

---

### Q24. JEE Main 2022 (29 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>,</mo><mi>k</mi><mo>&#8712;</mo><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>c</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mi>x</mi><mo>+</mo><mn>2</mn><mi>k</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>-</mo><mi>x</mi><mi>y</mi></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mn>2</mn><mfenced><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mi>f</mi><mfenced><mn>20</mn></mfenced></mrow></mfenced></mrow></mfenced></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3395**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>c</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mi>x</mi><mo>+</mo><mn>2</mn><mi>k</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mi>i</mi></mfenced></math></p><p>&amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>-</mo><mi>x</mi><mi>y</mi><mo>&#160;&#160;</mo><mo>&#8704;</mo><mi>x</mi><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mi>c</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>c</mi><mn>2</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>y</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mi>y</mi></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>y</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>-</mo><mi>x</mi><mi>y</mi></mrow><mi>y</mi></mfrac><mo>=</mo><munder><mi>lim</mi><mrow><mi>y</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>y</mi></mfenced></mrow><mi>y</mi></mfrac><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mo>-</mo><mi>x</mi></math></p><p>Integrating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>0</mn></mfenced><mi>x</mi><mo>+</mo><mi>&#955;</mi></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>c</mi><mn>2</mn></msup></math></p><p>Now comparing equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mi>x</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>&#183;</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mi>x</mi><mo>=</mo><mfrac><mrow><mn>20</mn><mfenced><mn>21</mn></mfenced><mfenced><mn>41</mn></mfenced></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced><mfrac><mrow><mn>20</mn><mfenced><mn>21</mn></mfenced></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2870</mn><mo>+</mo><mn>525</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3395</mn></math></p>

</details>

---

### Q25. JEE Main 2022 (27 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function defined <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mi>e</mi></mrow></mfrac></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>100</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2</mn><mn>100</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>3</mn><mn>100</mn></mfrac></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>99</mn><mn>100</mn></mfrac></mfenced></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **99**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mi>e</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced></mrow></msup></mrow><mrow><msup><mi>e</mi><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced></mrow></msup><mo>+</mo><mi>e</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>e</mi></mrow><mrow><mi>e</mi><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math> </p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>100</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>99</mn><mn>100</mn></mfrac></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>100</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2</mn><mn>100</mn></mfrac></mfenced><mo>+</mo><mn>...</mn><mi>f</mi><mfenced><mfrac><mn>99</mn><mn>100</mn></mfrac></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>49</mn><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>50</mn><mn>100</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>98</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>99</mn></math></p>

</details>

---

### Q26. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="bold-italic">N</mi><mo>&#8594;</mo><mi mathvariant="bold-italic">R</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></math> for natural numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mfrac><mn>512</mn><mn>3</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math> holds, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math>  in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup></math>, Similarly</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><msup><mn>2</mn><mn>5</mn></msup><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>Now</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mn>2</mn><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>k</mi></mfenced><mo>=</mo><mfrac><mn>512</mn><mn>3</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>2</mn><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced><mi>k</mi></mfenced><mo>=</mo><mfrac><mn>512</mn><mn>3</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>2</mn><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mfenced open="{" close="}"><mrow><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#8943;</mo><mi>f</mi><mfenced><mn>10</mn></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>512</mn><mn>3</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>2</mn><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>5</mn></msup><mo>&#8230;</mo></mrow></mfenced><mo>=</mo><mfrac><mn>512</mn><mn>3</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mfrac><mrow><mn>2</mn><mfenced><mrow><msup><mfenced><msup><mn>2</mn><mn>2</mn></msup></mfenced><mn>10</mn></msup><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>&#8722;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>512</mn><mn>3</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>&#215;</mo><mfrac><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>512</mn><mn>3</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>20</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now comparing both side we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><mn>512</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><mn>128</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>4</mn></math>.</p>

</details>

---

### Q27. JEE Main 2021 (01 Sep Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be a polynomial of degree <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>k</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mi>k</mi></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>.</mo></math> Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn><mo>-</mo><mn>10</mn><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>10</mn><mo>)</mo></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **26**

**Detailed Solution:**

<p>Given that: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>f</mi><mo>(</mo><mi>k</mi><mo>)</mo><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math> which means <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>k</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>5</mn><mo>)</mo></math> are the factors of this expression.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>f</mi><mo>(</mo><mi>k</mi><mo>)</mo><mo>+</mo><mn>2</mn><mo>=</mo><mi>a</mi><mo>(</mo><mi>k</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>4</mn><mo>)</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>5</mn><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>u</mi><mi>t</mi><mo>&#160;</mo><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>=</mo><mi>a</mi><mo>(</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mo>-</mo><mn>4</mn><mo>)</mo><mo>(</mo><mo>-</mo><mn>5</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>f</mi><mo>(</mo><mi>k</mi><mo>)</mo><mo>+</mo><mn>2</mn><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac><mo>(</mo><mi>k</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>4</mn><mo>)</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>5</mn><mo>)</mo></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>f</mi><mo>(</mo><mn>10</mn><mo>)</mo><mo>+</mo><mn>2</mn><mo>=</mo><mfrac><mn>1</mn><mn>60</mn></mfrac><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>10</mn><mo>)</mo><mo>=</mo><mn>26</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn><mo>-</mo><mn>10</mn><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>10</mn><mo>)</mo><mo>=</mo><mn>26</mn></math></p>

</details>

---

### Q28. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>m</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>n</mi></mfenced></math> for every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>6</mn></mfenced><mo>=</mo><mn>18</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn></math>**

**Detailed Solution:**

<p>Given functional equation is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>m</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>;</mo><mi>m</mi><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>9</mn><mfenced close="]" open="["><mrow><mo>&#8757;</mo><mi>f</mi><mfenced><mn>6</mn></mfenced><mo>=</mo><mn>18</mn></mrow></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>n</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mtext>in&#160;equation</mtext><mo>&#160;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>=</mo><mn>3</mn><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>6</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>&#183;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mo>(</mo><mn>6</mn><mo>)</mo><mo>(</mo><mn>9</mn><mo>)</mo><mo>=</mo><mn>54</mn></math></p>

</details>

---

### Q29. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>,</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>.</mo></math> Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfrac><mn>1</mn><mrow><mi>sin</mi><mfenced><mi>k</mi></mfenced><mi>sin</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mi>f</mi><mfenced><mi>k</mi></mfenced></mrow></mfenced></mrow></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>cosec</mo><mn>2</mn></msup><mfenced><mn>21</mn></mfenced><mi>cos</mi><mfenced><mn>20</mn></mfenced><mi>cos</mi><mfenced><mn>2</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mn>2</mn></msup><mfenced><mn>1</mn></mfenced><mi>sec</mi><mfenced><mn>21</mn></mfenced><mi>cos</mi><mfenced><mn>20</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>cosec</mo><mn>2</mn></msup><mfenced><mn>1</mn></mfenced><mo>cosec</mo><mfenced><mn>21</mn></mfenced><mi>sin</mi><mfenced><mn>20</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mn>2</mn></msup><mfenced><mn>21</mn></mfenced><mi>sin</mi><mfenced><mn>20</mn></mfenced><mi>sin</mi><mfenced><mn>2</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>cosec</mo><mn>2</mn></msup><mfenced><mn>1</mn></mfenced><mo>cosec</mo><mfenced><mn>21</mn></mfenced><mi>sin</mi><mfenced><mn>20</mn></mfenced></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mi>&#955;</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>=</mo><mi>cos</mi><mfrac><mi>&#955;</mi><mn>2</mn></mfrac><mo>&#8658;</mo><mfrac><mi>&#955;</mi><mn>2</mn></mfrac><mo>=</mo><mi mathvariant="normal">&#960;</mi></math></p><p>Thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mn>2</mn><mi>&#960;</mi><mi>x</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is a natural number</p><p>Thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>k</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfrac><mn>1</mn><mrow><mi>sin</mi><mfenced><mi>k</mi></mfenced><mi>sin</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><mn>1</mn></mrow></mfrac><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced close="]" open="["><mfrac><mrow><mi>sin</mi><mfenced><mrow><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>k</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mi>k</mi><mo>&#183;</mo><mi>sin</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>sin</mi><mn>1</mn></mrow></mfrac><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced close="]" open="["><mfrac><mrow><mi>sin</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mi>k</mi><mo>-</mo><mi>sin</mi><mi>k</mi><mi>cos</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>sin</mi><mi>k</mi><mo>&#183;</mo><mi>sin</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><mn>1</mn></mrow></mfrac><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><mi>cot</mi><mi>k</mi><mo>-</mo><mi>cot</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>cot</mi><mn>1</mn><mo>-</mo><mi>cot</mi><mn>21</mn></mrow><mrow><mi>sin</mi><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mrow><mi>cos</mi><mn>1</mn></mrow><mrow><mi>sin</mi><mn>1</mn></mrow></mfrac></mstyle><mo>-</mo><mstyle displaystyle="true"><mfrac><mrow><mi>cos</mi><mn>21</mn></mrow><mrow><mi>sin</mi><mn>21</mn></mrow></mfrac></mstyle></mrow><mrow><mi>sin</mi><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>sin</mi><mn>21</mn><mi>cos</mi><mn>1</mn><mo>-</mo><mi>sin</mi><mn>1</mn><mi>cos</mi><mn>21</mn></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mn>1</mn><mi>sin</mi><mn>21</mn></mrow></mfrac><mo>=</mo><mi>sin</mi><mfenced><mrow><mn>21</mn><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>cosec</mi><mn>2</mn></msup><mn>1</mn><mi>cosec</mi><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mo>cosec</mo><mn>2</mn></msup><mfenced><mn>1</mn></mfenced><mo>cosec</mo><mfenced><mn>21</mn></mfenced><mi>sin</mi><mfenced><mn>20</mn></mfenced></math></p>

</details>

---

### Q30. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>A function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mn>5</mn><mi>x</mi></msup><mrow><msup><mn>5</mn><mi>x</mi></msup><mo>+</mo><mn>5</mn></mrow></mfrac></math>, then the sum of the series</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>20</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2</mn><mn>20</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>3</mn><mn>20</mn></mfrac></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>39</mn><mn>20</mn></mfrac></mfenced></math></p><p>is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>49</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>39</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>29</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>39</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mn>5</mn><mi>x</mi></msup><mrow><msup><mn>5</mn><mi>x</mi></msup><mo>+</mo><mn>5</mn></mrow></mfrac><mo>&#160;&#160;</mo><mi>and</mi><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mrow><msup><mn>5</mn><mi>x</mi></msup><mo>+</mo><mn>5</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>20</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>2</mn><mn>20</mn></mfrac></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>39</mn><mn>20</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>20</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>39</mn><mn>20</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mi>f</mi><mfenced><mfrac><mn>19</mn><mn>20</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>21</mn><mn>20</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>20</mn><mn>20</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>19</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>39</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q31. JEE Main 2021 (24 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>b</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>&#945;</mi><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>b</mi><mi>x</mi><mo>+</mo><mfrac><mi>&#946;</mi><mi>x</mi></mfrac><mo>,</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> then the value of the expression <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfrac></math> is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>&#945;</mi><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>b</mi><mi>x</mi><mo>+</mo><mfrac><mi>&#946;</mi><mi>x</mi></mfrac><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>&#945;</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>b</mi><mi>x</mi></mfrac><mo>+</mo><mi>&#946;</mi><mi>x</mi><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>+</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>x</mi><mfenced><mrow><mi>b</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>b</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></mrow><mrow><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>b</mi><mo>+</mo><mi>&#946;</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>1</mn></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q32. JEE Main 2020 (06 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

Suppose that a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>:</mo><mi mathvariant="bold">R</mi><mo mathvariant="bold">&#8594;</mo><mi mathvariant="bold">R</mi></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>&#160;</mo><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">y</mi></mfenced></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">y</mi><mo>&#160;</mo><mi mathvariant="normal">&#949;</mi><mo>&#160;</mo><mi mathvariant="normal">R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mi mathvariant="normal">n</mi></munderover><mi mathvariant="normal">f</mi><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>=</mo><mn>363</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi></math> is equal to ..... .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>a</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>a</mi><mo>=</mo><mn>3</mn></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mn>3</mn><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>f</mi><mfenced><mi>i</mi></mfenced><mo>=</mo><mn>363</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>3</mn><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mn>3</mn><mi>n</mi></msup><mo>=</mo><mn>363</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mfenced><mrow><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>=</mo><mn>363</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mi>n</mi></msup><mo>=</mo><mn>243</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q33. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo largeop="true">&#931;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#8712;</mo><mi>N</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> is the set of all natural numbers, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo></mrow><mrow><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow></mfrac></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>a</mi><mi>x</mi></msup></math> satisfies the functional relation, so
<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo largeop="true">&#931;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>3</mn></msup><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8734;</mo><mo>&#160;</mo><mtext>terms</mtext><mo>&#160;</mo><mo>=</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mrow><mn>1</mn><mo>-</mo><mi>a</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mi>x</mi></msup></math>
Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo></mrow><mrow><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>4</mn></msup><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q34. JEE Main 2020 (04 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

Suppose a differentiable function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> satisfies the identity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>+</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>,</mo></math> for all real <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>3</mn></mfenced></math> is equal to :

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><mi>x</mi></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>f</mi><mo>&#39;</mo><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>+</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi></math></p><p>Differentiate w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> keeping <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> constant</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>0</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi></math></p><p>put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>=</mo><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>&#8722;</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>10</mn></math>.</p>

</details>

---

### Q35. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function which satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>y</mi></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math> . If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></munderover><mi>f</mi><mfenced><mi>k</mi></mfenced><mo>,</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>, for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mn>20</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>y</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>k</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>f</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#183;</mo><mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></mfrac><mi>n</mi><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">n</mi><mo>-</mo><mn>20</mn><mo>=</mo><mn>0</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">n</mi><mo>=</mo><mn>5</mn></math>.</p>

</details>

---

### Q36. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>f</mi><mo>:</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0,1</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi><mi>&#160;</mi></math> be such that <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>.</mo><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced><mo>,</mo></math> for all <math><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0,1</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi></math> and <math><mi>&#160;</mi><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>&#8800;</mo><mn>0</mn><mo>.</mo></math> If <math><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> satisfies the differential equation, <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> with <math><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math> then <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mn>5</mn></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mn>3</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>3</mn></math>**

**Detailed Solution:**

<p>Given relation is <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>.</mo><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>&#8712;</mo><mi>R</mi><mi>&#160;</mi></math> .....(i)

On putting <math><mi>x</mi><mo>=</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> we get <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><msup><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></math> but</p><p><math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>&#8800;</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math>

Now if we put <math><mi>y</mi><mo>=</mo><mn>0</mn></math> in (i), we get

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>

Hence <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></math>

<math><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></math> <math><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">e</mi><mi>&#160;</mi><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mo>+</mo><mi>y</mi><mfenced separators="|"><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mo>.</mo></math></p>

</details>

---

### Q37. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> . If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math> is such that <math><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>3</mn></math> and <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mi>y</mi></mrow></mfenced><mo>+</mo><mi>x</mi><mi>y</mi><mo>,</mo><mi>&#160;</mi><mo>&#8704;</mo><mi>&#160;</mi><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math> , then <math> <mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>n</mi><mo>=</mo><mn>1</mn> </mrow> <mrow> <mn>10</mn> </mrow> </munderover> <mrow> <mi>f</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo> </mrow> </mstyle> </mrow> </math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>330</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>165</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>190</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>255</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>330</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mi>y</mi></mfenced><mo>+</mo><mi>x</mi><mi>y</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8704;</mo><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>&#8712;</mo><mi>R</mi></math>

Put <math><mi>y</mi><mo>=</mo><mn>1</mn></math>, we get

<math><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>+</mo><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mo>+</mo><mi>x</mi></math></p><p>On taking Sigma on both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfenced><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mfenced><mrow><mn>3</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>f</mi><mfenced separators="|"><mn>4</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>f</mi><mfenced separators="|"><mn>5</mn></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mn>4</mn></mfenced></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mi>f</mi><mfenced separators="|"><mi>n</mi></mfenced><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>-</mo><mn>3</mn><mo>=</mo><mn>3</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfrac><msup><mi>n</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mi>n</mi></mrow><mn>2</mn></mfrac></math></p><p>Again taking Sigma on both the sides </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mfrac><msup><mi>n</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mi>n</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo><mfrac><mrow><mn>10</mn><mo>.</mo><mn>11</mn><mo>.</mo><mn>21</mn></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>.</mo><mfrac><mrow><mn>10</mn><mo>.</mo><mn>11</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mn>330</mn></math>.</p>

</details>

---

### Q38. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

For <math><mi>x</mi><mi>&#160;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8800;</mo><mn>1</mn><mo>,</mo></math> let <math><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math> and <math><msub><mrow><mi>f</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>f</mi></mrow><mrow><mi>n</mi></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mi>n</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></math> Then the value of <math><msub><mrow><mi>f</mi></mrow><mrow><mn>100</mn></mrow></msub><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>+</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn><mo>+</mo><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></math>

<math><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfrac><mo>=</mo><mi>x</mi></math>

<math><msub><mrow><mi>f</mi></mrow><mrow><mn>3</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math>

<math><msub><mrow><mi>f</mi></mrow><mrow><mn>4</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>3</mn><mo>+</mo><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>f</mi></mrow><mrow><mn>3</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></math>

<math><mo>&#8756;</mo></math> <math><msub><mrow><mi>f</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>6</mn></mrow></msub><mo>=</mo><mo>&#8230;</mo><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math>

<math><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>=</mo><mo>&#8230;</mo><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></math>

<math><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>8</mn></mrow></msub><mo>=</mo><mo>&#8230;</mo><mo>=</mo><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>100</mn></msub><mfenced separators="|"><mn>3</mn></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#160;,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>1</mn></msub><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>-</mo><mn>1</mn></mrow><mfrac><mn>2</mn><mn>3</mn></mfrac></mfrac><mo>=</mo><mi>&#160;</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<math><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>&#8756;</mo></math> <math><msub><mrow><mi>f</mi></mrow><mrow><mn>100</mn></mrow></msub><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced><mo>+</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math></p>

</details>

---

### Q39. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>

**Options:**

- **(A)** Contains exactly two elements
- **(B)** Contains more than two elements
- **(C)** Is an empty set
- **(D)** Contains exactly one element

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Contains exactly two elements**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><mn>2</mn><mo>.</mo><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math>

Replace <math><mi>x</mi></math> by <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></math>, we get

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mi>x</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math>

From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>

<math><mn>3</mn><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mn>3</mn><mi>x</mi></math>

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi>x</mi></math>

<math><mo>&#8757;</mo></math> <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></math>

Therefore <math><mfrac><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi>x</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>+</mo><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mn>4</mn><mi>x</mi></mfrac><mo>=</mo><mn>2</mn><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mi>&#160;</mi><mo>&#177;</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt></math>

Contains exactly two elements

</details>

---

### Q40. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

A real valued function $f(x)$ satisfies the functional equation $f(x-y)=f(x) f(y)-f(a-x)$ $f(a+y)$ where $a$ is a given constant and $f(0)=1, f(2 a-x)$ is equal to

**Options:**

- **(A)** $-f(x)$
- **(B)** $f(x)$
- **(C)** $f(a)+f(a-x)$
- **(D)** $f(-x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-f(x)$**

**Detailed Solution:**

$f(a-(x-a))=f(a) f(x-a)-f(0) f(x)$
$=-f(x)\left[\because x=0, y=0, f(0)=f^2(0)-f^2(a) \Rightarrow f^2(a)=0 \Rightarrow f(a)=0\right]$.

</details>

---

### Q41. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $f: R \rightarrow R$ satisfies $f(x+y)=f(x)+f(y)$, for all $x, y \in R$ and $f(1)=7$, then $\sum_{r=1}^n f(r)$ is

**Options:**

- **(A)** $\frac{7 n(n+1)}{2}$
- **(B)** $\frac{7 \mathrm{n}}{2}$
- **(C)** $\frac{7(\mathrm{n}+1)}{2}$
- **(D)** $7 n+(n+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{7 n(n+1)}{2}$**

**Detailed Solution:**

$\mathrm{f}(\mathrm{x}+\mathrm{y})=\mathrm{f}(\mathrm{x})+\mathrm{f}(\mathrm{y}) . \quad$ Let $\mathrm{f}(\alpha)=\mathrm{m} \alpha$
$\mathrm{f}(1)=7 ; \quad \therefore \mathrm{m}=7, \mathrm{f}(\mathrm{x})=7 \mathrm{x}$
$\sum_{\mathrm{r}=1}^{\mathrm{n}} \mathrm{f}(\mathrm{r})=7 \sum_1^{\mathrm{n}} \mathrm{r}=\frac{7 \mathrm{n}(\mathrm{n}+1)}{2}$

</details>

---

### Q42. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $f(x+y)=f(x) \cdot f(y) \forall x \cdot y$ and $f(5)=2, f^{\prime}(0)=3$ then $f^{\prime}(5)$ is

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 6
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 6**

**Detailed Solution:**

$$
f(x+y)=f(x) \times f(y)
$$
Differentiate with respect to $x$, treating $y$ as constant
$$
f^{\prime}(x+y)=f(x) f(y)
$$
Putting $x=0$ and $y=x$, we get $f^{\prime}(x)=f^{\prime}(0) f(x) ; \Rightarrow f^{\prime}(5)=3 f(5)=3 \times 2=6$

</details>

---

