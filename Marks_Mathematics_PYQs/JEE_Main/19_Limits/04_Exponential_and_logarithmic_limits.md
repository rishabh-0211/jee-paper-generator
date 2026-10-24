# JEE Main Mathematics - Limits

## Topic 4: Exponential and logarithmic limits

**Total Questions:** 13

---

### Q1. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\lim _{x \rightarrow 0} \frac{\log _{e}\left(\sec (e x) \cdot \sec \left(e^{2} x\right) \cdot \ldots \cdot \sec \left(e^{10} x\right)\right)}{e^{2}-e^{2 \cos x}}$ is equal to

**Options:**

- **(A)** $\frac{\left(e^{20}-1\right)}{2\left(e^{2}-1\right)}$
- **(B)** $\frac{\left(e^{10}-1\right)}{2\left(e^{2}-1\right)}$
- **(C)** $\frac{\left(e^{10}-1\right)}{2 e^{2}\left(e^{2}-1\right)}$
- **(D)** $\frac{\left(e^{20}-1\right)}{2 e^{2}\left(e^{2}-1\right)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\left(e^{20}-1\right)}{2\left(e^{2}-1\right)}$**

**Detailed Solution:**

Numerator: $\log_e(\sec(ex)\sec(e^2x)\cdots\sec(e^{10}x)) = \sum_{k=1}^{10} \log_e(\sec(e^kx))$.
Using $\sec(u) \approx 1 + \frac{u^2}{2}$ for small $u$, we get $\log_e(\sec(e^kx)) \approx \frac{e^{2k}x^2}{2}$.
Thus the numerator is $\approx \frac{x^2}{2}\sum_{k=1}^{10} e^{2k} = \frac{x^2 e^2(e^{20}-1)}{2(e^2-1)}$. 
Denominator: Using $\cos x \approx 1 - \frac{x^2}{2}$, we have $e^{2\cos x} \approx e^2(1-x^2)$, so $e^2 - e^{2\cos x} \approx e^2 x^2$. 
Therefore: $\lim_{x \to 0} = \frac{\frac{x^2 e^2(e^{20}-1)}{2(e^2-1)}}{e^2 x^2} = \frac{e^{20}-1}{2(e^2-1)}$.

</details>

---

### Q2. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f: \mathbf{R} \rightarrow(0, \infty)$ be a twice differentiable function such that $f(3)=18, f^{\prime}(3)=0$ and $f^{\prime \prime}(3)=4$. Then $\lim _{x \rightarrow 1}\left(\log _{\mathrm{e}}\left(\frac{f(2+x)}{f(3)}\right)^{\frac{18}{(x-1)^{2}}}\right)$ is equal to :

**Options:**

- **(A)** 1
- **(B)** 18
- **(C)** 2
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

