# JEE Main Mathematics - Sets and Relations

## Topic 1: Questions on Symmetric Transitive and Reflexive Properties

**Total Questions:** 59

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the relation R on the set $\{-2,-1,0,1,2\}$ defined by $(a, b) \in R$ if and only if $1+ab > 0$. Then, among the statements:
I. The number of elements in R is 17
II. R is an equivalence relation

**Options:**

- **(A)** Only I is true
- **(B)** Only II is true
- **(C)** Both I and II are true
- **(D)** Neither I nor II is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Only I is true**

**Detailed Solution:**

The set is $A = \{-2, -1, 0, 1, 2\}$.

For Statement I, the relation is defined as $(a, b) \in R \iff 1 + ab > 0$.
The pairs $(a, b)$ that do not belong to $R$ satisfy $1 + ab \le 0 \Rightarrow ab \le -1$.
The pairs satisfying $ab \le -1$ are $(-2, 1), (-2, 2), (-1, 1), (-1, 2), (1, -2), (1, -1), (2, -2), (2, -1)$.
There are $8$ such pairs.
The total number of pairs in $A \times A$ is $5 \times 5 = 25$.
The number of elements in $R$ is $25 - 8 = 17$.
Thus, Statement I is true.

For Statement II, checking transitivity gives $(-2, 0) \in R$ since $1 + (-2)(0) = 1 > 0$.
Also, $(0, 2) \in R$ since $1 + (0)(2) = 1 > 0$.
However, $(-2, 2) \notin R$ since $1 + (-2)(2) = -3 \le 0$.
Since $R$ is not transitive, it is not an equivalence relation.
Thus, Statement II is false.

Answer: Only I is true

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $R = \{(x, y) \in \mathbb{N} \times \mathbb{N} : \log_e(x + y) \leq 2\}$. Then the minimum number of elements, required to be added in $R$ to make it a transitive relation, is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

Given the relation $R = \{(x, y) \in \mathbb{N} \times \mathbb{N} : \log_e(x + y) \leq 2\}$.

This condition simplifies to:
$x + y \leq e^2$

Since $e \approx 2.718$, we have $e^2 \approx 7.389$.
As $x, y \in \mathbb{N}$, the sum $x + y$ must be a natural number. Therefore, the condition becomes:
$x + y \leq 7$

Let's find the number of elements in $R$ by listing the possible pairs $(x, y)$:
For $x = 1$, $y \in \{1, 2, 3, 4, 5, 6\}$ (6 elements)
For $x = 2$, $y \in \{1, 2, 3, 4, 5\}$ (5 elements)
For $x = 3$, $y \in \{1, 2, 3, 4\}$ (4 elements)
For $x = 4$, $y \in \{1, 2, 3\}$ (3 elements)
For $x = 5$, $y \in \{1, 2\}$ (2 elements)
For $x = 6$, $y \in \{1\}$ (1 element)

Total number of elements in $R = 6 + 5 + 4 + 3 + 2 + 1 = 21$.

To make $R$ a transitive relation, we must ensure that if $(x, y) \in R$ and $(y, z) \in R$, then $(x, z) \in R$.
Notice that $(x, 1) \in R$ for all $x \in \{1, 2, 3, 4, 5, 6\}$ and $(1, z) \in R$ for all $z \in \{1, 2, 3, 4, 5, 6\}$.
For the relation to be transitive, it must contain $(x, z)$ for all possible combinations of $x$ and $z$ from the set $A = \{1, 2, 3, 4, 5, 6\}$.

Thus, the transitive closure of $R$ will be the Cartesian product $A \times A$, which contains $6 \times 6 = 36$ elements.

The minimum number of elements required to be added to $R$ to make it transitive is the difference between the number of elements in the transitive closure and the number of elements already in $R$:
Minimum elements to add $= 36 - 21 = 15$.

Answer: $15$

</details>

---

### Q3. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=\{0,1,2, \ldots, 9\}$. Let R be a relation on A defined by $(x, y) \in \mathrm{R}$ if and only if $|x-y|$ is a multiple of 3. Given below are two statements: 
 <b>Statement I</b>: $n(\mathrm{R})=36$. 
 <b>Statement II</b>: $R$ is an equivalence relation. 
 In the light of the above statements, choose the correct answer from the options given below

**Options:**

- **(A)** Statement I is incorrect but Statement II is correct
- **(B)** Statement I is correct but Statement II is incorrect
- **(C)** Both Statement I and Statement II are incorrect
- **(D)** Both Statement I and Statement II are correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement I is incorrect but Statement II is correct**

**Detailed Solution:**

The relation $R$ on $A = \{0,1,2,\ldots,9\}$ is defined by $(x,y) \in R$ iff $|x-y|$ is a multiple of 3, i.e., $x \equiv y \pmod{3}$.
Statement II:
$R$ is reflexive ($|x-x|=0$, a multiple of 3), symmetric ($|x-y|=|y-x|$), and transitive (if $x \equiv y$ and $y \equiv z \pmod{3}$, then $x \equiv z \pmod{3}$). So $R$ is an equivalence relation. Statement II is correct.
Statement I:
The equivalence classes are $\{0,3,6,9\}$ (4 elements), $\{1,4,7\}$ (3 elements), $\{2,5,8\}$ (3 elements).
$n(R) = 4^2 + 3^2 + 3^2 = 16 + 9 + 9 = 34 \neq 36$. Statement I is incorrect.

</details>

---

### Q4. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{A}=\{-2,-1,0,1,2,3,4\}$. Let R be a relation on A defined by $x \mathrm{Ry}$ if and only if $2 x+y \leqslant 2$. Let $l$ be the number of elements in R. Let m and n be the minimum number of elements required to be added in $R$ to make it reflexive and symmetric relations respectively. Then $l+m+n$ is equal to :

**Options:**

- **(A)** 35
- **(B)** 34
- **(C)** 33
- **(D)** 32

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 33**

**Detailed Solution:**

Given $A = \{-2, -1, 0, 1, 2, 3, 4\}$ and $xRy$ iff $2x + y \leqslant 2$.
For $x = -2$: $y \leqslant 6$, all 7 elements valid (7 pairs).
For $x = -1$: $y \leqslant 4$, all 7 elements valid (7 pairs).
For $x = 0$: $y \leqslant 2 \Rightarrow y \in \{-2,-1,0,1,2\}$ (5 pairs).
For $x = 1$: $y \leqslant 0 \Rightarrow y \in \{-2,-1,0\}$ (3 pairs).
For $x = 2$: $y \leqslant -2 \Rightarrow y \in \{-2\}$ (1 pair).
For $x = 3, 4$: no valid $y$.
So $l = 7+7+5+3+1 = 23$.
For reflexive: $(x,x) \in R \Rightarrow 3x \leqslant 2 \Rightarrow x \leqslant 2/3$. Already present for $x = -2, -1, 0$. Missing for $x = 1, 2, 3, 4$, so $m = 4$.
For symmetric: need $(y,x) \in R$ for every $(x,y) \in R$. Missing pairs: $(3,-2), (4,-2), (2,-1), (3,-1), (4,-1), (2,0)$, so $n = 6$.
$l + m + n = 23 + 4 + 6 = 33$.

</details>

---

### Q5. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the relation R on the set $\mathrm{M}=\{1,2,3, \ldots, 16\}$ be given by $\mathrm{R}=\{(x, y): 4 y=5 x-3, x, y \in \mathrm{M}\}$. Then the minimum number of elements required to be added in R, in order to make the relation symmetric, is equal to

**Options:**

- **(A)** 4
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2**

**Detailed Solution:**

Given $R = \{(x, y) : 4y = 5x - 3,\ x, y \in M\}$ where $M = \{1, 2, \ldots, 16\}$.
From $4y = 5x - 3$, we get $y = \frac{5x-3}{4}$.
For $y$ to be a positive integer, $5x - 3 \equiv 0 \pmod{4}$, i.e., $x \equiv 3 \pmod{4}$.
So $x = 3, 7, 11, 15$.
$x=3 \Rightarrow y=3$,
$x=7 \Rightarrow y=8$,
$x=11 \Rightarrow y=13$,
$x=15 \Rightarrow y=18 \notin M$.
$R = \{(3,3),\ (7,8),\ (11,13)\}$.
For symmetry, $(7,8) \in R$ requires $(8,7) \in R$ and $(11,13) \in R$ requires $(13,11) \in R$.
$(3,3)$ is already symmetric.
Minimum elements to be added $= 2$.

</details>

---

### Q6. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=\{2,3,5,7,9\}$. Let R be the relation on A defined by $x \mathrm{R} y$ if and only if $2 x \leq 3 y$. Let $l$ be the number of elements in R, and m be the minimum number of elements required to be added in R to make it a symmetric relation. Then $l+\mathrm{m}$ is equal to :

**Options:**

- **(A)** 21
- **(B)** 27
- **(C)** 23
- **(D)** 25

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 25**

**Detailed Solution:**

Given $A = \{2, 3, 5, 7, 9\}$ and $xRy$ iff $2x \le 3y$, i.e., $y \ge \frac{2x}{3}$.
For $x=2$: $y \in \{2,3,5,7,9\}$ → 5 pairs
For $x=3$: $y \in \{2,3,5,7,9\}$ → 5 pairs
For $x=5$: $y \in \{5,7,9\}$ → 3 pairs
For $x=7$: $y \in \{5,7,9\}$ → 3 pairs
For $x=9$: $y \in \{7,9\}$ → 2 pairs
So $l = 18$.
For symmetry, pairs in $R$ whose reversal is missing: $(2,5),(2,7),(2,9),(3,5),(3,7),(3,9),(5,9)$ require adding $(5,2),(7,2),(9,2),(5,3),(7,3),(9,3),(9,5)$ → $m = 7$.
$l + m = 18 + 7 = 25$.

</details>

---

### Q7. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\{0,1,2,3,4,5\}$. Let $R$ be a relation on A defined by $(x, y) \in R$ if and only if max $\{x, y\} \in\{3,4\}$. Then among the statements $\left(\mathrm{S}_1\right)$ : The number of elements in R is 18 , and $\left(\mathrm{S}_2\right)$ : The relation R is symmetric but neither reflexive nor transitive

**Options:**

- **(A)** both are true
- **(B)** both are false
- **(C)** only $\left(\mathrm{S}_2\right)$ is true
- **(D)** only $\left(\mathrm{S}_1\right)$ is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) only $\left(\mathrm{S}_2\right)$ is true**

**Detailed Solution:**

$A=\{0,1,2,3,4,5\}$
$\mathrm{R} \equiv\{(0,3),(3,0),(0,4),(4,0),(1,3),(3,1),(1,4)$,
$(4,1),(2,3),(3,2),(2,4),(4,2),(3,3),(3,4),(4,3)$,
$(4,4)\}$
Total 16 elements
Not reflexive as $(0,0), \ldots \ldots,(2,2) \notin \mathrm{R}$
Symmetric $\because \forall$ all a,b
$(a, b) \&(b, a) \in R$
Not transitive $\because(0,3),(3,1) \in R$
but $(0,1) \notin \mathrm{R}$
$\Rightarrow$ Only $\mathrm{S}_2$ correct

