# BITSAT Mathematics - Permutation Combination

## Topic 4: Arrangement under Constraint

**Total Questions:** 4

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `1`

How many different nine digit numbers can be formed from the number 223355888 by rearranging its digits so that the odd digits occupy even positions

**Options:**

- **(A)** 16
- **(B)** 36
- **(C)** 60
- **(D)** 100

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 60**

**Detailed Solution:**

Here we have 4 odd digits $(3,3,5,5)$ and 5 even digits (2, 2, 8, 8, 8).
$\bar{O} \bar{E} \bar{O} \bar{E} \bar{O} \bar{O} \bar{E} \bar{O}$
where, $E \rightarrow$ even place and $O \rightarrow$ odd place
$\Rightarrow$ Number of ways odd digits will be place on even places
$=\frac{4!}{2!2!}$
Number of ways even digits will be place on odd places
$\begin{aligned}
& \quad=\frac{5!}{2!3!} \\
& \therefore \text { Total number of ways }=\frac{4!}{2!2!} \times \frac{5!}{2!3!}=60
\end{aligned}$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Number of words from the letters of the words BHARAT in which $B$ and $\mathrm{H}$ will never come together is

**Options:**

- **(A)** 210
- **(B)** 240
- **(C)** 422
- **(D)** 400

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 240**

**Detailed Solution:**

There are 6 letters in the word BHARAT, 2 of them are identical. Hence total number of words $=6 ! / 2 !=360$
Number of words in which $B$ and $\mathrm{H}$ come together
$=\frac{5 ! 2 !}{2 !}=120$
final ans $=360-120=240$

</details>

---

### Q3. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `1`

The number of ways of arranging letters of the word HAVANA so that $\mathrm{V}$ and $\mathrm{N}$ do not appear together is

**Options:**

- **(A)** 40
- **(B)** 60
- **(C)** 80
- **(D)** 100

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 80**

**Detailed Solution:**

We can arrange the letters $\mathrm{H}, \mathrm{A}, \mathrm{A}, \mathrm{A}$ in $\frac{4 !}{3 !}=4$ ways. If one possible arrangement is
$$
X X X X
$$
Then, we can arrange $\mathrm{V}, \mathrm{N}$ at any of the two places marked with $\mathrm{O}$ in the following arrangement
$$
\mathrm{O} \times \mathrm{O} \times \mathrm{O} \times \mathrm{O} \times \mathrm{O}
$$
Thus, we can arrange $V$ and $N$ in ${ }^5 P_2=20$ ways. Thus, the number of ways in which letters can be arranged is $4 \times 20=80$

</details>

---

### Q4. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `2`

A person invites a party of 10 friends at dinner and place them so that 4 are on one round table and 6 on the other round table. The number of ways in which he can arrange the guests is

**Options:**

- **(A)** $\frac{(10) !}{6 !}$
- **(B)** $\frac{(10) !}{24}$
- **(C)** $\frac{(9) !}{24}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{(10) !}{24}$**

**Detailed Solution:**

Selection of 6 guests $=10 \mathrm{C} 6$ 

Permutation of 6 on round table $=5 !$ 

Permutation of 4 on round table $=3 !$

Then, total number of arrangements $=10 \mathrm{C} 6.5 ! .3 !$

$=\frac{(10) !}{6 ! 4 !} \cdot 5 ! .3 !=\frac{(10) !}{24}$

</details>

---

