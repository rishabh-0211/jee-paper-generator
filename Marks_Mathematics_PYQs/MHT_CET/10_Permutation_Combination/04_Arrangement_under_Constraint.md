# MHT CET Mathematics - Permutation Combination

## Topic 4: Arrangement under Constraint

**Total Questions:** 25

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

There are 4 boys and 6 girls to be seated in a circle for a photograph. The probability that no two boys are sitting together is...

**Options:**

- **(A)** $\dfrac{5}{42}$
- **(B)** $\dfrac{1}{6}$
- **(C)** $\dfrac{5}{14}$
- **(D)** $\dfrac{1}{210}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{5}{42}$**

**Detailed Solution:**

Total number of people is $10$.

Total number of ways to seat $10$ people in a circle is $(10 - 1)! = 9!$.

To ensure no two boys sit together, first seat the $6$ girls in a circle.

Number of ways to seat $6$ girls in a circle is $(6 - 1)! = 5!$.

There are $6$ gaps between the $6$ girls. The $4$ boys can be placed in these $6$ gaps.

Number of ways to choose $4$ gaps for the $4$ boys is $^{6}C_{4}$.

Number of ways to arrange the $4$ boys in the chosen gaps is $4!$.

Total number of favorable ways is $5! \times ^{6}C_{4} \times 4!$.

The required probability is $\dfrac{5! \times ^{6}C_{4} \times 4!}{9!}$.

Probability $= \dfrac{5! \times 15 \times 24}{9 \times 8 \times 7 \times 6 \times 5!} = \dfrac{360}{3024} = \dfrac{5}{42}$.

Answer: $\dfrac{5}{42}$

</details>

---

### Q2. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A teacher has 2 different books on English, 3 different books on physics, and 4 different books on mathematics. These books are to be placed on the shelf so that all books of the same subjects are together. The number of different ways this can be done is:

**Options:**

- **(A)** $1278$
- **(B)** $1728$
- **(C)** $1872$
- **(D)** $1782$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1728$**

**Detailed Solution:**

Treat the books of each subject as a single unit. Since there are $3$ subjects (English, physics, and mathematics), these $3$ units can be arranged on the shelf in $3!$ ways.

Within their respective units, the $2$ English books can be arranged in $2!$ ways, the $3$ physics books in $3!$ ways, and the $4$ mathematics books in $4!$ ways.

Total number of ways is given by the product of these possibilities:

$3! \times 2! \times 3! \times 4!$

$= 6 \times 2 \times 6 \times 24$

$= 1728$

Answer: $1728$

</details>

---

### Q3. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of arrangements of the letters in the word SOLAPUR, so that consonants and vowels are placed alternately is

**Options:**

- **(A)** $100$
- **(B)** $129$
- **(C)** $144$
- **(D)** $121$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $144$**

**Detailed Solution:**

The word SOLAPUR consists of 7 letters.

The vowels are O, A, U (3 vowels).

The consonants are S, L, P, R (4 consonants).

Since consonants and vowels must be placed alternately and there are 4 consonants and 3 vowels, the arrangement must start and end with a consonant. The only possible pattern is C V C V C V C, where C represents a consonant and V represents a vowel.

The 4 consonants can be arranged in the 4 alternate positions in $4!$ ways.

The 3 vowels can be arranged in the 3 remaining alternate positions in $3!$ ways.

Total number of arrangements is $4! \times 3!$.

$24 \times 6 = 144$

</details>

---

### Q4. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If 6 boys and 3 girls are to be seated in a row for a photograph, then the probability that the end seats are occupied by the girls and no two girls are side by side is

**Options:**

- **(A)** $\dfrac{5}{12}$
- **(B)** $\dfrac{1}{28}$
- **(C)** $\dfrac{1}{84}$
- **(D)** $\dfrac{5}{84}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{5}{84}$**

**Detailed Solution:**

Total number of arrangements of $6$ boys and $3$ girls in a row is $9!$.

For the end seats to be occupied by girls, we can select and arrange $2$ girls out of $3$ in $^{3}P_{2} = 6$ ways.

The remaining $1$ girl and $6$ boys are to be seated in the remaining $7$ middle seats. To ensure no two girls are side by side, the remaining $1$ girl cannot sit in the seats adjacent to the ends (i.e., the 2nd and 8th seats).