</details>

---

### Q8. JEE Main 2025 (7 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of relations on the set $\mathrm{A}=\{1,2,3\}$ containing at most 6 elements including $(1,2)$, which are reflexive and transitive but not symmetric, is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

$\begin{aligned}
& A=\{1,2,3\} \\
& (1,1),(2,2),(3,3),(1,2) \in R
\end{aligned}$
Remaining elements are
$(2,1),(2,3),(1,3),(3,1),(3,2)$
(1) If relation contains exactly 4 elements = 1 way
(2) if relation contains exactly 5 elements
It can be $(1,3),(3,2) \Rightarrow 2$ ways
(3) If relation contain exactly 6 elements
It can be $((2,3),(1,3)),((1,3),(3,2)),((3,1),(3,2))$
$\Rightarrow 3$ ways.
Total $=6$ ways

</details>

---

### Q9. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{A}=\{-3,-2,-1,0,1,2,3\}$ and R be a relation on $A$ defined by $x R y$ if and only if $2 x-y \in\{0,1\}$. Let $l$ be the number of elements in R. Let $m$ and $n$ be the minimum number of elements required to be added in R to make it reflexive and symmetric relations, respectively. Then $l+\mathrm{m} \mathrm{n}$ is equal to :-

**Options:**

- **(A)** $18$
- **(B)** $17$
- **(C)** $15$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $17$**

**Detailed Solution:**

$\begin{aligned} & \begin{array}{l}2 \mathrm{x}-\mathrm{y}=0 \\ \{0,0\}\{-1,-2\}\{1,2\} \\ 2 \mathrm{x}-\mathrm{y}=1\end{array} \\ & \{0,-1\}\{1,1\}\{2,3\}\{-1,-3\} \\ & \text { Total }(0,0)(-1,-2),(1,2)(0,-1),(1,1)(2,3)(-1,-3) \\ & \text { Reflexive } \quad \mathrm{m}=5 \quad \& \ell=7 \\ & \text { Symm. } \quad \mathrm{n}=5 \quad \ell+\mathrm{m}+\mathrm{n}=17 \\ & \text { option (2) }\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\{-2,-1,0,1,2,3\}$. let R be a relation on A defined by $x R y$ if and only if $y=\max \{x, 1\}$. Let $l$ be the number of elements in R. Let m and n be the minimum number of elements required to be added in R to make it reflexive and symmetric relations, respectively. Then $l+\mathrm{m}+\mathrm{n}$ is equal to

**Options:**

- **(A)** $12$
- **(B)** $11$
- **(C)** $13$
- **(D)** $14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $12$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{A}=\{-2,-1,0,1,2,3\} \\ & \mathrm{R}=\{(-2,1),(-1,1),(0,1),(1,1),(2,2),(3,3)\} \\ & \ell=6 \\ & \mathrm{~m}=3 \\ & \mathrm{n}=3 \\ & \ell+\mathrm{m}+\mathrm{n}=12\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\{-3,-2,-1,0,1,2,3$,$\} . Let R$ be a relation on A defined by $x R y$ if and only if $0 \leq x^2+2 y \leq 4$.
Let $l$ be the number of elements in R and $m$ be the minimum number of elements required to be added in R to make it a reflexive relation. then $l+m$ is equal to

**Options:**

- **(A)** $19$
- **(B)** $20$
- **(C)** $17$
- **(D)** $18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $18$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{A}=\{-3,-2,-1,0,1,2,3\} \\ & -2 \mathrm{y} \leq \mathrm{x}^2 \leq 4-2 \mathrm{y}\end{aligned}$
$\begin{array}{lll}y=-3 & 6 \leq x^2 \leq 10 & \Rightarrow x \in\{-3,3\} \\ y=-2 & 4 \leq x^2 \leq 8 & \Rightarrow x \in\{-2,2\} \\ y=-1 & 2 \leq x^2 \leq 6 & \Rightarrow x \in\{-2,2\} \\ y=0 & 0 \leq x^2 \leq 4 & \Rightarrow x \in\{-2,-1,0,1,2\} \\ y=1 & -2 \leq x^2 \leq 2 & \Rightarrow x \in\{-1,0,1\} \\ y=2 & -4 \leq x^2 \leq 0 & \Rightarrow x \in\{0\} \\ y=3 & -6 \leq x^2 \leq-2 & \Rightarrow \text { No } x \text {-Exist }\end{array}$
$\begin{aligned} & \mathrm{R}=\{(-3,-3)(-3,3),(-2,-2)(-2,2)(-1,-2)(-1,2) \\ & (0,-2)(0,-1)(0,0)(0,1)(0,2)(1,-1)(1,0)(1,1) \\ & (2,0)\} \\ & \therefore \ell=15\end{aligned}$
To make it reflexive we will add
$\begin{aligned} & \{(-1,-1),(2,2),(3,3)\} \quad \therefore \mathrm{m}=3 \\ & \therefore \ell+\mathrm{m}=15+3=18\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let A be the set of all functions $f: \mathbf{Z} \rightarrow \mathbf{Z}$ and R be a relation on A such that $\mathrm{R}=\{(\mathrm{f}, \mathrm{g}): f(0)=\mathrm{g}(1)$ and $f(1)=\mathrm{g}(0)\}$. Then R is:

**Options:**

- **(A)** Symmetric and transitive but not reflective
- **(B)** Symmetric but neither reflective nor transitive
- **(C)** Reflexive but neither symmetric nor transitive
- **(D)** Transitive but neither reflexive nor symmetric

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Symmetric but neither reflective nor transitive**

**Detailed Solution:**

$\begin{aligned} & \mathrm{R}=\{(\mathrm{f}, \mathrm{g}): \mathrm{f}(0)=\mathrm{g}(1) \text { and } \mathrm{f}(1)=\mathrm{g}(0)\} \\ & \text { Reflexive: }(\mathrm{f}, \mathrm{f}) \in \mathrm{R} \\ & =\mathrm{f}(0)=\mathrm{f}(1) \text { and } \mathrm{f}(1)=\mathrm{f}(0) \rightarrow \text { must hold } \\ & \Rightarrow \text { but this is not true for all function }\end{aligned}$
so not reflexive
Symmetric: If $(\mathrm{f}, \mathrm{g}) \in \mathrm{R} \Rightarrow(\mathrm{g}, \mathrm{f}) \in \mathrm{R}$
Now, $g(0)=f(1)$ and $g(1)=f(0) \rightarrow$ true
$\therefore$ symmetric
Transitive : $\operatorname{If}(\mathrm{f}, \mathrm{g}) \in \mathrm{R}$ and $(\mathrm{g}, \mathrm{h}) \in \mathrm{R}$
$\Rightarrow(\mathrm{f}, \mathrm{h}) \in \mathrm{R}$
Now $(f, g) \in R \Rightarrow f(0)=g(1)$ and $f(1)=g(0)$
$(\mathrm{g}, \mathrm{h}) \in \mathrm{R} \Rightarrow \mathrm{g}(0)=\mathrm{h}(1)$ and $\mathrm{g}(1)=\mathrm{h}(0)$
For $(f, h) \in R$ we need $f(0)=h(1)$ and $f(1)=h(0)$
Now $f(0)=g(1)=h(0)$ and $f(1)=g(0)=h(1)$
Hence not transitive

</details>

---

### Q13. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Define a relation R on the interval \(\left[0, \frac{\pi}{2}\right)\) by \(x \mathrm{R} y\) if and only if \(\sec ^2 x-\tan ^2 y=1\). Then R is :

**Options:**

- **(A)** both reflexive and transitive but not symmetric
- **(B)** an equivalence relation
- **(C)** reflexive but neither symmetric not transitive
- **(D)** both reflexive and symmetric but not transitive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) an equivalence relation**

**Detailed Solution:**

$\begin{aligned}
& \sec ^2 x-\tan ^2 x=1 \quad(\text { on replacing } y \text { with } x) \\
& \Rightarrow \text { Reflexive } \\
& \sec ^2 x-\tan ^2 y=1 \\
& \Rightarrow 1+\tan ^2 x+1-\sec ^2 y=1 \\
& \Rightarrow \sec ^2 y-\tan ^2 x=1 \\
& \Rightarrow \text { symmetric } \\
& \sec ^2 x-\tan ^2 y=1 \\
& \sec ^2 y-\tan ^2 z=1
\end{aligned}$

Adding both

$\begin{aligned}
& \Rightarrow \sec ^2 x-\tan ^2 y+\sec ^2 y-\tan ^2 z=1+1 \\
& \sec ^2 x+1-\tan ^2 z=2 \\
& \sec ^2 x-\tan ^2 z=1 \\
& \Rightarrow \text { Transitive }
\end{aligned}$
hence equivalence releation

</details>

---

### Q14. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The relation $R=\{(x, y): x, y \in \mathbb{Z}$ and $x+y$ is even $\}$ is:

**Options:**

- **(A)** reflexive and symmetric but not transitive
- **(B)** an equivalence relation
- **(C)** symmetric and transitive but not reflexive
- **(D)** reflexive and transitive but not symmetric

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) an equivalence relation**

**Detailed Solution:**

For reflexive $(x, x) \in \mathbb{R}, x \in \mathbb{Z}$
$\Rightarrow x+x=2 x \rightarrow \text { even }$
For symmetric of $(x, y) \in \mathbb{R}$ then $(y, x) \in \mathbb{R}$ when $x, y \in \mathbb{Z}$
$x+y \rightarrow$ even
$\Rightarrow y+x \rightarrow \text { even }$
for transitive if $(x, y) \in \mathbb{R} \Rightarrow x+y \rightarrow$ even
$(y, z) \in \mathbb{R} \Rightarrow y+z \rightarrow \text { even }$
$x+2 y+z \rightarrow$ even
$\Rightarrow x+z$ is even
$\Rightarrow(x, z) \in \mathbb{R}$
$\Rightarrow \mathbb{R}$ is an equivalence relation.

</details>

---

### Q15. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $X=\mathbf{R} \times \mathbf{R}$. Define a relation $R$ on $X$ as :
$\left(a_1, b_1\right) R\left(a_2, b_2\right) \Leftrightarrow b_1=b_2$

Statement I : $\quad \mathrm{R}$ is an equivalence relation.
Statement II : For some $(a, b) \in X$, the set $S=\{(x, y) \in X:(x, y) R(a, b)\}$ represents a line parallel to $y=x$.
In the light of the above statements, choose the correct answer from the options given below :

**Options:**

- **(A)** Both Statement I and Statement II are false
- **(B)** Statement I is true but Statement II is false
- **(C)** Both Statement I and Statement II are true
- **(D)** Statement I is false but Statement II is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement I is true but Statement II is false**

**Detailed Solution:**

Reflexive : $\left(a_1, b\right) R\left(a_1, b_1\right) \Rightarrow b_1=b_1 \quad$ True

$\left.\begin{array}{rl}\text { Symmetric : } & \left(a_1, b_1\right) R\left(a_2, b_2\right) \Rightarrow b_1=b_2 \\ & \left(a_2, b_2\right) R\left(a_1, b_1\right) \Rightarrow b_2=b_1\end{array}\right\}$ True

