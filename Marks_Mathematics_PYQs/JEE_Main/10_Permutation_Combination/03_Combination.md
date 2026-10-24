# JEE Main Mathematics - Permutation Combination

## Topic 3: Combination

**Total Questions:** 42

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A building has ground floor and 10 more floors. Nine persons enter in a lift at the ground floor. The lift goes up to the $10^{\text{th}}$ floor. The number of ways, in which any 4 persons exit at a floor and the remaining 5 persons exit at a different floor, if the lift does not stop at the first and the second floors, is equal to :

**Options:**

- **(A)** $2184$
- **(B)** $3064$
- **(C)** $7056$
- **(D)** $11340$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7056$**

**Detailed Solution:**

Total number of persons = $9$

The lift goes up to the $10^{\text{th}}$ floor but does not stop at the $1^{\text{st}}$ and $2^{\text{nd}}$ floors. Thus, the available floors for the persons to exit are from the $3^{\text{rd}}$ to the $10^{\text{th}}$ floor.

Number of available floors = $8$

The number of ways to select $4$ persons out of $9$ to form the first group is $^{9}C_{4}$. The remaining $5$ persons automatically form the second group.

$^{9}C_{4} = \dfrac{9 \times 8 \times 7 \times 6}{4 \times 3 \times 2 \times 1} = 126$

Now, these two distinct groups must exit at two different floors out of the $8$ available floors. The number of ways to assign $2$ different floors to the $2$ groups is $^{8}P_{2}$.

$^{8}P_{2} = 8 \times 7 = 56$

Total number of ways = $126 \times 56 = 7056$

Answer: $7056$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of $4$-letter words, with or without meaning, each consisting of two vowels and two consonants that can be formed from the letters of the word INCONSEQUENTIAL, without repeating any letter, is:

**Options:**

- **(A)** $2670$
- **(B)** $2840$
- **(C)** $2920$
- **(D)** $3600$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3600$**

**Detailed Solution:**

The given word is INCONSEQUENTIAL.

The vowels present in the word are I, O, E, U, A. There are $5$ distinct vowels.

The consonants present in the word are N, C, S, Q, T, L. There are $6$ distinct consonants.

We need to form $4$-letter words consisting of $2$ vowels and $2$ consonants without repeating any letter. This means all $4$ letters in the formed word must be distinct.

Number of ways to select $2$ distinct vowels from $5$ distinct vowels = $^{5}C_{2} = \dfrac{5 \times 4}{2} = 10$

Number of ways to select $2$ distinct consonants from $6$ distinct consonants = $^{6}C_{2} = \dfrac{6 \times 5}{2} = 15$

Number of ways to arrange the $4$ selected letters = $4! = 24$

Total number of $4$-letter words that can be formed = $10 \times 15 \times 24 = 3600$

Answer: $3600$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A box contains $5$ blue, $6$ yellow and $4$ red balls. The number of ways, of drawing $8$ balls containing at least two balls of each colour, is :

**Options:**

- **(A)** $4100$
- **(B)** $4140$
- **(C)** $4230$
- **(D)** $4290$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4100$**

**Detailed Solution:**

Let $B$, $Y$, and $R$ be the number of blue, yellow, and red balls drawn respectively.

We are given $B + Y + R = 8$ with $B \ge 2$, $Y \ge 2$, and $R \ge 2$.

The possible combinations for $(B, Y, R)$ are:
Case 1: $(2, 2, 4)$
Case 2: $(2, 3, 3)$
Case 3: $(2, 4, 2)$
Case 4: $(3, 2, 3)$
Case 5: $(3, 3, 2)$
Case 6: $(4, 2, 2)$

The number of ways for each case is calculated as follows:
Case 1: $^{5}C_{2} \times ^{6}C_{2} \times ^{4}C_{4} = 10 \times 15 \times 1 = 150$
Case 2: $^{5}C_{2} \times ^{6}C_{3} \times ^{4}C_{3} = 10 \times 20 \times 4 = 800$
Case 3: $^{5}C_{2} \times ^{6}C_{4} \times ^{4}C_{2} = 10 \times 15 \times 6 = 900$
Case 4: $^{5}C_{3} \times ^{6}C_{2} \times ^{4}C_{3} = 10 \times 15 \times 4 = 600$
Case 5: $^{5}C_{3} \times ^{6}C_{3} \times ^{4}C_{2} = 10 \times 20 \times 6 = 1200$
Case 6: $^{5}C_{4} \times ^{6}C_{2} \times ^{4}C_{2} = 5 \times 15 \times 6 = 450$

Total number of ways $= 150 + 800 + 900 + 600 + 1200 + 450 = 4100$

Answer: $4100$

</details>

---

### Q4. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $p_n$ denote the total number of triangles formed by joining the vertices of an $n$-side regular polygon. If $p_{n+1} - p_n = 66$, then the sum of all distinct prime divisors of $n$ is:

**Options:**

- **(A)** $7$
- **(B)** $8$
- **(C)** $5$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

The number of triangles formed by joining the vertices of an $n$-sided regular polygon is given by $p_n = ^{n}C_{3}$.

Given that $p_{n+1} - p_n = 66$.

$^{n+1}C_{3} - ^{n}C_{3} = 66$

Using the property $^{n+1}C_{r} - ^{n}C_{r} = ^{n}C_{r-1}$, we get:

$^{n}C_{2} = 66$

$\dfrac{n(n-1)}{2} = 66$

$n(n-1) = 132$

$n^2 - n - 132 = 0$

$(n-12)(n+11) = 0$

Since $n$ must be a positive integer, $n = 12$.

The prime factorization of $12$ is $2^2 \times 3$. The distinct prime divisors of $12$ are $2$ and $3$.

The sum of all distinct prime divisors of $n$ is $2 + 3 = 5$.

Answer: $5$

</details>

---

### Q5. JEE Main 2026 (23 January Shift 2)

*Type:* `numerical` | *Level:* `2`

Let S denote the set of 4-digit numbers $a b c d$ such that $a>b>c>d$ and P denote the set of 5 -digit numbers having product of its digits equal to 20. Then $n(\mathrm{~S})+n(\mathrm{P})$ is equal to $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **260**

**Detailed Solution:**