Thus, the remaining girl can sit in any of the $5$ available middle seats (3rd, 4th, 5th, 6th, or 7th).

The $6$ boys can then be arranged in the remaining $6$ seats in $6!$ ways.

Total number of favorable arrangements is $6 \times 5 \times 6! = 30 \times 6!$.

The required probability is $\dfrac{30 \times 6!}{9!} = \dfrac{30}{9 \times 8 \times 7} = \dfrac{5}{84}$.

Answer: $\dfrac{5}{84}$

</details>

---

### Q5. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of five-digit numbers formed using the digits $2, 3, 5, 7, 9$ without repetition and which are greater than $24000$ are

**Options:**

- **(A)** $120$
- **(B)** $117$
- **(C)** $114$
- **(D)** $96$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $114$**

**Detailed Solution:**

The total number of five-digit numbers that can be formed using the digits $2, 3, 5, 7, 9$ without repetition is $5! = 120$.

For a number to be less than $24000$, it must start with $2$ and the second digit must be less than $4$.

From the given digits, the only possible second digit less than $4$ is $3$. Thus, the numbers less than $24000$ must be of the form $23XXX$.

The remaining three positions can be filled by the remaining three digits ($5, 7, 9$) in $3! = 6$ ways.

Therefore, the number of five-digit numbers greater than $24000$ is $120 - 6 = 114$.

</details>

---

### Q6. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of ways in which 6 boys and 4 girls can be seated around a round table such that 2 special boys and a special girl never all sit together is

**Options:**

- **(A)** 332620
- **(B)** 332540
- **(C)** 332640
- **(D)** 332520

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 332640**

**Detailed Solution:**

Total number of persons = $6 + 4 = 10$

Total number of ways to arrange $10$ persons around a round table = $(10 - 1)! = 9!$

To find the number of ways where the $2$ special boys and $1$ special girl sit together, we consider them as a single unit.

Number of units to arrange = $7$ remaining persons + $1$ special unit = $8$ units.

Number of ways to arrange these $8$ units around a round table = $(8 - 1)! = 7!$

The $3$ special persons can be arranged among themselves in $3!$ ways.

Number of ways in which the $3$ special persons sit together = $7! \times 3!$

Number of ways in which they never all sit together = Total ways - Ways they sit together

$= 9! - 7! \times 3!$

$= 9 \times 8 \times 7! - 6 \times 7!$

$= (72 - 6) \times 7!$

$= 66 \times 5040$

$= 332640$

Answer: 332640

</details>

---

### Q7. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of ways, in which 6 boys and 5 girls can sit at a round table, if no two girls are to sit together, is

**Options:**

- **(A)** $518400$
- **(B)** $14400$
- **(C)** $86400$
- **(D)** $17280$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $86400$**

**Detailed Solution:**

First, arrange the 6 boys around the round table. The number of ways to arrange $n$ distinct objects in a circle is $(n-1)!$.

Number of ways to arrange 6 boys = $(6-1)! = 5! = 120$.

These 6 boys create 6 gaps between them. To ensure that no two girls sit together, the 5 girls must be seated in these 6 gaps.

The number of ways to arrange 5 girls in 6 gaps is $^{6}P_{5}$.

$^{6}P_{5} = \dfrac{6!}{(6-5)!} = 6! = 720$.

Total number of ways = $120 \times 720 = 86400$.

Answer: $86400$

</details>

---

### Q8. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A five digit number divisible by 3 is to be formed using the digits $0,1,2,3,4,5$ without repetition, then the total number of ways this can be done is

**Options:**

- **(A)** 216
- **(B)** 240
- **(C)** 96
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 216**

**Detailed Solution:**

The given digits are $0, 1, 2, 3, 4, 5$.

The sum of all these $6$ digits is $0 + 1 + 2 + 3 + 4 + 5 = 15$.

To form a $5$-digit number, exactly one digit must be excluded. For the number to be divisible by $3$, the sum of its digits must be divisible by $3$. Since the sum of all $6$ digits is $15$ (which is divisible by $3$), the excluded digit must also be a multiple of $3$.

The possible digits to exclude are $0$ and $3$.

Case 1: Excluding $0$
The digits available are $1, 2, 3, 4, 5$.
The number of $5$-digit numbers that can be formed is $5! = 120$.

