# JEE Main Mathematics - Permutation Combination

## Topic 2: Permutation

**Total Questions:** 48

---

### Q1. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of ways of forming a queue of $4$ boys and $3$ girls such that all the girls are not together, is:

**Options:**

- **(A)** $5040$
- **(B)** $3050$
- **(C)** $3410$
- **(D)** $4320$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4320$**

**Detailed Solution:**

Total number of boys $= 4$

Total number of girls $= 3$

Total number of children $= 7$

Total number of ways to arrange $7$ children in a queue $= 7! = 5040$

To find the number of ways where all $3$ girls are together, consider the $3$ girls as a single unit.

Total number of units to arrange $= 4$ boys $+ 1$ unit of girls $= 5$ units.

Number of ways to arrange these $5$ units $= 5! = 120$

Number of ways to arrange the $3$ girls among themselves $= 3! = 6$

Total number of ways where all girls are together $= 5! \times 3! = 120 \times 6 = 720$

Number of ways such that all the girls are not together $= \text{Total ways} - \text{Ways where all girls are together}$

$= 5040 - 720 = 4320$

Answer: $4320$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of seven-digit numbers, that can be formed by using the digits $1, 2, 3, 5$ and $7$ such that each digit is used at least once, is :

**Options:**

- **(A)** $15400$
- **(B)** $17800$
- **(C)** $16800$
- **(D)** $29400$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $16800$**

**Detailed Solution:**

A seven-digit number is to be formed using the $5$ digits $1, 2, 3, 5,$ and $7$. Since each digit must be used at least once, the remaining $2$ places can be filled by either repeating one digit two more times, or repeating two digits one more time each.

This gives rise to two cases for the frequencies of the digits:

Case 1: One digit appears $3$ times and the other four digits appear $1$ time each.
The number of ways to choose the digit that appears $3$ times is $^{5}C_{1}$.
The number of arrangements of these $7$ digits is $\dfrac{7!}{3!}$.
Number of numbers formed in this case = $^{5}C_{1} \times \dfrac{7!}{3!} = 5 \times \dfrac{5040}{6} = 4200$.

Case 2: Two digits appear $2$ times each and the other three digits appear $1$ time each.
The number of ways to choose the two digits that appear $2$ times is $^{5}C_{2}$.
The number of arrangements of these $7$ digits is $\dfrac{7!}{2!2!}$.
Number of numbers formed in this case = $^{5}C_{2} \times \dfrac{7!}{2!2!} = 10 \times \dfrac{5040}{4} = 12600$.

Total number of seven-digit numbers = $4200 + 12600 = 16800$.

Answer: $16800$

</details>

---

### Q3. JEE Main 2026 (28 January Shift 2)

*Type:* `numerical` | *Level:* `1`

Three persons enter in a lift at the ground floor. The lift will go upto $10^{\text {th }}$ floor. The number of ways, in which the three persons can exit the lift at three different floors, if the lift does not stop at first, second and third floors, is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **210**

**Detailed Solution:**

Three persons must exit at three different floors.
The lift goes to the 10th floor and does not stop at floors 1, 2, and 3.
Available floors for exit: 4, 5, 6, 7, 8, 9, 10 (7 floors total).
The number of ways to assign 3 persons to 3 different floors from 7 available floors is a permutation problem: $P(7, 3) = 7 \times 6 \times 5 = 210$.
Alternatively, choose 3 floors from 7 and arrange 3 persons: ${}^{7}P_{3} = 35 \times 6 = 210$.

</details>

---

### Q4. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{S}=\{1,2,3,4,5,6,7,8,9\}$. Let $x$ be the number of 9 -digit numbers formed using the digits of the set S such that only one digit is repeated and it is repeated exactly twice. Let $y$ be the number of 9-digit numbers formed using the digits of the set S such that only two digits are repeated and each of these is repeated exactly twice. Then,

**Options:**

- **(A)** $56 x=9 y$
- **(B)** $29 x=5 y$
- **(C)** $45 x=7 y$
- **(D)** $21 x=4 y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $21 x=4 y$**

**Detailed Solution:**

$x$ counts 9-digit numbers using $\{1,2,3,4,5,6,7,8,9\}$ with exactly one digit repeated twice (8 distinct digits, one twice, one absent). 
 Choose digit appearing twice: 9 ways.
Choose absent digit: 8 ways.
Arrange: $\frac{9!}{2!}$ ways. 
 $x = 9 \times 8 \times \frac{9!}{2!} = 72 \times 181440 = 13043520$. 
 $y$ counts 9-digit numbers with exactly two digits each repeated twice (7 distinct digits, two appear twice, two absent). 
 Choose 2 digits for repetition: $\binom{9}{2}$ ways.
Choose 2 absent digits: $\binom{7}{2}$ ways.
Arrange: $\frac{9!}{2! \times 2!}$ ways. 
 $y = 36 \times 21 \times \frac{9!}{4} = 756 \times \frac{9!}{4}$. 
 $\frac{x}{y} = \frac{72 \times 9!/2}{756 \times 9!/4} = \frac{72 \times 4}{756 \times 2} = \frac{288}{1512} = \frac{4}{21}$. 
 Therefore $21x = 4y$

</details>

---

### Q5. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The letters of the word "UDAYPUR" are written in all possible ways with or without meaning and these words are arranged as in a dictionary. The rank of the word "UDAYPUR" is

**Options:**

- **(A)** 1579
- **(B)** 1581
- **(C)** 1578
- **(D)** 1580

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1580**

**Detailed Solution:**

Letters of UDAYPUR: A, D, P, R, U, U, Y (U repeated twice).
Words starting with a letter before U: letters A, D, P, R each give $\frac{6!}{2!} = 360$ arrangements $\Rightarrow 4 \times 360 = 1440$.
Fix U at position 1. Remaining: A, D, P, R, U, Y (all distinct).
Words starting with UA: $5! = 120$.
Fix UD at positions 1-2. Remaining: A, P, R, U, Y. No letter before A, so fix UDA.
Remaining: P, R, U, Y. Letters before Y: P, R, U give $3 \times 3! = 18$.
Fix UDAY. Remaining: P, R, U. No letter before P, fix UDAYP.
Remaining: R, U. Letter before U: R gives $1! = 1$.
Fix UDAYPU, last letter R: the word itself.
Rank $= 1440 + 120 + 18 + 1 + 1 = 1580$.

</details>

---

