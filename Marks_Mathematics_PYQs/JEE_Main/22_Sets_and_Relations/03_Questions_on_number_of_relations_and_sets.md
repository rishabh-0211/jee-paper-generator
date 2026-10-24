# JEE Main Mathematics - Sets and Relations

## Topic 3: Questions on number of relations and sets

**Total Questions:** 43

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $A = \{1, 4, 7\}$ and $B = \{2, 3, 8\}$. Then the number of elements, in the relation $R = \{((a_1, b_1), (a_2, b_2)) \in ((A \times B) \times (A \times B)) : a_1 + b_2 \text{ divides } a_2 + b_1\}$ is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

Let $A = \{1, 4, 7\}$ and $B = \{2, 3, 8\}$. The relation $R$ consists of pairs $((a_1, b_1), (a_2, b_2))$ from $A \times B$ such that $(a_1 + b_2)$ divides $(a_2 + b_1)$.

Let $x = a_1 + b_2$ and $y = a_2 + b_1$. Note that $(a_1, b_2)$ and $(a_2, b_1)$ are both independent elements of $A \times B$. So choosing $((a_1, b_1), (a_2, b_2))$ is equivalent to independently choosing two elements of $A \times B$ with sums $x$ and $y$ such that $x \mid y$.

All possible sums $a + b$ with $a \in A$ and $b \in B$:
$1 + 2 = 3$, $1 + 3 = 4$, $1 + 8 = 9$
$4 + 2 = 6$, $4 + 3 = 7$, $4 + 8 = 12$
$7 + 2 = 9$, $7 + 3 = 10$, $7 + 8 = 15$

Frequencies of each sum:
$f(3) = 1$, $f(4) = 1$, $f(6) = 1$, $f(7) = 1$, $f(9) = 2$, $f(10) = 1$, $f(12) = 1$, $f(15) = 1$

For each possible divisor $x$, count the number of valid pairs $(x, y)$ with $x \mid y$, each contributing $f(x) \cdot f(y)$:

$x = 3$: divides $3, 6, 9, 12, 15$
Ways $= 1 \cdot (1 + 1 + 2 + 1 + 1) = 6$

$x = 4$: divides $4, 12$
Ways $= 1 \cdot (1 + 1) = 2$

$x = 6$: divides $6, 12$
Ways $= 1 \cdot (1 + 1) = 2$

$x = 7$: divides $7$
Ways $= 1 \cdot 1 = 1$

$x = 9$: divides $9$
Ways $= 2 \cdot 2 = 4$

$x = 10$: divides $10$
Ways $= 1 \cdot 1 = 1$

$x = 12$: divides $12$
Ways $= 1 \cdot 1 = 1$

$x = 15$: divides $15$
Ways $= 1 \cdot 1 = 1$

Total number of elements in $R$:
$6 + 2 + 2 + 1 + 4 + 1 + 1 + 1 = 18$

Hence, the answer is $18$.

</details>

---

### Q2. JEE Main 2026 (02 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $A = \{2, 3, 4, 5, 6\}$. Let R be a relation on the set $A \times A$ given by $(x, y) R (z, w)$ if and only if $x$ divides $z$ and $y \leq w$. Then the number of elements in R is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **120**

**Detailed Solution:**

Given the set $A = \{2, 3, 4, 5, 6\}$.

The relation $R$ is defined on $A \times A$ such that $(x, y) R (z, w)$ if and only if $x$ divides $z$ and $y \leq w$.

The number of elements in $R$ is the number of ordered pairs $((x, y), (z, w))$ satisfying these conditions. Since the conditions for $(x, z)$ and $(y, w)$ are independent, the total number of elements in $R$ will be the product of the number of pairs $(x, z)$ satisfying $x$ divides $z$ and the number of pairs $(y, w)$ satisfying $y \leq w$.

First, we find the number of pairs $(x, z) \in A \times A$ such that $x$ divides $z$:
For $x = 2$, $z \in \{2, 4, 6\}$ ($3$ pairs)
For $x = 3$, $z \in \{3, 6\}$ ($2$ pairs)
For $x = 4$, $z \in \{4\}$ ($1$ pair)
For $x = 5$, $z \in \{5\}$ ($1$ pair)
For $x = 6$, $z \in \{6\}$ ($1$ pair)
Total number of pairs $(x, z) = 3 + 2 + 1 + 1 + 1 = 8$.

Next, we find the number of pairs $(y, w) \in A \times A$ such that $y \leq w$:
For $y = 2$, $w \in \{2, 3, 4, 5, 6\}$ ($5$ pairs)
For $y = 3$, $w \in \{3, 4, 5, 6\}$ ($4$ pairs)
For $y = 4$, $w \in \{4, 5, 6\}$ ($3$ pairs)
For $y = 5$, $w \in \{5, 6\}$ ($2$ pairs)
For $y = 6$, $w \in \{6\}$ ($1$ pair)
Total number of pairs $(y, w) = 5 + 4 + 3 + 2 + 1 = 15$.

The total number of elements in the relation $R$ is the product of the number of these pairs:
Total elements = $8 \times 15 = 120$.

Answer: $120$

</details>

---

### Q3. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let R be a relation defined on the set $\{1,2,3,4\} \times\{1,2,3,4\}$ by $\mathrm{R}=\{((a, b),(c, d)): 2 a+3 b=3 c+4 d\}$. Then the number of elements in R is

**Options:**

- **(A)** 18
- **(B)** 6
- **(C)** 15
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 12**

**Detailed Solution:**

We need $2a+3b = 3c+4d$ where $a,b,c,d \in \{1,2,3,4\}$.
Possible values of $2a+3b$: range from $5$ to $20$.
Possible values of $3c+4d$: range from $7$ to $28$.
For each common value $k$, the number of elements in $R$ equals (number of $(a,b)$ with $2a+3b=k$) $\times$ (number of $(c,d)$ with $3c+4d=k$).
$k=7$: $(a,b)=(2,1)$, $(c,d)=(1,1)$ $\Rightarrow 1 \times 1=1$
$k=10$: $(2,2)$, $(2,1)$ $\Rightarrow 1$
$k=11$: $(1,3),(4,1)$, $(1,2)$ $\Rightarrow 2$
$k=13$: $(2,3)$, $(3,1)$ $\Rightarrow 1$
$k=14$: $(1,4),(4,2)$, $(2,2)$ $\Rightarrow 2$
$k=15$: $(3,3)$, $(1,3)$ $\Rightarrow 1$
$k=16$: $(2,4)$, $(4,1)$ $\Rightarrow 1$
$k=17$: $(4,3)$, $(3,2)$ $\Rightarrow 1$
$k=18$: $(3,4)$, $(2,3)$ $\Rightarrow 1$
$k=20$: $(4,4)$, $(4,2)$ $\Rightarrow 1$
Total $= 1+1+2+1+2+1+1+1+1+1 = 12$

</details>

---

### Q4. JEE Main 2026 (22 January Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $S$ be the set of the first 11 natural numbers. Then the number of elements in $A=\{B \subseteq S: n(B) \geqslant 2$ and the product of all elements of $B$ is even $\}$ is $\_\_\_\_$ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1979**

**Detailed Solution:**

The set $S = \{1, 2, 3, ..., 11\}$ has 11 elements.
We need to count subsets $B$ with $n(B) \geq 2$ and even product.
A product is even iff at least one element is even.
Equivalently, count complements: a product is odd iff all elements are odd.
The odd numbers in $S$ are $\{1, 3, 5, 7, 9, 11\}$ (6 elements).
Subsets of odd numbers: $2^6 = 64$.
Among these, those with $n(B) \geq 2$ are all except empty set (1) and singletons (6): $64 - 7 = 57$.
Total subsets with $n(B) \geq 2$: $2^{11} - 1 - 11 = 2036$.
Subsets with even product and $n(B) \geq 2$: $2036 - 57 = 1979$.

</details>

---

### Q5. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of elements in the relation $\mathrm{R}=\left\{(x, y): 4 x^{2}+y^{2}<52, x, y \in \mathbf{Z}\right\}$ is

