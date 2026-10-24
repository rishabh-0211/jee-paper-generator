# MHT CET Mathematics - Permutation Combination

## Topic 3: Combination

**Total Questions:** 17

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Everyone in the room handshakes with everyone else. If the total number of handshakes is 66, then the number of persons in the room is...

**Options:**

- **(A)** $10$
- **(B)** $6$
- **(C)** $11$
- **(D)** $12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12$**

**Detailed Solution:**

Let the number of persons in the room be $n$.

Since everyone handshakes with everyone else exactly once, the total number of handshakes is given by $^{n}C_{2}$.

Given that the total number of handshakes is $66$, we have:

$^{n}C_{2} = 66$

$\dfrac{n(n-1)}{2} = 66$

$n(n-1) = 132$

$n^2 - n - 132 = 0$

$(n - 12)(n + 11) = 0$

Since the number of persons must be a positive integer, $n = 12$.

Answer: $12$

</details>

---

### Q2. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A man has seven relatives, 4 of them are ladies and 3 gentlemen, his wife also has 7 relatives out of which 3 are ladies and 4 gentlemen. The number of ways in which they can invite a dinner party of 3 ladies and 3 gentlemen, so that there are 3 of the man's relatives and 3 of the wife's relatives, are

**Options:**

- **(A)** $144$
- **(B)** $485$
- **(C)** $336$
- **(D)** $535$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $485$**

**Detailed Solution:**

Let $x$ be the number of ladies invited from the man's relatives.

Since exactly $3$ relatives are to be invited from the man's side, the number of gentlemen invited from his side will be $3 - x$.

The total number of ladies to be invited is $3$. Therefore, the number of ladies invited from the wife's relatives must be $3 - x$.

Since exactly $3$ relatives are to be invited from the wife's side, the number of gentlemen invited from her side will be $3 - (3 - x) = x$.

The possible values for $x$ are $0, 1, 2, 3$. We calculate the number of ways for each case:

Case 1: $x = 0$
Man's side ($0$ ladies, $3$ gentlemen): $^{4}C_{0} \times ^{3}C_{3} = 1 \times 1 = 1$
Wife's side ($3$ ladies, $0$ gentlemen): $^{3}C_{3} \times ^{4}C_{0} = 1 \times 1 = 1$
Number of ways = $1 \times 1 = 1$

Case 2: $x = 1$
Man's side ($1$ lady, $2$ gentlemen): $^{4}C_{1} \times ^{3}C_{2} = 4 \times 3 = 12$
Wife's side ($2$ ladies, $1$ gentleman): $^{3}C_{2} \times ^{4}C_{1} = 3 \times 4 = 12$
Number of ways = $12 \times 12 = 144$

Case 3: $x = 2$
Man's side ($2$ ladies, $1$ gentleman): $^{4}C_{2} \times ^{3}C_{1} = 6 \times 3 = 18$
Wife's side ($1$ lady, $2$ gentlemen): $^{3}C_{1} \times ^{4}C_{2} = 3 \times 6 = 18$
Number of ways = $18 \times 18 = 324$

Case 4: $x = 3$
Man's side ($3$ ladies, $0$ gentlemen): $^{4}C_{3} \times ^{3}C_{0} = 4 \times 1 = 4$
Wife's side ($0$ ladies, $3$ gentlemen): $^{3}C_{0} \times ^{4}C_{3} = 1 \times 4 = 4$
Number of ways = $4 \times 4 = 16$

Total number of ways = $1 + 144 + 324 + 16 = 485$

Answer: $485$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a polygon, the number of diagonals is $54$. Then the number of sides of the polygon is

**Options:**

- **(A)** $10$
- **(B)** $11$
- **(C)** $12$
- **(D)** $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $12$**

**Detailed Solution:**

Let the number of sides of the polygon be $n$.

The number of diagonals of an $n$-sided polygon is given by $^{n}C_{2} - n = \dfrac{n(n-3)}{2}$.

Given that the number of diagonals is $54$, we have:

$\dfrac{n(n-3)}{2} = 54$

$n^2 - 3n = 108$

$n^2 - 3n - 108 = 0$

$(n - 12)(n + 9) = 0$

Since the number of sides must be a positive integer, $n = 12$.

Answer: $12$

</details>

---

### Q4. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of ways in which a team of 11 players can be formed out of 25 players, if 6 out of them are always to be included and 5 of them are always to be excluded, is