### Q6. JEE Main 2026 (24 January Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of numbers greater than 5000, less than 9000 and divisible by 3, that can be formed using the digits $0,1,2,5,9$, if the repetition of the digits is allowed, is $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **42**

**Detailed Solution:**

(1) all different
$5, 0, 1, 9 \Rightarrow \lfloor 3 = 6$ ways
(2) 2 alike, 2 different
$5, 0, 0, 1 \Rightarrow 3$ ways
$5, 1, 1, 2 \Rightarrow 3$ ways
$5, 2, 2, 0 \Rightarrow 3$ ways
$5, 2, 2, 9 \Rightarrow 3$ ways
$5, 5, 0, 2 \Rightarrow 6$ ways
$5, 5, 2, 9 \Rightarrow 6$ ways
$5, 1, 9, 9 \Rightarrow 3$ ways
(3) 3 alike, 1 different
$5, 5, 5, 0 \Rightarrow 3$ ways
$5, 5, 5, 9 \Rightarrow 3$ ways
(4) 2 alike, 2 other alike
$5, 5, 1, 1 \Rightarrow 3$ ways
Total ways $= 42$

</details>

---

### Q7. JEE Main 2026 (23 January Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of 4 -letter words, with or without meaning, which can be formed using the letters PQRPQRSTUVP, is $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1422**

**Detailed Solution:**

Letters: P(3), Q(2), R(2), S(1), T(1), U(1), V(1) — 7 distinct letters.
All distinct: $\binom{7}{4} \times 4! = 840$.
One pair + 2 distinct: choose repeating letter from $\{P,Q,R\}$ (3 ways), choose 2 from remaining 6 ($\binom{6}{2}=15$), arrange $= 4!/2! = 12$. Total $= 3 \times 15 \times 12 = 540$.
Two pairs: choose 2 from $\{P,Q,R\}$ ($\binom{3}{2}=3$), arrange $= 4!/(2!2!) = 6$. Total $= 18$.
One triple + 1 distinct: only P can repeat 3 times, choose 1 from 6, arrange $= 4!/3! = 4$. Total $= 24$.
Answer $= 840 + 540 + 18 + 24 = 1422$.

</details>

---

### Q8. JEE Main 2025 (4 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let m and $\mathrm{n},(\mathrm{m} \lt \mathrm{n})$ be two 2-digit numbers. Then the total numbers of pairs $(m, n)$, such that $\operatorname{gcd}(m, n)=6$, is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **64**

**Detailed Solution:**

Let $\mathrm{m}=6 \mathrm{a}, \mathrm{n}=6 \mathrm{~b}$
$\mathrm{m} \lt \mathrm{n} \Rightarrow \mathrm{a} \lt \mathrm{b}$
where $\mathrm{a} \& \mathrm{~b}$ are co-prime numbers also since $m \& n$ are 2 digit nos, so
$10 \leq \mathrm{m} \leq 99 \& 10 \leq \mathrm{n} \leq 99$
i.e. $2 \leq \mathrm{a} \leq 16 \& 2 \leq \mathrm{b} \leq 16$
( $\because$ a is integer)
Now
$2 \leq \mathrm{a} \lt \mathrm{b} \leq 16 \& \quad \mathrm{a} \& \mathrm{~b}$ are co-prime
$\therefore$ if
$\mathrm{a}=2, \mathrm{~b}=3,5,7,9,11,13,15$
$a=3, b=4,5,7,8,10,11,13,14,16$
$a=4, b=5,7,9,11,13,15$
$a=5, b=6,7,8,9,11,12,13,14,16$
$\mathrm{a}=6, \mathrm{~b}=7,11,13$
$\mathrm{a}=7, \mathrm{~b}=8,9,10,11,12,13,15,16$
$\mathrm{a}=8, \mathrm{~b}=9,11,13,15$
$a=9, b=10,11,13,14,16$
$\mathrm{a}=10, \mathrm{~b}=11,13$
$\mathrm{a}=11, \mathrm{~b}=12,13,14,15,16$
$\mathrm{a}=12, \mathrm{~b}=13$
$a=13, b=14,15,16$
$\mathrm{a}=14, \mathrm{~b}=15$
$\mathrm{a}=15, \mathrm{~b}=16$
64 ordered pairs

</details>

---

### Q9. JEE Main 2025 (3 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

If the number of seven-digit numbers, such that the sum of their digits is even, is $m \cdot n \cdot 10^{\mathrm{n}}$; $m, n \in\{1,2,3, \ldots, 9\}$, then $m+n$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

Total 7 digit nos. $=9000000$
7 digit nos. having sum of digits
Even $=4500000$
$=9.5 \cdot 10^5$
$\mathrm{m}=9, \mathrm{n}=5$
$\mathrm{m}+\mathrm{n}=14$

</details>

---

### Q10. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of sequences of ten terms, whose terms are either 0 or 1 or 2 , that contain exactly five 1 s and exactly three 2 s , is equal to

**Options:**

- **(A)** 360
- **(B)** 45
- **(C)** 2520
- **(D)** 1820

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2520**

**Detailed Solution:**

11111 222 00
No. of sequences $=\frac{10!}{5!3!2!}=2520$
Note : Sequence can start with 0.

</details>

---

### Q11. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If all the words with or without meaning made using all the letters of the word "KANPUR" are arranged as in a dictionary, then the word at $440^{\text {th }}$ position in this arrangement, is :

**Options:**

- **(A)** PRNAUK
- **(B)** PRKANU
- **(C)** PRKAUN
- **(D)** PRNAKU

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) PRKAUN**

**Detailed Solution:**

A, K, N, P, R, U
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/WwKjf38ETt6eK45ggjQW9cqzF5NvUEF8SXN5g__wdR8.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pJrPQ38zr-dXLIS9GgklYfwjt18amtH_za6d_HchsGs.original.fullsize.png">

$\begin{aligned} & \text { Total }=440 \\ & \Rightarrow 440^{\text {th }} \text { word is P R K A U N }\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of 6-letter words, with or without meaning, that can be formed using the letters of the word MATHS such that any letter that appears in the word must appear at least twice, is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1405**

**Detailed Solution:**

(i) Single letter is used, then no. of words $=5$
(ii) Two distinct letters are used, then no. of words
${ }^5 \mathrm{C}_2 \times\left(\frac{6!}{2!4!} \times 2+\frac{6!}{3!3!}\right)=10(30+20)=500$
(iii) Three distinct letters are used, then no. of words
${ }^5 \mathrm{C}_3 \times \frac{6!}{2!2!2!}=900$

Total no. of words $=1405$

</details>

---

