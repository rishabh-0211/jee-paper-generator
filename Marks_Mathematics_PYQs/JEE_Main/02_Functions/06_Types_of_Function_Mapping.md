# JEE Main Mathematics - Functions

## Topic 6: Types of Function (Mapping)

**Total Questions:** 57

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be defined as $f(x) = \dfrac{2x^2 - 3x + 2}{3x^2 + x + 3}$. Then $f$ is :

**Options:**

- **(A)** both one-one and onto
- **(B)** one-one but not onto
- **(C)** onto but not one-one
- **(D)** neither one-one nor onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) neither one-one nor onto**

**Detailed Solution:**

Given $f(x) = \dfrac{2x^2 - 3x + 2}{3x^2 + x + 3}$

To check for one-one, let $f(x) = f(y)$

$\dfrac{2x^2 - 3x + 2}{3x^2 + x + 3} = \dfrac{2y^2 - 3y + 2}{3y^2 + y + 3}$

Cross-multiplying and simplifying, we get:

$11x^2y - 11xy^2 - 11x + 11y = 0$

$11xy(x - y) - 11(x - y) = 0$

$11(x - y)(xy - 1) = 0$

This implies $x = y$ or $xy = 1$.

Since $f(x) = f(1/x)$ for $x \neq 0$ (for example, $f(2) = f(1/2) = \dfrac{4}{17}$), the function is many-one (not one-one).

To check for onto, let $y = \dfrac{2x^2 - 3x + 2}{3x^2 + x + 3}$

$(3y - 2)x^2 + (y + 3)x + (3y - 2) = 0$

For $x \in \mathbb{R}$, the discriminant $D \ge 0$:

$(y + 3)^2 - 4(3y - 2)^2 \ge 0$

$(y + 3 - 6y + 4)(y + 3 + 6y - 4) \ge 0$

$(7 - 5y)(7y - 1) \ge 0$

$(5y - 7)(7y - 1) \le 0$

$y \in \left[\dfrac{1}{7}, \dfrac{7}{5}\right]$

Since the range is a proper subset of the codomain $\mathbb{R}$, the function is not onto.

Thus, $f$ is neither one-one nor onto.

Answer: neither one-one nor onto

</details>

---

### Q2. JEE Main 2026 (05 April Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $A = \{1, 2, 3, 4, 5, 6\}$. The number of one-one functions $f: A \rightarrow A$ such that $f(1) \geq 3$, $f(3) \leq 4$ and $f(2) + f(3) = 5$, is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **72**

**Detailed Solution:**

Given $A = \{1, 2, 3, 4, 5, 6\}$. Since $f: A \rightarrow A$ is a one-one function, $f(x)$ takes distinct values from $A$ for each $x \in A$.

We are given the condition $f(2) + f(3) = 5$. The possible pairs for $(f(2), f(3))$ from the set $A$ are:
$(1, 4), (2, 3), (3, 2), (4, 1)$

Notice that for all these pairs, the condition $f(3) \leq 4$ is automatically satisfied.

We also have the condition $f(1) \geq 3$. Since $f$ is one-one, $f(1)$ cannot take the values already assigned to $f(2)$ and $f(3)$. Let us find the number of choices for $f(1)$ in each case:

Case 1: $(f(2), f(3)) = (1, 4)$
$f(1) \geq 3$ and $f(1) \notin \{1, 4\} \Rightarrow f(1) \in \{3, 5, 6\}$. (3 choices)

Case 2: $(f(2), f(3)) = (2, 3)$
$f(1) \geq 3$ and $f(1) \notin \{2, 3\} \Rightarrow f(1) \in \{4, 5, 6\}$. (3 choices)

Case 3: $(f(2), f(3)) = (3, 2)$
$f(1) \geq 3$ and $f(1) \notin \{3, 2\} \Rightarrow f(1) \in \{4, 5, 6\}$. (3 choices)

Case 4: $(f(2), f(3)) = (4, 1)$
$f(1) \geq 3$ and $f(1) \notin \{4, 1\} \Rightarrow f(1) \in \{3, 5, 6\}$. (3 choices)

In each of the 4 cases, there are exactly 3 choices for $f(1)$.

After assigning values to $f(1), f(2),$ and $f(3)$, there are exactly 3 elements left in the codomain to be assigned to $f(4), f(5),$ and $f(6)$. Since $f$ is one-one, these can be assigned in $3! = 6$ ways.

Total number of such functions = (Number of pairs) $\times$ (Choices for $f(1)$) $\times$ (Arrangements for remaining elements)
Total = $4 \times 3 \times 6 = 72$

Answer: $72$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of functions $f: \{1, 2, 3, 4\} \rightarrow \{a, b, c\}$, which are not onto, is:

**Options:**

- **(A)** $48$
- **(B)** $45$
- **(C)** $51$
- **(D)** $35$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $45$**

**Detailed Solution:**

Total number of functions from a set of $4$ elements to a set of $3$ elements is $3^4 = 81$.

The number of onto functions is given by the inclusion-exclusion principle:

$3^4 - ^{3}C_{1} 2^4 + ^{3}C_{2} 1^4$

$= 81 - 3 \times 16 + 3 \times 1$

$= 81 - 48 + 3 = 36$

The number of functions which are not onto is the total number of functions minus the number of onto functions:

$81 - 36 = 45$

Answer: $45$

</details>

---

### Q4. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given below are two statements:
<b>Statement I:</b> The function $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=\frac{x}{1+|x|}$ is one-one.
<b>Statement II:</b> The function $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=\frac{x^{2}+4 x-30}{x^{2}-8 x+18}$ is many-one. 
 In the light of the above statements, choose the correct answer from the options given below :

**Options:**

- **(A)** Both Statement I and Statement II are true
- **(B)** Statement I is true but Statement II is false
- **(C)** Statement I is false but Statement II is true
- **(D)** Both Statement I and Statement II are false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both Statement I and Statement II are true**

**Detailed Solution:**

Statement I: $f(x) = \frac{x}{1+|x|}$. For $x \geq 0$, $f(x) = \frac{x}{1+x}$ is strictly increasing. For $x < 0$, $f(x) = \frac{x}{1-x}$ with $f'(x) = \frac{1}{(1-x)^2} > 0$, also strictly increasing. The function is continuous at $x = 0$, so $f$ is strictly increasing on $\mathbb{R}$ and hence one-one. Statement I is true.
Statement II: $f(x) = \frac{x^2+4x-30}{x^2-8x+18}$. The denominator $(x-4)^2 + 2 > 0$ for all $x$.
$f'(x) = \frac{-12(x^2 - 8x + 14)}{(x^2 - 8x + 18)^2}$
$f'(x) = 0 \Rightarrow x = 4 \pm \sqrt{2}$. Since $f'$ changes sign, $f$ is not monotonic and hence many-one. Statement II is true.
Both statements are true.

</details>

---

### Q5. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Consider two sets $\mathrm{A}=\{x \in \mathrm{Z}:|(|x-3|-3)| \leq 1\}$ and $\mathrm{B}=\left\{x \in \mathbb{R}-\{1,2\}: \frac{(x-2)(x-4)}{x-1} \log _{e}(|x-2|)=0\right\}$. Then the number of onto functions $f: \mathrm{A} \rightarrow \mathrm{B}$ is equal to

**Options:**

- **(A)** 32
- **(B)** 79
- **(C)** 62
- **(D)** 81

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 62**

**Detailed Solution:**

For set $A$:
 $|(|x-3|-3)| \le 1 \Rightarrow 2 \le |x-3| \le 4$.
If $x \ge 3$: $5 \le x \le 7 \Rightarrow x \in \{5,6,7\}$.
If $x < 3$: $-1 \le x \le 1 \Rightarrow x \in \{-1,0,1\}$.
So $A = \{-1,0,1,5,6,7\}$, $|A|=6$.
For set $B$:
 $\frac{(x-2)(x-4)}{x-1}\log_e(|x-2|) = 0$ with $x \in \mathbb{R}-\{1,2\}$.
Either $\frac{(x-2)(x-4)}{x-1}=0 \Rightarrow x=4$ (since $x \neq 1,2$), or $\log_e|x-2|=0 \Rightarrow |x-2|=1 \Rightarrow x=3$ (since $x \neq 1$).
So $B = \{3,4\}$, $|B|=2$.
Number of onto functions from $A$ to $B$ $= 2^6 - 2 = 62$.

</details>

---

### Q6. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider the sets $\mathrm{A}=\left\{(\mathrm{x}, \mathrm{y}) \in \mathbb{R} \times \mathbb{R}: \mathrm{x}^2+\mathrm{y}^2=25\right\}$, $\mathrm{B}=\left\{(\mathrm{x}, \mathrm{y}) \in \mathbb{R} \times \mathbb{R}: \mathrm{x}^2+9 \mathrm{y}^2=144\right\}, \mathrm{C}=\{(\mathrm{x}, \mathrm{y})$ $\left.\in \mathbb{Z} \times \mathbb{Z}: x^2+y^2 \leq 4\right\}$, and $D=A \cap B$. The total number of one-one functions from the set D to the set C is:

