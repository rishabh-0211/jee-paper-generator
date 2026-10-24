# BITSAT Mathematics - Differential Equations

## Topic 5: Linear Differential Equation

**Total Questions:** 13

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $(x+1) \frac{d y}{d x}-y=e^{3 x}(x+1)^2$ is

**Options:**

- **(A)** $y=(x+1) e^{3 x}+C$
- **(B)** $3 y=(x+1)+e^{3 x}+C$
- **(C)** $\frac{3 y}{x+1}=e^{3 x}+C$
- **(D)** $y e^{-3 x}=3(x+1)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3 y}{x+1}=e^{3 x}+C$**

**Detailed Solution:**

Given, $\frac{d y}{d x}-\frac{y}{x+1}=e^{3 x}(x+1)$
Above is linear differential equation of form
$\begin{aligned}
& \frac{d y}{d x}+P x=Q \\
& \therefore \quad \mathrm{IF}=e^{\int P d x}=e^{\int-\frac{1}{x+1} d x}=e^{-\ln (1+x)}=\frac{1}{1+x}
\end{aligned}$
$\Rightarrow$ Solution will be
$\begin{aligned}
y \cdot \mathrm{IF} & =\int Q \cdot \mathrm{IF} d x \\
y \cdot \frac{1}{1+x} & =\int e^{3 x}(x+1) \times \frac{1}{(1+x)} d x \\
\frac{y}{1+x} & =\frac{e^{3 x}}{3}+C^{\prime} \\
\frac{3 y}{1+x} & =e^{3 x}+C^{\prime} \quad \quad\left[\because C=3 C^{\prime}\right]
\end{aligned}$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\frac{d y}{d x}-y \log _e 2=2^{\sin x}(\cos x-1) \log _e 2$, then $y$

**Options:**