$\begin{aligned} \text { Transitive : } & \left(a_1, b_1\right) R\left(a_2, b_2\right) \Rightarrow b_1=b_2 \\ & \&\left(a_2, b_2\right) R\left(a_3, b_3\right) b_2=b_3 \\ & \Rightarrow\left(a_1, b_1\right) R\left(a_3 . b_3\right) \Rightarrow \text { True }\} b_1=b_3\end{aligned}$

Hence Relation $R$ is an equivence relation Statement-I is true.
For statement $-\mathrm{II} \Rightarrow \mathrm{y}=\mathrm{b}$ so False

</details>

---

### Q16. JEE Main 2025 (22 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Let $A=\{1,2,3\}$. The number of relations on $A$, containing $(1,2)$ and $(2,3)$, which are reflexive and transitive but not symmetric, is ______ -

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

$R$ is reflexive $\Rightarrow R$ have $(1,1),(2,2),(3,3)$
$R$ is transitive
$\begin{aligned}
& \because(1,2),(23) \in R \quad \therefore(1,3) \in R \\
& \therefore \quad R_1=\{(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)\}
\end{aligned}$

Clearly $R_1$ is reflexive and transitive but not symmetric.

Similarly,
$\begin{aligned}
& R_2=\{(1,1),(2,2),(3,3),(1,2),(2,3),(1,3),(3,2)\} \\
& R_3=\{(1,1),(2,2),(3,3),(1,2),(2,3),(1,3),(2,1)\}
\end{aligned}$

Therefore, 3 relations are possible

</details>

---

### Q17. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\{2,3,6,8,9,11\}$ and $B=\{1,4,5,10,15\}$. Let $R$ be a relation on $A \times B$ defined by $(a, b) R(c, d)$ if and only if $3 a d-7 b c$ is an even integer. Then the relation $R$ is

**Options:**

- **(A)** an equivalence relation.
- **(B)** reflexive and symmetric but not transitive.
- **(C)** transitive but not symmetric.
- **(D)** reflexive but not symmetric.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) reflexive and symmetric but not transitive.**

**Detailed Solution:**

$\begin{array}{lc}\mathrm{A}=\{2,3,6,8,9,11\} & (\mathrm{a}, \mathrm{b}) \mathrm{R}(\mathrm{c}, \mathrm{d}) \\ \mathrm{B}=\{1,4,5,10,15\} & 3 \mathrm{ad}-7 \mathrm{bc}\end{array}$
Reflexive : $(\mathrm{a}, \mathrm{b}) \mathrm{R}(\mathrm{a}, \mathrm{b})$
$\Rightarrow 3 \mathrm{ab}-7 \mathrm{ba}=-4 \mathrm{ab}$ always even so it is reflexive.
Symmetric : If $3 \mathrm{ad}-7 \mathrm{bc}=$ Even
Case-I : odd odd
Case-II : even even
(c, d) $\mathrm{R}(\mathrm{a}, \mathrm{b}) \Rightarrow 3 \mathrm{bc}-3 \mathrm{ab}$
Case-I : odd odd
Case-II : even even
so symmetric relation
Transitive :
Set $(3,4) R(6,4)$ Satisfy relation
Set $(6,4) R(3,1)$ Satisfy relation
but $(3,4) \mathrm{R}(3,1)$ does not satisfy relation so not transitive.

</details>

---

### Q18. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\{1,2,3,4,5\}$. Let $\mathrm{R}$ be a relation on $\mathrm{A}$ defined by $x \mathrm{R} y$ if and only if $4 x \leq 5 \mathrm{y}$. Let $\mathrm{m}$ be the number of elements in $\mathrm{R}$ and $\mathrm{n}$ be the minimum number of elements from $\mathrm{A} \times \mathrm{A}$ that are required to be added to $\mathrm{R}$ to make it a symmetric relation. Then $\mathrm{m}+\mathrm{n}$ is equal to :

**Options:**

- **(A)** 25
- **(B)** 24
- **(C)** 26
- **(D)** 23

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 25**

**Detailed Solution:**

Given : $4 x \leq 5 y$
then
$\begin{aligned}
\mathrm{R}=\{ & (1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4) \\
& (2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(5,4),(5,5)\}
\end{aligned}$
i.e. 16 elements.
i.e. $\mathrm{m}=16$
Now to make R a symmetric relation add
$\{(2,1)(3,2)(4,3)(3,1)(4,2)(5,3)(4,1)(5,2)(5,1)\}$
i.e. $n=9$
So $m+n=25$

</details>

---

### Q19. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the relations $R_1$ and $R_2$ on the set $X=\{1,2,3, \ldots, 20\}$ be given by $R_1=\{(x, y): 2 x-3 y=2\}$ and $R_2=\{(x, y):-5 x+4 y=0\}$. If $M$ and $N$ be the minimum number of elements required to be added in $R_1$ and $R_2$, respectively, in order to make the relations symmetric, then $M+N$ equals

**Options:**

- **(A)** 12
- **(B)** 16
- **(C)** 8
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 10**

**Detailed Solution:**

$\begin{aligned} & \mathrm{x}=\{1,2,3, \ldots \ldots . .20\} \\ & \mathrm{R}_1=\{(\mathrm{x}, \mathrm{y}): 2 \mathrm{x}-3 \mathrm{y}=2\} \\ & \mathrm{R}_2=\{(\mathrm{x}, \mathrm{y}):-5 \mathrm{x}+4 \mathrm{y}=0\}\end{aligned}$
$\begin{aligned}
& \mathrm{R}_1=\{(4,2),(7,4),(10,6),(13,8),(16,10),(19,12)\} \\
& \mathrm{R}_2=\{(4,5),(8,10),(12,15),(16,20)\}
\end{aligned}$
in $R_1 6$ element needed
in $R_2 4$ element needed
So, total $6+4=10$ element

</details>

---

### Q20. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let a relation $\mathrm{R}$ on $\mathrm{N} \times N$ be defined as: $\left(x_1, y_1\right) \mathrm{R}\left(x_2, y_2\right)$ if and only if $x_1 \leq x_2$ or $y_1 \leq y_2$. Consider the two statements:
(I) $\mathrm{R}$ is reflexive but not symmetric.
(II) $R$ is transitive Then which one of the following is true?

**Options:**

- **(A)** Both (I) and (II) are correct.
- **(B)** Only (II) is correct.
- **(C)** Neither (I) nor (II) is correct.
- **(D)** Only (I) is correct.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Only (I) is correct.**

**Detailed Solution:**

All $\left(\left(\mathrm{x}_1 \mathrm{y}_1\right),\left(\mathrm{x}_1, \mathrm{y}_1\right)\right)$ are in $\mathrm{R}$ where
$\mathrm{x}_1, \mathrm{y}_1 \in \mathrm{N} \therefore \mathrm{R}$ is reflexive
$((1,1),(2,3)) \in \mathrm{R} \text { but }((2,3),(1,1)) \notin \mathrm{R}$
$\therefore \mathrm{R}$ is not symmetric
$((2,4),(3,3)) \in \mathrm{R}$ and $((3,3),(1,3)) \in \mathrm{R}$ but $((2,4)$,
$(1,3)) \notin \mathrm{R}$
$\therefore \mathrm{R}$ is not transitive

</details>

---

### Q21. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider the relations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msub><mi>R</mi><mn>1</mn></msub><mi>b</mi><mo>⇔</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mo>∈</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><msub><mi>R</mi><mn>2</mn></msub><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>⇔</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mi>b</mi><mo>+</mo><mi>c</mi></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>∈</mo><mi>N</mi><mo>×</mo><mi>N</mi></math>. Then</p>

**Options:**

- **(A)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is an equivalence relation
- **(B)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> both are equivalence relation
- **(D)** Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Only <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msub><mi>R</mi><mn>1</mn></msub><mi>b</mi><mo>⇔</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>∈</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is not reflexive as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>∉</mo><mi>a</mi><msub><mi>R</mi><mn>1</mn></msub><mi>b</mi></math></p><p>So, it is not equivalence.</p><p>Now, solving</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><msub><mi>R</mi><mn>2</mn></msub><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>⇔</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>∈</mo><mi>N</mi></math></p><p>Reflexive: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mi>b</mi><mo>+</mo><mi>a</mi><mo>→</mo><mi>True</mi></math></p><p>Symmetric: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><msub><mi>R</mi><mn>2</mn></msub><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mi>b</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mo>+</mo><mi>a</mi><mo>=</mo><mi>c</mi><mo>+</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>+</mo><mi>b</mi><mo>=</mo><mi>d</mi><mo>+</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><msub><mi>R</mi><mn>2</mn></msub><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math></p><p>Transitive: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><msub><mi>R</mi><mn>2</mn></msub><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><msub><mi>R</mi><mn>2</mn></msub><mfenced><mrow><mi>e</mi><mo>,</mo><mi>f</mi></mrow></mfenced><mo>⇒</mo><mi>c</mi><mo>+</mo><mi>f</mi><mo>=</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, adding above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>f</mi><mo>=</mo><mi>b</mi><mo>+</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><msub><mi>R</mi><mn>2</mn></msub><mfenced><mrow><mi>e</mi><mo>,</mo><mi>f</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is reflexive, symmetric and transitive</p><p>Hence only <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is equivalence relation.</p>

</details>

---

### Q22. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mn>3</mn><mo>,</mo><mo> </mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mo>(</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>)</mo><mo>,</mo><mo> </mo><mo>(</mo><mn>2</mn><mo>,</mo><mo> </mo><mn>3</mn><mo>)</mo><mo>,</mo><mo> </mo><mo>(</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>4</mn><mo>)</mo></mrow></mfenced></math> be a relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the equivalence relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>⊂</mo><mi>S</mi></math> and the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>. Then, the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mn>3</mn><mo>,</mo><mo> </mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mo>(</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>)</mo><mo>,</mo><mo> </mo><mo>(</mo><mn>2</mn><mo>,</mo><mo> </mo><mn>3</mn><mo>)</mo><mo>,</mo><mo> </mo><mo>(</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>4</mn><mo>)</mo></mrow></mfenced></math> be a relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>.</p><p>Now, given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the equivalence relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>⊂</mo><mi>S</mi></math></p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> to be equivalence it should be Reflexive, Symmetric and Transitive on given relation,</p><p>Now, for reflexive Relation we need, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></mrow></mfenced><mo>→</mo><mn>4</mn></math> elements,</p><p>For Symmetric relation we need, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>→</mo><mn>3</mn></math> elements,</p><p>And for Transitive relation we need, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>→</mo><mn>6</mn></math> elements</p><p>So, minimum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math> elements should be added in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></p><p>Hence , <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>S</mi></mfenced><mo>=</mo><mn>16</mn></math> elements.</p>

</details>

---

### Q23. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is the smallest equivalence relation on the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>}</mo><mo>⊂</mo><mi>R</mi></math>, then the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is ______.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p>To make <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> as Reflexive, the required elements are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>To make <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> as Symmetric, the required elements are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>To make <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> as Transitive, the required elements are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> elements are required to make <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> an equivalence relation.</p><p>Hence, the total number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>.</p>

</details>

---

### Q24. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be a relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mo>×</mo><mi>Z</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mo> </mo><mi>b</mi><mo>)</mo><mi>R</mi><mo>(</mo><mi>c</mi><mo>,</mo><mo> </mo><mi>d</mi><mo>)</mo></math> if and only if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> . Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> is

**Options:**

- **(A)** Reflexive and symmetric but not transitive
- **(B)** Reflexive but neither symmetric not transitive
- **(C)** Reflexive, symmetric and transitive
- **(D)** Reflexive and transitive but not symmetric

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Reflexive and symmetric but not transitive**

**Detailed Solution:**

<p>Given relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo> </mo><mo>:</mo><mo> </mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo> </mo><mi>R</mi><mo> </mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>5</mn><mi>k</mi><mo> </mo><mfenced close="}" open="{"><mrow><mtext>where </mtext><mi>k</mi><mo>∈</mo><mi>Z</mi></mrow></mfenced></math></p><p>Now, for reflexive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo> </mo><mo>:</mo><mo> </mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo> </mo><mi>R</mi><mo> </mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mi>b</mi><mo>-</mo><mi>b</mi><mi>a</mi><mo>=</mo><mn>0</mn></math> which is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></p><p>So, the relation is reflexive,</p><p>Now, for symmetric <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo> </mo><mo>:</mo><mo> </mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo> </mo><mi>R</mi><mo> </mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mi>d</mi><mo>=</mo><mo>-</mo><mn>5</mn><mi>k</mi><mo> </mo></math> which is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></p><p>So, the relation is symmetric,</p><p>Now for transitive relation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo> </mo><mo>:</mo><mo> </mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo> </mo><mi>R</mi><mo> </mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo> </mo><mi>R</mi><mo> </mo><mfenced><mrow><mi>e</mi><mo>,</mo><mi>f</mi></mrow></mfenced><mo> </mo></math></p><p>Taking example <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mn>10</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>e</mi><mo>,</mo><mi>f</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>10</mn><mo>-</mo><mn>20</mn><mo>=</mo><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mi>f</mi><mo>-</mo><mi>e</mi><mi>d</mi><mo>=</mo><mn>40</mn><mo>-</mo><mn>40</mn><mo>=</mo><mn>0</mn></math></p><p>But <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>f</mi><mo>-</mo><mi>b</mi><mi>e</mi><mo>=</mo><mn>8</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>4</mn></math> which is not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>,</p><p>Hence, the relation is reflexive, symmetric but not transitive.</p>

</details>

---

### Q25. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>…</mo><mo>,</mo><mn>10</mn><mo>}</mo></math>. Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is the set of all the subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>, then the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mo>(</mo><mi>A</mi><mo>,</mo><mi>B</mi><mo>)</mo><mo>:</mo><mi>A</mi><mo>∩</mo><mi>B</mi><mo>≠</mo><mi>ϕ</mi><mo>;</mo><mi>A</mi><mo>,</mo><mi>B</mi><mo>∈</mo><mi>M</mi><mo>}</mo></math> is :

**Options:**

- **(A)** symmetric and reflexive only
- **(B)** reflexive only
- **(C)** symmetric and transitive only
- **(D)** symmetric only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) symmetric only**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>…</mo><mo>,</mo><mn>10</mn><mo>}</mo></math> and  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mo>(</mo><mi>A</mi><mo>,</mo><mi>B</mi><mo>)</mo><mo>:</mo><mi>A</mi><mo>∩</mo><mi>B</mi><mo>≠</mo><mi>ϕ</mi><mo>;</mo><mi>A</mi><mo>,</mo><mi>B</mi><mo>∈</mo><mi>M</mi><mo>}</mo></math></p><p>For Reflexive, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is subset of '<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>'</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>ϕ</mi><mo>∈</mo><mi mathvariant="normal">M</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ϕ</mi><mo>∩</mo><mi>ϕ</mi><mo>=</mo><mi>ϕ</mi></math></p><p>But it is given that relation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>∩</mo><mi mathvariant="normal">B</mi><mo>≠</mo><mi>ϕ</mi></math>.</p><p>So, it is not reflexive.</p><p>For symmetric,</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>R</mi><mi>B</mi><none></none><mprescripts></mprescripts><mi>A</mi><none></none></mmultiscripts><mo>⇒</mo><mi mathvariant="normal">A</mi><mo>∩</mo><mi mathvariant="normal">B</mi><mo>≠</mo><mi>ϕ</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>R</mi><mi>A</mi><none></none><mprescripts></mprescripts><mi>B</mi><none></none></mmultiscripts><mo>⇒</mo><mi mathvariant="normal">B</mi><mo>∩</mo><mi mathvariant="normal">A</mi><mo>≠</mo><mi mathvariant="normal">ϕ</mi></math>,</p><p>So, it is symmetric.</p><p>For transitive,</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>}</mo></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mo>{</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>}</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mo>{</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>)</mo><mo>}</mo></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mmultiscripts><mi>R</mi><mi>B</mi><none></none><mprescripts></mprescripts><mi>A</mi><none></none></mmultiscripts><mo>,</mo><mo> </mo><mmultiscripts><mi>R</mi><mi>C</mi><none></none><mprescripts></mprescripts><mi>B</mi><none></none></mmultiscripts></math> is applicable but <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>R</mi><mi>C</mi><none></none><mprescripts></mprescripts><mi>A</mi><none></none></mmultiscripts></math> is not followed.</p><p>So, it not transitive</p><p>Hence, the given relation is symmetric only.</p>

