# MHT CET Mathematics - Definite Integration

## Topic 7: Miscellaneous

**Total Questions:** 22

---

### Q1. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of the integral $\int_1^2 \frac{x \mathrm{~d} x}{(x+2)(x+3)}$ is

**Options:**

- **(A)** $\log \left(\frac{125}{16}\right)$
- **(B)** $\log \left(\frac{1024}{1125}\right)$
- **(C)** $\log \left(\frac{16}{125}\right)$
- **(D)** $\log \left(\frac{1125}{1024}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log \left(\frac{1125}{1024}\right)$**

**Detailed Solution:**

Let $I = \int_1^2 \dfrac{x}{(x+2)(x+3)} \mathrm{d}x$

Using partial fractions,

$\dfrac{x}{(x+2)(x+3)} = \dfrac{A}{x+2} + \dfrac{B}{x+3}$

$x = A(x+3) + B(x+2)$

Putting $x = -2$, we get $A = -2$

Putting $x = -3$, we get $B = 3$

Therefore, the integral becomes:

$I = \int_1^2 \left( \dfrac{-2}{x+2} + \dfrac{3}{x+3} \right) \mathrm{d}x$

$I = \left[ -2 \log|x+2| + 3 \log|x+3| \right]_1^2$

Substituting the upper and lower limits:

$I = (-2 \log 4 + 3 \log 5) - (-2 \log 3 + 3 \log 4)$

$I = 3 \log 5 + 2 \log 3 - 5 \log 4$

Using the properties of logarithms $m \log n = \log(n^m)$ and $\log a + \log b = \log(ab)$:

$I = \log(5^3) + \log(3^2) - \log(4^5)$

$I = \log(125) + \log(9) - \log(1024)$

$I = \log(125 \times 9) - \log(1024)$

$I = \log(1125) - \log(1024)$

$I = \log \left( \dfrac{1125}{1024} \right)$

Answer: $\log \left(\frac{1125}{1024}\right)$

</details>

---

### Q2. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{\frac{\pi}{3}}^{\frac{\pi}{2}} \frac{\sqrt{1+\cos x}}{(1-\cos x)^{\frac{5}{2}}} d x=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{-1}{2}$
- **(C)** $\frac{3}{2}$
- **(D)** $\frac{-3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{2}$**

**Detailed Solution:**

Let $I = \int_{\dfrac{\pi}{3}}^{\dfrac{\pi}{2}} \dfrac{\sqrt{1+\cos x}}{(1-\cos x)^{\dfrac{5}{2}}} d x$

Multiplying the numerator and the denominator by $\sqrt{1-\cos x}$:

$I = \int_{\dfrac{\pi}{3}}^{\dfrac{\pi}{2}} \dfrac{\sqrt{1-\cos^2 x}}{(1-\cos x)^3} d x$

Since $x \in [\dfrac{\pi}{3}, \dfrac{\pi}{2}]$, $\sin x > 0$, so $\sqrt{1-\cos^2 x} = \sin x$.

$I = \int_{\dfrac{\pi}{3}}^{\dfrac{\pi}{2}} \dfrac{\sin x}{(1-\cos x)^3} d x$

Substituting $t = 1-\cos x$, which gives $dt = \sin x d x$.

When $x = \dfrac{\pi}{3}$, $t = 1 - \dfrac{1}{2} = \dfrac{1}{2}$.

When $x = \dfrac{\pi}{2}$, $t = 1 - 0 = 1$.

The integral becomes:

$I = \int_{\dfrac{1}{2}}^{1} \dfrac{dt}{t^3}$

$I = \left[ \dfrac{t^{-2}}{-2} \right]_{\dfrac{1}{2}}^{1}$

$I = -\dfrac{1}{2} \left[ \dfrac{1}{t^2} \right]_{\dfrac{1}{2}}^{1}$

$I = -\dfrac{1}{2} \left( 1 - \dfrac{1}{(\dfrac{1}{2})^2} \right)$

$I = -\dfrac{1}{2} (1 - 4)$

$I = \dfrac{3}{2}$

Answer: $\frac{3}{2}$

</details>

---

### Q3. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{f}(x)$ be positive for all real $x$. If $\mathrm{I}_1=\int_{1-\mathrm{h}}^{\mathrm{h}} x \mathrm{f}(x(1-x)) \mathrm{d} x$ and $\mathrm{I}_2=\int_{1-\mathrm{h}}^{\mathrm{h}} \mathrm{f}(x(1-x)) \mathrm{d} x$, where $(2 h-1)>0$, then $\frac{I_1}{I_2}$ is

**Options:**

- **(A)** $2$
- **(B)** $h$
- **(C)** $\frac{1}{2}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{I}_1 & =\int_{1-\mathrm{h}}^{\mathrm{h}} x \mathrm{f}(x(1-x)) \mathrm{d} x \text { and } \\ \mathrm{I}_2 & =\int_{1-\mathrm{h}}^{\mathrm{h}} \mathrm{f}(x(1-x)) \mathrm{d} x \\ \mathrm{I}_1 & =\int_{1-\mathrm{h}}^{\mathrm{h}}(1-x) \mathrm{f}[(1-x)(1-1+x)] \mathrm{d} x \\ \therefore \quad \ldots\left[\because \int_{\mathrm{a}} \mathrm{f}(x) \mathrm{d} x=\int_{\mathrm{a}}^{\mathrm{b}} \mathrm{f}(\mathrm{a}+\mathrm{b}-x) \mathrm{d} x\right] & \mathrm{I}_1=\int_{1-\mathrm{h}}^{\mathrm{h}}(1-x) \mathrm{f}(x(1-x)) \mathrm{d} x \\ & =\int_{1-\mathrm{h}}^{\mathrm{h}} \mathrm{f}(x(1-x)) \mathrm{d} x-\int_{1-\mathrm{h}}^{\mathrm{h}} x \mathrm{f}(x(1-x)) \mathrm{d} x \\ & \Rightarrow \mathrm{I}_1=\mathrm{I}_2-\mathrm{I}_1 \\ & \Rightarrow 2 \mathrm{I}_1=\mathrm{I}_2 \\ & \Rightarrow \frac{\mathrm{I}_1}{\mathrm{I}_2}=\frac{1}{2}\end{aligned}$

</details>

---

### Q4. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)$ is a function satisfying $\mathrm{f}^{\prime}(x)=\mathrm{f}(x)$ with $\mathrm{f}(0)=1$ and $\mathrm{g}(x)$ is a function that satisfies $\mathrm{f}(x)+\mathrm{g}(x)=x^2$. Then the value of the integral $\int_0^1 \mathrm{f}(x) \mathrm{g}(x) \mathrm{d} x$ is

**Options:**

- **(A)** $e-\frac{e^2}{2}-\frac{5}{2}$
- **(B)** $\mathrm{e}+\frac{\mathrm{e}^2}{2}-\frac{3}{2}$
- **(C)** $e-\frac{e^2}{2}-\frac{3}{2}$
- **(D)** $e+\frac{e^2}{2}+\frac{5}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e-\frac{e^2}{2}-\frac{3}{2}$**

**Detailed Solution:**

As $\mathrm{f}^{\prime}(x)=\mathrm{f}(x)$
$\frac{f^{\prime}(x)}{\mathrm{f}(x)}=1$
Integrating on both sides, we get
$\log \mathrm{f}(x)=x+\mathrm{c}$
As $f(0)=1$
$\begin{array}{ll}
\therefore & (\mathrm{i}) \Rightarrow \mathrm{c}=0 \\
\therefore & \log \mathrm{f}(x)=x \\
\therefore & \mathrm{f}(x)=\mathrm{e}^x
\end{array}$
$\begin{aligned}
& \text { As } \mathrm{f}(x)+\mathrm{g}(x)=x^2 \\
& \mathrm{~g}(x)=x^2-\mathrm{e}^x
\end{aligned}$
$\therefore \quad \mathrm{f}(x) \mathrm{g}(x)=\mathrm{e}^x\left(x^2-\mathrm{e}^x\right)$
$\begin{aligned}
& =\int_0^1\left(\mathrm{e}^x x^2-\mathrm{e}^{2 x}\right) \mathrm{d} x \\
& =\left[\left(x^2-2 x+2\right) \mathrm{e}^x\right]_0^1-\frac{1}{2} \mathrm{e}^2+\frac{1}{2} \\
& =\mathrm{e}-\frac{1}{2} \mathrm{e}^2-\frac{3}{2}
\end{aligned}$

</details>

---

### Q5. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the straight-line $x=b$ divides the area enclosed by $y=(1-x)_{-}^2$ $y=0$ and $x=0$ in two parts $R_1(0 \leq x \leq b)$ and $R_2(b \leq x \leq 1)$ such that $R_1-R_2=\frac{1}{4}$. Then $\mathrm{b}$ equals

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{4}$
- **(C)** $\frac{3}{4}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & \int_0^b(1-x)^2 \mathrm{~d} x-\int_b^1(1-x)^2 \mathrm{~d} x=\frac{1}{4} \\ & \Rightarrow\left[\frac{(1-x)^3}{-3}\right]_0^b-\left[\frac{(1-x)^3}{-3}\right]_b^1=\frac{1}{4}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/DyfGli1vde-U0CM8r48Q-A4BlTsVxGzPR3nw8Dp1k5c.original.fullsize.png">

$\begin{aligned} & \Rightarrow \frac{(1-b)^3-(1-0)^3-(1-1)^3+(1-b)^3}{-3}=\frac{1}{4} \\ & 2(1-b)^3-1=\frac{-3}{4} \\ & \Rightarrow 2(1-b)^3-1=\frac{-3}{4} \\ & \Rightarrow(1-b)^3=\frac{1}{8} \\ & \Rightarrow b=\frac{1}{2}\end{aligned}$

</details>

---

### Q6. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int_0^2[x] d x+\int_0^2|x-1| d x=$
(where $[x]$ denotes the greatest integer function.)

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

$\begin{aligned} & \int_0^2[x] d x+\int_0^2[x-1] d x \\ & =\int_0^1 0 . d x+\int_1^2 1 . d x+\int_0^1(1-x) d x+\int_1^2(x-1) d x \\ & =[0]_0^1+[x]_1^2+\left[x-\frac{x^2}{2}\right]_0^1+\left[\frac{x^2}{2}-x\right]_1^2 \\ & =0+1+\frac{1}{2}+\frac{1}{2}=2\end{aligned}$

</details>

---

### Q7. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $[t]$ denot the greatest integer less than or equal to $t$. Then the value of $\int_1^2|2 x-[3 x]| d x$ is

**Options:**

- **(A)** $1$
- **(B)** $\frac{3}{2}$
- **(C)** $2$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

$\begin{aligned} & \int_1^2|2 x-[3 x]| d x=\int_1^{\frac{4}{3}}|2 x-3| d x+\int_{\frac{4}{3}}^{\frac{5}{3}}|2 x-4| d x+\int_{\frac{5}{3}}^2|2 x-5| d x \\ & =\int_1^{\frac{4}{3}}(3-2 x) d x+\int_{\frac{4}{3}}^{\frac{5}{3}}(4-2 x) d x+\int_{\frac{5}{3}}^2(5-2 x) d x \\ & =\left[3 x-x^2\right]_1^{4 / 3}+\left[4 x-x^2\right]_{4 / 3}^{5 / 3}+\left[5 x-x^2\right]_{5 / 3}^2 \\ & =3[x]_1^{4 / 3}+[4 x]_{4 / 3}^{5 / 3}+5\left[x^2\right]_{5 / 3}^2-\left[x^2\right]_1^2 \\ & =(3+4+5) \times \frac{1}{3}-\left(2^2-1^2\right) \\ & =4-3=1\end{aligned}$

</details>

---

### Q8. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_2^5 2[x] d 
18x=\{$ where $[x]$ denotes the greatest integer function $\leq x\}$

**Options:**

- **(A)** 18
- **(B)** 16
- **(C)** 12
- **(D)** 24

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 18**

**Detailed Solution:**

$\begin{aligned} & \text { Let } I=\int_2^5 2[x] d x \\ & =\int_2^3 2(2) d x+\int_3^4 2(3) d x+\int_4^5 2(4) d x \\ & =4[x]_2^3+6[x]_3^4+8[x]_4^5=4+6+8=18\end{aligned}$

</details>

---

### Q9. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int \tan ^{-1}(\sec x+\tan x) d x=$

**Options:**

- **(A)** $\frac{\pi x}{4}+\frac{x^2}{4}+c$
- **(B)** $\sin x \cos x+c$
- **(C)** $\frac{\pi \mathrm{x}}{2}+\frac{\mathrm{x}^2}{2}+\mathrm{c}$
- **(D)** $\sin x+\cos x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi x}{4}+\frac{x^2}{4}+c$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } I=\tan ^{-1}(\sec x+\tan x) d x \\ & =\int \tan ^{-1}\left(\frac{1+\sin x}{\cos x}\right) d x \\ & =\int \tan ^{-1} x\left[\frac{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)^2}{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)}\right]_{d x} \\ & =\int \tan ^{-1}\left(\frac{\left.\cos \frac{x}{2}+\sin \frac{x}{2}\right)}{\cos \frac{x}{2}-\sin \frac{x}{2}}\right) d x \quad=\int \tan ^{-1}\left(\frac{1+\sin \frac{x}{2}}{1-\tan \frac{x}{2}}\right) d x \\ & =\int \tan ^{-1}\left[\tan \left(\frac{\pi}{4}+\frac{x}{2}\right)\right] d x=\int\left(\frac{\pi}{4}+\frac{x}{2}\right) d x \\ & =\frac{\pi x}{4}+\frac{x^2}{4}+c\end{aligned}$