Case 2: Excluding $3$
The digits available are $0, 1, 2, 4, 5$.
For a $5$-digit number, the first digit cannot be $0$. Thus, the first digit can be chosen in $4$ ways (from $1, 2, 4, 5$).
The remaining $4$ positions can be filled by the remaining $4$ digits in $4!$ ways.
The number of $5$-digit numbers that can be formed is $4 \times 4! = 4 \times 24 = 96$.

Total number of $5$-digit numbers divisible by $3$ is $120 + 96 = 216$.

Answer: 216

</details>

---

### Q9. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of arrangements, of the letters of the word MANAMA in which two M's do not appear adjacent, is

**Options:**

- **(A)** 40
- **(B)** 60
- **(C)** 80
- **(D)** 100

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 40**

**Detailed Solution:**

The word MANAMA consists of 6 letters: 2 M's, 3 A's, and 1 N.

Total number of arrangements of these letters is $\dfrac{6!}{2!3!} = \dfrac{720}{2 \times 6} = 60$.

To find the number of arrangements where the two M's are adjacent, we treat them as a single unit (MM). The letters to arrange are (MM), A, A, A, N, which are 5 units.

Number of arrangements with M's adjacent is $\dfrac{5!}{3!} = \dfrac{120}{6} = 20$.

Number of arrangements where two M's do not appear adjacent is $60 - 20 = 40$.

Answer: 40

</details>

---

### Q10. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider a group of 5 boys and 7 girls. The number of different teams, consisting of 2 boys and 3 girls that can be formed from this group if there are two specific girls A and B , who refuse to be the members of the same team, is

**Options:**

- **(A)** 350
- **(B)** 300
- **(C)** 200
- **(D)** 500

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 300**

**Detailed Solution:**

Number of ways to select $2$ boys from $5$ boys = $^{5}C_{2} = 10$

Number of ways to select $3$ girls from $7$ girls without any restriction = $^{7}C_{3} = 35$

Number of ways to select $3$ girls such that both specific girls A and B are included = $^{5}C_{1} = 5$

Number of ways to select $3$ girls such that A and B are not in the same team = $35 - 5 = 30$

Total number of different teams that can be formed = $10 \times 30 = 300$

Answer: 300

</details>

---

### Q11. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of ways in which 5 boys and 3 girls can be seated on a round table, if a particular boy $B_1$ and a particular girl $G_1$ never sit adjacent to each other, is

**Options:**

- **(A)** 7 !
- **(B)** $5 \times 6$ !
- **(C)** $6 \times 6$ !
- **(D)** $5 \times 7$ !

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5 \times 6$ !**

**Detailed Solution:**

Total number of persons is $5 + 3 = 8$.

Total number of ways to arrange $8$ persons around a round table is $(8 - 1)! = 7!$.

To find the number of ways in which $B_1$ and $G_1$ sit together, consider them as a single unit. The number of entities to be arranged is now $6 + 1 = 7$.

The number of ways to arrange these $7$ entities around a round table is $(7 - 1)! = 6!$.

The unit of $B_1$ and $G_1$ can be arranged internally in $2! = 2$ ways.

Number of ways in which $B_1$ and $G_1$ sit together is $2 \times 6!$.

Number of ways in which $B_1$ and $G_1$ never sit adjacent is the total number of ways minus the number of ways they sit together.

Required number of ways is $7! - 2 \times 6! = 7 \times 6! - 2 \times 6! = 5 \times 6!$.

Answer: $5 \times 6$ !

</details>

---

### Q12. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A committee of 11 members is to be formed from 8 males and 5 females. If $m$ is the number of ways the committee is formed with at least 6 males and $n$ is the number of ways the committee is formed with at least 3 females, then

**Options:**

- **(A)** $\mathrm{m}+\mathrm{n}=68$
- **(B)** $\mathrm{m}=\mathrm{n}=78$
- **(C)** $\quad \mathrm{m}=\mathrm{n}=68$
- **(D)** $\mathrm{n}=\mathrm{m}-8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{m}=\mathrm{n}=78$**

**Detailed Solution:**

Total number of males = $8$

Total number of females = $5$

Total members to be selected = $11$

Total available members = $13$

Total ways to select $11$ members = $^{13}C_{11} = ^{13}C_{2} = \dfrac{13 \times 12}{2} = 78$