$n(S)$: Choose 4 distinct digits from $\{0,1,\ldots,9\}$ and arrange in decreasing order. $n(S) = \binom{10}{4} = 210$.
$n(P)$: 5-digit numbers with digit product $= 20 = 2^2 \times 5$. All digits $\ge 1$ (else product $= 0$). Must include exactly one $5$, remaining 4 digits multiply to $4$.
Case 1: $\{1,1,1,4,5\}$: $\frac{5!}{3!} = 20$ arrangements.
Case 2: $\{1,1,2,2,5\}$: $\frac{5!}{2!\cdot 2!} = 30$ arrangements.
$n(P) = 50$. Hence $n(S) + n(P) = 210 + 50 = 260$.

</details>

---

### Q6. JEE Main 2026 (22 January Shift 1)

*Type:* `numerical` | *Level:* `2`

Let ABC be a triangle. Consider four points $\mathrm{p}_{1}, \mathrm{p}_{2}, \mathrm{p}_{3}, \mathrm{p}_{4}$ on the side AB, five points $p_{5}, p_{6}, p_{7}, p_{8}, p_{9}$ on the side $B C$, and four points $p_{10}, p_{11}, p_{12}, p_{13}$ on the side AC. None of these points is a vertex of the triangle ABC. Then the total number of pentagons, that can be formed by taking all the vertices from the points $\mathrm{p}_{1}, \mathrm{p}_{2}, \ldots, \mathrm{p}_{13}$, is $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **660**

**Detailed Solution:**

Points: 4 on AB, 5 on BC, 4 on AC. For a valid pentagon, no 3 vertices can be collinear, so at most 2 points from each side.
Only valid distribution $(a, b, c)$ with $a+b+c = 5$ and each $\le 2$ is permutations of $(1, 2, 2)$:
$(1,2,2)$: $\binom{4}{1}\binom{5}{2}\binom{4}{2} = 4 \cdot 10 \cdot 6 = 240$
$(2,1,2)$: $\binom{4}{2}\binom{5}{1}\binom{4}{2} = 6 \cdot 5 \cdot 6 = 180$
$(2,2,1)$: $\binom{4}{2}\binom{5}{2}\binom{4}{1} = 6 \cdot 10 \cdot 4 = 240$
Total $= 240 + 180 + 240 = 660$.

</details>

---

### Q7. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of strictly increasing functions $f$ from the set $\{1,2,3,4,5,6\}$ to the set $\{1,2,3, \ldots., 9\}$ such that $f(i) \neq i$ for $1 \leq i \leq 6$, is equal to :

**Options:**

- **(A)** $27$
- **(B)** $22$
- **(C)** $21$
- **(D)** $28$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $28$**

**Detailed Solution:**

For strictly increasing $f$, if we choose elements $a_1 < a_2 < \cdots < a_6$, then $f(i) = a_i$.
Since $f(i) \geq i$ always, condition $f(i) \neq i$ means $f(i) \geq i + 1$ for all $i$.
Let $h(i) = f(i) - i$. Then $h(i) \geq 1$, $h(6) \leq 3$, and $h$ is non-decreasing.
So $h(i) \in \{1, 2, 3\}$ for all $i$.
Number of non-decreasing sequences of length 6 from $\{1, 2, 3\} = \binom{8}{2} = 28$.

</details>

---

### Q8. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

There are 12 points in a plane, no three of which are in the same straight line, except 5 points which are collinear. Then the total number of triangles that can be formed with the vertices at any three of these 12 points is

**Options:**

- **(A)** 230
- **(B)** 220
- **(C)** 200
- **(D)** 210

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 210**

**Detailed Solution:**

${ }^{12} \mathrm{C}_3-{ }^5 \mathrm{C}_3=210$

</details>

---

### Q9. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let p be the number of all triangles that can be formed by joining the vertices of a regular polygon P of n sides and q be the number of all quadrilaterals that can be formed by joining the vertices of $P$. If $p+q=126$, then the eccentricity of the ellipse $\frac{x^2}{16}+\frac{y^2}{n}=1$ is :

**Options:**

- **(A)** $\frac{3}{4}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{\sqrt{7}}{4}$
- **(D)** $\frac{1}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{\sqrt{2}}$**

**Detailed Solution:**

$\begin{aligned} & \text { Total trangles }=\Rightarrow={ }^{\mathrm{h}} \mathrm{C}_3 \\ & \text { Total auadrilaterals }={ }^{\mathrm{h}} \mathrm{C}_4=\mathrm{q} \\ & { }^{\mathrm{n}} \mathrm{C}_3+{ }^{\mathrm{n}} \mathrm{C}_4=126 \Rightarrow{ }^{\mathrm{n}+1} \mathrm{C}_4=126 \\ & \Rightarrow \mathrm{n}+1=9 \Rightarrow \mathrm{n}=8 \\ & \frac{\mathrm{x}^2}{16}+\frac{\mathrm{y}^2}{\mathrm{n}}=1 \Rightarrow \frac{\mathrm{x}^2}{16}+\frac{\mathrm{y}^2}{8}=1 \\ & \mathrm{e}=\sqrt{1-\frac{8}{16}}=\sqrt{\frac{8}{16}}=\frac{1}{\sqrt{2}}\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

From a group of 7 batsmen and 6 bowlers, 10 players are to be chosen for a team, which should include atleast 4 batsmen and atleast 4 bowlers. One batsmen and one bowler who are captain and vice-captain respectively of the team should be included. Then the total number of ways such a selection can be made, is

**Options:**

- **(A)** 165
- **(B)** 155
- **(C)** 145
- **(D)** 135

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 155**

**Detailed Solution:**

7 Batsmen \& 6 Bowlers
To select 10 players including atleast
4 Batsmen \& 4 Bowlers
Captain \& vice-captain already selected
$\begin{aligned}
& \text { No. of ways }={ }^6 \mathrm{C}_5 \times{ }^5 \mathrm{C}_3+{ }^6 \mathrm{C}_4 \times{ }^5 \mathrm{C}_4+{ }^6 \mathrm{C}_3 \times{ }^5 \mathrm{C}_5 \\
& =6 \times 10+15 \times 5+20 \times 1 \\
& =60+75+20=155
\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Line $L_1$ of slope 2 and line $L_2$ of slope $\frac{1}{2}$ intersect at the origin O . In the first quadrant, $\mathrm{P}_1, \mathrm{P}_2, \ldots . \mathrm{P}_{12}$ are 12 points on line $L_1$ and $Q_1, Q_2, \ldots . . Q_9$ are 9 points on line $L_2$. Then the total number of triangles, that can be formed having vertices at three of the 22 points $\mathrm{O}, \mathrm{P}_1, \mathrm{P}_2, \ldots \mathrm{P}_{12}$, $\mathrm{Q}_1, \mathrm{Q}_2, \ldots . \mathrm{Q}_9$, is:

**Options:**

- **(A)** $1080$
- **(B)** $1134$
- **(C)** $1026$
- **(D)** $1188$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1134$**

**Detailed Solution:**

Total number of $\Delta$ are
$\begin{aligned}
& ={ }^9 \mathrm{C}_1{ }^{12} \mathrm{C}_2+{ }^9 \mathrm{C}_2{ }^{12} \mathrm{C}_1+{ }^1 \mathrm{C}_1{ }^9 \mathrm{C}_1{ }^{12} \mathrm{C}_1 \\
& =594+432+108 \\
& =1134
\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Group A consists of 7 boys and 3 girls, while group B consists of 6 boys and 5 girls. The number of ways, 4 boys and 4 girls can be invited for a picnic if 5 of them must be from group $A$ and the remaining 3 from group $B$, is equal to :

**Options:**

- **(A)** 8750
- **(B)** 9100
- **(C)** 8925
- **(D)** 8575

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8925**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KLiYg-DBlqoSQc4Wx-oK-mU5Hog6gLFxF3xKf7eP9eM.original.fullsize.png">

</details>

---

### Q13. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

In an examination of Mathematics paper, there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> questions of equal marks and the question paper is divided into three sections : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>,</mo><mi mathvariant="normal">B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math>. A student is required to attempt total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> questions taking at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> questions from each section. If section <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> questions, section <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> questions and section <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> questions, then the total number of ways a student can select <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> questions is _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11376**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Mathematics paper has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> questions of equal marks</p><p>and have three sections <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>,</mo><mo> </mo><mi mathvariant="normal">B</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mi mathvariant="normal">C</mi></math>, also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> questions, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> questions and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> questions,</p><p>Now, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> questions from each section are selected,</p><p>then remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> questions can be selected either in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo> </mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></math> {as we have already selected <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>×</mo><mn>3</mn><mo>=</mo><mn>12</mn></math> questions}</p><p>So, the total ways will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>×</mo><mn>2</mn><mo>+</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>×</mo><mn>2</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>×</mo><mn>2</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>·</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>56</mn><mo>·</mo><mn>6</mn><mo>·</mo><mn>6</mn><mo>+</mo><mn>28</mn><mo>·</mo><mn>6</mn><mo>·</mo><mn>15</mn><mo>·</mo><mn>2</mn><mo>+</mo><mn>56</mn><mo>·</mo><mn>15</mn><mo>·</mo><mn>2</mn><mo>+</mo><mn>70</mn><mo>·</mo><mn>6</mn><mo>·</mo><mn>2</mn><mo>+</mo><mn>8</mn><mo>·</mo><mn>15</mn><mo>·</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2016</mn><mo>+</mo><mn>5040</mn><mo>+</mo><mn>1680</mn><mo>+</mo><mn>840</mn><mo>+</mo><mn>1800</mn><mo>=</mo><mn>11376</mn></math></p></blockquote>

</details>

---

### Q14. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Some couples participated in a mixed doubles badminton tournament. If the number of matches played, so that no couple played in a match, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>840</mn></math>, then the total numbers of persons, who participated in the tournament, is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Some couples participated in a mixed doubles badminton tournament. If the number of matches played, so that no couple played in a match, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>840</mn></math>,</p><p>Now Let total number of persons be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math>, so number of couples will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></p><p>Now number of matches played, so that no couple played in a match is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mmultiscripts><mo>&#183;</mo><mn>2</mn><mo>=</mo><mn>840</mn></math></p><p>{as if we choose couple as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>A</mi><mo>,</mo><mi>B</mi></mrow></mfenced></math> and other couple as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>C</mi><mo>,</mo><mi>D</mi></mrow></mfenced></math> and taking other two couple as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mi>w</mi><mo>,</mo><mi>z</mi></mrow></mfenced></math>, so the possible combination of the match  where no couple played in a match will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>A</mi><mo>,</mo><mi>x</mi></mrow></mfenced><mo>&#8594;</mo><mfenced close="}" open="{"><mrow><mi>C</mi><mo>,</mo><mi>w</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mi>C</mi><mo>,</mo><mi>x</mi></mrow></mfenced><mo>&#8594;</mo><mfenced close="}" open="{"><mrow><mi>A</mi><mo>,</mo><mi>w</mi></mrow></mfenced><mo>&#160;</mo></math>, hence there are two possible combination after choosing }</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mo>&#183;</mo><mn>6</mn><mo>&#183;</mo><mn>7</mn><mo>&#183;</mo><mn>8</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>8</mn></math></p><p>Hence, the number of persons will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi><mo>=</mo><mn>16</mn></math></p></blockquote>

</details>

---

### Q15. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

A class contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> boys and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> girls. If the number of ways of selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> boys and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> girls from the class is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>168</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>+</mo><mn>3</mn><mi>g</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mtext>&#160;boys&#160;and&#160;g&#160;girls</mtext></math></p><p>Also given total ways of selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mtext>&#160;boys&#160;and&#160;2&#160;girls</mtext></math> which will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>b</mi></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>g</mi></mmultiscripts><mo>=</mo><mn>168</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mi>b</mi><mfenced><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mi>g</mi><mfenced><mrow><mi>g</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>=</mo><mn>168</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>b</mi><mfenced><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>g</mi><mfenced><mrow><mi>g</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>b</mi><mfenced><mrow><mi>b</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>g</mi><mfenced><mrow><mi>g</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn></math></p><p>Now on comparing both side we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo><mn>3</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mi>b</mi><mo>+</mo><mn>3</mn><mi>g</mi><mo>=</mo><mn>8</mn><mo>+</mo><mn>9</mn><mo>=</mo><mn>17</mn></math></p></blockquote>

</details>

---

### Q16. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `1`

There are ten boys <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>1</mn></msub><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>B</mi></mrow><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><msub><mi>B</mi><mn>10</mn></msub></math> and five girls <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>G</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">G</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><msub><mi mathvariant="normal">G</mi><mn>5</mn></msub></math>  in a class. Then the number of ways of forming a group consisting of three boys and three girls, if both <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>2</mn></msub></math> together should not be the members of a group, is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1120**

**Detailed Solution:**