</details>

---

### Q10. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{4}|x-2| d x=$

**Options:**

- **(A)** 0
- **(B)** 4
- **(C)** 8
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4**

**Detailed Solution:**

$\begin{aligned} \int_{0}^{4}|x-2| d x &=\int_{0}^{2}(2-x) d x+\int_{2}^{4}(x-2) d x \\ &=2[x]_{0}^{2}-\frac{1}{2}\left[x^{2}\right]_{0}^{2}+\frac{1}{2}\left[x^{2}\right]_{2}^{4}-2[x]_{2}^{4} \\ &=2(2)-\frac{1}{2}(4)+\frac{1}{2}(16-4)-2(4-2) \\ &=4-2+6-4=4 \end{aligned}$

</details>

---

### Q11. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{-2}^{2.24}[x] d x=$
where $[x]$ is the greatest integer function

**Options:**

- **(A)** 2
- **(B)** 4
- **(C)** $-2$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-2$**

**Detailed Solution:**

(D)
$\begin{aligned} \int_{-2}^{2}[\mathrm{x}] \mathrm{dx} &=\int_{-2}^{-1}-2 \mathrm{dx}+\int_{-1}^{0}-1 \mathrm{dx}+\int_{0}^{1} 0 \mathrm{dx}+\int_{1}^{2} 1 \mathrm{dx} \\ &=-2[\mathrm{x}]_{-2}^{-1}+(-1)[\mathrm{x}]_{-1}^{0}+1[\mathrm{x}]_{1}^{2} \\ &=-2[-1-(-2)]-1[-(-1)]+1[2-1] \\ &=-2[1]-1[1]+1[1]=-2-1+1=-2 \end{aligned}$