**Options:**

- **(A)** 15120
- **(B)** 19320
- **(C)** 17160
- **(D)** 18290

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 17160**

**Detailed Solution:**

$\mathrm{A}: \mathrm{x}^2+\mathrm{y}^2=25...(i)$
B : $\frac{x^2}{144}+\frac{y^2}{16}=1...(ii)$
C: $x^2+y^2 \leq 4...(iii)$
Solve (1) \& (2)
$\begin{aligned}
& x^2+9\left(25-x^2\right)=144 \\
& -8 x^2=144-225=-81 \\
& x= \pm \frac{9}{2 \sqrt{2}}
\end{aligned}$
$\operatorname{By}(1) \Rightarrow y= \pm \sqrt{25-x^2}$
$= \pm \sqrt{25-\frac{81}{8}}= \pm \frac{\sqrt{119}}{2 \sqrt{2}}$
$\therefore \mathrm{D}=\mathrm{A} \cap \mathrm{~B}=$
$\left\{\left(\frac{9}{2 \sqrt{2}}, \frac{\sqrt{119}}{2 \sqrt{2}}\right),\left(\frac{9}{2 \sqrt{2}},-\frac{\sqrt{119}}{2 \sqrt{2}}\right),\left(\frac{-9}{2 \sqrt{2}}, \frac{\sqrt{119}}{2 \sqrt{2}}\right),\left(\frac{-9}{2 \sqrt{2}}, \frac{-\sqrt{119}}{2 \sqrt{2}}\right)\right\}$
No. of elements in set $D=4$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hiM-DfQup4kp5DeFXCKLYfKiRDKdXweZmUqd6gSXHx8.original.fullsize.png"/>
$\begin{aligned}
& \because C=\left\{(x, y) \in \mathrm{Z} \times \mathrm{Z}: \mathrm{x}^2+\mathrm{y}^2 \leq 4\right\} \\
& =\{(0,2),(2,0),(0,-2),(-2,0),(1,1),(-1,-1), \\
& (1,-1),(-1,1),(1,0),(0,1),(-1,0),(0,-1), \\
& (0,0)\}
\end{aligned}$
No. of elements in set $\mathrm{C}=13$
Total no. of one-one function from
Set $D$ to $\sec C \Rightarrow 13 \times 12 \times 11 \times 10=17160$

</details>

---

### Q7. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f:[0,3] \rightarrow$ A be defined by $f(x)=2 x^3-15 x^2+36 x+7$ and $g:[0, \infty) \rightarrow B$ be defined by $\mathrm{g}(x)=\frac{x^{2025}}{x^{2025}+1}$. If both the functions are onto and $\mathrm{S}=\{x \in \mathbf{Z}: x \in \mathrm{~A}$ or $x \in \mathrm{~B}\}$, then $\mathrm{n}(\mathrm{S})$ is equal to :

**Options:**

- **(A)** $29$
- **(B)** $30$
- **(C)** $31$
- **(D)** $36$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $30$**

**Detailed Solution:**

as $f(x)$ is onto hence $A$ is range of $f(x)$
$\begin{aligned}
& \text { now } \begin{array}{l}
\mathrm{f}^{\prime}(\mathrm{x})=6 \mathrm{x}^2-30 \mathrm{x}+36 \\
\quad=6(\mathrm{x}-2)(\mathrm{x}-3) \\
\quad \mathrm{f}(2)=16-60+72+7=35 \\
\mathrm{f}(3)=54-135+108+7=34 \\
\mathrm{f}(0)=7
\end{array}
\end{aligned}$
hence range $\in[7,35]=\mathrm{A}$
also for range of $g(x)$
$\begin{aligned}
& g(x)=1-\frac{1}{x^{2025}+1} \in[0,1)=B \\
& s=\{0,7,8, \ldots .35\} \text { hence } n(s)=30
\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\text { The function } f:(-\infty, \infty) \rightarrow(-\infty, 1) \text {, defined by } f(x)=\frac{2^x-2^{-x}}{2^x+2^{-x}} \text { is : }$

**Options:**

- **(A)** $\text { Neither one-one nor onto }$
- **(B)** $\text { Onto but not one-one }$
- **(C)** $\text { Both one-one and onto }$
- **(D)** $\text { One-one but not onto }$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\text { One-one but not onto }$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(\mathrm{x})=\frac{2^{2 \mathrm{x}}-1}{2^{2 \mathrm{x}}+1} \\
& =1-\frac{2}{2^{2 \mathrm{x}}+1} \\
& \mathrm{f}^{\prime}(\mathrm{x})=\frac{2}{\left(2^{2 \mathrm{x}}+1\right)^2} \cdot 2.2^{2 \mathrm{x}} \cdot \ln 2 \text { i.e always }+\mathrm{ve}
\end{aligned}$
so $f(x)$ is $\uparrow$ function
$\begin{aligned}
& \therefore \mathrm{f}(-\infty)=-1 \\
& \mathrm{f}(\infty)=1 \\
& \therefore \mathrm{f}(\mathrm{x}) \in(-1,1) \neq \text { co-domain }
\end{aligned}$
so function is one-one but not onto

</details>

---

### Q9. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{A}=\{1,2,3,4\}$ and $\mathrm{B}=\{1,4,9,16\}$. Then the number of many-one functions $f: \mathrm{A} \rightarrow \mathrm{B}$ such that $1 \in f(\mathrm{~A})$ is equal to :

**Options:**

- **(A)** 151
- **(B)** 139
- **(C)** 163
- **(D)** 127

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 151**

**Detailed Solution:**

$\begin{aligned}
& A=\{1,2,3,4\} \\
& B=\{1,4,9,16\}
\end{aligned}$

Total number of functions $=4^4$
Total number of one-one functions $=4!$
Total number of many one functions $=4^4-4!=232$
Total number of many-one functions in which $1 \notin f(A)=3 \times 3 \times 3 \times 3=81$
$\therefore$ Total number of many one functions $1 \notin f(A)$
$\begin{aligned}
& =232-81 \\
& =151
\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $A=\{(x, y): 2 x+3 y=23, x, y \in \mathbb{N}\}$ and $B=\{x:(x, y) \in A\}$. Then the number of one-one functions from $A$ to $B$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

$\begin{array}{ll}
2 x+3 y=23 \\
x=1 & y=7 \\
x=4 & y=5 \\
x=7 & y=3 \\
x=10 & y=1 \\
A & B \\
(1,7) & 1 \\
(4,5) & 4 \\
(7,3) & 7 \\
(10,1) & 10
\end{array}$
The number of one-one functions from $A$ to $B$ is equal to 4 !

</details>

---

### Q11. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=\left\{\begin{array}{ccc}-\mathrm{a} & \text { if } & -\mathrm{a} \leq x \leq 0 \\ x+\mathrm{a} & \text { if } & 0 < x \leq \mathrm{a}\end{array}\right.$ where $\mathrm{a}>0$ and $\mathrm{g}(x)=(f(x \mid)-|f(x)|) / 2$.
Then the function $g:[-a, a] \rightarrow[-a, a]$ is

**Options:**

- **(A)** neither one-one nor onto.
- **(B)** onto.
- **(C)** both one-one and onto.
- **(D)** one-one.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) neither one-one nor onto.**

**Detailed Solution:**

$y=f(x)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/w518Vp-1wvOhnmhK-44wc-GezcELscgNsUNfj1NU0t8.original.fullsize.png">
$y=f|x|$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZDyQUL79sZm7svDWvTumQrxAgOYRVxfSgEdHpJEYcRM.original.fullsize.png">
$y=|f(x)|$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/m-oXVi36JbqgZ3kaw4crKu4B3rz3viDY2Mptq-qD8DU.original.fullsize.png">
$g(x)=\frac{f(|x|)-|f(x)|}{2}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BqtHmA1OHZJf8vQ2KHdVImbfOGvxqdUQp4d0yzqAzlw.original.fullsize.png">

</details>

---

### Q12. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $[t]$ be the greatest integer less than or equal to $t$. Let $A$ be the set of all prime factors of 2310 and $f: A \rightarrow \mathbb{Z}$ be the function $f(x)=\left[\log _2\left(x^2+\left[\frac{x^3}{5}\right]\right)\right]$. The number of one-to-one functions from $A$ to the range of $f$ is

**Options:**

- **(A)** 25
- **(B)** 24
- **(C)** 20
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 120**

**Detailed Solution:**

