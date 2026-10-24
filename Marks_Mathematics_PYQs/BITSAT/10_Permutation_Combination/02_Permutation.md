# BITSAT Mathematics - Permutation Combination

## Topic 2: Permutation

**Total Questions:** 10

---

### Q1. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of arrangements of all digits of 12345 such that at least 3 digits will not come in its position is

**Options:**

- **(A)** $89$
- **(B)** $109$
- **(C)** $78$
- **(D)** $57$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $109$**

**Detailed Solution:**

Total number of ways such that at least 3 digits will not come in its position
$={ }^5 C_3\left\{3!-{ }^3 C_1 2!+{ }^3 C_2 1!-{ }^3 C_3 0!\right\}$
$+{ }^5 C_4\left\{4!-{ }^4 C_1(3!)+{ }^4 C_2(2!)-{ }^4 C_3(1!)+{ }^4 C_4\right.(0!)\}$
$+{ }^5 C_4\left\{5!-{ }^5 C_1 4!+{ }^5 C_7 3!-{ }^5 C_2 2!+{ }^5 C_4 1!-\right.\left.{ }^5 C_5(0!)\right\}$
$=10(2)+5(9)+(44)=20+45+44=109$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

How many different nine digit numbers can be formed from the number 223355888 by rearranging its digits so that the odd digits occupy even positions?

**Options:**

- **(A)** 16
- **(B)** 36
- **(C)** 60
- **(D)** 180

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 60**

**Detailed Solution:**

$\mathrm{X}-\mathrm{X}-\mathrm{X}-\mathrm{X}-\mathrm{X}$. The four digits 3, 3, 5,5 can be arranged at $(-)$ places in $\frac{4 !}{2 ! 2 !}=6$ ways. The five digits $2,2,8,8,8$ can be arranged at $(X)$ places in $\frac{5 !}{2 ! 3 !}$ ways $=10$ ways
Total no. of arrangements $=6 \times 10=60$ ways

</details>

---

### Q3. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

The number of different seven-digit numbers that can be written using only the three digit 1 , 2 and 3 with the condition that the digit 2 occurs twice in each number is

**Options:**

- **(A)** ${ }^7 C_2 2^5$
- **(B)** ${ }^7 p_2 2^5$
- **(C)** ${ }^7 C_2 5^2$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) ${ }^7 C_2 2^5$**

**Detailed Solution:**

Other than 2, remaining five places can be filled by 1 and 3 for each place. The number of ways for five places is $2 \times 2 \times 2 \times 2 \times 2=2^5$. For 2 , selecting 2 places out of 7 is ${ }^7 C_2$. Hence, the required number of ways is ${ }^7 C_2 \times 2^5$.

</details>

---

### Q4. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `2`

How many numbers lying between 999 and 10000 can be formed with the help of the digits $0,2,3,6,7,8$, when the digits are not repeated?

**Options:**

- **(A)** 100
- **(B)** 200
- **(C)** 300
- **(D)** 400

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 300**

**Detailed Solution:**

The numbers between 999 and 10000 are all 4-digit numbers. The number of 4 - digit numbers formed by digits $0,2,3,6,7,8$ is ${ }^{6} \mathrm{P}_{4}=360$. But here those numbers are also involved which begin from 0 . So, we take those numbers as three-digit numbers.

Taking initial digit 0 , the number of ways to fill remaining 3 places from five digits $2,3,6,7,8$ are ${ }^{5} \mathrm{P}_{3}=60$

So, the required numbers $=360-60=300$.

</details>

---

### Q5. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `2`

The number of possible outcomes in a throw of n ordinary dice in which at least one of the dice shows an odd number is

**Options:**

- **(A)** $6^{n}-1$
- **(B)** $3^{n}-1$
- **(C)** $6^{n}-3^{n}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6^{n}-3^{n}$**

**Detailed Solution:**

Total number of ways $=6 \times 6 \times \ldots \ldots$ to $n$ times $=6^{n}$ Total number of ways to show only even number $=3 \times 3 \times \ldots \ldots$ to $n$ times $=3^{n}$