</details>

---

### Q26. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>&#8712;</mo><mi>A</mi><mo>&#215;</mo><mi>A</mi></math> : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mo>|</mo><mi>a</mi><mo>|</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open=""><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> be a relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. Then the minimum number of elements, that must be added to the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> so that it becomes reflexive and symmetric, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>&#8712;</mo><mi>A</mi><mo>&#215;</mo><mi>A</mi></math> : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mo>|</mo><mi>a</mi><mo>|</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open=""><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> be a relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>,</p><p>So, the relation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mo>(</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mo>-</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>}</mo></math></p><p>Now, relation to be reflexive <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mi>a</mi><mo>)</mo><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>a</mi><mo>&#8712;</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo></math> also should be added in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>.</p><p>Now relation to be symmetric if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>&#8712;</mo><mi>R</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>b</mi><mo>,</mo><mi>a</mi><mo>)</mo><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>4</mn><mo>,</mo><mo>-</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> also should be added in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></p><p>Hence, minimum number of elements to be added to
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>7</mn></math></p></blockquote>

</details>

---

### Q27. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of relations, on the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math> containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math> which are reflexive and transitive but not symmetric, is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Given,</p><p>Set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Now Cartesian product <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></math></p><p>Now, given the relation is reflexive,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo><mo>&#8712;</mo><mo>&#160;</mo><mi>R</mi></math></p><p>Also given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>&#8712;</mo><mo>&#160;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math> must <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8712;</mo><mo>&#160;</mo><mi>R</mi></math></p><p>Now finding, <strong>Possible cases</strong> :</p><p><strong>Case-1</strong>: All of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>&#8713;</mo><mi>R</mi><mo>&#8594;</mo><mn>1</mn></math> relation.</p><p><strong>Case-2: </strong>Only one of<strong> </strong><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#8594;</mo><mn>3</mn></math> relations.</p><p>For example if relation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math> then it is reflexive as well as transitive as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mtext>is&#160;present&#160;in&#160;relation</mtext></math></p><p>Note that exactly two of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math> is not possible because if two of these <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8712;</mo><mi>R</mi></math>, third must <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8712;</mo><mi>R</mi></math>  to make relation transitive.</p><p>Total number of relations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q28. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>}</mo></math>. Then the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi>A</mi><mo>&#215;</mo><mi>A</mi><mo>:</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>7</mn><mo>}</mo></math> is

**Options:**

- **(A)** an equivalence relation
- **(B)** symmetric but neither reflexive nor transitive
- **(C)** transitive but neither symmetric nor reflexive
- **(D)** reflexive but neither symmetric nor transitive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) symmetric but neither reflexive nor transitive**

**Detailed Solution:**

<blockquote><p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p><strong>Reflexive</strong>: A relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> on a set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is said to be reflexive if every element of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is related to itself.</p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>reflexive</mi><mo>&#8660;</mo><mo>(</mo><mi>a</mi><mo>,</mo><mi>a</mi><mo>)</mo><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mi>for</mi><mo>&#160;</mo><mi>all</mi><mo>&#160;</mo><mi>a</mi><mo>&#8712;</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>7</mn><mo>,</mo><mn>7</mn><mo>)</mo></math> does not satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>7</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is not reflexive.</p><p><strong>Symmetric</strong>: A relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> is symmetric on a set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> iff</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>&#8712;</mo><mi>R</mi><mo>&#8658;</mo><mo>(</mo><mi>b</mi><mo>,</mo><mi>a</mi><mo>)</mo><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mi>for</mi><mo>&#160;</mo><mi>all</mi><mo>&#160;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>7</mn></math></p><p>Now on interchanging <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mi>x</mi><mo>=</mo><mn>7</mn></math> which is always true for given set,</p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is symmetric.</p><p><strong>Transitive</strong>: A relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is said to be transitive relation iff </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="italic">a</mi><mo mathvariant="italic">,</mo><mi mathvariant="italic">b</mi></mrow></mfenced><mo mathvariant="italic">&#8712;</mo><mi>R</mi><mo mathvariant="italic">&#160;</mo><mi>and</mi><mo mathvariant="italic">&#160;</mo><mo mathvariant="italic">(</mo><mi>b</mi><mo mathvariant="italic">,</mo><mi>c</mi><mo mathvariant="italic">)</mo><mo mathvariant="italic">&#8712;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mi>for</mi><mo>&#160;</mo><mi>all</mi><mo>&#160;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><mi>A</mi></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> so  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> does not satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>7</mn></math>,</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is not transitive and not equivalence.</p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is only Symmetric.</p></blockquote>

</details>

---

### Q29. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be the relation defined on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>A</mi><mo>&#215;</mo><mi>A</mi><mo>:</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>&#160;</mo><mtext>is&#160;odd&#160;positive&#160;integer</mtext><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>2</mn></mrow></mfenced></math>. The minimum number of elements that must be added to the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>,</mo></math> so that it is a symmetric relation, is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>10</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Now relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mtext>&#160;is&#160;odd&#160;or</mtext><mo>&#160;</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>2</mn></math> can be given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>R</mi><mo>=</mo><mrow><mo>(</mo><mn>10</mn><mo>,</mo><mn>9</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>10</mn><mo>,</mo><mn>8</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>10</mn><mo>,</mo><mn>7</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>10</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>9</mn><mo>,</mo><mn>8</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>9</mn><mo>,</mo><mn>7</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>9</mn><mo>,</mo><mn>6</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>9</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>9</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>8</mn><mo>,</mo><mn>7</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>8</mn><mo>,</mo><mn>6</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>8</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>7</mn><mo>,</mo><mn>6</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>7</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>7</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>6</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>6</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>0</mn><mo>)</mo></mrow></mrow></mfenced></math></p><p>So, total there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math> elements and all the elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo></math> are of type <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>&#62;</mo><mo>&#160;</mo><mi>b</mi></math>.</p><p>Hence, we need to add total of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math> more elements to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> to make in symmetric</p></blockquote>

