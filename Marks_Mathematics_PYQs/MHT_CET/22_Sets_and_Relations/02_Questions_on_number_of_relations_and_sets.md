# MHT CET Mathematics - Sets and Relations

## Topic 2: Questions on number of relations and sets

**Total Questions:** 8

---

### Q1. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $S$ be a non-empty subset of $\mathbb{R}$. Consider the following statement:
p : There is a rational number $x \in \mathrm{~S}$ such that $x\gt0$.
Which of the following statements is the negation of the statement p?

**Options:**

- **(A)** There is a rational number $x \in \mathrm{~S}$ such that $x \leq 0$.
- **(B)** There is no rational number $x \in \mathrm{~S}$ such that $x \leq 0$.
- **(C)** Every rational number $x \in \mathrm{~S}$ satisfies $x \leq 0$.
- **(D)** $x \in \mathrm{~S}$ and $x \leq 0 \Rightarrow x$ is not a rational number.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Every rational number $x \in \mathrm{~S}$ satisfies $x \leq 0$.**

**Detailed Solution:**

The given statement is $p : \exists x \in \mathrm{S}$ such that $x$ is a rational number and $x > 0$.

The negation of an existential quantifier ($\exists$) is the universal quantifier ($\forall$). The negation of the inequality $x > 0$ is $x \leq 0$.

Therefore, the negation of the statement $p$ is $\sim p : \forall x \in \mathrm{S}$, if $x$ is a rational number, then $x \leq 0$.

This can be written in words as: Every rational number $x \in \mathrm{S}$ satisfies $x \leq 0$.

Answer: Every rational number $x \in \mathrm{~S}$ satisfies $x \leq 0$.

</details>

---

### Q2. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $n(A)=4, n(B)=2$. Then the number of subsets of the set $\mathrm{A} \times \mathrm{B}$ each having at least 3 elements are

**Options:**

- **(A)** 275
- **(B)** 510
- **(C)** 219
- **(D)** 256

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 219**

**Detailed Solution:**

Given $n(A) = 4$ and $n(B) = 2$

The number of elements in $A \times B$ is $n(A \times B) = n(A) \times n(B) = 4 \times 2 = 8$

The total number of subsets of $A \times B$ is $2^8 = 256$

The number of subsets having at least 3 elements is the total number of subsets minus the number of subsets having 0, 1, or 2 elements.

Number of subsets with at least 3 elements $= 2^8 - (^{8}C_{0} + ^{8}C_{1} + ^{8}C_{2})$

$^{8}C_{0} = 1$

$^{8}C_{1} = 8$

$^{8}C_{2} = \dfrac{8 \times 7}{2} = 28$

Number of subsets with at least 3 elements $= 256 - (1 + 8 + 28) = 256 - 37 = 219$

Answer: 219

</details>

---

### Q3. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{A}=[\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{d}], \mathrm{B}=[1,2,3]$. Relation $\mathrm{R}_1, \mathrm{R}_2, \mathrm{R}_4$ are as follows:
$$
\begin{aligned}
& \mathrm{R}_1=[(\mathrm{a}, 1),(\mathrm{b}, 2),(\mathrm{c}, 1),(\mathrm{d}, 2)] \\
& \mathrm{R}_2=[(\mathrm{a}, 1),(\mathrm{b}, 1),(\mathrm{c}, 1),(\mathrm{d}, 1)] \\
& \mathrm{R}_3=[(\mathrm{a}, 2),(\mathrm{b}, 3),(\mathrm{c}, 2),(\mathrm{d}, 2)] \\
& \mathrm{R}_4=[(\mathrm{a}, 1),(\mathrm{b}, 2),(\mathrm{a}, 2),(\mathrm{d}, 3)], \text { then }
\end{aligned}
$$

**Options:**

- **(A)** only $\mathrm{R}_3$ and $\mathrm{R}_4$ are not functions
- **(B)** only $R_1$ and $R_2$ are not functions
- **(C)** only $\mathrm{R}_3$ is not a function
- **(D)** only $\mathrm{R}_4$ is not a function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) only $\mathrm{R}_4$ is not a function**