$\mathrm{N}=2310=231 \times 10$
$=3 \times 11 \times 7 \times 2 \times 5$
$A=\{2,3,5,7,11\}$
$\begin{aligned} & f(x)=\left[\log _2\left(x^2+\left[\frac{x^3}{5}\right]\right)\right] \\ & f(2)=\left[\log _2(5)\right]=2 \\ & f(3)=\left[\log _2(14)\right]=3 \\ & f(5)=\left[\log _2(25+25)\right]=5 \\ & f(7)=\left[\log _2(117)\right]=6 \\ & f(11)=\left[\log _2 387\right]=8\end{aligned}$
Range of $f: B=\{2,3,5,6,8\}$
No. of one-one functions $=5 !=120$

</details>

---

### Q13. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The function $\text { f: R->R, }$ $f(x)=\frac{x^2+2 x-15}{x^2-4 x+9}, x \in \mathbb{R}$ is

**Options:**

- **(A)** one-one but not onto.
- **(B)** both one-one and onto.
- **(C)** onto but not one-one.
- **(D)** neither one-one nor onto.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) neither one-one nor onto.**

**Detailed Solution:**

$f(x)=\frac{(x+5)(x-3)}{x^2-4 x+9}$
$\begin{aligned} & \text { Let } g(x)=x^2-4 x+9 \\ & D < 0 \\ & g(x)>0 \text { for } x \in R\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/xvg6zGx0EutEzhHBqBY86HrL5SdQuHK6DMjQsX8fZuo.original.fullsize.png">
$\therefore\left[\begin{array}{l}
\mathrm{f}(-5)=0 \\
\mathrm{f}(3)=0
\end{array}\right.$
So, $\mathrm{f}(\mathrm{x})$ is many-one.
again,
$\begin{aligned}
& y x^2-4 x y+9 y=x^2+2 x-15 \\
& x^2(y-1)-2 x(2 y+1)+(9 y+15)=0 \\
& \text { for } \forall x \in R \Rightarrow D \geq 0 \\
& D=4(2 y+1)^2-4(y-1)(9 y+15) \geq 0 \\
& 5 y^2+2 y+16 \leq 0 \\
& (5 y-8)(y+2) \leq 0
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EIgqBDcNF1gfTLCKXkTOTFPOo1QFUGGPSbQSFvFVjrI.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/iSt6LrXnj_nKQvULE-hm-VpSv3-9jyNWkTTIBAhgvrk.original.fullsize.png">

</details>

---

### Q14. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $A=\{1,3,7,9,11\}$ and $B=\{2,4,5,7,8,10,12\}$. Then the total number of one-one maps $f: \mathrm{A} \rightarrow \mathrm{B}$, such that $f(1)+f(3)=14$, is :

**Options:**

- **(A)** 480
- **(B)** 240
- **(C)** 120
- **(D)** 180

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 240**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ualR7H5WOb_9GPKPhCt_4ijnviD9CzPasGitjg9u5bs.original.fullsize.png">
$\begin{aligned}
& A=\{1,3,7,9,11\} \\
& B=\{2,4,5,7,8,10,12\} \\
& f(1)+f(3)=14
\end{aligned}$
(i) $2+12$
(ii) $4+10$
$2 \times(2 \times 5 \times 4 \times 3)=240$

</details>

---

### Q15. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&gt;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>≤</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>≥</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&lt;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>R</mi></math> is:</p>

**Options:**

- **(A)** one-one but not onto
- **(B)** neither one-one nor onto
- **(C)** onto but not one-one
- **(D)** both one-one and onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) neither one-one nor onto**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>&gt;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>≤</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mi>x</mi><mo>,</mo></mtd><mtd><mi>x</mi><mo>≥</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo></mtd><mtd><mi>x</mi><mo>&lt;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>,</mo></mtd><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>≥</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mi>e</mi><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></msup><mo>,</mo></mtd><mtd><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&lt;</mo><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>,</mo></mtd><mtd><mfenced close="]"><mrow><mo>−</mo><mi>∞</mi><mo>,</mo><mn>0</mn></mrow></mfenced></mtd></mtr><mtr><mtd><msup><mi>e</mi><mrow><mi>log</mi><mi>x</mi></mrow></msup><mo>,</mo></mtd><mtd><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mi>log</mi><mi>x</mi><mo>,</mo></mtd><mtd><mfenced open="["><mrow><mn>1</mn><mo>,</mo><mi>∞</mi></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p>Graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is given below:</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/eea7419f-4666-4b28-a69e-2a66cbeb3dc2.png" style="width: 320px; height: 207px;"/></p><p>Range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mo>[</mo><mn>0</mn><mo>,</mo><mo>∞</mo><mo>)</mo><mo>≠</mo></math>Codomain</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is many-one and into.</p>

</details>

---

### Q16. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close=""><mfenced close="]" open=""><mrow><mo>−</mo><mi>∞</mi><mo>,</mo><mo>−</mo><mn>1</mn></mrow></mfenced></mfenced><mo>→</mo><mfenced close="]" open=""><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></mfenced></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></msup></math> is one-one and onto, then the distance of the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mi>b</mi><mo>+</mo><mn>4</mn><mo>,</mo><mo> </mo><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math> from the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>3</mn></mrow></msup><mi>y</mi><mo>=</mo><mn>4</mn></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup></msqrt></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>×</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mo>×</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>×</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>×</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mo>(</mo><mo>-</mo><mo>∞</mo><mo>,</mo><mo>-</mo><mn>1</mn><mo>]</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>&gt;</mo><mn>0</mn></math>, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing function in given domain,</p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mo>-</mo><mo>∞</mo></mrow></munder><mfenced><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>2</mn><mi>b</mi><mo>+</mo><mn>4</mn><mo>,</mo><mo> </mo><mi>a</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>≡</mo><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><mn>4</mn><mo>,</mo><mo> </mo><mn>2</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fee53ad0-c982-4d34-9163-0303b3b516c9.png" style="width: 280px; height: 152px;"/></p><p>Now, finding the distance from the given line we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>−</mo><mn>3</mn></mrow></msup><mo>−</mo><mn>4</mn></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>6</mn></mrow></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>3</mn></mrow></msup></mrow></mfenced></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>6</mn></mrow></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfrac><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>6</mn></mrow></msup></mrow></mfenced></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>6</mn></mrow></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>6</mn></mrow></msup></msqrt></mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mn>2</mn><msqrt><mfrac><mn>1</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup></mfrac><mo>+</mo><mn>1</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>=</mo><mn>2</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup></msqrt></math></p>

</details>

---

### Q17. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>…</mo><mo>.</mo><mn>7</mn><mo>}</mo></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo> </mo></math>denote the power set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. If the number of functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>→</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>∈</mo><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo><mo>,</mo><mo>∀</mo><mi>a</mi><mo>∈</mo><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>m</mi><mi>n</mi></msup><mo>,</mo><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>∈</mo><mi>N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is least, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **44**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>…</mo><mo>.</mo><mn>7</mn><mo>}</mo></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>→</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>∈</mo><mi>A</mi></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>∈</mo><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo></math>, that means <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>‘</mo><mi>a</mi><mo>’</mo></math> will be the element of subset as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>→</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo></math>,</p><p>Now, total options for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>6</mn></msup></math>. (Because <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>6</mn></msup></math> subsets contains elements<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>)</p><p>Similarly, for every other element we get, total  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>6</mn></msup><mo>×</mo><msup><mn>2</mn><mn>6</mn></msup><mo>×</mo><msup><mn>2</mn><mn>6</mn></msup><mo>×</mo><msup><mn>2</mn><mn>6</mn></msup><mo>×</mo><msup><mn>2</mn><mn>6</mn></msup><mo>×</mo><msup><mn>2</mn><mn>6</mn></msup><mo>×</mo><msup><mn>2</mn><mn>6</mn></msup><mo>=</mo><msup><mn>2</mn><mn>42</mn></msup></math> subsets.</p><p>Now, comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>m</mi><mi>n</mi></msup></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>2</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mi>n</mi><mo>=</mo><mn>42</mn></math></p><p>Hence,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>42</mn><mo>=</mo><mn>44</mn></math></p>

</details>

---

### Q18. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>:</mo><mi mathvariant="normal">N</mi><mo>-</mo><mo>{</mo><mn>1</mn><mo>}</mo><mo>→</mo><mi mathvariant="normal">N</mi></math>; defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi mathvariant="normal">n</mi></mfenced><mo>=</mo></math> the highest prime factor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>, is :

**Options:**