</details>

---

### Q30. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi mathvariant="normal">S</mi></mfenced></math> denote the power set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn></mrow></mfenced></math>. Define the relations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>S</mi></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msub><mi>R</mi><mn>1</mn></msub><mi>B</mi></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><mi>B</mi><mo>&#8745;</mo><msup><mi>A</mi><mi>c</mi></msup></mrow></mfenced><mo>=</mo><mi>&#981;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msub><mi>R</mi><mn>2</mn></msub><mo>&#160;</mo><mi>B</mi></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8746;</mo><msup><mi>B</mi><mi>c</mi></msup><mo>=</mo><mi>B</mi><mo>&#8746;</mo><msup><mi>A</mi><mi>c</mi></msup><mo>,</mo><mo>&#8704;</mo><mi>A</mi><mo>,</mo><mi>B</mi><mo>&#8712;</mo><mi>P</mi><mfenced><mi>S</mi></mfenced></math> . Then :

**Options:**

- **(A)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are equivalence relations
- **(B)** only <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is an equivalence relation
- **(C)** only <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation
- **(D)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are not equivalence relations

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are equivalence relations**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>S</mi></mfenced><mo>=</mo></math> power set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msub><mi>R</mi><mn>1</mn></msub><mi>B</mi><mo>&#8658;</mo><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><msup><mi>A</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>&#981;</mi></math></p><p>Now for reflexive property, replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>A</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><msup><mi>A</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>A</mi></mrow></mfenced></math> which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi></math> always,</p><p>Now checking symmetric we will interchange <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>B</mi></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>B</mi><mo>&#8745;</mo><msup><mi>A</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><msup><mi>B</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>A</mi></mrow></mfenced></math> which is same as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><msup><mi>A</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math>, hence the relation is symmetric,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is reflexive, symmetric</p><p>Now checking for transitive
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><msup><mi>A</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>&#981;</mi><mo>;</mo></math></p><p>Now from diagram the elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mi>c</mi></msup></mrow></mfenced><mo>&#8746;</mo><mfenced><mrow><msup><mi>A</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mi>a</mi></mfenced><mo>&#8746;</mo><mfenced open="{" close="}"><mi>b</mi></mfenced></math> which is given as empty set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi></math></p><p>Hence, we can say that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mi>a</mi></mfenced><mo>=</mo><mi>&#981;</mi><mo>=</mo><mfenced close="}" open="{"><mi>b</mi></mfenced><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mi>B</mi></math></p><p>Now taking, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>B</mi><mo>&#8745;</mo><msup><mi>C</mi><mi>c</mi></msup><mo>)</mo><mo>&#8746;</mo><mo>(</mo><msup><mi>B</mi><mi>c</mi></msup><mo>&#8745;</mo><mi>C</mi><mo>)</mo><mo>=</mo><mi>&#981;</mi><mo>&#8756;</mo><mi>B</mi><mo>=</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mi>C</mi></math> equivalence.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7dda9698-159e-473c-a185-7b6eb321b64c-9896795.png" style="width: 250px; height: 219px;" /></p><p> </p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8801;</mo><mi>A</mi><mo>&#8746;</mo><msup><mi>B</mi><mi>c</mi></msup><mo>=</mo><msup><mi>A</mi><mi>c</mi></msup><mo>&#8746;</mo><mi>B</mi></math></p><p>Now for reflexive replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8594;</mo><mi>A</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8746;</mo><msup><mi>A</mi><mi>c</mi></msup><mo>=</mo><msup><mi>A</mi><mi>c</mi></msup><mo>&#8746;</mo><mi>A</mi></math> which is true,</p><p>And for symmetric interchanging <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8660;</mo><mi>B</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8746;</mo><msup><mi>A</mi><mi>c</mi></msup><mo>=</mo><msup><mi>B</mi><mi>c</mi></msup><mo>&#8746;</mo><mi>A</mi></math> which is again true,</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo></math> Reflexive, symmetric</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f85793dd-c45c-48ad-94cd-a80954a303c0-9896795_2.png" style="width: 250px; height: 219px;" /></p><p>Now for transitive,</p><p>From diagram the elements in<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8746;</mo><msup><mi>B</mi><mi>c</mi></msup><mo>=</mo><msup><mi>A</mi><mi>c</mi></msup><mo>&#8746;</mo><mi>B</mi><mo>&#8658;</mo><mfenced close="}" open="{"><mrow><mi>a</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>=</mo><mfenced close="}" open="{"><mrow><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced></math></p><p>On comparing both side, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mi>a</mi></mfenced><mo>=</mo><mfenced close="}" open="{"><mi>b</mi></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mi>B</mi></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8746;</mo><msup><mi>C</mi><mi>c</mi></msup><mo>=</mo><msup><mi>B</mi><mi>c</mi></msup><mo>&#8746;</mo><mi>C</mi><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mi>C</mi><mo>&#160;&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>A</mi><mo>&#8746;</mo><msup><mi>C</mi><mi>c</mi></msup><mo>=</mo><msup><mi>A</mi><mi>c</mi></msup><mo>&#8746;</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo></math> Equivalence</p><p>Hence, both given relation are equivalence.</p>

</details>

---

### Q31. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be a relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi></math>, given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi><mo>+</mo><msqrt><mn>7</mn></msqrt></math> is an irrational number <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>}</mo></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is

**Options:**

- **(A)** Reflexive but neither symmetric nor transitive
- **(B)** Reflexive and transitive but not symmetric
- **(C)** Reflexive and symmetric but not transitive
- **(D)** An equivalence relation

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Reflexive but neither symmetric nor transitive**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi><mo>+</mo><msqrt><mn>7</mn></msqrt><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>irrational</mi></mrow></mfenced></math></p><p><strong>Reflexive:</strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>a</mi><mo>-</mo><mn>3</mn><mi>a</mi><mo>+</mo><msqrt><mn>7</mn></msqrt><mo>=</mo><msqrt><mn>7</mn></msqrt></math> is irrational.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math>, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is reflexive.</p><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mn>3</mn><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi><mo>+</mo><msqrt><mn>7</mn></msqrt><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>irrational</mi></mrow></mfenced></math></p><p><strong>Symmetric:</strong></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi><mo>+</mo><msqrt><mn>7</mn></msqrt></math> is irrational.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>b</mi><mo>-</mo><mn>3</mn><mi>a</mi><mo>+</mo><msqrt><mn>7</mn></msqrt></math> is not necessarily irrational, since if <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>a</mi><mo>=</mo><msqrt><mn>7</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>b</mi><mo>&#8712;</mo><mi>Z</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi><mo>+</mo><msqrt><mn>7</mn></msqrt></math> is irrational., but <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>b</mi><mo>-</mo><mn>3</mn><mi>a</mi><mo>+</mo><msqrt><mn>7</mn></msqrt></math> is not irrational.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi><menclose notation="updiagonalstrike"><mo>&#8658;</mo></menclose><mfenced><mrow><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math>, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is not symmetric</p><p><strong>Transitive:</strong></p><p>Take <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><msqrt><mn>7</mn></msqrt><mn>3</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mn>2</mn><msqrt><mn>7</mn></msqrt></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#8713;</mo><mi>R</mi></math> which means relation is not transitive.</p>

</details>

---

### Q32. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Among the relations
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced><mo>,</mo><mn>2</mn><mo>+</mo><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>&#8712;</mo><mi>Z</mi></mrow></mfenced></math>,

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is transitive but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is not
- **(B)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> are symmetric
- **(C)** neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> not <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is transitive
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is symmetric but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is not

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is symmetric but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is not**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#160;</mo><mo>&#8712;</mo><mo>&#160;</mo><mi>I</mi></math> and relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>&#8712;</mo><mi>I</mi></math></p><p>Now if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>&#8712;</mo><mi>I</mi></math> so <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup></math> will also be integer, for example if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mn>2</mn></msup><mo>-</mo><msup><mn>4</mn><mn>2</mn></msup><mo>=</mo><mn>9</mn></math> is integer then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>9</mn></math> is also a integer,</p><p>Now checking transitive,</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mn>2</mn></msup><mo>-</mo><msup><mn>3</mn><mn>2</mn></msup><mo>=</mo><mn>7</mn></math> is an integer, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>2</mn></msup><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><mn>5</mn></math> is an integer then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mn>2</mn></msup><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><mn>12</mn></math> is also an integer, hence we can say that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is symmetric and transitive,</p><p> Now checking relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> which is defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>&#62;</mo><mn>0</mn></math>,</p><p>So, if we replace <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>b</mi></mfrac></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>9</mn></mfrac></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>&#62;</mo><mn>0</mn></math> is true but we take <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>=</mo><mo>-</mo><mn>9</mn></math> for symmetric we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>=</mo><mn>2</mn><mo>-</mo><mn>9</mn><mo>=</mo><mo>-</mo><mn>7</mn><mo>&#8815;</mo><mn>0</mn></math> hence, the relation is not symmetric, </p><p>Now checking transitive, now if <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>&#62;</mo><mn>0</mn><mo>&#8658;</mo><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>&#62;</mo><mo>-</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>b</mi><mi>c</mi></mfrac><mo>&#62;</mo><mo>-</mo><mn>2</mn></math> then we cannot say that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>c</mi></mfrac><mo>&#62;</mo><mo>-</mo><mn>2</mn></math>,</p><p>For example if we take <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>1</mn></mfrac><mo>&#62;</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#62;</mo><mo>-</mo><mn>2</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#8815;</mo><mo>-</mo><mn>2</mn></math>, hence it is not transitive,</p><p>Hence, we can say that  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is symmetric and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is not.</p>

</details>

---

### Q33. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be a relation on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>&#215;</mo><mi>N</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mi>R</mi><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced></math>  if and only if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mfenced><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mi>b</mi><mi>c</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>d</mi></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is

**Options:**

- **(A)** symmetric but neither reflexive nor transitive
- **(B)** transitive but neither reflexive nor symmetric
- **(C)** reflexive and symmetric but not transitive
- **(D)** symmetric and transitive but not reflexive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) symmetric but neither reflexive nor transitive**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mi>R</mi><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mfenced><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mi>b</mi><mi>c</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mi>R</mi><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8660;</mo><mfrac><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow><mrow><mi>b</mi><mi>c</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>a</mi><mo>-</mo><mi>d</mi></mrow><mrow><mi>a</mi><mi>d</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>c</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>c</mi></mfrac></math></p><p><strong>Reflexive:</strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mi>R</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8658;</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>a</mi></mfrac></math></p><p>It is false. So, given relation is not reflexive.</p><p><strong>Symmetric:</strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mi>R</mi><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8658;</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>c</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>c</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mi>R</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math></p><p>It is symmetric.</p><p>Transitive:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mi>R</mi><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8658;</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>c</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mi>R</mi><mfenced><mrow><mi>e</mi><mo>,</mo><mi>f</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>c</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>f</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>b</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>f</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><menclose notation="updiagonalstrike"><mi>R</mi></menclose><mfenced><mrow><mi>e</mi><mo>,</mo><mi>f</mi></mrow></mfenced></math></p><p>So, not transitive.</p>

