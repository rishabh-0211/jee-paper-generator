# MHT CET Mathematics - Permutation Combination

## Topic 6: Selection of one or more item

**Total Questions:** 4

---

### Q1. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A bag contains 23 balls, of which 7 are identical. The number of ways of selecting 12 balls from the bag is....

**Options:**

- **(A)** ${}^{18}C_6 + {}^{18}C_8$
- **(B)** ${}^{18}C_7 + {}^{19}C_8$
- **(C)** ${}^{16}C_8 + {}^{18}C_{15}$
- **(D)** ${}^{16}C_8 + {}^{18}C_9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) ${}^{18}C_6 + {}^{18}C_8$**

**Detailed Solution:**

Total number of balls = $23$
Number of identical balls = $7$
Number of distinct balls = $23 - 7 = 16$

We need to select $12$ balls. Let the number of identical balls selected be $k$, where $0 \le k \le 7$.
The remaining $12 - k$ balls must be selected from the $16$ distinct balls. The number of ways to do this is ${}^{16}C_{12-k}$.

The total number of ways to select $12$ balls is the sum of these possibilities for $k = 0$ to $7$:
$S = \sum_{k=0}^{7} {}^{16}C_{12-k}$
$S = {}^{16}C_{12} + {}^{16}C_{11} + {}^{16}C_{10} + {}^{16}C_{9} + {}^{16}C_{8} + {}^{16}C_{7} + {}^{16}C_{6} + {}^{16}C_{5}$

Using the property ${}^{n}C_{r} = {}^{n}C_{n-r}$, we can rewrite the first four terms:
${}^{16}C_{12} = {}^{16}C_{4}$
${}^{16}C_{11} = {}^{16}C_{5}$
${}^{16}C_{10} = {}^{16}C_{6}$
${}^{16}C_{9} = {}^{16}C_{7}$

Substituting these back into the sum:
$S = {}^{16}C_{4} + {}^{16}C_{5} + {}^{16}C_{6} + {}^{16}C_{7} + {}^{16}C_{8} + {}^{16}C_{7} + {}^{16}C_{6} + {}^{16}C_{5}$

Rearranging and grouping the terms:
$S = ({}^{16}C_{4} + {}^{16}C_{5}) + ({}^{16}C_{5} + {}^{16}C_{6}) + ({}^{16}C_{6} + {}^{16}C_{7}) + ({}^{16}C_{7} + {}^{16}C_{8})$

Using Pascal's identity ${}^{n}C_{r} + {}^{n}C_{r-1} = {}^{n+1}C_{r}$:
$S = {}^{17}C_{5} + {}^{17}C_{6} + {}^{17}C_{7} + {}^{17}C_{8}$

Grouping again:
$S = ({}^{17}C_{5} + {}^{17}C_{6}) + ({}^{17}C_{7} + {}^{17}C_{8})$
$S = {}^{18}C_{6} + {}^{18}C_{8}$

Answer: ${}^{18}C_6 + {}^{18}C_8$

</details>

---

### Q2. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Total number of 3-digit numbers, whose g.c.d with 36 is 2 , is

**Options:**

- **(A)** $140$
- **(B)** $150$
- **(C)** $165$
- **(D)** $170$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $150$**

**Detailed Solution:**

Let the 3-digit number be $N$. The range of 3-digit numbers is $100 \le N \le 999$.

We are given $\gcd(N, 36) = 2$. Since $36 = 2^2 \times 3^2$, this condition implies:
1. $N$ must be divisible by $2$.
2. $N$ must not be divisible by $2^2 = 4$.
3. $N$ must not be divisible by $3$.

Let $N = 2k$, where $k$ is an integer. 
For $N$ to not be divisible by $4$, $k$ must not be divisible by $2$ (i.e., $k$ is odd).
For $N$ to not be divisible by $3$, $k$ must not be divisible by $3$.
Thus, $k$ must be coprime to $6$, which means $\gcd(k, 6) = 1$.

Substituting $N = 2k$ into the range of 3-digit numbers:
$100 \le 2k \le 999$
$50 \le k \le 499.5$

Since $k$ is an integer, $k$ takes values from $50$ to $499$.
The total number of integers in this range is $499 - 50 + 1 = 450$.

In any block of $6$ consecutive integers, there are exactly $\phi(6) = 2$ integers that are coprime to $6$ (specifically, those congruent to $1$ and $5$ modulo $6$).

Since $450$ is an exact multiple of $6$ ($450 = 6 \times 75$), the number of blocks of $6$ integers is $75$.

Therefore, the total number of valid values for $k$ (and hence for $N$) is:
$75 \times 2 = 150$

Answer: $150$

</details>

---

### Q3. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A linguistic club consists of 6 girls and 4 boys. A team of 4 members is to be selected from this group including the selection of a leader (from among these 4 members) for the team. If the team has to include at most one boy, the number of ways of selecting the team is

**Options:**

- **(A)** $140$
- **(B)** $320$
- **(C)** $76$
- **(D)** $380$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $380$**

**Detailed Solution:**

Case I: No boy is included.
Selecting 4 girls from 6 girls $={ }^6 \mathrm{C}_4$
Selecting 1 captain from selected members $={ }^4 \mathrm{C}_1$

Total number of ways $={ }^6 \mathrm{C}_4 \times{ }^4 \mathrm{C}_1=60$
Case II: One boy is included.
Selecting 3 girls and 1 boy from given members $={ }^6 \mathrm{C}_3 \times{ }^4 \mathrm{C}_1$.

Selecting 1 captain from the selected members $={ }^4 \mathrm{C}_1$.

Total Number of ways $={ }^6 \mathrm{C}_3 \times{ }^4 \mathrm{C}_1 \times{ }^4 \mathrm{C}_1=320$.
$\therefore \quad$ Total Number of ways $=320+60=380$.

</details>

---

### Q4. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A committee of 5 is to be formed out of 6 men and 4 ladies. The number of ways this can be done, when at most 2 ladies are include, is

**Options:**

- **(A)** 240
- **(B)** 186
- **(C)** 60
- **(D)** 120

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 186**

**Detailed Solution:**

The committee can be formed in following ways:
( 5 men), (4 men, 1 lady) , (3 men, 2 ladies)
$\begin{aligned}
& \therefore \text { Number of was }=\left({ }^6 \mathrm{C}_5\right)+\left({ }^6 \mathrm{C}_4 \times{ }^4 \mathrm{C}_1\right)+\left({ }^6 \mathrm{C}_3 \times{ }^4 \mathrm{C}_2\right) \\
& =(6)+(15 \times 4)+(20 \times 6)=6+60+120=186
\end{aligned}$

</details>

---