- **(A)** both one-one and onto
- **(B)** one-one only
- **(C)** onto only
- **(D)** neither one-one nor onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) neither one-one nor onto**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">f</mi><mo>:</mo><mi mathvariant="normal">N</mi><mo>-</mo><mo>{</mo><mn>1</mn><mo>}</mo><mo>→</mo><mi mathvariant="normal">N</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>=</mo></math> The highest prime factor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>.</p><p>Since, the only prime factor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>2</mn></math></p><p>Also, factors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo> </mo><mtext>and</mtext><mo> </mo><mn>4</mn></math>. Out of these, the highest prime factor is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mn>2</mn></math></p><p>Similarly the highest prime factor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>,</mo><mo> </mo><mn>32</mn><mo>,</mo><mo> </mo><mn>64</mn><mo>,</mo><mo> </mo><mn>128</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p>So, the given function is many one.</p><p>Now, no composite number will be image of any number.</p><p>Example: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> is not image of any element</p><p>So, the given function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is into.</p><p>Hence many one and into</p><p>Or, neither one-one nor onto.</p>

</details>

---

### Q19. JEE Main 2023 (11 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>. Then the number of functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>B</mi></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>-</mo><mn>1</mn></math> is equal to........

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **360**

**Detailed Solution:**

<p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mi>f</mi><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#8804;</mo><mn>5</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo>&#160;</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>&#8804;</mo><mn>6</mn></mrow></mfenced></math> </p><p>Now taking cases we get,</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#8594;</mo><mn>4</mn><mo>&#160;</mo><mtext>mappings</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>mappings</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mn>2</mn><mo>&#160;</mo><mtext>mappings</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfenced open="{" close="}"><mn>1</mn></mfenced><mo>&#8594;</mo><mn>1</mn><mo>&#160;</mo><mtext>mappings</mtext></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>6</mn></mfenced><mo>&#8594;</mo><mn>6</mn><mo>&#160;</mo><mtext>mapping&#160;each</mtext></math></p><p>So, total number of function will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>4</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>360</mn></math></p>

</details>

---

### Q20. JEE Main 2023 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>,</mo><mi>e</mi><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math>. Total number of onto functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>S</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo><mo>&#8800;</mo><mn>1</mn></math>, is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **180**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>,</mo><mi>e</mi><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4c69d607-8e05-4bc5-b412-17ee243b9b0d-image.png" style="width: 227px; height: 171px;" /></p><p>Now taking, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo><mo>=</mo><mn>1</mn></math> we get, one of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>b</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>c</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>d</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>e</mi><mo>)</mo><mo>=</mo><mn>1</mn></math> then total such cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#183;</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>24</mn></math>
Now if, only <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo><mo>=</mo><mn>1</mn></math>, then we have distribute <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> amongst <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>,</mo><mi>e</mi></mrow></mfenced></math>,
So, total cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><mn>4</mn></msup><mo>-</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>4</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>&#183;</mo><mn>1</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn></math>
So, number of onto functions when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>a</mi><mo>)</mo><mo>=</mo><mn>1</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>+</mo><mn>36</mn><mo>=</mo><mn>60</mn></math></p><p>Now finding, total number of onto functions,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>4</mn><mn>5</mn></msup><mo>-</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#183;</mo><msup><mn>3</mn><mn>5</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>5</mn></msup></mrow></mfenced><mo>-</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#183;</mo><mn>1</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1024</mn><mo>-</mo><mn>973</mn><mo>+</mo><mn>192</mn><mo>-</mo><mn>4</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>240</mn></math>
Number of required functions when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>&#8800;</mo><mn>1</mn></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>240</mn><mo>-</mo><mn>60</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>180</mn></math></p></blockquote>

</details>

---

### Q21. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>}</mo></math>. Then the number of possible functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>A</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>m</mi><mo>&#183;</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>m</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced></math> for every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi>A</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#183;</mo><mi>n</mi><mo>&#8712;</mo><mi>A</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **432**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>m</mi><mo>&#183;</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>m</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mrow><mn>1</mn><mo>&#183;</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>3</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>9</mn><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>&#215;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>9</mn></mfenced></mrow></mfenced></math> have two possibility <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>2</mn><mo>&#183;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math></p><p>Now here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced></math> can take all <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> numbers,</p><p>Similarly, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>8</mn></mfenced></math> there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> ways each,</p><p>So, total possible function will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>432</mn></math></p>

</details>

---

### Q22. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>}</mo></math>. Then the number of oneone functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>S</mi><mo>&#8594;</mo><mi>P</mi><mo>(</mo><mi>S</mi><mo>)</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>S</mi><mo>)</mo></math> denote the power set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>&#8834;</mo><mi>f</mi><mo>(</mo><mi>m</mi><mo>)</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#60;</mo><mi>m</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3240**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>}</mo></math>, then the number of one-one functions, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>S</mi><mo>&#183;</mo><mi>P</mi><mo>(</mo><mi>S</mi><mo>)</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>S</mi><mo>)</mo></math> denotes the power set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>&#60;</mo><mi>f</mi><mo>(</mo><mi>m</mi><mo>)</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#60;</mo><mi>m</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><mi>S</mi><mo>)</mo><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>S</mi></mfenced><mo>=</mo><mfenced open="{" close="}"><mtable><mtr><mtd><mi>&#981;</mi><mo>,</mo><mo>{</mo><mn>1</mn><mo>}</mo><mo>,</mo><mo>&#8230;</mo><mo>{</mo><mn>6</mn><mo>}</mo><mo>,</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>}</mo><mo>,</mo><mo>&#8230;</mo><mo>,</mo></mtd></mtr><mtr><mtd><mo>{</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>}</mo><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>}</mo></mtd></mtr></mtable></mfenced></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>5</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> choices</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo></math>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>  choices</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>  choices</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>  choices</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> or empty subset i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>  choices</p><p>Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>1080</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>6</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>5</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo></math> empty subset i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> option</p><p>Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>720</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>6</mn><mo>)</mo><mo>=</mo><mi>S</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>5</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>  choices</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> choices 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo></math>any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> </p><p> choices</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>  choices</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo></math> empty subset i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> option</p><p>Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>360</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>6</mn><mo>)</mo><mo>=</mo><mi>S</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>5</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> options,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> options,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo></math> empty subset i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> option
Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>360</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>6</mn><mo>)</mo><mo>=</mo><mi>S</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>5</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo></math>any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo></math> empty subset i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> option</p><p>Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>360</mn></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>6</mn><mo>)</mo><mo>=</mo><mi>S</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>5</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo></math> any <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> element subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>  choices
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo></math> empty subset i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> option</p><p>Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>360</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Number of such functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3240</mn></math></p>

</details>

---

### Q23. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math>. Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is many-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is many-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is one-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> but not in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math> is one-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is one-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> but not in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>-</mo><mo>(</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mn>2</mn><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><menclose notation="updiagonalstrike"><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></menclose><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><menclose notation="updiagonalstrike"><mn>2</mn><mi>x</mi></menclose><mo>+</mo><mn>2</mn><mo>-</mo><menclose notation="updiagonalstrike"><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></menclose><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><menclose notation="updiagonalstrike"><mn>2</mn><mi>x</mi></menclose></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mn>2</mn><mo>(</mo><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>)</mo></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mn>2</mn><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1aeceb0e-b37a-4219-a0c3-430e2857e3e7-9895002_1a.PNG" style="width: 247px; height: 70px;" /></p><p>Clearly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is one-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> and also in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is not one-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p>

</details>

---

### Q24. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math>. Consider two statements</p><p>(I) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is an increasing function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>(II) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is one-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>
Then,</p>

**Options:**

- **(A)** Only (I) is true
- **(B)** Only (II) is true
- **(C)** Neither (I) nor (II) is true
- **(D)** Both (I) and (II) are true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Both (I) and (II) are true**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac><mo>-</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac></math></p><p>Now differentiating the above function with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> is always positive</p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is one-one in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q25. JEE Main 2022 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>, from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mi>N</mi><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>&#8804;</mo><mn>0</mn></mrow></mfenced></math> to the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>:</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></math>, for every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>A</mi></math>, is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1440**

**Detailed Solution:**

<blockquote><p>For set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>9</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>1</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>:</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8804;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>:</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#8804;</mo><mn>5</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>,</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>:</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#8804;</mo><mn>2</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><msup><mn>1</mn><mn>2</mn></msup></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mo>:</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>&#8804;</mo><mn>1</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><msup><mn>1</mn><mn>2</mn></msup></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn><mo>:</mo><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>&#8804;</mo><mn>2</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><msup><mn>1</mn><mn>2</mn></msup></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn><mo>:</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#8804;</mo><mn>5</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>,</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>6</mn><mo>:</mo><mi>f</mi><mfenced><mn>6</mn></mfenced><mo>&#8804;</mo><mn>10</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>,</mo><msup><mn>2</mn><mn>2</mn></msup><mo>,</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>7</mn><mo>:</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>7</mn></mfenced><mo>&#8804;</mo><mn>17</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>,</mo><msup><mn>2</mn><mn>2</mn></msup><mo>,</mo><msup><mn>3</mn><mn>2</mn></msup><mo>,</mo><msup><mn>4</mn><mn>2</mn></msup></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>8</mn><mo>:</mo><mi>f</mi><mfenced><mn>8</mn></mfenced><mo>&#8804;</mo><mn>26</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>,</mo><msup><mn>2</mn><mn>2</mn></msup><mo>,</mo><msup><mn>3</mn><mn>2</mn></msup><mo>,</mo><msup><mn>4</mn><mn>2</mn></msup><mo>,</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>9</mn><mo>:</mo><mi>f</mi><mfenced><mn>9</mn></mfenced><mo>&#8804;</mo><mn>37</mn><mo>&#8658;</mo><mi>B</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>,</mo><msup><mn>2</mn><mn>2</mn></msup><mo>,</mo><msup><mn>3</mn><mn>2</mn></msup><mo>,</mo><msup><mn>4</mn><mn>2</mn></msup><mo>,</mo><msup><mn>5</mn><mn>2</mn></msup><mo>,</mo><msup><mn>6</mn><mn>2</mn></msup></mrow></mfenced></math></p><p>Total number of such function</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>2</mn><mfenced><mn>720</mn></mfenced><mo>=</mo><mn>1440</mn></math></p></blockquote>