**Options:**

- **(A)** 77
- **(B)** 67
- **(C)** 86
- **(D)** 89

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 77**

**Detailed Solution:**

We need $4x^2 + y^2 < 52$ with $x, y \in \mathbb{Z}$. This requires $x^2 < 13$, so $x \in \{-3,-2,-1,0,1,2,3\}$.
$x=0$: $y^2<52 \Rightarrow y \in \{-7,...,7\}$ → 15 values
$x=\pm1$: $y^2<48 \Rightarrow |y|\leq 6$ → 13 each → 26 values
$x=\pm2$: $y^2<36 \Rightarrow |y|\leq 5$ → 11 each → 22 values
$x=\pm3$: $y^2<16 \Rightarrow |y|\leq 3$ → 7 each → 14 values
Total $= 15+26+22+14 = 77$

</details>

---

### Q6. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of relations, defined on the set $\{\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{d}\}$, which are both reflexive and symmetric, is equal to:

**Options:**

- **(A)** 16
- **(B)** 1024
- **(C)** 64
- **(D)** 256

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 64**

**Detailed Solution:**

For a set with $n = 4$ elements, reflexive condition requires all diagonal pairs $(a,a), (b,b), (c,c), (d,d)$ to be included.
For symmetric relations, non-diagonal pairs come in symmetric pairs. Number of such pairs = $\binom{4}{2} = 6$.
For each pair, we either include both elements or exclude both → 2 choices each.
Total reflexive and symmetric relations = $2^6 = 64$.

</details>

---

### Q7. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=\{1,2,3, \ldots, 10\}$ and R be a relation on A such that $\mathrm{R}=\{(\mathrm{a}, \mathrm{b}): \mathrm{a}=2 \mathrm{~b}+1\}$. Let $\left(\mathrm{a}_1, \mathrm{a}_2\right)$, $\left(a_2, a_3\right),\left(a_3, a_4\right), \ldots .,\left(a_k, a_{k+1}\right)$ be a sequence of $k$ elements of R such that the second entry of an ordered pair is equal to the first entry of the next ordered pair. Then the largest integer k , for which such a sequence exists, is equal to :

**Options:**

- **(A)** $6$
- **(B)** $7$
- **(C)** $5$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{a}=2 \mathrm{~b}+1 \\
& 2 \mathrm{~b}=\mathrm{a}-1 \\
& \mathrm{R}=\{(3,1),(5,2), \ldots,(99,49)\}
\end{aligned}$
Let $(2 m+1, m),(2 \lambda-1, \lambda)$ are such ordered pairs.
According to the condition
$\mathrm{m}=2 \lambda-1 \Rightarrow \mathrm{~m}=\text { odd number }$
$\Rightarrow 1^{\text {st }}$ element of ordered pair $(\mathrm{a}, \mathrm{b})$
$a=2(2 \lambda-1)+1=4 \lambda-1$
Hence $a \in\{3,7, \ldots, 99\}$
$\Rightarrow \lambda \in\{1,2, \ldots, 25\}$
$\Rightarrow$ set of sequence
$\begin{aligned} & \left\{(4 \lambda-1,2 \lambda-1),(2 \lambda-1, \lambda-1),\left(\lambda-1, \frac{\lambda-2}{2}\right), \ldots \ldots .\right\} \\ & 2^{\text {nd }} \text { element of each ordered pair }=\frac{\lambda-2^{\mathrm{r}-2}}{2^{\mathrm{r}-2}}\end{aligned}$
For maximum number of ordered pairs in such sequence
$\begin{aligned} & \frac{\lambda-2^{\mathrm{r}-2}}{2^{\mathrm{r}-2}}=1 \text { or } 2 ; 1 \leq \lambda \leq 25 \\ & \lambda=2^{\mathrm{r}-1} \text { or } \lambda=3.2^{\mathrm{r}-2}\end{aligned}$
$\begin{aligned} & \text { Case-I : } \lambda=2 \mathrm{r}-1 \\ & \lambda=2,2^2, 2^3, 2^4 \\ & r=2,3,4,5\end{aligned}$
Hence maximum value of $r$ is 5 when $\lambda=16$
$\begin{aligned} & \text { Case-II }: \lambda=3.2^{\mathrm{r}-2} \\ & \lambda=3,6,12,24 \\ & \mathrm{r}=2, \quad 3, \quad 4,5\end{aligned}$
Hence maximum value of $r$ is 5 when $\lambda=24$

</details>

---

### Q8. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $S=\mathbf{N} \cup\{0\}$. Define a relation $R$ from $S$ to $\mathbf{R}$ by :
$\mathrm{R}=\left\{(x, y): \log _{\mathrm{e}} y=x \log _{\mathrm{e}}\left(\frac{2}{5}\right), x \in \mathrm{~S}, y \in \mathbf{R}\right\}$

Then, the sum of all the elements in the range of $R$ is equal to :

**Options:**

- **(A)** $\frac{10}{9}$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{5}{2}$
- **(D)** $\frac{5}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5}{3}$**

**Detailed Solution:**

$\begin{aligned} & S=\{0,1,2,3 \ldots \ldots\} \\ & \log _y y=\log _e\left(\frac{2}{5}\right) \\ & \Rightarrow y=\left(\frac{2}{5}\right)^x\end{aligned}$



<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/D9WPjjdEUit2TlHrZMTdWmtVlQMoEftGDBl2beTaqhA.original.fullsize.png">





Required
$\text { Sum }=1+\left(\frac{2}{5}\right)^1+\left(\frac{2}{5}\right)^2+\left(\frac{2}{5}\right)^3+\ldots . .-=\frac{1}{1-\frac{2}{5}}=\frac{5}{3}$

</details>

---

### Q9. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=\left\{x \in(0, \pi)-\left\{\frac{\pi}{2}\right\}: \log _{(2 / \pi)}|\sin x|+\log _{(2 / \pi)}|\cos x|=2\right\}$ and $\mathrm{B}=\{x \geqslant 0: \sqrt{x}(\sqrt{x}-4)-3|\sqrt{x}-2|+6=0\}$. Then $\mathrm{n}(\mathrm{A} \cup \mathrm{B})$ is equal to :

**Options:**

- **(A)** 4
- **(B)** 8
- **(C)** 6
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

$\begin{aligned} & \mathrm{A}: \log _{2 \pi}|\sin \mathrm{x}|+\log _{2 \pi}|\cos \mathrm{x}|=2 \\ & \Rightarrow \log _{2 \pi}(|\sin \mathrm{x} \cdot \cos \mathrm{x}|)=2 \\ & \Rightarrow|\sin 2 \mathrm{x}|=\frac{8}{\pi^2}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3J_p-bEoEqcOHsgjHK5HIH8hDJrfGq7KKNL-R-DPlL0.original.fullsize.png">




Number of solution 4
$\text { B : let } \sqrt{\mathrm{x}}=\mathrm{t} < 2$

Then $\sqrt{x}(\sqrt{x}-4)+3(\sqrt{x}-2)+6=0$
$\begin{aligned}
& \Rightarrow \mathrm{t}^2-4 \mathrm{t}+3 \mathrm{t}-6+6=0 \\
& \Rightarrow \mathrm{t}^2-\mathrm{t}=0, \mathrm{t}=0, \mathrm{t}=1 \\
& \mathrm{x}=0, \mathrm{x}=1
\end{aligned}$
again let $\sqrt{\mathrm{x}}=\mathrm{t}>2$
then $\mathrm{t}^2-4 \mathrm{t}-3 \mathrm{t}+6+6=0$
$\begin{aligned}
& \Rightarrow \mathrm{t}^2-7 \mathrm{t}+12=0 \\
& \Rightarrow \mathrm{t}=3,4 \\
& \mathrm{x}=9,16
\end{aligned}$

Total number of solutions
$\mathrm{n}(\mathrm{~A} \cup \mathrm{~B})=4+4=8$

</details>

---

