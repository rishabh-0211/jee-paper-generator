# JEE Advanced Mathematics - Sets and Relations

## Topic 2: Questions on number of relations and sets

**Total Questions:** 6

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `numerical` | *Level:* `3`

Let $S = \{1, 2, 3, \ldots, 10\}$. Consider the set
$X = \{R : R$ is an equivalence relation on the set $S$ such that $R$ has exactly $42$ elements$\}$.

Then the number of elements in $X$ is _____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2520**

**Detailed Solution:**

An equivalence relation on a set $S$ corresponds to a partition of $S$ into disjoint equivalence classes. Let the sizes of these equivalence classes be $a_1, a_2, \ldots, a_k$.

The number of elements in the equivalence relation $R$ is given by the sum of the squares of the sizes of its equivalence classes:
$\sum_{i=1}^k a_i^2 = 42$

Since the total number of elements in $S$ is $10$, we also have:
$\sum_{i=1}^k a_i = 10$

We need to find all possible partitions of $10$ such that the sum of their squares is $42$. Let's check the possible sizes of the largest equivalence class, $a_1$:

Case 1: $a_1 = 6$
$a_1^2 = 36$. The remaining sum of squares is $42 - 36 = 6$, and the remaining sum of elements is $10 - 6 = 4$.
The only way to partition $4$ such that the sum of squares is $6$ is $2, 1, 1$ (since $2^2 + 1^2 + 1^2 = 6$).
Thus, one valid partition is $\{6, 2, 1, 1\}$.

Case 2: $a_1 = 5$
$a_1^2 = 25$. The remaining sum of squares is $42 - 25 = 17$, and the remaining sum of elements is $10 - 5 = 5$.
The only way to partition $5$ such that the sum of squares is $17$ is $4, 1$ (since $4^2 + 1^2 = 17$).
Thus, another valid partition is $\{5, 4, 1\}$.

Case 3: $a_1 \le 4$
The maximum possible sum of squares would be for the partition $\{4, 4, 2\}$, which gives $4^2 + 4^2 + 2^2 = 36 < 42$. No other partitions can yield a sum of $42$.

Now, we calculate the number of ways to form these partitions from the $10$ elements of $S$.

For the partition $\{6, 2, 1, 1\}$:
The number of ways to divide $10$ elements into groups of sizes $6, 2, 1, 1$ is:
$\dfrac{10!}{6! \times 2! \times 1! \times 1! \times 2!} = \dfrac{3628800}{720 \times 2 \times 1 \times 1 \times 2} = \dfrac{3628800}{2880} = 1260$
(Note: We divide by $2!$ because there are two groups of identical size $1$).

For the partition $\{5, 4, 1\}$:
The number of ways to divide $10$ elements into groups of sizes $5, 4, 1$ is:
$\dfrac{10!}{5! \times 4! \times 1!} = \dfrac{3628800}{120 \times 24 \times 1} = \dfrac{3628800}{2880} = 1260$

Total number of equivalence relations in $X$ is:
$1260 + 1260 = 2520$

Answer: $2520$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `numerical` | *Level:* `3`

Let the set of all relations $R$ on the set $\{a, b, c, d, e, f\}$, such that $R$ is reflexive and symmetric, and $R$ contains exactly 10 elements, be denoted by $S$. Then the number of elements in $S$ is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **105**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/dotJ_FKh6L4BVL2nbdGcgwQqrQArjgv3o2UyULbVZCs.original.fullsize.png">
For relation to be reflexive all the diagonal elements must be taken and out of remaining 30 elements there are 15 pairs and we need 2 pairs such that R contains exactly 10 elements and is both reflexive and symmetric.
$\therefore$ number of ways $={ }^{15} \mathrm{C}_2=105$

</details>

---

### Q3. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `2`

If the value of $n(Y)+n(Z)$ is $k^2$, then $|k|$ is
Let \(S=\{1,2,3,4,5,6\}\) and \(X\) be the set of all relations \(R\) from \(S\) to \(S\) that satisfy both the following properties:
i. \(R\) has exactly 6 elements.
ii. For each \((a, b) \in R\), we have \(|a-b| \geq 2\).
Let \(Y=\{R \in X\) : The range of \(R\) has exactly one element \(\}\) and \(Z=\{R \in X: R\) is a function from \(S\) to \(S\}\).
Let \(n(A)\) denote the number of elements in a set \(A\).

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