$\therefore$ required number of ways $=6^{\mathrm{n}}-3^{\mathrm{n}}$

</details>

---

### Q6. BITSAT 2018

*Type:* `singleCorrect` | *Level:* `2`

If a parallelogram is cut by two sets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> lines parallel to its sides, then the number of parallelogram thus formed, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>m</mi></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>m</mi></mmultiscripts></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts></mfenced><mn>2</mn></msup></math>
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts></mfenced><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>The two sets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> parallel lines along with two sets of two parallel lines of the given parallelogram will form two sets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math> parallel lines. Each parallelogram is formed by choosing two parallel lines from each of the above</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total number of parallelograms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts><mo>=</mo><msup><mfenced><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts></mfenced><mn>2</mn></msup></math></p><p>Hence, option (c) is correct.</p>

</details>

---

### Q7. BITSAT 2016

*Type:* `singleCorrect` | *Level:* `1`

All the words that can be formed using alphabets A, $H, L, U$ and $R$ are written as in a dictionary (no alphabet is repeated). Rank of the word RAHUL is

**Options:**

- **(A)** 71
- **(B)** 72
- **(C)** 73
- **(D)** 74

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 74**

**Detailed Solution:**

No. of words starting with $\mathrm{A}$ are $4 !=24$

No. of words starting with $\mathrm{H}$ are $4 !=24$

No. of words starting with $L$ are $4 !=24$

These account for 72 words Next word is RAHLU and the $74^{\text {th }}$ word RAHUL

</details>

---

### Q8. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `2`

In a polygon no three diagonals are concurrent. If the total number of points of intersection of diagonals interior to the polygon be 70 then the number of diagonals of the polygon is

**Options:**

- **(A)** 20
- **(B)** 28
- **(C)** 8
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 20**

**Detailed Solution:**

A combination of four vertices is equivalent to one interior point of intersection of diagonals.
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/rPkMaoMA84X7jjk_MZSrQoolKg3Y1oDMudbyYmES1nc.original.fullsize.png">

\(\therefore\) No. of interior points of intersection
\(\begin{aligned}
& ={ }^{\mathrm{n}} \mathrm{C}_4=70 \\
& \Rightarrow \mathrm{n}(\mathrm{n}-1)(\mathrm{n}-2)(\mathrm{n}-3)=5.6 .7 .8 \\
& \therefore \mathrm{n}=8
\end{aligned}\)
So, number of diagonals \(={ }^8 \mathrm{C}_2-8=20\)

</details>

---

### Q9. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `2`

If \(\frac{1-i \alpha}{1+i \alpha}=A+i B\), then \(A^2+B^2\) equals to

**Options:**

- **(A)** 1
- **(B)** \(\alpha^2\)
- **(C)** -1
- **(D)** \(-\alpha^2\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

\(\begin{aligned}
& A+i B=\frac{1-i \alpha}{1+i \alpha} \Rightarrow A-i B=\frac{1+i \alpha}{1-i \alpha} \\
& \Rightarrow(A+i B)(A-i B)=\frac{(1-i \alpha)(1+i \alpha)}{(1+i \alpha)(1-i \alpha)}=1 \\
& \Rightarrow A^2+B^2=1
\end{aligned}\)

</details>

---

### Q10. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `2`

If \(\frac{2 x+3}{5}  < \frac{4 x-1}{2}\), then \(x\) lies in the interval

**Options:**

- **(A)** \(\left[0, \frac{11}{16}\right)\)
- **(B)** \(\left[\frac{11}{16}, \infty\right)\)
- **(C)** \(\left(0, \frac{11}{16}\right)\)
- **(D)** \(\left(\frac{11}{16}, \infty\right)\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) \(\left(\frac{11}{16}, \infty\right)\)**

**Detailed Solution:**

\(\begin{aligned}
& \frac{2 x+3}{5}  < \frac{4 x-1}{2} \Rightarrow-16 x < -11 \\
& \Rightarrow 16 x > 11 \Rightarrow x > \frac{11}{16} \\
& \text { Hence, } x \in\left(\frac{11}{16}, \infty\right)
\end{aligned}\)

</details>

---