### Q10. JEE Main 2025 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $S=\left\{p_1, p_2 \ldots ., p_{10}\right\}$ be the set of first ten prime numbers. Let $A=S \cup P$, where $P$ is the set of all possible products of distinct elements of $S$. Then the number of all ordered pairs ( $x, y$ ), $x \in S$, $y \in A$, such that $x$ divides $y$, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5120**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \frac{y}{x}=\lambda \\ & y=\lambda x \\ & =10 \times\left({ }^9 C_0+{ }^9 C_1+{ }^9 C_2+{ }^9 C_3+\ldots+{ }^9 C_9\right) \\ & =10 \times 2 \\ & =10 \times 512=5120\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=\{(x, y) \in \mathbf{R} \times \mathbf{R}:|x+y| \geqslant 3\}$ and $\mathrm{B}=\{(x, y) \in \mathbf{R} \times \mathbf{R}:|x|+|y| \leq 3\}$.
If $\mathrm{C}=\{(x, y) \in \mathrm{A} \cap \mathrm{B}: x=0$ or $y=0\}$, then $\sum_{(x, y) \in \mathrm{C}}|x+y|$ is :

**Options:**

- **(A)** 15
- **(B)** 24
- **(C)** 18
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 12**

**Detailed Solution:**

$\begin{aligned} & A=\{(x, y) \in \mathbf{R} \times \mathbf{R}:|x+y| \geq 3\} \\ & \text { and } B=\{(x, y) \in \mathbf{R} \times \mathbf{R}:|x|+|y| \leq 3\} \\ & C=\{(x, y) \in A \cap B: x=0 \text { or } y=0\}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tu2o4lxXTKS59YcsJ5lTvblslwcCAI7-f6sG5zUNTpo.original.fullsize.png">

$A \cap B$ will have only common points lying on the line $P Q$ and $R S$
Now, $C=\{(-3,0),(3,0),(0,3),(0,-3)\}$
$\sum_{(x, y) \in c}|x+y|=3+3+3+3=12$

</details>

---

### Q12. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{R}=\{(1,2),(2,3),(3,3)\}$ be a relation defined on the set $\{1,2,3,4\}$. Then the minimum number of elements, needed to be added in R so that R becomes an equivalence relation, is:

**Options:**

- **(A)** $10$
- **(B)** $7$
- **(C)** $8$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $7$**

**Detailed Solution:**

$A=\{1,2,3,4\}$

For relation to be reflexive
$\mathrm{R}=\{(1,2),(2,3),(3,3)\}$

Minimum elements added will be
$(1,1),(2,2),(4,4)(2,1)(3,2)(3,2)(3,1)(1,3)$
$\therefore$ Minimum number of elements $=7$

</details>

---

### Q13. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\{1,2,3, \ldots, 10\}$ and $B=\left\{\frac{m}{n}: m, n \in A, m \lt n\right.$ and $\left.\operatorname{gcd}(m, n)=1\right\}$. Then $n(B)$ is equal to :

**Options:**

- **(A)** $36$
- **(B)** $31$
- **(C)** $37$
- **(D)** $29$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $31$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{A}=\{1,2, \ldots, 10\} \\ & \mathrm{B}\left\{\frac{\mathrm{m}}{\mathrm{n}}=\mathrm{m}, \mathrm{n} \in \mathrm{A}, \mathrm{m} < \mathrm{n}, \operatorname{gcd}(\mathrm{m}, \mathrm{n})=1\right\} \\ & \mathrm{n}(\mathrm{B}) \end{aligned}$


$\mathrm{n}=2 \quad\left\{\frac{1}{2}\right\}$
$\mathrm{n}=3 \quad\left\{\frac{1}{3}, \frac{2}{3}\right\}$

$\begin{array}{ll}\mathrm{n}=4 & \left\{\frac{1}{4}, \frac{3}{4}\right\} \\ \mathrm{n}=5 & \left\{\frac{1}{5}, \frac{2}{5}, \frac{3}{5}, \frac{4}{5}\right\}\end{array}$

$\begin{array}{ll}\mathrm{n}=6 & \left\{\frac{1}{6}, \frac{5}{6}\right\} \\ \mathrm{n}=7 & \left\{\frac{1}{7}, \frac{2}{7}, \frac{3}{7}, \frac{4}{7}, \frac{5}{7}, \frac{6}{7}\right\} \\ \mathrm{n}=8 & \left\{\frac{1}{8}, \frac{3}{8}, \frac{5}{8}, \frac{7}{8}\right\}\end{array}$

$\begin{array}{ll}\mathrm{n}=9 & \left\{\frac{1}{9}, \frac{2}{9}, \frac{4}{9}, \frac{5}{9}, \frac{7}{9}, \frac{8}{9}\right\} \\ \mathrm{n}=10 & \left\{\frac{1}{10}, \frac{3}{10}, \frac{7}{10}, \frac{9}{10}\right\} \\ \mathrm{n}(\mathrm{B})=31\end{array}$

</details>

---

### Q14. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of non-empty equivalence relations on the set $\{1,2,3\}$ is :

**Options:**

- **(A)** $6$
- **(B)** $5$
- **(C)** $7$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5$**

**Detailed Solution:**

Let $R$ be the required relation
$\mathrm{A}=\{(1,1)(2,2),(3,3)\}$
(i) $|\mathrm{R}|=3$, when $\mathrm{R}=\mathrm{A}$
(ii) $|\mathrm{R}|=5$, e.g. $\mathrm{R}=\mathrm{A} \cup\{(1,2),(2,1)\}$

Number of $R$ can be [3]
(iii) $\mathrm{R}=\{1,2,3\} \times\{1,2,3\}$
Ans. (5)

</details>

---

### Q15. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let $A=\{2,3,6,7\}$ and $B=\{4,5,6,8\}$. Let $R$ be a relation defined on $A \times B$ by $\left(a_1, b_1\right) R\left(a_2, b_2\right)$ if and only if $a_1+a_2=b_1+b_2$. Then the number of elements in $R$ is _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

$\begin{aligned} & A=\{2,3,6,7\} \\ & B=\{2,5,6,8\} \\ & \left(a_1, b_1\right) R\left(a_2, b_2\right) \\ & a_1+a_2=b_1+b_2\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/z0AzxhoS94ZtP1I08IIYNdhGLDIIdafsRvkaOd3SBns.original.fullsize.png">
Total 24 + 1 = 25

</details>

---

### Q16. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the set $S=\{2,4,8,16, \ldots, 512\}$ be partitioned into 3 sets $A, B, C$ with equal number of elements such that $\mathrm{A} \cup \mathrm{B} \cup \mathrm{C}=\mathrm{S}$ and $\mathrm{A} \cap \mathrm{B}=\mathrm{B} \cap \mathrm{C}=\mathrm{A} \cap \mathrm{C}=\phi$. The maximum number of such possible partitions of $S$ is equal to:

**Options:**

- **(A)** 1680
- **(B)** 1640
- **(C)** 1520
- **(D)** 1710

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1680**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZomYeN9iKIocbtU6PSv0BM3XqR4pq3tIqg_LwQN0kUE.original.fullsize.png">
$\frac{9 !}{(3 ! 3 ! 3 !) 3 !} \times 3 !$

</details>

---

### Q17. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>..20</mo></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> two relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> such that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mo>{</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>b</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mo>{</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>a</mi></math> is an integral multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>}</p><p>Then, number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>−</mo><msub><mi>R</mi><mn>2</mn></msub></math> is equal to __________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **46**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>..20</mo></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mo>{</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>b</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>} and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mo>{</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>a</mi></math> is an integral multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>}.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>20</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>20</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>18</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>20</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>20</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>18</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>18</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>14</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>16</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>18</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>10</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>10</mn><mo>,</mo><mn>20</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>11</mn><mo>,</mo><mn>11</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>20</mn><mo>,</mo><mn>20</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mfenced><msub><mi>R</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>20</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>10</mn><mo>=</mo><mn>66</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>R</mi><mn>1</mn></msub><mo>∩</mo><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>20</mn><mo>,</mo><mn>20</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>∩</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mi>n</mi><mfenced><msub><mi>R</mi><mn>1</mn></msub></mfenced><mo>-</mo><mi>n</mi><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>∩</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>66</mn><mo>-</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>46</mn></math></p>

