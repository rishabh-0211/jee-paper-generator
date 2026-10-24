# JEE Main Mathematics - Determinants

## Topic 1: Expansion of Determinants

**Total Questions:** 53

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $f: \mathbf{N} \rightarrow \mathbf{Z}$ is defined by
$f(n) = \begin{vmatrix} n & -1 & -5 \\ -2n^2 & 3(2k+1) & 2k+1 \\ -3n^3 & 3k(2k+1) & 3k(k+2)+1 \end{vmatrix}$, $k \in \mathbf{N}$,
and $\sum_{n=1}^{k} f(n) = 98$, then $k$ is equal to :

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $5$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3$**

**Detailed Solution:**

Let $S = \displaystyle\sum_{n=1}^{k} f(n)$, where
$f(n) = \begin{vmatrix} n & -1 & -5 \\ -2n^2 & 3(2k+1) & 2k+1 \\ -3n^3 & 3k(2k+1) & 3k(k+2)+1 \end{vmatrix}$

Since only the first column depends on $n$, the summation can be taken inside that column:
$S = \begin{vmatrix} \displaystyle\sum_{n=1}^{k} n & -1 & -5 \\ \displaystyle\sum_{n=1}^{k} (-2n^2) & 3(2k+1) & 2k+1 \\ \displaystyle\sum_{n=1}^{k} (-3n^3) & 3k(2k+1) & 3k(k+2)+1 \end{vmatrix}$

Using standard summation formulas:
$\displaystyle\sum_{n=1}^{k} n = \dfrac{k(k+1)}{2}$
$\displaystyle\sum_{n=1}^{k} (-2n^2) = -\dfrac{k(k+1)(2k+1)}{3}$
$\displaystyle\sum_{n=1}^{k} (-3n^3) = -\dfrac{3k^2(k+1)^2}{4}$

Substituting:
$S = \begin{vmatrix} \dfrac{k(k+1)}{2} & -1 & -5 \\ -\dfrac{k(k+1)(2k+1)}{3} & 3(2k+1) & 2k+1 \\ -\dfrac{3k^2(k+1)^2}{4} & 3k(2k+1) & 3k^2+6k+1 \end{vmatrix}$

Taking $\dfrac{k(k+1)}{12}$ common from $C_1$:
$S = \dfrac{k(k+1)}{12} \begin{vmatrix} 6 & -1 & -5 \\ -4(2k+1) & 3(2k+1) & 2k+1 \\ -9k(k+1) & 3k(2k+1) & 3k^2+6k+1 \end{vmatrix}$

Applying $C_1 \to C_1 + C_2 + C_3$:
Row 1: $6 - 1 - 5 = 0$
Row 2: $-8k - 4 + 6k + 3 + 2k + 1 = 0$
Row 3: $-9k^2 - 9k + 6k^2 + 3k + 3k^2 + 6k + 1 = 1$

$S = \dfrac{k(k+1)}{12} \begin{vmatrix} 0 & -1 & -5 \\ 0 & 3(2k+1) & 2k+1 \\ 1 & 3k(2k+1) & 3k^2+6k+1 \end{vmatrix}$

Expanding along $C_1$:
$S = \dfrac{k(k+1)}{12} \cdot 1 \cdot \begin{vmatrix} -1 & -5 \\ 3(2k+1) & 2k+1 \end{vmatrix}$

$S = \dfrac{k(k+1)}{12}\left[(-1)(2k+1) - (-5)(3(2k+1))\right]$

$S = \dfrac{k(k+1)}{12}\left[-(2k+1) + 15(2k+1)\right]$

$S = \dfrac{k(k+1)}{12} \cdot 14(2k+1) = 7 \cdot \dfrac{k(k+1)(2k+1)}{6}$

Note that $\dfrac{k(k+1)(2k+1)}{6} = \displaystyle\sum_{n=1}^{k} n^2$.

Given $S = 98$:
$7 \cdot \dfrac{k(k+1)(2k+1)}{6} = 98$

$\dfrac{k(k+1)(2k+1)}{6} = 14$

Checking integer values of $k$:
$k = 1$: sum $= 1$
$k = 2$: sum $= 5$
$k = 3$: sum $= 14$

Hence, $k = 3$, and the correct option is $(1)\ 3$.

</details>

---

### Q2. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Among the statements : 
 I: If $\left|\begin{array}{ccc}1 & \cos \alpha & \cos \beta \\ \cos \alpha & 1 & \cos \gamma \\ \cos \beta & \cos \gamma & 1\end{array}\right|=\left|\begin{array}{ccc}0 & \cos \alpha & \cos \beta \\ \cos \alpha & 0 & \cos \gamma \\ \cos \beta & \cos \gamma & 0\end{array}\right|$, then $\cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=\frac{3}{2}$, and 
 II : If $\left|\begin{array}{ccc}x^{2}+x & x+1 & x-2 \\ 2 x^{2}+3 x-1 & 3 x & 3 x-3 \\ x^{2}+2 x+3 & 2 x-1 & 2 x-1\end{array}\right|=\mathrm{p} x+\mathrm{q}$, then $\mathrm{p}^{2}=196 \mathrm{q}^{2}$,

**Options:**

- **(A)** only II is true
- **(B)** both are false
- **(C)** both are true
- **(D)** only I is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) both are false**

**Detailed Solution:**

Statement I: Let $D_1 = \begin{vmatrix} 1 & \cos\alpha & \cos\beta \\ \cos\alpha & 1 & \cos\gamma \\ \cos\beta & \cos\gamma & 1 \end{vmatrix} = 1 - \cos^2\alpha - \cos^2\beta - \cos^2\gamma + 2\cos\alpha\cos\beta\cos\gamma$.
$D_2 = \begin{vmatrix} 0 & \cos\alpha & \cos\beta \\ \cos\alpha & 0 & \cos\gamma \\ \cos\beta & \cos\gamma & 0 \end{vmatrix} = 2\cos\alpha\cos\beta\cos\gamma$.
$D_1 = D_2 \Rightarrow 1 - \cos^2\alpha - \cos^2\beta - \cos^2\gamma = 0 \Rightarrow \cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1 \neq \frac{3}{2}$. Statement I is false.
Statement II: Evaluate by substituting $x = 0$: determinant $= -12$, so $q = -12$.
At $x = 1$: determinant $= 12$, so $p + q = 12 \Rightarrow p = 24$.
$p^2 = 576$ and $196q^2 = 196 \times 144 = 28224$. Since $p^2 \neq 196q^2$, Statement II is false.
Both statements are false.

</details>

---

### Q3. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let M and m respectively be the maximum and the minimum values of
\(f(x)=\left|\begin{array}{ccc}
1+\sin ^2 x & \cos ^2 x & 4 \sin 4 x \\
\sin ^2 x & 1+\cos ^2 x & 4 \sin 4 x \\
\sin ^2 x & \cos ^2 x & 1+4 \sin 4 x
\end{array}\right|, x \in \mathrm{R}\)
Then \(M^4-m^4\) is equal to :

**Options:**

- **(A)** 1280
- **(B)** 1295
- **(C)** 1215
- **(D)** 1040

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1280**

**Detailed Solution:**

$\begin{aligned}
& \left|\begin{array}{ccc}
1+\sin ^2 x & \cos ^2 x & 4 \sin 4 x \\
\sin ^2 x & 1+\cos ^2 x & 4 \sin 4 x \\
\sin ^2 x & \cos ^2 x & 1+4 \sin 4 x
\end{array}\right|, x \in R \\
& R_2 \rightarrow R_2-R_1 \& R_3 \rightarrow R_3 \rightarrow R_1 \\
& f(x)\left|\begin{array}{ccc}
1+\sin ^2 x & \cos ^2 x & 4 \sin 4 x \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right|
\end{aligned}$

Expand about $\mathrm{R}_1$, use get
$f(x)=2+4 \sin 4 x$
$\therefore \mathrm{M}=$ max value of $\mathrm{f}(\mathrm{x})=6$
$m=\min$ value of $f(x)=-2$
$\therefore \mathrm{m}^4-\mathrm{M}^4=1280$

</details>

---

### Q4. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For some $\mathrm{a}, \mathrm{b}$, let $f(x)=\left|\begin{array}{ccc}\mathrm{a}+\frac{\sin x}{x} & 1 & \mathrm{~b} \\ \mathrm{a} & 1+\frac{\sin x}{x} & \mathrm{~b} \\ \mathrm{a} & 1 & \mathrm{~b}+\frac{\sin x}{x}\end{array}\right|, x \neq 0, \lim _{x \rightarrow 0} f(x)=\lambda+\mu \mathrm{a}+\nu \mathrm{b}$. Then $(\lambda+\mu+\nu)^2$ is equal to :

**Options:**

- **(A)** 16
- **(B)** 25
- **(C)** 9
- **(D)** 36

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 16**

**Detailed Solution:**

$\lim _{x \rightarrow 0}\left|\begin{array}{ccc}
a+\frac{\sin x}{x} & 1 & b \\
a & 1+\frac{\sin x}{x} & b \\
a & 1 & b+\frac{\sin x}{x}
\end{array}\right|=\lambda+\mu a+v b$
At $\lim x \rightarrow 0$,
$\begin{aligned}
& f(x)=\left|\begin{array}{ccc}
a+1 & 1 & b \\
a & 1+1 & b \\
a & 1 & b+1
\end{array}\right|=\lambda+\mu a+v b \\
& R_1 \rightarrow R_1-R_2 \\
& R_2 \rightarrow R_2-R_3 \\
& \left|\begin{array}{ccc}
1 & -1 & 0 \\
0 & 1 & -1 \\
a & 1 & b+1
\end{array}\right|=\lambda+\mu a+v b \\
& \mathrm{C}_2 \rightarrow \mathrm{C}_1-\mathrm{C}_2 \\
& \left|\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & -1 \\
a & a+1 & b+1
\end{array}\right|=\lambda+\mu a+v b \\
& a+b+2=\lambda+\mu a+v b \\
& \lambda=2, \mu=1, \quad v=1 \\
& (\lambda+\mu+v)=(2+1+1)^2=16
\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha \neq \mathrm{a}, \beta \neq \mathrm{b}, \gamma \neq \mathrm{c}$ and $\left|\begin{array}{lll}\alpha & \mathrm{b} & \mathrm{c} \\ \mathrm{a} & \beta & \mathrm{c} \\ \mathrm{a} & \mathrm{b} & \gamma\end{array}\right|=0$, then $\frac{\mathrm{a}}{\alpha-\mathrm{a}}+\frac{\mathrm{b}}{\beta-\mathrm{b}}+\frac{\gamma}{\gamma-\mathrm{c}}$ is equal to:

**Options:**

- **(A)** 3
- **(B)** 0
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

$\begin{aligned} & \mathrm{R}_1 \rightarrow \mathrm{R}_1-\mathrm{R}_2, \mathrm{R}_2 \rightarrow \mathrm{R}_2-\mathrm{R}_3 \\ & \left|\begin{array}{ccc}\alpha-\mathrm{a} & \mathrm{b}-\beta & 0 \\ 0 & \beta-\mathrm{b} & \mathrm{c}-\gamma \\ \mathrm{a} & \mathrm{b} & \gamma\end{array}\right|=0 \\ & (\alpha-\mathrm{a})(\gamma(\beta-\mathrm{b})-\mathrm{b}(\mathrm{c}-\gamma))-(\mathrm{b}-\beta)(-\mathrm{a}(\mathrm{c}-\gamma))=0 \\ & \gamma(\alpha-\mathrm{a})(\beta-\mathrm{b})-\mathrm{b}(\alpha-\mathrm{a})(\mathrm{c}-\gamma)+\mathrm{a}(\mathrm{b}-\beta)(\mathrm{c}-\gamma) \\ & \frac{\gamma}{\gamma-\mathrm{c}}+\frac{\mathrm{b}}{\beta-\mathrm{b}}+\frac{\mathrm{a}}{\alpha-\mathrm{a}}=0\end{aligned}$

</details>

---