</details>

---

### Q26. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mi>g</mi><mo>:</mo><mi mathvariant="normal">&#8469;</mi><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8469;</mi></math> be functions defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi mathvariant="normal">a</mi></mfenced><mo>=</mo><mi>&#945;</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is the maximum of the powers of those primes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mi>&#945;</mi></msup></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mi>a</mi><mo>+</mo><mn>1</mn></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced></math>. Then, the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>+</mo><mi>g</mi></math> is

**Options:**

- **(A)** one-one but not onto
- **(B)** onto but not one-one
- **(C)** both one-one and onto
- **(D)** neither one-one nor onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) neither one-one nor onto**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mi>g</mi><mo>:</mo><mi>N</mi><mo>-</mo><mfenced close="}" open="{"><mn>1</mn></mfenced><mo>&#8594;</mo><mi>N</mi></math> defined as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mi>&#945;</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is the maximum power of those primes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mi>&#945;</mi></msup></math> divides a.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mi>a</mi><mo>+</mo><mn>1</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>3</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced><mrow><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced><mrow><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>g</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced><mrow><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>g</mi><mfenced><mn>5</mn></mfenced><mo>=</mo><mn>6</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced><mrow><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mfenced><mn>5</mn></mfenced><mo>=</mo><mn>7</mn></math></p><p>We can see <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mfenced><mn>5</mn></mfenced><mo>=</mo><mfenced><mrow><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mfenced><mn>4</mn></mfenced></math>, so<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>+</mo><mi>g</mi></math> is not one-one function</p><p>Now, again we can see <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>min</mi></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>g</mi><mi>min</mi></msub><mo>=</mo><mn>3</mn></math></p><p>So, there does not exist any <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>N</mi><mo>-</mo><mfenced close="}" open="{"><mn>1</mn></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mo>+</mo><mi>g</mi></math> is not onto</p><p>So function is neither one-one nor onto.</p></blockquote>

</details>

---

### Q27. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The number of bijective function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mo>&#8943;</mo><mo>,</mo><mn>99</mn></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>8</mn><mo>,</mo><mo>&#8943;</mo><mo>,</mo><mn>100</mn></mrow></mfenced></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>7</mn></mfenced><mo>&#8943;</mo><mo>&#62;</mo><mi>f</mi><mfenced><mn>99</mn></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>50</mn></mmultiscripts></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>50</mn></mmultiscripts></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>50</mn><mo>!</mo></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>50</mn></mmultiscripts><mo>&#215;</mo><mn>3</mn><mo>!</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>50</mn></mmultiscripts></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mo>&#8943;</mo><mo>,</mo><mn>99</mn></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>8</mn><mo>,</mo><mo>&#8943;</mo><mo>,</mo><mn>100</mn></mrow></mfenced></math></p><p>The number of elements in domain and codomain is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99</mn></math>.</p><p>Now, let us assume <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>100</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/313916fe-0c5f-412d-a252-42d6dc5764fb-acf71c03-cfeb-496b-a99b-532940d809da-image.png" style="width: 300px; height: 300px;" /></p><p>Now as per diagram we have only <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> way for arranging <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>7</mn></mfenced><mo>&#8943;</mo><mo>&#62;</mo><mi>f</mi><mfenced><mn>99</mn></mfenced></math>,</p><p>Similarly if we choose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>98</mn></math> then again we have only <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> way for arranging  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>7</mn></mfenced><mo>&#8943;</mo><mo>&#62;</mo><mi>f</mi><mfenced><mn>99</mn></mfenced></math>,</p><p>So we can see the arrangement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>7</mn></mfenced><mo>&#8943;</mo><mo>&#62;</mo><mi>f</mi><mfenced><mn>99</mn></mfenced></math> depends upon <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced></math>,</p><p>So number of ways for choosing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts></math></p></blockquote>

</details>

---

### Q28. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The total number of functions, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#8594;</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>3</mn></mfenced></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>126</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>3</mn></mfenced></math></p><p>Now possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> (it cannot be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> as minimum value <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn></math> )</p><p>For each <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mi>k</mi></math> then there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> set of values for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced></math></p><p>For example if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>3</mn></math> then possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> values </p><p>Similarly for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>4</mn></math>, possible values will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> values.</p><p>And so on.</p><p>So number of possible combinations of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>15</mn></math></p><p>And for each value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced></math> there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced></math>, so total cases will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>90</mn></math></p></blockquote>

</details>

---

### Q29. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>. Then the number of elements in the set {<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>S</mi><mo>&#215;</mo><mi>S</mi><mo>&#8594;</mo><mi>S</mi><mo>:</mo><mi>f</mi></math> is onto and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8805;</mo><mi>a</mi><mo>&#8704;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>S</mi><mo>&#215;</mo><mi>S</mi></math>} is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **37**

**Detailed Solution:**

<p>Finding the cases for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>&#8805;</mo><mi>a</mi></math> we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>- all have one choice for image.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>-</mo></math> all have three choices for image.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>-</mo></math>all have two choices for image.</p><p>So the total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>72</mn></math></p><p>Case 1: None of the pre-images have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> as image. </p><p>Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>4</mn></math></p><p>Case 2: None of the pre-images have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> as image</p><p>Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>32</mn></math></p><p>Case 3: None of the pre-images have either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> as image</p><p>Total functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total onto functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>72</mn><mo>-</mo><mn>4</mn><mo>-</mo><mn>32</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>37</mn></math></p>

</details>

---

### Q30. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The probability that a randomly chosen one-one function from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced></math> to the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> satisfied <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>d</mi></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>24</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>40</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>30</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>20</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>20</mn></mfrac></math>**

**Detailed Solution:**

<p>Total cases will be  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>5</mn></msup><msub><mi>C</mi><mn>4</mn></msub><mo>&#215;</mo><mn>4</mn><mo>!</mo></math></p><p>Now favourable cases for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>d</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>a</mi></mfenced></math> will be,</p><p>Case (I) if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>=</mo><mn>1</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>d</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>a</mi></mfenced></math> can take the value  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></math> respectively</p><p>Case (II) if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>=</mo><mn>2</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>d</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>a</mi></mfenced></math> can take value  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></math> respectively</p><p>Case (III) if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>=</mo><mn>3</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>d</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>a</mi></mfenced></math> can take value <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></math> respectively</p><p>So total favourable case will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></p><p>So probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>favourable</mi><mo>&#160;</mo><mi>cases</mi></mrow><mrow><mi>total</mi><mo>&#160;</mo><mi>outcomes</mi></mrow></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>6</mn><mrow><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>20</mn></mfrac></math></p>

</details>

---

### Q31. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8469;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8469;</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfenced close="" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn><mi>n</mi><mo>,</mo></mtd><mtd><mi>n</mi><mo>=</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>8</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></mtd></mtr><mtr><mtd><mi>n</mi><mo>-</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>n</mi><mo>=</mo><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>15</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></mtd></mtr><mtr><mtd><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo></mtd><mtd><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>13</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></mtd></mtr></mtable></mfenced></math>
then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is

**Options:**

- **(A)** One-one and onto
- **(B)** One-one but not onto
- **(C)** Onto but not one-one
- **(D)** Neither one-one nor onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) One-one and onto**

**Detailed Solution:**

<p>For one value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> we will get only one corresponding value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced></math> is one-one</p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>&#8943;</mo><mo>;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mn>4</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>12</mn><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>&#8943;</mo><mo>;</mo><mo>&#160;</mo><mi>f</mi><mo>&#160;</mo><mfenced><mi>n</mi></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>10</mn><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn><mo>&#8943;</mo><mo>;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>So range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced></math> is onto</p>

</details>

---

### Q32. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mn>1</mn></math>  and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>. Then the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi></math> is:

**Options:**