</details>

---

### Q18. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi></mrow></mfenced><mo>:</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi><mo>∈</mo><mi>Z</mi><mo>,</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>42</mn><mo>,</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi><mo>≥</mo><mn>0</mn></mrow></mfenced></math> equals ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **169**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>z</mi><mo>=</mo><mn>42</mn><mo>,</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi><mo>≥</mo><mn>0</mn></math></p><p>Now, taking cases for different value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>0</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>42</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> can take values <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>21</mn></mrow></mfenced><mo>→</mo><mn>22</mn><mo> </mo><mtext>elements</mtext></math></p><p>Similarly, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>1</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>39</mn><mo>⇒</mo><mn>20</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>2</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>36</mn><mo>⇒</mo><mn>19</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>3</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>33</mn><mo>⇒</mo><mn>17</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>4</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>30</mn><mo>⇒</mo><mn>16</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>5</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>27</mn><mo>⇒</mo><mn>14</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>6</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>24</mn><mo>⇒</mo><mn>13</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>7</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>21</mn><mo>⇒</mo><mn>11</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>8</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>18</mn><mo>⇒</mo><mn>10</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>9</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>15</mn><mo>⇒</mo><mn>8</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>10</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>12</mn><mo>⇒</mo><mn>7</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>11</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>9</mn><mo>⇒</mo><mn>5</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>12</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>6</mn><mo>⇒</mo><mn>4</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>13</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>3</mn><mo>⇒</mo><mn>2</mn><mo> </mo><mtext>elements</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>14</mn><mo>;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>0</mn><mo>⇒</mo><mn>1</mn><mo> </mo><mtext>elements</mtext></math></p><p>Total : <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>169</mn></math></p>

</details>

---

### Q19. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>...100</mo></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be a relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo> </mo><mi>y</mi></mrow></mfenced><mo>∈</mo><mi>R</mi></math> if and only if <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>=</mo><mn>3</mn><mi>y</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> be a symmetric relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>⊂</mo><msub><mi>R</mi><mn>1</mn></msub></math> and the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>. Then the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **66**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>=</mo><mn>3</mn><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>k</mi></math></p><p>Now, given set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mn>3</mn><mo>,</mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>100</mn></mrow></mfenced></math></p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>≤</mo><mn>33</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>12</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>...</mo><mfenced><mrow><mn>99</mn><mo>,</mo><mn>66</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mfenced><mi>R</mi></mfenced><mo>=</mo><mn>33</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is symmetric relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>⊂</mo><msub><mi>R</mi><mn>1</mn></msub></math> so, we need elements <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>9</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>12</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>...</mo><mfenced><mrow><mn>99</mn><mo>,</mo><mn>66</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>...</mo><mfenced><mrow><mn>66</mn><mo>,</mo><mn>99</mn></mrow></mfenced></mrow></mfenced></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math></p><p>Hence, the minimum number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn><mo>+</mo><mn>33</mn><mo>=</mo><mn>66</mn></math></p>

</details>

---

### Q20. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The number of symmetric relations defined on the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math> which are not reflexive is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **960**

**Detailed Solution:**

<blockquote><p>We know that,</p><p>Total number of relation both symmetric and reflexive <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi></mrow><mn>2</mn></mfrac></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is number of elements in given set,</p><p>Also, total number of symmetric relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mfenced><mfrac><mrow><msup><mi mathvariant="normal">n</mi><mn>2</mn></msup><mo>+</mo><mi mathvariant="normal">n</mi></mrow><mn>2</mn></mfrac></mfenced></msup></math></p><p>Then number of symmetric relation which are not reflexive will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac></msup><mo>-</mo><msup><mn>2</mn><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mo>-</mo><msup><mn>2</mn><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1024</mn><mo>-</mo><mn>64</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>960</mn></math></p></blockquote>

</details>

---

### Q21. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be a relation on the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>A</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced></mrow></mfenced><mo>:</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>4</mn><mi>c</mi><mo>+</mo><mn>5</mn><mi>d</mi></mrow></mfenced></math>. Then the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>And relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>A</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>4</mn><mi>c</mi><mo>+</mo><mn>5</mn><mi>d</mi></math></p><p>Now, Maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>20</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math></p><p>And Minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>c</mi><mo>+</mo><mn>5</mn><mi>d</mi><mo>=</mo><mn>9</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>c</mi><mo>+</mo><mn>5</mn><mi>d</mi></math> can be equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>13</mn><mo>,</mo><mo>&#160;</mo><mn>14</mn><mo>,</mo><mo>&#160;</mo><mn>17</mn><mo>,</mo><mo>&#160;</mo><mn>18</mn><mo>,</mo><mo>&#160;</mo><mn>19</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> if  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8658;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>&#8658;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo></mrow></mfenced><mo>&#160;</mo><mtext>or&#160;</mtext><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>&#8658;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p><p>Hence, there are total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> elements which satisfy the given relation.</p></blockquote>

</details>

---

### Q22. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi><mo>:</mo><mn>10</mn><mo>&#8804;</mo><mi>n</mi><mo>&#8804;</mo><mn>100</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mn>3</mn></math> is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>}</mo></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>10</mn><mo>,</mo><mn>100</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>.</p><p>Let us take the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> and check whether <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mn>3</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> or not.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>1</mn></msup><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>-</mo><mn>3</mn><mo>=</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> is not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>6</mn></msup><mo>=</mo><mn>7</mn><mi>k</mi><mo>+</mo><mn>1</mn></math> is not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>7</mn></msup><mo>=</mo><mn>7</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>7</mn></msup><mo>-</mo><mn>3</mn><mo>=</mo><mn>7</mn><mi>&#945;</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>13</mn></msup><mo>=</mo><mfenced><mrow><mn>7</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>7</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mi>&#946;</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>13</mn></msup><mo>-</mo><mn>3</mn><mo>=</mo><mn>7</mn><mi>&#946;</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p>If we observe the pattern for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>13</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mn>3</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>.</p><p>That means the series forms an AP with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mn>6</mn></math>.</p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>10</mn><mo>,</mo><mn>100</mn></mrow></mfenced></math></p><p>The required progression is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>,</mo><mn>19</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>a</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>13</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>6</mn></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>6</mn><mo>&#60;</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>&#60;</mo><mn>15</mn><mo>.</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>15</mn><mo>&#8712;</mo><mi>N</mi></math></p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>.</p></blockquote>

</details>

---

### Q23. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be a relation defined on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>B</mi></math> such that  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced close=""><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mfenced open=""><msub><mi>b</mi><mn>1</mn></msub></mfenced><mo>,</mo><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced><mo>:</mo><msub><mi>a</mi><mn>1</mn></msub><mo>&#8804;</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced><mtext>&#160;and</mtext><mo>&#160;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>&#8804;</mo><msub><mi>a</mi><mn>2</mn></msub></mrow></mfenced></math>. Then the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>160</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>160</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math></p><p>And relation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced close=""><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mfenced open=""><msub><mi>b</mi><mn>1</mn></msub></mfenced><mo>,</mo><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced><mo>:</mo><msub><mi>a</mi><mn>1</mn></msub><mo>&#8804;</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced><mtext>&#160;and</mtext><mo>&#160;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>&#8804;</mo><msub><mi>a</mi><mn>2</mn></msub></mrow></mfenced></math></p><p>Now taking cases for <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>&#8804;</mo><msub><mi>b</mi><mn>2</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>&#8594;</mo><mn>5</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>&#8594;</mo><mn>4</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>&#8594;</mo><mn>4</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>8</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>&#8594;</mo><mn>2</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mn>10</mn></mfenced><mo>&#8594;</mo><mn>1</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p>So, total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math> cases will be there </p><p>Now finding cases of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>&#8804;</mo><msub><mi>a</mi><mn>2</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>&#8594;</mo><mn>4</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>6</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>&#8594;</mo><mn>2</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mn>9</mn></mfenced><mo>&#8594;</mo><mn>1</mn><mo>&#160;</mo><mtext>cases</mtext></math></p><p>So, here total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> cases,</p><p>Hence, total elements in relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>160</mn></math></p>