### Q6. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For $\alpha, \beta \in \mathbb{R}$ and a natural number $n$, let $A_r=\left|\begin{array}{ccc}r & 1 & \frac{n^2}{2}+\alpha \\ 2 r & 2 & n^2-\beta \\ 3 r-2 & 3 & \frac{n(3 n-1)}{2}\end{array}\right|$. Then $2A_{10} - 2A_8$ is

**Options:**

- **(A)** 0
- **(B)** $4 \alpha+2 \beta$
- **(C)** $2 \alpha+4 \beta$
- **(D)** $2 n$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 \alpha+2 \beta$**

**Detailed Solution:**

$A_r=\left|\begin{array}{ccc}r & 1 & \frac{n^2}{2}+\alpha \\ 2 r & 2 & n^2-\beta \\ 3 r-2 & 3 & \frac{n(3 n-1)}{2}\end{array}\right|$
$2 \mathrm{~A}_{10}-\mathrm{A}_8=\left|\begin{array}{ccc}20 & 1 & \frac{\mathrm{n}^2}{2}+\alpha \\ 40 & 2 & \mathrm{n}^2-\beta \\ 56 & 3 & \frac{\mathrm{n}(3 \mathrm{n}-1)}{2}\end{array}\right|-\left|\begin{array}{ccc}8 & 1 & \frac{\mathrm{n}^2}{2}+\alpha \\ 16 & 2 & \mathrm{n}^2-\beta \\ 22 & 3 & \frac{\mathrm{n}(3 \mathrm{n}-1)}{2}\end{array}\right|$
$\begin{aligned} & \Rightarrow\left|\begin{array}{ccc}12 & 1 & \frac{n^2}{2}+\alpha \\ 24 & 2 & n^2-\beta \\ 34 & 3 & \frac{n(3 n-1)}{2}\end{array}\right| \\ & \Rightarrow\left|\begin{array}{ccc}0 & 1 & \frac{n^2}{2}+\alpha \\ 0 & 2 & n^2-\beta \\ -2 & 3 & \frac{n(3 n-1)}{2}\end{array}\right| \\ & \Rightarrow-2\left(\left(n^2-\beta\right)-\left(n^2+2 \alpha\right)\right) \\ & \Rightarrow-2(-\beta-2 \alpha) \Rightarrow 4 \alpha+2 \beta\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math>, for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mi>α</mi><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd><mtd><mi>α</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mn>2</mn><mi>α</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>3</mn><mi>α</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math>, lie in the interval</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>0</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>0</mn><mo>)</mo></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mi mathvariant="normal">α</mi><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd><mtd><mi mathvariant="normal">α</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mn>2</mn><mi mathvariant="normal">α</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>3</mn><mi mathvariant="normal">α</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Applying, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>→</mo><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mfrac><mn>7</mn><mn>6</mn></mfrac></mtd><mtd><mfrac><mn>7</mn><mn>6</mn></mfrac></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd><mtd><mi mathvariant="normal">α</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mn>2</mn><mi mathvariant="normal">α</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>3</mn><mi mathvariant="normal">α</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Applying, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub><mo>→</mo><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mfrac><mn>7</mn><mn>6</mn></mfrac></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi mathvariant="normal">α</mi></mtd><mtd><mi mathvariant="normal">α</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mtd></mtr><mtr><mtd><mn>2</mn><mi mathvariant="normal">α</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>3</mn><mi mathvariant="normal">α</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>-</mo><mn>0</mn><mo>+</mo><mfrac><mn>7</mn><mn>6</mn></mfrac><mfenced><mrow><mn>3</mn><mi mathvariant="normal">α</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi mathvariant="normal">α</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi mathvariant="normal">α</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mi mathvariant="normal">α</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi mathvariant="normal">α</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>6</mn><mo>±</mo><msqrt><mn>36</mn><mo>-</mo><mn>4</mn><mfenced><mn>2</mn></mfenced><mfenced><mn>1</mn></mfenced></msqrt></mrow><mrow><mn>2</mn><mo>×</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>6</mn><mo>±</mo><mn>2</mn><msqrt><mn>7</mn></msqrt></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mo>±</mo><msqrt><mn>7</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>≈</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mo>±</mo><mn>2</mn><mo>.</mo><mn>6</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>≈</mo><mfrac><mrow><mo>-</mo><mn>0</mn><mo>.</mo><mn>4</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mo> </mo><mfrac><mrow><mo>-</mo><mn>5</mn><mo>.</mo><mn>6</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>≈</mo><mo>-</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>,</mo><mo> </mo><mo>-</mo><mn>2</mn><mo>.</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>∈</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p>

</details>

---

### Q8. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>&#955;</mi></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>x</mi></mtd><mtd><mi>x</mi><mo>+</mo><msup><mi>&#955;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>9</mn><mn>8</mn></mfrac><mfenced><mrow><mn>103</mn><mi>x</mi><mo>+</mo><mn>81</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mfrac><mi>&#955;</mi><mn>3</mn></mfrac></math> are the roots of the equation

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>24</mn><mi>x</mi><mo>-</mo><mn>27</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>x</mi><mo>-</mo><mn>27</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>27</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>27</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>27</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>&#955;</mi></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>x</mi></mtd><mtd><mi>x</mi><mo>+</mo><msup><mi>&#955;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>9</mn><mn>8</mn></mfrac><mfenced><mrow><mn>103</mn><mi>x</mi><mo>+</mo><mn>81</mn></mrow></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><msup><mi>&#955;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>9</mn><mn>8</mn></mfrac><mfenced><mrow><mn>103</mn><mfenced><mn>0</mn></mfenced><mo>+</mo><mn>81</mn></mrow></mfenced></math></p><p>On expanding the determinant we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>9</mn><mn>8</mn></mfrac><mo>&#215;</mo><mn>81</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>3</mn></msup><mo>=</mo><mfrac><msup><mn>9</mn><mn>3</mn></msup><msup><mn>2</mn><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#955;</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>6</mn></mfrac></math></p><p>Now the required quadratic equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>9</mn><mn>6</mn></mfrac></mrow></mfenced><mi>x</mi><mo>+</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>9</mn><mn>6</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mn>6</mn></mfenced><mi>x</mi><mo>+</mo><mfrac><mn>27</mn><mn>4</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>27</mn><mo>=</mo><mn>0</mn></math></p><p>Hence, the required quadratic equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>27</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q9. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> be a root of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mi>x</mi><mo>+</mo><mfenced><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math> are distinct real numbers such that the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced></math> is singular. Then the value of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mn>2</mn></msup><mrow><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup></mstyle><mrow><mfenced><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mstyle displaystyle="true"><mfenced><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced></mstyle></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup></mstyle><mrow><mfenced><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mstyle displaystyle="true"><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mstyle></mrow></mfrac></math> is</p><p> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>It is given that the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced></math> is singular, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mfenced><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>-</mo><mi>&#945;</mi><mfenced><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Above equation holds true if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn></math>. Now, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mn>2</mn></msup><mrow><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup></mstyle><mrow><mfenced><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mstyle displaystyle="true"><mfenced><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced></mstyle></mrow></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup></mstyle><mrow><mfenced><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mstyle displaystyle="true"><mfenced><mrow><mi>b</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow></mfenced><mn>3</mn></msup></mrow><mrow><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mfenced><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mfenced><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mfenced><mrow><mi>c</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup><mo>+</mo><msup><mi>z</mi><mn>3</mn></msup><mo>=</mo><mn>3</mn><mi>x</mi><mi>y</mi><mi>z</mi><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></mrow></mfenced></math></p>

</details>

---

### Q10. JEE Main 2022 (29 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mn>2</mn></math> be prime numbers and let
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mi>p</mi><mo>!</mo></mtd><mtd><mfenced><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>p</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mtd></mtr><mtr><mtd><mfenced><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>p</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>p</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mtd></mtr><mtr><mtd><mfenced><mrow><mi>p</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>p</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>p</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>!</mo></mtd></mtr></mtable></mfenced></math>
Then the sum of the maximum values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mi>&#945;</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>p</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>&#946;</mi></msup></math> divide <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi></math>, is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>P</mi><mo>!</mo></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mtd></mtr><mtr><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mtd></mtr><mtr><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>!</mo></mtd></mtr></mtable></mfenced></math></p><p>Now using the factorial concept and taking common terms we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#916;</mi><mo>=</mo><mi>P</mi><mo>!</mo><mfenced><mrow><mi>P</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>P</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>P</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>P</mi><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p>Now on solving determinant we get,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>P</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>P</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>P</mi><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p>Using operation <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>1</mn></msub><mo>-</mo><msub><mi>C</mi><mn>2</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>P</mi><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><mi>P</mi><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn><mi>P</mi><mo>-</mo><mn>6</mn></mtd><mtd><mfenced><mrow><mi>P</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>P</mi><mo>+</mo><mn>6</mn><mo>-</mo><mfenced><mrow><mn>2</mn><mi>P</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now putting the value of determinant we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#916;</mi><mo>=</mo><mn>2</mn><mi>P</mi><mo>!</mo><mfenced><mrow><mi>P</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#916;</mi><mo>=</mo><mn>2</mn><msup><mi>P</mi><mn>3</mn></msup><mfenced><mrow><mi>P</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mfenced><mrow><mi>P</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>P</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></math></p><p>Which is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>&#945;</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>P</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>&#946;</mi></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn></math></p></blockquote>

</details>

---

### Q11. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi></msub><mo>=</mo><mi>cos</mi><mfrac><mrow><mn>2</mn><mi mathvariant="normal">r</mi><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>2</mn><mi mathvariant="normal">r</mi><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>,</mo><mi mathvariant="normal">r</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math>, then the determinant <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>4</mn></msub></mtd><mtd><msub><mi>a</mi><mn>5</mn></msub></mtd><mtd><msub><mi>a</mi><mn>6</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>7</mn></msub></mtd><mtd><msub><mi>a</mi><mn>8</mn></msub></mtd><mtd><msub><mi>a</mi><mn>9</mn></msub></mtd></mtr></mtable></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>9</mn></msub></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>9</mn></msub><mo>-</mo><msub><mi>a</mi><mn>3</mn></msub><msub><mi>a</mi><mn>7</mn></msub></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>5</mn></msub></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><msub><mi>a</mi><mn>6</mn></msub><mo>-</mo><msub><mi>a</mi><mn>4</mn></msub><msub><mi>a</mi><mn>8</mn></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>9</mn></msub><mo>-</mo><msub><mi>a</mi><mn>3</mn></msub><msub><mi>a</mi><mn>7</mn></msub></math>**

**Detailed Solution:**