For $m$: The committee must have at least $6$ males. Since the maximum number of females available is $5$, any committee of $11$ members will automatically have at least $11 - 5 = 6$ males. Thus, all possible committees satisfy this condition.

$m = 78$

For $n$: The committee must have at least $3$ females. Since the maximum number of males available is $8$, any committee of $11$ members will automatically have at least $11 - 8 = 3$ females. Thus, all possible committees satisfy this condition.

$n = 78$

Therefore, $m = n = 78$

Answer: $\mathrm{m}=\mathrm{n}=78$

</details>

---

### Q13. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Number of different nine digit numbers, that can be formed from the digits in the number 223355888 by rearranging its digits, so that the odd digits occupy even positions, is

**Options:**

- **(A)** 16
- **(B)** 40
- **(C)** 60
- **(D)** 180

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 60**

**Detailed Solution:**

The given digits are $2, 2, 3, 3, 5, 5, 8, 8, 8$.

Total number of digits is $9$.

The odd digits are $3, 3, 5, 5$ (total $4$ digits).

The even digits are $2, 2, 8, 8, 8$ (total $5$ digits).

In a $9$-digit number, the even positions are $2, 4, 6, 8$ (total $4$ positions) and the odd positions are $1, 3, 5, 7, 9$ (total $5$ positions).

Since the odd digits must occupy the even positions, we arrange the $4$ odd digits in the $4$ even positions. The number of ways to do this is $\dfrac{4!}{2!2!} = 6$.

The remaining $5$ even digits must be arranged in the $5$ odd positions. The number of ways to do this is $\dfrac{5!}{2!3!} = 10$.

The total number of different $9$-digit numbers that can be formed is $6 \times 10 = 60$.

Answer: 60

</details>

---

### Q14. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If 3 books on Physics, 2 books on Chemistry and 4 books on Mathematics are to be arranged on a shelf so that all the Physics books are together and all the Mathematics books are together, then the number of such arrangements is

**Options:**

- **(A)** 576
- **(B)** 288
- **(C)** 3456
- **(D)** 1152

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3456**

**Detailed Solution:**

Let the 3 Physics books be grouped together as a single unit and the 4 Mathematics books be grouped together as another single unit.

The 2 Chemistry books are treated as individual units since there is no restriction on them.

Total number of units to arrange = $1$ (Physics unit) + $1$ (Mathematics unit) + $2$ (Chemistry books) = $4$ units.

These $4$ units can be arranged in $4!$ ways.

The $3$ Physics books can be arranged among themselves in $3!$ ways.

The $4$ Mathematics books can be arranged among themselves in $4!$ ways.

Total number of arrangements = $4! \times 3! \times 4!$

Total number of arrangements = $24 \times 6 \times 24 = 3456$

Answer: 3456

</details>

---

### Q15. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of words that can be formed by using the letters of the word CALCULATE such that each word starts and ends with a consonant, are

**Options:**

- **(A)** $5 \times 7 !$
- **(B)** $\frac{9 !}{8}$
- **(C)** $\frac{5 \times 7 !}{2}$
- **(D)** $20 \times 7 !$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{5 \times 7 !}{2}$**

**Detailed Solution:**

Word CALCULATE has 9 letters.
Out of which ' $C$ ' repeats 2 times,
'A' repeats 2 times,
' $L$ ' repeats 2 times,
'E', 'U' and ' $T$ ' repeats once.
$\therefore \quad$ There are 5 consonants and 4 vowels.
Two consonants out of 5 can take start and end position of the word in ${ }^5 \mathrm{P}_2$ ways.
And remaining 7 letters can take remaining 7 positions in 7 ! ways.
Also, 'C', 'A' and ' $L$ ' repeats twice each.
$\therefore \quad$ The required number of words that can be formed $=\frac{5 p_2 \times 7 !}{2 ! \times 2 ! \times 2 !}=\frac{5 \times 4 \times 3 ! \times 7 !}{3 ! \times 2 \times 2 \times 2}=\frac{5 \times 7 !}{2}$

</details>

---

### Q16. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The teacher wants to arrange 5 students on the platform such that the boy $\mathrm{B}_1$ occupies second position and the girls $\mathrm{G}_1$ and $\mathrm{G}_2$ are always adjacent to each other, then the number of such arrangements is

**Options:**