</details>

---

### Q24. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>12</mn></mrow></mfenced></math>. Then the number of elements in the relation  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>b</mi><mn>1</mn></msub></mrow></mfenced><mo>,</mo><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mo>&#8712;</mo><mfenced><mrow><mi>A</mi><mo>&#215;</mo><mi>B</mi><mo>,</mo><mi>A</mi><mo>&#215;</mo><mi>B</mi></mrow></mfenced><mo>:</mo><msub><mi>a</mi><mn>1</mn></msub><mo>&#160;</mo><mtext>divides</mtext><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>&#160;</mo><mtext>divides</mtext><mo>&#160;</mo><msub><mi>b</mi><mn>1</mn></msub></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>12</mn></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>&#8712;</mo><mi>A</mi><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#8712;</mo><mi>B</mi></math></p><p>Now finding elements where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>2</mn></msub></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>2</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>12</mn></mrow></mfenced></mrow></mfenced></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>&#8712;</mo><mi>A</mi><mo>,</mo><msub><mi>b</mi><mn>1</mn></msub><mo>&#8712;</mo><mi>B</mi></math></p><p>Now finding elements when <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub></math> divides <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub></math>, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>1</mn></msub></mrow></mfenced><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>2</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>12</mn></mrow></mfenced></mrow></mfenced></math></p><p>Hence, Number of relations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>6</mn><mo>&#160;</mo><mo>&#215;</mo><mo>&#160;</mo><mn>6</mn><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>36</mn></math></p></blockquote>

</details>

---

### Q25. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi><mo>:</mo><mfenced open="|" close="|"><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>n</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mo>&#60;</mo><mn>6</mn></mrow></mfenced></math> is _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>n</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mo>&#60;</mo><mn>6</mn></math></p><p>Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>&#60;</mo><mi>a</mi><mo>&#8658;</mo><mo>-</mo><mi>a</mi><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mi>a</mi></math></p><p>Now using above formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>6</mn><mo>&#60;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>n</mi><mo>+</mo><mn>19</mn><mo>&#60;</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>n</mi><mo>+</mo><mn>25</mn><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>n</mi><mo>+</mo><mn>13</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>-</mo><mfenced><mrow><mn>5</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mfenced><mrow><mn>5</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi><mo>-</mo><mfenced close="}" open="{"><mn>5</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q26. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the number of elements in sets <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be five and two respectively. Then the number of subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>B</mi></math> each having  at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and at most <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> elements is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>752</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>782</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>792</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>772</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>792</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The number of elements in sets <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be five and two respectively,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><mi>B</mi><mo>)</mo><mo>=</mo><mn>2</mn></math></p><p>Now Cartesian product will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#215;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>10</mn></math></p><p>Number of subsets having three elements <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>10</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math></p><p>Number of subsets having four elements<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>10</mn></msup><msub><mi>C</mi><mn>4</mn></msub></math></p><p>Number of subsets having five elements <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>10</mn></msup><msub><mi>C</mi><mn>5</mn></msub></math></p><p>Number of subsets having six elements <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>10</mn></msup><msub><mi>C</mi><mn>6</mn></msub></math></p><p>So, number of subsets having atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and at most <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> elements will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>10</mn></msup><msub><mi>C</mi><mn>3</mn></msub><msup><mo>+</mo><mn>10</mn></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mo>+</mo><mn>10</mn></msup><msub><mi>C</mi><mn>5</mn></msub><msup><mo>+</mo><mn>10</mn></msup><msub><mi>C</mi><mn>6</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>120</mn><mo>+</mo><mn>210</mn><mo>+</mo><mn>252</mn><mo>+</mo><mn>210</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>792</mn></math></p></blockquote>

</details>

---

### Q27. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>10</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>.</mo></math> The number of elements in the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>&#8712;</mo><mi>A</mi><mo>&#215;</mo><mi>A</mi><mo>:</mo><mn>2</mn><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>B</mi></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn><mo>}</mo><mo>&#160;&#160;</mo><mi>B</mi><mo>=</mo><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>&#8712;</mo><mi>A</mi><mo>&#215;</mo><mi>A</mi></math> such that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>-</mo><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math></p><p>Now finding discriminant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>9</mn><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mi>k</mi></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mi>k</mi></mrow></mfenced></math> a perfect square for any possible <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced></math> will be a integer,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>+</mo><mn>8</mn><mi>k</mi></math> is a perfect square</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>0</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mfenced close="]" open="["><mrow><mn>2</mn><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>&#8712;</mo><mo>{</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>&#8230;</mo><mo>.</mo><mo>(</mo><mn>10</mn><mo>,</mo><mn>10</mn><mo>)</mo><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> elements belonging to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>.</mo></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> is not possible</p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>2</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> (not possible)</p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> possible pair will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>&#8712;</mo><mo>{</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>(</mo><mn>8</mn><mo>,</mo><mn>10</mn><mo>)</mo><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn></math> elements belonging to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></p><p>Total number of elements will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn></math></p></blockquote>

</details>

---

### Q28. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be a relation from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>60</mn></mrow></mfenced></math> to itself such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>b</mi><mo>=</mo><mi>p</mi><mi>q</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><mi>q</mi><mo>&#8805;</mo><mn>3</mn></math> are prime numbers}. Then, the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>600</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>660</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>540</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>720</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>660</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>p</mi><mi>q</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>q</mi></math> are prime numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8805;</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#8804;</mo><mi>p</mi><mi>q</mi><mo>&#8804;</mo><mn>60</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>q</mi><mo>=</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>17</mn><mo>,</mo><mn>19</mn></math></p><p>And if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn></math> and so on,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>&#215;</mo><mn>5</mn><mo>,</mo><mn>3</mn><mo>&#215;</mo><mn>7</mn><mo>,</mo><mn>3</mn><mo>&#215;</mo><mn>11</mn><mo>,</mo><mn>3</mn><mo>&#215;</mo><mn>13</mn><mo>,</mo><mn>3</mn><mo>&#215;</mo><mn>17</mn><mo>,</mo><mn>3</mn><mo>&#215;</mo><mn>19</mn><mo>,</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>,</mo><mn>5</mn><mo>&#215;</mo><mn>7</mn><mo>,</mo><mn>5</mn><mo>&#215;</mo><mn>11</mn><mo>,</mo><mn>7</mn><mo>&#215;</mo><mn>7</mn></math></p><p>i.e. total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> possibilities</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8943;</mo><mo>,</mo><mn>60</mn></mrow></mfenced></math></p><p>i.e. total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math> possibilities</p><p>Hence, the number of relations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn><mo>&#215;</mo><mn>11</mn><mo>=</mo><mn>660</mn></math></p></blockquote>

</details>

---

### Q29. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math>. Then the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>C</mi><mo>&#8838;</mo><mi>A</mi><mo>:</mo><mi>C</mi><mo>&#8745;</mo><mi>B</mi><mo>&#8800;</mo><mi>&#981;</mi></mrow></mfenced></math> is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **112**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math></p><p>We know that if any set has <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> elements then total number of subset is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>n</mi></msup></math></p><p>So, total subset of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup><mo>=</mo><mn>128</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo><mi>&#981;</mi></math> when set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> contains the element <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>C</mi><mo>&#8838;</mo><mi>A</mi><mo>;</mo><mi>C</mi><mo>&#8745;</mo><mi>B</mi><mo>&#8800;</mo><mi>&#981;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Total<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfenced><mrow><mi>C</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo><mi>&#981;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>128</mn><mo>-</mo><msup><mn>2</mn><mn>4</mn></msup><mo>=</mo><mn>128</mn><mo>-</mo><mn>16</mn><mo>=</mo><mn>112</mn></math></p></blockquote>

</details>

---