Let $T = \lim_{x \to 1} \left( \dfrac{f(x+2)}{f(3)} \right)^{\dfrac{18}{(x-1)^2}}$ ; $1^{\infty}$ form
$\Rightarrow T = e^{\lim_{x \to 1} \dfrac{18}{(x-1)^2} \left( \dfrac{f(x+2) - f(3)}{f(3)} \right)}$
$\Rightarrow T = e^{\lim_{x \to 1} \dfrac{18}{(x-1)^2} \left( \dfrac{f(x+2) - f(3)}{18} \right)}$
$\Rightarrow T = e^{\lim_{x \to 1} \left( \dfrac{f(x+2) - f(3)}{(x-1)^2} \right)}$ $\dfrac{0}{0}$ form, apply L'pital
$\Rightarrow T = e^{\lim_{x \to 1} \dfrac{f'(x+2)}{2(x-1)}}$ ; $\dfrac{0}{0}$ form, apply L'pital
$\Rightarrow T = e^{\lim_{x \to 1} \dfrac{f''(x+2)}{2}}$ $= e^{\dfrac{4}{2}} = e^2$
$\Rightarrow \log_e(T) = 2$

</details>

---

### Q3. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given below are two statements :
Statement I : $\lim _{x \rightarrow 0}\left(\frac{\tan ^{-1} x+\log _e \sqrt{\frac{1+x}{1-x}}-2 x}{x^5}\right)=\frac{2}{5}$
Statement II : $\lim _{\mathrm{x} \rightarrow 1}\left(\mathrm{x}^{\frac{2}{1-\mathrm{x}}}\right)=\frac{1}{\mathrm{e}^2}$
In the light of the above statements, choose the correct answer from the options given below :

**Options:**

- **(A)** Statement I is false but Statement II is true
- **(B)** Statement I is true but Statement II is false
- **(C)** Both Statement I and Statement II are false
- **(D)** Both Statement I and Statement II are true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Both Statement I and Statement II are true**

**Detailed Solution:**

$\begin{aligned}
& \lim _{x \rightarrow 0} \frac{\tan ^{-1} x+\frac{1}{2}[\ln (1+x)-\ln (1-x)]-2 x}{x^5} \\
& =\lim _{x \rightarrow 0} \frac{\left(x-\frac{x^3}{3}+\frac{x^5}{5} \ldots\right)+\frac{1}{2}\left[x-\frac{x^2}{2}+\frac{x^3}{3} \ldots-\left(-x-\frac{x^2}{2}-\frac{x^3}{3} \ldots\right)\right]-2 x}{x^5} \\
& =\lim _{x \rightarrow 0} \frac{2 x+\frac{2 x^5}{5} \ldots-2 x}{x^5}=\frac{2}{5} \\
& \lim _{x \rightarrow 1} x^{\frac{2}{(1-x)}}=e^{\lim _{x \rightarrow l}\left(\frac{2}{(1-x)}\right)(x-1)}=e^{-2}
\end{aligned}$
$\Rightarrow$ Both statements correct

</details>

---

### Q4. JEE Main 2025 (28 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $f(x)=\lim _{\mathrm{n} \rightarrow \infty} \sum_{\mathrm{r}=0}^{\mathrm{n}}\left(\frac{\tan \left(x / 2^{r+1}\right)+\tan ^3\left(x / 2^{r+1}\right)}{1-\tan ^2\left(x / 2^{r+1}\right)}\right)$. Then $\lim _{x \rightarrow 0} \frac{\mathrm{e}^x-\mathrm{e}^{f(x)}}{(x-f(x))}$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

$\begin{aligned} & f(x)=\lim _{x \rightarrow \infty}\left(\frac{\tan \left(x / 2^{r+1}\right)+\tan ^3\left(x / 2^{r+1}\right)}{1-\tan ^2\left(x / 2^{r+1}\right)}\right) \\ & =\lim _{x \rightarrow \infty} \frac{\tan \left(\frac{x}{2^{r+1}}\right)}{\cos \left(\frac{x}{2^r}\right)} \\ & =\lim _{x \rightarrow \infty} \frac{\sin \left(x / 2^{r+1}\right)}{\cos \left(\frac{x}{2^{r+1}}\right) \cos \left(\frac{x}{2^r}\right)} \\ & =\lim _{x \rightarrow \infty} \frac{\sin \left(\frac{x}{2^r}-\frac{x}{2^{r+1}}\right)}{\cos \left(\frac{x}{2^{r+1}}\right) \cos \left(\frac{x}{2^r}\right)}\end{aligned}$
$=\lim _{x \rightarrow \infty} \tan \left(\frac{x}{2^r}\right)-\tan \left(\frac{x}{2^{r+1}}\right)$
From condition given question
$\begin{aligned}
& \therefore \lim _{n \rightarrow \infty} \sum_{r=0}^n\left[\tan \left(\frac{x}{2^r}\right)-\tan \left(\frac{x}{2^{r+1}}\right)\right]=\tan x \\
& \therefore \lim _{x \rightarrow 0}\left(\frac{e^x-e^{\tan x}}{x-\tan x}\right) \\
& \Rightarrow \lim _{x \rightarrow 0} e^{\tan x}\left(\frac{e^{x-\tan x}-1}{x-\tan x}\right) \\
& \Rightarrow \lim _{x \rightarrow 0} e^{\tan x} \lim _{x \rightarrow 0}\left(\frac{e^{x-\tan x}-1}{x-\tan x}\right) \\
& \Rightarrow 1.1\left(\because \lim _{x \rightarrow 0} \frac{e^{x-1}}{x}=1\right) \\
& \quad=1
\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow \infty} \frac{\left(2 x^2-3 x+5\right)(3 x-1)^{\frac{x}{2}}}{\left(3 x^2+5 x+4\right) \sqrt{(3 x+2)^x}}$ is equal to :

**Options:**

- **(A)** $\frac{2}{\sqrt{3 \mathrm{e}}}$
- **(B)** $\frac{2 \mathrm{e}}{\sqrt{3}}$
- **(C)** $\frac{2}{3 \sqrt{\mathrm{e}}}$
- **(D)** $\frac{2 \mathrm{e}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{3 \sqrt{\mathrm{e}}}$**

**Detailed Solution:**

$\begin{aligned}
& \lim _{x \rightarrow \infty} \frac{\left(2 x^2-3 x+5\right)(3 x-1)^{x / 2}}{\left(3 x^2+5 x+4\right) \sqrt{(3 x+2)^x}} \\
& =\lim _{x \rightarrow \infty} \frac{x^2\left(2-\frac{3}{x}+\frac{5}{x^2}\right)(3 x)^{\frac{x}{2}}}{x^2\left(3+\frac{5}{x}+\frac{4}{x^2}\right)(3 x)^{\frac{x}{2}}} \cdot \frac{\left(1-\frac{1}{3 x}\right)^{\frac{x}{2}}}{\left(1+\frac{2}{3 x}\right)^{\frac{x}{2}}} \\
& \lim _{x \rightarrow \infty}\left(1-\frac{1}{3 x}\right)^{\frac{x}{2}}=e^{\lim _{x \rightarrow \infty}\left(1-\frac{1}{3 x}-1\right) \times \frac{x}{2}}=e^{\frac{-1}{6}} \\
& \lim _{x \rightarrow \infty}\left(1+\frac{2}{3 x}\right)=e^{\lim _{x \rightarrow \infty}\left(1+\frac{2}{3 x}-1\right) \times \frac{x}{2}} \\
& =e^{\frac{1}{3}}
\end{aligned}$
So, $\frac{2}{3} \times \frac{e^{\frac{-1}{6}}}{e^{\frac{1}{3}}}=\frac{2}{3} \times \frac{1}{e^{\frac{1}{3}+\frac{1}{6}}}=\frac{2}{3 \sqrt{e}}$

</details>

---

### Q6. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\lim _{x \rightarrow 0} \frac{e-(1+2 x)^{\frac{1}{2 x}}}{x}$ is equal to

**Options:**

- **(A)** 0
- **(B)** $\frac{-2}{e}$
- **(C)** e
- **(D)** $e-e^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) e**

**Detailed Solution:**

$\begin{aligned} & \operatorname{Lim}_{x \rightarrow 0} \frac{e-e^{\frac{1}{2 x} \ln (1+2 x)}}{x} \\ & =\operatorname{Lim}_{x \rightarrow 0}(-e) \frac{\left(e^{\frac{\ln (1+2 x)}{2 x}-1}-1\right)}{x} \\ & =\operatorname{Lim}_{x \rightarrow 0}(-e) \frac{\ln (1+2 x)-2 x}{2 x^2} \\ & =(-e) \times(-1) \frac{4}{2 \times 2}=e\end{aligned}$

</details>

---

### Q7. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mi>x</mi><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>a</mi><mi>x</mi><mfenced><mrow><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math> exists and is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></math> is ___ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mi>x</mi><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>a</mi><mi>x</mi><mfenced><mrow><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>&#160;&#160;</mo><mfenced><mfrac><mn>0</mn><mn>0</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mi>x</mi><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>a</mi><mi>x</mi><mo>&#183;</mo><mn>4</mn><mi>x</mi></mrow></mfrac></math>    Use <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>4</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p>Apply <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>&#39;Hospital Rule</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>a</mi><mo>-</mo><mn>4</mn><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup></mrow><mrow><mn>8</mn><mi>a</mi><mi>x</mi></mrow></mfrac></math> ( <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>-</mo><mn>4</mn></mrow><mn>0</mn></mfrac></math> form )</p><p>limit exists only when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>4</mn><mo>-</mo><mn>4</mn><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup></mrow><mrow><mn>32</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup></mrow><mrow><mn>8</mn><mi>x</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mfrac><mn>0</mn><mn>0</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mo>-</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><mn>4</mn></mrow><mn>8</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>4</mn><mo>-</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q8. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>x</mi><mfenced><mrow><msup><mi>e</mi><mrow><mfenced><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mo>/</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></math>

**Options:**

- **(A)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>e</mi></msqrt></math>
- **(B)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mfenced><mrow><msup><mi>e</mi><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></msqrt><mo>&#8722;</mo><mn>1</mn></mrow><mi>x</mi></mfrac></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></msqrt><mo>&#8722;</mo><mn>1</mn></mrow><mi>x</mi></mfrac></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mi>u</mi><mi>t</mi><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup></msqrt><mo>&#8722;</mo><mn>1</mn></mrow><mi>x</mi></mfrac><mo>=</mo><mi>t</mi></math></p><p>clearly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mn>0</mn><mo>&#8658;</mo><mi>t</mi><mo>&#8594;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> given limit <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mi>e</mi><mi>t</mi></msup><mo>&#8722;</mo><mn>1</mn></mrow><mi>t</mi></mfrac><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q9. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mrow><mo>(</mo><mn>27</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>-</mo><mn>3</mn></mrow><mrow><mn>9</mn><mo>-</mo><msup><mrow><mo>(</mo><mn>27</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mrow></mfrac></math> equals

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(B)** <math><mi>&#160;</mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(C)** <math><mi>&#160;</mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>**

**Detailed Solution:**

Given limit is <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><msup><mfenced separators="|"><mrow><mn>27</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>-</mo><mn>3</mn><mi>&#160;</mi></mrow><mrow><mn>9</mn><mo>-</mo><msup><mfenced separators="|"><mrow><mn>27</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mn>0</mn><mn>0</mn></mfrac><mi>&#160;</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">m</mi></mrow></mfenced></math>

Applying L&#39;Hospital&#39;s rule,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn><mi>&#160;</mi></mrow></munder><mfrac><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mfenced separators="|"><mrow><mn>27</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></msup><mi>&#160;</mi></mrow><mrow><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mfenced separators="|"><mrow><mn>27</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><msup><mfenced separators="|"><mn>27</mn></mfenced><mrow><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></msup><mrow><mo>-</mo><mn>2</mn><msup><mfenced separators="|"><mn>27</mn></mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></msup></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mfenced separators="|"><mn>27</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mi>&#160;</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math>.

</details>

---

### Q10. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

The function $f:R \sim\{0\} \rightarrow R$ given by
$f(x)=\frac{1}{x}-\frac{2}{e^{2 x}-1}$
can be made continuous at $x=0$ by defining $f(0)$ as

**Options:**

- **(A)** $2$
- **(B)** $-1$
- **(C)** $0$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1$**

**Detailed Solution:**

$\lim _{x \rightarrow 0} \frac{1}{x}-\frac{2}{e^{2 x}-1}$
$\lim _{x \rightarrow 0} \frac{e^{2 x}-1-2 x}{x\left(e^{2 x}-1\right)}$
$\lim _{x \rightarrow 0} \frac{2 e^{2 x}-2}{\left(e^{2 x}-1\right)+2 x e^{2 x}}$
$\lim _{x \rightarrow 0} \frac{4 e^{2 x}}{4 e^{2 x}+4 x e^{2 x}}=1$.

</details>

---

### Q11. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $\lim _{x \rightarrow \infty}\left(1+\frac{a}{x}+\frac{b}{x^2}\right)^{2 x}=e^2$, then the values of $a$ and $b$, are

**Options:**

- **(A)** $a \in \underline{\underline{R}}, \mathrm{~b} \in \underline{\underline{=}}$
- **(B)** $a=1, b \in \underline{R}$
- **(C)** $a \in \underline{\underline{R}}, b=2$
- **(D)** $a=1$ and $b=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a=1, b \in \underline{R}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/kIZy4JzxgjA3tcxUlvMDEILI7oibJfKVGG4Csl98nr8.original.fullsize.png">

</details>

---

### Q12. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

If $\lim _{x \rightarrow 0} \frac{\log (3+x)-\log (3-x)}{x}=k$, the value of $k$ is

**Options:**

- **(A)** $-\frac{2}{3}$
- **(B)** 0
- **(C)** $-\frac{1}{3}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{3}$**

**Detailed Solution:**

$\operatorname{Lim}_{x \rightarrow 0} \frac{\log (3+x)-\log (3-x)}{x}=K$ (by L'Hospital rule)
$\operatorname{Lim}_{x \rightarrow 0} \frac{\frac{1}{3+x}-\frac{-1}{3-x}}{1}=K \quad \therefore \frac{2}{3}=\mathrm{K}$

</details>

---

### Q13. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4zoEd1S-v10xsW1PC6JrIcSsejoe7BFb5kcGSYxuISM.original.fullsize.png">

**Options:**

- **(A)** $e^4$
- **(B)** $e^2$
- **(C)** $e^3$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/OP7CLl6jWOvedDoWt6TJ2JXgOO2EgLqftJRwA7M5icE.original.fullsize.png">

</details>

---