<p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi></msub><mo>=</mo><mi>cos</mi><mfrac><mrow><mn>2</mn><mi mathvariant="normal">r</mi><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>+</mo><mi>i</mi><mi>sin</mi><mfrac><mrow><mn>2</mn><mi mathvariant="normal">r</mi><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>,</mo><mi mathvariant="normal">r</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>r</mi></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>2</mn><mi>r</mi><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup><mo>-</mo><mo>-</mo><mo>-</mo><mo>-</mo><mo>(</mo><mi>I</mi><mo>)</mo></math></p><p>From Euler form <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>i</mi><mi>&#952;</mi></mrow></msup><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>cos</mi><mi>&#952;</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>i</mi><mo>&#160;</mo><mi>sin</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>4</mn></msub></mtd><mtd><msub><mi>a</mi><mn>5</mn></msub></mtd><mtd><msub><mi>a</mi><mn>6</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>7</mn></msub></mtd><mtd><msub><mi>a</mi><mn>8</mn></msub></mtd><mtd><msub><mi>a</mi><mn>9</mn></msub></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>6</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd></mtr><mtr><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>8</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mi>i</mi><mn>10</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>12</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd></mtr><mtr><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>14</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mi>i</mi><mn>16</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>18</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd></mtr></mtable></mfenced></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup><mo>,</mo><mo>&#160;</mo><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>8</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup><mo>,</mo><mo>&#160;</mo><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>14</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></math> common form each row</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mi>i</mi><mfenced><mrow><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>+</mo><mfrac><mrow><mn>14</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></mfenced></mrow></msup><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd><mtd><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>4</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup></mtd></mtr></mtable></mfenced></math></p><p>We know that If two rows are identical the value of determinant will be equal to zero.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>-</mo><mo>-</mo><mo>-</mo><mo>(</mo><mi>I</mi><mi>I</mi><mo>)</mo></math></p><p>Now From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><msup><mi>e</mi><mrow><mi>i</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mrow></msup><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>9</mn></msub><mo>=</mo><msup><mi>e</mi><mrow><mi>i</mi><mo>(</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>9</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>)</mo></mrow></msup><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><msup><mi>e</mi><mrow><mi>i</mi><mo>(</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>)</mo></mrow></msup><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>a</mi><mn>7</mn></msub><mo>=</mo><msup><mi>e</mi><mrow><mi>i</mi><mo>(</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>7</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac><mo>)</mo></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><msub><mi mathvariant="normal">a</mi><mn>9</mn></msub><mo>-</mo><msub><mi mathvariant="normal">a</mi><mn>3</mn></msub><msub><mi mathvariant="normal">a</mi><mn>7</mn></msub><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mi mathvariant="normal">i</mi><mfenced><mfrac><mrow><mn>20</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mfenced></mrow></msup><mo>-</mo><msup><mi mathvariant="normal">e</mi><mrow><mi mathvariant="normal">i</mi><mfenced><mfrac><mrow><mn>20</mn><mi>&#960;</mi></mrow><mn>9</mn></mfrac></mfenced></mrow></msup><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>-</mo><mo>-</mo><mo>-</mo><mo>-</mo><mo>(</mo><mi>I</mi><mi>I</mi><mi>I</mi><mo>)</mo></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mi>I</mi><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mi>I</mi><mi>I</mi><mi>I</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd><mtd><msub><mi>a</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>4</mn></msub></mtd><mtd><msub><mi>a</mi><mn>5</mn></msub></mtd><mtd><msub><mi>a</mi><mn>6</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>7</mn></msub></mtd><mtd><msub><mi>a</mi><mn>8</mn></msub></mtd><mtd><msub><mi>a</mi><mn>9</mn></msub></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>9</mn></msub><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><msub><mi>a</mi><mn>7</mn></msub></math></p><p> </p>

</details>

---

### Q12. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>]</mo></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>[</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>]</mo></mtd></mtr><mtr><mtd><mo>[</mo><mi>x</mi><mo>]</mo></mtd><mtd><mo>&#160;</mo><mo>[</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>]</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>]</mo></mtd></mtr><mtr><mtd><mo>[</mo><mi>x</mi><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>]</mo></mtd><mtd><mo>&#160;</mo><mo>[</mo><mi>x</mi><mo>+</mo><mn>4</mn><mo>]</mo></mtd></mtr></mtable></mfenced><mtable><mtr></mtr><mtr></mtr><mtr></mtr></mtable></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>det</mo><mo>(</mo><mi>A</mi><mo>)</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>192</mn></math>, then the set of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is in the interval:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>62</mn><mo>,</mo><mn>63</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>65</mn><mo>,</mo><mn>66</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>60</mn><mo>,</mo><mn>61</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>68</mn><mo>,</mo><mn>69</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>62</mn><mo>,</mo><mn>63</mn><mo>)</mo></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable columnalign="center center center" columnspacing="1em" rowspacing="4pt"><mtr><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>]</mo></mtd></mtr><mtr><mtd><mo>[</mo><mi>x</mi><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>]</mo></mtd></mtr><mtr><mtd><mo>[</mo><mi>x</mi><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>+</mo><mn>4</mn><mo>]</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable columnalign="center center center" columnspacing="1em" rowspacing="4pt"><mtr><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>1</mn></mtd><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>2</mn></mtd><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>[</mo><mi>x</mi><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>3</mn></mtd><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>[</mo><mi>x</mi><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>2</mn></mtd><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo stretchy="false">&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>&#8722;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>,</mo><msub><mi>R</mi><mn>2</mn></msub><mo stretchy="false">&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>&#8722;</mo><msub><mi>R</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable columnalign="center center center" columnspacing="1em" rowspacing="4pt"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>&#8722;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>&#8722;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>[</mo><mi>x</mi><mo>]</mo></mtd><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>2</mn></mtd><mtd><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>det</mi><mo>&#8289;</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>(</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>4</mn><mo>+</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>2</mn><mo>)</mo><mo>&#8722;</mo><mn>1</mn><mo>(</mo><mo>&#8722;</mo><mo>[</mo><mi>x</mi><mo>]</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>6</mn></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>de</mi><mi>t</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>192</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>192</mn><mo>=</mo><mn>3</mn><mo>[</mo><mi>x</mi><mo>]</mo><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>[</mo><mi>x</mi><mo>]</mo><mo>=</mo><mn>186</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>]</mo><mo>=</mo><mn>62</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>62</mn><mo>,</mo><mn>63</mn><mo>)</mo></math></p>

</details>

---

### Q13. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mo>-</mo><mn>2</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced><mo>.</mo></math> Then the maximum value of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mo>-</mo><mn>2</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mfenced><mtable columnalign="left"><mtr><mtd><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><mo>&#38;</mo><mo>&#160;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mn>4</mn><mi>cos</mi><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi></math></p><p>We know, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>&#8804;</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><msub><mfenced><mi>x</mi></mfenced><mi>max</mi></msub><mo>=</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q14. JEE Main 2021 (20 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi></math> be in arithmetic progression with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>-</mo><mi>c</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>a</mi></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>+</mo><mi>c</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>b</mi></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mi>b</mi><mo>+</mo><mi>d</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>d</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn></math>, then value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#955;</mi><mn>2</mn></msup></math> is equal to________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>d</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>, therefore</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>-</mo><mi>a</mi><mo>=</mo><mi>c</mi><mo>-</mo><mi>b</mi><mo>=</mo><mi>d</mi><mo>-</mo><mi>c</mi><mo>=</mo><mi>&#955;</mi></math></p><p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi><mo>-</mo><mi>c</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>a</mi></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>+</mo><mi>c</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>b</mi></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mi>b</mi><mo>+</mo><mi>d</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>d</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mtd><mtd><mi>&#955;</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>a</mi></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mn>1</mn></mtd><mtd><mi>&#955;</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>b</mi></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi></mtd><mtd><mi>&#955;</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>c</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;&#160;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mtd><mtd><mi>&#955;</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>a</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>b</mi><mo>-</mo><mi>a</mi></mtd></mtr><mtr><mtd><mn>4</mn><mi>&#955;</mi></mtd><mtd><mn>0</mn></mtd><mtd><mi>c</mi><mo>-</mo><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mfenced open="|" close="|"><mtable><mtr><mtd><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">a</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>&#955;</mi></mtd></mtr><mtr><mtd><mn>4</mn><mi>&#955;</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn><mi>&#955;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>&#955;</mi><mfenced><mrow><mn>4</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><msup><mi>&#955;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#955;</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q15. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></math> are in arithmetic progression with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>3</mn><mi>d</mi><mo>,</mo></math> and the determinant of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn><msqrt><mn>2</mn></msqrt></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>5</mn><msqrt><mn>2</mn></msqrt></mtd><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mi>k</mi></mtd><mtd><mi>z</mi></mtd></mtr></mtable></mfenced></math> is zero, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></math> are in arithmetic progression, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>z</mi><mo>,</mo></math> also <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn><msqrt><mn>2</mn></msqrt></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>5</mn><msqrt><mn>2</mn></msqrt></mtd><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mi>k</mi></mtd><mtd><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><mn>2</mn><msub><mi>R</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn><msqrt><mn>2</mn></msqrt></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>k</mi><mo>-</mo><mn>6</mn><msqrt><mn>2</mn></msqrt></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mi>k</mi></mtd><mtd><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>6</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>(</mo><mn>3</mn><mi>z</mi><mo>-</mo><mn>5</mn><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>k</mi><mo>-</mo><mn>6</mn><msqrt><mn>2</mn></msqrt><mo>)</mo><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mi>z</mi><mo>-</mo><mn>5</mn><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>z</mi><mo>-</mo><mn>5</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>d</mi><mo>)</mo><mo>-</mo><mn>5</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>3</mn><mi>d</mi></math> (Not possible)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>6</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>72</mn><mo>.</mo></math></p>

</details>

---

### Q16. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>7</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msub><mi>C</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></math></p><p>Expanding w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><menclose notation="right"><mi>f</mi><mfenced><mi>x</mi></mfenced></menclose><mi>max</mi></msub><mo>=</mo><msqrt><mn>1</mn><mo>+</mo><mn>4</mn></msqrt><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p>

</details>

---

### Q17. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mtd><mtd><mi>a</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mtd><mtd><mi>a</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>a</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mtd><mtd><mi>a</mi><mo>+</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mtd><mtd><mi>a</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>a</mi><mo>+</mo><mn>3</mn><mo>-</mo><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>a</mi><mo>+</mo><mn>12</mn><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>a</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>a</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn><mi>a</mi><mo>+</mo><mn>10</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>4</mn><mo>&#160;</mo><mi>a</mi><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>a</mi><mo>+</mo><mn>8</mn><mo>-</mo><mn>4</mn><mi>a</mi><mo>-</mo><mn>10</mn><mo>=</mo><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q18. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let m and M be respectively the minimum and maximum value values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></math> Then the ordered pair (m, M) is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><mn>2</mn><msub><mi>R</mi><mn>3</mn></msub><mtext>&#160;and&#160;</mtext><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><mn>2</mn><msub><mi>R</mi><mn>3</mn></msub></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mo>-</mo><mo>(</mo><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>)</mo></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mo>-</mo><mo>(</mo><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>)</mo></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>D</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>-</mo><mi>sin</mi><mn>2</mn><mi>x</mi></math></p><p>As range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, thus</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mi>M</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q19. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>x</mi><mo>=</mo><mi>b</mi><mo>+</mo><mi>y</mi><mo>=</mo><mi>c</mi><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi></math> are non-zero distinct real numbers, then<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd><mtd><mi>a</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>x</mi><mo>+</mo><mi>a</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd><mtd><mi>b</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>y</mi><mo>+</mo><mi>b</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd><mtd><mi>c</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>z</mi><mo>+</mo><mi>c</mi></mtd></mtr></mtable></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>b</mi><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mi>a</mi><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#160;</mo><mo>(</mo><mi>a</mi><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>a</mi><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mi>c</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#160;</mo><mo>(</mo><mi>a</mi><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>a</mi><mo>=</mo><mi>y</mi><mo>+</mo><mi>b</mi><mo>=</mo><mi>z</mi><mo>+</mo><mi>c</mi><mo>+</mo><mn>1</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd><mtd><mi>a</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>a</mi><mo>+</mo><mi>x</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd><mtd><mi>b</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>b</mi><mo>+</mo><mi>y</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd><mtd><mi>c</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>c</mi><mo>+</mo><mi>z</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd><mtd><mi>a</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd><mtd><mi>b</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd><mtd><mi>c</mi><mo>+</mo><mi>y</mi></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mfenced><mrow><msub><mi>C</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>3</mn></msub><mo>-</mo><msub><mi>C</mi><mn>1</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced><mfenced><mrow><msub><mi>C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><msub><mi>C</mi><mn>3</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>y</mi><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>y</mi><mo>-</mo><mi>x</mi></mtd><mtd><mn>0</mn></mtd><mtd><mi>b</mi><mo>-</mo><mi>a</mi></mtd></mtr><mtr><mtd><mi>z</mi><mo>-</mo><mi>x</mi></mtd><mtd><mn>0</mn></mtd><mtd><mi>c</mi><mo>-</mo><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mi>y</mi><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>a</mi><mo>-</mo><mi>b</mi></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mo>(</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>)</mo></mtd></mtr><mtr><mtd><mi>z</mi><mo>-</mo><mi>x</mi></mtd><mtd><mn>0</mn></mtd><mtd><mi>c</mi><mo>-</mo><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mi>y</mi><mo>(</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>)</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>z</mi><mo>-</mo><mi>x</mi></mtd><mtd><mn>0</mn></mtd><mtd><mi>c</mi><mo>-</mo><mi>a</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mi>y</mi><mo>(</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>)</mo><mo>(</mo><mi>c</mi><mo>-</mo><mi>a</mi><mo>+</mo><mi>z</mi><mo>-</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>y</mi><mo>(</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>)</mo></math></p>