**Options:**

- **(A)** 2002
- **(B)** $^{20}C_{11}$
- **(C)** $^{20}C_{6}$
- **(D)** $^{14}C_{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2002**

**Detailed Solution:**

Total number of players = $25$

Number of players to be selected = $11$

Number of players always included = $6$

Number of players always excluded = $5$

Number of remaining players available for selection = $25 - 6 - 5 = 14$

Number of players to be selected from the remaining players = $11 - 6 = 5$

The required number of ways is given by $^{14}C_{5}$.

$^{14}C_{5} = \dfrac{14!}{5!(14-5)!} = \dfrac{14 \times 13 \times 12 \times 11 \times 10}{5 \times 4 \times 3 \times 2 \times 1} = 2002$

Answer: 2002

</details>

---

### Q5. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

There are 11 points in a plane of which 5 points are collinear. Then the total number of distinct quadrilaterals with vertices at these points is

**Options:**

- **(A)** 265
- **(B)** 330
- **(C)** 250
- **(D)** 325

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 265**

**Detailed Solution:**

To form a quadrilateral, we need to select 4 points out of the given 11 points.

Total number of ways to select 4 points from 11 points is $^{11}C_{4}$.

$^{11}C_{4} = \dfrac{11 \times 10 \times 9 \times 8}{4 \times 3 \times 2 \times 1} = 330$

However, a quadrilateral cannot be formed if 3 or 4 of the selected points are collinear. We are given that 5 points are collinear.

Number of selections where all 4 points are collinear is $^{5}C_{4} = 5$.

Number of selections where exactly 3 points are collinear (chosen from the 5 collinear points) and 1 point is non-collinear (chosen from the remaining 6 points) is $^{5}C_{3} \times ^{6}C_{1}$.

$^{5}C_{3} \times ^{6}C_{1} = 10 \times 6 = 60$

Therefore, the total number of distinct quadrilaterals that can be formed is the total selections minus the invalid selections:

Total quadrilaterals = $330 - 5 - 60 = 265$

Answer: 265

</details>

---

### Q6. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If ${ }^{n+4} C_{n+1}-{ }^{n+3} C_n=15(n+2)$, then $n=$

**Options:**

- **(A)** $15$
- **(B)** $23$
- **(C)** $21$
- **(D)** $27$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $27$**

**Detailed Solution:**

Using the property $^{n}C_{r} = ^{n}C_{n-r}$, we get:

$^{n+4}C_{n+1} = ^{n+4}C_{3}$

$^{n+3}C_{n} = ^{n+3}C_{3}$

The given equation becomes:

$^{n+4}C_{3} - ^{n+3}C_{3} = 15(n+2)$

Using the identity $^{n+1}C_{r} - ^{n}C_{r} = ^{n}C_{r-1}$, we have $^{n+4}C_{3} - ^{n+3}C_{3} = ^{n+3}C_{2}$.

Substituting this in the equation, we get:

$^{n+3}C_{2} = 15(n+2)$

$\dfrac{(n+3)(n+2)}{2} = 15(n+2)$

Since $n \ge 0$, $n+2 \neq 0$, we can cancel $(n+2)$ from both sides:

$\dfrac{n+3}{2} = 15$

$n+3 = 30$

$n = 27$

Answer: $27$

</details>

---

### Q7. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

4 red balls and 5 green balls are selected from n balls. If the sum of both the selections is greater then ${ }^{n+1} C_4$ then the value of $n$ is equal to

**Options:**

- **(A)** $n>8$
- **(B)** $\mathrm{n} < 8$
- **(C)** $n>10$
- **(D)** $n>12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $n>8$**

**Detailed Solution:**

The number of ways to select 4 red balls from $n$ red balls is $^{n}C_{4}$.

The number of ways to select 5 green balls from $n$ green balls is $^{n}C_{5}$.

According to the given condition, the sum of both selections is greater than $^{n+1}C_{4}$.

$^{n}C_{4} + ^{n}C_{5} > ^{n+1}C_{4}$

Using the standard identity $^{n}C_{r} + ^{n}C_{r-1} = ^{n+1}C_{r}$, we get:

$^{n+1}C_{5} > ^{n+1}C_{4}$

Expanding the combinations:

$\dfrac{(n+1)!}{5!(n-4)!} > \dfrac{(n+1)!}{4!(n-3)!}$

$\dfrac{1}{5} > \dfrac{1}{n-3}$

Since $n \ge 5$, $n-3$ is strictly positive. Cross-multiplying gives:

$n - 3 > 5$

$n > 8$

Answer: $n>8$

</details>

---

### Q8. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A regular polygon has 20 sides. The number of triangles that can be drawn by using the vertices but not using the sides are

**Options:**

- **(A)** $1140$
- **(B)** $800$
- **(C)** $340$
- **(D)** $20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $800$**

**Detailed Solution:**

Total number of vertices of the polygon is $n = 20$.

Total number of triangles that can be formed using the vertices is $^{20}C_{3} = \dfrac{20 \times 19 \times 18}{3 \times 2 \times 1} = 1140$.

Number of triangles having exactly two sides common with the polygon is $n = 20$.

Number of triangles having exactly one side common with the polygon is $n(n - 4) = 20 \times 16 = 320$.

Number of triangles having no side common with the polygon is the total number of triangles minus the triangles having one or two sides common.

Required number of triangles $= 1140 - (20 + 320) = 1140 - 340 = 800$.

Answer: $800$

</details>

---

### Q9. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If in a regular polygon, the number of diagonals are 54 , then the number of sides of the polygon are

**Options:**

- **(A)** 10
- **(B)** 12
- **(C)** 9
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 12**

**Detailed Solution:**

Number of diagonals in a polygon of $\mathrm{n}$ sides is ${ }^{\mathrm{n}} \mathrm{C}_2-\mathrm{n}$.
$\begin{aligned}
\therefore \quad & { }^{\mathrm{n}} \mathrm{C}_2-\mathrm{n}=54 \\
& \Rightarrow \frac{\mathrm{n}(\mathrm{n}-1)}{2}-\mathrm{n}=54 \\
& \Rightarrow \mathrm{n}^2-3 \mathrm{n}-108=0 \\
& \Rightarrow(\mathrm{n}-12)(\mathrm{n}+9)=0
\end{aligned}$
But, number of sides cannot be negative.
$\therefore \quad \mathrm{n}=12$

</details>

---

### Q10. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn successively with replacement from a well-shuffled pack of 52 cards. Then mean of number of tens is

**Options:**

- **(A)** $\frac{1}{13}$
- **(B)** $\frac{1}{169}$
- **(C)** $\frac{2}{13}$
- **(D)** $\frac{4}{169}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{13}$**

**Detailed Solution:**

Probability of getting ten $=\frac{4}{52}=\frac{1}{13}$
$\therefore \quad$ Probability of getting a card without ten $=\frac{12}{13}$
Let random variable $\mathrm{X}$ denotes the number of tens.
$\therefore \quad$ Possible values of $\mathrm{X}$ are $0,1,2$
Consider following probability distribution table.
\begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{12}{13} \times \frac{12}{13} & \frac{1}{13} \times \frac{12}{13}+\frac{12}{13} \times \frac{1}{13} & \frac{1}{13} \times \frac{1}{13} \\
\hline
\end{array}
$\therefore \quad$ Required mean
$\begin{aligned}
& =0+1 \times\left(\frac{12}{13 \times 13}+\frac{12}{13 \times 13}\right)+2 \times\left(\frac{1}{13} \times \frac{1}{13}\right) \\
& =\frac{24}{169}+\frac{2}{169} \\
& =\frac{26}{169} \\
& =\frac{2}{13}
\end{aligned}$

</details>

---

### Q11. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If at the end of certain meeting, everyone had shaken hands with everyone else, it was found that 45 handshakes were exchanged, then the number of members present at the meeting, are

**Options:**

- **(A)** 10
- **(B)** 15
- **(C)** 20
- **(D)** 21

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 10**

**Detailed Solution:**

Let ' $n$ ' be the number of members in the meeting
$\therefore \quad$ Total number of handshakes $={ }^{\mathrm{n}} \mathrm{C}_2$
$\therefore \quad{ }^{\mathrm{n}} \mathrm{C}_2=45$
$\begin{array}{ll} & \frac{\mathrm{n} !}{2 !(\mathrm{n}-2) !}=45 \\ & \frac{\mathrm{n}(\mathrm{n}-1)(\mathrm{n}-2) !}{2 \times(\mathrm{n}-2) !}=45 \\ & \mathrm{n}(\mathrm{n}-1)=90 \\ \therefore \quad & \mathrm{n}^2-\mathrm{n}-90=0 \\ & \mathrm{n}=10 \text { or } \mathrm{n}=-9 \text { (not possible) } \\ \therefore \quad & \mathrm{n}=10\end{array}$

</details>

---

### Q12. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A man $P$ has 7 friends, 4 of them are ladies and 3 are men, His wife $Q$ also has 7 friends, 3 of them are ladies and 4 are men. Assume $P$ and $Q$ have no common friends. Then the total number of ways in which $P$ and $Q$ together can throw a party inviting 3 ladies and 3 men, so that 3 friends of each of $P$ and $Q$ are in this party, is<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/5pI3oQYPvcNYetdxuaI2la6-epe66O1ZiwEqi-5Tf2M.original.fullsize.png">

**Options:**

- **(A)** 468
- **(B)** 485
- **(C)** 484
- **(D)** 469

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 485**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/-cq78DCa53_oBtkubCAWZD-qig9A-_520LDD3Ig-HRo.original.fullsize.png">

</details>

---

### Q13. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a question paper consists of 11 questions divided into two section I and II. Section I consist of 6 questions and section II consists of 5 question, then the number of different ways can student select 6 questions, taking at least 2 questions from each section, is

**Options:**

- **(A)** 350
- **(B)** 225
- **(C)** 275
- **(D)** 425

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 425**

**Detailed Solution:**

$\begin{array}{ccl}\text { Section-I } & \text { Section-II } & \text { No. of ways } \\ 2 & 4 & { }^6 C_2 \times{ }^5 C_4=15 \times 5=75 \\ 3 & 3 & { }^6 C_3 \times{ }^5 C_3=20 \times 10=200 \\ 4 & 2 & { }^6 C_4 \times{ }^5 C_2=15 \times 10=150 \\ & & \\ & & \text { Total }=425\end{array}$

</details>

---

### Q14. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Out of 7 consonants and 4 vowels, the number of words consisting of 3 consonants and 2 vowels are

**Options:**

- **(A)** 3300
- **(B)** 210
- **(C)** 120
- **(D)** 25200

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 25200**

**Detailed Solution:**

We have to choose 3 consonants and 2 vowels from 7 consonants and 4 vowels.
$\therefore$ Number of words $=\left({ }^7 \mathrm{C}_3\right) \times\left({ }^4 \mathrm{C}_2\right) \times 5$ !
$=\frac{7 !}{3 ! 4 !} \times \frac{4 !}{2 ! 2 !} \times 5 !=25200$

</details>

---

### Q15. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A polygon has 44 diagonals. Then the number of sides of the polygon are

**Options:**

- **(A)** 11
- **(B)** 12
- **(C)** 10
- **(D)** 13

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 11**

**Detailed Solution:**

Number of diagonals of ' $n$ ' sided polygons $={ }^n C_2-n$
$$
\begin{aligned}
& \therefore{ }^n C_2-n=44 \\
& \frac{n !}{2 !(n-2) !}-n=44 \Rightarrow n(n-1)-2 n=88 \\
& \therefore n^2-3 n-88=0 \Rightarrow(n-11)(n+8)=0 \\
& \Rightarrow n=11 \ldots[n \in N]
\end{aligned}
$$

</details>

---

### Q16. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For a set of five true or false questions, no student has written the all correct answers and no two students have given the same sequence of answers. The maximum number of students in the class for this to be possible is

**Options:**

- **(A)** 30
- **(B)** 31
- **(C)** 32
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 31**

**Detailed Solution:**

Each of the five questions can be solved in two ways.
$\therefore$ Maximum number of wrong answers.
$$
=(2 \times 2 \times 2 \times 2 \times 2)-1=31
$$

</details>

---

### Q17. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

Three numbers are selected randomly between 1 to 20 . Then, the probability that they are consecutive numbers will be

**Options:**

- **(A)** $\frac{7}{190}$
- **(B)** $\frac{3}{190}$
- **(C)** $\frac{5}{190}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{190}$**

**Detailed Solution:**

Number of sample space for selecting three numbers between 1 to $20={ }^{20} C_{3}$
Number of ways that they are consecutive numbers $=18$.
$\therefore$ Required probability
$$
\begin{array}{l}
=\frac{18}{20} C_{3}=\frac{18 \times 3 \times 2}{20 \times 19 \times 18} \\
=\frac{3}{190}
\end{array}
$$

</details>

---