- **(A)** $24$
- **(B)** $12$
- **(C)** $8$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_uWfV_Y3fb9lUsLgR7fYpmXx40cmr8qy10JJKH_SDPY.original.fullsize.png">

There are 5 positions. Given that $\mathrm{B}_1$ occupies $2^{\text {nd }}$ position
$\therefore \quad \mathrm{B}_1$ can be arranged in 1 way. As $G_1$ and $G_2$ are always together, none of them can take $1^{\text {st }}$ position.
$\therefore \quad \mathrm{G}_1, \mathrm{G}_2$ and one of the remaining students can be arranged on $3^{\text {rd }}, 4^{\text {th }}$ and $5^{\text {th }}$ position when $\mathrm{G}_1$ and $\mathrm{G}_2$ are always together in $2 ! \times 2$ ! Ways.
And remaining 2 students can be arranged in 2 ! Ways.
$\therefore \quad$ The required number of arrangements
$\begin{aligned}
& =2 ! \times 2 ! \times 2 ! \\
& =8
\end{aligned}$

</details>

---

### Q17. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Five students are to be arranged on a platform such that the boy $B_1$ occupies the second position and such that the girl $\mathrm{G}_1$ is always adjacent to the girl $G_2$. Then, the number of such possible arrangements is

**Options:**

- **(A)** $4$
- **(B)** $7$
- **(C)** $8$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bCPLypbjtYZ1Bc4-rf-yRhuvk8Hw4s3EM-8b4Tm9J28.original.fullsize.png">


There are 5 positions. Given that $\mathrm{B}_1$ occupies $2^{\text {nd }}$ position
$\therefore \quad \mathrm{B}_1$ can be arranged in 1 way. As $\mathrm{G}_1$ and $\mathrm{G}_2$ are always together, none of them can take $1^{\text {st }}$ position.
$\therefore \quad \mathrm{G}_1, \mathrm{G}_2$ and one of the remaining students can be arranged on $3^{\text {rd }}, 4^{\text {th }}$ and $5^{\text {th }}$ position when $\mathrm{G}_1$ and $\mathrm{G}_2$ are always together in $2 ! \times 2$ ! Ways.
And remaining 2 students can be arranged in 2 ! Ways.
$\therefore \quad$ The required number of arrangements $=2 ! \times 2 ! \times 2 !=8$

</details>

---

### Q18. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A linguistic club of a certain Institute consists of 6 girls and 4 boys. A team of 4 members to be selected from this group including the selection of a Captain (from among these 4 members) for the team. If the team has to include atmost one boy, the number of ways of selecting the team is

**Options:**

- **(A)** 95
- **(B)** 260
- **(C)** 320
- **(D)** 380

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 380**

**Detailed Solution:**

Case I: No boy is included. Selecting 4 girls from 6 girls $={ }^6 \mathrm{C}_4$
Selecting 1 captain from selected members $={ }^4 C_1$ Total number of ways $={ }^6 \mathrm{C}_4 \times{ }^4 \mathrm{C}_1=60$
Case II: One boy is included.
Selecting 3 girls and 1 boy from given members $={ }^6 \mathrm{C}_3 \times{ }^4 \mathrm{C}_1$.
Selecting 1 captain from the selected members $={ }^4 \mathrm{C}_1$.
Total Number of ways $={ }^6 \mathrm{C}_3 \times{ }^4 \mathrm{C}_1 \times{ }^4 \mathrm{C}_1=320$.
Total Number of ways $=320+60=380$.

</details>

---

### Q19. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

There are 6 periods in each working day of a school. The number of ways one can arrange 5 subjects such that each is allowed at least one period, is

**Options:**

- **(A)** 3600
- **(B)** 725
- **(C)** 720
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3600**

**Detailed Solution:**

First of all we can choose the subject which is to be repeated twice in ${ }^5 C_1$ ways

Now 6 subjects with one repeation can be arranged among 6 periods in
$\frac{6 !}{2 !}$
Hence, total number of ways ${ }^5 C_1 \times \frac{6 !}{2 !}=1800$

</details>

---

### Q20. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of different 9 digit number that can be formed, from the digits of the number 445577888 by rearranging its digits, so that the odd digits occupy even positions, are

**Options:**