</details>

---

### Q12. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\int_{0}^{\frac{\pi}{2}} \sin ^{2} x \mathrm{~d} x=$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{3 \pi}{2}$
- **(C)** $\frac{3 \pi}{4}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} \int_{0}^{\frac{\pi}{2}} \sin ^{2} x d x &=\frac{1}{2} \int_{0}^{\frac{\pi}{2}}(1-\cos 2 x) d x=\frac{1}{2}\left[x-\frac{\sin 2 x}{2}\right]_{0}^{\frac{\pi}{2}} \\ &=\frac{1}{2}\left[\frac{\pi}{2}+0\right]=\frac{\pi}{4} \end{aligned}$

</details>

---

### Q13. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

$\int_{-2}^{1}[x+1] d x=$
(Where $[x]$ is greatest integer function not greater than $x$ )

**Options:**

- **(A)** $1$
- **(B)** $0$
- **(C)** $-1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

$\begin{aligned} \int_{-2}^{1}[x+1] d x &=\int_{-2}^{-1}([x]+1) d x+\int_{-1}^{0}([x]+1) d y+\int_{0}^{1}([x]+1) d x \\ &=\int_{-2}^{-1}(-2+1) d x+\int_{-1}^{0}(-1+1) d x+\int_{0}^{1}(0+1) d x \\ &=-[x]_{-2}^{-1}+0+[x]_{0}^{1}=-(-1+2)+0+(1-0) \\ &=0 \end{aligned}$

