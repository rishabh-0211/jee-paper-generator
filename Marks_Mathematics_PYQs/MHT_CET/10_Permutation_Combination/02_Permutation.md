# MHT CET Mathematics - Permutation Combination

## Topic 2: Permutation

**Total Questions:** 24

---

### Q1. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If all permutations of the letters of the word THREE are arranged as in dictionary, then $47^{th}$ word is...

**Options:**

- **(A)** $RTEHE$
- **(B)** $RTHEE$
- **(C)** $TEEHR$
- **(D)** $TEERH$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $RTEHE$**

**Detailed Solution:**

The letters of the word THREE in alphabetical order are E, E, H, R, T.

Number of words starting with E = $4! = 24$

Number of words starting with H = $\dfrac{4!}{2!} = 12$

Total words so far = $24 + 12 = 36$

Number of words starting with RE = $3! = 6$

Total words so far = $36 + 6 = 42$

Number of words starting with RH = $\dfrac{3!}{2!} = 3$

Total words so far = $42 + 3 = 45$

The next words will start with RT. The remaining letters are E, E, H.

The $46^{th}$ word is RTEEH.

The $47^{th}$ word is RTEHE.

The $48^{th}$ word is RTHEE.

Thus, the $47^{th}$ word is RTEHE.

Answer: $RTEHE$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

How many numbers (without repetition) between $400$ and $1000$ can be made with the digits $2, 3, 4, 5, 6,$ and $0$?

**Options:**

- **(A)** $120$
- **(B)** $720$
- **(C)** $60$
- **(D)** $24$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $60$**

**Detailed Solution:**

The numbers between $400$ and $1000$ must be $3$-digit numbers.

To ensure the number is greater than $400$, the hundreds place can only be filled by $4, 5,$ or $6$.
Number of ways to fill the hundreds place = $3$

Since repetition of digits is not allowed, the tens place can be filled by any of the remaining $5$ digits.
Number of ways to fill the tens place = $5$

Similarly, the units place can be filled by any of the remaining $4$ digits.
Number of ways to fill the units place = $4$

Total number of such numbers = $3 \times 5 \times 4 = 60$

Answer: $60$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Four Rupee 5 coins, three rupee 2 coins and two rupee 1 coin are stacked together in a column at random. The probability that the coins of the same denomination are consecutive, is

**Options:**

- **(A)** $\dfrac{13}{9!}$
- **(B)** $\dfrac{1}{210}$
- **(C)** $\dfrac{1}{35}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{210}$**

**Detailed Solution:**

Total number of coins is $4 + 3 + 2 = 9$.

Considering all coins to be distinct, the total number of ways to arrange them in a column is $9!$.

To find the number of ways where coins of the same denomination are consecutive, we treat the coins of each denomination as a single group. There are $3$ such groups (Rupee $5$, Rupee $2$, and Rupee $1$).

These $3$ groups can be arranged among themselves in $3!$ ways.

Within their respective groups, the $4$ Rupee $5$ coins can be arranged in $4!$ ways, the $3$ Rupee $2$ coins in $3!$ ways, and the $2$ Rupee $1$ coins in $2!$ ways.

Total number of favorable arrangements is $3! \times 4! \times 3! \times 2!$.

The required probability is $\dfrac{3! \times 4! \times 3! \times 2!}{9!}$.

$\Rightarrow \dfrac{6 \times 4! \times 6 \times 2}{9 \times 8 \times 7 \times 6 \times 5 \times 4!} = \dfrac{72}{9 \times 8 \times 7 \times 6 \times 5} = \dfrac{72}{15120} = \dfrac{1}{210}$.

Answer: $\dfrac{1}{210}$

</details>

---

### Q4. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

How many different five digit numbers which are divisible by $4$ can be formed using the digits in the number $22457$ ?

**Options:**

- **(A)** $60$
- **(B)** $12$
- **(C)** $54$
- **(D)** $18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $18$**

**Detailed Solution:**

A number is divisible by $4$ if the number formed by its last two digits is divisible by $4$.

The given digits are $2, 2, 4, 5, 7$.

The possible two-digit numbers that can be formed using these digits and are divisible by $4$ are $24, 52$, and $72$.

Case 1: The last two digits are $24$.
The remaining digits to be placed in the first three positions are $2, 5, 7$.
Since all three digits are distinct, the number of ways to arrange them is $3! = 6$.