- **(A)** $120$
- **(B)** $60$
- **(C)** $180$
- **(D)** $36$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $60$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/6bXaO9a9swJudZWn1AiWl_vV5SZG9MUc35Xkfpsb0xc.original.fullsize.png">
ways
and remaing five even digits $4,4,8,8,8$ can be arranged in 5 places in $\frac{\underline{5}}{2 \underline{3}}$
Hence total no of ways $=\frac{\lfloor 4}{\lfloor 2 L 2} \times \frac{\underline{5}}{2 \underline{2} \underline{3}}=6 \times 10=60$

</details>

---

### Q21. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of ways in which the letters of the word MACHINE can be arranged such that the vowels may occupy only odd positions, is

**Options:**

- **(A)** 288
- **(B)** 625
- **(C)** 576
- **(D)** 1152

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 576**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/jg9XA4iBi03NQPJO3jsOCHOvqScQX2AvuUvJ1tYE8EU.original.fullsize.png">
A, I, E (3 vowels)
M, C, H, N (4 consonants)
There are 4 odd places. So, three vowels can be arranged in four places in $4_{\mathrm{P}_3}$ ways and 4 consonants can be arranged in remaining four places in $4_{\mathrm{P}_4}$ ways.
Hence total number of ways $=4_{\mathrm{P}_3} \times 4_{\mathrm{P}_4}=576$

</details>

---

### Q22. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

It is required to seat 5 men and 4 women in a row so that the men occupy odd places. Then the number of arrangements that are possible is

**Options:**

- **(A)** $144$
- **(B)** $362880$
- **(C)** $2880$
- **(D)** $1140$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2880$**

**Detailed Solution:**

$\frac{M}{1} \frac{W}{2} \frac{M}{3} \frac{W}{4} \frac{M}{5} \frac{W}{6} \frac{M}{7} \frac{W}{8} \frac{M}{9}$
5 men can be seated in 5 odd places in $5_{\mathrm{P}_5}=120$ ways and 4 women can be seated in remaining 4 places in $4_{p_4}=24$ ways $\Rightarrow$ Total possible arrangements $=120 \times 24=2880$

</details>

---

### Q23. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The numbers can be formed using the digit $1,2,3,4,3,2,1$ so that odd digits always occupy odd places in <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/nhevxViltEdZtH2omqY4EKG5wOMChiXZp2okHK3YKPs.original.fullsize.png">
ways.

**Options:**

- **(A)** 9
- **(B)** 18
- **(C)** 6
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 18**

**Detailed Solution:**

We have 4 odd digits i.e. 1,1,3,3 and 3 even digits i.e. 2,2, 4 In a 7 digit number, there are 4 odd and 3 even places.
So number of possible ways $=\frac{4 !}{2 ! 2 !} \times \frac{3 !}{2 !}=18$

</details>

---

### Q24. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

If the four positive integers are selected randomly from the set of positive integers, then the probability that the number $1,3,7$ and 9 are in the unit place in the product of 4 -digit, so selected is

**Options:**

- **(A)** $\frac{7}{625}$
- **(B)** $\frac{2}{5}$
- **(C)** $\frac{5}{625}$
- **(D)** $\frac{16}{625}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{16}{625}$**

**Detailed Solution:**

The number of digits on unit place of any number $=10$
$\therefore$
$$
n(S)=10
$$
The necessary condition for becoming the digits $1,3,5$ or 7 at the unit place of product of four numbers that the digits $1,3,5$ or 7 at unit place of every number.
$$
\begin{array}{ll}
\therefore & n(A)=4 \\
\therefore & P(A)=\frac{4}{10}=\frac{2}{5}
\end{array}
$$
So, required $y=\left(\frac{2}{5}\right)^{4}=\frac{16}{625}$

</details>

---

### Q25. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

All letters of the word 'CEASE' are arranged randomly in a row, then the probability that two $\mathrm{E}$ are found together is

**Options:**

- **(A)** $\frac{7}{5}$
- **(B)** $\frac{3}{5}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{5}$**

**Detailed Solution:**

Sample space arrangement for the word 'CEASE' $=5$ !
$$
\text { Here, } \mathrm{E} \rightarrow 2, \mathrm{C} \rightarrow 1, \mathrm{~A} \rightarrow 1, \mathrm{~S} \rightarrow 1
$$
Now, consider $2 \mathrm{E}$ as one character, so that arranging for four letters $=4 !$ ways
$\therefore$ Required probability $=\frac{4 !}{5 !}=\frac{1}{5}$

</details>

---