</details>

---

### Q20. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the minimum and the maximum values of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>&#8594;</mo><mi>R</mi><mo>,</mo></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mo>-</mo><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mo>-</mo><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>12</mn></mtd><mtd><mn>10</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>respectively, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">m</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">M</mi><mo>)</mo></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>-</mo><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>12</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>4</mn><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#8722;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mfenced><mrow><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p>Again, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>&#8804;</mo><mi>&#952;</mi><mo>&#8804;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#8658;</mo><mn>2</mn><mfenced><mfrac><mstyle displaystyle="true"><mi mathvariant="normal">&#960;</mi></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac></mfenced><mo>&#8804;</mo><mn>2</mn><mi>&#952;</mi><mo>&#8804;</mo><mn>2</mn><mfenced><mfrac><mstyle displaystyle="true"><mi mathvariant="normal">&#960;</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>&#8804;</mo><mi>&#952;</mi><mo>&#8804;</mo><mi>&#960;</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>&#8658;</mo><mn>2</mn><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mi mathvariant="normal">&#960;</mi></mrow></mfenced></math> i.e., Second Quadrant.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#952;</mi></mfenced><msub><mrow></mrow><mi>max</mi></msub><mo>=</mo><mi>M</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><msub><mfenced><mi>&#952;</mi></mfenced><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>&#160;</mo><mo>=</mo><mi>m</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p>

</details>

---

### Q21. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>.</mo></math>
If <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>a</mi></mtd><mtd><mi>x</mi><mo>+</mo><mn>2</mn></mtd><mtd><mi>x</mi><mo>+</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>+</mo><mn>3</mn></mtd><mtd><mi>x</mi><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mi>c</mi></mtd><mtd><mi>x</mi><mo>+</mo><mn>4</mn></mtd><mtd><mi>x</mi><mo>+</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>,</mo></math> then:

**Options:**

- **(A)** <math><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>50</mn></mrow></mfenced><mo>=</mo><mn>501</mn></math>
- **(B)** <math><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>50</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mi>f</mi><mfenced separators="|"><mrow><mn>50</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>501</mn></math>
- **(D)** <math><mi>f</mi><mfenced separators="|"><mrow><mn>50</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>f</mi><mfenced separators="|"><mrow><mn>50</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Apply <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>-</mo><mn>2</mn><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mi>b</mi></mtd><mtd><mi>x</mi><mo>+</mo><mn>3</mn></mtd><mtd><mi>x</mi><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mi>c</mi></mtd><mtd><mi>x</mi><mo>+</mo><mn>4</mn></mtd><mtd><mi>x</mi><mo>+</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>50</mn></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q22. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi><mi>j</mi></mrow></msub></mrow></mfenced></math> <em>and</em> <math><mi mathvariant="normal">B</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><msub><mrow><mi>b</mi></mrow><mrow><mi>i</mi><mi>j</mi></mrow></msub></mrow></mfenced></math> be two <math><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> real matrices such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><msup><mfenced separators="|"><mn>3</mn></mfenced><mfenced separators="|"><mrow><mi>i</mi><mo>+</mo><mi>j</mi><mo>-</mo><mn>2</mn></mrow></mfenced></msup><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></math> , where <math><mi>i</mi><mo>,</mo><mi>j</mi><mo>=</mo><mn>1,2</mn><mo>,</mo><mn>3</mn></math> . If the determinant of <math><mi mathvariant="normal">B</mi></math><span style="display: none;"> </span> is<span style="display: none;"> </span> <math><mn>81</mn></math> <em>,</em><span style="display: none;"> </span><span style="display: none;"> </span><em> </em>then determinant of <math><mi mathvariant="normal">A</mi></math> i<span style="display: none;"> </span><span style="display: none;"> </span>s

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>81</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi mathvariant="normal">B</mi></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><msub><mi>b</mi><mn>11</mn></msub></mtd><mtd><msub><mi>b</mi><mn>12</mn></msub></mtd><mtd><msub><mi>b</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><msub><mi>b</mi><mn>21</mn></msub></mtd><mtd><msub><mi>b</mi><mn>22</mn></msub></mtd><mtd><msub><mi>b</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><msub><mi>b</mi><mn>31</mn></msub></mtd><mtd><msub><mi>b</mi><mn>32</mn></msub></mtd><mtd><msub><mi>b</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><msup><mn>3</mn><mn>0</mn></msup><msub><mi>a</mi><mn>11</mn></msub></mtd><mtd><msup><mn>3</mn><mn>1</mn></msup><msub><mi>a</mi><mn>12</mn></msub></mtd><mtd><msup><mn>3</mn><mn>2</mn></msup><msub><mi>a</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><msup><mn>3</mn><mn>1</mn></msup><msub><mi>a</mi><mn>21</mn></msub></mtd><mtd><msup><mn>3</mn><mn>2</mn></msup><msub><mi>a</mi><mn>22</mn></msub></mtd><mtd><msup><mn>3</mn><mn>3</mn></msup><msub><mi>a</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><msup><mn>3</mn><mn>2</mn></msup><msub><mi>a</mi><mn>31</mn></msub></mtd><mtd><msup><mn>3</mn><mn>3</mn></msup><msub><mi>a</mi><mn>32</mn></msub></mtd><mtd><msup><mn>3</mn><mn>4</mn></msup><msub><mi>a</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>81</mn><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mo>&#8729;</mo><mn>3</mn><mo>&#8729;</mo><msup><mn>3</mn><mn>2</mn></msup><mfenced open="|" close="|" separators="|"><mi mathvariant="normal">A</mi></mfenced><mo>&#8658;</mo><msup><mn>3</mn><mn>4</mn></msup><mo>=</mo><msup><mn>3</mn><mn>6</mn></msup><mfenced open="|" close="|" separators="|"><mi mathvariant="normal">A</mi></mfenced><mo>&#8658;</mo><mfenced open="|" close="|" separators="|"><mi mathvariant="normal">A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q23. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A value of <math><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>,</mo></math> for which <math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mn>4</mn><mtext>&#8201;</mtext><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mn>4</mn><mtext>&#8201;</mtext><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn><mtext>&#8201;</mtext><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>&#952;</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>24</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn><mi>π</mi></mrow><mrow><mn>36</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>18</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>→</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math>  
<math><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mtd><mtd><mn>4</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>θ</mi></mtd></mtr><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>→</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></math>  
<math><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mtd><mtd><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mtd><mtd><mn>1</mn><mo>+</mo><mn>4</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>θ</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mo>⇒</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>4</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>θ</mi></mrow></mfenced><mo>+</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>θ</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>θ</mi><mo>=</mo><mn>0</mn><mo>⇒</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>6</mn><mi>θ</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>  
<math><mn>6</mn><mi>θ</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>⇒</mo><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>9</mn></mrow></mfrac></math>

</details>

---

### Q24. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The sum of the real roots of the equation
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>+</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> is equal to:

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mo>-</mo><mn>4</mn></math>
- **(C)** <math><mn>6</mn></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>0</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>+</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>On expansion, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced open="{" close="}"><mrow><mo>-</mo><mn>3</mn><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced open="{" close="}"><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>4</mn><mi>x</mi><mo>-</mo><mn>9</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced open="{" close="}"><mrow><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced open="{" close="}"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mo>-</mo><mn>5</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>30</mn><mi>x</mi><mo>-</mo><mn>30</mn><mo>+</mo><mn>5</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>35</mn><mi>x</mi><mo>+</mo><mn>30</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>.</mo></math></p><p>Here all roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>3</mn></mrow></mfenced></math> are real, hence the sum of the real roots is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>.</mo></math></p>

</details>

---

### Q25. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><msub><mrow><mi>&#916;</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#952;</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#952;</mi></mtd><mtd><mo>-</mo><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>x</mi></mtd></mtr></mtable></mrow></mfenced></math> and <math><msub><mrow><mi mathvariant="normal">&#916;</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi mathvariant="normal">&#952;</mi></mtd><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi mathvariant="normal">&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi mathvariant="normal">&#952;</mi></mtd><mtd><mo>-</mo><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi mathvariant="normal">&#952;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>x</mi></mtd></mtr></mtable></mrow></mfenced><mo>,</mo></math> <math><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>;</mo></math> then for all <math><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mo>&#8201;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> :

**Options:**