- **(A)** One-one but not onto
- **(B)** onto but not one-one
- **(C)** Both one-one and onto
- **(D)** Neither one-one nor onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Neither one-one nor onto**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>f</mi><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mn>1</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#60;</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#8804;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>&#60;</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#8805;</mo><mfrac><mn>1</mn><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#60;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>So, range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>&#8834;</mo><mi>R</mi></math>.</p><p> Hence, the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is into function and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mstyle displaystyle="true"><msup><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mstyle><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is an even function. So, it is a many one function.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mfenced><mi>x</mi></mfenced></math> is neither one-one nor onto function.</p>

</details>

---

### Q33. JEE Main 2022 (24 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of one-one functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="}" open="{"><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8594;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>+</mo><mn>3</mn><mi>f</mi><mfenced><mi mathvariant="normal">c</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>d</mi></mfenced><mo>=</mo><mn>0</mn></math> is _____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **31**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>d</mi></mfenced></math></p><p>Using fundamental principle of counting,</p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mtext>then</mtext><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>d</mi></mfenced><mo>=</mo><mn>2</mn></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> choices,</p><p>Similarly when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mtext>then</mtext><mo>&#160;</mo><mi>f</mi><mfenced><mi>b</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>d</mi></mfenced></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> choices.</p><p>Counting like this we get the total number of one-one function as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math></p>

</details>

---

### Q34. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>.</mo></math> Then the number of possible functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>S</mi><mo>&#8594;</mo><mi>S</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>m</mi><mo>&#183;</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>m</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced></math> for every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>,</mo><mi>n</mi><mo>&#8712;</mo><mi>S</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#183;</mo><mi>n</mi><mo>&#8712;</mo><mi>S</mi></math>, is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **490**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>m</mi><mi>n</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>m</mi></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>1</mn><mo>&#183;</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>&#8658;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mfenced open="{" close="}"><mrow><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mi>n</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>1</mn></math> and if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mn>4</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>6</mn></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>&#183;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced></math> can be any value between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>,</mo><mi>f</mi><mfenced><mn>7</mn></mfenced></math> can take any value from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>So, total number of function <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>7</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>7</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>490</mn></math></p>

</details>

---

### Q35. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>B</mi><mo>&#8594;</mo><mi>C</mi><mfenced><mrow><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi><mo>&#8838;</mo><mi>R</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>g</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo></math> exists, then:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> both are one-one
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> both are onto
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is one-one and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is onto
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is onto and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is one-one

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is one-one and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is onto**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mfenced><mrow><mi>g</mi><mi>o</mi><mi>f</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> exist <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi><mo>=</mo><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is bijective</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi></math> must be one-one and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> must be onto.</p>

</details>

---

### Q36. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math> be defined as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8805;</mo><mn>0</mn></math></p><p>Then which of the following statements is true ?</p>

**Options:**

- **(A)** There exists an onto function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mo>=</mo><mi>f</mi></math>
- **(B)** There exists a one-one function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math> such
that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mo>=</mo><mi>f</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>g</mi><mi>o</mi><mi>g</mi><mo>=</mo><mi>g</mi></math>
- **(D)** There exists a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi><mo>=</mo><mi>f</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) There exists an onto function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi><mo>=</mo><mi>f</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mtable columnalign="left left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mn>2</mn><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>3</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced><mtable columnalign="left"><mtr/><mtr/><mtr/></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mtable columnalign="left left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mn>1</mn><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>-</mo><mn>1</mn><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>3</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced><mtable columnalign="left"><mtr/><mtr/><mtr/></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>g</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left left"><mtr><mtd><mi>x</mi><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mtable columnalign="left"><mtr/><mtr/><mtr/></mtable><mtable columnalign="left"><mtr/><mtr/><mtr/></mtable></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi><mo>,</mo><mi>f</mi></math> is a one-one function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8658;</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi></math>, which is not the case</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi></math> is an onto function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> one possibility is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable columnalign="left left"><mtr><mtd><mi>n</mi><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi>n</mi><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>n</mi><mo>;</mo></mtd><mtd><mi>x</mi><mo>=</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mo>;</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is onto, also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>N</mi></math></p>

</details>

---

### Q37. JEE Main 2021 (22 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>}</mo><mo>.</mo></math> Then the number of bijective functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>A</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>3</mn><mo>-</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **720**

**Detailed Solution:**

<p>Given the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>}</mo><mo>.</mo></math></p><p>And, also a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>A</mi></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>3</mn><mo>-</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>3</mn></math></p><p>Since, the range of the function is also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo></math> hence the only possibility satisfying the given condition is: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>3</mn></math></p><p>We know that, the number of arrangements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> objects at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> places is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>!</mo><mo>.</mo></math></p><p>Since, the given function is bijective i.e. one-one and onto, hence, the elements <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math> in the domain can be mapped with only <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></math> in the co-domain in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>!</mo></math> ways and the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> elements <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> in the domain can be mapped with any of the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> elements <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>!</mo></math> ways. </p><p>So, the number of bijective functions are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>!</mo><mo>&#215;</mo><mn>5</mn><mo>!</mo><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>120</mn><mo>=</mo><mn>720</mn><mo>.</mo></math></p>

</details>

---

### Q38. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>A</mi></math> be defined as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>k</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="center left"><mtr><mtd><mi>k</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>k</mi><mo>&#160;</mo><mi>is</mi><mo>odd</mo></mtd></mtr><mtr><mtd><mi>k</mi></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>k</mi><mo>&#160;</mo><mi>is</mi><mo>even</mo></mtd></mtr></mtable></mfenced></math></p><p>Then the number of possible functions <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>A</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>o</mi><mi>f</mi><mo>=</mo><mi>f</mi></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>5</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mn>5</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>!</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>5</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>5</mn></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="center left"><mtr><mtd><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>is</mi><mo>odd</mo></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>if</mi><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>is</mi><mo>even</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>g</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo></math> A such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is even then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is odd then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we can say that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is even</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is odd then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> can take any value in set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></p><p>so number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#215;</mo><mn>1</mn></math></p>

</details>

---

### Q39. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> denote the total number of one-one functions from a set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> elements to a set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> elements and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> denote the total number of one-one functions from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> to the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>B</mi></math>. Then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>273</mn><mi>x</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>=</mo><mn>273</mn><mi>x</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>=</mo><mn>91</mn><mi>x</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>91</mn><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mo>=</mo><mn>91</mn><mi>x</mi></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>3</mn><mo>,</mo><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#215;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>&#215;</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>15</mn><mo>&#215;</mo><mn>14</mn><mo>&#215;</mo><mn>13</mn><mo>=</mo><mn>30</mn><mo>&#215;</mo><mn>91</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>60</mn><mo>&#215;</mo><mn>91</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>91</mn><mi>x</mi></math></p>

</details>

---

### Q40. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>,</mo><mi>g</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> be any arbitrary function. Which of the following statements is NOT true?

**Options:**

- **(A)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is onto, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mi>n</mi><mo>&#8704;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>
- **(B)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is onto, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi></math> is one-one
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is one-one
- **(D)** If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi></math> is one-one, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is one-one

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is onto, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi></math> is one-one**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math></p><p>A.P. with common difference = <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>General term = <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>n</mi><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mi>n</mi><mi>f</mi><mfenced><mn>1</mn></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi></math> is one-one</p><p>Now, Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><msub><mi>x</mi><mn>2</mn></msub></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><msub><mi>x</mi><mn>1</mn></msub></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>g</mi><mfenced><msub><mi>x</mi><mn>2</mn></msub></mfenced><mo>=</mo><mi>g</mi><mfenced><msub><mi>x</mi><mn>1</mn></msub></mfenced></math> (as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is one-one)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><msub><mi>x</mi><mn>2</mn></msub></math> (as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi></math> is one-one)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>g</mi></math> is one-one</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> to be onto, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo></math> should take all the values of natural numbers.</p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is increasing, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>=</mo><mi>n</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>n</mi></mfenced></mrow></mfenced><mo>=</mo><mi>g</mi><mfenced><mi>n</mi></mfenced><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced></math></p><p>may be many-one if</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>n</mi></mfenced></math> is many-one</p><p>So &ldquo;if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> is onto, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>o</mi><mi>g</mi></math> is one-one&rdquo; is incorrect.</p>

</details>

---

### Q41. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>:</mo><mi>R</mi><mo>-</mo><mfenced open="{" close="}"><mn>1</mn></mfenced><mo>&#8594;</mo><mi>R</mi></math>. be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math>. Then the composition function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is:

**Options:**

- **(A)** neither one-one nor onto
- **(B)** one-one but not onto
- **(C)** onto but not one-one
- **(D)** both one-one and onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) one-one but not onto**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>2</mn><mfenced><mfrac><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mfenced><mo>-</mo><mn>1</mn><mo>.</mo></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>x</mi><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>Range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>=</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mn>1</mn></mfenced></math></p><p>Range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is not onto</p><p>&amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is one-one</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mi>g</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is one-one but not onto.</p><p>one-one, into</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a30cadf9-43b7-4a4c-9183-9eb3a3d18792-image.png" style="width: 225px; height: 193px;" /></p>