### Q30. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math>. Define <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>&#8838;</mo><mi>A</mi></math>: either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#8713;</mo><mi>T</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#8712;</mo><mi>T</mi></math>} and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>&#8838;</mo><mi>A</mi><mo>:</mo><mi>T</mi></math> the sum of all the elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is a prime number.} Then the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8746;</mo><mi>C</mi></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **107**

**Detailed Solution:**

<blockquote><p>We know that,</p><p>By demorgan&#39;s law <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>B</mi><mo>&#8746;</mo><mi>C</mi></mrow></mfenced><mo>&#39;</mo></msup><mo>=</mo><msup><mi>B</mi><mo>&#39;</mo></msup><mo>&#8745;</mo><msup><mi>C</mi><mo>&#39;</mo></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mo>&#39;</mo></msup></math> is a set containing sub sets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> containing element <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and not containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>.</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>C</mi><mo>&#39;</mo></msup></math> is a set containing subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> whose sum of elements is not prime.</p><p>So, we need to calculate number of subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math> whose sum of elements plus <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> is composite.</p><p>Number of such <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> elements subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math></p><p>Number of such <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> elements subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math> (except selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>)</p><p>Number of such <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> elements subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math> (except selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced close="}" open="{"><mrow><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math>)</p><p>Number of such <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> elements subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn></math> (except selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced close="}" open="{"><mrow><mn>4</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced close="}" open="{"><mrow><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math>)</p><p>Number of such <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> elements subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math> (except selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mn>4</mn></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mn>6</mn></mfenced></math>)</p><p>Number of such <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> elements subset <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math></p><p>So, number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><msup><mi>B</mi><mo>&#39;</mo></msup><mo>&#8745;</mo><msup><mi>C</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>21</mn></math></p><p>And number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>B</mi><mo>&#8745;</mo><mi>C</mi></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup><mo>-</mo><mn>21</mn><mo>=</mo><mn>107</mn></math></p></blockquote>

</details>

---

### Q31. JEE Main 2022 (28 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> be relations on the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>50</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>p</mi><mo>,</mo><msup><mi>p</mi><mi>n</mi></msup></mrow></mfenced><mo>:</mo><mi>p</mi></math> is a prime and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8805;</mo><mn>0</mn></math> is an integer} and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>p</mi><mo>,</mo><msup><mi>p</mi><mi>n</mi></msup></mrow></mfenced><mo>:</mo><mi>p</mi></math> is a prime and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>}. Then, the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></math> is ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo><msup><mi>p</mi><mi>n</mi></msup><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mn>50</mn></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> can take values</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>17</mn><mo>,</mo><mn>23</mn><mo>,</mo><mn>29</mn><mo>,</mo><mn>31</mn><mo>,</mo><mn>37</mn><mo>,</mo><mn>41</mn><mo>,</mo><mn>43</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>47</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>{</mo><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>1</mn></msup></mrow></mfenced><mo>&#8230;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>5</mn></msup></mrow></mfenced><mo>,</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><msup><mn>3</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><msup><mn>3</mn><mn>3</mn></msup></mrow></mfenced><mo>,</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><msup><mn>5</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mfenced><mrow><mn>5</mn><mo>,</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced><mo>,</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>7</mn><mo>,</mo><msup><mn>7</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mfenced><mrow><mn>7</mn><mo>,</mo><msup><mn>7</mn><mn>2</mn></msup></mrow></mfenced><mo>,</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>11</mn><mo>,</mo><msup><mn>11</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>11</mn><mo>,</mo><msup><mn>11</mn><mn>1</mn></msup></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mn>47</mn><mo>,</mo><msup><mn>47</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>47</mn><mo>,</mo><msup><mn>47</mn><mn>1</mn></msup></mrow></mfenced><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>1</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><msup><mn>3</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><msup><mn>3</mn><mn>1</mn></msup></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mn>47</mn><mo>,</mo><msup><mn>47</mn><mn>0</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>47</mn><mo>,</mo><msup><mn>47</mn><mn>1</mn></msup></mrow></mfenced></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub><mo>&#8801;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>&#8745;</mo><msup><msub><mi>R</mi><mn>2</mn></msub><mo>'</mo></msup></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>3</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>4</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><msup><mn>2</mn><mn>5</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><msup><mn>3</mn><mn>3</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><msup><mn>7</mn><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>n</mi><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>-</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q32. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>n</mi><mo>&#8712;</mo><mo>&#160;</mo><mi>N</mi><mo>:</mo><mi mathvariant="normal">H</mi><mo>.</mo><mi mathvariant="normal">C</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>&#160;</mo><mfenced><mrow><mi>n</mi><mo>,</mo><mn>45</mn></mrow></mfenced><mo>=</mo><mn>1</mn></mrow></mfenced></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mi>k</mi><mo>:</mo><mi>k</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>100</mn></mrow></mfenced></mrow></mfenced></math>. Then the sum of all the elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5264**

**Detailed Solution:**

<p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>8</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>200</mn></mrow></mfenced></math></p><p>Sum of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><munder><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>200</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mi>Multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;2</mo></mrow></munder><mo>-</mo><munder><munder><mfenced><mrow><mn>6</mn><mo>+</mo><mn>12</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>198</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mi>Multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;&#160;</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">i</mi><mo>.</mo><mi mathvariant="normal">e</mi><mo>.&#160;</mo><mn>6</mn></mrow></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><munder><munder><mfenced><mrow><mn>10</mn><mo>+</mo><mn>20</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>200</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mi>Multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mn>5</mn><mo>&#160;</mo><mo>&#38;&#160;</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">i</mi><mo>.</mo><mi mathvariant="normal">e</mi><mo>.&#160;</mo><mn>10</mn></mrow></munder><mo>+</mo><munder><munder><mfenced><mrow><mn>30</mn><mo>+</mo><mn>60</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>180</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mi>Multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mn>2</mn><mo>,</mo><mn>5</mn><mo>&#160;</mo><mo>&#38;&#160;</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">i</mi><mo>.</mo><mi mathvariant="normal">e</mi><mo>.&#160;</mo><mn>30</mn></mrow></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mfrac><mrow><mn>100</mn><mo>&#215;</mo><mn>101</mn></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>6</mn><mfenced><mfrac><mrow><mn>33</mn><mo>&#215;</mo><mn>34</mn></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>10</mn><mfenced><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>21</mn></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>30</mn><mfenced><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>7</mn></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5264</mn></math></p>

</details>

---

### Q33. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

The sum of all the elements of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>&#945;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mn>100</mn></mrow></mfenced><mo>:</mo><mi>H</mi><mi>C</mi><mi>F</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>24</mn></mrow></mfenced><mo>=</mo><mn>1</mn></mrow></mfenced></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1633**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>&#8230;</mo><mn>100</mn></mrow></mfenced></math></p><p>Now finding the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mrow><mn>100</mn><mo>&#215;</mo><mn>101</mn></mrow><mn>2</mn></mfrac></math></p><p> Prime factors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup><mo>&#215;</mo><mn>3</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>=</mo></math> Multiples of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>=</mo></math> Multiples of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo></math> Multiples of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>&#8722;</mo><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math></p><p>To have H.C.F to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> we need to subtract the sum of multiples of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>3</mn></math> from sum of set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> to get required answer,</p><p>So required answer</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>100</mn><mo>&#215;</mo><mn>101</mn></mrow><mn>2</mn></mfrac><mo>&#8722;</mo></math> Sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>100</mn><mo>&#215;</mo><mn>101</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>&#215;</mo><mfrac><mrow><mn>50</mn><mo>&#215;</mo><mn>51</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>33</mn><mn>2</mn></mfrac><mfenced><mn>102</mn></mfenced><mo>&#8722;</mo><mfrac><mn>16</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>102</mn></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1633</mn></math></p>

</details>

---