given $|a-b| \geq 2$ so if
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/hn7i07O6ZaG7UvnOx0EtvNsr1x2V_GouFl2skzjeIFQ.original.fullsize.png">
i.e. Total elements in $\mathrm{X}$ is ${ }^{20} \mathrm{C}_6$
Now for $\mathrm{n}(\mathrm{Y})$,
range of $\mathrm{R}$ has exactly one element i.e. second elements must be constant in $\mathrm{R}$ and since $\mathrm{R}$ must have 6 element so it is not possible to satisfy both condition so $\mathrm{n}(\mathrm{Y})=0$.
$\begin{aligned} & \text { for } \quad n(z) \\ & 1 \rightarrow 3,4,5,6 \\ & 2 \rightarrow 4,5,6 \\ & 3 \rightarrow 1,5,6 \\ & 4 \rightarrow 1,2,6 \\ & 5 \rightarrow 1,2,3 \\ & 6 \rightarrow 1,2,3,4 \\ & \end{aligned}$
no. of relation that are function will be $\quad={ }^4 \mathrm{C}_1 \times{ }^3 \mathrm{C}_1 \times{ }^3 \mathrm{C}_1 \times{ }^3 \mathrm{C}_1 \times{ }^3 \mathrm{C}_1 \times{ }^4 \mathrm{C}_1$
$\begin{aligned} & =(4 \times 3 \times 3)^2=k^2 \\ & \text { i.e. } \mathrm{k}=36\end{aligned}$

</details>

---

### Q4. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `2`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/on97X5TCK54arKma2zxcmrlZp_wpNv-ZITyDmpt8iQk.original.fullsize.png">
If $n(X)={ }^m C_6$, then the value of $m$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

\(S=\{1,2,3,4,5,6\} \quad R: S \rightarrow S\)
Number of elements in \(R=6\)
and for each \((a, b) \in R ;|a-b| \geq 2\)
\(X \rightarrow\) set of all relation \(R: S \rightarrow S\)
If \(a=1, b=3,4,5,6 \rightarrow(4)\)
\(a=2, b=4,5,6 \rightarrow(3)\)
\(a=3, b=1,5,6 \rightarrow(3)\)
\(a=4, b=1,2,6 \rightarrow(3)\)
\(a=5, b=1,2,3 \rightarrow(3)\)
\(a=6, b=1,2,3,4 \rightarrow(4)\)
Total number of ordered pairs \((a, b)\)
s.t. \(|a-b| \geq 2 =20\)
\(\therefore n(X)=\) number of elements in \(\mathrm{X}={ }^{20} C_6\)
\(\therefore m=20\)

</details>

---

### Q5. JEE Advanced 2017 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mn>1,2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mn>9</mn></mrow></mfenced></math>. For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1,2</mn><mo>,</mo><mo>&#8230;</mo><mn>5</mn><mo>,</mo></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mi>k</mi></msub></math> be the number of subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>, each containing five elements out of which exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> are odd. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mn>1</mn></msub><mo>+</mo><msub><mi>N</mi><mn>2</mn></msub><mo>+</mo><msub><mi>N</mi><mn>3</mn></msub><mo>+</mo><msub><mi>N</mi><mn>4</mn></msub><mo>+</mo><msub><mi>N</mi><mn>5</mn></msub><mo>=</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>125</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>252</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>210</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>126</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>126</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mn>1</mn></msub><mo>+</mo><msub><mi>N</mi><mn>2</mn></msub><mo>+</mo><msub><mi>N</mi><mn>3</mn></msub><mo>+</mo><msub><mi>N</mi><mn>4</mn></msub><mo>+</mo><msub><mi>N</mi><mn>5</mn></msub><mo>=</mo></math> Total ways &ndash; {when no odd}</p><p>Total ways <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>9</mn></msup><msub><mi>C</mi><mn>5</mn></msub></math></p><p>Number of ways when no odd, is zero     (<math><mo>&#8757;</mo></math> only available even are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mo>&#160;</mo><mn>9</mn></msup><msub><mi>C</mi><mn>5</mn></msub><mo>-</mo><mi>zero</mi><mo>=</mo><mn>126</mn></math></p>

</details>

---

### Q6. JEE Advanced 2010 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $S=\{1,2,3,4\}$. The total number of unordered pairs of disjoint subsets of $S$ is equal to

**Options:**

- **(A)** 25
- **(B)** 34
- **(C)** 42
- **(D)** 41

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 41**

**Detailed Solution:**

Let $A \cap B=\phi, A, B \subset S$
$$
\begin{aligned}
& 3^4=\frac{81+1}{2}=41 \\
\Rightarrow \quad & \frac{3^4+1}{2}=41
\end{aligned}
$$

</details>

---