</details>

---

### Q42. JEE Main 2020 (05 Sep Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo><mo>.</mo></math> Then the number of elements in the set<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mo>{</mo><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>B</mi><mo>&#8739;</mo><mn>2</mn><mo>&#8712;</mo><mi>f</mi><mo>(</mo><mi>A</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is not one-one<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>}</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8230;</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

<p>only <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mn>2</mn><mo>&#39;</mo></math> in range <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>1</mn></math> function.</p><p>Total no of many one function without any condition = 60-24=40.</p><p>Number of many one function with 2 is not in range =27-6 =21.</p><p>Therefore no of not one-one functions with 2 in range = 40-21=19.</p>

</details>

---

### Q43. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi>A</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>,</mo></math> is surjective, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mo>{</mo><mo>-</mo><mn>1</mn><mo>}</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="["><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1,</mn><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="["><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>A function is surjective, when the range of the function is same as the co-domain.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>-</mo><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><mi>y</mi><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>&#8805;</mo><mn>0</mn><mi>&#160;</mi><mo>&#8658;</mo><mfrac><mi>y</mi><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>&#160;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>-</mo><mfenced open="["><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>=</mo><mi>A</mi><mo>=</mo><mi>R</mi><mo>-</mo><mfenced open="["><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q44. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of functions $f$ from $\{1,2,3, \ldots, 20\}$ onto $\{1,2,3, \ldots, 20\}$ such that $f(k)$ is a multiple of $3,$ whenever $k$ is a multiple of 4 is:

**Options:**

- **(A)** $6^{5} \times(15) !$
- **(B)** $5 ! \times 6 !$
- **(C)** $(15) ! \times 6 !$
- **(D)** $5^{6} \times 15$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(15) ! \times 6 !$**

**Detailed Solution:**

Domain and codomain $=\{1,2,3, \ldots, 20\}$.

There are five multiple of 4 as 4,8,12,16 and 20 .

and there are 6 multiple of 3 as 3,6,9,12,15,18 .

Since, when ever $k$ is multiple of 4 then $f(k)$ is multiple of 3

then total number of arrangement

$={ }^{6} c_{5} \times 5 !=6 !$

Remaining 15 elements can be arranged in $15 !$ ways.

Since, for every input, there is an output

$\Rightarrow$ function $f(k)$ in onto

$\therefore \quad$ Total number of arrangement $=15 ! .6 !$

</details>

---

### Q45. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let a function $f:(0, \infty) \rightarrow(0, \infty)$ be defined by

$f(x)=\left|1-\frac{1}{x}\right| .$ Then $f$ is :

**Options:**

- **(A)** not injective but it is surjective
- **(B)** injective only
- **(C)** neither injective nor surjective
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of the above**

**Detailed Solution:**

$f:(0, \infty) \rightarrow(0, \infty)$

$f(x)=\left|1-\frac{1}{x}\right|$ is not a function

$\because f(1)=0$ and $1 \in$ domain but $0 \notin$ co-domain

Hence, $f(x)$ is not a function.

</details>

---

### Q46. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>N</mi></math> be the set of natural numbers and two functions <math><mi>f</mi></math> and <math><mi>g</mi></math> be defined as <math><mi>f</mi><mo>,</mo><mi>g</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>N</mi></math> such that

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>n</mi></mfenced><mo>=</mo><mfenced open="{" close="" separators="|"><mtable><mtr><mtd><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>i</mi><mi>f</mi><mi>&#160;</mi><mi>n</mi><mi>&#160;</mi><mi>i</mi><mi>s</mi><mi>&#160;</mi><mi>o</mi><mi>d</mi><mi>d</mi></mtd></mtr><mtr><mtd><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfrac><mi>n</mi><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>i</mi><mi>f</mi><mi>&#160;</mi><mi>n</mi><mi>&#160;</mi><mi>i</mi><mi>s</mi><mi>&#160;</mi><mi>e</mi><mi>v</mi><mi>e</mi><mi>n</mi></mtd></mtr></mtable></mfenced></math>

and <math><mi>g</mi><mfenced separators="|"><mrow><mi>n</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>.</mo></math> Then <math><mi>f</mi><mi>o</mi><mi>g</mi></math> is:

**Options:**

- **(A)** onto but not one-one
- **(B)** Both one-one and onto
- **(C)** One-one but not onto
- **(D)** Neither one-one nor onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) onto but not one-one**

**Detailed Solution:**

We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mtable><mtr><mtd><mi>n</mi><mo>+</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>i</mi><mi>f</mi><mtext>&#8201;</mtext><mi>n</mi><mtext>&#8201;</mtext><mi>o</mi><mi>d</mi><mi>d</mi></mtd></mtr><mtr><mtd><mi>n</mi><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>i</mi><mi>f</mi><mtext>&#8201;</mtext><mi>n</mi><mtext>&#8201;</mtext><mi>e</mi><mi>v</mi><mi>e</mi><mi>n</mi></mtd></mtr></mtable></mfenced></math>

<math><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>1</mn></math>

<math><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn></math>

<math><mo>&#8756;</mo><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></math> is many one.

<math><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mn>2</mn><mi>k</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mo>(</mo><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>k</mi></math>

<math><mi>f</mi><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>k</mi><mo>+</mo><mn>1</mn></math>

<math><mo>&#8756;</mo><mi>f</mi><mo>(</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo></math> is onto.

</details>

---

### Q47. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>A</mi><mo>=</mo><mi>&#160;</mi></math> { <math><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mi>x</mi></math> is not a positive integer} <math><mo>.</mo></math> Define a function <math><mi>&#160;</mi><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>R</mi></math> as <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math> , then <math><mi>f</mi></math> is:

**Options:**

- **(A)** Injective but not surjective
- **(B)** Not injective
- **(C)** Surjective but not injective
- **(D)** Neither injective nor surjective

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Injective but not surjective**

**Detailed Solution:**

<p>Given, function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math> and domain of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is <math><mfenced close="]" separators="|"><mrow><mo>-</mo><mi>&#8734;</mi><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced></math>

Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mo>-</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfenced></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>&#60;</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>f</mi></math> is always decreasing in the given domain.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/vlfmdnlgxdrppcsmpzgjykjjnwhbtvnjrxmprwyhzwoqluotzp.png" />

Clearly, given function is one-one or injective.
Since, codomain <math><mfenced separators="|"><mrow><mo>-</mo><mi>&#8734;</mi><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>&#8800;</mo></math> Range <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced></math> , hence <math><mi>f</mi></math> is into.</p>

</details>

---

### Q48. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The function <math><mi>f</mi><mi>&#160;</mi><mo>:</mo><mi>N</mi><mo>&#8594;</mo><mi>I</mi></math> defined by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mn>5</mn><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></math> , where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> is the set of natural numbers and <math><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi></mrow></mfenced></math> denotes the greatest integer less than or equal to <math><mi>x</mi></math>, is:

**Options:**

- **(A)** one-one but not onto
- **(B)** one-one and onto
- **(C)** neither one-one nor onto
- **(D)** onto but not one-one

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) neither one-one nor onto**

**Detailed Solution:**

Given, <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mi>x</mi><mo>&#8722;</mo><mn>5</mn><mrow><mo>[</mo> <mrow> <mfrac> <mi>x</mi> <mn>5</mn> </mfrac> </mrow> <mo>]</mo></mrow></mrow> </math>