### Q13. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let P be the set of seven digit numbers with sum of their digits equal to 11 . If the numbers in P are formed by using the digits 1,2 and 3 only, then the number of elements in the set \(P\) is :

**Options:**

- **(A)** 173
- **(B)** 164
- **(C)** 158
- **(D)** 161

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 161**

**Detailed Solution:**

(i) number of numbers created using
$1111133=\frac{7!}{5!2!} \Rightarrow 21$
(ii) number of numbers created using
$1111223=\frac{7!}{4!2!} \Rightarrow 105$
(iii) number of numbers created using
$1112222=\frac{7!}{4!3!} \Rightarrow 35$

Total $=161$

</details>

---

### Q14. JEE Main 2025 (28 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of natural numbers, between 212 and 999 , such that the sum of their digits is 15 , is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **64**

**Detailed Solution:**

Let the number be
$\begin{aligned}
& 2 a b, a+b=13 \\
& \Rightarrow a, b \in\{0,9\} \\
& \Rightarrow 6 \text { numbers }\{(9,4),(8,5) \ldots(4,9)\}
\end{aligned}$
Similarly, for $3 a b, a+b=12 \Rightarrow 7$ numbers
For $4 a b, a+b=11 \Rightarrow$ Numbers
For $5 a b, a+b=10 \Rightarrow 9$ numbers
For $6 a b, a+b=9 \Rightarrow 10$ numbers
For $7 a b, a+b=8 \Rightarrow 9$ numbers
For $8 a b, a+b=7 \Rightarrow 8$ numbers
For $9 a b, a+b=6 \Rightarrow 7$ numbers
$\therefore$ Total ways $=64$.

</details>

---

### Q15. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of different 5 digit numbers greater than 50000 that can be formed using the digits 0 , $1,2,3,4,5,6,7$, such that the sum of their first and last digits should not be more than 8 , is

**Options:**

- **(A)** 4608
- **(B)** 5720
- **(C)** 5719
- **(D)** 4607

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4607**

**Detailed Solution:**

$\begin{array}{lll}
\text { Case I } & 5 \ldots \ldots & 0 \\
\text { Case II } & 5 \ldots \ldots & \\
& 5 & 1 \\
& 5 & 3 \\
& 6 & 0 \\
& 6 & 1 \\
& 6 & 2 \\
& 7 & 0 \\
& 7 & 1
\end{array}$

$9 \times(8 \times 8 \times 8)=4608$ but 50000 is not included, so total numbers $4608-1=4607$

</details>

---

### Q16. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of 3-digit numbers, formed using the digits $2,3,4,5$ and 7 , when the repetition of digits is not allowed, and which are not divisible by 3 , is equal to__________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

total number of three digit numbers not divisible by 3 will be formed by using the digits
$\begin{aligned}
& (4,5,7) \\
& (3,4,7) \\
& (2,5,7) \\
& (2,4,7) \\
& (2,4,5) \\
& (2,3,5) \\
& \text { number of ways }=6 \times 3 !=36
\end{aligned}$

</details>

---

### Q17. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If all the words with or without meaning made using all the letters of the word "NAGPUR" are arranged as in a dictionary, then the word at $315^{\text {th }}$ position in this arrangement is :

**Options:**

- **(A)** NRAGUP
- **(B)** NRAPUG
- **(C)** NRAPGU
- **(D)** NRAGPU

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) NRAPGU**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6Q7jUu9_0sKCHcr9-jG3UBzRah0n28mjps3IoA0Axc8.original.fullsize.png">

</details>

---

### Q18. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

A person forgets his <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>-digit ATM pin code. But he remembers that in the code all the digits are different, the greatest digit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> and the sum of the first two digits is equal to the sum of the last two digits. Then the maximum number of trials necessary to obtain the correct code is________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **72**

**Detailed Solution:**

<blockquote><p>Let the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>-</mo></math>digit pin be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mi>d</mi></math></p><p>Now given sum of first two is equal to last two, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mi>c</mi><mo>+</mo><mi>d</mi></math></p><p>And number available are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math></p><p>Now Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>=</mo><mi>&#955;</mi></math></p><p>Also the greatest digit that he has used is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>=</mo><mi>&#955;</mi><mo>&#8805;</mo><mn>7</mn></math></p><p>Now taking all cases starting from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>7</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and vice-versa, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>12</mn><mo>=</mo><mn>24</mn></math> numbers</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and vice versa so total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>8</mn><mo>=</mo><mn>16</mn></math> numbers,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>c</mi><mo>,</mo><mi>d</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and vice versa, so total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>8</mn><mo>=</mo><mn>16</mn></math> numbers,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mtext>so</mtext><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>&#8594;</mo><mn>8</mn></math> numbers</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>11</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mtext>so</mtext><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>&#8594;</mo><mn>8</mn></math> numbers</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mn>13</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>14</mn></math> are not possible,</p><p>So, Total numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>72</mn></math></p></blockquote>

</details>

---

### Q19. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The total number of three-digit numbers, divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, which can be formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></math>, if repetition of digits is allowed, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Three-digit number to be formed which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn></math> and repetition is allowed,</p><p>Now taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>, where all digits are same, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>&#8594;</mo><mn>4</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>Now taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo></math>digit are same and one is distinct, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>&#8594;</mo><mfrac><mrow><mn>3</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>3</mn><mo>&#160;</mo><mtext>ways,</mtext><mo>&#160;</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>&#8594;</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>Now taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math>, where all are distinct, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>&#8594;</mo><mn>6</mn><mtext>&#160;ways</mtext><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#8594;</mo><mn>6</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>So, total ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>22</mn></math></p></blockquote>

</details>

---

### Q20. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Total numbers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>-digit numbers that are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and can be formed by using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></math> with repetition, is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<blockquote><p>A number is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> when it is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> both.</p><p>The three digit number can be <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>a</mi><mo>&#175;</mo></munder><munder><mi>b</mi><mo>&#175;</mo></munder><munder><mn>2</mn><mo>&#175;</mo></munder></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>10</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>4</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>)</mo></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>)</mo></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>7</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo></math> can be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mn>5</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>5</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> </p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>10</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>)</mo></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>5</mn><mo>,</mo><mn>5</mn><mo>)</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> such cases when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> is at unit&#39;s place</p><p>Similarly, there exist <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> such cases when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> is at unit&#39;s place.</p><p>Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn></math> cases.</p><p>Hence this is the required answer.</p></blockquote>

</details>

---

### Q21. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