- **(A)** $2^{\sin x}+c 2^x$
- **(B)** $2^{\cos x}+c 2^x$
- **(C)** $2^{\sin x}+c 2^{-x}$
- **(D)** $2^{\cos x}+c 2^{-x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2^{\sin x}+c 2^x$**

**Detailed Solution:**

$\frac{d y}{d x}-y \log _e 2=2^{\sin x}(\cos x-1) \log _e 2$
This is linear differential equation
$\text { I.F. }=e^{-\log _e 2 \int d x}=e^{-x \log _e 2}=2^{-x}$
then general Solution is
$y 2^{-x}=\int 2^{-x} 2^{\sin x}(\cos x-1) \log _e 2 d x+c$
Now let $\sin x-x=t \Rightarrow(\cos x-1) d x=d t$
$\begin{aligned}
& \therefore y 2^{-x}=\log _e 2 \int 2^t d t+c \\
& \therefore y 2^{-x}=2^t+c \\
& \therefore y=2^{x+t}+c 2^x \\
& \therefore y=2^{\sin x}+c 2^x
\end{aligned}$

</details>

---

### Q3. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

The integrating factor of $\frac{x d y}{d x}-y=x^4-3 x$ is

**Options:**

- **(A)** x
- **(B)** $\log x$
- **(C)** $\frac{1}{x}$
- **(D)** $-\mathbf{X}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{x}$**

**Detailed Solution:**

$\begin{aligned}
& \text { (c) Since } x \frac{d y}{d x}-y=x^4-3 x \\
& \therefore \frac{d y}{d x}-\frac{y}{x}=x^3-3
\end{aligned}$
Hence $I F=e^{\int P d x}=e^{-\int \frac{1}{x} d x}=e^{-\log x}=\frac{1}{x}$

</details>

---

### Q4. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

$\left(\frac{d y}{d x}\right) \tan x=y \sec ^2 x+\sin x$, find general solution

**Options:**

- **(A)** $y=\tan x(\log |\operatorname{cosec} x-\cot x|+\cos x+c)$
- **(B)** $y=\sec ^2 x+\tan x+c$
- **(C)** $y=\log |\sec x+\tan x|+\operatorname{cosec} x+c$
- **(D)** $y=\tan ^2 x+\sin x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y=\tan x(\log |\operatorname{cosec} x-\cot x|+\cos x+c)$**

**Detailed Solution:**

Given that
$$
\begin{aligned}
& \left(\frac{d y}{d x}\right) \tan x=y \sec ^2 x+\sin x \\
& \tan x\left(\frac{d y}{d x}\right)-y \sec ^2 x=\sin x \\
& \frac{d y}{d x}+\left(\frac{-\sec ^2 x}{\tan x}\right) y=\frac{\sin x}{\tan x} \\
& \text { Here, } P=-\frac{\sec ^2 x}{\tan x} \text { and } Q=\cos x \\
& \text { IF }=e^{\int P d x}=e^{\int \frac{-\sec ^ 2 x}{\tan x} d x} \\
& \text { IF }=e^{-\log (\tan x)}=e^{\log \cot x}=\cot x \\
& \text { Now, } y \times \mathrm{IF}=\int(Q \times \mathrm{IF}) d x+C \\
& y \cdot \cot x=\int \cos x \cdot \cot x+C \\
& y \cdot \cot x=\int \frac{1-\sin ^2 x}{\sin x}+C \\
& y \cdot \cot x=\log |\operatorname{cosec} x-\cot x|+\cos x+C
\end{aligned}
$$

</details>

---

### Q5. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\left(\tan ^{-1} y-x\right) d y=\left(1+y^{2}\right) d x$ is

**Options:**

- **(A)** $x=\left(\tan ^{-1} y+1\right)+\mathrm{C} e^{-\tan ^{-1} y}$
- **(B)** $x=\left(\tan ^{-1} y-1\right)+\mathrm{C} e^{-\tan ^{-1} y}$
- **(C)** $x=\left(\tan ^{-1} x-1\right)+\mathrm{C} e^{-\tan ^{-1} x}$
- **(D)** $x=\left(\tan ^{-1} x+1\right)+\mathrm{Ce}^{-\tan ^{-1} x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x=\left(\tan ^{-1} y-1\right)+\mathrm{C} e^{-\tan ^{-1} y}$**

**Detailed Solution:**

The given differential equation can be written as $\frac{d x}{d y}+\frac{x}{1+y^{2}}=\frac{\tan ^{-1} y}{1+y^{2}} \ldots$ (i)

Now, eq. (i) is a linear differential equation of the form $\frac{d x}{d y}+\mathrm{P}_{1} x=\mathrm{Q}_{1}$

where $\mathrm{P}_{1}=\frac{1}{1+y^{2}}$ and $\mathrm{Q}_{1}=\frac{\tan ^{-1} y}{1+y^{2}}$

Therefore, I.F $=e^{\int \frac{1}{1+y^{2}} d y}=e^{\tan ^{-1} y}$

Thus, the solution of the given differential equation is given by $x e^{\tan ^{-1} y}=\int\left(\frac{\tan ^{-1} y}{1+y^{2}}\right) e^{\tan ^{-1} y} \mathrm{dy}+\mathrm{C} \ldots$ (ii)

Let $\mathrm{I}=\int\left(\frac{\tan ^{-1} y}{1+y^{2}}\right) e^{\tan ^{-1} y} \mathrm{dy}$

On substituting $\tan ^{-1} y=t$, so that

$\left(\frac{1}{1+y^{2}}\right) \mathrm{dy}=\mathrm{dt}$, we get

$I=\int t e^{t} d t=t e^{t}-\int 1 \cdot e^{t} d t=t e^{t}-e^{t}=e^{t}(t-1)$

or $\mathrm{I}=e^{\tan ^{-1} y}\left(\tan ^{-1} y-1\right)$

On substituting the value of 1 in equation (i1), we get

$x \cdot e^{\tan ^{-1} y}=\cdot e^{\tan ^{-1} y}\left(\tan ^{-1} y-1\right)+\mathrm{C}$

or $x=\left(\tan ^{-1} y-1\right)+\mathrm{C} e^{\tan ^{-1} y}$

which is the general solution of the given differntial equation.

</details>

---

### Q6. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation

$(x+1) \frac{d y}{d x}-y=e^{3 x}(x+1)^{2}$ is

**Options:**

- **(A)** $y=(x+1) e^{3 x}+c$
- **(B)** $3 y=(x+1)+e^{3 x}+c$
- **(C)** $\frac{3 y}{x+1}=e^{3 x}+c$
- **(D)** $y e^{-3 x}=3(x+1)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3 y}{x+1}=e^{3 x}+c$**

**Detailed Solution:**

The given equation is $\frac{d y}{d x}-\frac{y}{x+1}=e^{3 x}(x+1)$

I.F. $=e^{\int-\frac{1}{x+1} d x}=e^{-\log (x+1)}=\frac{1}{x+1}$

The solution is

$y\left(\frac{1}{x+1}\right)=\int e^{3 x}(x+1) \cdot \frac{1}{x+1} d x+a$

$\Rightarrow \frac{y}{x+1}=\int e^{3 x} d x+a=\frac{e^{3 x}}{3}+a$

$\Rightarrow \frac{3 y}{x+1}=e^{3 x}+c, c=3 a$

</details>

---

### Q7. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>e</mi><mi>x</mi></msup><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>2</mn><mo>-</mo><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>e</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>2</mn><mo>-</mo><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow><mrow><mn>3</mn><mo>+</mo><mi>e</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced></mrow><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced></mrow><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>log</mi><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>A</mi><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>A</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>K</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi>A</mi><mo>+</mo><mi>K</mi><mo>=</mo><mn>1</mn></math>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>A</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>A</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>K</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><mi>A</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>k</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>+</mo><msubsup><mfenced open="[" close="]"><mrow><mi>A</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>K</mi><mi>x</mi></mrow></mfenced><mn>0</mn><mn>1</mn></msubsup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>k</mi><mo>+</mo><mi>A</mi><mi>e</mi><mo>-</mo><mi>A</mi><mo>+</mo><mi>K</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>A</mi><mo>(</mo><mi>e</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>2</mn><mi>k</mi><mo>=</mo><mn>0</mn></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>iii</mi><mo>)</mo></math></p><p>From Eqs. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>ii</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>iii</mi><mo>)</mo></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac><mo>,</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>e</mi></mrow><mrow><mn>3</mn><mo>-</mo><mi>e</mi></mrow></mfrac></math></p>

</details>

---

### Q8. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `2`

Solution of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mi>y</mi></msup></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>y</mi></msup><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>y</mi><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><msup><mi>e</mi><mi>y</mi></msup><mo>=</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></msup></math>
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>y</mi></msup><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></msup></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mi>y</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>e</mi><mi>y</mi></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><msup><mi>e</mi><mi>y</mi></msup><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>y</mi></msup><mo>=</mo><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>e</mi><mi>y</mi></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>v</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math></p><p>This is linear equation </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>=</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Required solution is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>&#183;</mo><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>&#183;</mo><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup><mo>=</mo><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>e</mi><mi>y</mi></msup><mo>&#183;</mo><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup><mo>=</mo><msup><mi>e</mi><msup><mi>e</mi><mi>x</mi></msup></msup><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>e</mi><mi>y</mi></msup><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></msup></math></p>

</details>

---

### Q9. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `2`

Solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><mn>2</mn><mo>+</mo><mi>sec</mi><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mi>y</mi><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mi>v</mi><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mi>sin</mi><mi>v</mi><mo>+</mo><mi>cos</mi><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>sin</mi><mi>v</mi><mo>+</mo><mi>cos</mi><mi>v</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>sin</mi><mi>v</mi><mo>+</mo><mi>cos</mi><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfenced><mfrac><mn>1</mn><mrow><mi>sin</mi><mi>v</mi><mo>+</mo><mi>cos</mi><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mi>d</mi><mi>v</mi><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mfenced close="}" open="{"><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>tan</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>v</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>v</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow></mfrac></mstyle></mfenced><mo>+</mo><mfenced close="}" open="{"><mstyle displaystyle="true"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>v</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>v</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow></mfrac></mstyle></mfenced><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>v</mi><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfenced close="]" open="["><mfrac><mfenced close="}" open="{"><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>v</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow></mfenced><mrow><mstyle displaystyle="true"><mn>2</mn></mstyle><mstyle displaystyle="true"><mi>tan</mi></mstyle><mstyle displaystyle="true"><mfenced><mfrac><mstyle displaystyle="true"><mi>v</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mfenced></mstyle><mo>+</mo><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mo>-</mo></mstyle><mstyle displaystyle="true"><msup><mstyle displaystyle="true"><mi>tan</mi></mstyle><mn>2</mn></msup></mstyle><mstyle displaystyle="true"><mfenced><mfrac><mstyle displaystyle="true"><mi>v</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mfenced></mstyle><mo>+</mo><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>v</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow></mfrac></mfenced><mi>d</mi><mi>v</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfenced close="]" open="["><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mi>v</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mstyle displaystyle="true"><mi>tan</mi><mfenced><mfrac><mstyle displaystyle="true"><mi>v</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mfenced><mo>+</mo><mn>1</mn></mstyle></mfrac></mfenced><mi>d</mi><mi>v</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><mfenced><mrow><mi>tan</mi><mfenced><mfrac><mstyle displaystyle="true"><mi>v</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><mfenced><mrow><mi>tan</mi><mfenced><mfrac><mstyle displaystyle="true"><mi>x</mi><mo>+</mo><mi>y</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math></p>

</details>

---

### Q10. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `2`

The solution of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced open="[" close="]"><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math>
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mi>v</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p>Therefore, the differential equation reduces to</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>cos</mi><mi>v</mi></mrow></mfenced><mo>+</mo><mi>sin</mi><mi>v</mi><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>v</mi><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>sin</mi><mfrac><mi>v</mi><mn>2</mn></mfrac><mi>cos</mi><mfrac><mi>v</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>v</mi><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>tan</mi><mi>v</mi></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>V</mi><mn>2</mn></mfrac></mrow><mrow><mn>2</mn><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mi>v</mi><mn>2</mn></mfrac></mfenced></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>v</mi><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>log</mi><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi></math></p>

</details>

---

### Q11. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `3`

The solution to the differential equation $\frac{d y}{d x}=\frac{y f^{\prime}(x)-y^{2}}{f(x)}$ where $f(x)$ is a given function is

**Options:**

- **(A)** $f(x)=y(x+c)$
- **(B)** $f(x)=c x y$
- **(C)** $f(x)=c(x+y)$
- **(D)** $\mathrm{yf}(\mathrm{x})=\mathrm{cx}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $f(x)=y(x+c)$**

**Detailed Solution:**

We have $\frac{d y}{d x}=\frac{f^{\prime}(x)}{f(x)} y-\frac{y^{2}}{f(x)}$

$\Rightarrow \frac{d y}{d x}-\frac{f^{\prime}(x)}{f(x)} y=-\frac{y^{2}}{f(x)}$

Divide by $y^{2}: y^{-2} \frac{d y}{d x}-y^{-1} \frac{f^{\prime}(x)}{f(x)}=-\frac{1}{f(x)}$

Put $y^{-1}=z \Rightarrow-y^{-2} \frac{d y}{d x}=\frac{d z}{d x}$

$-\frac{d z}{d x}-\frac{f^{\prime}(x)}{f(x)}(z)=-\frac{1}{f(x)}$

$\Rightarrow \frac{d z}{d x}+\frac{f^{\prime}(x)}{f(x)} z=\frac{1}{f(x)}$

$I F=e^{\int \frac{f^{\prime}(x)}{f(x)} d x}=e^{\log f(x)}=f(x)$

$\therefore$ The solution is $z(f(x))=\int \frac{1}{f(x)}(f(x)) d x+c$

$\Rightarrow y^{-1}(f(x))=x+c \Rightarrow f(x)=y(x+c)$

</details>

---

### Q12. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `1`

The area of the region bounded by the curve \(y=x|x|, x\)-axis and the ordinates \(x=1, x=-1\) is given by :

**Options:**

- **(A)** zero
- **(B)** \(\frac{1}{3}\)
- **(C)** \(\frac{2}{3}\)
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \(\frac{2}{3}\)**

**Detailed Solution:**

The area of the region bounded by the curve \(y=f(x)\) and the ordinates \(x=a, x=b\) is given by
\(\text {Area }=\left|\int_a^b y d x\right|\)
According to the question,
\(y=x|x|= \begin{cases}x^2, & x \geq 0 \\ -x^2, & x  < 0\end{cases}\)<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/FZCw9yBYXriAVn3LRBhGUGiFnLoUl_9mYiLSqNxNlqc.original.fullsize.png">

Required area
\(=\) area of region \(\mathrm{OAB}+\) area of region \(\mathrm{OCD}\)
\(=2 \times\) Area of region \(\mathrm{OAB}\)
\(=2 \int_0^1 x^2 d x=\frac{2}{3} s q\). units

</details>

---

### Q13. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `2`

Area of the triangle formed by the line \(x+y=3\) and angle bisectors of the pair of straight lines \(x^2-y^2+2 y=1\) is

**Options:**

- **(A)** 2 sq. units
- **(B)** 4 sq. units
- **(C)** 6 sq. units
- **(D)** 8 sq. units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2 sq. units**

**Detailed Solution:**

\(\mathrm{x}^2-\mathrm{y}^2+2 \mathrm{y}=1 \Rightarrow \mathrm{x}= \pm(\mathrm{y}-1)\)
Bisectors of above line are \(x=0 ~\&~ y=1\)
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/q9-e-nY41f9GD5ETl-tSN4Ed4dRtdgHVdnw95PKOA4k.original.fullsize.png">

So area between \(x=0, y=1 ~\&~ x+y=3\) is shaded Region shown in figure.<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/HlzbRdJnBytZmsPrh3LCzmrLogiaYjEvOdpefLciUfA.original.fullsize.png">

Area \(=1 / 2 \times 2 \times 2=2\) sq. units

</details>

---