Case 2: The last two digits are $52$.
The remaining digits to be placed in the first three positions are $2, 4, 7$.
Since all three digits are distinct, the number of ways to arrange them is $3! = 6$.

Case 3: The last two digits are $72$.
The remaining digits to be placed in the first three positions are $2, 4, 5$.
Since all three digits are distinct, the number of ways to arrange them is $3! = 6$.

Total number of such five-digit numbers $= 6 + 6 + 6 = 18$.

Answer: $18$

</details>

---

### Q5. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of permutations of the letters of the word INSTITUTION are .......

**Options:**

- **(A)** $6652800$
- **(B)** $221760$
- **(C)** $1108800$
- **(D)** $554400$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $554400$**

**Detailed Solution:**

The word INSTITUTION has $11$ letters.

The frequencies of the letters are:
I appears $3$ times.
N appears $2$ times.
T appears $3$ times.
S, U, O appear $1$ time each.

The total number of permutations is given by $\dfrac{11!}{3! \times 2! \times 3!}$.

$\dfrac{11!}{3! \times 2! \times 3!} = \dfrac{39916800}{6 \times 2 \times 6} = \dfrac{39916800}{72} = 554400$

Answer: $554400$

</details>

---

### Q6. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a test, there are 7 questions of the type 'True or False'. No student got all the answers correct. If the sequence of answers for every student is unique, then the maximum number of students who appeared for the test is $\ldots$

**Options:**

- **(A)** $128$
- **(B)** $126$
- **(C)** $127$
- **(D)** $125$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $127$**

**Detailed Solution:**

Total number of questions = $7$

Each question can be answered in $2$ ways (True or False).

Total number of possible answer sequences = $2^7 = 128$

Since no student got all the answers correct, the sequence corresponding to all correct answers is excluded.

Number of available sequences = $128 - 1 = 127$

Since every student's sequence of answers is unique, the maximum number of students is equal to the number of available sequences.

Maximum number of students = $127$

Answer: $127$

</details>

---

### Q7. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a test, there are 5 questions of the 'true or false' type. No student has got all the answers correct and the sequence of answers for every student is unique. The maximum number of students who could have appeared for the test is....

**Options:**

- **(A)** $5$
- **(B)** $31$
- **(C)** $15$
- **(D)** $89$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $31$**

**Detailed Solution:**

The test has $5$ questions, and each question has $2$ possible answers (True or False).

The total number of possible sequences of answers is $2^5 = 32$.

Out of these $32$ sequences, exactly $1$ sequence corresponds to all answers being correct.

Since no student has got all the answers correct, this specific sequence cannot be chosen by any student.

The number of available sequences of answers is $32 - 1 = 31$.

Since the sequence of answers for every student is unique, the maximum number of students who could have appeared for the test is equal to the maximum number of available unique sequences, which is $31$.

Answer: $31$

</details>

---

### Q8. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of 4-letter words formed from the English alphabet such that there are exactly 2 vowels and 2 consonants and no vowel is repeated, but consonants may be repeated is:

**Options:**

- **(A)** ${}^{4}C_2 \times {}^{5}C_2 \times (21)^2$
- **(B)** ${}^{4}C_2 \times {}^{5}C_2 \times {}^{21}C_2$
- **(C)** ${}^{4}C_2 \times {}^{5}P_2 \times {}^{21}P_2$
- **(D)** ${}^{4}C_2 \times {}^{5}P_2 \times (21)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) ${}^{4}C_2 \times {}^{5}P_2 \times (21)^2$**

**Detailed Solution:**

The 4-letter word requires exactly 2 vowels and 2 consonants.

The number of ways to choose 2 positions out of 4 for the vowels is $^{4}C_{2}$.

Since no vowel is repeated, the number of ways to choose and arrange 2 distinct vowels from the 5 available vowels in the chosen positions is $^{5}P_{2}$.

The remaining 2 positions must be filled with consonants. Since there are 21 consonants and repetition is allowed, each position can be filled in 21 ways. The number of ways to fill the consonant positions is $21 \times 21 = (21)^2$.

The total number of 4-letter words formed is $^{4}C_{2} \times ^{5}P_{2} \times (21)^2$.

Answer: ${}^{4}C_2 \times {}^{5}P_2 \times (21)^2$

</details>

---