<p>Given, total number of boys is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and total number of girls is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></p><p>So total number of selections <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>=</mo><mn>1200</mn></math></p><p>No. of selections in which <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>B</mi><mn>2</mn></msub></math> both are there in group <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>=</mo><mn>80</mn></math></p><p>Required no. of selections <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1200</mn><mo>-</mo><mn>80</mn><mo>=</mo><mn>1120</mn></math></p>

</details>

---

### Q17. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Team <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>A</mi><none></none><mo>&#39;</mo><mprescripts></mprescripts><none></none><mo>&#39;</mo></mmultiscripts></math> consists of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> boys and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> girls and Team <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>B</mi><none></none><mo>&#39;</mo><mprescripts></mprescripts><none></none><mo>&#39;</mo></mmultiscripts></math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> boys and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> girls. If a total of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math> single matches can be arranged between these two teams when a boy plays against a boy and a girl plays against a girl, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Total matches between boys of both team<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>=</mo><mn>28</mn></math></p><p>Total matches between girls of both team<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><mo>=</mo><mn>6</mn><mi>n</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><mo>+</mo><mn>6</mn><mi>n</mi><mo>=</mo><mn>52</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q18. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

There are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> sections in a question paper and each section contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> questions. A candidate has to answer a total of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> questions, choosing at least one question from each section. Then the number of ways, in which the candidate can choose the questions, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3000</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1500</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2255</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2250</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2250</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mn>5</mn><mi mathvariant="normal">Q</mi><mo>&#160;&#160;</mo><mi mathvariant="normal">B</mi><mo>&#8594;</mo><mn>5</mn><mi mathvariant="normal">Q</mi><mo>&#160;&#160;</mo><mi mathvariant="normal">C</mi><mo>&#8594;</mo><mn>5</mn><mi mathvariant="normal">Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">A</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">A</mi><mn>2</mn></msub><mo>,</mo><msub><mi mathvariant="normal">A</mi><mn>3</mn></msub><mo>,</mo><msub><mi mathvariant="normal">A</mi><mn>4</mn></msub><mo>,</mo><msub><mi mathvariant="normal">A</mi><mn>5</mn></msub><mo>&#160;&#160;</mo><msub><mi mathvariant="normal">B</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">B</mi><mn>2</mn></msub><mo>,</mo><msub><mi mathvariant="normal">B</mi><mn>3</mn></msub><mo>,</mo><msub><mi mathvariant="normal">B</mi><mn>4</mn></msub><mo>,</mo><msub><mi mathvariant="normal">B</mi><mn>5</mn></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>,</mo><msub><mi mathvariant="normal">C</mi><mn>3</mn></msub><mo>,</mo><msub><mi mathvariant="normal">C</mi><mn>4</mn></msub><mo>,</mo><msub><mi mathvariant="normal">C</mi><mn>5</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">A</mi><mn>1</mn></msub><msub><mi mathvariant="normal">A</mi><mn>2</mn></msub><msub><mi mathvariant="normal">A</mi><mn>3</mn></msub><msub><mi mathvariant="normal">B</mi><mn>1</mn></msub><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>&#8658;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>=</mo><mn>750</mn></math>, where three questions are picked from any of the subject and one each from other two subjects.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">A</mi><mn>1</mn></msub><msub><mi mathvariant="normal">A</mi><mn>2</mn></msub><msub><mi mathvariant="normal">B</mi><mn>1</mn></msub><msub><mi mathvariant="normal">B</mi><mn>2</mn></msub><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>&#8658;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>=</mo><mn>1500</mn></math>, where one question is picked from one of the subject and two each from rest of the two subjects.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>Total number of ways<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2250</mn></math></p>

</details>

---

### Q19. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A group of students comprises of <math><mn>5</mn></math> boys and n girls. If the number of ways, in which a team of <math><mn>3</mn></math> students can randomly be selected from this group such that there is at least one boy and at least one girl in each team, is <math><mn>1750</mn><mo>,</mo></math> then n is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>**

**Detailed Solution:**

<table border="1" cellpadding="1" cellspacing="1" style="width:100%;">	<tbody>		<tr>			<td>(5)</td>			<td>(n)</td>		</tr>		<tr>			<td>Boys</td>			<td>Girls</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>		</tr>	</tbody></table>Here total number of ways

<math> <mrow> <mo>=</mo><msup> <mtext>&#160;</mtext> <mn>5</mn> </msup> <msub> <mtext>C</mtext> <mn>2</mn> </msub> <mo>&#215;</mo><msup> <mtext>&#160;</mtext> <mtext>n</mtext> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> <msup> <mo>+</mo> <mn>5</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> <mo>&#215;</mo><msup> <mtext>&#160;</mtext> <mtext>n</mtext> </msup> <msub> <mtext>C</mtext> <mn>2</mn> </msub> <mo>=</mo><mn>1750</mn></mrow> </math>

<math> <mrow> <mo>&#8658;</mo><mn>10</mn><mtext>n</mtext><mo>+</mo><mn>5</mn><mfrac> <mrow> <mtext>n</mtext><mrow><mo>(</mo> <mrow> <mtext>n</mtext><mo>&#8722;</mo><mn>1</mn></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </mfrac> <mo>=</mo><mn>1750</mn></mrow> </math>

<math> <mrow> <mo>&#8658;</mo><msup> <mtext>n</mtext> <mn>2</mn> </msup> <mo>+</mo><mn>3</mn><mtext>n</mtext><mo>&#8722;</mo><mn>700</mn><mo>=</mo><mn>0</mn></mrow> </math>

<math> <mrow> <mo>&#8658;</mo><mtext>n</mtext><mo>=</mo><mo>&#8722;</mo><mn>28</mn><mo>,</mo><mtext>&#160;</mtext><mn>25</mn></mrow> </math>

<math> <mtext>n</mtext> </math> cannot be negative

Hence <math> <mrow> <mtext>n</mtext><mo>=</mo><mn>25</mn></mrow> </math>

</details>

---

### Q20. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A committee of <math><mn>11</mn></math> member is to be formed from <math><mn>8</mn></math> males and <math><mn>5</mn></math> females. If <math><mi>m</mi></math> is the number of ways the committee is formed with at least <math><mn>6</mn></math> males and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the number of ways the committee is formed with at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> females, then:

**Options:**