All words, with or without meaning, are made using all the letters of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>O</mi><mi>N</mi><mi>D</mi><mi>A</mi><mi>Y</mi></math>. These words are written as in a dictionary with serial numbers. The serial number of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>O</mi><mi>N</mi><mi>D</mi><mi>A</mi><mi>Y</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>327</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>328</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>324</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>326</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>327</mn></math>**

**Detailed Solution:**

<blockquote><p>The given word is MONDAY</p><p>Arranging the letters alphabetically, we get</p><p>ADMNOY</p><p>When the word starts with any of the letters A/D, the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>!</mo><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>240</mn></math></p><p>Now when the word starts with MA, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Now when the word starts with MD, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Now when the word starts with MN, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Now when the word starts with MOA, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></math></p><p>Now when the word starts with MOD, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></math></p><p>Now when the word starts with MONA, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>!</mo><mo>=</mo><mn>2</mn></math></p><p>Now when the word starts with MONDAY, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math></p><p>Rank <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>240</mn><mo>+</mo><mn>24</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>327</mn></math></p><p>Hence, rank of the word MONDAY is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>327</mn></math>.</p><p><strong>SHORTCUT METHOD</strong></p><p>Another method is a shortcut, first number the alphabet and then check how many number are there on right hand side less that number and then start number in factorial in decreasing order and then multiply and add them and in last add one to find rank, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mi>M</mi></mtd><mtd><mi>O</mi></mtd><mtd><mi>N</mi></mtd><mtd><mi>D</mi></mtd><mtd><mi>A</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>5</mn><mo>!</mo></mtd><mtd><mn>4</mn><mo>!</mo></mtd><mtd><mn>3</mn><mo>!</mo></mtd><mtd><mn>2</mn><mo>!</mo></mtd><mtd><mn>1</mn><mo>!</mo></mtd><mtd><mn>0</mn><mo>!</mo></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Rank <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>2</mn><mo>&#215;</mo><mn>5</mn><mo>!</mo><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>!</mo><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>!</mo><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>!</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>240</mn><mo>+</mo><mn>72</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>327</mn></math></p></blockquote>

</details>

---

### Q22. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the letters of the word MATHS are permuted and all possible words so formed are arranged as in a dictionary with serial numbers, then the serial number of the word THAMS is

**Options:**

- **(A)** <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>103</mn></math></p>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>102</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>104</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>103</mn></math></p>**

**Detailed Solution:**

<p>The given word is MATHS</p><p>Arranging the letters alphabetically, we get</p><p>AHMST</p><p>When the word starts with any of the letters A/H/M/S, the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>96</mn></math></p><p>Now when the word starts with TA, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></math></p><p>Now when the word starts with THAMS, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math></p><p>Rank <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>96</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>103</mn></math></p><p>Hence, rank of the work THAMS is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>103</mn></math>.</p>

</details>

---

### Q23. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

All the letters of the word PUBLIC are written in all possible orders and these words are written as in a dictionary with serial numbers. Then the serial number of the word PUBLIC is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>576</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>578</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>580</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>582</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>582</mn></math>**

**Detailed Solution:**

<blockquote><p>The given word is PUBLIC</p><p>Arranging the letters alphabetically, we get</p><p>BCILPU</p><p>When the word starts with any of the letters B/C/I/L, the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>!</mo><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>480</mn></math></p><p>Now when the word starts with PB, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Now when the word starts with PC, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Now when the word starts with PI, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Now when the word starts with PL, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Now when the word starts with PUBC, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>!</mo><mo>=</mo><mn>2</mn></math></p><p>Now when the word starts with PUBI, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>!</mo><mo>=</mo><mn>2</mn></math></p><p>Now when the word starts with PUBLC, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math></p><p>Now when the word starts with PUBLIC, then the number of possibilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math></p><p>Rank <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>480</mn><mo>+</mo><mn>24</mn><mo>&#215;</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>582</mn></math></p><p>Hence, rank of the work PUBLIC is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>582</mn></math>.</p></blockquote>

</details>

---

### Q24. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

The total number of six digit numbers, formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn></math> only and divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **81**

**Detailed Solution:**

<p>Given,</p><p>We have to form <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> digit number using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>9</mn></math> and for number should be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> which means that the addition of number should be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and unit place should be even, so we will make following cases:</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> The number is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>444444</mn></math> which can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> way,</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> when the number is formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn></math> and last place is fixed with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, that can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>20</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> when number is formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn></math> and last place is fixed with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, that can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> when number is formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>9</mn></math> and last place is fixed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, that can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>5</mn></mfenced></math> when number is formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>9</mn></math> and last place is fixed with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, that can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>30</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>6</mn></mfenced></math> when number is formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>9</mn></math> and last place is fixed with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, that can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>7</mn></mfenced></math> when number is formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn></math> and last place is fixed with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, that can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>Now adding all the cases we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>20</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>30</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>81</mn><mo>&#160;</mo><mtext>ways</mtext></math>.</p>

</details>

---

### Q25. JEE Main 2023 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers be constructed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></math> with repetition allowed, and are arranged in ascending order with serial numbers. Then the serial number of the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>42923</mn></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2997**

**Detailed Solution:**

<p>Number of five-digit numbers formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>9</mn></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> at the first place is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>1296</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>1296</mn></math></p><p>Number of five-digit numbers formed using the given digits with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> at the first place is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1296</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>1296</mn></math></p><p>Number of five-digit numbers formed using the given digits with  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math> at the first place is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>216</mn></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>216</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>420</mn><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="bottom"><mn>4</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>2</mn></menclose><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>423</mn><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>424</mn><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>427</mn><munder><mo>+</mo><mn>6</mn></munder><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>429</mn><mo>&#160;</mo><menclose notation="bottom"><mn>0</mn></menclose><munder><mo>+</mo><mn>6</mn></munder><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>429</mn><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mn>0</mn><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>429</mn><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mn>2</mn><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>429</mn><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mn>3</mn><mo>=</mo><mn>1</mn></math></p><p>Required serial number is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1296</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>216</mn><mo>+</mo><mn>5</mn><mo>&#215;</mo><mn>36</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>2997</mn></math></p>

</details>

---

### Q26. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The letters of the word OUGHT are written in all possible ways and these words are arranged as in a dictionary, in a series. Then the serial number of the word TOUGH is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>89</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>84</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>86</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>79</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>89</mn></math>**

**Detailed Solution:**