### Q9. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of arrangements of the numbers  strictly between 10 and 1000 formed with the digits 0, 1, 2, 3, 4, 5, 6 without repetition is

**Options:**

- **(A)** $180$
- **(B)** $215$
- **(C)** $216$
- **(D)** $222$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $215$**

**Detailed Solution:**

The numbers between $10$ and $1000$ consist of $2$-digit and $3$-digit numbers, strictly greater than $10$.

Available digits: $0, 1, 2, 3, 4, 5, 6$ (a total of $7$ digits).

For $2$-digit numbers:
The tens place can be filled in $6$ ways (excluding $0$).
The units place can be filled in $6$ ways (any of the remaining $6$ digits, including $0$).
Total $2$-digit numbers formed = $6 \times 6 = 36$.
Since the numbers must be strictly between $10$ and $1000$, the number $10$ itself must be excluded.
Valid $2$-digit numbers = $36 - 1 = 35$.

For $3$-digit numbers:
The hundreds place can be filled in $6$ ways (excluding $0$).
The tens place can be filled in $6$ ways.
The units place can be filled in $5$ ways.
Total $3$-digit numbers formed = $6 \times 6 \times 5 = 180$.

Total valid numbers = $35 + 180 = 215$.

Answer: $215$

</details>

---

### Q10. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of cubic equations that can be formed with the coefficients 0, 3, 2, 4, 5, 6 when repetition of coefficients is allowed, is....

**Options:**

- **(A)** $720$
- **(B)** $1296$
- **(C)** $864$
- **(D)** $1080$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1080$**

**Detailed Solution:**

A cubic equation is of the form $ax^3 + bx^2 + cx + d = 0$, where $a \neq 0$.

The given set of coefficients is $\{0, 2, 3, 4, 5, 6\}$, which contains 6 elements.

Since $a \neq 0$, the coefficient $a$ can be chosen in 5 ways (any number from the set except 0).

The coefficients $b, c,$ and $d$ can each be chosen in 6 ways, as repetition of coefficients is allowed.

Total number of cubic equations $= 5 \times 6 \times 6 \times 6 = 1080$.

Answer: $1080$

</details>

---

### Q11. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

There are $5$ boys and $3$ girls seated in a row for a photograph. The number of ways in which a photograph can be taken if the girls occupy only odd places is...

**Options:**

- **(A)** $5040$
- **(B)** $2880$
- **(C)** $720$
- **(D)** $40320$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2880$**

**Detailed Solution:**

Total number of persons is $5 + 3 = 8$.

The seats are numbered $1, 2, 3, 4, 5, 6, 7, 8$.

The odd places are $1, 3, 5, 7$. There are $4$ odd places.

The $3$ girls can be seated in these $4$ odd places in $^{4}P_{3}$ ways.

$^{4}P_{3} = 24$

After seating the girls, there are $5$ seats remaining ($1$ odd and $4$ even places).

The $5$ boys can be seated in the remaining $5$ places in $5!$ ways.

$5! = 120$

Total number of ways $= 24 \times 120 = 2880$.

Answer: $2880$

</details>

---

### Q12. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $m$ denotes the number of ways in which 5 boys and 5 girls can be arranged in a line alternately and n denotes the number of ways in which 5 boys and 5 girls can be arranged in a circle so that no two boys are together. If $m=k n$, then the value of $k$ is

**Options:**

- **(A)** 10
- **(B)** 30
- **(C)** 5
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 10**

**Detailed Solution:**

The number of ways to arrange 5 boys and 5 girls alternately in a line is given by $m$. The arrangement can start with either a boy or a girl.

Number of ways starting with a boy = $5! \times 5!$

Number of ways starting with a girl = $5! \times 5!$

Total ways $m = 2 \times 5! \times 5!$

The number of ways to arrange 5 boys and 5 girls in a circle such that no two boys are together is given by $n$.

First, arrange the 5 girls in a circle in $(5-1)! = 4!$ ways.

There are 5 gaps between the girls. The 5 boys can be arranged in these 5 gaps in $5!$ ways.

Total ways $n = 4! \times 5!$

Given $m = k n$

$2 \times 5! \times 5! = k \times 4! \times 5!$

$2 \times 5 \times 4! \times 5! = k \times 4! \times 5!$

$k = 10$

Answer: 10

</details>

---