- **(A)** <math><mi>m</mi><mo>=</mo><mi>n</mi><mo>=</mo><mn>68</mn></math>
- **(B)** <math><mi> </mi><mi>n</mi><mo>=</mo><mi> </mi><mi>m</mi><mi> </mi><mo>–</mo><mn>8</mn></math>
- **(C)** <math><mi>m</mi><mo>=</mo><mi>n</mi><mo>=</mo><mn>78</mn></math>
- **(D)** <math><mi> </mi><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>68</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>m</mi><mo>=</mo><mi>n</mi><mo>=</mo><mn>78</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mo>(</mo><mn>6</mn><mi>M</mi><mo>,</mo><mo>&#160;</mo><mn>5</mn><mi>F</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>7</mn><mi>M</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><mi>F</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>8</mn><mi>M</mi><mo>,</mo><mo>&#160;</mo><mn>3</mn><mi>F</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><msub><mi>C</mi><mn>6</mn></msub><mprescripts/><mi>&#160;</mi><mn>8</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><msub><mi>C</mi><mn>5</mn></msub><mprescripts/><mi>&#160;</mi><mn>5</mn></mmultiscripts><mo>+</mo><mmultiscripts><msub><mi>C</mi><mn>7</mn></msub><mprescripts/><mi>&#160;</mi><mn>8</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><msub><mi>C</mi><mn>4</mn></msub><mprescripts/><mi>&#160;</mi><mn>5</mn></mmultiscripts><mo>+</mo><mmultiscripts><msub><mi>C</mi><mn>8</mn></msub><mprescripts/><mi>&#160;</mi><mn>8</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><msub><mi>C</mi><mn>3</mn></msub><mprescripts/><mi>&#160;</mi><mn>5</mn></mmultiscripts></math></p><p><math><mo>=</mo><mn>28</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>8</mn><mo>&#215;</mo><mn>5</mn><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>78</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mo>(</mo><mn>3</mn><mi>F</mi><mo>,</mo><mo>&#160;</mo><mn>8</mn><mi>M</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>4</mn><mi>F</mi><mo>,</mo><mo>&#160;</mo><mn>7</mn><mi>M</mi><mo>)</mo><mo>+</mo><mo>(</mo><mn>5</mn><mi>F</mi><mo>,</mo><mo>&#160;</mo><mn>6</mn><mi>M</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><msub><mi>C</mi><mn>3</mn></msub><mprescripts/><mi>&#160;</mi><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><msub><mi>C</mi><mn>8</mn></msub><mprescripts/><mi>&#160;</mi><mn>8</mn></mmultiscripts><mo>+</mo><mmultiscripts><msub><mi>C</mi><mn>4</mn></msub><mprescripts/><mi>&#160;</mi><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><msub><mi>C</mi><mn>7</mn></msub><mprescripts/><mi>&#160;</mi><mn>8</mn></mmultiscripts><mo>+</mo><mmultiscripts><msub><mi>C</mi><mn>5</mn></msub><mprescripts/><mi>&#160;</mi><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><msub><mi>C</mi><mn>6</mn></msub><mprescripts/><mi>&#160;</mi><mn>8</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>5</mn><mo>&#215;</mo><mn>8</mn><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>28</mn><mo>=</mo><mn>78</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mi>n</mi><mo>=</mo><mn>78</mn><mo>.</mo></math></p>

</details>

---

### Q21. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

There are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> men and two women participating in a chess tournament. Each participant plays two games with every other participant. If the number of games played by the men between themselves exceeds the number of games played between the men and the women by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>84</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is :

**Options:**

- **(A)** <math><mn>11</mn></math>
- **(B)** <math><mn>12</mn></math>
- **(C)** <math><mn>7</mn></math>
- **(D)** <math><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>12</mn></math>**

**Detailed Solution:**

<p>Given, number of men is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and number of women is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo></math></p><p>Since each participants competes two games with each other, Hence count of men Vs men total number of game plays <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msup><mi>&#160;</mi><mi>m</mi></msup><msub><mi>C</mi><mn>2</mn></msub></math>.</p><p>count of men Vs women total number of game plays <math><mo>=</mo><mn>4</mn><mi>m</mi></math>.</p><p>As per given condition in question,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>&#160;</mi><mi>m</mi></msup><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mn>84</mn><mo>+</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>-</mo><mn>84</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>+</mo><mn>7</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>-</mo><mn>84</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>m</mi><mo>+</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>.</p><p><math><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>12</mn><mo>,</mo><mi>&#160;</mi><mo>-</mo><mn>7</mn></math></p>

</details>

---

### Q22. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The number of numbers between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>000</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>000</mn></math> that can be formed with the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></math> (repetition of digits is not allowed) and are multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>**

**Detailed Solution:**

<p>When a number is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, then sum of digits of a number is also divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>.</p><p>Number can be formed from <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>)</mo></math>.

Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digits number</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn></math>.</p>

</details>

---

### Q23. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

The number of four letter words that can be formed using the letters of the word BARRACK is

**Options:**

- **(A)** 144
- **(B)** 120
- **(C)** 264
- **(D)** 270

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 270**

**Detailed Solution:**

If all four letters are different then the number of words ${ }^5 \mathrm{C}_4 \times 4 !=120$
If two letters are $\mathrm{R}$ and other two different letters are chosen from $\mathrm{B}, \mathrm{A}, \mathrm{C}, \mathrm{K}$ then the number of words $={ }^4 \mathrm{C}_2 \times \frac{4 !}{2 !}=72$
If two letters are $\mathrm{A}$ and other two different letters are chosen from $\mathrm{B}, \mathrm{R}, \mathrm{C}, \mathrm{K}$ then the number of words $={ }^4 \mathrm{C}_2 \times \frac{4 !}{2 !}=72$
If word is formed using two $R$ 's and two $A$ 's then the number of words $=\frac{4 !}{2 ! 2 !}=6$
Therefore, the number of four-letter words that can be formed $=120+72+72+6=270$

</details>

---

### Q24. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>-digit numbers are formed using only three digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>. The smallest value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>900</mn></math> such distinct numbers can be formed is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>- digit number are formed using only three digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> with repetition <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><mi>n</mi></msup></math>.</p><p>Since, <math><msup><mrow><mn>3</mn></mrow><mrow><mn>6</mn></mrow></msup><mo>&#60;</mo><mn>900</mn></math> and <math><msup><mrow><mn>3</mn></mrow><mrow><mn>7</mn></mrow></msup><mo>&#62;</mo><mn>900</mn></math></p><p>So, <math><mi>n</mi><mo>=</mo><mn>7</mn></math>.</p>

</details>

---

### Q25. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

$n$ - digit numbers are formed using only three digits 2,5 and 7 . The smallest value of $n$ for which 900 such distinct numbers can be formed, is

**Options:**