- **(A)** <math><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>-</mo><mn>2</mn><mo>(</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></math>
- **(B)** <math><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi>x</mi><mo>(</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>2</mn><mi mathvariant="normal">θ</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mn>4</mn><mi mathvariant="normal">θ</mi><mo>)</mo></math>
- **(C)** <math><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
- **(D)** <math><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi mathvariant="normal">Δ</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math>**

**Detailed Solution:**

<math><msub><mrow><mi mathvariant="normal">&#916;</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#952;</mi></mtd><mtd><mo>-</mo><mi>x</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable><mtable><mtr><mtd><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>=</mo><mi>x</mi><mfenced separators="|"><mrow><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi mathvariant="normal">&#952;</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#952;</mi><mo>-</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi></mrow></mfenced><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi><mo>(</mo><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#952;</mi><mo>+</mo><mi>x</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">&#952;</mi><mo>)</mo></math>
<math><mo>=</mo><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>+</mo><mi>x</mi><mi>s</mi><mi>i</mi><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi><mo>+</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi><mrow><mrow><mi mathvariant="italic">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow><mo>-</mo><mi>s</mi><mi>i</mi><mi>n</mi><mi>&#952;</mi><mi>c</mi><mi>o</mi><mi>s</mi><mi>&#952;</mi><mo>+</mo><mi>x</mi><mi>c</mi><mi>o</mi><msup><mrow><mi>s</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></math>
<math><mo>=</mo><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>+</mo><mi>x</mi><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi mathvariant="normal">&#952;</mi></mrow></mrow></mrow></mfenced></math>
<math><mo>=</mo><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
Similarly: <math><msub><mrow><mi mathvariant="normal">&#916;</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
<math><mo>&#8756;</mo><msub><mrow><mi mathvariant="normal">&#916;</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi mathvariant="normal">&#916;</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math>

</details>

---

### Q26. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>&#945;</mi><mi>&#160;</mi></math> and <math><mi>&#946;</mi></math> be the roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>.</mo></math> Then for <math><mi>y</mi><mo>&#8800;</mo><mn>0</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>,</mo><mo>&#160;</mo><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>y</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>y</mi><mo>+</mo><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>y</mi><mo>+</mo><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math> is equal to

**Options:**

- **(A)** <math><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
- **(B)** <math><mi>y</mi><mo>(</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>–</mo><mn>1</mn><mo>)</mo></math>
- **(C)** <math><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>–</mo><mn>1</mn></math>
- **(D)** <math><mi> </mi><mi>y</mi><mo>(</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>–</mo><mn>3</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></math>**

**Detailed Solution:**

<p>Roots of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> and we know that the sum of roots of a quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>b</mi><mi>a</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>c</mi><mi>a</mi></mfrac></math> respectively.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>1</mn><mo>.</mo></math></p><p>Now, let <math><mo>&#8710;</mo><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>y</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>y</mi><mo>+</mo><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>y</mi><mo>+</mo><mi>&#945;</mi></mtd></mtr></mtable></mrow></mfenced></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub><mo>+</mo><msub><mi>R</mi><mn>3</mn></msub><mo>,</mo></math> we get</p><p><math><mo>&#8710;</mo><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>y</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mtd><mtd><mi>y</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mtd><mtd><mi>y</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>y</mi><mo>+</mo><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>y</mi><mo>+</mo><mi>&#945;</mi></mtd></mtr></mtable></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>y</mi><mo>+</mo><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>y</mi><mo>+</mo><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mfenced open="[" close="]"><mrow><mn>1</mn><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>y</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced open="{" close="}"><mrow><mi>&#945;</mi><mfenced><mrow><mi>y</mi><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced open="{" close="}"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mfenced><mrow><mi>y</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>y</mi><mfenced open="[" close="]"><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mi>y</mi><mi>&#945;</mi><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mi>y</mi><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>y</mi><mfenced open="[" close="]"><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>&#946;</mi><mo>-</mo><mi>y</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced></mrow></mfenced></math></p><p>On putting the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>y</mi><mfenced open="[" close="]"><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>y</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>y</mi><mfenced><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>y</mi><mfenced open="[" close="]"><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>-</mo><mfenced><mrow><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>y</mi><mfenced open="[" close="]"><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math><mo>=</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></math> (on simplifying)</p>

</details>

---

### Q27. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the numbers <math><mn>2</mn><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi></math> be in an A.P. and <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd></mtr></mtable></mrow></mfenced></math> . If <math><mi mathvariant="normal">d</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">t</mi><mo>(</mo><mi>A</mi><mo>)</mo><mi>&#160;</mi><mo>&#8712;</mo><mo>[</mo><mn>2,16</mn><mo>]</mo><mo>,</mo></math> then <math><mi>c</mi></math> lies in the interval:

**Options:**

- **(A)** <math><mfenced open="[" separators="|"><mrow><mn>2,3</mn></mrow></mfenced></math>
- **(B)** <math><mfenced open="[" close="]" separators="|"><mrow><mn>4,6</mn></mrow></mfenced></math>
- **(C)** <math><mfenced open="[" close="]" separators="|"><mrow><mn>3,2</mn><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></mrow></mfenced></math>
- **(D)** <math><mi> </mi><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup><mo>,</mo><mn>4</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfenced open="[" close="]" separators="|"><mrow><mn>4,6</mn></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><msup><mi>b</mi><mn>2</mn></msup></mtd><mtd><msup><mi>c</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mover><mo>&#8594;</mo><mrow><msub><mi>C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><msub><mi>C</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>C</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>3</mn></msub><mo>-</mo><msub><mi>C</mi><mn>1</mn></msub></mrow></mover><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>b</mi><mo>-</mo><mn>2</mn></mtd><mtd><mi>c</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mtd><mtd><msup><mi>c</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mtd></mtr></mtable></mfenced><mspace linebreak="newline"></mspace><mspace linebreak="newline"></mspace><mo>=</mo><mfenced separators="|"><mrow><mi>b</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>c</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>c</mi><mo>-</mo><mi>b</mi></mrow></mfenced></math>
Let common difference of <math><mi>A</mi><mi>P</mi><mo>=</mo><mi>d</mi></math>
<math><mo>&#8756;</mo><mtext>&#8201;</mtext><mi>b</mi><mo>=</mo><mn>2</mn><mo>+</mo><mi>d</mi><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>c</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>d</mi></math>
<math><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mi>d</mi><mo>&#215;</mo><mn>2</mn><mi>d</mi><mo>&#215;</mo><mi>d</mi><mo>=</mo><mn>2</mn><msup><mrow><mi>d</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>16</mn></mrow></mfenced></math>
<math><mo>&#8658;</mo><msup><mrow><mi>d</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>8</mn></mrow></mfenced><mo>&#8658;</mo><mi>d</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced><mo>&#8658;</mo><mn>2</mn><mi>d</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn></mrow></mfenced></math>
<math><mo>&#8658;</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>d</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>6</mn></mrow></mfenced></math>
<math><mo>&#8756;</mo><mtext>&#8201;</mtext><mi>c</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>6</mn></mrow></mfenced></math>

</details>

---

### Q28. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>sin</mi><mi>&#952;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mtd><mtd><mn>1</mn></mtd><mtd><mi>sin</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>, then for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>det</mi><mfenced separators="|"><mi>A</mi></mfenced></math> lies in the interval :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" separators="|"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" separators="|"><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" separators="|"><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" separators="|"><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

$A=\left[\begin{array}{ccc}1 & \sin \theta & 1 \\ -\sin \theta & 1 & \sin \theta \\ -1 & -\sin \theta & 1\end{array}\right]$
$\Rightarrow \operatorname{det}(A)=\left(11+\sin ^2 \theta\right)-\sin \theta(-\sin \theta+\sin \theta)+1\left(\sin ^2 \theta+1\right)$
$=2+2 \sin ^2 \theta$
$\because \theta \in\left(\frac{3 \pi}{4}, \frac{5 \pi}{4}\right)$
$\therefore \sin 2 \theta \in\left[0, \frac{1}{2}\right]$
$\therefore \operatorname{det}(A) \in[2,3]$ which is a subset of $\left(\frac{3}{2}, 3\right]$

</details>

---

### Q29. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\left|\begin{array}{ccc}a-b-c & 2 a & 2 a \\ 2 b & b-c-a & 2 b \\ 2 c & 2 c & c-a-b\end{array}\right|$

$=(a+b+c)(x+a+b+c)^{2}, x \neq 0$ and $a+b+c \neq 0,$ then $x$

is equal to

**Options:**

- **(A)** abc
- **(B)** $-(a+b+c)$
- **(C)** $2(a+b+c)$
- **(D)** $-2(a+b+c)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-2(a+b+c)$**

**Detailed Solution:**

$\Delta=\left|\begin{array}{ccc}a-b-c & 2 a & 2 a \\ 2 b & b-c-a & 2 b \\ 2 c & 2 c & c-a-b\end{array}\right|$

$R_{1} \rightarrow R_{1}+R_{2}+R$

$\Delta=\left|\begin{array}{ccc}a+b+c & a+b+c & a+b+c \\ 2 b & b-c-a & 2 b \\ 2 c & 2 c & c-a-b\end{array}\right|$

$=(a+b+c)\left|\begin{array}{ccc}1 & 1 & 1 \\ 2 b & b-c-a & 2 b \\ 2 c & 2 c & c-a-b\end{array}\right|$

$\begin{array}{l}

C_{1} \rightarrow C_{1}-C_{y}, C_{2} \rightarrow C_{2}-C_{3} \\

\Delta=(a+b+c)\left|\begin{array}{ccc}

0 & 0 & 1 \\

0 & -b-c-a & 2 b \\

c+a+b & c+a+b & c-a-b

\end{array}\right|

\end{array}$

$=(a+b+c)(a+b+c)^{2}$

Hence, $x=-2(a+b+c)$

</details>

---

### Q30. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8230;</mo><mo>,</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>10</mn></mrow></msub></math> be in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mo>.</mo><mi>P</mi><mo>.</mo><mo>&#160;</mo></math>with <math><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>&#62;</mo><mn>0</mn><mi>&#160;</mi></math> for <math><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mo>&#8230;</mo><mo>,</mo><mi>&#160;</mi><mn>10</mn></math> and <math><mi>S</mi></math> be the set of pairs <math><mfenced separators="|"><mrow><mi>r</mi><mo>,</mo><mi>&#160;</mi><mi>k</mi></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mi>r</mi><mo>,</mo><mi>&#160;</mi><mi>k</mi><mo>&#8712;</mo><mi>N</mi></math> (the set of natural numbers) for which

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>1</mn><mi>r</mi></msubsup><mi>&#160;</mi><msubsup><mi>a</mi><mn>2</mn><mi>k</mi></msubsup></mtd><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>2</mn><mi>r</mi></msubsup><msubsup><mi>a</mi><mn>3</mn><mi>k</mi></msubsup></mtd><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>3</mn><mi>r</mi></msubsup><msubsup><mi>a</mi><mn>4</mn><mi>k</mi></msubsup></mtd></mtr><mtr><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>4</mn><mi>r</mi></msubsup><mi>&#160;</mi><msubsup><mi>a</mi><mn>5</mn><mi>k</mi></msubsup></mtd><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>5</mn><mi>r</mi></msubsup><msubsup><mi>a</mi><mn>6</mn><mi>k</mi></msubsup></mtd><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>6</mn><mi>r</mi></msubsup><msubsup><mi>a</mi><mn>7</mn><mi>k</mi></msubsup></mtd></mtr><mtr><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>7</mn><mi>r</mi></msubsup><msubsup><mi>a</mi><mn>8</mn><mi>k</mi></msubsup></mtd><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>8</mn><mi>r</mi></msubsup><msubsup><mi>a</mi><mn>9</mn><mi>k</mi></msubsup></mtd><mtd><msub><mi>log</mi><mi>e</mi></msub><mo>&#8289;</mo><msubsup><mi>a</mi><mn>9</mn><mi>r</mi></msubsup><msubsup><mi>a</mi><mn>10</mn><mi>k</mi></msubsup></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math>

Then the number of elements in <math><mi>S</mi><mo>,</mo></math> is:

**Options:**

- **(A)** Infinitely many
- **(B)** <math><mn>4</mn></math>
- **(C)** <math><mn>10</mn></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Infinitely many**

**Detailed Solution:**

<math><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>→</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>-</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mtext>  </mtext><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>→</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></math>   <math><mo>(</mo></math> Let  <math><mi>α</mi></math>  is common ratio of  <math><mi>G</mi><mi>P</mi><mo>)</mo></math> 

 <math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><msubsup><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow><mrow><mi>r</mi></mrow></msubsup><msubsup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow><mrow><mi>k</mi></mrow></msubsup></mtd><mtd><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>r</mi><mo>+</mo><mi>k</mi></mrow></msup></mrow></mfenced></mtd><mtd><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>r</mi><mo>+</mo><mi>k</mi></mrow></msup></mrow></mfenced></mtd></mtr><mtr><mtd><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><msubsup><mrow><mi>a</mi></mrow><mrow><mn>4</mn></mrow><mrow><mi>r</mi></mrow></msubsup><msubsup><mrow><mi>a</mi></mrow><mrow><mn>5</mn></mrow><mrow><mi>k</mi></mrow></msubsup></mtd><mtd><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>r</mi><mo>+</mo><mi>k</mi></mrow></msup></mrow></mfenced></mtd><mtd><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>r</mi><mo>+</mo><mi>k</mi></mrow></msup></mrow></mfenced></mrow></mrow></mtd></mtr><mtr><mtd><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><msubsup><mrow><mi>a</mi></mrow><mrow><mn>7</mn></mrow><mrow><mi>r</mi></mrow></msubsup><msubsup><mrow><mi>a</mi></mrow><mrow><mn>8</mn></mrow><mrow><mi>k</mi></mrow></msubsup></mtd><mtd><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>r</mi><mo>+</mo><mi>k</mi></mrow></msup></mrow></mfenced></mrow></mrow></mtd><mtd><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><msup><mrow><mi>α</mi></mrow><mrow><mi>r</mi><mo>+</mo><mi>k</mi></mrow></msup></mrow></mfenced></mrow></mrow></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>0</mn></math>  which is always true because <math><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mi> </mi><mo>&amp;</mo><mi> </mi><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub></math>  are identical.

</details>

---

### Q31. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#62;</mo><mn>0</mn></math>. Then the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>det</mi><mfenced separators="|"><mi>A</mi></mfenced></mrow><mi>b</mi></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mi>b</mi><mfenced separators="|"><mrow><mn>2</mn><mi>b</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced separators="|"><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced open="|" close="|"><mi>A</mi></mfenced><mi>b</mi></mfrac><mo>=</mo><mi>b</mi><mo>+</mo><mfrac><mn>3</mn><mi>b</mi></mfrac><mo>=</mo><msup><mfenced separators="|"><mrow><msqrt><mi>b</mi></msqrt><mo>-</mo><msqrt><mfrac><mn>3</mn><mi>b</mi></mfrac></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

Hence, the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|"><mi>A</mi></mfenced><mi>b</mi></mfrac></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>.  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><msup><mfenced separators="|"><mrow><msqrt><mi>b</mi></msqrt><mo>-</mo><msqrt><mfrac><mn>3</mn><mi>b</mi></mfrac></msqrt></mrow></mfenced><mn>2</mn></msup><mo>&#8805;</mo><mn>0</mn></mrow></mfenced></math>

</details>

---

### Q32. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>d</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>4</mn><mo>+</mo><mi>d</mi></mtd><mtd><mfenced separators="|"><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mfenced separators="|"><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>2</mn></mtd><mtd><mi>d</mi></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mfenced separators="|"><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mi>d</mi></mtd><mtd><mfenced separators="|"><mrow><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>d</mi></mtd></mtr></mtable></mfenced><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>.</mo></math> If the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>e</mi><mi>t</mi><mfenced><mi>A</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>,</mo></math> then a value of <math><mi>d</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math><mo>-</mo><mn>5</mn></math>
- **(D)** <math><mo>-</mo><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mn>5</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>4</mn><mo>+</mo><mi>d</mi></mtd><mtd><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mfenced separators="|"><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>2</mn></mtd><mtd><mi>d</mi></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mfenced separators="|"><mrow><mn>2</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mi>d</mi></mtd><mtd><mfenced separators="|"><mrow><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><mn>2</mn><msub><mi>R</mi><mn>2</mn></msub><mo>+</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>4</mn><mo>+</mo><mi>d</mi></mtd><mtd><mfenced separators="|"><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>&#952;</mi></mrow></mfenced><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mfenced separators="|"><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mn>2</mn></mtd><mtd><mi>d</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>4</mn><mo>+</mo><mi>d</mi></mrow></mfenced><mi>d</mi><mo>-</mo><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>d</mi><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>+</mo><mn>4</mn><mo>=</mo><msup><mfenced separators="|"><mrow><mi>d</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#8804;</mo><mn>1</mn></math></p><p>Given, the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi>A</mi></mfenced><mo>=</mo><mn>8</mn><mo>,</mo></math> which is possible, when <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced separators="|"><mrow><mi>d</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>+</mo><mn>2</mn><mo>=</mo><mo>&#177;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mo>-</mo><mn>5</mn><mo>.</mo></math></p>

</details>

---

### Q33. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\left|\begin{array}{ccc}\cos x & x & 1 \\ 2 \sin x & x^2 & 2 x \\ \tan x & x & 1\end{array}\right|$, then $\lim _{x \rightarrow 0} \frac{f^{\prime}(x)}{x}$

**Options:**

- **(A)** Exists and is equal to $-2$
- **(B)** Does not exist
- **(C)** Exist and is equal to 0
- **(D)** Exists and is equal to 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Exists and is equal to $-2$**

**Detailed Solution:**

$\begin{aligned} & f(x)=\left|\begin{array}{ccc}\cos x & x & 1 \\ 2 \sin x & x^2 & 2 x \\ \tan x & x & 1\end{array}\right| \\=& \cos x\left(x^2-2 x^2\right)-x(2 \sin x-2 x \tan x) \\=&-x^2 \cos x-2 x \sin x+2 x^2 \tan x \\\left.+2 x \sin x-x^2 \tan x\right) \\=& x^2 \tan x-x^2 \tan x \\ \Rightarrow & f^{\prime}(x)=2 x(\tan x-\cos x)+x^2\left(\sec ^2 x+\sin x\right) \\ \therefore & \lim _{x \rightarrow 0} \frac{f^{\prime}(x)}{x} \\=& \lim _{x \rightarrow 0} \frac{2 x(\tan x-\cos x)+x^2\left(\sec ^2 x+\sin x\right)}{x} \\=& \lim _{x \rightarrow 0}(\tan x-\cos x)+x\left(\sec ^2 x+\sin x\right) \\=& 2(0-1)+0=-2 \\ \text { So, } \lim _{x \rightarrow 0} \frac{f^{\prime}(x)}{x}=-2 \end{aligned}$

</details>

---

### Q34. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi><mi>x</mi></mrow></mfenced><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>A</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>,</mo></math> then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>A</mi><mo>,</mo><mo> </mo><mi>B</mi><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>4, 5</mn></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mi></mi><mo>-</mo><mn>5</mn></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mi> </mi><mn>3</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>B</mi><mi>x</mi></mrow></mfenced><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>A</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

Put <math><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mo>-</mo><mn>4</mn></math>

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>x</mi><mo>-</mo><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>B</mi><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>B</mi><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mi>&#8734;</mi><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>B</mi></math></p><p>On expanding the determinant along the first row, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>5</mn></math>.</p>

</details>

---

### Q35. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mi>&#160;</mi><mo>:</mo><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mtd><mtd><mn>0</mn></mtd><mtd><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mtd><mtd><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>x</mi><mtext>&#8201;</mtext><mo>&#8712;</mo><mtext>&#8201;</mtext><mi>S</mi></mrow></munder><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mn>4</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math><mo>-</mo><mn>4</mn><mo>-2</mo><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math><mo>-</mo><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math><mo>-2</mo><mo>-</mo><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mn>4</mn><mo>-2</mo><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mtd><mtd><mn>0</mn></mtd><mtd><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mtd></mtr><mtr><mtd><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mtd><mtd><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Expanding the determinant,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>(</mo><mn>0</mn><mo>-</mo><mi>cos</mi><mo>&#8289;</mo><mi>x</mi><mi>sin</mi><mo>&#8289;</mo><mi>x</mi><mo>)</mo><mo>-</mo><mi>cos</mi><mo>&#8289;</mo><mi>x</mi><mfenced separators="|"><mrow><mn>0</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>sin</mi><mo>&#8289;</mo><mi>x</mi><mfenced separators="|"><mrow><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>-</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math> <mo>&#8658;</mo> </math> <math><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mn>0</mn></math>

<math> <mo>&#8658;</mo> </math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mn>3</mn></msup><mo>&#8289;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>&#160;</mi><mi>tan</mi><mo>&#8289;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mi>&#160;</mi><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><munder><mo>&#8721;</mo><mrow><mi>x</mi><mtext>&#8201;</mtext><mo>&#8712;</mo><mtext>&#8201;</mtext><mi>S</mi></mrow></munder><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><mo>&#8721;</mo><mrow><mi>x</mi><mtext>&#8201;</mtext><mo>&#8712;</mo><mtext>&#8201;</mtext><mi>S</mi></mrow></munder><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>&#8722;</mo><msqrt><mn>3</mn></msqrt><mtext>&#8201;</mtext><mi>tan</mi><mi>x</mi></mrow></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced separators="|"><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>4</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q36. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The number of distinct real roots of the equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> is :

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mn>4</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>2</mn></math>**

**Detailed Solution:**

<p>Given equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Performing row and column operations</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>3</mn></msub></math></p><p><math><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mtable><mtr><mtd><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mtd><mtd><mi>cos</mi><mi>x</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Expanding using second row, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>-</mo><mi>sin</mi><mi>x</mi><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mi>cos</mi><mi>x</mi><mo>&#8658;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>Or</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> solutions are there.</p>

</details>

---

### Q37. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi></mtd><mtd><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn><mi>x</mi></mtd><mtd><mn>3</mn><mi>x</mi><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></mtd><mtd><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>a</mi><mi>x</mi><mo>-</mo><mn>12</mn></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to:

**Options:**

- **(A)** <math><mo>-</mo><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(C)** <math><mo>-</mo><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>**

**Detailed Solution:**

Put <math><mi>x</mi><mo>=</mo><mn>1</mn></math> on both the sides

<math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>a</mi><mo>-</mo><mn>12</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mn>18</mn></mrow></mfenced><mo>=</mo><mi>a</mi><mo>-</mo><mn>12</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>-</mo><mn>8</mn><mo>+</mo><mn>14</mn><mo>=</mo><mi>a</mi><mo>-</mo><mn>12</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mo>=</mo><mi>a</mi><mo>-</mo><mn>12</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>24</mn><mo>=</mo><mi>a</mi><mo>.</mo></math>

</details>

---

### Q38. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The least value of the product <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi></math> (such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>z</mi></math> are positive real numbers) for which the determinant <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mi>&#160;</mi><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>z</mi></mtd></mtr></mtable></mrow></mfenced></math> is non-negative is

**Options:**

- **(A)** <math><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>16</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math><mo>-</mo><mn>8</mn></math>
- **(D)** <math><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mn>8</mn></math>**

**Detailed Solution:**

<p>Since  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">M</mi><mi mathvariant="normal">&#160;</mi><mo>&#8805;</mo><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">M</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi></mrow><mn>3</mn></mfrac><mi>&#160;</mi><mo>&#8805;</mo><msup><mfenced separators="|"><mrow><mi>x</mi><mi>y</mi><mi>z</mi></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mi>&#160;</mi><mo>&#8805;</mo><mn>3</mn><msup><mfenced separators="|"><mrow><mi>x</mi><mi>y</mi><mi>z</mi></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>z</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>x</mi><mi>y</mi><mi>z</mi><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mo>+</mo><mn>2</mn></math></p><p>Now determinant is non-negative</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mi>z</mi><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mo>+</mo><mn>2</mn><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mi>z</mi><mo>-</mo><mfenced separators="|"><mn>3</mn></mfenced><msup><mfenced separators="|"><mrow><mi>x</mi><mi>y</mi><mi>z</mi></mrow></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mn>2</mn><mi>&#160;</mi><mo>&#8805;</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi><mo>=</mo><msup><mi>t</mi><mn>3</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>2</mn><mi>&#160;</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>(</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>&#8805;</mo><mn>0</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced><msup><mrow><mo>(</mo><mi>t</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></msup><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>&#8805;</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>3</mn></msup><mo>&#8805;</mo><mo>-</mo><mn>8</mn></math></p><p><math><mo>&#8658;</mo></math> Least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>8</mn></math></p>

</details>

---

### Q39. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#916;</mi><mi>r</mi></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mi>r</mi></mtd><mtd><mn>2</mn><mi>r</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn><mi>r</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mfrac><mi>n</mi><mn>2</mn></mfrac></mtd><mtd><mi>n</mi><mo>-</mo><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mo>&#160;</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><msub><mi mathvariant="normal">&#916;</mi><mi>r</mi></msub></math>

**Options:**

- **(A)** Is independent of both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
- **(B)** Depends only on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>
- **(C)** Depends only on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
- **(D)** Depends both on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Is independent of both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#916;</mi><mi>r</mi></msub><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mi>r</mi></mtd><mtd><mfenced><mrow><mn>2</mn><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mfenced><mrow><mn>3</mn><mi>r</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mfrac><mi>n</mi><mn>2</mn></mfrac></mtd><mtd><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mo>&#160;</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p>Since, the second and the third rows are independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>,</mo></math> hence the sum is applied to the first row only.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><msub><mi mathvariant="normal">&#916;</mi><mi>r</mi></msub><mo>=</mo><mfenced close="|" open="|"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><mi>r</mi></mtd><mtd><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><mi>r</mi><mo>&#8722;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><mn>1</mn></mtd><mtd><mn>3</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><mi>r</mi><mo>&#8722;</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mi>n</mi><mn>2</mn></mfrac></mtd><mtd><mfenced><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>n</mi><mfenced><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mtd><mtd><msup><mfenced><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>r</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi mathvariant="normal">n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><msub><mi mathvariant="normal">&#916;</mi><mi mathvariant="normal">r</mi></msub><mi mathvariant="normal">=</mi><mfenced close="|" open="|"><mtable><mtr><mtd><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></mrow><mn>2</mn></mfrac></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mn>3</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mfrac><mi>n</mi><mn>2</mn></mfrac></mtd><mtd><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi mathvariant="normal">n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><msub><mi mathvariant="normal">&#916;</mi><mi mathvariant="normal">r</mi></msub><mi mathvariant="normal">=</mi><mfenced close="|" open="|"><mtable><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi></mtd><mtd><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mfrac><mn>1</mn><mrow><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn></mrow></mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mfrac><mi>n</mi><mn>2</mn></mfrac></mtd><mtd><mo>&#160;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>&#8722;</mo><mn>1</mn></mrow></munderover><msub><mi mathvariant="normal">&#916;</mi><mi>r</mi></msub><mo>=</mo><mn>0</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>&#8757;</mo><mo>&#160;</mo><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub></math> are identical<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math></p><p>Hence, the sum is independent of both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>.</mo></math></p>

</details>

---

### Q40. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(\theta)=\left|\begin{array}{ccc}1 & \cos \theta & 1 \\ -\sin \theta & 1 & -\cos \theta \\ -1 & \sin \theta & 1\end{array}\right|$ and
$\mathrm{A}$ and $\mathrm{B}$ are respectively the maximum and the minimum values of $f(\theta)$, then $(A, B)$ is equal to:

**Options:**

- **(A)** $(3,-1)$
- **(B)** $(4,2-\sqrt{2})$
- **(C)** $(2+\sqrt{2}, 2-\sqrt{2})$
- **(D)** $(2+\sqrt{2},-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(2+\sqrt{2}, 2-\sqrt{2})$**

**Detailed Solution:**

$$
\begin{aligned}
&\text { Let } f(\theta)=\left|\begin{array}{ccc}
1 & \cos \theta & 1 \\
-\sin \theta & 1 & -\cos \theta \\
-1 & \sin \theta & 1
\end{array}\right| \\
&=(1+\sin \theta \cos \theta)-\cos \theta(-\sin \theta-\cos \theta) \\
&+1\left(-\sin ^2 \theta+1\right) \\
&=1+\sin \theta \cos \theta+\sin \theta \cos \theta+ \\
&=2+2 \sin \theta \cos \theta+\cos 2 \theta \\
&=2+\sin 2 \theta+\cos 2 \theta
\end{aligned}
$$
Now, maximum value of (1)
is $2+\sqrt{1^2+1^2}=2+\sqrt{2}$ and minimum value of (1) is
$$
2-\sqrt{1^2+1^2}=2-\sqrt{2} \text {. }
$$

</details>

---

### Q41. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $$
\begin{aligned}
&\left.\mid \begin{array}{ccc}
a^2 & b^2 & c^2 \\
(a+\lambda)^2 & (b+\lambda)^2 & \left(c+\lambda^2\right) \\
(a-\lambda)^2 & \left(b-\lambda^2\right) & \left(-\lambda^2\right.
\end{array}\right) \\
&=k \lambda\left|\begin{array}{ccc}
a^2 & b^2 & c^2 \\
a & b & c \\
1 & 1 & 1
\end{array}\right|, \lambda \neq 0
\end{aligned}
$$
then $\mathrm{k}$ is equal to:

**Options:**

- **(A)** $4 \lambda \mathrm{abc}$
- **(B)** $-4 \lambda \mathrm{abc}$
- **(C)** $4 \lambda^2$
- **(D)** $-4 \lambda^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \lambda^2$**

**Detailed Solution:**

Let $\Delta=\left|\begin{array}{ccc}a^2 & b^2 & c^2 \\ (a+\lambda)^2 & (b+\lambda)^2 & (c+\lambda)^2 \\ (a-\lambda)^2 & (b-\lambda)^2 & (c-\lambda)^2\end{array}\right|$
$$
\begin{aligned}
&\text { Apply } \mathrm{R}_2 \rightarrow \mathrm{R}_2-\mathrm{R}_3 \\
&\Delta=\left|\begin{array}{ccc}
a^2 & b^2 & c^2 \\
(a+\lambda)^2-(a-\lambda)^2 & (b+\lambda)^2-(b-\lambda)^2 & (c+\lambda)^2-(c-\lambda)^2 \\
(a-\lambda)^2 & (b-\lambda)^2 & (c-\lambda)^2
\end{array}\right| \\
&=\left|\begin{array}{ccc}
a^2 & b^2 & c^2 \\
4 a \lambda & 4 b \lambda & 4 c \lambda \\
(a-\lambda)^2 & (b-\lambda)^2 & (c-\lambda)^2
\end{array}\right| \\
&\left(\because(x+y)^2-(x-y)^2=4 x y\right) \\
&
\end{aligned}
$$
Taking out 4 common from $\mathrm{R}_2$
$=4\left|\begin{array}{ccc}a^2 & b^2 & c^2 \\ a \lambda & b \lambda & c \lambda \\ a^2+\lambda^2-2 a \lambda & b^2+\lambda^2-2 b \lambda & c^2+\lambda^2-2 c \lambda\end{array}\right|$


$$
\begin{aligned}
&\text { Apply } \mathrm{R}_3 \rightarrow\left[\mathrm{R}_3-\left(\mathrm{R}_1-2 \mathrm{R}_2\right)\right] \\
&=4\left|\begin{array}{lll}
a^2 & b^2 & c^2 \\
a \lambda & b \lambda & c \lambda \\
\lambda^2 & \lambda^2 & \lambda^2
\end{array}\right|
\end{aligned}
$$
Taking out $\lambda$ common from $\mathrm{R}_2$ and $\lambda^2$ from $\mathrm{R}_3$.
$$
=4 \lambda\left(\lambda^2\right)\left|\begin{array}{ccc}
a^2 & b^2 & c^2 \\
a & b & c \\
1 & 1 & 1
\end{array}\right|
$$
$$
\begin{aligned}
&=k \lambda\left|\begin{array}{ccc}
a^2 & b^2 & c^2 \\
a & b & c \\
1 & 1 & 1
\end{array}\right| \\
&\Rightarrow k=4 \lambda^2
\end{aligned}
$$

</details>

---

### Q42. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>&#8800;</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><msup><mi>&#945;</mi><mi>n</mi></msup><mo>+</mo><msup><mi>&#946;</mi><mi>n</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></mtd><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></mtd><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></mtd><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced></mtd></mtr><mtr><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></mtd><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mn>3</mn></mfenced></mtd><mtd><mn>1</mn><mo>+</mo><mi>f</mi><mfenced><mn>4</mn></mfenced></mtd></mtr></mtable></mfenced><mo>=</mo><mi>K</mi><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math> <mrow> <mi>&alpha;</mi> <mi>&beta;</mi> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mi>&alpha;</mi> <mi>&beta;</mi> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>3</mn></msup><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>4</mn></msup></math></p><p>So, the given determinant can be written as

<math> <mrow> <mfenced close="|" open="|" separators=","> <mrow> <mtable> <mtr> <mtd> <mn>1</mn> <mo>+</mo> <mn>1</mn> <mo>+</mo> <mn>1</mn> </mtd> <mtd> <mn>1</mn> <mo>+</mo> <mi>&#945;</mi> <mo>+</mo> <mi>&#946;</mi> </mtd> <mtd> <mn>1</mn> <mo>+</mo> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> <mo>+</mo> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> <mo>+</mo> <mi>&#945;</mi> <mo>+</mo> <mi>&#946;</mi> </mtd> <mtd> <mn>1</mn> <mo>+</mo> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> <mo>+</mo> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> </mtd> <mtd> <mn>1</mn> <mo>+</mo> <msup> <mi>&#945;</mi> <mn>3</mn> </msup> <mo>+</mo> <msup> <mi>&#946;</mi> <mn>3</mn> </msup> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> <mo>+</mo> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> <mo>+</mo> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> </mtd> <mtd> <mn>1</mn> <mo>+</mo> <msup> <mi>&#945;</mi> <mn>3</mn> </msup> <mo>+</mo> <msup> <mi>&#946;</mi> <mn>3</mn> </msup> </mtd> <mtd> <mn>1</mn> <mo>+</mo> <msup> <mi>&#945;</mi> <mn>4</mn> </msup> <mo>+</mo> <msup> <mi>&#946;</mi> <mn>4</mn> </msup> </mtd> </mtr> </mtable> </mrow> </mfenced> </mrow> </math> <math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd></mtr></mtable></mrow></mfenced><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#946;</mi></mtd><mtd><msup><mrow><mi>&#946;</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd></mtr></mtable></mrow></mfenced></math>

<math> <mrow> <mo>=</mo> <mfenced close="|" open="|" separators=","> <mrow> <mtable> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mn>1</mn> </mtd> <mtd> <mn>1</mn> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mi>&#945;</mi> </mtd> <mtd> <mi>&#946;</mi> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> </mtd> <mtd> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> </mtd> </mtr> </mtable> </mrow> </mfenced> <mfenced close="|" open="|" separators=","> <mrow> <mtable> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mn>1</mn> </mtd> <mtd> <mn>1</mn> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mi>&#945;</mi> </mtd> <mtd> <mi>&#946;</mi> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> </mtd> <mtd> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> </mtd> </mtr> </mtable> </mrow> </mfenced> </mrow> </math>

<math> <mrow> <mo>=</mo> <msup> <mrow> <mfenced close="|" open="|" separators=","> <mrow> <mtable> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mn>1</mn> </mtd> <mtd> <mn>1</mn> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mi>&#945;</mi> </mtd> <mtd> <mi>&#946;</mi> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> </mtd> <mtd> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> </mtd> </mtr> </mtable> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> <mo>=</mo> <msup> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#945;</mi> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> <mo>-</mo> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> <mi>&#946;</mi> </mrow> </mfenced> <mo>-</mo> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>&#946;</mi> <mn>2</mn> </msup> <mo>-</mo> <mi>&#946;</mi> </mrow> </mfenced> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>&#945;</mi> <mn>2</mn> </msup> <mo>-</mo> <mi>&#945;</mi> </mrow> </mfenced> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> </mrow> </math>

<math> <mrow> <mo>=</mo> <msup> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mi>&#945;</mi> <mi>&#946;</mi> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#946;</mi> <mo>-</mo> <mi>&#945;</mi> </mrow> </mfenced> <mo>-</mo> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#946;</mi> <mo>-</mo> <mi>&#945;</mi> </mrow> </mfenced> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#946;</mi> <mo>+</mo> <mi>&#945;</mi> </mrow> </mfenced> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#946;</mi> <mo>-</mo> <mi>&#945;</mi> </mrow> </mfenced> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> </mrow> </math>

<math><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>&#946;</mi><mo>-</mo><mi>a</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi mathvariant="italic">&#945;&#946;</mi><mo>-</mo><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

 <math> <mrow> <mo>=</mo> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#946;</mi> <mo>-</mo> <mi>&#945;</mi> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#945;</mi> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>&#946;</mi> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> </mrow> </math>

Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q43. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If $a, b, c$ are sides of a scalene triangle, then the value of $\left|\begin{array}{lll}a & b & c \\ b & c & a \\ c & a & b\end{array}\right|$ is :

**Options:**

- **(A)** non - negative
- **(B)** negative
- **(C)** positive
- **(D)** non-positive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) negative**

**Detailed Solution:**

$$
\begin{aligned}
&\left|\begin{array}{lll}
a & b & c \\
b & c & a \\
c & a & b
\end{array}\right|=\left|\begin{array}{ccc}
a+b+c & a+b+c & a+b+c \\
b & c & a \\
c & a & b
\end{array}\right| \\
&=(a+b+c)\left|\begin{array}{lll}
1 & 1 & 1 \\
b & c & a \\
c & a & b
\end{array}\right| \\
&=(a+b+c)\left|\begin{array}{ccc}
0 & 0 & 1 \\
b-c & c-a & a \\
c-a & a-b & b
\end{array}\right| \\
&=(a+b+c)\left[a b+b c+c a-a^2-b^2-c^2\right] \\
&=-(a+b+c)\left[(a-b)^2+(b-c)^2+(c-a)^2\right]
\end{aligned}
$$
Since $a, b, c$ are sides of $a$ scalene triangle, therefore at least two of the $a, b, c$ will be unequal.
$\begin{array}{ll}\therefore \quad & (a-b)^2+(b-c)^2+(c-a)^2>0 \\ & \text { Also } a+b+c>0 \\ \therefore \quad & -(a+b+c)\left[(a-b)^2+\right. \\ & \left.(b-c)^2+(c-a)^2\right] < 0\end{array}$

</details>

---

### Q44. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If $a, b, c$, are non zero complex numbers satisfying $a^2+b^2+c^2=0$ and
$\left|\begin{array}{ccc}b^2+c^2 & a b & a c \\ a b & c^2+a^2 & b c \\ a c & b c & a^2+b^2\end{array}\right|=k a^2 b^2 c^2$, then $k$ is equal to

**Options:**

- **(A)** 1
- **(B)** 3
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

Let $\Delta=\left|\begin{array}{ccc}b^2+c^2 & a b & a c \\ a b & c^2+a^2 & b c \\ a c & b c & a^2+b^2\end{array}\right|$
Multiply $C_1$ by $a, C_2$ by b and $C_3$ by $\mathrm{c}$ and hence divide by $a b c$.

$$
=\frac{1}{a b c}\left|\begin{array}{ccc}
a\left(b^2+c^2\right. & \left.a b^2\right) & a c^2 \\
a^2 b & b\left(c^2+a^2\right. & \left.b c^2\right) \\
a^2 c & b^2 c & c\left(a^2+b^2\right.
\end{array}\right|
$$
Take out $a, b, c$ common from $R_1, R_2$ and $R_3$ respectively.
$$
\begin{aligned}
& \therefore \quad \Delta=\frac{a b c}{a b c}\left|\begin{array}{ccc}
b^2+c^2 & b^2 & c^2 \\
a^2 & c^2+a^2 & c^2 \\
a^2 & b^2 & a^2+b^2
\end{array}\right| \\
& \text { Apply } C_1 \rightarrow C_1-C_2-C_3 \\
& \Delta=\left|\begin{array}{ccc}
0 & b^2 & c^2 \\
-2 c^2 & c^2+a^2 & c^2 \\
-2 b^2 & b^2 & a^2+b^2
\end{array}\right| \\
& =-2\left|\begin{array}{ccc}
0 & b^2 & c^2 \\
c^2 & c^2+a^2 & c^2 \\
b^2 & b^2 & a^2+b^2
\end{array}\right| \\
&
\end{aligned}
$$
Apply $C_2-C_1$ and $C_3-C_1$
$$
\begin{aligned}
& =-2\left|\begin{array}{ccc}
0 & b^2 & c^2 \\
c^2 & a^2 & 0 \\
b^2 & 0 & a^2
\end{array}\right| \\
& =-2\left[-b^2\left(c^2 a^2\right)+c^2\left(-a^2 b^2\right)\right] \\
& =2 a^2 b^2 c^2+2 a^2 b^2 c^2=4 a^2 b^2 c^2 \\
& \text { But } \Delta=k a^2 b^2 c^2 \therefore k=4
\end{aligned}
$$

</details>

---

### Q45. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\left|\begin{array}{ccc}-2 a & a+b & a+c \\ b+a & -2 b & b+c \\ c+a & b+c & -2 c\end{array}\right|$
$$
=\alpha(a+b() b+c() c+a) \neq 0
$$
then $\alpha$ is equal to

**Options:**

- **(A)** $a+b+c$
- **(B)** $a b c$
- **(C)** 4
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

Let $\Delta=\left|\begin{array}{ccc}-2 a & a+b & a+c \\ b+a & -2 b & b+c \\ c+a & b+c & -2 c\end{array}\right|$


Applying $C_1+C_3$ and $C_2+C_3$
$$
\Delta=\left|\begin{array}{ccc}
-a+c & 2 a+b+c & a+c \\
2 b+a+c & -b+c & b+c \\
a-c & b-c & -2 c
\end{array}\right|
$$
Now, applying $R_1+R_3$ and $R_2+R_3$
$$
\Delta=\left|\begin{array}{ccc}
0 & 2(a+b & ) a-c \\
2(a+b & 0 & b-c \\
a-c & b-c & -2 c
\end{array}\right|
$$
On expanding, we get
$$
\begin{aligned}
\Delta= & -2(a+b)\{-2 c[2(a+b)] \\
& -(a-c)(b-c)\} \\
& +(a-c)[2(a+b)(b-c)] \\
\Delta= & 8 \mathrm{c}(a+b)(a+b) \\
& +4(a+b)(a-c)(b-c)
\end{aligned}
$$

$$
\begin{aligned}
& =4(a+b)\left[2 a c+2 b c+a b-b c-a c+c^2\right] \\
& =4(a+b)\left[a c+b c+a b+c^2\right] \\
& =4(a+b)[c(a+c)+b(a+c)] \\
& =4(a+b)(b+c)(c+a) \\
& =\alpha(a+b)(b+c)(c+a)
\end{aligned}
$$
Hence, $\alpha=4$

</details>

---

### Q46. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `3`

Let $a, b, c$ be such that $b(a+c) \neq 0$. If $\left|\begin{array}{ccc}a & a+1 & a-1 \\ -b & b+1 & b-1 \\ c & c-1 & c+1\end{array}\right|+\left|\begin{array}{ccc}a+1 & b+1 & c-1 \\ a-1 & b-1 & c+1 \\ (-1)^{n+2} a & (-1)^{n+1} b & (-1)^n c\end{array}\right|=0$, then the value of ' $n$ ' is

**Options:**

- **(A)** zero
- **(B)** any even integer
- **(C)** any odd integer
- **(D)** any integer

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) any odd integer**

**Detailed Solution:**

$$
\begin{aligned}
& \left|\begin{array}{ccc}
a & a+1 & a-1 \\
-b & b+1 & b-1 \\
c & c-1 & c+1
\end{array}\right|+(-1)^n\left|\begin{array}{ccc}
a+1 & b+1 & c-1 \\
a-1 & b-1 & c+1 \\
a & -b & c
\end{array}\right|=\left|\begin{array}{ccc}
a & a+1 & a-1 \\
-b & b+1 & b-1 \\
c & c-1 & c+1
\end{array}\right|+(-1)^n\left|\begin{array}{cccc}
a+1 & a-1 & a \\
b+1 & b-1 & -b \\
c-1 & c+1 & c
\end{array}\right| \\
& =\left|\begin{array}{ccc}
a & a+1 & a-1 \\
-b & b+1 & b-1 \\
c & c-1 & c+1
\end{array}\right|+(-1)^{n+1}\left|\begin{array}{ccc}
a+1 & a & a-1 \\
b+1 & -b & b-1 \\
c-1 & c & c+1
\end{array}\right|=\left|\begin{array}{ccc}
a & a+1 & a-1 \\
-b & b+1 & b-1 \\
c & c-1 & c+1
\end{array}\right|+(-1)^{n+2}\left|\begin{array}{ccc}
a & a+1 & a-1 \\
-b & b+1 & b-1 \\
c & c-1 & c+1
\end{array}\right|
\end{aligned}
$$
This is equal to zero only if $n+2$ is odd i.e. $n$ is odd integer.

</details>

---

### Q47. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

If $D=\left|\begin{array}{ccc}1 & 1 & 1 \\ 1 & 1+x & 1 \\ 1 & 1 & 1+y\end{array}\right|$ for $x \neq 0, y \neq 0$ then $D$ is

**Options:**

- **(A)** divisible by neither $x$ nor $y$
- **(B)** divisible by both $x$ and $y$
- **(C)** divisible by $x$ but not $y$
- **(D)** divisible by $y$ but not $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) divisible by both $x$ and $y$**

**Detailed Solution:**

$D=\left|\begin{array}{ccc}1 & 1 & 1 \\ 1 & 1+x & 1 \\ 1 & 1 & 1+y\end{array}\right|$
$\mathrm{C}_2 \rightarrow \mathrm{C}_2-\mathrm{C}_1$ \& $\mathrm{C}_3 \rightarrow \mathrm{C}_3-\mathrm{C}_1$
$\left|\begin{array}{lll}
1 & 0 & 0 \\
1 & x & 0 \\
1 & 0 & y
\end{array}\right|=x y$.
Hence $D$ is divisible by both $x$ and $y$.

</details>

---

### Q48. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If $a_1, a_2, a_3, \ldots, a_n, \ldots$ are in G.P., then the determinant $\Delta=\left|\begin{array}{lll}\log a_n & \log a_{n+1} & \log a_{n+2} \\ \log a_{n+3} & \log a_{n+4} & \log a_{n+5} \\ \log a_{n+6} & \log a_{n+7} & \log a_{n+8}\end{array}\right|$ is equal to

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

$\mathrm{C}_1-\mathrm{C}_2, \mathrm{C}_2-\mathrm{C}_3$
two rows becomes identical
Answer: 0.

</details>

---

### Q49. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If $a^2+b^2+c^2=-2$ and $f(x)=\left|\begin{array}{ccc}1+a^2 x & \left(1+b^2\right) x & \left(1+c^2\right) x \\ \left(1+a^2\right) x & 1+b^2 x & \left(1+c^2\right) x \\ \left(1+a^2\right) x & \left(1+b^2\right) x & 1+c^2 x\end{array}\right|$ then $f(x)$ is $a$ polynomial of degree

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** 3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

$$
\begin{aligned}
& f(x)=\left|\begin{array}{ccc}
1+\left(a^2+b^2+c^2+2\right) x & \left(1+b^2\right) x & \left(1+c^2\right) x \\
1+\left(a^2+b^2+c^2+2\right) x & 1+b^2 x & \left(1+c^2\right) x \\
1+\left(a^2+b^2+c^2+2\right) x & \left(1+b^2\right) x & 1+c^2 x
\end{array}\right| \text {, Applying } C_1 \rightarrow C_1+C_2+C_3 \\
& =\left|\begin{array}{ccc}
1 & \left(1+b^2\right) x & \left(1+c^2\right) x \\
1 & 1+b^2 x & \left(1+c^2\right) x \\
1 & \left(1+b^2\right) x & 1+c^2 x
\end{array}\right| \because a^2+b^2+c^2+2=0 \\
& f(x)=\left|\begin{array}{ccc}
0 & x-1 & 0 \\
0 & 1-x & x-1 \\
1 & \left(1+b^2\right) x & 1+c x
\end{array}\right| ; \text { Applying } R_1 \rightarrow R_1-R_2, R_2 \rightarrow R_2-R_3 \\
& f(x)=(x-1)^2
\end{aligned}
$$
Hence degree $=2$.

</details>

---

### Q50. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $a_1, a_2, a_3, \ldots, a_n, \ldots$. are in G.P., then the value of the determinant
$$
\left|\begin{array}{ccc}
\log a_n & \log a_{n+1} & \log a_{n+2} \\
\log a_{n+3} & \log a_{n+4} & \log a_{n+5} \\
\log a_{n+6} & \log a_{n+7} & \log a_{n+8}
\end{array}\right| \text {, is }
$$

**Options:**

- **(A)** 0
- **(B)** $-2$
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

$$
\begin{aligned}
& \left|\begin{array}{lll}
\log a_n & \log a_{n+1} & \log a_{n+2} \\
\log a_{n+3} & \log a_{n+4} & \log a_{n+5} \\
\log a_{n+6} & \log a_{n+7} & \log a_{n+8}
\end{array}\right| \\
& C_3 \rightarrow C_3-C_2, C_2 \rightarrow C_3-C_1 \\
& =\left|\begin{array}{lll}
\log a_n & \log r & \log r \\
\log a_{n+3} & \log r & \log r \\
\log a_{n+6} & \log r & \log r
\end{array}\right|=0
\end{aligned}
$$
(where $r$ is a common ratio).

</details>

---

### Q51. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $1, \omega, \omega^2$ are the cube roots of unity, then $\Delta=\left|\begin{array}{ccc}1 & \omega^n & \omega^{2 n} \\ \omega^n & \omega^{2 n} & 1 \\ \omega^{2 n} & 1 & \omega^n\end{array}\right|$ is equal to

**Options:**

- **(A)** $\omega^2$
- **(B)** 0
- **(C)** 1
- **(D)** $\omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

Applying $\mathrm{R}_1 \rightarrow \mathrm{R}_1+\mathrm{R}_2+\mathrm{R}_3$
As, $1+\omega^{\mathrm{n}}+\omega^{2 \mathrm{n}}=0 ; \quad \therefore \Delta=0$

</details>

---

### Q52. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If $a>0$ discriminant of $a x^2+2 b x+c$ is -ve, then
$\left|\begin{array}{ccc}a & b & a x+b \\ b & c & b x+c \\ a x+b & b x+c & 0\end{array}\right|$ is

**Options:**

- **(A)** +ve
- **(B)** $\left(a c-b^2\right)\left(a x^2+2 b x+c\right)$
- **(C)** -ve
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -ve**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/j6cOEa0akGPgCOwil256WvLGq6C0zjMKZSGdiXqe9uU.original.fullsize.png">

</details>

---

### Q53. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$l, m, n$ are the $p^{\text {th }}, q^{\text {th }}$ and $r^{\text {th }}$ term of a G.P. all positive, then $\left|\begin{array}{ccc}\log l & p & 1 \\ \log m & q & 1 \\ \log n & r & 1\end{array}\right|$ equals

**Options:**

- **(A)** -1
- **(B)** 2
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/DQGdlezvja-RtbhQl-IQwmQRRdsY4gjFJFoPf-0mnWs.original.fullsize.png">

</details>

---