### Q13. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If four digit numbers are formed by using the digits $1,2,3,4,5,6,7$ without repetition, then out of these numbers, the numbers exactly divisible by 25 are

**Options:**

- **(A)** $20$
- **(B)** $40$
- **(C)** $50$
- **(D)** $51$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $40$**

**Detailed Solution:**

A number is divisible by $25$ if its last two digits are $00$, $25$, $50$, or $75$.

Since the available digits are $1, 2, 3, 4, 5, 6, 7$ and repetition is not allowed, the last two digits can only be $25$ or $75$.

Case 1: The last two digits are $25$.
The remaining two places (thousands and hundreds) must be filled using any $2$ of the remaining $5$ digits ($1, 3, 4, 6, 7$).
Number of ways = $^{5}P_{2} = 5 \times 4 = 20$.

Case 2: The last two digits are $75$.
The remaining two places must be filled using any $2$ of the remaining $5$ digits ($1, 2, 3, 4, 6$).
Number of ways = $^{5}P_{2} = 5 \times 4 = 20$.

Total number of such four-digit numbers = $20 + 20 = 40$.

Answer: $40$

</details>

---

### Q14. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that in a random arrangement of the letters of the word 'UNIVERSITY' , the two 'I' s do not come together is

**Options:**

- **(A)** $\frac{1}{5}$
- **(B)** $\frac{1}{10}$
- **(C)** $\frac{4}{5}$
- **(D)** $\frac{3}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{5}$**

**Detailed Solution:**

The word 'UNIVERSITY' consists of $10$ letters, in which the letter 'I' appears $2$ times and all other letters are distinct.

Total number of possible arrangements of the letters is $\dfrac{10!}{2!}$.

To find the number of arrangements where the two 'I's come together, we treat them as a single unit (II).

Along with the remaining $8$ distinct letters, there are now $9$ units to arrange. These can be arranged in $9!$ ways.

The probability that the two 'I's come together is:

$P(\text{together}) = \dfrac{9!}{\dfrac{10!}{2!}} = \dfrac{9! \times 2}{10!} = \dfrac{2}{10} = \dfrac{1}{5}$

The probability that the two 'I's do not come together is:

$P(\text{not together}) = 1 - P(\text{together}) = 1 - \dfrac{1}{5} = \dfrac{4}{5}$

Answer: $\frac{4}{5}$

</details>

---

### Q15. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The greatest possible number of points of intersection of 8 distinct straight lines and 4 distinct circles is

**Options:**

- **(A)** $28$
- **(B)** $104$
- **(C)** ${ }^{12} \mathrm{C}_2$
- **(D)** ${ }^4 C_2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $104$**

**Detailed Solution:**

To find the greatest possible number of points of intersection, we consider the maximum number of intersections for each pair of curves:

1. Intersection of two straight lines:
Two distinct straight lines intersect at a maximum of $1$ point.
Number of intersection points from $8$ lines = $^{8}C_{2} \times 1 = \dfrac{8 \times 7}{2} = 28$

2. Intersection of two circles:
Two distinct circles intersect at a maximum of $2$ points.
Number of intersection points from $4$ circles = $^{4}C_{2} \times 2 = \dfrac{4 \times 3}{2} \times 2 = 12$

3. Intersection of a straight line and a circle:
A straight line and a circle intersect at a maximum of $2$ points.
Number of intersection points from $8$ lines and $4$ circles = $8 \times 4 \times 2 = 64$

Total maximum number of points of intersection = $28 + 12 + 64 = 104$

Answer: $104$

</details>

---

### Q16. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Eight chairs are numbered 1 to 8 . Two women and three men wish to occupy one chair each. First the women choose chairs from amongst the chairs marked 1 to 4 , and then the men select the chairs from amongst the remaining. The number of possible arrangements is

**Options:**

- **(A)** ${ }^6 \mathrm{C}_3 \times{ }^4 \mathrm{C}_2$
- **(B)** ${ }^4 \mathrm{P}_2 \times{ }^6 \mathrm{P}_3$
- **(C)** ${ }^4 \dot{C}_2+{ }^4 \mathrm{P}_3$
- **(D)** ${ }^4 \mathrm{P}_2+{ }^6 \mathrm{P}_3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) ${ }^4 \mathrm{P}_2 \times{ }^6 \mathrm{P}_3$**

**Detailed Solution:**