- **(A)** 6
- **(B)** 8
- **(C)** 9
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7**

**Detailed Solution:**

Required $n$ digit numbers is $3^n$ as each place can be filled by $2,5,7$.
So smallest value of $n$ such that $3^n>900$. Therefore $n=7$.

</details>

---

### Q26. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If all the words, with or without meaning, are written using the letters of the word QUEEN and are arranged as in English dictionary, then the position of the word QUEEN is:

**Options:**

- **(A)** <math><msup><mrow><mn>47</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>
- **(B)** <math><msup><mrow><mn>45</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>
- **(C)** <math><msup><mrow><mn>46</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>
- **(D)** <math><msup><mrow><mn>44</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mn>46</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>**

**Detailed Solution:**

<math><mi>E</mi><mo>,</mo><mi>&#160;</mi><mi>E</mi><mo>,</mo><mi>&#160;</mi><mi>N</mi><mo>,</mo><mi>&#160;</mi><mi>Q</mi><mo>,</mo><mi>&#160;</mi><mi>U</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mo>)</mo></math>  <math><mi>E</mi><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>=&#160;</mo><mo>4!&#160;</mo><mo>=&#160;</mo><mn>24</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math> <math><mi>N</mi><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>=</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>12</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo></math> <math><mi>Q</mi><mi>&#160;</mi><mi>E</mi><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>=</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math> <math><mi>Q</mi><mi>&#160;</mi><mi>N</mi><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>=</mo><mfrac><mrow><mn>3</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>v</mi></mfenced></math> <math><mi>Q</mi><mi>&#160;</mi><mi>U</mi><mi>&#160;</mi><mi>E</mi><mi>&#160;</mi><mi>E</mi><mi>&#160;</mi><mi>N</mi><mo>=</mo><mn>1</mn></math>

Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mi>i</mi><mo>)</mo><mo>+</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo><mo>+</mo><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo><mo>+</mo><mo>(</mo><mi>i</mi><mi>v</mi><mo>)</mo><mo>+</mo><mo>(</mo><mi>v</mi><mo>)</mo><mo>=</mo></math><math><msup><mrow><mn>46</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math>

</details>

---

### Q27. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>x</mi><mn>7</mn></msub></mrow></mfenced><mi>&#160;</mi><mtext>and</mtext><mi>&#160;</mi><mi>B</mi><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo>,</mo><msub><mi>y</mi><mn>3</mn></msub></mrow></mfenced></math> be two sets containing seven and three distinct elements respectively. Then the total number of functions <math><mi>f</mi><mo>:</mo><mi>A</mi><mo>&#8594;</mo><mi>B</mi></math> that are onto, if there exist exactly three elements <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> such that <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msup><mo>&#183;</mo><mn>7</mn></msup><msub><mi>C</mi><mn>2</mn></msub></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><msup><mo>&#183;</mo><mn>7</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>&#183;</mo><msup><mi>&#160;</mi><mn>7</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msup><mo>&#183;</mo><mn>7</mn></msup><msub><mi>C</mi><mn>2</mn></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>&#183;</mo><msup><mi>&#160;</mi><mn>7</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math>**

**Detailed Solution:**

<p><math><mi>A</mi><mo>=</mo><mo>{</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#8230;</mo><mo>.</mo><mo>.</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>7</mn></mrow></msub><mo>}</mo></math> and <math><mi>B</mi><mo>=</mo><mi>&#160;</mi><mo>{</mo><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>}</mo></math>

Let us select <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> elements from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> &amp; connect it to <math><msub><mrow><mi>y</mi></mrow><mrow><mn>2&#160;</mn></mrow></msub></math></p><p>Number of ways <math><mo>=</mo><msup><mrow></mrow><mrow><mn>7</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>&#160;</mi></math>

The number of ways would be equal to <math><msup><mrow></mrow><mrow><mn>7</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>&#160;</mi></math> and now we have 2 elements <math><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><msub><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>&#160;</mi></math> in set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> to be mapped from the remaining element of set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></p><p>Hence, total number of function <math><msup><mrow><mn>2</mn></mrow><mrow><mn>4</mn></mrow></msup><mo>=</mo><mn>16</mn></math> and out of which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> would be &quot;into&quot; functions (when all four goes in <math><msub><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></msub></math> &amp; when all four goes in <math><msub><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>)</mo></math> <math><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>2</mn><mo>=</mo><mn>14</mn></math>

<math><mo>&#8756;</mo></math>So the total number of onto functions would be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msup><mo>&#183;</mo><mn>7</mn></msup><msub><mi>C</mi><mn>3</mn></msub></math>  </p>

</details>

---

### Q28. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The number of points, having both co-ordinates as integers, that lie in the interior of the triangle with vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>41</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>41</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>780</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>901</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>861</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>820</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>780</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/54ac97dd-f54f-4c51-8956-f6cb010dd0bb-image.png" style="width: 258px; height: 225px;" />

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced></math> lies inside the triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>&#8712;</mo><mi>N</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub><mo>&#60;</mo><mn>4</mn><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;&#160;</mo><mn>2</mn><mo>&#8804;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub><mo>&#8804;</mo><mn>4</mn><mn>0</mn></math>

Number of points inside <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Number of solutions of the equation

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mi>n</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#8804;</mo><mi>n</mi><mo>&#8804;</mo><mn>4</mn><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>&#8805;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>&#8805;</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>

(Number of non - negative integral solutions of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>....</mo><mo>+</mo><msub><mi>x</mi><mi>n</mi></msub><mo>=</mo><mi>r</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mspace/><mrow><mi>n</mi><mo>+</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mi>r</mi></msub></math>)

Number of solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow><none/><mprescripts/><none/><mrow><mn>2</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>1</mn></mrow></mmultiscripts></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mspace/><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><msub><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msub></math>

 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mo>-</mo><mn>1</mn></math>

We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#8804;</mo><mi>n</mi><mo>&#8804;</mo><mn>4</mn><mn>0</mn></math>

<math> <mrow> <mo>&#8756;</mo> </mrow> </math>  Number of solutions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>39</mn></math></p><p> <math> <mrow> <mo>=</mo> <mfrac> <mrow> <mn>3</mn> <mn>9</mn> <mo>&#215;</mo> <mn>4</mn> <mn>0</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

 <math> <mrow> <mo>=</mo> <mn>7</mn> <mn>8</mn> <mn>0</mn> </mrow> </math></p>

</details>

---

### Q29. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The number of integers greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6000</mn></math> that can be formed, using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>, without repetition is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>216</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>192</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>192</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers are possible.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit numbers:

<math> <mrow> <mtable> <mtr> <mtd> <mn>6</mn> <mo>/</mo> <mn>7</mn> <mo>/</mo> <mn>8</mn> </mtd> <mtd> </mtd> <mtd> </mtd> <mtd> </mtd> </mtr> <mtr> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> </mtr> <mtr> <mtd> <mn>3</mn> </mtd> <mtd> <mn>4</mn> </mtd> <mtd> <mn>3</mn> </mtd> <mtd> <mn>2</mn> </mtd> </mtr> </mtable> <mo>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Total numbers possible</mo> <mo>=</mo> <mtext>3 . 4 . 3 . 2</mtext> <mo>=</mo> <mtext>72</mtext> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers

<math> <mrow> <mtable> <mtr> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> <mtd> <mover accent="true"> <mo>&#8593;</mo> <mo>&#175;</mo> </mover> </mtd> </mtr> <mtr> <mtd> <mn>5</mn> </mtd> <mtd> <mn>4</mn> </mtd> <mtd> <mn>3</mn> </mtd> <mtd> <mn>2</mn> </mtd> <mtd> <mn>1</mn> </mtd> </mtr> </mtable> <mo>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Total numbers possible</mo> <mo>=</mo> <mtext>5 . 4 . 3 . 2 . 1</mtext> <mo>=</mo> <mtext>120</mtext> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mtext>Total numbers</mtext><mo>=</mo><mo>72</mo><mo>+</mo><mn>120</mn><mo>=</mo><mn>192</mn></math></p>

</details>

---

### Q30. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Two women and some men participated in a chess tournament in which every participant played two games with each of the other participants. If the number of games that the men played between them-selves exceeds the number of games that the men played with the women by<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>66</mn></math>, then the number of men who participated in the tournament lies in the interval

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>11</mn><mo>,</mo><mn>13</mn><mo>]</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>14</mn><mo>,</mo><mn>17</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>10</mn><mo>,</mo><mn>12</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>10</mn><mo>,</mo><mn>12</mn><mo>)</mo></math>**