</details>

---

### Q34. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The minimum number of elements that must be added to the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>(</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>)</mo><mo>,</mo><mo>(</mo><mi>b</mi><mo>,</mo><mi mathvariant="normal">c</mi><mo>)</mo></math> on the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi mathvariant="normal">a</mi><mo>,</mo><mi mathvariant="normal">b</mi><mo>,</mo><mi mathvariant="normal">c</mi><mo>}</mo></math> so that it becomes symmetric and transitive is:</p><p> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></mrow></mfenced></math></p><p>For symmetric relation, we must add <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>b</mi></mrow></mfenced></mrow></mfenced></math>.</p><p>For transitive relation, we must add</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math></p><p>Hence, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></mrow></mfenced></math></p><p>So, number of new elements added<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q35. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be a relation defined on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8469;</mi></math> as a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> b is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math> is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is

**Options:**

- **(A)** not reflexive
- **(B)** transitive but not symmetric
- **(C)** symmetric but not transitive
- **(D)** an equivalence relation

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) an equivalence relation**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>divisible</mi><mo>&#160;</mo><mi>by</mi><mo>&#160;</mo><mn>5</mn><mo>&#160;</mo><mi>for</mi><mo>&#160;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced></math></p><p><strong>Reflexive:</strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>a</mi><mo>=</mo><mn>5</mn><mi>a</mi></math> is always divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math></p><p><strong>Symmetric:</strong></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math> i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>5</mn><mi>&#955;</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><msup><mi>Z</mi><mo>+</mo></msup></math>.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>a</mi><mo>+</mo><mn>5</mn><mi>b</mi><mo>=</mo><mi>multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mi>b</mi><mo>+</mo><mn>3</mn><mi>a</mi></mrow></mfenced><mo>=</mo><mi>multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>&#955;</mi><mo>+</mo><mfenced><mrow><mn>2</mn><mi>b</mi><mo>+</mo><mn>3</mn><mi>a</mi></mrow></mfenced><mo>=</mo><mi>multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>b</mi><mo>+</mo><mn>3</mn><mi>a</mi><mo>=</mo><mi>multiple</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mn>5</mn><mo>-</mo><mn>5</mn><mi>&#955;</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><mo>+</mo><mn>3</mn><mi>a</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></p><p><strong>Transitive:</strong></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>5</mn><msub><mi>&#955;</mi><mn>1</mn></msub><mo>;</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>1</mn></msub><mo>&#8712;</mo><msup><mi>Z</mi><mo>+</mo></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><mo>+</mo><mn>3</mn><mi>c</mi><mo>=</mo><mn>5</mn><msub><mi>&#955;</mi><mn>2</mn></msub><mo>;</mo><mo>&#160;</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>&#8712;</mo><msup><mi>Z</mi><mo>+</mo></msup></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>5</mn><mi>b</mi><mo>+</mo><mn>3</mn><mi>c</mi><mo>=</mo><mn>5</mn><mfenced><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#955;</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>c</mi><mo>=</mo><mn>5</mn><mfenced><mrow><msub><mi>&#955;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#955;</mi><mn>2</mn></msub><mo>-</mo><mi>b</mi></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>c</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#8712;</mo><mi>R</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is an equivalence relation.</p>

</details>

---

### Q36. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>The minimum number of elements that must be added to relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>d</mi></mrow></mfenced></mrow></mfenced></math> on the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced></math>, so that it is an equivalence relation is</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>{</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>}</mo><mo>,</mo><mo>&#160;</mo><mi>R</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>A</mi><mo>&#8594;</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>d</mi></mrow></mfenced></mrow></mfenced></math></p><p><strong>Reflexive:</strong></p><p>For reflexivity, we must add <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>d</mi><mo>,</mo><mi>d</mi></mrow></mfenced></math></p><p><strong>Symmetric and Transitive:</strong></p><p>For symmetric and transitivity, we must add</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>d</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>d</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>d</mi><mo>,</mo><mi>a</mi></mrow></mfenced></math></p><p>So, we can say that minimum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math> elements are required to make an equivalence relation.</p>

</details>

---

### Q37. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>g</mi><mi>c</mi><mi>d</mi><mfenced><mrow><mi mathvariant="italic">a</mi><mo mathvariant="italic">,</mo><mi mathvariant="italic">b</mi></mrow></mfenced><mo mathvariant="italic">=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>a</mi><mo>&#8800;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** transitive but not reflexive
- **(B)** symmetric but not transitive
- **(C)** reflexive but not symmetric
- **(D)** neither symmetric nor transitive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) neither symmetric nor transitive**

**Detailed Solution:**

<p>Given relation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><mi>g</mi><mi>c</mi><mi>d</mi><mfenced><mrow><mi>a</mi><mo mathvariant="italic">,</mo><mi>b</mi></mrow></mfenced><mo mathvariant="italic">=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>a</mi><mo>&#8800;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi></mrow></mfenced></math></p><p>Now,</p><p><strong>Reflexive: </strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>gcd</mi><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>&#8800;</mo><mn>1</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>a</mi><mo>&#8712;</mo><mi>Z</mi></math>, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is not reflexive.</p><p><strong>Symmetric:</strong></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>gcd</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>=</mo><mn>4</mn><mo>&#8800;</mo><mi>b</mi></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>g</mi><mi>c</mi><mi>d</mi><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p>But, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>=</mo><mn>2</mn><mo>=</mo><mi>b</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>R</mi></math> is not Symmetric</p><p><strong>Transitive:</strong></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>14</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>19</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>c</mi><mi>d</mi><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>c</mi><mi>d</mi><mo>(</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>c</mi><mi>d</mi><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>)</mo><mo>=</mo><mn>7</mn></math></p><p>Hence, not transitive</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is neither symmetric nor transitive.</p>

</details>

---

### Q38. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi>N</mi></math>, consider a relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi>y</mi></math> is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>}. The relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is an equivalence relation if and only if

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>14</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>is the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> is the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> is the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<blockquote><p>Given, a relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi>y</mi></math> is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>},</p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> to be reflexive <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>R</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi>x</mi><mo>=</mo><mn>7</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mi>x</mi><mo>=</mo><mn>7</mn><mi>K</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>+</mo><mi>&#945;</mi><mo>=</mo><mn>7</mn><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>7</mn><mi>&#955;</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>7</mn><mo>&#160;</mo><mi>N</mi><mo>+</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>where&#160;</mtext><mi>K</mi><mo>,</mo><mi>&#955;</mi><mo>,</mo><mi>N</mi><mo>&#8712;</mo><mi>I</mi></mrow></mfenced></math></p><p>So, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>, remainder is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>.</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> to be symmetric <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>R</mi><mi>y</mi><mo>&#8658;</mo><mi>y</mi><mi>R</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi>y</mi><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>1</mn></msub><mo>,</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>x</mi><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>7</mn><mfenced><mrow><msub><mi>N</mi><mn>1</mn></msub><mo>+</mo><msub><mi>N</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>3</mn></msub></math></p><p>Which holds when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mi>&#945;</mi></math> is multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>7</mn><mi>N</mi><mo>+</mo><mn>4</mn></math> (as did earlier)</p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> to be transitive</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>R</mi><mi>y</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mi>R</mi><mi>z</mi><mo>&#8658;</mo><mi>x</mi><mi>R</mi><mi>z</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi>y</mi><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>1</mn></msub><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>2</mn></msub><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>And  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>&#945;</mi><mi>z</mi><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>3</mn></msub><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced><mo>-</mo><mfenced><mn>2</mn></mfenced></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>7</mn><msub><mi>N</mi><mn>2</mn></msub><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>3</mn></msub></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi></math> from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msub><mi>N</mi><mn>1</mn></msub><mo>-</mo><mi>&#945;</mi><mi>y</mi><mo>+</mo><mn>7</mn><msub><mi>N</mi><mn>2</mn></msub><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mfenced><mrow><msub><mi>N</mi><mn>1</mn></msub><mo>+</mo><msub><mi>N</mi><mn>2</mn></msub></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mn>7</mn><msub><mi>N</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mn>7</mn><mi>N</mi></math></p><p>Which is true again when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mi>&#945;</mi></math> divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>, i.e. when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>, remainder is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> .</p></blockquote>

</details>

---

### Q39. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> be two relations defined on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8477;</mi></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msub><mi mathvariant="normal">R</mi><mn>1</mn></msub><mi>b</mi><mo>&#8660;</mo><mi>a</mi><mi>b</mi><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><msub><mi>R</mi><mn>2</mn></msub><mi>b</mi><mo>&#8660;</mo><mi>a</mi><mo>&#8805;</mo><mi>b</mi></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is an equivalence relation but not <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation but not <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math>
- **(C)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are equivalence relations
- **(D)** neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mi>a</mi><mi>b</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math></p><p>For reflexive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#215;</mo><mi>a</mi><mo>&#8805;</mo><mn>0</mn></math> which is true,</p><p>For symmetric</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>&#8805;</mo><mn>0</mn><mo>&#8658;</mo><mi>b</mi><mi>a</mi><mo>&#8805;</mo><mn>0</mn></math> which is true,</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>b</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#183;</mo><mi>b</mi><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#183;</mo><mi>c</mi><mo>&#8805;</mo><mn>0</mn></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#183;</mo><mi>c</mi><mo>&#8805;</mo><mn>0</mn></math> is not true</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> not transitive relation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>R</mi><mn>1</mn></msub></math> is not equivalence</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8805;</mo><mi>b</mi></math> it does not implies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#8805;</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>R</mi><mn>2</mn></msub></math> is not equivalence relation</p><p>So, neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation</p></blockquote>

</details>

---

### Q40. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msub><mi>A</mi><mn>1</mn></msub><mo>&#8746;</mo><msub><mi>A</mi><mn>2</mn></msub><mo>&#8746;</mo><mo>&#8230;</mo><mo>&#8746;</mo><msub><mi>A</mi><mi>k</mi></msub></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>i</mi></msub><mo>&#8745;</mo><msub><mi>A</mi><mi>j</mi></msub><mo>=</mo><mi>&#981;</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>&#8800;</mo><mi>j</mi><mo>;</mo><mo>&#160;</mo><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>&#8804;</mo><mi>k</mi><mo>.</mo></math> Define the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mi>y</mi><mo>&#8712;</mo><msub><mi>A</mi><mi>i</mi></msub></math> if and only if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><msub><mi>A</mi><mi>i</mi></msub><mo>,</mo><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>&#8804;</mo><mi>k</mi></math>}. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is:

**Options:**

- **(A)** reflexive, symmetric but not transitive
- **(B)** reflexive, transitive but not symmetric
- **(C)** reflexive but not symmetric and transitive
- **(D)** an equivalence relation

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) an equivalence relation**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></math></p><p>which is an equivalence relation.</p>

</details>

---

### Q41. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>N</mi><mo>&#215;</mo><mi>N</mi><mo>:</mo><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>&#8804;</mo><mn>13</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><mi>N</mi><mo>&#215;</mo><mi>N</mi><mo>:</mo><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>&#8800;</mo><mn>13</mn></mrow></mfenced></math> Then on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>:

**Options:**

- **(A)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are equivalence relations
- **(B)** Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is an equivalence relation but <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is not
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation but <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is not

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation**

**Detailed Solution:**

<p>To check if <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is transitive -</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>16</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>16</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#8804;</mo><mn>13</mn></math> holds true</p><p>now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>4</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>13</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mn>3</mn></mfenced><mo>&#10877;</mo><mn>13</mn></math>   also holds true</p><p>but <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>16</mn><mo>&#8722;</mo><mn>1</mn></mrow></mfenced><mo>&#8816;</mo><mn>13</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is not transitive</p><p>Similarly, to check transitivity of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>16</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>3</mn></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>16</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>&#8800;</mo><mn>13</mn><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mi>b</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>4</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>&#8800;</mo><mn>13</mn></math></p><p>but <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>16</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>13</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is also not transitive.</p><p>Hence neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is an equivalence relation</p>

</details>

---

### Q42. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following is not correct for relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> on the set of real numbers?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#8660;</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>-</mo><mo>|</mo><mi>y</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></math> is reflexive but not symmetric.
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#8660;</mo><mo>|</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></math> is reflexive and symmetric.
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#8660;</mo><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></math> is symmetric and transitive.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#8660;</mo><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>-</mo><mo>|</mo><mi>y</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></math> is not transitive but symmetric.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#8660;</mo><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>x</mi><mo>|</mo><mo>-</mo><mo>|</mo><mi>y</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></math> is not transitive but symmetric.**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">y</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#160;</mo><mo>&#8658;</mo></math>symmetric</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">y</mi><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mi>z</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi><mo>&#8658;</mo></math>transitive
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open=""><mtable columnalign="left"><mtr><mtd><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>y</mi><mo>-</mo><mi>x</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math>is symmetric</p><p>let </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></math>                                         .......(1)
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math> satisfy the equation (1)
but <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>&#8713;</mo><mi>R</mi></math> not satisfied
Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mo>|</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>|</mo><mo>&#8804;</mo><mn>1</mn></math> is symmetric but not transitive relation</p>

</details>

---

### Q43. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> be the set of natural numbers and a relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> be defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>N</mi><mo>&#215;</mo><mi>N</mi><mo>:</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>-</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>y</mi><mn>3</mn></msup><mo>=</mo><mn>0</mn></mrow></mfenced></math>. Then the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is

**Options:**

- **(A)** symmetric but neither reflexive nor transitive
- **(B)** reflexive but neither symmetric nor transitive
- **(C)** reflexive and symmetric, but not transitive
- **(D)** an equivalence relation

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) reflexive but neither symmetric nor transitive**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>-</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>y</mi><mn>3</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>3</mn><mi>y</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi><mo>&#160;</mo><mo>&#8704;</mo><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>N</mi><mo>&#215;</mo><mi>N</mi></math> so its a reflexive relation.
But not symmetric &amp; transitive</p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> satisfies but <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> does not.</p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#38;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> satisfies but <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> does not.</p>

</details>

---

### Q44. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Define a relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> over a class of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#215;</mo><mi>n</mi></math> real matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> as &quot;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>R</mi><mi>B</mi></math> iff there exists a non-singular matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>A</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>B</mi></math>&quot;. Then which of the following is true ?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is symmetric, transitive but not reflexive
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is reflexive, symmetric but not transitive
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is an equivalence relation
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is reflexive, transitive but not symmetric

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is an equivalence relation**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are matrices of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#215;</mo><mi>n</mi></math> order and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>R</mi><mi>B</mi></math> iff there exists a non-singular matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#160;</mo><mfenced><mrow><mo>det</mo><mfenced><mi>P</mi></mfenced><mo>&#8800;</mo><mn>0</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>A</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>B</mi></math>.</p><p>Reflexivity Check :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>R</mi><mi>A</mi><mo>&#8658;</mo><mi>P</mi><mi>A</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>A</mi></math> which is true for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>I</mi></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is reflexive relation.</p><p>Symmetric Check :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>R</mi><mi>B</mi><mo>&#8658;</mo><mi>P</mi><mi>A</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>B</mi><mo>&#8658;</mo><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>P</mi><mi>A</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>P</mi><mo>=</mo><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>B</mi><mi>P</mi><mo>&#8658;</mo><mi>I</mi><mi>A</mi><mi>I</mi><mo>=</mo><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>B</mi><mi>P</mi><mo>&#8658;</mo><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>B</mi><mi>P</mi><mo>=</mo><mi>A</mi><mo>&#8658;</mo><mi>B</mi><mi>R</mi><mi>A</mi></math> for matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is symmetric relation.</p><p>Transitivity Check :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>R</mi><mi>B</mi><mo>&#8658;</mo><mi>P</mi><mi>A</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>R</mi><mi>C</mi><mo>&#8658;</mo><mi>P</mi><mi>B</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>C</mi></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>P</mi><mi>A</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>C</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>2</mn></msup><mi>A</mi><msup><mfenced><msup><mi>P</mi><mn>2</mn></msup></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>C</mi><mo>&#8658;</mo><mi>A</mi><mi>R</mi><mi>C</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is a transitive relation.</p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is reflexive, symmetric and transitive all.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is an equivalence relation.</p>

</details>

---

### Q45. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mo>{</mo><mfenced><mrow><mi>P</mi><mo>,</mo><mi>Q</mi></mrow></mfenced><mo>|</mo><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> are at the same distance from the origin<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>}</mo></math> be a relation, then the equivalence class of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> is the set<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>|</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>|</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>|</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>|</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>|</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

Equivalence class of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> is a circle with centre at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>2</mn></msqrt></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>|</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q46. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> be two relations defined as follows :<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>:</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>&#8712;</mo><mi>Q</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>&#8712;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>:</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>&#8713;</mo><mi>Q</mi></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is the set of all rational numbers, then</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is transitive but <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is not transitive.
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math>  is transitive but <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is not transitive.
- **(C)** Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is transitive.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are both transitive.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is transitive.**

**Detailed Solution:**

For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><msup><mn>8</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msub><mi>R</mi><mn>1</mn></msub><mi>b</mi><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>6</mn><mo>&#8712;</mo><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><msub><mi>R</mi><mn>1</mn></msub><mi>c</mi><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><msup><mn>8</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mfenced><mn>2</mn></msup><mo>=</mo><mn>3</mn><mo>&#8712;</mo><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msub><mi>R</mi><mn>1</mn></msub><mi>c</mi><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><msup><mn>8</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mfenced><mn>2</mn></msup><mo>=</mo><mn>3</mn><mo>+</mo><mn>4</mn><msqrt><mn>2</mn></msqrt><mo>&#8713;</mo><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is not transitive.</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msub><mi>R</mi><mn>2</mn></msub><mi>b</mi><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>2</mn></msup><mo>=</mo><mn>5</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&#8713;</mo><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><msub><mi>R</mi><mn>2</mn></msub><mi>c</mi><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>5</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&#8713;</mo><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msub><mi>R</mi><mn>2</mn></msub><mi>c</mi><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>6</mn><mo>&#8712;</mo><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is not transitive.</p>

</details>

---

### Q47. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced><mo>:</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8712;</mo><mi>Z</mi><mo>,</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>8</mn></mrow></mfenced></math> is a relation on the set of integers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math>, then the domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>R</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>&#8722;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>8</mn></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>3</mn></mfrac></mstyle></mfrac><mo>&#8804;</mo><mn>1</mn><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8712;</mo><mi>Z</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0e378e88-948a-42c5-8c4f-5a3d9f749166-image.png" style="width: 250px; height: 197px;" /></p><p>Domain of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>R</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo></math> Range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is possible integral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>coordinates</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q48. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> denote the set of all natural numbers. Define two binary relations on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>N</mi><mo>&#215;</mo><mi>N</mi><mo>:</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>10</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8712;</mo><mi>N</mi><mo>&#215;</mo><mi>N</mi><mo>:</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>10</mn></mrow></mfenced></math>. Then

**Options:**

- **(A)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are transitive relations
- **(B)** range of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>
- **(C)** range of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math>
- **(D)** both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> are symmetric relations

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) range of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}" separators="|"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>8</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced><mrow><mn>6</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced></mrow></mfenced></math> }

Range of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>

</details>

---

### Q49. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `1`

Consider the following two binary relations on the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></mrow></mfenced><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi></mrow></mfenced></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></mrow></mfenced></mrow></mfenced></math>, then :

**Options:**

- **(A)** <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is symmetric but it is not transitive
- **(B)** both <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> are not symmetric
- **(C)** both <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> are transitive
- **(D)** <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  is not symmetric but it is transitive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is symmetric but it is not transitive**

**Detailed Solution:**

<blockquote><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>)</mo><mo>&#8712;</mo><msub><mi>R</mi><mn>1</mn></msub></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo><mo>&#8713;</mo><msub><mi>R</mi><mn>1</mn></msub><mi>&#160;</mi></math></p><p>Hence, <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is not symmetric.</p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi></mrow></mfenced><mo>&#8712;</mo><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>c</mi><mo>,</mo><mi>&#160;</mi><mi>a</mi></mrow></mfenced><mo>&#8712;</mo><msub><mi>R</mi><mn>1</mn></msub></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>a</mi></mrow></mfenced><mo>&#8713;</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p>So, <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is not transitive.</p><p><math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is symmetric.</p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>a</mi></mrow></mfenced><mo>&#8712;</mo><msub><mi>R</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi></mrow></mfenced><mo>&#8712;</mo><msub><mi>R</mi><mn>1</mn></msub></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi></mrow></mfenced><mo>&#8713;</mo><msub><mi>R</mi><mn>2</mn></msub></math></p><p>So, <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is not transitive.</p></blockquote>

</details>

---

### Q50. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `1`

Consider the following two binary relations on the set $A=\{a, b, c\}: R_1=\{(\mathrm{c}, a)(b, b),(\mathrm{a}, c),(c$, $c),(b, c),(a, a)\}$ and $\mathrm{R}_2=\{(\mathrm{a}, \mathrm{b}),(\mathrm{b}, \mathrm{a}),(\mathrm{c}, \mathrm{c})$, (c, a), (a, a), (b, b), (a, c). Then

**Options:**

- **(A)** $R_2$ is symmetric but it is not transitive
- **(B)** Both $R_1$ and $R_2$ are transitive
- **(C)** Both $R_1$ and $R_2$ are not symmetric
- **(D)** $R_1$ is not symmetric but it is transitive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $R_2$ is symmetric but it is not transitive**

**Detailed Solution:**

Both $R_1$ and $R_2$ are symmetric as For any $(x, y) \in R_1$, we have $(y, x) \in R_1$ and similarly for $R_2$ Now, for $R_2,(b, a) \in R_2,(a, c) \in R_2$ but $(b, c) \notin R_2$. Similarly, for $R_1,(b, c) \in R_1,(c, a) \in R_1$ but $(b, a) \notin R_1$.
Therefore, neither $R_1$ nor $R_2$ is transitive.

</details>

---

### Q51. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be the relation defined on the set of all real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>a</mi><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>b</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is

**Options:**

- **(A)** reflexive and symmetric but not transitive
- **(B)** symmetric and transitive but not reflexive
- **(C)** reflexive and transitive but not symmetric
- **(D)** an equivalence relation

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) an equivalence relation**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>a</mi><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>b</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced><mo>:</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>a</mi><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>a</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>its reflexive relation.</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>:</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>a</mi><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>b</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mn>2</mn></msup><mi>a</mi><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>b</mi><mo>=</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>a</mi><mo>=</mo><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>b</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>a</mi><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>b</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>sec</mi><mo>&#160;</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>sec</mi><mo>&#160;</mo><mi>b</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mn>2</mn></msup><mi>a</mi><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>b</mi><mo>=</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>a</mi><mo>-</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>b</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mn>2</mn></msup><mi>b</mi><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>a</mi><mo>=</mo><mn>1</mn></math>