First, the $2$ women choose chairs from the $4$ chairs marked $1$ to $4$. The number of ways to arrange $2$ women on $4$ chairs is $^{4}P_{2}$.

After the women have occupied their chairs, $2$ chairs are taken. The number of remaining chairs is $8 - 2 = 6$.

Next, the $3$ men choose chairs from the remaining $6$ chairs. The number of ways to arrange $3$ men on $6$ chairs is $^{6}P_{3}$.

By the fundamental principle of counting, the total number of possible arrangements is $^{4}P_{2} \times ^{6}P_{3}$.

Answer: ${ }^4 \mathrm{P}_2 \times{ }^6 \mathrm{P}_3$

</details>

---

### Q17. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

There are 3 sections in a question paper and each section contains 5 questions. A candidate has to answer a total of 5 questions, choosing at least one question from each section. Then the number of ways, in which the candidate can choose the questions, is

**Options:**

- **(A)** 750
- **(B)** 1500
- **(C)** 2255
- **(D)** 2250

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2250**

**Detailed Solution:**

The candidate has to answer 5 questions from 3 sections, choosing at least one from each section.

The possible distributions of the number of questions chosen from the three sections are $(1, 1, 3)$ and $(1, 2, 2)$.

Case 1: Selecting 1 question from two sections and 3 questions from one section.
The number of ways to choose the sections is $3$.
The number of ways to select the questions is $3 \times (^{5}C_{1} \times ^{5}C_{1} \times ^{5}C_{3}) = 3 \times (5 \times 5 \times 10) = 750$.

Case 2: Selecting 1 question from one section and 2 questions from two sections.
The number of ways to choose the sections is $3$.
The number of ways to select the questions is $3 \times (^{5}C_{1} \times ^{5}C_{2} \times ^{5}C_{2}) = 3 \times (5 \times 10 \times 10) = 1500$.

Total number of ways $= 750 + 1500 = 2250$.

Answer: 2250

</details>

---

### Q18. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\qquad$ numbers greater than a million can be formed with the digits $2,3,0,3,4,2,3$.

**Options:**

- **(A)** 60
- **(B)** 360
- **(C)** 420
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 360**

**Detailed Solution:**

The given digits are $0, 2, 2, 3, 3, 3, 4$. There are $7$ digits in total, with $2$ repeating twice and $3$ repeating thrice.

A number greater than a million ($1,000,000$) must be a $7$-digit number, which means the first digit cannot be $0$.

Total number of arrangements of the $7$ digits without any restriction is:
$\dfrac{7!}{2!3!} = \dfrac{5040}{2 \times 6} = 420$

Number of arrangements where $0$ is at the first place (which forms a $6$-digit number) is:
$\dfrac{6!}{2!3!} = \dfrac{720}{2 \times 6} = 60$

Therefore, the number of $7$-digit numbers that can be formed is:
$420 - 60 = 360$

Answer: 360

</details>

---

### Q19. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Words of length 10 are formed by using the letters A, B, C, D, E, F, G, H, I, J. Let $x$. be number of such words where no letter is repeated and $y$ be number of such words where exactly two letters are repeated twice and no other letter is repeated, then the value of $\dfrac{y}{x}$ is

**Options:**

- **(A)** 45
- **(B)** 415
- **(C)** 315
- **(D)** 215

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 315**

**Detailed Solution:**

The number of words of length 10 where no letter is repeated is the number of ways to arrange 10 distinct letters.

$x = 10!$

For the words where exactly two letters are repeated twice and no other letter is repeated, the word must contain 2 letters appearing 2 times each and 6 letters appearing exactly once.

The number of ways to choose the 2 letters that appear twice from the 10 available letters is $^{10}C_{2}$.

The number of ways to choose the 6 letters that appear once from the remaining 8 letters is $^{8}C_{6}$.

The number of ways to arrange these 10 letters (with two letters repeating twice) is $\dfrac{10!}{2! 2!}$.

The total number of such words is given by:

$y = ^{10}C_{2} \times ^{8}C_{6} \times \dfrac{10!}{2! 2!}$

$y = 45 \times 28 \times \dfrac{10!}{4}$

$y = 315 \times 10!$

The ratio $\dfrac{y}{x}$ is:

$\dfrac{y}{x} = \dfrac{315 \times 10!}{10!} = 315$

Answer: 315

</details>

---

### Q20. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of four letter words that can be formed using letters of the word BARRACK is