</details>

---

### Q14. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\frac{d^{2} y}{d x^{2}}=\sin x+e^{x} ; y(0)=3$ and $\frac{d y}{d x}$ at $x=0$ is 4 , then the equation of the

**Options:**

- **(A)** $y=4+2 x+e^{x}-\sin x$
- **(B)** $y=2+3 x+e^{x}-\sin x$
- **(C)** $y=2+4 x+e^{x}-\sin x$
- **(D)** $y=4+2 x+e^{x}+\sin x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y=2+4 x+e^{x}-\sin x$**

**Detailed Solution:**

$\frac{d}{d x}\left(\frac{d y}{d x}\right)=\sin x+e^{x}$
Integrating both sides.;
$y \rightarrow \frac{d y}{d x}=e^{x}-\cos x+c$
at $x=0 ; \frac{d y}{d x}=4 ; \quad c=4$
$\frac{d y}{d x}=e^{x}-\cos x+4$
Integrating both sides;
$y=e^{x}-\sin x+4 x+c$
put $x=0 ; y(0)=3$;
$c=2$
Equation of curve $y=e^{x}-\sin x+4 x+2$

</details>

---

### Q15. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int_{0}^{1}\left(5 x^{2}-3 x+k\right) d x=0$, then $k=$

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{1}{6}$
- **(C)** $\frac{-1}{3}$
- **(D)** $\frac{-1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{-1}{6}$**

**Detailed Solution:**

Given $\int_{0}^{1}\left(5 x^{2}-3 x+k\right) d x=0$
$\therefore\left[5 \frac{x^{3}}{3}-\frac{3 x^{2}}{2}+k x\right]_{0}^{1}=0 \Rightarrow \frac{5}{3}-\frac{3}{2}+k=0 \Rightarrow k=-\frac{1}{6}$

</details>

---

### Q16. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

By Simpson rule taking $n=4$, the value of the integral $\int_{0}^{1} \frac{1}{1+x^{2}} d x$ is equal to

**Options:**

- **(A)** $0.788$
- **(B)** $0.781$
- **(C)** $0.785$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.785$**

**Detailed Solution:**

Here, $h=1 / 4,=0.25, y=\frac{1}{1+x^{2}}$
\begin{array}{c|c|c}
\hline & x & y \\
\hline 1 & 0 & 1.0 \\
2 & 0.25 & 0.941 \\
3 & 0.5 & 0.8 \\
4 & 0.75 & 0.64 \\
\hline 5 & 1 & 0.5 \\
\hline
\end{array}

$$
\begin{array}{c|c|c}
\hline & x & y \\
\hline 1 & 0 & 1.0 \\
2 & 0.25 & 0.941 \\
3 & 0.5 & 0.8 \\
4 & 0.75 & 0.64 \\
\hline 5 & 1 & 0.5 \\
\hline
\end{array}
$$
By Simpson's Rule
$$
\begin{array}{l}
\int_{0}^{1} \frac{d x}{1+x^{2}}=\frac{1}{4 \times 3} \\
\quad[(1+0.5)+4(0.941+0.64)+2(0.8)] \\
=\frac{1}{12}[9.424]=0.785
\end{array}
$$

</details>

---

### Q17. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `3`

If $\int_{0}^{1} \tan ^{-1} x d x=p$, then the value of $\int_{0}^{1} \tan ^{-1}\left(\frac{1-x}{1+x}\right) d x$ is

**Options:**

- **(A)** $\frac{\pi}{4}+p$
- **(B)** $\frac{\pi}{4}-p$
- **(C)** $1+p$
- **(D)** $1-p$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\pi}{4}-p$**