Hence, it is symmetric.

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>sec</mi><mo>&#160;</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>sec</mi><mo>&#160;</mo><mi>b</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>sec</mi><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>sec</mi><mo>&#160;</mo><mi>c</mi></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>sec</mi><mo>&#160;</mo><mi mathvariant="normal">a</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>sec</mi><mo>&#160;</mo><mi>c</mi></mrow></mfenced><mo>&#8658;</mo></math> transitive 

So, it is an equivalence relation.</p>

</details>

---

### Q52. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{R}=\left\{(x, y): x, y \in N\right.$ and $\left.x^2-4 x y+3 y^2=0\right\}$, where $N$ is the set of all natural numbers. Then the relation $R$ is :

**Options:**

- **(A)** reflexive but neither symmetric nor transitive.
- **(B)** symmetric and transitive.
- **(C)** reflexive and symmetric,
- **(D)** reflexive and transitive.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) reflexive and transitive.**

**Detailed Solution:**

$\mathrm{R}=\left\{(x, y): x, y \in \mathrm{N}\right.$ and $\left.x^2-4 x y+3 y^2=0\right\}$
Now, $x^2-4 x y+3 y^2=0$
$\Rightarrow(x-y)(x-3 y)=0$
$\therefore x=y$ or $x=3 y$
$\therefore \quad \mathrm{R}=\{(1,1),(3,1),(2,2),(6,2),(3,3)$, $(9,3), \ldots \ldots\}$
Since $(1,1),(2,2),(3,3), \ldots \ldots$ are present in the relation, therefore $\mathrm{R}$ is reflexive.
Since $(3,1)$ is an element of $R$ but $(1,3)$ is not the element of $\mathrm{R}$, therefore $\mathrm{R}$ is not symmetric
Here $(3,1) \in R$ and $(1,1) \in R \Rightarrow(3,1) \in R$ $(6,2) \in \mathrm{R}$ and $(2,2) \in \mathrm{R} \Rightarrow(6,2) \in \mathrm{R}$
For all such $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R}$ $\Rightarrow(a, c) \in \mathrm{R}$
Hence $\mathrm{R}$ is transitive.

</details>

---

### Q53. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $R=\{(3,3)(5,5),(9,9),(12,12),(5,12),(3,9)$, $(3,12),(3,5)\}$ be a relation on the $\operatorname{set} A=\{3,5,9,12\}$. Then, $R$ is :

**Options:**

- **(A)** reflexive, symmetric but not transitive.
- **(B)** symmetric, transitive but not reflexive.
- **(C)** an equivalence relation.
- **(D)** reflexive, transitive but not symmetric.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) reflexive, transitive but not symmetric.**

**Detailed Solution:**

Let $\mathrm{R}=\{(3,3),(5,5),(9,9),(12,12),(5,12)$, $(3,9),(3,12),(3,5)\}$ be a relation on set $\mathrm{A}=\{3,5,9,12\}$
Clearly, every element of $A$ is related to itself. Therefore, it is a reflexive.
Now, $\mathrm{R}$ is not symmetry because 3 is related to 5 but 5 is not related to 3 .
Also $\mathrm{R}$ is transitive relation because it satisfies the property that if $a \mathrm{R} b$ and $b \mathrm{R} c$ then $a \mathrm{R} c$.

</details>

---

### Q54. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `1`

Let $R$ be the set of real numbers
This question has Statement $-1$ and Statement $-2$. Of the four choices given after the statements, choose the one that best describes the two statements.
Statement-1 : $A=\{(x, y) \in R \times R: y-x$ is an integer $\}$ is an equivalence relation on $R$.
Statement-2 : $B=\{(x, y) \in R \times R: x=\alpha y$ for some rational number $\alpha\}$ is an equivalence relation on $\mathrm{R}$.

**Options:**

- **(A)** Statement $-1$ is true, Statement $-2$ is true; Statement $-2$ is not a correct explanation for Statement $-1$
- **(B)** Statement $-1$ is true, Statement- 2 is false.
- **(C)** Statement $-1$ is false, Statement $-2$ is true.
- **(D)** Statement $-1$ is true, Statement $-2$ is true; Statement $-2$ is a correct explanation for Statement $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement $-1$ is true, Statement- 2 is false.**

**Detailed Solution:**

$\mathrm{x}-\mathrm{y}$ is an integer
$x-x=0$ is an integer $\Rightarrow A$ is Reflexive
$x-y$ is an integer $\Rightarrow y-x$ is an integer $\Rightarrow A$ is symmetric
$x-y, y-z$ are integers
As sum of two integers is an integer.
$\Rightarrow(x-y)+(y-z)=x-z$ is an integer
$\Rightarrow \mathrm{A}$ is transitive. Hence statement $-1$ is true.
Also $\frac{\mathrm{x}}{\mathrm{x}}=1$ is a rational number $\Rightarrow B$ is reflexive
$\frac{\mathrm{x}}{\mathrm{y}}=\alpha$ is rational $\Rightarrow \frac{\mathrm{y}}{\mathrm{x}}$ need not be rational
i.e., $\frac{0}{1}$ is rational $\Rightarrow \frac{1}{0}$ is not rational
Hence B is not symmetric
$\Rightarrow B$ is not an equivalence relation.

</details>

---

### Q55. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

Consider the following relations:
$R=\{(x, y) \mid x, y$ are real numbers and $x=$ wy for some rational number w $\}$;
$S=\left\{\left(\frac{m}{n}, \frac{p}{q}\right) \mid m, n, p\right.$ and $q$ are integers such that $n, q \neq 0$ and $\left.q m=p n\right\}$. Then

**Options:**

- **(A)** neither $\mathrm{R}$ nor $\mathrm{S}$ is an equivalence relation
- **(B)** $S$ is an equivalence relation but $R$ is not an equivalence relation
- **(C)** $R$ and $S$ both are equivalence relations
- **(D)** $\mathrm{R}$ is an equivalence relation but $\mathrm{S}$ is not an equivalence relation

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{R}$ is an equivalence relation but $\mathrm{S}$ is not an equivalence relation**

**Detailed Solution:**

xRy need not implies $y R x$
$\mathrm{S}: \frac{\mathrm{m}}{\mathrm{n}} \mathrm{s} \frac{\mathrm{p}}{\mathrm{q}} \Leftrightarrow \mathrm{qm}=\mathrm{pn}$ $\frac{m}{n} s \frac{m}{n}$ reflexive
$$
\begin{array}{ll}
\frac{m}{n} s \frac{p}{q} & \Rightarrow \frac{p}{q} s \frac{m}{n} \text { symmetric } \\
\frac{m}{n} s \frac{p}{q}, \frac{p}{q} s \frac{r}{s} & \Rightarrow q m=p n, p s=r q \quad \Rightarrow m s=r n \text { transitive. }
\end{array}
$$
$S$ is an equivalence relation.

</details>

---

### Q56. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `3`

Let $R$ be the real line. Consider the following subsets of the plane $R \times R$.
$S=\{(x, y): y=x+1$ and $0 < x < 2\}, T=\{(x, y): x-y$ is an integer $\}$. Which one of the following is true?

**Options:**

- **(A)** neither $S$ nor $T$ is an equivalence relation on $R$
- **(B)** both $S$ and $T$ are equivalence relations on $R$
- **(C)** $S$ is an equivalence relation on $R$ but $T$ is not
- **(D)** $\mathrm{T}$ is an equivalence relation on $\mathrm{R}$ but $S$ is not

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{T}$ is an equivalence relation on $\mathrm{R}$ but $S$ is not**

**Detailed Solution:**

$$
T=\{(x, y): x-y \in l\}
$$
as $0 \in \mathrm{I} \mathrm{T}$ is a reflexive relation.
If $x-y \in 1 \Rightarrow y-x \in I$
$\therefore \mathrm{T}$ is symmetrical also
If $x-y=l_1$ and $y-z=l_2$
Then $x-z=(x-y)+(y-z)=l_1+I_2 \in I$
$\therefore \mathrm{T}$ is also transitive.
Hence $T$ is an equivalence relation.
Clearly $x \neq x+1 \Rightarrow(x, x) \notin S$
$\therefore S$ is not reflexive.

</details>

---

### Q57. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

Let W denote the words in the English dictionary. Define the relation R by :
$R=\{(x, y) \in W \times W \mid$ the words $x$ and $y$ have at least one letter in common $\}$. Then $R$ is

**Options:**

- **(A)** not reflexive, symmetric and transitive
- **(B)** reflexive, symmetric and not transitive
- **(C)** reflexive, symmetric and transitive
- **(D)** reflexive, not symmetric and transitive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) reflexive, symmetric and not transitive**

**Detailed Solution:**

Clearly $(\mathrm{x}, \mathrm{x}) \in \mathrm{R} \forall \mathrm{x} \in \mathrm{W}$. So, $\mathrm{R}$ is reflexive.
Let $(x, y) \in R$, then $(y, x) \in R$ as $x$ and $y$ have at least one letter in common. So, $R$ is symmetric.
But $R$ is not transitive for example
Let $x=$ DELHI, $y=$ DWARKA and $z=$ PARK
then $(x, y) \in R$ and $(y, z) \in R$ but $(x, z) \notin R$.

</details>

---

### Q58. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

Let $R=\{(3,3),(6,6),(9,9),(12,12),(6,12),(3,9),(3,12),(3,6)\}$ be a relation on the set $A=\{3,6,9,12\}$ . The relation is

**Options:**

- **(A)** reflexive and transitive only
- **(B)** reflexive only
- **(C)** an equivalence relation
- **(D)** reflexive and symmetric only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) reflexive and transitive only**

**Detailed Solution:**

Reflexive and transitive only.
e.g. $(3,3),(6,6),(9,9),(12,12)$ [Reflexive]
$(3,6),(6,12),(3,12)$
[Transitive].

</details>

---

### Q59. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Let $R=\{(1,3),(4,2),(2,4),(2,3),(3,1)\}$ be a relation on the set $A=\{1,2,3,4\}$. The relation $R$ is

**Options:**

- **(A)** a function
- **(B)** reflexive
- **(C)** not symmetric
- **(D)** transitive

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) not symmetric**

**Detailed Solution:**

$(2,3) \in \mathrm{R}$ but $(3,2) \notin \mathrm{R}$
Hence R is not symmetric.

</details>

---

