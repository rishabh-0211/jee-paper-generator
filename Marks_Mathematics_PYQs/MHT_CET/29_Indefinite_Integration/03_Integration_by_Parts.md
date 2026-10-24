# MHT CET Mathematics - Indefinite Integration

## Topic 3: Integration by Parts

**Total Questions:** 53

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int [\sin(\log x) - \cos(\log x)] dx = xf(x) + c$, then the value of $f(x)$ is:

**Options:**

- **(A)** $\sin(\log x)$
- **(B)** $-\cos(\log x)$
- **(C)** $-\sin(\log x)$
- **(D)** $\cos(\log x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\cos(\log x)$**

**Detailed Solution:**

Let $I = \int [\sin(\log x) - \cos(\log x)] dx$

Substitute $\log x = t \Rightarrow x = e^t \Rightarrow dx = e^t dt$

$I = \int e^t (\sin t - \cos t) dt$

Using the standard integral $\int e^t [g(t) + g'(t)] dt = e^t g(t) + c$

Let $g(t) = -\cos t$, then $g'(t) = \sin t$

Therefore, $I = e^t (-\cos t) + c$

Substituting $t = \log x$ and $e^t = x$, we get:

$I = -x \cos(\log x) + c$

Comparing this with $x f(x) + c$, we find $f(x) = -\cos(\log x)$

Answer: $-\cos(\log x)$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \tan^{-1}\left(\dfrac{6x}{1 - 9x^2}\right) dx$, where $|x| < \dfrac{1}{3}$ is:

**Options:**

- **(A)** $2x \tan^{-1} 3x + \dfrac{1}{3}\log(1 + 9x^2) + c$
- **(B)** $2x \tan^{-1} 3x - \log(1 + 9x^2) + c$
- **(C)** $2x \tan^{-1} 3x - \dfrac{1}{3}\log(1 + 9x^2) + c$
- **(D)** $x \tan^{-1} 3x + \dfrac{1}{3}\log(1 + 9x^2) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2x \tan^{-1} 3x - \dfrac{1}{3}\log(1 + 9x^2) + c$**

**Detailed Solution:**

Given integral is $I = \int \tan^{-1}\left(\dfrac{6x}{1 - 9x^2}\right) dx$

We can rewrite the argument of the inverse tangent as:

$\dfrac{6x}{1 - 9x^2} = \dfrac{2(3x)}{1 - (3x)^2}$

Using the trigonometric identity $\tan^{-1}\left(\dfrac{2\theta}{1 - \theta^2}\right) = 2\tan^{-1}\theta$ for $|\theta| < 1$, and given $|x| < \dfrac{1}{3} \Rightarrow |3x| < 1$, we get:

$\tan^{-1}\left(\dfrac{6x}{1 - 9x^2}\right) = 2\tan^{-1}(3x)$

Now, the integral becomes:

$I = \int 2\tan^{-1}(3x) dx$

Using integration by parts, taking $\tan^{-1}(3x)$ as the first function and $2$ as the second function:

$I = \tan^{-1}(3x) \int 2 dx - \int \left( \dfrac{d}{dx}(\tan^{-1}(3x)) \int 2 dx \right) dx$

$I = 2x \tan^{-1}(3x) - \int \dfrac{3}{1 + 9x^2} \cdot 2x dx$

$I = 2x \tan^{-1}(3x) - \int \dfrac{6x}{1 + 9x^2} dx$

Let $1 + 9x^2 = t$, then $18x dx = dt \Rightarrow 6x dx = \dfrac{dt}{3}$

$I = 2x \tan^{-1}(3x) - \int \dfrac{1}{3t} dt$

$I = 2x \tan^{-1}(3x) - \dfrac{1}{3}\log|t| + c$

Substituting back $t = 1 + 9x^2$:

$I = 2x \tan^{-1}(3x) - \dfrac{1}{3}\log(1 + 9x^2) + c$

Answer: $2x \tan^{-1} 3x - \dfrac{1}{3}\log(1 + 9x^2) + c$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int e^x\left(\log(\sin x) + \sqrt{\dfrac{1 + \cos 2x}{1 - \cos 2x}}\right) dx = \ldots$

**Options:**

- **(A)** $e^x \cot x + C$
- **(B)** $e^x \log \sin x + C$
- **(C)** $e^x \log \sin x + \tan x + C$
- **(D)** $e^x + \sin x + C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e^x \log \sin x + C$**

**Detailed Solution:**

We have $\sqrt{\dfrac{1 + \cos 2x}{1 - \cos 2x}} = \sqrt{\dfrac{2 \cos^2 x}{2 \sin^2 x}} = \cot x$

The given integral becomes:

$\int e^x (\log(\sin x) + \cot x) dx$

Let $f(x) = \log(\sin x)$

Differentiating with respect to $x$, we get $f'(x) = \dfrac{1}{\sin x} \cdot \cos x = \cot x$

The integral is of the standard form $\int e^x (f(x) + f'(x)) dx = e^x f(x) + C$

Therefore, the value of the integral is $e^x \log(\sin x) + C$

Answer: $e^x \log \sin x + C$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Evaluate $\displaystyle\int e^x(\sin x + 2\cos x)\sin x\, dx$

**Options:**

- **(A)** $e^x \cos x + C$
- **(B)** $e^x \sin x + C$
- **(C)** $e^x \sin^2 x + C$
- **(D)** $e^x \sin 2x + C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e^x \sin^2 x + C$**

**Detailed Solution:**

Let $I = \int e^x(\sin x + 2\cos x)\sin x \, dx$

$I = \int e^x(\sin^2 x + 2\sin x \cos x) \, dx$

$I = \int e^x(\sin^2 x + \sin 2x) \, dx$

Let $f(x) = \sin^2 x$, then $f'(x) = 2\sin x \cos x = \sin 2x$

Using the standard integral $\int e^x(f(x) + f'(x)) \, dx = e^x f(x) + C$

$I = e^x \sin^2 x + C$

Answer: $e^x \sin^2 x + C$

</details>

---

### Q5. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\int x^3 e^x\,dx = e^x(px^3 + qx^2 + rx + s) + c$, then the value of $p + q + r + s$ is

**Options:**

- **(A)** $0$
- **(B)** $-2$
- **(C)** $6$
- **(D)** $-4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

Using integration by parts successively on $\int x^3 e^x \, dx$:

$\int x^3 e^x \, dx = x^3 e^x - \int 3x^2 e^x \, dx$

$= x^3 e^x - 3 \left( x^2 e^x - \int 2x e^x \, dx \right)$

$= x^3 e^x - 3x^2 e^x + 6 \left( x e^x - \int e^x \, dx \right)$

$= x^3 e^x - 3x^2 e^x + 6x e^x - 6e^x + c$

$= e^x (x^3 - 3x^2 + 6x - 6) + c$

Comparing this with the given expression $e^x(px^3 + qx^2 + rx + s) + c$, we get:

$p = 1$

$q = -3$

$r = 6$

$s = -6$

Therefore, $p + q + r + s = 1 - 3 + 6 - 6 = -2$.

Answer: $-2$

</details>

---

### Q6. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int x^7 e^x \, dx = e^x f(x) + c$, then $f(x)$ is equal to...

**Options:**

- **(A)** $\sum_{r=0}^{7}(-1)^r x^{7-r} \cdot {}^7P_r$
- **(B)** $\sum_{r=0}^{7} x^{7-r} \cdot {}^7P_r$
- **(C)** $\sum_{r=0}^{7}(-1)^r x^{7-r} \cdot {}^7C_r$
- **(D)** $\sum_{r=0}^{7} x^{7-r} \cdot {}^7C_r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sum_{r=0}^{7}(-1)^r x^{7-r} \cdot {}^7P_r$**

**Detailed Solution:**

Using the generalized integration by parts formula (also known as the DI method), we have:

$\int u v \, dx = u v_1 - u' v_2 + u'' v_3 - u''' v_4 + \dots$

where $u$ is differentiated and $v$ is integrated repeatedly. Let $u = x^7$ and $v = e^x$.

$\int x^7 e^x \, dx = x^7 e^x - (7x^6) e^x + (7 \times 6 x^5) e^x - (7 \times 6 \times 5 x^4) e^x + \dots - (7!) e^x + c$

Factoring out $e^x$, we get:

$\int x^7 e^x \, dx = e^x [x^7 - 7x^6 + 42x^5 - 210x^4 + 840x^3 - 2520x^2 + 5040x - 5040] + c$

Comparing this with $e^x f(x) + c$, we find:

$f(x) = x^7 - 7x^6 + 42x^5 - 210x^4 + 840x^3 - 2520x^2 + 5040x - 5040$

The general term of this polynomial can be written as:

$(-1)^r \dfrac{7!}{(7-r)!} x^{7-r}$ for $r = 0, 1, 2, \dots, 7$

Since $^{7}P_{r} = \dfrac{7!}{(7-r)!}$, we can express $f(x)$ in summation notation as:

$f(x) = \sum_{r=0}^{7} (-1)^r x^{7-r} \cdot ^{7}P_{r}$

Answer: $\sum_{r=0}^{7}(-1)^r x^{7-r} \cdot {}^7P_r$

</details>

---

### Q7. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int f(x)dx = g(x) + c$ then $\int f^{-1}(x)dx =$

**Options:**

- **(A)** $xf^{-1}(x) + c$
- **(B)** $f(g^{-1}(x)) + c$
- **(C)** $xf^{-1}(x) - g(f^{-1}(x)) + c$
- **(D)** $g^{-1}(x) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $xf^{-1}(x) - g(f^{-1}(x)) + c$**

**Detailed Solution:**

Let $I = \int f^{-1}(x) dx$

Substitute $f^{-1}(x) = t \Rightarrow x = f(t) \Rightarrow dx = f'(t) dt$

$I = \int t f'(t) dt$

Applying integration by parts, taking $t$ as the first function and $f'(t)$ as the second function:

$I = t \int f'(t) dt - \int \left( \dfrac{d}{dt}(t) \int f'(t) dt \right) dt$

$I = t f(t) - \int f(t) dt$

Given $\int f(x) dx = g(x) + c$, we have $\int f(t) dt = g(t) + c$

$I = t f(t) - g(t) + C$

Substituting $t = f^{-1}(x)$ and $f(t) = x$:

$I = x f^{-1}(x) - g(f^{-1}(x)) + C$

Answer: $xf^{-1}(x) - g(f^{-1}(x)) + c$

</details>

---

### Q8. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \left(e^{\log(\sin x)} + \cos x\right) x\, dx = $

**Options:**

- **(A)** $x(\sin x + \cos x) + (\sin x - \cos x) + c$
- **(B)** $x(\sin x - \cos x) + (\sin x - \cos x) + c$
- **(C)** $x(\sin x + \cos x) + (\sin x + \cos x) + c$
- **(D)** $x(\sin x - \cos x) + (\sin x + \cos x) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x(\sin x - \cos x) + (\sin x + \cos x) + c$**

**Detailed Solution:**

Using the property $e^{\log f(x)} = f(x)$, the given integral simplifies to:

$\int x(\sin x + \cos x) dx$

Applying integration by parts, taking $x$ as the first function and $(\sin x + \cos x)$ as the second function:

$\int x(\sin x + \cos x) dx = x \int (\sin x + \cos x) dx - \int \left( \dfrac{d}{dx}(x) \int (\sin x + \cos x) dx \right) dx$

$= x(\sin x - \cos x) - \int 1 \cdot (\sin x - \cos x) dx$

$= x(\sin x - \cos x) - (-\cos x - \sin x) + c$

$= x(\sin x - \cos x) + (\sin x + \cos x) + c$

Answer: $x(\sin x - \cos x) + (\sin x + \cos x) + c$

</details>

---

### Q9. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of integral $\int x^3 \cos x\,dx$ is...

**Options:**

- **(A)** $x^3\sin x + x^2\cos x - 6x\sin x + 6\cos x + c$
- **(B)** $x^3\sin x + 3x^2\sin x - 6x\sin x - 6\cos x + c$
- **(C)** $x^3\sin x + 3x^2\cos x - 6x\sin x - 6\cos x + c$
- **(D)** $x^3\sin x + 3x^2\cos x - 6x\sin x + 6\cos x + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^3\sin x + 3x^2\cos x - 6x\sin x - 6\cos x + c$**

**Detailed Solution:**

Let $I = \int x^3 \cos x \, dx$.

Using integration by parts, $\int u \, dv = uv - \int v \, du$.

Taking $u = x^3$ and $dv = \cos x \, dx$, we get:

$I = x^3 \sin x - \int 3x^2 \sin x \, dx$

Applying integration by parts again for $\int 3x^2 \sin x \, dx$ with $u = 3x^2$ and $dv = \sin x \, dx$:

$I = x^3 \sin x - \left[ 3x^2 (-\cos x) - \int 6x (-\cos x) \, dx \right]$

$I = x^3 \sin x + 3x^2 \cos x - \int 6x \cos x \, dx$

Applying integration by parts once more for $\int 6x \cos x \, dx$ with $u = 6x$ and $dv = \cos x \, dx$:

$I = x^3 \sin x + 3x^2 \cos x - \left[ 6x \sin x - \int 6 \sin x \, dx \right]$

$I = x^3 \sin x + 3x^2 \cos x - 6x \sin x + \int 6 \sin x \, dx$

$I = x^3 \sin x + 3x^2 \cos x - 6x \sin x - 6 \cos x + c$

Answer: $x^3\sin x + 3x^2\cos x - 6x\sin x - 6\cos x + c$

</details>

---

### Q10. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int\sin(\log x)\,dx = $

**Options:**

- **(A)** $\dfrac{x}{2}[\sin(\log x) - \cos(\log x)] + c$
- **(B)** $\dfrac{x}{2}[\sin(\log x) + \cos(\log x)] + c$
- **(C)** $\dfrac{x}{2}[\cos(\log x) - \sin(\log x)] + c$
- **(D)** $\dfrac{x}{4}[\cos(\log x) - \sin(\log x)] + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{x}{2}[\sin(\log x) - \cos(\log x)] + c$**

**Detailed Solution:**

Let $I = \int \sin(\log x) \, dx$

Using integration by parts, taking $1$ as the second function:

$I = \sin(\log x) \int 1 \, dx - \int \left( \dfrac{d}{dx}(\sin(\log x)) \int 1 \, dx \right) dx$

$I = x \sin(\log x) - \int \cos(\log x) \cdot \dfrac{1}{x} \cdot x \, dx$

$I = x \sin(\log x) - \int \cos(\log x) \, dx$

Applying integration by parts again to the second integral:

$I = x \sin(\log x) - \left[ \cos(\log x) \int 1 \, dx - \int \left( \dfrac{d}{dx}(\cos(\log x)) \int 1 \, dx \right) dx \right]$

$I = x \sin(\log x) - \left[ x \cos(\log x) - \int \left( -\sin(\log x) \cdot \dfrac{1}{x} \cdot x \right) dx \right]$

$I = x \sin(\log x) - x \cos(\log x) - \int \sin(\log x) \, dx$

$I = x \sin(\log x) - x \cos(\log x) - I$

$2I = x [\sin(\log x) - \cos(\log x)]$

$I = \dfrac{x}{2} [\sin(\log x) - \cos(\log x)] + c$

Answer: $\dfrac{x}{2}[\sin(\log x) - \cos(\log x)] + c$

</details>

---

### Q11. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int x^3 \log x\,dx = $

**Options:**

- **(A)** $\dfrac{x^4}{16}[4\log x - 1] + c$
- **(B)** $\dfrac{x^4}{16}[4\log x + 1] + c$
- **(C)** $\dfrac{x^4}{16}[-4\log x - 1] + c$
- **(D)** $\dfrac{x^4}{16}[-4\log x + 1] + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{x^4}{16}[4\log x - 1] + c$**

**Detailed Solution:**

Using integration by parts, $\int u v \, dx = u \int v \, dx - \int \left( \dfrac{du}{dx} \int v \, dx \right) dx$

Let $u = \log x$ and $v = x^3$

$\int x^3 \log x \, dx = (\log x) \left( \dfrac{x^4}{4} \right) - \int \left( \dfrac{1}{x} \left( \dfrac{x^4}{4} \right) \right) dx$

$= \dfrac{x^4}{4} \log x - \int \dfrac{x^3}{4} \, dx$

$= \dfrac{x^4}{4} \log x - \dfrac{x^4}{16} + c$

$= \dfrac{x^4}{16}[4\log x - 1] + c$

Answer: $\dfrac{x^4}{16}[4\log x - 1] + c$

</details>

---

### Q12. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \cos x$, then the value of $\int\dfrac{e^{f(x)}(x\sin^3 x + f(x))}{1 - (f(x))^2}dx = $

**Options:**

- **(A)** $e^{f(x)}(-\text{cosec}\ x - x) + c$
- **(B)** $e^{f(x)}(\text{cosec}\,x + x) + c$
- **(C)** $e^{f(x)}(\cos x - x) + c$
- **(D)** $e^{f(x)}(\cot^2 x + x) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^{f(x)}(-\text{cosec}\ x - x) + c$**

**Detailed Solution:**

Given $f(x) = \cos x$.

Substituting $f(x)$ into the integral, we get:

$I = \int \dfrac{e^{\cos x}(x\sin^3 x + \cos x)}{1 - \cos^2 x} dx$

$I = \int \dfrac{e^{\cos x}(x\sin^3 x + \cos x)}{\sin^2 x} dx$

$I = \int e^{\cos x} \left( x\sin x + \dfrac{\cos x}{\sin^2 x} \right) dx$

$I = \int e^{\cos x} (x\sin x + \text{cosec}\ x \cot x) dx$

We know that $\dfrac{d}{dx} \left( e^{\cos x} g(x) \right) = e^{\cos x} (g'(x) - g(x)\sin x)$.

Let $g'(x) - g(x)\sin x = x\sin x + \text{cosec}\ x \cot x$.

By observation, if we choose $g(x) = -x - \text{cosec}\ x$, then:

$g'(x) = -1 + \text{cosec}\ x \cot x$

$-g(x)\sin x = (x + \text{cosec}\ x)\sin x = x\sin x + 1$

Adding these gives:

$g'(x) - g(x)\sin x = -1 + \text{cosec}\ x \cot x + x\sin x + 1 = x\sin x + \text{cosec}\ x \cot x$.

Thus, the integral evaluates to $e^{\cos x} g(x) + c$.

$I = e^{\cos x} (-x - \text{cosec}\ x) + c$

Substituting back $f(x) = \cos x$:

$I = e^{f(x)} (-\text{cosec}\ x - x) + c$

Answer: $e^{f(x)}(-\text{cosec}\ x - x) + c$

</details>

---

### Q13. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If an antiderivative of $f(x)$ is $e^x$ and an antiderivative of $g(x)$ is $\cos x$, then $\int f(x)\cos x\, dx + \int g(x)e^x\, dx = $

**Options:**

- **(A)** $e^x \sin x + c$
- **(B)** $e^x(f(x) + g(x)) + c$
- **(C)** $e^x \cos x + c$
- **(D)** $e^x + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e^x \cos x + c$**

**Detailed Solution:**

Given that an antiderivative of $f(x)$ is $e^x$, we have $\int f(x)\, dx = e^x \Rightarrow f(x) = \dfrac{d}{dx}(e^x) = e^x$.

Given that an antiderivative of $g(x)$ is $\cos x$, we have $\int g(x)\, dx = \cos x \Rightarrow g(x) = \dfrac{d}{dx}(\cos x) = -\sin x$.

We need to evaluate the integral:

$I = \int f(x)\cos x\, dx + \int g(x)e^x\, dx$

Substituting $f(x) = e^x$ and $g(x) = -\sin x$:

$I = \int e^x \cos x\, dx + \int (-\sin x)e^x\, dx$

$I = \int e^x (\cos x - \sin x)\, dx$

Using the standard integral formula $\int e^x (h(x) + h'(x))\, dx = e^x h(x) + c$, where $h(x) = \cos x$ and $h'(x) = -\sin x$:

$I = e^x \cos x + c$

Answer: $e^x \cos x + c$

</details>

---

### Q14. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\int x^2 \cdot e^x dx = e^x f(x) + c$, then the minimum value of $f(x)$ is ...

**Options:**

- **(A)** $0$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $\dfrac{-1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Using integration by parts:

$\int x^2 e^x dx = x^2 e^x - \int 2x e^x dx$

$= x^2 e^x - 2(x e^x - \int e^x dx)$

$= x^2 e^x - 2x e^x + 2e^x + c$

$= e^x (x^2 - 2x + 2) + c$

Comparing with the given expression, we get $f(x) = x^2 - 2x + 2$.

To find the minimum value of $f(x)$, we can complete the square:

$f(x) = (x - 1)^2 + 1$

Since $(x - 1)^2 \geq 0$ for all real $x$, the minimum value of $f(x)$ is $1$.

Answer: $1$

</details>

---

### Q15. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\int e^{2x} \dfrac{2(\sin 2x \cos 2x - 1)}{2 \sin^2 2x} \, dx = A \, e^{2x} \cot 2x + c$
(Where c is the constant of integration.), then $A^3 =$

**Options:**

- **(A)** $\dfrac{1}{8}$
- **(B)** $64$
- **(C)** $8$
- **(D)** $\dfrac{1}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{8}$**

**Detailed Solution:**

Let the given integral be $I$.

$I = \int e^{2x} \dfrac{2(\sin 2x \cos 2x - 1)}{2 \sin^2 2x} \, dx$

$I = \int e^{2x} \left( \dfrac{\sin 2x \cos 2x}{\sin^2 2x} - \dfrac{1}{\sin^2 2x} \right) \, dx$

$I = \int e^{2x} (\cot 2x - \csc^2 2x) \, dx$

We know the standard integral form: $\int e^{ax} (a f(x) + f'(x)) \, dx = e^{ax} f(x) + c$.

Let $a = 2$ and $f(x) = \dfrac{1}{2} \cot 2x$.

Then $a f(x) = 2 \left( \dfrac{1}{2} \cot 2x \right) = \cot 2x$.

Differentiating $f(x)$ with respect to $x$, we get:

$f'(x) = \dfrac{1}{2} (-\csc^2 2x) \times 2 = -\csc^2 2x$

Substituting these into the integral, we get:

$I = \int e^{2x} (2 f(x) + f'(x)) \, dx = e^{2x} f(x) + c$

$I = \dfrac{1}{2} e^{2x} \cot 2x + c$

Comparing this with the given expression $A \, e^{2x} \cot 2x + c$, we find:

$A = \dfrac{1}{2}$

Therefore, $A^3 = \left(\dfrac{1}{2}\right)^3 = \dfrac{1}{8}$.

Answer: $\dfrac{1}{8}$

</details>

---

### Q16. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \mathrm{e}^x \cos x \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{\mathrm{e}^x(\sin x+\cos x)}{2}+\mathrm{c}, \quad$ where c is the constant of integration.
- **(B)** $\frac{\mathrm{e}^x \cos x}{2}+\sin x+\mathrm{c}, \quad$ where c is the constant of integration.
- **(C)** $\mathrm{e}^x\left(\frac{\cos x-\sin x}{2}\right)+\mathrm{c}, \quad$ where c is the constant of integration.
- **(D)** $\mathrm{e}^x\left(\frac{\sin x-\cos x}{2}\right)+\mathrm{c}, \quad$ where c is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{e}^x(\sin x+\cos x)}{2}+\mathrm{c}, \quad$ where c is the constant of integration.**

**Detailed Solution:**

Let $I = \int \mathrm{e}^x \cos x \mathrm{~d} x$

Using integration by parts, taking $\cos x$ as the first function and $\mathrm{e}^x$ as the second function:

$I = \cos x \int \mathrm{e}^x \mathrm{~d} x - \int \left( \dfrac{\mathrm{d}}{\mathrm{d}x}(\cos x) \int \mathrm{e}^x \mathrm{~d} x \right) \mathrm{d} x$

$I = \mathrm{e}^x \cos x - \int (-\sin x) \mathrm{e}^x \mathrm{~d} x$

$I = \mathrm{e}^x \cos x + \int \mathrm{e}^x \sin x \mathrm{~d} x$

Applying integration by parts again on the second term:

$I = \mathrm{e}^x \cos x + \left[ \sin x \int \mathrm{e}^x \mathrm{~d} x - \int \left( \dfrac{\mathrm{d}}{\mathrm{d}x}(\sin x) \int \mathrm{e}^x \mathrm{~d} x \right) \mathrm{d} x \right]$

$I = \mathrm{e}^x \cos x + \mathrm{e}^x \sin x - \int \mathrm{e}^x \cos x \mathrm{~d} x$

$I = \mathrm{e}^x (\cos x + \sin x) - I$

$2I = \mathrm{e}^x (\sin x + \cos x)$

$I = \dfrac{\mathrm{e}^x(\sin x + \cos x)}{2} + \mathrm{c}$

Answer: $\frac{\mathrm{e}^x(\sin x+\cos x)}{2}+\mathrm{c}, \quad$ where c is the constant of integration.

</details>

---

### Q17. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $I=\int \tan ^{-1}\left(\frac{2 x}{1-x^2}\right) d x$, then $I-2 x \tan ^{-1} x=$

**Options:**

- **(A)** $-\log \left(1+x^2\right)+\mathrm{c}$
- **(B)** $\log \left(1+x^2\right)+\mathrm{c}$
- **(C)** $-\log \left(1-x^2\right)+c$
- **(D)** $\log \left|\frac{2 \mathrm{x}}{1-\mathrm{x}^2}\right|+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\log \left(1+x^2\right)+\mathrm{c}$**

**Detailed Solution:**

$I = \int \tan^{-1}\left(\dfrac{2x}{1-x^2}\right) dx$

Substitute $x = \tan \theta \Rightarrow dx = \sec^2 \theta d\theta$

$I = \int \tan^{-1}(\tan 2\theta) \sec^2 \theta d\theta$

$I = \int 2\theta \sec^2 \theta d\theta$

Using integration by parts:

$I = 2\theta \tan \theta - \int 2 \tan \theta d\theta$

$I = 2\theta \tan \theta - 2 \log|\sec \theta| + c$

Substituting back $\tan \theta = x$, $\theta = \tan^{-1} x$, and $\sec \theta = \sqrt{1+x^2}$:

$I = 2x \tan^{-1} x - 2 \log(1+x^2)^{1/2} + c$

$I = 2x \tan^{-1} x - \log(1+x^2) + c$

$I - 2x \tan^{-1} x = -\log(1+x^2) + c$

Answer: $-\log \left(1+x^2\right)+\mathrm{c}$

</details>

---

### Q18. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int x^2 \cos x \mathrm{~d} x=$

**Options:**

- **(A)** $x^2 \sin x+2 x \cos x-2 \sin x+\mathrm{c}$ where c is the constant of integration
- **(B)** $x^2 \sin x-2 x \cos x-2 \sin x+\mathrm{c}$ where $c$ is the constant of integration
- **(C)** $x^2 \sin x-2 x \cos x+2 \sin x+c$
where c is the constant of integration
- **(D)** $x^2 \sin x+2 x \cos x+2 \sin x+c$
where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x^2 \sin x+2 x \cos x-2 \sin x+\mathrm{c}$ where c is the constant of integration**

**Detailed Solution:**

Let $I = \int x^2 \cos x \, dx$

Using integration by parts, $\int u v \, dx = u \int v \, dx - \int \left( \dfrac{du}{dx} \int v \, dx \right) dx$

Taking $u = x^2$ and $v = \cos x$:

$I = x^2 \sin x - \int 2x \sin x \, dx$

Applying integration by parts again for $\int 2x \sin x \, dx$ with $u = 2x$ and $v = \sin x$:

$\int 2x \sin x \, dx = 2x (-\cos x) - \int 2 (-\cos x) \, dx$

$\int 2x \sin x \, dx = -2x \cos x + 2 \sin x$

Substituting this back into $I$:

$I = x^2 \sin x - (-2x \cos x + 2 \sin x) + c$

$I = x^2 \sin x + 2x \cos x - 2 \sin x + c$

Answer: $x^2 \sin x+2 x \cos x-2 \sin x+\mathrm{c}$ where c is the constant of integration

</details>

---

### Q19. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \mathrm{e}^x\left(\frac{x+5}{(x+6)^2}\right) \mathrm{d} x$ is

**Options:**

- **(A)** $\frac{\mathrm{e}^x}{(x+6)^2}+\mathrm{c}$, where c is the constant of integration.
- **(B)** $\frac{e^x}{x+5}+c,$ where $c$ is the constant of integration.
- **(C)** $\frac{\mathrm{e}^x}{(x+5)^2}+\mathrm{c}$, where c is the constant of integration.
- **(D)** $\frac{\mathrm{e}^x}{x+6}+\mathrm{c},$ where c is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{e}^x}{x+6}+\mathrm{c},$ where c is the constant of integration.**

**Detailed Solution:**

Let $I = \int \mathrm{e}^x\left(\dfrac{x+5}{(x+6)^2}\right) \mathrm{d} x$

Adding and subtracting $1$ in the numerator, we get:

$I = \int \mathrm{e}^x\left(\dfrac{x+6-1}{(x+6)^2}\right) \mathrm{d} x$

$I = \int \mathrm{e}^x\left(\dfrac{x+6}{(x+6)^2} - \dfrac{1}{(x+6)^2}\right) \mathrm{d} x$

$I = \int \mathrm{e}^x\left(\dfrac{1}{x+6} - \dfrac{1}{(x+6)^2}\right) \mathrm{d} x$

Using the standard integral $\int \mathrm{e}^x [f(x) + f'(x)] \mathrm{d} x = \mathrm{e}^x f(x) + \mathrm{c}$

Here, $f(x) = \dfrac{1}{x+6}$ and $f'(x) = -\dfrac{1}{(x+6)^2}$

Therefore, $I = \dfrac{\mathrm{e}^x}{x+6} + \mathrm{c}$

Answer: $\frac{\mathrm{e}^x}{x+6}+\mathrm{c},$ where c is the constant of integration.

</details>

---

### Q20. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \mathrm{e}^{2 x} \frac{(\sin 2 x \cos 2 x-1)}{\sin ^2 2 x} \mathrm{~d} x=$

**Options:**

- **(A)** $\mathrm{e}^{2 x} \cot (2 x)+\mathrm{c}$, where c is the constant of integration
- **(B)** $2 \mathrm{e}^{2 x} \cot (2 x)+\mathrm{c}$, where c is the constant of integration
- **(C)** $4 e^{2 x} \cot (2 x)+c$, where $c$ is the constant of integration
- **(D)** $\frac{1}{2} \mathrm{e}^{2 x} \cot (2 x)+\mathrm{c}$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2} \mathrm{e}^{2 x} \cot (2 x)+\mathrm{c}$, where c is the constant of integration**

**Detailed Solution:**

Let the given integral be $I = \int \mathrm{e}^{2x} \dfrac{\sin 2x \cos 2x - 1}{\sin^2 2x} \mathrm{d}x$

Separating the terms in the numerator, we get:

$I = \int \mathrm{e}^{2x} \left( \dfrac{\sin 2x \cos 2x}{\sin^2 2x} - \dfrac{1}{\sin^2 2x} \right) \mathrm{d}x$

$I = \int \mathrm{e}^{2x} (\cot 2x - \csc^2 2x) \mathrm{d}x$

We know the standard integral formula:

$\int \mathrm{e}^{kx} [k f(x) + f'(x)] \mathrm{d}x = \mathrm{e}^{kx} f(x) + c$

To express the integrand in this form, let $k = 2$. We need $2 f(x) = \cot 2x$, which gives:

$f(x) = \dfrac{1}{2} \cot 2x$

Differentiating $f(x)$ with respect to $x$, we get:

$f'(x) = \dfrac{1}{2} (-\csc^2 2x) \times 2 = -\csc^2 2x$

Since the integrand perfectly matches the form $\mathrm{e}^{2x} [2 f(x) + f'(x)]$, the integral evaluates to:

$I = \mathrm{e}^{2x} f(x) + c$

$I = \dfrac{1}{2} \mathrm{e}^{2x} \cot 2x + c$

Answer: $\frac{1}{2} \mathrm{e}^{2 x} \cot (2 x)+\mathrm{c}$, where c is the constant of integration

</details>

---

### Q21. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int e^x \frac{(x-1)}{(x+1)^3} \mathrm{~d} x=$

**Options:**

- **(A)** $\mathrm{e}^x(x+1)^2+\mathrm{c}, \quad$ where c is the constant of integration
- **(B)** $\mathrm{e}^x(x+1)^3+\mathrm{c}$, where c is the constant of integration
- **(C)** $\frac{\mathrm{e}^x}{(x+1)^2}+\mathrm{c}, \quad$ where c is the constant of integration
- **(D)** $\frac{\mathrm{e}^x}{(x+1)^3}+\mathrm{c}, \quad$ where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{e}^x}{(x+1)^2}+\mathrm{c}, \quad$ where c is the constant of integration**

**Detailed Solution:**

Let $I = \int e^x \dfrac{x-1}{(x+1)^3} \mathrm{~d} x$

Adding and subtracting $1$ in the numerator:

$I = \int e^x \left( \dfrac{x+1-2}{(x+1)^3} \right) \mathrm{~d} x$

$I = \int e^x \left( \dfrac{1}{(x+1)^2} - \dfrac{2}{(x+1)^3} \right) \mathrm{~d} x$

Let $f(x) = \dfrac{1}{(x+1)^2}$, then $f'(x) = \dfrac{-2}{(x+1)^3}$

Using the standard integral $\int e^x (f(x) + f'(x)) \mathrm{~d} x = e^x f(x) + c$:

$I = \dfrac{e^x}{(x+1)^2} + c$

Answer: $\frac{\mathrm{e}^x}{(x+1)^2}+\mathrm{c}, \quad$ where c is the constant of integration

</details>

---

### Q22. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \log (2+x)^{2+x} \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{(2+x)^2}{2} \log \left(\frac{2+x}{\sqrt{\mathrm{e}}}\right)+\mathrm{c}$, where c is the constant of integration
- **(B)** $\frac{(2+x)^2}{2} \log \left(\frac{2+x}{e}\right)+\mathrm{c}$, where c is the constant of integration
- **(C)** $\frac{2+x}{2} \log \left(\frac{2+x}{\sqrt{\mathrm{e}}}\right)+\mathrm{c}$, where c is the constant of integration
- **(D)** $\frac{2+x}{2} \log (2+x) \sqrt{\mathrm{e}}+\mathrm{c}$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{(2+x)^2}{2} \log \left(\frac{2+x}{\sqrt{\mathrm{e}}}\right)+\mathrm{c}$, where c is the constant of integration**

**Detailed Solution:**

Let $I = \int \log (2+x)^{2+x} \mathrm{d} x$

Using the property of logarithms, $\log a^b = b \log a$, we get:

$I = \int (2+x) \log (2+x) \mathrm{d} x$

Substitute $2+x = t$, which gives $\mathrm{d}x = \mathrm{d}t$:

$I = \int t \log t \mathrm{d}t$

Using integration by parts, taking $\log t$ as the first function and $t$ as the second function:

$I = \log t \int t \mathrm{d}t - \int \left( \dfrac{\mathrm{d}}{\mathrm{d}t}(\log t) \int t \mathrm{d}t \right) \mathrm{d}t$

$I = (\log t) \dfrac{t^2}{2} - \int \dfrac{1}{t} \cdot \dfrac{t^2}{2} \mathrm{d}t$

$I = \dfrac{t^2}{2} \log t - \dfrac{1}{2} \int t \mathrm{d}t$

$I = \dfrac{t^2}{2} \log t - \dfrac{t^2}{4} + \mathrm{c}$

$I = \dfrac{t^2}{2} \left( \log t - \dfrac{1}{2} \right) + \mathrm{c}$

Since $\dfrac{1}{2} = \log \mathrm{e}^{1/2} = \log \sqrt{\mathrm{e}}$:

$I = \dfrac{t^2}{2} \left( \log t - \log \sqrt{\mathrm{e}} \right) + \mathrm{c}$

$I = \dfrac{t^2}{2} \log \left( \dfrac{t}{\sqrt{\mathrm{e}}} \right) + \mathrm{c}$

Substituting back $t = 2+x$:

$I = \dfrac{(2+x)^2}{2} \log \left( \dfrac{2+x}{\sqrt{\mathrm{e}}} \right) + \mathrm{c}$

Answer: $\frac{(2+x)^2}{2} \log \left(\frac{2+x}{\sqrt{\mathrm{e}}}\right)+\mathrm{c}$, where c is the constant of integration

</details>

---

### Q23. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)=1+x ; \mathrm{g}(x)=\log x$, then $\int \mathrm{g}(\mathrm{f}(x)) \mathrm{d} x$ is equal to

**Options:**

- **(A)** $(1+x) \log (1+x)-x+\mathrm{c}$,
(where c is a constant of integration)
- **(B)** $(1+x) \log x-x+\mathrm{c}$,
(where c is a constant of integration)
- **(C)** $x \log (1+x)+\mathrm{c}$,
(where c is a constant of integration)
- **(D)** $(1+x) \log (1+x)+x+\mathrm{c}$, (where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(1+x) \log (1+x)-x+\mathrm{c}$,
(where c is a constant of integration)**

**Detailed Solution:**

Given $\mathrm{f}(x) = 1+x$ and $\mathrm{g}(x) = \log x$.

$\mathrm{g}(\mathrm{f}(x)) = \mathrm{g}(1+x) = \log(1+x)$

Let $I = \int \mathrm{g}(\mathrm{f}(x)) \mathrm{d}x = \int \log(1+x) \mathrm{d}x$

Using integration by parts, taking $1$ as the second function:

$I = \log(1+x) \int 1 \mathrm{d}x - \int \left( \dfrac{\mathrm{d}}{\mathrm{d}x} \log(1+x) \int 1 \mathrm{d}x \right) \mathrm{d}x$

$I = x \log(1+x) - \int \dfrac{x}{1+x} \mathrm{d}x$

$I = x \log(1+x) - \int \dfrac{x+1-1}{1+x} \mathrm{d}x$

$I = x \log(1+x) - \int \left( 1 - \dfrac{1}{1+x} \right) \mathrm{d}x$

$I = x \log(1+x) - (x - \log(1+x)) + \mathrm{c}$

$I = (1+x) \log(1+x) - x + \mathrm{c}$

Answer: $(1+x) \log (1+x)-x+\mathrm{c}$,
(where c is a constant of integration)

</details>

---

### Q24. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \dfrac{1+\sin (\log x)}{1+\cos (\log x)} \mathrm{d} x=$

**Options:**

- **(A)** $x^2 \tan \left(\dfrac{\log x}{2}\right)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\quad x \tan \left(\log \left(\dfrac{x}{2}\right)\right)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $x^3 \log \left(\dfrac{\tan x}{2}\right)+\mathrm{c}$, where c is a constant of
- **(D)** $x \cdot \tan \left(\dfrac{\log x}{2}\right)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \cdot \tan \left(\dfrac{\log x}{2}\right)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $\log x = t \Rightarrow x = e^t \Rightarrow \mathrm{d}x = e^t \mathrm{d}t$

Substituting these into the integral, we get:

$I = \int e^t \left( \dfrac{1+\sin t}{1+\cos t} \right) \mathrm{d}t$

Using the half-angle formulas $\sin t = 2\sin\left(\dfrac{t}{2}\right)\cos\left(\dfrac{t}{2}\right)$ and $1+\cos t = 2\cos^2\left(\dfrac{t}{2}\right)$:

$I = \int e^t \left( \dfrac{1 + 2\sin\left(\dfrac{t}{2}\right)\cos\left(\dfrac{t}{2}\right)}{2\cos^2\left(\dfrac{t}{2}\right)} \right) \mathrm{d}t$

$I = \int e^t \left( \dfrac{1}{2}\sec^2\left(\dfrac{t}{2}\right) + \tan\left(\dfrac{t}{2}\right) \right) \mathrm{d}t$

This is of the form $\int e^t (f(t) + f'(t)) \mathrm{d}t = e^t f(t) + c$, where $f(t) = \tan\left(\dfrac{t}{2}\right)$ and $f'(t) = \dfrac{1}{2}\sec^2\left(\dfrac{t}{2}\right)$.

$I = e^t \tan\left(\dfrac{t}{2}\right) + c$

Substituting $t = \log x$ and $e^t = x$:

$I = x \tan\left(\dfrac{\log x}{2}\right) + c$

Answer: $x \cdot \tan \left(\dfrac{\log x}{2}\right)+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q25. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\mathrm{I}=\int \dfrac{(x-1) \mathrm{e}^x}{(x+1)^3} \mathrm{~d} x$ is

**Options:**

- **(A)** $\dfrac{-\mathrm{e}^x}{(x+1)^2}+\mathrm{C}$, (where C is a constant of
integration)
- **(B)** $\dfrac{-x \mathrm{e}^x}{(x+1)^2}+\mathrm{C}$, (where C is a constant of integration)
- **(C)** $\dfrac{x \mathrm{e}^x}{(x+1)^2}+\mathrm{C}$, (where C is a constant of integration)
- **(D)** $\dfrac{\mathrm{e}^x}{(x+1)^2}+\mathrm{C}$, (where C is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\mathrm{e}^x}{(x+1)^2}+\mathrm{C}$, (where C is a constant of integration)**

**Detailed Solution:**

The given integral is $\mathrm{I} = \int \dfrac{(x-1) \mathrm{e}^x}{(x+1)^3} \mathrm{~d} x$

We can rewrite the numerator as $(x+1-2)$ to split the fraction:

$\mathrm{I} = \int \mathrm{e}^x \left( \dfrac{x+1-2}{(x+1)^3} \right) \mathrm{~d} x$

$\mathrm{I} = \int \mathrm{e}^x \left( \dfrac{1}{(x+1)^2} - \dfrac{2}{(x+1)^3} \right) \mathrm{~d} x$

Let $f(x) = \dfrac{1}{(x+1)^2}$, then its derivative is $f'(x) = \dfrac{-2}{(x+1)^3}$.

Using the standard integral formula $\int \mathrm{e}^x [f(x) + f'(x)] \mathrm{~d} x = \mathrm{e}^x f(x) + \mathrm{C}$, we get:

$\mathrm{I} = \dfrac{\mathrm{e}^x}{(x+1)^2} + \mathrm{C}$

Answer: $\dfrac{\mathrm{e}^x}{(x+1)^2}+\mathrm{C}$, (where C is a constant of integration)

</details>

---

### Q26. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $I=\int e^{\sin \theta}\left(\log \sin \theta+\operatorname{cosec}^2 \theta\right) \cos \theta d \theta$, then $I$ is equal to

**Options:**

- **(A)** $\mathrm{e}^{\sin \theta}\left(\log \sin \theta+\operatorname{cosec}^2 \theta\right)+\mathrm{c}$, (where c is a constant of integration)
- **(B)** $\mathrm{e}^{\sin \theta}(\log \sin \theta+\operatorname{cosec} \theta)+\mathrm{c}$, (where c is a constant of integration)
- **(C)** $\mathrm{e}^{\sin \theta}(\log \sin \theta-\operatorname{cosec} \theta)+\mathrm{c}$, (where c is a constant of integration)
- **(D)** $\mathrm{e}^{\sin \theta}\left(\log \sin \theta-\operatorname{cosec}^2 \theta\right)+\mathrm{c}, \quad($ where c is a constant of integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{e}^{\sin \theta}(\log \sin \theta-\operatorname{cosec} \theta)+\mathrm{c}$, (where c is a constant of integration)**

**Detailed Solution:**

Let $t = \sin \theta$, then $dt = \cos \theta d\theta$.

Substituting this into the integral, we get:

$I = \int e^t \left(\log t + \dfrac{1}{t^2}\right) dt$

We can rewrite the integrand by adding and subtracting $\dfrac{1}{t}$:

$I = \int e^t \left(\log t - \dfrac{1}{t} + \dfrac{1}{t} + \dfrac{1}{t^2}\right) dt$

Let $f(t) = \log t - \dfrac{1}{t}$.

Then $f'(t) = \dfrac{1}{t} - \left(-\dfrac{1}{t^2}\right) = \dfrac{1}{t} + \dfrac{1}{t^2}$.

Using the standard integral form $\int e^t (f(t) + f'(t)) dt = e^t f(t) + c$, we have:

$I = e^t \left(\log t - \dfrac{1}{t}\right) + c$

Substituting back $t = \sin \theta$, we get:

$I = e^{\sin \theta} \left(\log \sin \theta - \dfrac{1}{\sin \theta}\right) + c$

$I = e^{\sin \theta} (\log \sin \theta - \operatorname{cosec} \theta) + c$

Answer: $\mathrm{e}^{\sin \theta}(\log \sin \theta-\operatorname{cosec} \theta)+\mathrm{c}$, (where c is a constant of integration)

</details>

---

### Q27. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\int \dfrac{(x-1) \mathrm{e}^x}{(x+1)^3} \mathrm{~d} x$ is equal to

**Options:**

- **(A)** $\dfrac{\mathrm{e}^x}{(x+1)}+\mathrm{c}$, (where c is constant of integration)
- **(B)** $\dfrac{\mathrm{e}^x}{(x+1)^2}+\mathrm{c}$, (where c is constant of integration)
- **(C)** $\dfrac{-\mathrm{e}^x}{(x+1)}+\mathrm{c}$, (where c is constant of integration)
- **(D)** $\dfrac{-\mathrm{e}^x}{(x+1)^2}+\mathrm{c}$, (where c is constant of ' integration)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\mathrm{e}^x}{(x+1)^2}+\mathrm{c}$, (where c is constant of integration)**

**Detailed Solution:**

Let $I = \int \dfrac{(x - 1)e^x}{(x + 1)^3} dx$

$I = \int e^x \left[ \dfrac{(x + 1) - 2}{(x + 1)^3} \right] dx$

$I = \int e^x \left[ \dfrac{1}{(x + 1)^2} - \dfrac{2}{(x + 1)^3} \right] dx$

Let $f(x) = \dfrac{1}{(x + 1)^2}$

Then $f'(x) = \dfrac{-2}{(x + 1)^3}$

The integral is of the form $\int e^x [f(x) + f'(x)] dx = e^x f(x) + c$

Therefore, $I = e^x \left( \dfrac{1}{(x + 1)^2} \right) + c$

$I = \dfrac{e^x}{(x + 1)^2} + c$

</details>

---

### Q28. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int\left(f(x) \mathrm{g}^{\prime \prime}(x)-\mathrm{f}^{\prime \prime}(x) \mathrm{g}(x)\right) \mathrm{d} x$ is equal to

**Options:**

- **(A)** $\mathrm{f}(x) \mathrm{g}(x)-\mathrm{f}^{\prime}(x) \mathrm{g}^{\prime}(x)$
- **(B)** $\mathrm{f}^{\prime}(x) \mathrm{g}(x)-\mathrm{f}(x) \mathrm{g}^{\prime}(x)$
- **(C)** $\mathrm{f}(x) \mathrm{g}^{\prime}(x)-\mathrm{f}^{\prime}(x) \mathrm{g}(x)$
- **(D)** $\mathrm{f}(x) \mathrm{g}^{\prime}(x)+\mathrm{f}^{\prime}(x) \mathrm{g}(x)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{f}(x) \mathrm{g}^{\prime}(x)-\mathrm{f}^{\prime}(x) \mathrm{g}(x)$**

**Detailed Solution:**

Let $I = \int \left( f(x) g''(x) - f''(x) g(x) \right) dx$

Consider the derivative of $f(x) g'(x) - f'(x) g(x)$ with respect to $x$:

$\dfrac{d}{dx} \left( f(x) g'(x) - f'(x) g(x) \right) = \left( f'(x) g'(x) + f(x) g''(x) \right) - \left( f''(x) g(x) + f'(x) g'(x) \right)$

$\dfrac{d}{dx} \left( f(x) g'(x) - f'(x) g(x) \right) = f(x) g''(x) - f''(x) g(x)$

Integrating both sides with respect to $x$:

$\int \left( f(x) g''(x) - f''(x) g(x) \right) dx = f(x) g'(x) - f'(x) g(x) + C$

Answer: $\mathrm{f}(x) \mathrm{g}^{\prime}(x)-\mathrm{f}^{\prime}(x) \mathrm{g}(x)$

</details>

---

### Q29. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int\left(\dfrac{x+2}{x+4}\right)^2 \cdot e^x d x=$

**Options:**

- **(A)** $\mathrm{e}^x\left(\dfrac{x}{x+4}\right)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\mathrm{e}^x\left(\dfrac{x+2}{x+4}\right)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\mathrm{e}^x\left(\dfrac{x-2}{x+4}\right)+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\mathrm{e}^x\left(\dfrac{2 x}{x+4}\right)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^x\left(\dfrac{x}{x+4}\right)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \left(\dfrac{x+2}{x+4}\right)^2 e^x dx$

Expanding the numerator:

$I = \int \dfrac{x^2+4x+4}{(x+4)^2} e^x dx$

Rearranging the terms in the numerator to split the fraction:

$I = \int \dfrac{x(x+4)+4}{(x+4)^2} e^x dx$

$I = \int \left( \dfrac{x}{x+4} + \dfrac{4}{(x+4)^2} \right) e^x dx$

Let $f(x) = \dfrac{x}{x+4}$. Differentiating with respect to $x$ gives:

$f'(x) = \dfrac{(x+4)(1) - x(1)}{(x+4)^2} = \dfrac{4}{(x+4)^2}$

The integral is now in the standard form $\int e^x (f(x) + f'(x)) dx = e^x f(x) + c$.

Substituting $f(x)$ into the formula:

$I = e^x \left( \dfrac{x}{x+4} \right) + c$

Answer: $\mathrm{e}^x\left(\dfrac{x}{x+4}\right)+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q30. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \log (1+x)^{1+x} \mathrm{~d} x=$

**Options:**

- **(A)** $(1+x)^2 \log (1+x)-\dfrac{1}{2}+\mathrm{c}$; where c is a constant of integration.
- **(B)** $\dfrac{(1+x)^2}{2} \cdot \log (1+x)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\dfrac{(1+x)^2}{2}\left[\log (1+x)-\dfrac{1}{2}\right]+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\dfrac{1+x}{2} \log (1+x)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{(1+x)^2}{2}\left[\log (1+x)-\dfrac{1}{2}\right]+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $I = \int \log (1+x)^{1+x} \mathrm{~d} x$

Using the property of logarithms, $\log a^b = b \log a$, we can rewrite the integral as:

$I = \int (1+x) \log (1+x) \mathrm{~d} x$

Let $1+x = t$, which gives $\mathrm{d}x = \mathrm{d}t$. Substituting this into the integral:

$I = \int t \log t \mathrm{~d} t$

Using integration by parts, let $u = \log t$ and $\mathrm{d}v = t \mathrm{~d}t$. Then $\mathrm{d}u = \dfrac{1}{t} \mathrm{~d}t$ and $v = \dfrac{t^2}{2}$.

$I = u v - \int v \mathrm{~d}u$

$I = \left(\log t\right) \left(\dfrac{t^2}{2}\right) - \int \left(\dfrac{t^2}{2}\right) \left(\dfrac{1}{t}\right) \mathrm{~d} t$

$I = \dfrac{t^2}{2} \log t - \dfrac{1}{2} \int t \mathrm{~d} t$

$I = \dfrac{t^2}{2} \log t - \dfrac{t^2}{4} + \mathrm{c}$

$I = \dfrac{t^2}{2} \left[ \log t - \dfrac{1}{2} \right] + \mathrm{c}$

Substituting back $t = 1+x$:

$I = \dfrac{(1+x)^2}{2} \left[ \log (1+x) - \dfrac{1}{2} \right] + \mathrm{c}$

Answer: $\dfrac{(1+x)^2}{2}\left[\log (1+x)-\dfrac{1}{2}\right]+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q31. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{x^2}{\sqrt{1-x}} \mathrm{~d} x=\mathrm{p} \sqrt{1-x}\left(3 x^2+4 x+8\right)+\mathrm{c}$ where $\mathrm{c}$ is a constant of integration, then the value of $\mathrm{p}$ is

**Options:**

- **(A)** $\frac{-2}{15}$
- **(B)** $\frac{2}{15}$
- **(C)** $\frac{4}{15}$
- **(D)** $\frac{-4}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-2}{15}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \mathrm{I}=\int \frac{x^2}{\sqrt{1-x}} \mathrm{~d} x \\ & \text { Put } 1-x=\mathrm{t} \\ & \Rightarrow \mathrm{d} x=-\mathrm{dt} \\ & \therefore \quad \mathrm{I}=\int \frac{(1-\mathrm{t})^2}{\sqrt{\mathrm{t}}} \cdot(-\mathrm{dt}) \\ & =-\int \frac{1-2 \mathrm{t}+\mathrm{t}^2}{\mathrm{t}^{\frac{1}{2}}} \mathrm{dt} \\ & =-\int\left(t^{-\frac{1}{2}}-2 t^{\frac{1}{2}}+t^{\frac{3}{2}}\right) d t \\ & =-\left(2 t^{\frac{1}{2}}-\frac{4}{3} t^{\frac{3}{2}}+\frac{2}{5} t^{\frac{5}{2}}\right)+c \\ & =t^{\frac{1}{2}}\left(\frac{-30+20 t-6 t^2}{15}\right)+c \\ & \end{aligned}$
$\begin{aligned} & =\sqrt{1-x}\left(\frac{-30+20(1-x)-6(1-x)^2}{15}\right)+\mathrm{c} \\ & =\sqrt{1-x}\left(\frac{-6 x^2-8 x-16}{15}\right)+\mathrm{c} \\ & =-\frac{2}{15} \sqrt{1-x}\left(3 x^2+4 x+8\right)+\mathrm{c} \\ \therefore \quad \mathrm{p} & =\frac{-2}{15}\end{aligned}$

</details>

---

### Q32. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \mathrm{e}^x\left(\frac{x^2+4 x+4}{(x+4)^2}\right) \mathrm{d} x$ is

**Options:**

- **(A)** $\mathrm{e}^x\left(\frac{x}{x+4}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\mathrm{e}^x\left(\frac{4}{x+4}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\mathrm{e}^x\left(\frac{x}{(x+4)^2}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\mathrm{e}^x\left(\frac{4}{(x+4)^2}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^x\left(\frac{x}{x+4}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{aligned} & \int \mathrm{e}^x\left[\frac{x^2+4 x+4}{(x+4)^2}\right] \mathrm{d} x \\ & =\int \mathrm{e}^x\left[\frac{x(x+4)+4}{(x+4)^2}\right] \mathrm{d} x \\ & =\int \mathrm{e}^x\left[\frac{x}{x+4}+\frac{4}{(x+4)^2}\right] \mathrm{d} x\end{aligned}$
$\begin{aligned}=\mathrm{e}^x\left(\frac{x}{x+4}\right)+\mathrm{c} & \\ & \cdots\left[\because \int \mathrm{e}^x\left[\mathrm{f}(x)+\mathrm{f}^{\prime}(x)\right] \mathrm{d} x=\mathrm{e}^x \mathrm{f}(x)+\mathrm{c}\right]\end{aligned}$

</details>

---

### Q33. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{x^3 \mathrm{~d} x}{\sqrt{1+x^2}}=\mathrm{a}\left(1+x^2\right) \sqrt{1+x^2}+\mathrm{b} \sqrt{1+x^2}+\mathrm{c}$ (where $\mathrm{c}$ is a constant of integration), then the value of $3 \mathrm{ab}$ is

**Options:**

- **(A)** $-3$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-1$**

**Detailed Solution:**

$\begin{aligned} & \text { Put } 1+x^2=\mathrm{t}^2 \\ & \Rightarrow 2 x \mathrm{~d} x=2 \mathrm{t} \mathrm{dt} \\ & \Rightarrow x \mathrm{~d} x=\mathrm{t} d \mathrm{t} \\ & \quad \int \frac{x^3 \mathrm{~d} x}{\sqrt{1+x^2}} \\ & =\int \frac{\mathrm{t}^2-1}{\mathrm{t}} \cdot \mathrm{t} d \mathrm{t} \\ & =\int\left(\mathrm{t}^2-1\right) \mathrm{dt} \\ & =\frac{\mathrm{t}^3}{3}-\mathrm{t}+\mathrm{c} \\ & =\frac{\left(1+x^2\right)^{\frac{3}{2}}}{3}-\sqrt{1+x^2}+\mathrm{c} \\ & =\frac{1}{3}\left(1+x^2\right) \sqrt{1+x^2}-\sqrt{1+x^2}+\mathrm{c}\end{aligned}$
$\begin{aligned} \therefore \quad & a=\frac{1}{3}, b=-1 \\ & \Rightarrow 3 a b=-1\end{aligned}$

</details>

---

### Q34. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{x-3}{(x-1)^3} \mathrm{e}^x \mathrm{~d} x=$

**Options:**

- **(A)** $\mathrm{e}^x\left(\frac{1}{(x-1)^2}\right)+\mathrm{c}$, where $\mathrm{c}$ is constant of integration,
- **(B)** $\mathrm{e}^x\left(\frac{1}{x+1}\right)+\mathrm{c}$, where $\mathrm{c}$ is constant of integration.
- **(C)** $\mathrm{e}^x\left((x-1)^2\right)+\mathrm{c}$, where $\mathrm{c}$ is constant of integration.
- **(D)** $\mathrm{e}^x\left((x-1)^3\right)+\mathrm{c}$, where $\mathrm{c}$ is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^x\left(\frac{1}{(x-1)^2}\right)+\mathrm{c}$, where $\mathrm{c}$ is constant of integration,**

**Detailed Solution:**

$\int \frac{x-3}{(x-1)^3} e^x d x$
$\begin{aligned} & =\int\left[\frac{x-1}{(x-1)^3}-\frac{2}{(x-1)^3}\right] \mathrm{e}^x \mathrm{~d} x \\ & =\int \mathrm{e}^x\left[\frac{1}{(x-1)^2}-\frac{2}{(x-1)^3}\right] \mathrm{d} x \\ & =\mathrm{e}^x\left(\frac{1}{(x-1)^2}\right)+\mathrm{c}\end{aligned}$
$\ldots\left[\because \int \mathrm{e}^x\left[\mathrm{f}(x)+\mathrm{f}^{\prime}(x)\right] \mathrm{d} x=\mathrm{e}^x \mathrm{f}(x)+\mathrm{c}\right]$

</details>

---

### Q35. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\int \frac{\sqrt{1-x^2}}{x^4} \mathrm{~d} x=\mathrm{A}(x)\left(\sqrt{1-x^2}\right)^{\mathrm{m}}+\mathrm{c}$ for a suitable chosen integer $\mathrm{m}$ and a function $\mathrm{A}(x)$, where $\mathrm{c}$ is a constant of integration, then $(\mathrm{A}(x))^{\mathrm{m}}$ equals

**Options:**

- **(A)** $\frac{1}{9 x^4}$
- **(B)** $\frac{-1}{3 x^3}$
- **(C)** $\frac{-1}{27 x^9}$
- **(D)** $\frac{1}{27 x^6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-1}{27 x^9}$**

**Detailed Solution:**

$$
\text { Let } \begin{aligned}
\mathrm{I} & =\int \frac{\sqrt{1-x^2}}{x^4} \mathrm{~d} x \\
& =\int \frac{x \sqrt{\frac{1}{x^2}-1}}{x^4} \mathrm{~d} x \\
& =\int \frac{\sqrt{\frac{1}{x^2}-1}}{x^3} \mathrm{~d} x
\end{aligned}
$$

Let $\frac{1}{x^2}-1=\mathrm{t}$
$$
\begin{aligned}
\therefore \quad \frac{-2}{x^3} & \mathrm{~d} x=\mathrm{dt} \Rightarrow \frac{1}{x^3} \mathrm{~d} x=\frac{-\mathrm{dt}}{2} \\
\therefore \quad \mathrm{I} & =-\frac{1}{2} \int \sqrt{\mathrm{t}} \mathrm{dt} \\
& =\frac{-1}{2} \times \frac{(\mathrm{t})^{\frac{3}{2}}}{\frac{3}{2}}+\mathrm{c} \\
& =\frac{-1}{3} \times\left(\frac{1}{x^2}-1\right)^{\frac{3}{2}}+\mathrm{c} \\
& =\frac{-1}{3} \times \frac{\left(1-x^2\right)^{\frac{3}{2}}}{\left(x^2\right)^{\frac{3}{2}}}+\mathrm{c} \\
& =\frac{-1}{3} \times \frac{\left(\sqrt{1-x^2}\right)^3}{x^3}
\end{aligned}
$$

Comparing with $\mathrm{A}(x)\left(\sqrt{1-x^2}\right)^{\mathrm{m}}+\mathrm{c}$, we get
$$
\begin{gathered}
\mathrm{A}(x)=\frac{-1}{3 x^3} \text { and } \mathrm{m}=3 \\
\therefore \quad(\mathrm{A}(x))^{\mathrm{m}}=\left(\frac{-1}{3 x^3}\right)^3=\frac{-1}{27 x^9}
\end{gathered}
$$

</details>

---

### Q36. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{I}=\int \sin (\log (x)) \mathrm{d} x$, then $\mathrm{I}$ is given by

**Options:**

- **(A)** $-\frac{x}{2}(\sin (\log x)-\cos (\log x))+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\frac{x}{2}(\sin (\log x)-\cos (\log x))+\mathrm{c}, \text { where } \mathrm{c}$
is a constant of integration.
- **(C)** $\frac{x}{2}(\sin (\log x)+\cos (\log x))+\mathrm{c}$, where $\mathrm{c}$ is a constant of 'integration.
- **(D)** $-\frac{x}{2}(\sin (\log x)+\cos (\log x))+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x}{2}(\sin (\log x)-\cos (\log x))+\mathrm{c}, \text { where } \mathrm{c}$
is a constant of integration.**

**Detailed Solution:**

Let $\log x=\mathrm{t} \Rightarrow x=\mathrm{e}^{\mathrm{t}}$ Differentiating w.r.t. t, we get $\mathrm{d} x=\mathrm{e}^{\mathrm{t}} \mathrm{dt}$
$\begin{aligned}
\therefore \quad \mathrm{I} & =\int \sin (\mathrm{t}) \mathrm{e}^{\mathrm{t}} \mathrm{dt} \\
& =\sin \mathrm{t} \mathrm{e}^{\mathrm{t}}-\int \cos \mathrm{t} \mathrm{e}^{\mathrm{t}} \mathrm{dt} \\
& =\sin \mathrm{t} \mathrm{e}^{\mathrm{t}}-\left[\cos \mathrm{t} \mathrm{e}^{\mathrm{t}}+\int \sin \mathrm{t} \mathrm{e}^{\mathrm{t}} \mathrm{dt}\right] \\
& =\sin \mathrm{t} \mathrm{e}^{\mathrm{t}}-\cos \mathrm{t} \mathrm{e}^{\mathrm{t}}-\mathrm{I}
\end{aligned}$
$\begin{array}{ll}\therefore & 2 \mathrm{I}=x \sin (\log x)-x \cos (\log x)+\mathrm{c} \\ \therefore \quad & \mathrm{I}=\frac{x}{2}(\sin (\log x)-\cos (\log x))+\mathrm{c}\end{array}$

</details>

---

### Q37. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \sec ^{-1} x d x=$

**Options:**

- **(A)** $x \sec ^{-1} x+\log \left|x+\sqrt{x^2-1}\right|+c$
- **(B)** $x \sec ^{-1} x-\log \left|x+\sqrt{x^2-1}\right|+c$
- **(C)** $x \sec ^{-1} x-\log \left|x+\sqrt{x^2+1}\right|+c$
- **(D)** $x \sec ^{-1} x+\log \left|x+\sqrt{x^2+1}\right|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x \sec ^{-1} x-\log \left|x+\sqrt{x^2-1}\right|+c$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } I=\int \sec ^{-1} x d x=\int \sec ^{-1} x \cdot d x \\ & =\left(x \sec ^{-1} x\right)-\int \frac{x}{x \sqrt{x^2-1}} d x \\ & =\left(x \sec ^{-1} x\right)-\log \left|x+\sqrt{x^2-1}\right|+C\end{aligned}$

</details>

---

### Q38. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \cos ^{-1} x d x=$

**Options:**

- **(A)** $x \cos ^{-1} x+\sqrt{1-x^2}+c$
- **(B)** $-x \cos ^{-1} x+\sqrt{1+x^2}+c$
- **(C)** $x \cos ^{-1} x-\sqrt{1+x^2}+c$
- **(D)** $x \cos ^{-1} x-\sqrt{1-x^2}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \cos ^{-1} x-\sqrt{1-x^2}+c$**

**Detailed Solution:**

Let $I=\int \cos ^{-1} x d x=\int\left(\cos ^{-1} x\right) \cdot(1) d x$
$$
=x \cos ^{-1} x-\int \frac{-x}{\sqrt{1-x^2}} d x=x \cos ^{-1} x-\frac{1}{2} \int \frac{-2 x}{\sqrt{1-x^2}} d x
$$
Put $\sqrt{1-\mathrm{x}^2}=\mathrm{t} \Rightarrow \frac{(1)(-2 \mathrm{x})}{2 \sqrt{1-\mathrm{x}^2}} \mathrm{dx}=\mathrm{dt}$
$$
=x \cos ^{-1} x-\int d t=x \cos ^{-1} x-t=x \cos ^{-1} x-\sqrt{1-x^2}+c
$$

</details>

---

### Q39. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \operatorname{cosec}(x-a) \operatorname{cosec} x d x=$

**Options:**

- **(A)** $\operatorname{cosec} a \cdot \log [\sin (x-a)
\operatorname{cosec} x]+c$
- **(B)** $\operatorname{cosec} a \log [\sin (x-a)
\sin x]+c$
- **(C)** $\sin a \log [\sin (\mathrm{x}-\mathrm{a}) \sin \mathrm{x}]+\mathrm{c}$
- **(D)** $\operatorname{cosec} \mathrm{a} \cdot \log [\operatorname{cosec}(\mathrm{x}-\mathrm{a}) \sin \mathrm{x}]+\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\operatorname{cosec} a \cdot \log [\sin (x-a)
\operatorname{cosec} x]+c$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } I=\int \operatorname{cosec}(x-a) \operatorname{cosec} x d x \\ & =\int \frac{d x}{\sin (x-a) \sin x} \quad=\int \frac{\sin a}{\sin a \sin (x-a) \sin x} d x \\ & =\frac{1}{\sin a} \int \frac{\sin (a+x-x)}{\sin (x-a) \sin x} d x=\frac{1}{\sin a} \int \frac{\sin -[x-a-x)}{\sin (x-a) \sin x} d x \\ & =\frac{1}{\sin a} \int \frac{\sin -[(x-a)-(x)]}{\sin (x-a) \sin x} d x=\frac{-1}{\sin a} \int \frac{\sin [(x-a)-x]}{\sin (x-a) \sin x} d x \\ & =\frac{-1}{\sin a} \int \frac{\sin (x-a) \cos x-\cos (x-a) \sin x]}{\sin (x-a) \sin x} d x\end{aligned}$
$\begin{aligned} & \left.=\frac{-1}{\sin a} \int[\cot x-\cot (x-a)] d x=\frac{-1}{\sin a} \int \cot x d x-\cot (x-a)\right] d x \\ & =\frac{-1}{\sin a}[\log |\sin x|-\log \mid \sin (x-a \mid]+c \\ & =\frac{1}{\sin a}[\log |\sin (x-a)|-\log \mid \sin x]+c \\ & =(\operatorname{cosec} a)\left[\log \left|\frac{\sin (x-a)}{\sin x}\right|\right]+c \\ & =\operatorname{cosec} a \cdot \log \mid \sin (x-a) \cdot \operatorname{cosec} x\end{aligned}$

</details>

---

### Q40. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int e^{x} \cdot \sec x(1+\tan x) d x=$

**Options:**

- **(A)** $e^{x} \operatorname{cosec} x+c$
- **(B)** $e^{x} \sec x+c$
- **(C)** $e^{x} \cot x+c$
- **(D)** $e^{x} \tan x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e^{x} \sec x+c$**

**Detailed Solution:**

$\int e^{x} \sec x(1+\tan x) d x$
$=\int e^{x}(\sec x+\sec x \tan x)=e^{x} \sec x+c$

</details>

---

### Q41. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int(1+x) \log x \mathrm{~d} x=$

**Options:**

- **(A)** $\left(x+\frac{x^{2}}{2}\right) \log x+\left(x-\frac{x^{2}}{4}\right)+C$
- **(B)** $\left(x+\frac{x^{2}}{2}\right) \log x-\left(x+\frac{x^{2}}{4}\right)+C$
- **(C)** $\left(x+\frac{x^{2}}{2}\right) \log x-\left(x-\frac{x^{2}}{4}\right)+C$
- **(D)** $\left(x+\frac{x^{2}}{2}\right) \log x+\left(x+\frac{x^{2}}{4}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(x+\frac{x^{2}}{2}\right) \log x-\left(x+\frac{x^{2}}{4}\right)+C$**

**Detailed Solution:**

Let $I=\int(1+x) \log x d x$
Put $\quad \log x=t \quad \Rightarrow x=e^{t} \Rightarrow d x=e^{t} d t$
$$
\begin{aligned}
\therefore I &=\int\left(1+e^{t}\right) t \cdot e^{t} d t=\int\left(t e^{t}+t e^{2 t}\right) d t \\
&=\int t e^{t} d t+\int t e^{2 t} d t=\left[t e^{t}-\int e^{t} d t\right]+\left[t \frac{e^{2 t}}{2}-\int \frac{e^{2 t}}{2} d t\right] \\
&=t e^{t}-e^{t}+t \frac{e^{2 t}}{2}-\frac{e^{2 t}}{4}+C=x \log x-x+\frac{1}{2}(\log x) \cdot x^{2}-\frac{x^{2}}{4}+C \\
&=\left(x+\frac{x^{2}}{2}\right) \log x-\left(x+\frac{x^{2}}{4}\right)+C
\end{aligned}
$$

</details>

---

### Q42. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \log x \cdot(\log x+2) d x=$

**Options:**

- **(A)** $e^{x}(\log x)^{2}+c$
- **(B)** $(\log x)^{2}+c$
- **(C)** $x(\log x)^{2}+c$
- **(D)** $x \log x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x(\log x)^{2}+c$**

**Detailed Solution:**

(A)
Let $\mathrm{I}=\int \log \mathrm{x} \cdot(\log \mathrm{x}+2) \mathrm{dx}$
Put $\quad \log \mathrm{x}=t \Rightarrow \frac{1}{\mathrm{x}} \mathrm{dx}=\mathrm{dt} \Rightarrow \mathrm{dx}=\mathrm{e}^{t} \mathrm{dt}$
$\therefore \begin{aligned} \mathrm{I} &=\int \mathrm{e}^{\mathrm{t}}[\mathrm{t}(\mathrm{t}+2)] \mathrm{dt} \\ &=\int \mathrm{e}^{t}\left(\mathrm{t}^{2}+2 \mathrm{t}\right) \mathrm{dt}=\mathrm{e}^{t}\left(\mathrm{t}^{2}\right)+\mathrm{c} \\ &=\mathrm{x}[\log \mathrm{x}]^{2}+\mathrm{c} \end{aligned}$

</details>

---

### Q43. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int \sin ^{-1} x d x=$

**Options:**

- **(A)** $x \sin ^{-1} x+\sqrt{1-x^{2}}+c$
- **(B)** $x \sin ^{-1} x-\sqrt{1-x^{2}}+c$
- **(C)** $x \sin ^{-1} x-\sqrt{1+x^{2}}+c$
- **(D)** $x \sin ^{-1} x+\sqrt{1+x^{2}}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x \sin ^{-1} x+\sqrt{1-x^{2}}+c$**

**Detailed Solution:**

(A)
Let $\begin{aligned} I &=\int \sin ^{-1} x d x=\int\left(\sin ^{-1} x\right) \cdot 1 \cdot d x \\ &=\sin ^{-1} x \int 1 d x-\int\left(\frac{d}{d x} \sin ^{-1} x \cdot \int 1 d x\right) d x \end{aligned}$
$=x \cdot \sin ^{-1} x-\int \frac{x}{\sqrt{1-x^{2}}} d x$...(1)
Consider, $\int \frac{x}{\sqrt{1-x^{2}}} d x$
Now, put $1-x^{2}=t \Rightarrow-2 x d x=d t$
$\therefore \int \frac{x}{\sqrt{1-x^{2}}} d x=\int \frac{-1}{2} \times \frac{1}{\sqrt{t}} d t=\frac{-1}{2} \frac{t^{\frac{1}{2}}}{\frac{1}{2}}=-\sqrt{t}$
Substituting in $(1)$, we get:
$I=x \cdot \sin ^{-1} x-.-\sqrt{1-x^{2}}-c=x \cdot \sin ^{-1} x+\sqrt{1-x^{2}}+c$

</details>

---

### Q44. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int\left[\frac{\log x-1}{1+(\log x)^{2}}\right]^{2} d x=$

**Options:**

- **(A)** $\frac{x}{(1+\log x)}+c$
- **(B)** $\frac{x}{1+(\log x)^{2}}+c$
- **(C)** $\frac{x^{2}}{1+(\log x)^{2}}+c$
- **(D)** $\frac{1}{1+(\log x)^{2}}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x}{1+(\log x)^{2}}+c$**

**Detailed Solution:**

(B)

</details>

---

### Q45. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \cot x \cdot \log [\log (\sin x)] d x=$

**Options:**

- **(A)** $\log (\sin x)[\log (\sin x))+1]+c$
- **(B)** $\log (\sin x)[\log (\log (\sin x))+1]+c$
- **(C)** $\log (\sin x)[\log (\log (\sin x))-1]+c$
- **(D)** $\log (\sin x)[\log (\sin x)-1]+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log (\sin x)[\log (\log (\sin x))-1]+c$**

**Detailed Solution:**

(D)
Let $I=\int \cot x \cdot \log [\log (\sin x)] d x$
Put $\begin{aligned} \log (\sin x) &=t \Rightarrow \frac{\cos x}{\sin x} d x=d t \Rightarrow \cot x d x=d t \\ \therefore I &=\int \log t d t=\int \log t \cdot 1 d t \\ &=\log t \int 1 d t-\int\left[\frac{d}{d t}(\log t) \cdot \int 1 d t\right] d t \\ &=(\log t) \cdot t-\int \frac{1}{t} \cdot t d t=t \cdot \log t-\int 1 d t \\ &=t \cdot \log t-t+c=t(\log t-1)+c \\ &=\log (\sin x)[\log (\log (\sin x))-1]+c \end{aligned}$

</details>

---

### Q46. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int e^{\tan ^{-1} x}\left(1+\frac{x}{1+x^{2}}\right) d x$

**Options:**

- **(A)** $\left(\frac{x}{2}\right) e^{\tan ^{-1} x}+c$
- **(B)** $x e^{\tan ^{-1} x}+c$
- **(C)** $\left(\frac{1}{2}\right) e^{\tan ^{-1} x}+c$
- **(D)** $e^{\tan ^{-1} x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x e^{\tan ^{-1} x}+c$**

**Detailed Solution:**

Let $I=\int e^{\tan ^{-1} x}\left(1+\frac{x}{1+x^{2}}\right) d x$
$\begin{aligned} I &=\int e^{\tan ^{-1} x}\left(\frac{1+x^{2}+x}{1+x^{2}}\right) d x \\ \text { Put } \tan ^{-1} x &=t \Rightarrow x=\tan t \text { and } \frac{1}{1+x^{2}} d x=d t \\ \therefore I &=\int e^{t}\left(1+\tan ^{2} t+\tan t\right) d t \Rightarrow \int e^{t}\left(\tan t+\sec ^{2} t\right) d t \\ &=e^{t} \tan t+c=x e^{\tan ^{-1} x}+c \end{aligned}$

</details>

---

### Q47. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\int \frac{e^{x}}{\sqrt{x}}(1+2 x) d x=$

**Options:**

- **(A)** $\frac{1}{\sqrt{x}} e^{x}+c$
- **(B)** $2 \sqrt{x} e^{x}+c$
- **(C)** $\frac{\sqrt{x}}{2} e^{x}+c$
- **(D)** $\sqrt{x} e^{x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sqrt{x} e^{x}+c$**

**Detailed Solution:**

$\begin{aligned} I &=\int \frac{e^{x}}{\sqrt{x}}(1+2 x) d x \\ &=\int e^{x}\left(\frac{1}{\sqrt{x}}+2 \sqrt{x}\right) d x=\int e^{x}\left(2 \sqrt{x}+\frac{1}{\sqrt{x}}\right) d x=2 \int e^{x}\left(\sqrt{x}+\frac{1}{2 \sqrt{x}}\right) d x \\ &=2 e^{x} \sqrt{x}+c \end{aligned}$

</details>

---

### Q48. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int x^{3} \cdot e^{x^{2}} d x=$

**Options:**

- **(A)** $\frac{1}{2} e^{x^{2}}\left(x^{2}+1\right)+c$
- **(B)** $\frac{1}{2} e^{x^{2}}\left(x^{2}-1\right)+c$
- **(C)** $\frac{1}{2} e^{x}\left(x^{2}-1\right)+c$
- **(D)** $\frac{1}{2} e^{x}\left(x^{2}+1\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2} e^{x^{2}}\left(x^{2}-1\right)+c$**

**Detailed Solution:**

Let $I=\int x^{3} e^{x^{2}} d x$
Put $x^{2}=t \Rightarrow 2 x d x=d t \Rightarrow x d x=\frac{1}{2} d t$
$\therefore \mathrm{I}=\frac{1}{2} \int \mathrm{te}^{\mathrm{t}} \mathrm{dt}$
$=\frac{1}{2}\left[t e^{t}-e^{t}\right]+c=\frac{1}{2} e^{t}(t-1)+c=\frac{1}{2} e^{x^{2}}\left(x^{2}-1\right)+c$

</details>

---

### Q49. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `3`

The value of $\int e^{x}\left[\frac{1+\sin x}{1+\cos x}\right] d x$ is

**Options:**

- **(A)** $\frac{1}{2} e^{x} \sec \frac{x}{2}+C$
- **(B)** $e^{x} \sec \frac{x}{2}+C$
- **(C)** $\frac{1}{2} e^{x} \tan \frac{x}{2}+C$
- **(D)** $e^{x} \tan \frac{x}{2}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $e^{x} \tan \frac{x}{2}+C$**

**Detailed Solution:**

Let $I=\int e^{x}\left[\frac{1+\sin x}{1+\cos x}\right] d x$
$\begin{aligned}=& \int\left\{\frac{e^{x}}{(1+\cos x)}+\frac{e^{x} \sin x}{(1+\cos x)}\right\} d x \\=& \int \frac{e^{x}}{2 \cos ^{2} \frac{x}{2}} d x+\int \frac{e^{x} \cdot 2 \sin \frac{x}{2} \cdot \cos \frac{x}{2}}{2 \cos ^{2} \frac{x}{2}} \cdot d x \\=& \frac{1}{2} \int e^{x} \cdot \sec ^{2} \frac{x}{2} \cdot d x+\int \underset{\mathbb{I}}{e^{x} \tan } \frac{x}{2} \cdot d x \\=& \frac{1}{2} \int e^{x} \cdot \sec ^{2} \frac{x}{2} \cdot d x \\+\left\{\tan \frac{x}{2} \cdot e^{x}-\int \frac{1}{2} \cdot \sec ^{2} \frac{x}{2} \cdot e^{x} d x\right\} \end{aligned}$
(using integral by parts)
$=\frac{1}{2} \int e^{x} \cdot \sec ^{2} \frac{x}{2} d x+e^{x} \cdot \tan \frac{x}{2}-\frac{1}{2}$
$\int e^{x} \cdot \sec ^{2} \frac{x}{2} \cdot d x$
$=e^{x} \cdot \tan \frac{x}{2}+C$

</details>

---

### Q50. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \cos (\log x) d x$ is

**Options:**

- **(A)** $\frac{1}{2}[\sin (\log x)+\cos (\log x)]+C$
- **(B)** $\frac{x}{2}[\sin (\log x)+\cos (\log x)]+C$
- **(C)** $\frac{x}{2}[\sin (\log x)-\cos (\log x)]+C$
- **(D)** $\frac{1}{2}[\sin (\log x)-\cos (\log x)]+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x}{2}[\sin (\log x)+\cos (\log x)]+C$**

**Detailed Solution:**

Let $I=\int \cos (\log x) \cdot 1 d x...(i)$
Use integral by parts, $\begin{aligned} I=& \cos (\log x) \cdot x-\int[-\sin (\log x)] \cdot \frac{1}{x} \cdot x d x \\=& x \cdot \cos (\log x)+\int \sin (\log x) \cdot 1 d x \\=& x \cdot \cos (\log x)+[\sin (\log x) \cdot x\\ \left.\quad-\int \cos (\log x) \cdot \frac{1}{x} \cdot x d x\right]+C \\=& x \cdot \cos (\log x)+[x \sin (\log x)\\ \left.-\int \cos (\log x) d x\right]+C \\=& x\{\sin (\log x)+\cos (\log x)\}-I+C \\ \quad[\text { from Eq. (i) }] \\ \Rightarrow \quad & I=\frac{x}{2}\{\sin (\log x)+\cos (\log x)\}+C \end{aligned}$

</details>

---

### Q51. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{x^{2}}{(x \sin x+\cos x)^{2}} d x$ is equal to

**Options:**

- **(A)** $\frac{\sin x+\cos x}{x \sin x+\cos x}+C$
- **(B)** $\frac{x \sin x-\cos x}{x \sin x+\cos x}+C$
- **(C)** $\frac{\sin x-x \cos x}{x \sin x+\cos x}+C$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\sin x-x \cos x}{x \sin x+\cos x}+C$**

**Detailed Solution:**

Since, $\frac{d}{d x}(x \sin x+\cos x)=x \cos x$
$\therefore \quad I=\int \frac{x^{2} d x}{(x \sin x+\cos x)^{2}}$
$\quad=\int \frac{x}{\cos x} \cdot \frac{x \cos x}{(x \sin x+\cos x)^{2}} d x$
$$
\begin{array}{l}
=\frac{x}{\cos x} \cdot\left(\frac{-1}{x \sin x+\cos x}\right) \\
-\int \frac{\cos x-x(-\sin x)}{\cos ^{2} x} \cdot \frac{-1}{(x \sin x+\cos x)} d x \\
=\frac{-x}{\cos x(x \sin x+\cos x)}+\int \sec ^{2} d x \\
=\frac{-x}{\cos x(x \sin x+\cos x)}+\tan x+C \\
=\frac{-x+\sin x(x \sin x+\cos x)}{\cos x(x \sin x+\cos x)}+C \\
=\frac{-x \cos ^{2} x+\sin x \cdot \cos x}{\cos x(x \sin x+\cos x)}+C \\
=\left(\frac{\sin x-x \cos x}{\cos x+x \sin x}\right)+C
\end{array}
$$

</details>

---

### Q52. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

$\int x \log x d x$ is equal to

**Options:**

- **(A)** $\frac{x^{2}}{4}(2 \log x-1)+c$
- **(B)** $\frac{x^{2}}{2}(2 \log x-1)+c$
- **(C)** $\frac{x^{2}}{4}(2 \log x+1)+c$
- **(D)** $\frac{x^{2}}{2}(2 \log x+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{x^{2}}{4}(2 \log x-1)+c$**

**Detailed Solution:**

$\begin{aligned} \int \frac{x}{\Pi} \log _{I} x d x &=\log x \cdot \frac{x^{2}}{2}-\int \frac{1}{x} \cdot \frac{x^{2}}{2} d x \\ &=\frac{x^{2}}{2} \log x-\frac{1}{2} \frac{x^{2}}{2}+c \\ &=\frac{x^{2}}{4}(2 \log x-1)+c \end{aligned}$

</details>

---

### Q53. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

$\int e^{x} \frac{(x-1)}{x^{2}} d x$ is equal to

**Options:**

- **(A)** $\frac{e^{x}}{x^{2}}+c$
- **(B)** $\frac{-e^{x}}{x^{2}}+c$
- **(C)** $\frac{e^{x}}{x}+c$
- **(D)** $\frac{-e^{x}}{x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{e^{x}}{x}+c$**

**Detailed Solution:**

$\int e^{x}\left(\frac{x-1}{x^{2}}\right) d x$
$\quad=\int e^{x}\left(\frac{1}{x}-\frac{1}{x^{2}}\right) d x$
$=\frac{e^{x}}{x}+c\left[\because \int e^{x}\left[f(x)+f^{\prime}(x)\right] d x=e^{x} f(x)+c\right]$

</details>

---