**Options:**

- **(A)** $\cdot$ 120
- **(B)** 264
- **(C)** 270
- **(D)** 144

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 270**

**Detailed Solution:**

The word BARRACK has 7 letters: A, A, R, R, B, C, K.

The available letters are two A's, two R's, one B, one C, and one K.

To form a 4-letter word, the following cases arise:

Case 1: Two alike of one kind and two alike of another kind.
We must choose both pairs (A, A and R, R).
Number of selections = $^{2}C_{2} = 1$
Number of arrangements = $1 \times \dfrac{4!}{2!2!} = 6$

Case 2: Two alike and two different.
Choose 1 pair from the 2 available pairs: $^{2}C_{1} = 2$
Choose 2 distinct letters from the remaining 4 distinct letters: $^{4}C_{2} = 6$
Number of arrangements = $2 \times 6 \times \dfrac{4!}{2!} = 144$

Case 3: All four letters are different.
Choose 4 distinct letters from the 5 available distinct letters (A, R, B, C, K): $^{5}C_{4} = 5$
Number of arrangements = $5 \times 4! = 120$

Total number of 4-letter words = $6 + 144 + 120 = 270$

Answer: 270

</details>

---

### Q21. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Five students are selected from n students such that the ratio of number of ways in which 2 particular students are selected to the number of ways 2 particular students not selected is $2: 3$. Then the value of $\mathrm{n}$ is

**Options:**

- **(A)** 5
- **(B)** 6
- **(C)** 11
- **(D)** not possible

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 11**

**Detailed Solution:**

Five students are selected from $\mathrm{n}$ students. Number of ways in which 2 particular students are sélected $=\mathrm{n}^{-2} \mathrm{C}_3$
Number of ways in which 2 particular students are not selected $={ }^{\mathrm{n}-2} \mathrm{C}_5$
$\therefore \quad$ According to the given condition,
$\frac{{ }^{n-2} C_3}{{ }^{n-2} C_5}=\frac{2}{3}$
$\begin{aligned} & \Rightarrow \frac{(\mathrm{n}-2) !}{3 !(\mathrm{n}-5) !} \times \frac{5 !(\mathrm{n}-7) !}{(\mathrm{n}-2) !}=\frac{2}{3} \\ & \Rightarrow(\mathrm{n}-5)(\mathrm{n}-6)=30 \\ & \Rightarrow \mathrm{n}=11\end{aligned}$

</details>

---

### Q22. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $T_n$ denotes the number of triangles which can be formed using the vertices of regular polygon of $\mathrm{n}$ sides and $\mathrm{T}_{\mathrm{n}+1}-\mathrm{T}_{\mathrm{n}}=21$, then $\mathrm{n}=$

**Options:**

- **(A)** 5
- **(B)** 7
- **(C)** 6
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 7**

**Detailed Solution:**

According to the given condition, $\mathrm{T}_{\mathrm{n}}={ }^{\mathrm{n}} \mathrm{C}_3$
$$
\therefore \quad \mathrm{T}_{\mathrm{n}+1}-\mathrm{T}_{\mathrm{n}}=21 \Rightarrow{ }^{\mathrm{n}+1} \mathrm{C}_3-{ }^{\mathrm{n}} \mathrm{C}_3=21
$$
Note that $\mathrm{n}=7$ satisfies the above condition.
$\therefore \quad$ Option (B) is correct.

</details>

---

### Q23. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of ways in which 8 different pearls can be arranged to from a necklace is

**Options:**

- **(A)** 40320
- **(B)** 5040
- **(C)** 2520
- **(D)** 1260

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2520**

**Detailed Solution:**

Number of necklaces formed from 8 different pearls
$$
=\frac{(8-1) !}{2}=7 \times 6 \times 5 \times 4 \times 3=2520
$$

</details>

---

### Q24. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

All the letters of the word' ABRACADABRA' are arranged in different possible ways. Then the number of such arrangements in which the vowels are together is

**Options:**

- **(A)** 1200
- **(B)** 1240
- **(C)** 1220
- **(D)** 1260

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1260**

**Detailed Solution:**

The word ABRACADABRA has
A: 5 times, B: 2 times, R: 2 times, C, D: 1 time each When all vowels are together, we have to arrange 7 elements. $\therefore$ No. of arrangements $\frac{7 !}{2 ! 2 !}=1260$

</details>

---