**Detailed Solution:**

<p>Let the number of men participating in tournament <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>m</mi></math>.</p><p>Number of women participating in tournament <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math>.</p><p>Each player will play<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>2</mn></math> games with every other player and two women will play <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> games with each man.</p><p>Total numbers of games played by women <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mi>m</mi><mo>=</mo><mn>4</mn><mi>m</mi></math></p><p>Total number of games played by men <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msup><mo>&#183;</mo><mi>m</mi></msup><msub><mi>C</mi><mn>2</mn></msub></math></p><p>From given data</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mo>&#183;</mo><mrow><mo>&#160;</mo><mi>m</mi></mrow></msup><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><mn>4</mn><mi>m</mi><mo>=</mo><mn>66</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfrac><mrow><mi>m</mi><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>-</mo><mn>4</mn><mi>m</mi><mo>=</mo><mn>66</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>m</mi><mo>-</mo><mn>66</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>11</mn></mrow></mfenced><mfenced><mrow><mi>m</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>11</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo><mi>&#160;</mi><mi>m</mi><mo>&#8800;</mo><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>&#8712;</mo><mfenced open="[" separators="|"><mrow><mn>10</mn><mo>,</mo><mn>12</mn></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q31. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

8-digit numbers are formed using the digits 1, 1, 2, $2,2,3,4,4$. The number of such numbers in which the odd digits do no occupy odd places, is:

**Options:**

- **(A)** 160
- **(B)** 120
- **(C)** 60
- **(D)** 48

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 120**

**Detailed Solution:**

In 8 digits numbers, 4 places are odd places.
Also, in the given 8 digits, there are three odd digits 1,1 and 3.
No. of ways three odd digits arranged at
$$
\text { four even places }=\frac{4 P_3}{2 !}=\frac{4 !}{2 !}
$$
No. of ways the remaining five digits 2 , 2, 2, 4 and 4 arranged at remaining five places $=\frac{5 !}{3 ! 2 !}$
Hence, required number of 8 digits number $=\frac{4 !}{2 !} \times \frac{5 !}{3 ! 2 !}=120$

</details>

---

### Q32. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

An eight digit number divisible by 9 is to be formed using digits from 0 to 9 without repeating the digits. The number of ways in which this can be done is:

**Options:**

- **(A)** $72(7 !)$
- **(B)** $18(7 !)$
- **(C)** $40(7 !)$
- **(D)** $36(7 !)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $36(7 !)$**

**Detailed Solution:**

We know that any number is divisible by 9 if sum of the digits of the number is divisible by 9 .
Now sum of the digits from 0 to 9
$$
\begin{aligned}
&=0+1+2+3+4+5+6+7+8+9 \\
&=45
\end{aligned}
$$
Hence to form 8 digits numbers which are divisible by 9 , a pair of digits either 0 and 9,1 and 8,2 and 7,3 and 6 or 4 and 5 are not used.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/RQ5DcHkNatphZ81WIi_aFIr0giVET3LGNdNmKwpMRas.original.fullsize.png">

Hence total number of 8 digits numbers which are divisible by 9
$$
\begin{aligned}
&=8 \times(7 !)+7 \times(7 !)+7 \times(7 !)+7 \times(7 !) \\
&+7 \times(7 !) \\
&=36 \times(7 !)
\end{aligned}
$$

</details>

---

### Q33. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the digits in the unit&#39;s place of all the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> - digit numbers formed by using the numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></math> and<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>6</mn></math>, without repetition is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>432</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a05589b9-b41b-4dfa-af90-86292e7b77ac-image.png" style="width: 364px; height: 132px;" /></p><p> By fixing one digit at unit place we can form toal number without repetition is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>!</mo></math>    </p><p>Sum of digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>3</mn><mo>!</mo><mo>&#160;</mo><mo>.</mo><mo>&#160;</mo><mfenced><mrow><mn>6</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>5</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>4</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mn>6</mn></mfenced><mfenced><mn>18</mn></mfenced><mo>=</mo><mn>108</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><mi>n</mi><mo>!</mo><mo>=</mo><mi>n</mi><mo>.</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mn>3</mn><mo>.</mo><mn>2</mn><mo>.</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q34. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

5 - digit numbers are to be formed using $2,3,5,7$, 9 without repeating the digits. If $p$ be the number of such numbers that exceed 20000 and $q$ be the number of those that lie between 30000 and 90000 , then $p: q$ is:

**Options:**

- **(A)** $6: 5$
- **(B)** $3: 2$
- **(C)** $4: 3$
- **(D)** $5: 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5: 3$**

**Detailed Solution:**

$\mathrm{p}: \begin{array}{llllll}0 & 0 & 0 & 0 & 0 & \text { place } \\ 5 & 4 & 3 & 2 & 1 & \text { ways }\end{array}$
Total no, of ways $=5 !=120$
Since all numbers are $>20,000$
$\therefore$ all numbers $2,3,5,7,9$ can come at first place.
$\mathrm{q}: \begin{array}{llllll}0 & 0 & 0 & 0 & 0 & \text { place } \\ 3 & 4 & 3 & 2 & 1 & \text { ways }\end{array}$
Total no. of ways $=3 \times 4 !=72$
( $\because 2$ and 9 can not be put at first place)
So, $p: q=120: 72=5: 3$

</details>

---

### Q35. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `3`

The number of arrangements that can be formed from the letters $a, b, c, d, e, f$ taken 3 at a time without repetition and each arrangement containing at least one vowel, is

**Options:**

- **(A)** 96
- **(B)** 128
- **(C)** 24
- **(D)** 72

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 96**

**Detailed Solution:**

There are 2 vowels and 4 consonants in the letters $a, b, c, d, e, f$.
If we select one vowel, then number of arrangements
$$
={ }^2 C_1 \times{ }^4 C_2 \times 3 !=2 \times \frac{4 \times 3}{2} \times 3 \times 2=72
$$
If we select two vowels, then number of arrangements
$$
={ }^2 C_2 \times{ }^4 C_1 \times 3 !=1 \times 4 \times 6=24
$$
Hence, total number of arrangements
$$
=72+24=96
$$

</details>

---

### Q36. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If the number of 5-element subsets of the set $A=\left\{a_1, a_2, \ldots, a_{20}\right\}$ of 20 distinct elements is $k$ times the number of 5-element subsets containing $a_4$, then $k$ is

**Options:**

- **(A)** 5
- **(B)** $\frac{20}{7}$
- **(C)** 4
- **(D)** $\frac{10}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

Set $A=\left\{a_1, a_2, \ldots . ., a_{20}\right\}$ has 20 distinct elements.
We have to select 5-element subset.
$\therefore$ Number of 5-element subsets $={ }^{20} \mathrm{C}_5$
According to question
$$
\begin{aligned}
& { }^{20} \mathrm{C}_5=\left({ }^{19} \mathrm{C}_4 \cdot k\right. \\
& \Rightarrow \frac{20 !}{5 ! 15 !}=k \cdot\left(\frac{19 !}{4 ! 15 !}\right) \\
& \Rightarrow \quad \frac{20}{5}=k \Rightarrow k=4
\end{aligned}
$$

</details>

---

### Q37. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

Let $X=\{1,2,3,4,5\}$. The number of different ordered pairs $(Y, Z)$ that can be formed such that $Y \subseteq X, Z$ $\subseteq \mathrm{X}$ and $\mathrm{Y} \cap \mathrm{Z}$ is empty, is

**Options:**

- **(A)** $5^2$
- **(B)** $3^5$
- **(C)** $2^5$
- **(D)** $5^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3^5$**

**Detailed Solution:**

$\mathrm{Y} \subseteq \mathrm{X}, \mathrm{Z} \subseteq \mathrm{X}$
Let $a \in X$, then we have following chances that
(1) $a \in Y, \quad a \in Z$
(2) $a \notin Y, \quad a \in Z$
(3) $a \in Y, \quad a \notin Z$
(4) $a \notin Y, \quad a \notin Z$
We require $Y \cap Z=\phi$
Hence (2), (3), (4) are chances for '$a$' to satisfy $Y \cap Z=\phi$.
$\therefore Y \cap Z=\phi$ has $3$ chances for $a$.
Hence for five elements of $\mathrm{X}$, the number of required chances is $3 \times 3 \times 3 \times 3 \times 3=3^5$

</details>

---

### Q38. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

There are two urns. Urn A has 3 distinct red balls and urn B has 9 distinct blue balls. From each urn two balls are taken out at random and then transferred to the other. The number of ways in which this can be done is

**Options:**

- **(A)** 36
- **(B)** 66
- **(C)** 108
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 108**

**Detailed Solution:**

Total number of ways $={ }^3 \mathrm{C}_2 \times{ }^9 \mathrm{C}_2$
$$
=3 \times \frac{9 \times 8}{2}=3 \times 36=108
$$

</details>

---

### Q39. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If the letters of word SACHIN are arranged in all possible ways and these words are written out as in dictionary, then the word SACHIN appears at serial number

**Options:**

- **(A)** 601
- **(B)** 600
- **(C)** 603
- **(D)** 602

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 601**

**Detailed Solution:**

Alphabetical order is
A, C, H, I, N, S
No. of words starting with $A-5$ !
No. of words starting with $C-5$ !
No. of words starting with $\mathrm{H}-5$ !
No. of words starting with I $-5$ !
No. of words starting with $N-5$ !
$\mathrm{SACHIN}-1$
$601$

</details>

---

### Q40. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The number of ways in which 6 men and 5 women can dine at a found table if no two women are to sit together is given by

**Options:**

- **(A)** $7 \times 5$
- **(B)** $6 \times 5$
- **(C)** 30
- **(D)** $5 \times 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $7 \times 5$**

**Detailed Solution:**

No.of ways in which $6 \mathrm{~mm}$ can be arranged at a round table $=(6-1)$ ! Now women can be arranged in 6 ! ways.
Total number of ways $=6 ! \times 5$ !

</details>

---

### Q41. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

Number greater than 1000 but less than 4000 is formed using the digits 0, 1, 2, 3, 4 (repetition allowed) is

**Options:**

- **(A)** 125
- **(B)** 105
- **(C)** 375
- **(D)** 625

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 375**

**Detailed Solution:**

Required number of numbers $=3 \times 5 \times 5 \times 5=375$

</details>

---

### Q42. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

Total number of four digit odd numbers that can be formed using 0, 1, 2, 3, 5, 7 (using repetition allowed) are

**Options:**

- **(A)** 216
- **(B)** 375
- **(C)** 400
- **(D)** 720

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 720**

**Detailed Solution:**

Required number of numbers $=5 \times 6 \times 6 \times 4=36 \times 20=720$

</details>

---