<p>Lets arrange the letters of OUGHT in alphabetical order.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>,</mo><mi mathvariant="normal">H</mi><mo>,</mo><mi mathvariant="normal">O</mi><mo>,</mo><mi mathvariant="normal">T</mi><mo>,</mo><mi mathvariant="normal">U</mi></math></p><p>Number of words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Number of words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Number of words starting with  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Number of words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>G</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn><mo>!</mo></math></p><p>Number of words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>H</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></math></p><p>Number of words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>O</mi><mi>G</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>!</mo><mo>=</mo><mn>2</mn></math></p><p>Number of words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>O</mi><mi>H</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>!</mo><mo>=</mo><mn>2</mn></math></p><p>Next word is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>TOUGH</mi></math>.</p><p>Hence, the serial number of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>TOUGH</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>+</mo><mn>24</mn><mo>+</mo><mn>24</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn><mspace linebreak="newline"/><mo>=</mo><mn>89</mn></math></p>

</details>

---

### Q27. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Five digit numbers are formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> with repetitions and are written in descending order with serial numbers. For example, the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>77777</mn></math> has serial number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>. Then the serial number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35337</mn></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1436**

**Detailed Solution:**

<p>Given,</p><p>Five digit numbers are formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> with repetitions and are written in descending order with serial numbers,</p><p>Now number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>625</mn></math></p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>625</mn></math></p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>125</mn></math></p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>125</mn></math></p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>25</mn></math></p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>351</mn></math> will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>25</mn></math></p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>352</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>25</mn></math></p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3531</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math></p><p>And number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers starting with digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3532</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math></p><p>And before <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35337</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> numbers, So rank of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35337</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1690</mn></math></p><p>So, in descending order serial number will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3125</mn><mo>-</mo><mn>1690</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>1436</mn></math></p>

</details>

---

### Q28. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

If all the six digit numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><msub><mi mathvariant="normal">x</mi><mn>4</mn></msub><msub><mi mathvariant="normal">x</mi><mn>5</mn></msub><msub><mi mathvariant="normal">x</mi><mn>6</mn></msub></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>4</mn></msub><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>5</mn></msub><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>6</mn></msub></math> are arranged in the increasing order, then the sum of the digits in the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>72</mn><mtext>th&#160;</mtext></msup></math> number is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

<p>Taking case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>2</mn></math> at first two places,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td> </td>			<td> </td>			<td> </td>			<td> </td>		</tr>	</tbody></table><p>So, other number can be selected in <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mo>=</mo><mn>35</mn></math> ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mtext>as&#160;number&#160;are&#160;from&#160;1-9</mtext></mfenced></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>3</mn></math> at first two place,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td> </td>			<td> </td>			<td> </td>			<td> </td>		</tr>	</tbody></table><p>So, other number can be selected in<math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>=</mo><mn>15</mn></math> ways</p><p>Similarly,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td> </td>			<td> </td>			<td> </td>			<td> </td>		</tr>	</tbody></table><p>So, other number can be selected in<math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>=</mo><mn>5</mn></math> ways</p><p>Now fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>5</mn></math> we get,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td> </td>			<td> </td>			<td> </td>			<td> </td>		</tr>	</tbody></table><p>Other number can be selected in<math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>=</mo><mn>1</mn></math></p><p>Now fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>3</mn></math> in first two place,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td> </td>			<td> </td>			<td> </td>			<td> </td>		</tr>	</tbody></table><p>So, other number can be selected in <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>=</mo><mn>15</mn></math></p><p>So, the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>72</mn><mrow><mi>n</mi><mi>d</mi></mrow></msup></math> number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>245678</mn></math></p><p>Hence, sum will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>32</mn></math></p>

</details>

---

### Q29. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The number of numbers, strictly between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5000</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10000</mn></math> can be formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></math> without repetition, is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>Numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></math></p><p>Now to form number between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5000</mn><mo>-</mo><mn>10000</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mrow><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></mrow></munder></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mrow><mn>4</mn><mo>&#160;</mo><mtext>ways</mtext></mrow></munder></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mrow><mn>3</mn><mo>&#160;</mo><mtext>ways</mtext></mrow></munder></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mrow><mn>2</mn><mo>&#160;</mo><mtext>ways</mtext></mrow></munder></mtd></mtr></mtable></math></p><p>Here at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn><mo>&#39;</mo><mtext>s</mtext></math> place should be taken by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>9</mn></math></p><p>So for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn><mo>&#39;</mo><mtext>s</mtext></math> place there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> ways,</p><p>Now for hundredth place there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> ways,</p><p>For ten&#39;s place there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> ways,</p><p>And for unit place there will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> ways,</p><p>So total ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>72</mn></math> ways.</p>

</details>

---

### Q30. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of integers, greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7000</mn></math> that can be formed, using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn></math> without repetition is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>168</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>168</mn></math>**

**Detailed Solution:**

<p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> </p><p>forming <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit number,</p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn><mo>&#39;</mo><mtext>s</mtext></math> place</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi></math>,</p><p>So total number of ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>24</mn></math> ways,</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> </p><p>forming <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit number when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn><mo>&#39;</mo><mtext>s</mtext></math> place </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi></math>,</p><p>So total number of ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>24</mn></math> ways,</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> </p><p>forming <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit number,</p><p>So total number of ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>!</mo><mo>=</mo><mn>120</mn></math> ways,</p><p>Now adding all the cases we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn><mo>+</mo><mn>24</mn><mo>+</mo><mn>24</mn><mo>=</mo><mn>168</mn></math> ways.</p>

</details>

---

### Q31. JEE Main 2022 (29 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of natural numbers lying between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1012</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>23421</mn></math> that can be formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></math> (repetition of digits is not allowed) and divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Given number should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit numbers between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1012</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>23421</mn></math> and can be formed using the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>6</mn></math> and should be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn></math></p><p><strong>CASE I: </strong>When number has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit, </p><p>Now for divisibility by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn></math>, number should be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> both</p><p>Also, for divisibility by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> for below figure,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8fee91e2-8cc9-493e-b730-aef8108b47b8-image.png" style="width: 181px; height: 70px;" /></p><p>Now fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mn>5</mn></math> the total possible cases for <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>6</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p><strong>CASE II:</strong></p><p>When number has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digits.</p><p>Let the number be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mi>d</mi><mi>e</mi></math>.</p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math> is fixed at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>. So the other <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digits must be from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn></math></p><p>No such number is possible because even the least number formed is greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>23421</mn></math>.</p><p>Hence, the total number of required numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math></p></blockquote>

</details>

---