**Detailed Solution:**

$\begin{aligned} \int_{0}^{1}\left(\frac{1-x}{1+x}\right.&) d x \\ &=\int_{0}^{1}\left[\tan ^{-1}(1)-\tan ^{-1}(x)\right] d x \\ &=\int_{0}^{1} \frac{\pi}{4} d x-\int_{0}^{1} \tan ^{-1}(x) d x \\ &=\frac{\pi}{4}-p \end{aligned}$

</details>

---

### Q18. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

Which of the following is true?

**Options:**

- **(A)** $\int_{0}^{1} e^{x} d x=e$
- **(B)** $\int_{0}^{1} 2^{x} d x=\log 2$
- **(C)** $\int_{0}^{1} \sqrt{x} d x=\frac{2}{3}$
- **(D)** $\int_{0}^{1} x d x=\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\int_{0}^{1} \sqrt{x} d x=\frac{2}{3}$**

**Detailed Solution:**

$\int_{0}^{1} e^{x} d x=\left[e^{x}\right]_{0}^{1}=e-1$
(b) $\int_{0}^{1} 2^{x} d x=\left[\frac{2^{x}}{\log _{e} 2}\right]_{0}^{1}=\frac{1}{\log 2} \cdot\left(2-2^{0}\right)=\frac{1}{\log 2}$
(c) $\int_{0}^{1} \sqrt{x} d x=\left[\frac{x^{3 / 2}}{3 / 2}\right]_{0}^{1}=\frac{2}{3}$
(d) $\int_{0}^{1} x d x=\left[\frac{x^{2}}{2}\right]_{0}^{1}=\frac{1}{2}$