### Q34. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math> be the set of all integers,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi>Z</mi><mo>&#215;</mo><mi>Z</mi><mo>:</mo><mo>(</mo><mi>x</mi><mo>&#8722;</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi>Z</mi><mo>&#215;</mo><mi>Z</mi><mo>:</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn></mrow></mfenced><mtext>&#160;and&#160;</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi>Z</mi><mo>&#215;</mo><mi>Z</mi><mo>:</mo><mo>(</mo><mi>x</mi><mo>&#8722;</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>y</mi><mo>&#8722;</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn></mrow></mfenced></math>
If the total number of relations from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>p</mi></msup></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>49</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi>Z</mi><mo>&#215;</mo><mi>Z</mi><mo>;</mo><mo>(</mo><mi>x</mi><mo>&#8722;</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8804;</mo><mi>Z</mi><mo>&#215;</mo><mi>Z</mi><mo>;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi>Z</mi><mo>&#215;</mo><mi>Z</mi><mo>;</mo><mo>(</mo><mi>x</mi><mo>&#8722;</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>y</mi><mo>&#8722;</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/742d1d85-2a62-4d75-b7f1-b69df9089094-image.png" style="width: 387px; height: 300px;" /></p><p>Here, we can see from the above diagram <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo><mo>{</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>}</mo><mo>&#8658;</mo><mi>n</mi><mo>(</mo><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>)</mo><mo>=</mo><mn>5</mn></math></p><p>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><mi>A</mi><mo>&#8745;</mo><mi>C</mi><mo>)</mo><mo>=</mo><mn>5</mn></math></p><p>Relation from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>C</mi><mo>=</mo><msup><mn>2</mn><mrow><mn>5</mn><mo>&#215;</mo><mn>5</mn></mrow></msup><mo>=</mo><msup><mn>2</mn><mi>p</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>25</mn></math></p>

</details>

---

### Q35. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>&#8739;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>n</mi><mo>+</mo><mn>10</mn><mo>,</mo><mn>000</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>3</mn><mi>k</mi><mo>+</mo><mn>1</mn><mo>&#8739;</mo><mi>k</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mi>k</mi><mo>&#8739;</mo><mi>k</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced><mo>,</mo></math> then the sum of all the elements of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **832**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>n</mi><mo>&#8712;</mo><mi mathvariant="bold-italic">N</mi><mo>&#8739;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>&#8804;</mo><mi>n</mi><mo>+</mo><mn>10</mn><mo>,</mo><mn>000</mn></mrow></mfenced><mo>,</mo><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>3</mn><mi>k</mi><mo>+</mo><mn>1</mn><mo>&#8739;</mo><mi>k</mi><mo>&#8712;</mo><mi mathvariant="bold-italic">N</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mi>k</mi><mo>&#8739;</mo><mi>k</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8801;</mo><mfenced close="}" open="{"><mrow><mn>4</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>16</mn><mo>,</mo><mn>19</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>&#8801;</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>14</mn><mo>,</mo><mn>16</mn><mo>,</mo><mn>20</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>-</mo><mi>C</mi><mo>&#8801;</mo><mfenced close="}" open="{"><mrow><mn>7</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>19</mn><mo>,</mo><mo>&#8230;</mo><mn>97</mn><mo>,</mo><mo>&#8230;</mo></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi><mo>&#8804;</mo><mn>100</mn><mo>&#215;</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>100</mn><mo>&#215;</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>100</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mfenced><mrow><mi>B</mi><mo>-</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mfenced close="}" open="{"><mrow><mn>7</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>19</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>97</mn></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>7</mn><mo>+</mo><mn>13</mn><mo>+</mo><mn>19</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>97</mn></math></p><p>Clearly, the terms are in arithmetic progression. Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mn>13</mn><mo>-</mo><mn>7</mn><mo>=</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>97</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>=</mo><mn>97</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the number of terms.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>6</mn><mo>=</mo><mn>97</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>6</mn><mo>=</mo><mn>90</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>16</mn></math></p><p>Hence, sum <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>7</mn><mo>+</mo><mn>13</mn><mo>+</mo><mn>19</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>97</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced><mrow><mi>a</mi><mo>+</mo><mi>l</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>16</mn><mn>2</mn></mfrac><mfenced><mrow><mn>7</mn><mo>+</mo><mn>97</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>832</mn><mo>.</mo></math></p>

</details>

---

### Q36. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mn>30</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mo>&#8771;</mo><mo>&#39;</mo></math> be an equivalence relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>A</mi><mo>,</mo></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8771;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>,</mo></math> if and only if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>=</mo><mi>b</mi><mi>c</mi></math>. Then the number of ordered pairs which satisfy this equivalence relation with ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mo>,</mo><mn>30</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mo>=</mo><mi>b</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mn>4</mn><mi>d</mi><mo>=</mo><mn>3</mn><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>c</mi><mi>d</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>c</mi><mi>d</mi></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>30</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>12</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>16</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>20</mn><mo>,</mo><mn>15</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>24</mn><mo>,</mo><mn>18</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>28</mn><mo>,</mo><mn>21</mn></mrow></mfenced></mrow></mfenced></math></p><p>No. of ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q37. JEE Main 2021 (24 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>:</mo><mi>n</mi></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math>digit number<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>}</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>9</mn><mi>k</mi><mo>+</mo><mn>2</mn><mo>:</mo><mi>k</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>9</mn><mi>k</mi><mo>+</mo><mi>l</mi><mo>:</mo><mi>k</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mfenced><mrow><mn>0</mn><mo>&#60;</mo><mi>l</mi><mo>&#60;</mo><mn>9</mn></mrow></mfenced></math>. If the sum of all the elements of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mfenced><mrow><mi>B</mi><mo>&#8746;</mo><mi>C</mi></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>274</mn><mo>&#215;</mo><mn>400</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> will contain three digit numbers of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>k</mi><mo>+</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>k</mi><mo>+</mo><mi>l</mi></math> respectively. We need to find sum of all elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8746;</mo><mi>C</mi></math> effectively.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mfenced><mrow><mi>B</mi><mo>&#8746;</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mi>S</mi><mfenced><mi>B</mi></mfenced><mo>+</mo><mi>S</mi><mfenced><mi>C</mi></mfenced><mo>-</mo><mi>S</mi><mfenced><mrow><mi>B</mi><mo>&#8745;</mo><mi>C</mi></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>(</mo><mi>k</mi><mo>)</mo></math> denotes sum of elements of set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>.</mo></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>101</mn><mo>,</mo><mn>110</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>992</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>S</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfrac><mn>100</mn><mn>2</mn></mfrac><mfenced><mrow><mn>101</mn><mo>+</mo><mn>992</mn></mrow></mfenced><mo>=</mo><mn>54650</mn></math></p><p><strong>Case-I:</strong> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>2</mn></math></p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8745;</mo><mi>C</mi><mo>=</mo><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>S</mi><mfenced><mrow><mi>B</mi><mo>&#8746;</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mi>S</mi><mfenced><mi>B</mi></mfenced></math></p><p>which is not possible as given sum is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>274</mn><mo>&#215;</mo><mn>400</mn><mo>=</mo><mn>109600</mn><mo>.</mo></math></p><p>Case-II If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>&#8800;</mo><mn>2</mn></math></p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8745;</mo><mi>C</mi><mo>=</mo><mi>&#981;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>S</mi><mfenced><mrow><mi>B</mi><mo>&#8746;</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mi>S</mi><mfenced><mi>B</mi></mfenced><mo>+</mo><mi>S</mi><mfenced><mi>C</mi></mfenced><mo>=</mo><mn>400</mn><mo>&#215;</mo><mn>274</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>54650</mn><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>110</mn></munderover><mn>9</mn><mi>k</mi><mo>+</mo><mi>l</mi><mo>=</mo><mn>109600</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>9</mn><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>11</mn></mrow><mn>110</mn></munderover><mi>k</mi><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>11</mn></mrow><mn>110</mn></munderover><mi>l</mi><mo>=</mo><mn>54950</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>9</mn><mfenced><mrow><mfrac><mn>100</mn><mn>2</mn></mfrac><mfenced><mrow><mn>11</mn><mo>+</mo><mn>110</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>l</mi><mfenced><mn>100</mn></mfenced><mo>=</mo><mn>54950</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>54450</mn><mo>+</mo><mn>100</mn><mi>l</mi><mo>=</mo><mn>54950</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>l</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q38. JEE Main 2020 (06 Sep Shift 1)