### Q32. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Numbers are to be formed between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3000</mn></math>, which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> without repetition of digits. Then the total number of such numbers is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<blockquote><p>To find total numbers between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3000</mn></math> divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></math>,</p><p>We will solve in two cases.</p><p><strong>Case I :</strong> When first digit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.</p><p>Then last two digits can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>,</mo><mn>32</mn><mo>,</mo><mn>36</mn><mo>,</mo><mn>52</mn><mo>,</mo><mn>56</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math></p><p>So, total ways of choosing last two digit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and second digit will be chosen in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> ways</p><p>So, number of such numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>18</mn></math></p><p><strong>Case II:</strong> When first digit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p>Then last two digits can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>,</mo><mn>36</mn><mo>,</mo><mn>56</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math></p><p>So, total ways of choosing last two digit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> and second digit will be chosen in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> </p><p>So, number of such numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>12</mn></math></p><p>Total numbers of numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>18</mn><mo>+</mo><mn>12</mn><mo>=</mo><mn>30</mn></math></p></blockquote>

</details>

---

### Q33. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

The letters of the word &#39;MANKIND&#39; are written in all possible orders and arranged in serial order as in an English dictionary. Then the serial number of the word &#39;MANKIND&#39; is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1492**

**Detailed Solution:**

<blockquote><table border="1" cellpadding="1" cellspacing="1" style="width: 100px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">D</mi></math></td>		</tr>	</tbody></table><p>Arranging the letters alphabetically, we get</p><p>ADIKMNN</p><p>When the word starts with any of the letters A/D/I/K, the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>1440</mn></math></p><p>Now when the word starts with MA, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>36</mn></math></p><p>Now when the word starts with MAN, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>!</mo><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>12</mn></math></p><p>Now when the word starts with MANK, then the number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p><p>Hence, rank of the work MANKIND is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1492</mn></math></p></blockquote>

</details>

---

### Q34. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

The total number of three-digit numbers, with one digit repeated exactly two times, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **243**

**Detailed Solution:**

<p>For three digit number we have following cases,</p><p><strong>Case I:</strong> When digit zero is repeated</p><p>Number of numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mo>=</mo><mn>9</mn></math></p><p><strong>Case II:</strong> When digit zero is present but not repeated</p><p>Number of numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mo>&#183;</mo><mn>2</mn><mo>!</mo><mo>=</mo><mn>18</mn></math></p><p><strong>Case III:</strong> When digit zero is not present</p><p>Number of numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#183;</mo><mn>8</mn><mo>&#183;</mo><mfrac><mrow><mn>3</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>216</mn></math></p><p>Total number of numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>243</mn></math></p>

</details>

---

### Q35. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>-digit numbers which are multiples of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> and are formed using all the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **576**

**Detailed Solution:**

<p>Digits given are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></math></p><p>Now multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>&#8594;</mo></math> Difference of sum at even &amp; odd place should be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>.</p><p>Let number of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi><mi>d</mi><mi>e</mi><mi>f</mi><mi>g</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>b</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>f</mi></mrow></mfenced><mo>=</mo><mn>11</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>f</mi><mo>=</mo><mn>31</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> either <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>g</mi><mo>=</mo><mn>21</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>b</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>f</mi><mo>=</mo><mn>10</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math></p><p>Case-1</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>g</mi><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>f</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>,</mo><mi>d</mi><mo>,</mo><mi>f</mi></mrow></mfenced><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">a</mi><mo>,</mo><mi mathvariant="normal">c</mi><mo>,</mo><mi mathvariant="normal">e</mi><mo>,</mo><mi mathvariant="normal">g</mi></mrow></mfenced><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total number in case-1 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>3</mn><mo>!</mo><mo>&#215;</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><mo>!</mo></mrow></mfenced><mo>=</mo><mn>432</mn></math></p><p>Case-2</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>g</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>f</mi><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>e</mi><mo>,</mo><mi>g</mi></mrow></mfenced><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>b</mi><mo>,</mo><mi>d</mi><mo>,</mo><mi>f</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="}" open="{"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn></mrow></mfenced></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total number in case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>=</mo><mn>3</mn><mo>!</mo><mo>&#215;</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  Total numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>144</mn><mo>+</mo><mn>432</mn><mo>=</mo><mn>576</mn></math></p>

</details>

---

### Q36. JEE Main 2021 (01 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

All the arrangements, with or without meaning, of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>FARMER</mi></math> are written excluding any word that has two <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> appearing together. The arrangements are listed serially in the alphabetic order as in the English dictionary. Then the serial number of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>FARMER</mi></math> in this list is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **77**

**Detailed Solution:**

<p>Number of such words without both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> together</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> total possible words - total possible words with both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> together</p><p>Number of such words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>36</mn></math></p><p>Number of such words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>36</mn></math></p><p>Number of such words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>FAE</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mn>2</mn><mo>=</mo><mn>1</mn></math></p><p>Number of such words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>FAM</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mn>2</mn><mo>=</mo><mn>1</mn></math></p><p>Number of such words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>FARE</mi><mo>=</mo><mn>2</mn><mo>!</mo><mo>=</mo><mn>2</mn></math></p><p>Number of such words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>FARMER</mi><mo>=</mo><mn>1</mn></math></p><p>Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>77</mn></math></p>

</details>

---

### Q37. JEE Main 2021 (31 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>-digit numbers which are neither multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> nor multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> is <u>           </u> .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5143**

**Detailed Solution:**

<p>The total possible <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit numbers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>9000</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit number divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1002</mn><mo>,</mo><mo>&#160;</mo><mn>1005</mn><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mo>&#160;</mo><mn>9999</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1002</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>9999</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9999</mn><mo>=</mo><mn>1002</mn><mo>+</mo><mfenced><mrow><msub><mi>n</mi><mn>3</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>3</mn></msub><mo>=</mo><mn>3000</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> is the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit numbers divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1001</mn><mo>,</mo><mn>1008</mn><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mo>&#160;</mo><mn>9996</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1001</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>9996</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9996</mn><mo>=</mo><mn>1001</mn><mo>+</mo><mfenced><mrow><msub><mi>n</mi><mn>7</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>7</mn></msub><mo>=</mo><mn>1286</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit numbers divisible by both <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1008</mn><mo>,</mo><mn>1029</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>9996</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1008</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>21</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>9996</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9996</mn><mo>=</mo><mn>1008</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>429</mn></math></p><p>Hence,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> digit numbers neither divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9000</mn><mo>-</mo><mn>1286</mn><mo>-</mo><mn>3000</mn><mo>+</mo><mn>429</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5143</mn></math></p>