</details>

---

### Q19. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

By Simpson's rule, the value of $\int_{1}^{2} \frac{d x}{x}$ dividing the interval (1, 2) into four equal parts, is

**Options:**

- **(A)** $0.6932$
- **(B)** $0.6753$
- **(C)** $0.6692$
- **(D)** $7.1324$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.6932$**

**Detailed Solution:**

$\quad \begin{aligned} h=\frac{2-1}{4} &=\frac{1}{4} \\ \text { Now, } x_{0} &=1, x_{1}=1+\frac{1}{4}, x_{2}=1+2 \times \frac{1}{4}, \\ x_{3} &=1+3 \times \frac{1}{4}, x_{4}=1+4 \times \frac{1}{4} \end{aligned}$
$$
\text { ie, } \begin{aligned}
x_{0} &=1, x_{1}=1.25, x_{2}=1.5, x_{3} \\
&=1.75, x_{4}=2 \\
\Rightarrow \quad y_{0} &=1, y_{1}=0.8, y_{2}=0.667, y_{3} \\
&=0.571, y_{4}=0.5
\end{aligned}
$$
$\therefore$ Using Simpson's $\frac{1}{3}$ rd rule
$$
\begin{aligned}
\int_{1}^{2} \frac{d x}{x}=& \frac{1}{12}[(1+0.5)+4(0.8+0.571)\\
&+2(0.667)] \\
=& \frac{1}{12}[1.5+5.484+1.334] \\
=& \frac{1}{12}[8.318]=0.6932
\end{aligned}
$$