Hence, <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mn>5</mn><mrow><mo>(</mo> <mrow> <mfrac> <mi>x</mi> <mn>5</mn> </mfrac> <mo>&#8722;</mo><mrow><mo>[</mo> <mrow> <mfrac> <mi>x</mi> <mn>5</mn> </mfrac> </mrow> <mo>]</mo></mrow></mrow> <mo>)</mo></mrow></mrow> </math>

<math> <mrow> <mo>=</mo><mn>5</mn><mrow><mo>{</mo> <mrow> <mfrac> <mi>x</mi> <mn>5</mn> </mfrac> </mrow> <mo>}</mo></mrow></mrow> </math>

Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is a natural number. 

Hence, <math><mfenced close="}" open="{" separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

Hence, <math> <mrow> <mi>f</mi><mrow><mo>(</mo> <mi>x</mi> <mo>)</mo></mrow><mo>=</mo><mn>0</mn></mrow> </math>, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn><mi>n</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>

<math> <mrow> <mo>=</mo><mn>1</mn></mrow> </math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>

<math> <mrow> <mo>=</mo><mn>2</mn></mrow> </math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn><mi>n</mi><mo>+</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>

<math> <mrow> <mo>=</mo><mn>3</mn></mrow> </math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn><mi>n</mi><mo>+</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>

<math> <mo>=</mo><mn>4</mn> </math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn><mi>n</mi><mo>+</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>

Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is neither one-one nor onto.

</details>

---

### Q49. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The function <math><mi>f</mi><mi>&#160;</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> defined as <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>,</mo></math> is:

**Options:**

- **(A)** Invertible
- **(B)** Injective but not surjective
- **(C)** Surjective but not injective
- **(D)** Neither injective nor surjective

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Surjective but not injective**

**Detailed Solution:**

<p>Let, <math><mi>y</mi><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>y</mi><mo>+</mo><mi>y</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi><mo>-</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mo>+</mo><mn>1</mn><mo>&#177;</mo><mi>&#160;</mi><mi>&#160;</mi><msqrt><mn>1</mn><mo>-</mo><mn>4</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow><mrow><mn>2</mn><mi>y</mi></mrow></mfrac></math>

<math><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mn>4</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mo>&#8805;</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mn>4</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mo>&#8804;</mo><mn>1</mn></math>

<math><mo>&#8658;</mo></math> So, <math><mo></mo><mi>y</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>

Here, Co-Domain<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>Range</p><p>Hence, the function is surjective.

Now, for injective function</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>x</mi><mn>1</mn></msub><mrow><mn>1</mn><mo>+</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup></mrow></mfrac><mo>=</mo><mfrac><msub><mi>x</mi><mn>2</mn></msub><mrow><mn>1</mn><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup></mrow></mfrac></math>

<math><mo>&#8658;</mo></math><math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><msubsup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><msubsup><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><msub><mi>x</mi><mn>1</mn></msub><msub><mi>x</mi><mn>2</mn></msub><mfenced separators="|"><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><msub><mi>x</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math><math><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math><math><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub></math> or <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></math>

Hence, the function is not injective.</p>

</details>

---

### Q50. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>&#160;</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is

**Options:**

- **(A)** one-one but not onto
- **(B)** neither one-one nor onto
- **(C)** both one-one and onto
- **(D)** onto but not one-one

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) neither one-one nor onto**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>&#160;</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>-</mo><mn>1</mn></mrow><mrow><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfrac></math>

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>x</mi></mfenced></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>x</mi></mfenced></mfrac></mstyle></mrow></mfrac></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8594;</mo><mo>&#177;</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8594;</mo><mn>1</mn></math></p><p>Thus, the graph of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is given by</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c7558290-8216-415d-8bf2-18cc853de6c2-image.png" style="width: 315px; height: 220px;" /></p><p>If a line parallel to the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis intersects the graph of a function at more than one point, then the function is many-one.</p><p>And, it is clear from the graph that, the given function is many-one.</p><p>Also, the range of the function is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math> which is not same as the co-domain which is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and if the co-domain of a function and range are not same then the function is not onto.</p><p>Hence, the given function is neither one-one nor onto.</p>

</details>

---

### Q51. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\{1,2,3,4\}$ and $R: A \rightarrow A$ be the relation defined by $R=\{(1,1),(2,3),(3,4),(4,2)\}$. The correct statement is :

**Options:**

- **(A)** $R$ does not have an inverse.
- **(B)** $R$ is not a one to one function.
- **(C)** $R$ is an onto function.
- **(D)** $R$ is not a function.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $R$ is an onto function.**

**Detailed Solution:**

$\begin{aligned} & \text { Domain }=\{1,2,3,4\} \\ & \text { Range }=\{1,2,3,4\} \\ & \therefore \quad \text { Domain }=\text { Range }\end{aligned}$

</details>

---

### Q52. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $A$ and $B$ be non empty sets in $R$ and $f: A \rightarrow B$ is a bijective function.
Statement 1: $\mathrm{f}$ is an onto function.
Statement 2: There exists a function $g: B \rightarrow A$ such that fog $=I_B$.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is true, Statement 2 is true; Statement 2 is a correct explanation for Statement 1.
- **(C)** Statement 1 is false, Statement 2 is true.
- **(D)** Statement 1 is true, Statement 2 is true, Statement 2 is not the correct explanation for Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 1 is true, Statement 2 is true, Statement 2 is not the correct explanation for Statement 1.**

**Detailed Solution:**

Let $A$ and $B$ be non-empty sets in $R$.
Let $f: A \rightarrow B$ is bijective function.
Clearly statement - 1 is true which says that $f$ is an onto function.
Statement $-2$ is also true statement but it is not the correct explanation for statement-1

</details>

---

### Q53. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If $P(S)$ denotes the set of all subsets of a given set $S$, then the number of one-to-one functions from the set $S=\{1,2,3\}$ to the $\operatorname{set} P(S)$ is

**Options:**

- **(A)** 24
- **(B)** 8
- **(C)** 336
- **(D)** 320

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 336**

**Detailed Solution:**

Let $S=\{1,2,3\} \Rightarrow n(S)=3$
Now, $P(S)=$ set of all subsets of $S$ total no. of subsets $=2^3=8$
$$
\therefore n[P(S)]=8
$$
Now, number of one-to-one functions from
$$
S \rightarrow P(S) \text { is }{ }^8 P_3=\frac{8 !}{5 !}=8 \times 7 \times 6=336 .
$$

</details>

---

### Q54. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `1`

For real $x$, let $f(x)=x^3+5 x+1$, then

**Options:**

- **(A)** $f$ is one-one but not onto $R$
- **(B)** $\mathrm{f}$ is onto $\mathrm{R}$ but not one-one
- **(C)** $f$ is one-one and onto $R$
- **(D)** $f$ is neither one-one nor onto $R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f$ is one-one and onto $R$**

**Detailed Solution:**

Given $f(x)=x^3+5 x+1$
Now $f^{\prime}(x)=3 x^2+5>0, \forall x \in R$
$\therefore \mathrm{f}(\mathrm{x})$ is strictly increasing function
$\therefore$ It is one-one
Clearly, $f(x)$ is a continuous function and also increasing on $R$,
$\operatorname{Lt}_{x \rightarrow-\infty} f(x)=-\infty$ and $\operatorname{Lt}_{x \rightarrow \infty} f(x)=\infty$
$\therefore \mathrm{f}(\mathrm{x})$ takes every value between $-\infty$ and $\infty$.
Thus, $f(x)$ is onto function.

</details>

---

### Q55. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

Let $f:(-1,1) \rightarrow B$, be a function defined by $f(x)=\tan ^{-1} \frac{2 x}{1-x^2}$, then $f$ is both one-one and onto when $B$ is the interval

**Options:**

- **(A)** $\left(0, \frac{\pi}{2}\right)$
- **(B)** $\left[0, \frac{\pi}{2}\right)$
- **(C)** $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
- **(D)** $\left(\frac{\pi}{2}, \frac{\pi}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{\pi}{2}, \frac{\pi}{2}\right)$**

**Detailed Solution:**

Given $f(x)=\tan ^{-1}\left(\frac{2 x}{1-x^2}\right)$ for $x \in(-1,1)$
clearly range of $f(x)=\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.
$\therefore$ co-domain of function $=B=\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$.

</details>

---

### Q56. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $f: R \rightarrow S$, defined by $f(x)=\sin x-\sqrt{3} \cos x+1$, is onto, then the interval of $S$ is

**Options:**

- **(A)** $[0,3]$
- **(B)** $[-1,1]$
- **(C)** $[0,1]$
- **(D)** $[-1,3]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $[-1,3]$**

**Detailed Solution:**

$-2 \leq \sin x-\sqrt{3} \cos x \leq 2 \Rightarrow-1 \leq \sin x-\sqrt{3} \cos x+1 \leq 3$
$\Rightarrow$ range of $f(x)$ is $[-1,3]$.
Hence $S$ is $[-1,3]$

</details>

---

### Q57. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

A function $\mathrm{f}$ from the set of natural numbers to integers defined by $\mathrm{f}(\mathrm{n})=\left\{\begin{array}{l}\frac{\mathrm{n}-1}{2} \text {, when } n \text { isodd } \\ \frac{\mathrm{n}}{2} \text {, when } \mathrm{n} \text { is even }\end{array}\right.$ is

**Options:**

- **(A)** neither one-one nor onto
- **(B)** one-one but not onto
- **(C)** onto but not one-one
- **(D)** one-one and onto both.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) one-one and onto both.**

**Detailed Solution:**

$f: N \rightarrow 1$
$f(1)=0, f(2)=-1, f(3)=-1, f(4)=-2$
$f(5)=2$, and $f(6)=-3$ so on.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hAuAkB1tVJ7VkcIH2Z_ytAT4-Bh5p6GUix03MML7TIY.original.fullsize.png">

In this type of function every element of set $\mathrm{A}$ has unique image in set $\mathrm{B}$ and there is no element left in set $\mathrm{B}$. Hence $\mathrm{f}$ is one-one and onto function.

</details>

---