</details>

---

### Q38. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn><mo>}</mo></math>. Then the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mo>{</mo><mi>A</mi><mo>&#8838;</mo><mi>S</mi><mo>:</mo><mi>A</mi><mo>&#8800;</mo><mi>&#981;</mi></math> and the sum of all the elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is not a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>}</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **80**

**Detailed Solution:**

<p>We can categorise the numbers of set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><munder><munder><mrow><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn></mrow><mo>&#9183;</mo></munder><mrow><mo>&#160;</mo><mn>3</mn><mi>n</mi><mtext>&#160;type</mtext></mrow></munder><mo>,</mo><mo>&#160;</mo><munder><munder><mrow><mn>2</mn><mo>,</mo><mn>5</mn></mrow><mo>&#9183;</mo></munder><mrow><mo>&#160;</mo><mn>3</mn><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mtext>&#160;type</mtext></mrow></munder><mo>&#160;</mo><mo>&#160;</mo><mo>,</mo><munder><munder><mrow><mn>1</mn><mo>,</mo><mn>4</mn></mrow><mo>&#9183;</mo></munder><mrow><mo>&#160;</mo><mn>3</mn><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mtext>&#160;type</mtext></mrow></munder><mo>}</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"/></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mi>p</mi></msub><mo>=</mo></math>Number of subsets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> elements which are not divisible by<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><msub><mi>N</mi><mn>1</mn></msub><mo>)</mo><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>=</mo><mn>4</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><msub><mi>N</mi><mn>2</mn></msub><mo>)</mo><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>=</mo><mn>14</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>3</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><msub><mi>N</mi><mn>3</mn></msub><mo>)</mo><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>=</mo><mn>22</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>4</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><msub><mi>N</mi><mn>4</mn></msub><mo>)</mo><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mfenced open="[" close="]"><mrow><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced></mrow></mfenced><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced><mo>=</mo><mn>22</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>5</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><msub><mi>N</mi><mn>5</mn></msub><mo>)</mo><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mfenced open="[" close="]"><mrow><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><msub><mmultiscripts><mi mathvariant="normal">C</mi><mprescripts/><none/><mn>2</mn></mmultiscripts><mn>2</mn></msub></mrow></mfenced></mrow></mfenced><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced><mo>=</mo><mn>14</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>6</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><msub><mi>N</mi><mn>6</mn></msub><mo>)</mo><mo>=</mo><mfenced open="" close="]"><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mfenced open="["><mrow><mo>(</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Total subsets satisfying given condition <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>22</mn><mo>+</mo><mn>22</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>80</mn></math></p>

</details>

---

### Q39. JEE Main 2021 (27 Aug Shift 1)

*Type:* `numerical` | *Level:* `3`

A number is called a palindrome if it reads the same backward as well as forward. For example <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>285582</mn></math> is a six digit palindrome. The number of six digit palindromes, which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn><mo>,</mo></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **100**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d902ff78-af96-41d8-9b3e-7c9aaaed4e36-image-alt.png" style="width: 256px; height: 66px;" /></p><p>Palindrome Numbers only in this form will be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn></math>.</p><p>Numbers can be  between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mn>9</mn></math></p><p>Number of ways of selecting value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mmultiscripts><mi>P</mi><mprescripts></mprescripts><mn>1</mn><mn>10</mn></mmultiscripts></math></p><p>Similarly  number of ways of choosing value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mmultiscripts><mi>P</mi><mprescripts></mprescripts><mn>1</mn><mn>10</mn></mmultiscripts></math>  (As a and b can also be same)</p><p>Therefore, Total number of ways of getting palindrome numbers divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>100</mn></math></p></blockquote>

</details>

---

### Q40. JEE Main 2021 (26 Aug Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of three-digit even numbers, formed by the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></math> if the repetition of digits is not allowed, is______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **52**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></math></p><p>For three-digit even number, it must end with either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></math></p><p>The number of three -digit even numbers ending with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>20</mn></math></p><p>The number of three -digit even numbers ending with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>16</mn></math> </p><p>The number of three -digit even numbers ending with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>16</mn></math></p><p> Total three digits even numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>16</mn><mo>=</mo><mn>52</mn></math></p>

</details>

---

### Q41. JEE Main 2020 (04 Sep Shift 2)

*Type:* `numerical` | *Level:* `3`

A test consists of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> multiple choice questions, each having <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> alternative answers of which only one is correct. The number of ways, in which a candidate answers all six questions such that exactly four of the answers are correct, is ___________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **135**

**Detailed Solution:**

<p>No. of ways of giving wrong answer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math></p><p>So, required no. of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>(</mo><mn>1</mn><msup><mo>)</mo><mn>4</mn></msup><mo>&#215;</mo><mo>(</mo><mn>3</mn><msup><mo>)</mo><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>15</mn><mo>(</mo><mn>9</mn><mo>)</mo><mo>=</mo><mn>135</mn></math></p>

</details>

---

### Q42. JEE Main 2020 (02 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

If the letters of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mo>&#39;</mo></msup><msup><mi>MOTHER</mi><mo>&#39;</mo></msup></math> be permuted and all the words so formed (with or without meaning) be listed as in a dictionary, then the position of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mo>'</mo></msup><msup><mi>MOTHER</mi><mo>'</mo></msup></math> is.....

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **309**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mo>'</mo></msup><msup><mi>MOTHER</mi><mo>'</mo></msup></math></p><p>Rearrange in alphabetic order <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>EHMORT</mi></math></p><p>Number of words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">E</mi><mo>=</mo><mn>5</mn><mo>!</mo></math></p><p>Number of words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">H</mi><mo>=</mo><mn>5</mn><mo>!</mo></math></p><p>Number of words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ME</mi><mo>=</mo><mn>4</mn><mo>!</mo></math></p><p>Number of words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>MH</mi><mo>=</mo><mn>4</mn><mo>!</mo></math></p><p>Number of words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>MOE</mi><mo>=</mo><mn>3</mn><mo>!</mo></math></p><p>Number of words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>MOH</mi><mo>=</mo><mn>3</mn><mo>!</mo></math></p><p>Number of words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>MOR</mi><mo>=</mo><mn>3</mn><mo>!</mo></math></p><p>Number of words start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>MOTE</mi><mo>=</mo><mn>2</mn><mo>!</mo></math></p><p>Number of word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>MOTHER</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>5</mn><mo>!</mo><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>!</mo><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>!</mo><mo>+</mo><mn>2</mn><mo>!</mo><mo>+</mo><mn>1</mn><mo>=</mo><mn>240</mn><mo>+</mo><mn>48</mn><mo>+</mo><mn>18</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>309</mn></math></p>