</details>

---

### Q20. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

Considering four sub-intervals, the value of $\int_{0}^{1} \frac{1}{1+x} d x$ by Trapezoidal rule, is

**Options:**

- **(A)** $0.6870$
- **(B)** $0.6677$
- **(C)** $0.6977$
- **(D)** $0.5970$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.6977$**

**Detailed Solution:**

\begin{array}{c|l|l}
\hline \boldsymbol{i} & \boldsymbol{x}_{\boldsymbol{i}} & \boldsymbol{y}_{\boldsymbol{i}}=\frac{\mathbf{1}}{\mathbf{1 +} \boldsymbol{x}_{\boldsymbol{i}}} \\
\hline 0 & 0 & 1 \\

1 & 0.25 & 0.8 \\

2 & 0.5 & 0.67 \\

3 & 0.75 & 0.571 \\

4 & 1 & 0.5 \\
\hline
\end{array}
Trapezoidal rule gives
$\begin{aligned} \int_{0}^{1} \frac{1}{1+x} d x=& \frac{h}{2}\left[y_{0}+2\left(y_{1}+y_{2}+y_{3}\right)+y_{4}\right] \\=& \frac{1-0}{2 \times 4}[1+2(0.8+0.67\\ & \\=& 0.6977 \end{aligned}$

</details>

---

### Q21. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

By the application of Simpson's one-third rule for numerical integration, with two subintervals, the value of $\int_{0}^{1} \frac{d x}{1+x}$ is

**Options:**

- **(A)** $\frac{17}{36}$
- **(B)** $\frac{17}{25}$
- **(C)** $\frac{25}{36}$
- **(D)** $\frac{17}{24}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{25}{36}$**

**Detailed Solution:**

Since, the given integration is divided into two subintervals.
ie,
$$
h=\frac{1-0}{2}=\frac{1}{2}
$$
$$
\therefore \quad \int_{0}^{1} \frac{1}{1+x} d x=\frac{h}{3}\left[\left(y_{0}+y_{2}\right)+4\left(y_{1}\right)\right]
$$
At
$$
\begin{aligned}
x=0, y &=1 \\
x &=\frac{1}{2}, y_{1}=\frac{2}{3}
\end{aligned}
$$
and
$$
x=1, y_{2}=\frac{1}{2}
$$
$$
\begin{aligned}
\therefore \int_{0}^{1} \frac{1}{1+x} d x &=\frac{1}{2 \cdot 3}\left[\left(1+\frac{1}{2}\right)+4\left(\frac{2}{3}\right)\right] \\
&=\frac{1}{6}\left[\frac{3}{2}+\frac{8}{3}\right]=\frac{25}{36}
\end{aligned}
$$

</details>

---

### Q22. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int_{0}^{1} \tan ^{-1}\left(\frac{2 x-1}{1+x-x^{2}}\right) d x$ is

**Options:**

- **(A)** 1
- **(B)** 0
- **(C)** $-1$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

Let $\begin{aligned} I &=\int_{0}^{1} \tan ^{-1}\left(\frac{2 x-1}{1+x-x^{2}}\right) d x \\ &=\int_{0}^{1} \tan ^{-1}\left(\frac{x+x-1}{1-x(x-1)}\right) d x \\ &=\int_{0}^{1} \tan ^{-1} x d x+\int_{0}^{1} \tan ^{-1}(x-1) d x \\ &=\int_{0}^{1} \tan ^{-1} x d x+\int_{0}^{1} \tan ^{-1}(1-x-1) d x \\ &=\int_{0}^{1} \tan ^{-1} x d x-\int_{0}^{1} \tan ^{-1} x d x=0 \end{aligned}$

</details>

---