**Detailed Solution:**

We find that in $R_4, f(a)=1$ and $f(a)=2$. Hence $R_4$ is not a function.

</details>

---

### Q4. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{A}=\{x, y, z\}, \mathrm{B}=\{1,2\}$, then the total number of relations from set $\mathrm{A}$ to set $\mathrm{B}$ are

**Options:**

- **(A)** 64
- **(B)** 16
- **(C)** 32
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 64**

**Detailed Solution:**

It is given that $A=\{x, y, z\}$ and $B=\{1,2\} .$
$\therefore A \times B=\{(x, 1),(x, 2),(y, 1),(y, 2),(z, 1),(z, 2)\}$
Since $n(A \times B)=6$, the number of subsets of $A \times B$ is $2^{6} .$
Therefore, the number of relations from $A$ to $B$ is $2^{6} .$

</details>

---

### Q5. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Given $\mathrm{A}=\{1,2,3,4,5\}, \mathrm{B}=\{1,4,5\} .$ If $\mathrm{R}$ is a relation from $\mathrm{A}$ to $\mathrm{B}$ such that $\quad(x, y)$
$\in \mathrm{R}$ with $x>y$, then range of $\mathrm{R}$ is

**Options:**

- **(A)** {1,4}
- **(B)** {4,5}
- **(C)** {1,4,5}
- **(D)** {2,4}

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) {1,4}**

**Detailed Solution:**

$A=\{1,2,3,4,5\} ; B=\{1,4,5\}$
$R: \quad A \rightarrow B(x>y)$
Domain 
$\left(\begin{array}{l}2 \\ 3 \\ 4 \\ 5\end{array}\right)$
Range
$\left(\begin{array}{l}1 \\ 4\end{array}\right)$
Range $R=\{1,4\}$

</details>

---

### Q6. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\{x / x$ is a prime number, $0 \leq x \leq 9]$, then the number of elements of power
set of $A$ is

**Options:**

- **(A)** 12
- **(B)** 4
- **(C)** 16
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 16**

**Detailed Solution:**

$\begin{aligned} A=\{2,3,5,7\} & \\ \text { Power set of } A &=2^{4} \\ &=16 . \end{aligned}$

</details>

---

### Q7. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\{2,4\}, \quad B=\{3,4,5\}$, then $(\mathrm{A} \cap \mathrm{B}) \times(\mathrm{AUB})=$

**Options:**

- **(A)** $\{(3,2),(3,4),(4,4),(5,4)\}$
- **(B)** $\{(2,3),(2,4),(2,5)\}$
- **(C)** $\{(4,2),(4,3),(4,4),(4,5)\}$
- **(D)** $\{(4,3),(4,4),(4,5)\}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\{(4,2),(4,3),(4,4),(4,5)\}$**

**Detailed Solution:**

$\mathrm{A} \cap \mathrm{B}=\{4\}$
$\mathrm{A} \cup \mathrm{B}=\{2,3,4,5\}$
Hence
$(\mathrm{A} \cap \mathrm{B}) \times(\mathrm{A} \cup \mathrm{B})$
$=\{(4,2),(4,3),(4,4),(4,5)\}$

</details>

---

### Q8. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>A</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mi>x</mi><mo>∈</mo><mi>R</mi><mo>:</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></mrow></mfenced><mo>,</mo></math> then <math><mi>n</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>4</mn></math>**

**Detailed Solution:**

Given: <math><mi>A</mi><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mi>x</mi><mo>∈</mo><mi>R</mi><mo>:</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mo>=</mo><mfenced close="}" open="" separators="|"><mrow><mn>0</mn></mrow></mfenced></mrow></mfenced></math>  
<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>  
<math><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mi mathvariant="normal"></mi><mn>3</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>±</mo><mn>2</mn><mo>,</mo><mo>±</mo><mn>3</mn></math>  
Hence, <math><mi>n</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math>

</details>

---