</details>

---

### Q43. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the number of five digit numbers with distinct digits and <math><mn>2</mn></math> at the <math><msup><mrow><mn>10</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> place is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>336</mn><mi>k</mi></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to:

**Options:**

- **(A)** <math><mn>4</mn></math>
- **(B)** <math><mn>6</mn></math>
- **(C)** <math><mn>7</mn></math>
- **(D)** <math><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>8</mn></math>**

**Detailed Solution:**

<table border="1px solid">	<tbody>		<tr>			<td> </td>			<td> </td>			<td> </td>			<td>2</td>			<td> </td>		</tr>	</tbody></table>
Total Number of numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>2688</mn><mo>=</mo><mn>336</mn><mi>k</mi><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>8</mn></math>

</details>

---

### Q44. JEE Main 2020 (08 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

An urn contains <math><mn>5</mn></math> red marbles, <math><mn>4</mn></math> black marbles and <math><mn>3</mn></math> white marbles. Then, the number of ways in which <math><mn>4</mn></math> marbles can be drawn so that at the most three of them are red is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **490**

**Detailed Solution:**

<p>We have,<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>  red,<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> black, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> white marbles
Required number of ways </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>7</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>7</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>7</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>7</mn></mmultiscripts><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8203;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>35</mn><mo>+</mo><mn>175</mn><mo>+</mo><mn>210</mn><mo>+</mo><mn>70</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>490</mn></math></p>

</details>

---

### Q45. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>6</mn></math> digit number that can be formed using the digits <math><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn><mo>,</mo><mi>&#160;</mi><mn>7</mn></math> and <math><mn>9</mn></math> which are divisible by <math><mn>11</mn></math> and no digit is repeated is:

**Options:**

- **(A)** <math><mn>36</mn></math>
- **(B)** <math><mn>60</mn></math>
- **(C)** <math><mn>72</mn></math>
- **(D)** <math><mn>48</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>60</mn></math>**

**Detailed Solution:**

<p>Only one possibility is there, <math><mo>(</mo><mn>9,1</mn><mo>,</mo><mn>2</mn><mo>)</mo></math> or <math><mo>(</mo><mn>0,5</mn><mo>,</mo><mn>7</mn><mo>)</mo></math> as in even or odd places
<math><mo>&#8756;</mo></math> Total number of required <math><mn>6</mn></math> digit numbers</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>9</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></math> in odd and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></math> in even places<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>9</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></math> in even places and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></math> in odd places<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math>
<math><mo>=</mo><mn>3</mn><mo>!</mo><mo>&#215;</mo><mn>3</mn><mo>!</mo><mo>+</mo><mfenced separators="|"><mrow><mn>3</mn><mo>!</mo><mi>&#160;</mi><mo>&#8211;</mo><mn>2</mn></mrow></mfenced><mo>&#215;</mo><mn>3</mn><mo>!</mo></math>
<math><mo>=</mo><mn>36</mn><mo>+</mo><mn>24</mn></math>
<math><mo>=</mo><mn>60</mn></math></p>

</details>

---

### Q46. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

All possible numbers are formed using the digits <math><mn>1</mn><mo>,</mo><mi> </mi><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>,</mo><mi> </mi><mn>4</mn><mo>,</mo><mi> </mi><mn>4</mn><mi> </mi></math> taken all at a time. The number of such numbers in which the odd digits occupy even places is

**Options:**

- **(A)** <math><mn>175</mn></math>
- **(B)** <math><mn>162</mn></math>
- **(C)** <math><mn>180</mn></math>
- **(D)** <math><mn>160</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>180</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1aec8f06-15ca-4bbd-b70a-865b9b6bd459-image2.png" />
Odd digits: <math><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn></math>
Even digits: <math><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>4</mn></math>
The number of ways of placing odd digits at even position <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>4</mn></mmultiscripts><mo>&#215;</mo><mfrac><mrow><mn>3</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>12</mn></math>
The number of ways of placing even digits <math><mo>=</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo><mi>&#160;</mi><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>15</mn><mi>&#160;</mi></math>
<math><mo>&#8756;</mo></math> Total number of ways <math><mo>=</mo><mn>12</mn><mo>&#215;</mo><mn>15</mn><mo>=</mo><mn>180</mn></math>

</details>

---

### Q47. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of natural numbers less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7000</mn></math> which can be formed by using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mo>,</mo><mi>&#160;</mi><mn>7</mn><mo>,</mo><mi>&#160;</mi><mn>9</mn></math> (repetition of digits allowed) is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>375</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>374</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>372</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>374</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ntgzqpganfsgqigrgpyxevugezxqfavxuoaovnyenmmwafbpho.png" />

<math><mo>&#8756;</mo></math> Total number formed less than</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7000</mn><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>375</mn></math></p><p><math><mo>&#8756;</mo></math> Total natural number formed less than</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7000</mn><mo>=</mo><mn>375</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>374</mn></math></p><p>(number zero has been excluded)</p>

</details>

---

### Q48. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be two sets containing four and two elements respectively. Then the number of subsets of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#215;</mo><mi>B</mi></math>, each having at least three elements is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>510</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>219</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>256</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>275</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>219</mn></math>**

**Detailed Solution:**

<p>Given <math><mi>n</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math><mi>n</mi><mfenced separators="|"><mrow><mi>B</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>Number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mi>&#160;</mi><mo>&#215;</mo><mi>&#160;</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>8</mn></math></p><p>Number of subsets<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>8</mn></msup></math></p><p>Number of subsets having less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> elements <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>8</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mo>+</mo><msub><mmultiscripts><mi>C</mi><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mn>1</mn></msub><mo>+</mo><msub><mmultiscripts><mi>C</mi><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mn>2</mn></msub></math></p><p>Number of subsets having at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> elements
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>8</mn></msup><msup><mo>-</mo><mn>8</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mo>-</mo><msub><mmultiscripts><mi>C</mi><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mn>1</mn></msub><mo>-</mo><msub><mmultiscripts><mi>C</mi><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mn>2</mn></msub></math></p><p><math><mo>=</mo><mn>256</mn><mo>-</mo><mn>1</mn><mo>-</mo><mn>8</mn><mo>-</mo><mn>28</mn></math></p><p><math><mo>=</mo><mn>219</mn></math></p>

</details>

---