*Type:* `numerical` | *Level:* `2`

Set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>elements and set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>elements. If the total number of subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>112</mn></math> more than the total number of subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#183;</mo><mi>n</mi></math> is___.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **28**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>m</mi></msup><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mo>+</mo><mn>112</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>m</mi></msup><mo>-</mo><msup><mn>2</mn><mi>n</mi></msup><mo>=</mo><mn>112</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#183;</mo><mfenced><mrow><msup><mn>2</mn><mrow><mi>m</mi><mo>-</mo><mi>n</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>4</mn></msup><mo>&#183;</mo><mfenced><mrow><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>7</mn></math>

</details>

---

### Q39. JEE Main 2020 (07 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>:</mo><mn>1</mn><mo>&#8804;</mo><mi>n</mi><mo>&#8804;</mo><mn>50</mn></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mi>n</mi><mo>&#8712;</mo><mi>X</mi><mo>:</mo><mo>&#160;</mo><mi>n&#160;</mi><mi mathvariant="normal">i</mi><mi>s&#160;</mi><mi>a&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">l</mi><mi>e&#160;</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">f</mi><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mi>n</mi><mo>&#8712;</mo><mi>X</mi><mo>:</mo><mo>&#160;</mo><mi>n&#160;</mi><mi mathvariant="normal">i</mi><mi>s&#160;</mi><mi>a&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">l</mi><mi>e&#160;</mi><mi mathvariant="normal">o</mi><mi>f&#160;</mi><mn>7</mn></mrow></mfenced></math>, then the number of elements in the smallest subset of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>, containing both <math><mi mathvariant="normal">A</mi></math> and <math><mi mathvariant="normal">B</mi></math>, is.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **29**

**Detailed Solution:**

<p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>50</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>7</mn><mo>,</mo><mn>14</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>49</mn></mrow></mfenced></math></p><p>Required smallest subset is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8746;</mo><mi>B</mi></math>.</p><p>So, <math><mi>n</mi><mfenced separators="|"><mrow><mi mathvariant="normal">A</mi><mo>&#8746;</mo><mi mathvariant="normal">B</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mfenced separators="|"><mrow><mi mathvariant="normal">A</mi></mrow></mfenced><mo>+</mo><mi>n</mi><mfenced separators="|"><mrow><mi mathvariant="normal">B</mi></mrow></mfenced><mo>-</mo><mi>n</mi><mfenced separators="|"><mrow><mi mathvariant="normal">A</mi><mo>&#8745;</mo><mi mathvariant="normal">B</mi></mrow></mfenced></math>
<math><mo>=</mo><mn>25</mn><mo>+</mo><mn>7</mn><mo>-</mo><mn>3</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>29</mn></math>.</p>

</details>

---

### Q40. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>Z</mi></math> be the set of integers. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mi>x</mi><mo>&#8712;</mo><mi>Z</mi><mtext>&#8201;</mtext><mo>:</mo><mo>&#160;</mo><msup><mn>2</mn><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced></mrow></msup><mo>=</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>Z</mi><mtext>&#8201;&#8201;</mtext><mo>:</mo><mo>-</mo><mtext>&#8201;</mtext><mn>3</mn><mo>&#60;</mo><mtext>&#8201;</mtext><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#60;</mo><mn>9</mn><mo>}</mo></math>, then the number of subsets of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>B</mi></math>, is :

**Options:**

- **(A)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>12</mn></mrow></msup></math>
- **(B)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>18</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></msup></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></msup><mo>=</mo><mn>1</mn><mo>=</mo><msup><mn>2</mn><mn>0</mn></msup><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn></math>.</p><p><math><mo>&#8756;</mo><mi>n</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p>Again, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn><mo>&#60;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>&#60;</mo><mn>9</mn><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>n</mi><mfenced separators="|"><mi>B</mi></mfenced><mo>=</mo><mn>5</mn></math></p><p><math><mo>&#8756;</mo><mi>n</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#215;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>15</mn></math></p><p><math><mo>&#8756;</mo></math>Number of subset of <math><mi>A</mi><mo>&#215;</mo><mi>B</mi><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></msup></math></p>

</details>

---

### Q41. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A relation on the set $\mathrm{A}=\{\mathrm{x}:|\mathrm{x}| < 3, \mathrm{x} \in \mathrm{Z}\}$, where $Z$ is the set of integers is defined by $\mathrm{R}=\{(\mathrm{x}, \mathrm{y}): \mathrm{y}=|\mathrm{x}|, \mathrm{x} \neq-1\}$. Then the number of elements in the power set of $R$ is:

**Options:**

- **(A)** 32
- **(B)** 16
- **(C)** 8
- **(D)** 64

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 16**

**Detailed Solution:**

$$
\begin{aligned}
&\mathrm{A}=\{x:|x| < 3, x \in Z\} \\
&\mathrm{A}=\{-2,-1,0,1,2\} \\
&\mathrm{R}=\{(x, y): y=|x|, x \neq-1\} \\
&\mathrm{R}=\{(-2,2),(0,0),(1,1),(2,2)\}
\end{aligned}
$$
$\mathrm{R}$ has four elements
Number of elements in the power set of $\mathrm{R}$
$$
=2^4=16
$$

</details>

---

### Q42. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be two sets containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> elements and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> elements respectively. The number of subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>B</mi></math> having <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or more elements is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>219</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>211</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>256</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>219</mn></math>**

**Detailed Solution:**

As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mn>4</mn></math>

Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#215;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>8</mn></math>

Now subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>B</mi></math> containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or more elements will be
=Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> (no element <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> one element <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math> elements)

=<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>8</mn></msup><msup><mo>-</mo><mn>8</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mo>-</mo><mn>8</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>-</mo><mn>8</mn></msup><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mn>1</mn><mn>9</mn></math>

</details>

---

### Q43. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left\{x \in z^{+}: x < 10\right.$ and $x$ is a multiple of 3 or $4\}$, where $z^{+}$is the set of positive integers, then the total number of symmetric relations on $A$ is

**Options:**

- **(A)** $2^5$
- **(B)** $2^{15}$
- **(C)** $2^{10}$
- **(D)** $2^{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2^{15}$**

**Detailed Solution:**

A relation on a set A is said to be symmetric iff $(a, b) \in A \Rightarrow(b, a) \in A, \forall a, b \in A$
Here $A=\{3,4,6,8,9\}$
Number of order pairs of $A \times A=5 \times 5=25$
Divide 25 order pairs of $A \times A$ in 3 parts as follows :
$$
\begin{aligned}
& \text { Part }-A:(3,3),(4,4),(6,6),(8,8),(9,9) \\
& \text { Part }-B:(3,4),(3,6),(3,8),(3,9),(4,6), \\
& (4,8),(4,9),(6,8),(6,9),(8,9) \\
& \text { Part-C:(4,3),(6,3),(8,3),(9,3),(6,4),(8,4), } \\
& (9,4),(8,6),(9,6),(9,8)
\end{aligned}
$$
In part $-A$, both components of each order pair are same.
In part $-B$, both components are different but not two such order pairs are present in which first component of one order pair is the second component of another order pair and vice-versa.
In part $-C$, only reverse of the order pairs of part $-B$ are present i.e., if $(a, b)$ is present in part $-B$, then (b, a) will be present in part $-C$ For example $(3,4)$ is present in part $-B$ and $(4,3)$ present in part $-C$.
Number of order pair in $A, B$ and $C$ are 5, 10 and 10 respectively.
In any symmetric relation on set $A$, if any order pair of part $-B$ is present then its reverse order pair of part $-C$ will must be also present.
Hence number of symmetric relation on set $A$ is equal to the number of all relations on a set $D$, which contains all the order pairs of part $-A$ and part $-B$.
Now $n(D)=n(A)+n(B)=5+10=15$
Hence number of all relations on set $D=(2)^{15}$
$\Rightarrow$ Number of symmetric relations on set $D=(2)^{15}$

</details>

---

