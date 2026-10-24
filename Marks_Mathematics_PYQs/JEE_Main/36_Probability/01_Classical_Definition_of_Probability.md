# JEE Main Mathematics - Probability

## Topic 1: Classical Definition of Probability

**Total Questions:** 78

---

### Q1. JEE Main 2026 (04 April Shift 2)

*Type:* `numerical` | *Level:* `2`

From a month of $31$ days, $3$ different dates are selected at random. If the probability that these dates are in an increasing A.P. is equal to $\dfrac{a}{b}$, where $a,b \in \mathbb{N}$ and $\gcd(a,b)=1$, then $a+b$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **944**

**Detailed Solution:**

The total number of ways to select $3$ different dates from a month of $31$ days is given by choosing $3$ days out of $31$:

$^{31}C_{3} = \dfrac{31 \times 30 \times 29}{3 \times 2 \times 1} = 4495$

Let the three selected dates be $x, y, z$ such that $x < y < z$. For these dates to form an increasing Arithmetic Progression (A.P.), they must satisfy the condition:

$2y = x + z$

For $y$ to be an integer, the sum $x + z$ must be an even number. This is only possible if both $x$ and $z$ are either odd or even. Once $x$ and $z$ are chosen, $y$ is uniquely determined as their exact average.

In a month of $31$ days, the number of odd dates ($1, 3, 5, \dots, 31$) is $16$, and the number of even dates ($2, 4, 6, \dots, 30$) is $15$.

The number of ways to choose $x$ and $z$ such that both are odd is:

$^{16}C_{2} = \dfrac{16 \times 15}{2} = 120$

The number of ways to choose $x$ and $z$ such that both are even is:

$^{15}C_{2} = \dfrac{15 \times 14}{2} = 105$

The total number of favorable selections that form an increasing A.P. is:

$120 + 105 = 225$

The probability that the selected dates are in an increasing A.P. is:

$P = \dfrac{225}{4495}$

Dividing the numerator and the denominator by $5$, we get:

$P = \dfrac{45}{899}$

Since $45 = 3^2 \times 5$ and $899 = 29 \times 31$, they share no common factors, meaning $\gcd(45, 899) = 1$.

Thus, $a = 45$ and $b = 899$.

Finally, $a + b = 45 + 899 = 944$.

Answer: $944$

</details>

---

### Q2. JEE Main 2026 (24 January Shift 2)

*Type:* `numerical` | *Level:* `2`

Let S be a set of 5 elements and $\mathrm{P}(\mathrm{S})$ denote the power set of S. Let E be an event of choosing an ordered pair ($\mathrm{A}, \mathrm{B}$) from the set $\mathrm{P}(\mathrm{S}) \times \mathrm{P}(\mathrm{S})$ such that $\mathrm{A} \cap \mathrm{B}=\emptyset$. If the probability of the event $E$ is $\frac{3^{p}}{2^{q}}$, where $p, q \in N$, then $p+q$ is equal to $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

$S$ has 5 elements, so $P(S)$ has $2^5 = 32$ subsets.
Total ordered pairs from $P(S) \times P(S)$ is $32^2 = 1024$
For pairs $(A, B)$ with $A \cap B = \emptyset$: each of the 5 elements has 3 choices - in $A$ only, in $B$ only, or in neither
Number of favorable outcomes = $3^5 = 243$
Probability $= \frac{243}{1024} = \frac{3^5}{2^{10}}$
With $p = 5$ and $q = 10$, we get $p + q = 15$

</details>

---

### Q3. JEE Main 2026 (23 January Shift 1)

*Type:* `numerical` | *Level:* `2`

From the first 100 natural numbers, two numbers first $a$ and then $b$ are selected randomly without replacement. If the probability that $a-b \geqslant 10$ is $\frac{m}{n}, \operatorname{gcd}(m, n)=1$, then $m+n$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **311**

**Detailed Solution:**

Total ordered selections $= 100 \times 99 = 9900$.
Favorable ($a - b \geq 10$): for each $b$ from 1 to 90, $a$ ranges from $b+10$ to 100, giving $91 - b$ choices.
Count $= \sum_{b=1}^{90}(91-b) = \sum_{k=1}^{90}k = \frac{90 \times 91}{2} = 4095$.
Probability $= \frac{4095}{9900} = \frac{91}{220}$ (after dividing by 45).
$\gcd(91, 220) = 1$, so $m = 91, n = 220$.
$m + n = 311$.

</details>

---

### Q4. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two distinct numbers $a$ and $b$ are selected at random from $1,2,3, \ldots, 50$. The probability, that their product $a b$ is divisible by 3, is

**Options:**

- **(A)** $\frac{272}{1225}$
- **(B)** $\frac{561}{1225}$
- **(C)** $\frac{664}{1225}$
- **(D)** $\frac{8}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{664}{1225}$**

**Detailed Solution:**

Total ways $= \binom{50}{2} = 1225$.
$ab$ is divisible by 3 iff at least one of $a, b$ is divisible by 3.
Multiples of 3 in $\{1,\ldots,50\}$: $3,6,\ldots,48 \Rightarrow 16$ numbers. Non-multiples of 3: $34$.
$P(\text{neither divisible by 3}) = \frac{\binom{34}{2}}{\binom{50}{2}} = \frac{561}{1225}$.
$P(ab \text{ divisible by 3}) = 1 - \frac{561}{1225} = \frac{664}{1225}$.

</details>

---

### Q5. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A$ and $B$ are two events such that $P(A)=0.7$, $\mathrm{P}(\mathrm{B})=0.4$ and $\mathrm{P}(\mathrm{A} \cap \overline{\mathrm{B}})=0.5$, where $\overline{\mathrm{B}}$ denotes the complement of $B$, then $P(B \mid(A \cup \bar{B}))$ is equal:-

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{6}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{4}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{P}(\mathrm{A})=\frac{7}{10}, \mathrm{P}(\mathrm{B})=\frac{4}{10} \\ & \mathrm{P}(\mathrm{A} \cup \overline{\mathrm{B}})=\frac{5}{10} \\ & \mathrm{P}\left(\frac{\mathrm{B}}{\mathrm{A} \cup \overline{\mathrm{B}}}\right)=\frac{\mathrm{P}(\mathrm{B} \cap(\mathrm{A} \cup \overline{\mathrm{B}}))}{\mathrm{P}(\mathrm{A} \cup \overline{\mathrm{B}})} \\ & =\frac{\mathrm{P}((\mathrm{B} \cap \overline{\mathrm{B}}) \cup(\mathrm{B} \cap \mathrm{A}))}{\mathrm{P}(\mathrm{A} \cup \overline{\mathrm{B}})}=\frac{\mathrm{P}(\mathrm{A} \cap \mathrm{B})}{\mathrm{P}(\mathrm{A} \cup \overline{\mathrm{B}})}\end{aligned}$
$\begin{aligned} & =\frac{\mathrm{P}(\mathrm{A})-\mathrm{P}(\mathrm{A} \cap \overline{\mathrm{B}})}{\mathrm{P}(\mathrm{A})+\mathrm{P}(\overline{\mathrm{B}})-\mathrm{P}(\mathrm{A} \cap \overline{\mathrm{B}})}=\frac{\frac{7}{10}-\frac{5}{10}}{\frac{7}{10}+\left(1-\frac{4}{10}\right)-\frac{5}{10}} \\ & =\frac{2}{8}=\frac{1}{4}\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The probability, of forming a 12 persons committee from 4 engineers, 2 doctors and 10 professors containing at least 3 engineers and at least 1 doctor, is:

**Options:**

- **(A)** $\frac{129}{182}$
- **(B)** $\frac{103}{182}$
- **(C)** $\frac{17}{26}$
- **(D)** $\frac{19}{26}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{129}{182}$**

**Detailed Solution:**

$\begin{aligned}
& 3 \text { engineering }+1 \text { doctor }+8 \text { Prof } \rightarrow{ }^4 \mathrm{C}_3 \cdot{ }^2 \mathrm{C}_1 \cdot{ }^{10} \mathrm{C}_8 \\
& =360 \\
& 3 \text { engineering }+2 \text { doctors }+7 \text { Prof } \rightarrow{ }^4 \mathrm{C}_3 \cdot{ }^2 \mathrm{C}_2 \cdot{ }^{10} \mathrm{C}_7 \\
& =480 \\
& 4 \text { engineering }+1 \text { doctor }+7 \text { Prof } \rightarrow{ }^4 \mathrm{C}_4 \cdot{ }^2 \mathrm{C}_1 \cdot{ }^{10} \mathrm{C}_7 \\
& =240 \\
& 4 \text { engineering }+2 \text { doctors }+6 \text { Prof } \rightarrow{ }^4 \mathrm{C}_4 \cdot{ }^2 \mathrm{C}_2 \cdot{ }^{10} \mathrm{C}_6 \\
& =210
\end{aligned}$
Total $=1290$
Req. probability $=\frac{1290}{{ }^{16} \mathrm{C}_{12}}=\frac{1290}{1820}=\frac{129}{182}$

</details>

---

### Q7. JEE Main 2025 (3 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

All five letter words are made using all the letters $\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}$ and arranged as in an English dictionary with serial numbers. Let the word at serial number $n$ be denoted by $W_n$. Let the probability $\mathrm{P}\left(\mathrm{W}_{\mathrm{n}}\right)$ of choosing the word $\mathrm{W}_{\mathrm{n}}$ satisfy $\mathrm{P}\left(\mathrm{W}_{\mathrm{n}}\right)=2 \mathrm{P}\left(\mathrm{W}_{\mathrm{n}-1}\right), \mathrm{n} \gt 1$.
If $\mathrm{P}(\mathrm{CDBEA})=\frac{2^\alpha}{2^\beta-1}, \alpha, \beta \in \mathbb{N}$, then $\alpha+\beta$ is equal to : _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **183**

**Detailed Solution:**

Let $\mathrm{P}\left(\mathrm{W}_1\right)=\mathrm{x}$
$\begin{aligned}
& \sum_{i=1}^{120} P\left(W_i\right)=1 \\
& x+2 x+2^2 x+2^3 x+\ldots+2^{119} x=1 \\
& \frac{x\left(2^{120}-1\right)}{(2-1)}=1 \Rightarrow x=\frac{1}{2^{120}-1} \qquad...(i)
\end{aligned}$
Rank of CDBEA
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/DZhJe-limw_eiSyFNyCeIKHBGg2qv06Z3aqegUTAHCs.original.fullsize.png"/>
$\begin{aligned} & \text { C D B A E }=1 \\ & \text { C D B E A }=1\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/XJ7ZfTjBHxKeKZ4ylFtkb2Tm4dNONWFz93k1SbJYJPk.original.fullsize.png"/>
$\begin{aligned} & \text { So, } \mathrm{P}\left(\mathrm{W}_{64}\right)=2 \mathrm{P}\left(\mathrm{W}_{63}\right)=\ldots=2^{63} \mathrm{P}\left(\mathrm{W}_1\right) \\ & =\frac{2^{63}}{2^{120}-1} \\ & \alpha+\beta=63+120=183\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (2 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Three distinct numbers are selected randomly from the set $\{1,2,3, \ldots \ldots, 40\}$. If the probability, that the selected numbers are in an increasing G.P. is $\frac{m}{n}$, $\operatorname{gcd}(m, n)=1$, then $m+n$ is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4949**

**Detailed Solution:**

$1 \leq \mathrm{a} \lt \mathrm{ar} \lt \mathrm{ar}^2 \leq 40$
(If $r \in N$ )
If $r=2$
$1 \leq a \lt 2 a \lt 4 a \leq 40$
$a \in\{1, \ldots \ldots ., 10\}$ ________ (10 GP)
If $r=3$
$1 \leq a \lt 3 a \lt 9 a \leq 40$
$\mathrm{a} \in\{1,2,3,4\}$ ________ ________  (4 GP)
If $\mathrm{r}=4$
$1 \leq a \lt 4 a \lt 16 a \leq 40$
$a \in\{1,2\}$ ________ ________  (2 GP)
If $r=5$
$1 \leq a \lt 5 a \lt 25 a \leq 40$
$a \in\{1\}$ ________ ________ (1 GP)
If $r=6$
$1 \leq a \lt 6 a \lt 36 a \leq 40$
$\mathrm{a} \in\{1\}$ ________ ________  (1 GP)
$\left(\mathrm{P}=\frac{18}{9880}=\frac{9}{4940}\right)$ as per NTA for $\mathrm{r} \in \mathrm{N}$
$\mathrm{m}+\mathrm{n}=4949$
If $\underline{r} \notin \mathrm{~N}$ (also possible)
$\mathrm{r}=\frac{3}{2}$
$\operatorname{ar}^2=\frac{9 \mathrm{a}}{4} ; \mathrm{a}=4 \mathrm{k}$
$\left.\begin{array}{l}(4,6,9) \\ (8,12,18) \\ (12,18,27) \\ (16,24,36)\end{array}\right\} 4 \mathrm{GP}$
$\begin{aligned} & \begin{array}{l}\mathrm{r}=\frac{5}{2} \quad \mathrm{ar}^2=\frac{25 \mathrm{a}}{4} ; \mathrm{a}=4 \mathrm{k} \\ \\ \\ (4,10,25) \ldots \ldots . .(1) \mathrm{GP} \\ \mathrm{r}=\frac{4}{3} \quad \mathrm{ar}^2=\frac{16 \mathrm{a}}{9} \rightarrow \mathrm{a}=9 \mathrm{k} \\ \\ \\ (9,12,16),(18,24,32) \ldots \ldots .(2) \mathrm{GP} \\ \mathrm{r}=\frac{5}{3} \quad \mathrm{ar}^2=\frac{25 \mathrm{a}}{9} ; \mathrm{a}=9 \mathrm{k} \\ \\ \quad(9,15,25) \ldots \ldots \ldots .(1) \mathrm{GP} \\ \mathrm{r}=\frac{5}{4} \quad \mathrm{ar}^2=\frac{25 \mathrm{a}}{16} ; \mathrm{a}=16 \mathrm{k}\end{array} \\ & \quad \begin{array}{l}(16,20,25) \ldots \ldots \ldots . .(1) \mathrm{GP} \\ \mathrm{r}=\frac{6}{5} \quad \mathrm{ar}^2=\frac{36 \mathrm{a}}{25} ; \mathrm{a}=25 \mathrm{k}\end{array} \\ & \begin{array}{l}(25,30,36) \ldots \ldots \ldots . .(1) \mathrm{GP} \\ \mathrm{Total}=18+10=28 \\ \mathrm{P}=\frac{28}{40} \mathrm{C}_3=\frac{28}{9880}=\frac{7}{2470} \\ \mathrm{~m}+\mathrm{n}=2477\end{array}\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let S be the set of all the words that can be formed by arranging all the letters of the word GARDEN. From the set S, one word is selected at random. The probability that the selected word will NOT have vowels in alphabetical order is :

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{4}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

A, E,G R D N
$\text { Probabllity }(\mathrm{P})=\frac{\text { favourable case }}{\text { Total case }}$
(when A & E are in order)
Total case $=6$ !
Favourable case $={ }^6 \mathrm{C}_2 .4$ !
$P=\frac{(15) 4!}{(30) 4!}$

Probablity when not in order $=1-\frac{1}{2}=\frac{1}{2}$

</details>

---

### Q10. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two number $\mathrm{k}_1$ and $\mathrm{k}_2$ are randomly chosen from the set of natural numbers. Then, the probability that the value of $\mathrm{i}^{\mathrm{k}_1}+\mathrm{i}^{\mathrm{k}_2},(\mathrm{i}=\sqrt{-1})$ is non-zero, equals

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{3}{4}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{4}$**

**Detailed Solution:**

Let $k_1=4 \lambda_1+r_1, r_1 \in\{0,1,2,3\}$
$k_2=4 \lambda_2+r_2$
$\begin{aligned}
& (i)^{k_1}+(i)^{k_2}=(i)^{r_1}+(i)^{r_2} \\
& (i)^{r_1} \in\{1, i,-1,-i\}
\end{aligned}$
$\text { Zero } \Rightarrow 1,(-1) \text { pair } \quad \Rightarrow\left\{\begin{array}{cc}
1, & -1 \\
i, & -i \\
-i,+i \\
-1, & 1
\end{array}\right\}$
$i,(-i)$ pair
$\begin{aligned} & \text { Zero probability }=\frac{4}{{ }^4 C_1 \cdot{ }^4 C_1}=\frac{1}{4} \\ & \text { Probability (non-zero) }=1-\frac{1}{4}=\frac{3}{4}\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\left[a_{i j}\right]$ be a square matrix of order 2 with entries either 0 or 1 . Let $E$ be the event that $A$ is an invertible matrix. Then the probability $\mathrm{P}(\mathrm{E})$ is :

**Options:**

- **(A)** $\frac{3}{16}$
- **(B)** $\frac{5}{8}$
- **(C)** $\frac{3}{8}$
- **(D)** $\frac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{8}$**

**Detailed Solution:**

$A=\left[a_y\right]_{2 \times 2}$ and entries are 0 or 1.
$\begin{aligned}
& \therefore\left|\begin{array}{ll}
a & b \\
c & d
\end{array}\right|=0 \\
& \Rightarrow a d-b c=0
\end{aligned}$
Case I: $a d=b c=1$
$\therefore \quad a=b=c=d=1$
Case II: $a d=b c=0$
$\begin{array}{ll}
a=0, d=0 & b=0, c=0 \\
a=0, d=1 & b=0, c=1 \\
a=1, d=0 & b=1, c=0
\end{array}$
$\therefore$ Total 10 cases when matrix is non invertible Total possible matrix $=2^4=16$
Required probability of invertible
$=\frac{16-10}{16}=\frac{6}{16}=\frac{3}{8}$

</details>

---

### Q12. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$A$ and $B$ alternately throw a pair of dice. $A$ wins if he throws a sum of 5 before $B$ throws a sum of 8 , and $B$ wins if he throws a sum of 8 before $A$ throws a sum of 5 . The probability, that $A$ wins if A makes the first throw, is

**Options:**

- **(A)** $\frac{8}{17}$
- **(B)** $\frac{9}{19}$
- **(C)** $\frac{9}{17}$
- **(D)** $\frac{8}{19}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{9}{19}$**

**Detailed Solution:**

For sum ' 5 ' $\rightarrow(1,4),(2,3),(3,2)$
$(4,1) \Rightarrow P(A)=\frac{4}{36}$
For sum ' 8 ' $\rightarrow(2,6),(3,5),(4,4)$
For sum ' 5 ' $\rightarrow(1,4),(2,3),(3,2)$
$(4,1) \Rightarrow P(A)=\frac{4}{36}$
For sum ' 8 ' $\rightarrow(2,6),(3,5),(4,4)$
$\begin{aligned} & (5,3),(6,2) \Rightarrow P(B)=\frac{5}{36} \\ & \begin{aligned} P(\bar{A})=\frac{32}{36} & , P(\bar{B})=\frac{31}{36}\end{aligned} \\ & \begin{aligned} P(A \text { wins })= & P(A)+P(\bar{A}) P(\bar{B}) P(A)+ \\ & +P(\bar{A}) P(\bar{B}) P(\bar{A}) P(\bar{B}) P(A)+\ldots \\ = & \frac{P(A)}{1-P(\bar{A}) P(\bar{B})}=\frac{9}{19}\end{aligned}\end{aligned}$

</details>

---

### Q13. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A board has 16 squares as shown in the figure:
<img src="https://cdn.quizrr.in/question-assets/jee_main_pyq/Yfw6kJOWsbLAtJOMXpdUSvYyuAwAQxSZUaTpULCAaas.original.fullsize.png">
Out of these 16 squares, two squares are chosen at random. The probability that they have no side in common is :

**Options:**

- **(A)** 7/10
- **(B)** 4/5
- **(C)** 23/30
- **(D)** 3/5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4/5**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Yfw6kJOWsbLAtJOMXpdUSvYyuAwAQxSZUaTpULCAaas.original.fullsize.png">

$\begin{aligned}
& \text { Total }={ }^{16} \mathrm{C}_2 \\
& \text { Required ways }=\text { Total }- \text { (adjacent square) } \\
& ={ }^{16} \mathrm{C}_2- \\
& \text { [3 pair in vertical \& horizontal for } \\
& \text { each row and column] } \\
& ={ }^{16} C_2-[3 \times 4+3 \times 4] \\
& =96 \\
& \text { Probability }=\frac{96}{120}=\frac{4}{5}
\end{aligned}$

</details>

---

### Q14. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

One die has two faces marked 1 , two faces marked 2 , one face marked 3 and one face marked 4 . Another die has one face marked 1 , two faces marked 2 , two faces marked 3 and one face marked 4. The probability of getting the sum of numbers to be 4 or 5 , when both the dice are thrown together, is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{4}{9}$
- **(D)** $\frac{3}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}$**

**Detailed Solution:**

$\mathrm{a}=$ number or dice 1
$\mathrm{b}=$ number on dice 2
$(a, b)=(1,3),(3,1),(2,2),(2,3),(3,2),(1,4),(4,1)$

Required probability
$\begin{aligned}
& =\frac{2}{6} \times \frac{2}{6}+\frac{1}{6} \times \frac{1}{6}+\frac{2}{6} \times \frac{2}{6}+\frac{2}{6} \times \frac{2}{6}+\frac{1}{6} \times \frac{2}{6}+\frac{2}{6} \times \frac{1}{6}+\frac{1}{6} \times \frac{2}{6} \\
& =\frac{18}{36}=\frac{1}{2}
\end{aligned}$

</details>

---

### Q15. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If an unbiased dice is rolled thrice, then the probability of getting a greater number in the $i^{\text {th }}$ roll than the number obtained in the $(i-1)^{\text {th }}$ roll, $i=2,3$, is equal to

**Options:**

- **(A)** $3 / 54$
- **(B)** $2 / 54$
- **(C)** $1 / 54$
- **(D)** $5 / 54$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5 / 54$**

**Detailed Solution:**

Favourable cases $={ }^6 \mathrm{C}_3$
Total out comes $=6^3$
Probability of getting greater number than previous
$\text {one }=\frac{{ }^6 \mathrm{C}_3}{\mathrm{r}^3}=\frac{20}{216}=\frac{5}{54}$

</details>

---

### Q16. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $\mathrm{a}, \mathrm{b}$ and $\mathrm{c}$ denote the outcome of three independent rolls of a fair tetrahedral die, whose four faces are marked $1,2,3,4$. If the probability that $a x^2+b x+c=0$ has all real roots is $\frac{m}{n}$, $\operatorname{gcd}(\mathrm{m}, \mathrm{n})=1$, then $\mathrm{m}+\mathrm{n}$ is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

$\mathrm{a}, \mathrm{b}, \mathrm{c} \in\{1,2,3,4\}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Y8zN0RHGwJlz1-bk9msnKZA-SqLhC91VSLbr-1VRuJc.original.fullsize.png">
Tetrahedral dice
$a x^2+b x+c=0$
has all real roots
$\begin{aligned}
& \Rightarrow \mathrm{D} \geq 0 \\
& \Rightarrow \mathrm{b}^2-4 \mathrm{ac} \geq 0
\end{aligned}$
Let $b=1 \Rightarrow 1-4 a c \geq 0$ (Not feasible)
$\begin{aligned} & b=2 \Rightarrow 4-4 a c \geq 0 \\ & 1 \geq a c \Rightarrow a=1, c=1, \\ & b=3 \Rightarrow 9-4 a c \geq 0 \\ & \frac{9}{4} \geq a c \\ & \Rightarrow a=1, c=1 \\ & \Rightarrow a=1, c=2 \\ & \Rightarrow a=2, c=1 \\ & b=4 \Rightarrow 16-4 a c \geq 0 \\ & 4 \geq a c\end{aligned}$
$\begin{aligned} & \Rightarrow a=1, c=1 \\ & \Rightarrow a=1, c=2 \quad \Rightarrow a=2, c=1 \\ & \Rightarrow a=1, c=3 \quad \Rightarrow a=3, c=1 \\ & \Rightarrow a=1, c=4 \quad \Rightarrow a=4, c=1 \\ & \Rightarrow a=2, c=2 \\ & \text { Probability }=\frac{12}{(4)(4)(4)}=\frac{3}{16}=\frac{m}{m} \\ & m+n=19\end{aligned}$

</details>

---

### Q17. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If three letters can be posted to any one of the 5 different addresses, then the probability that the three letters are posted to exactly two addresses is:

**Options:**

- **(A)** $\frac{18}{25}$
- **(B)** $\frac{12}{25}$
- **(C)** $\frac{6}{25}$
- **(D)** $\frac{4}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{12}{25}$**

**Detailed Solution:**

$\begin{aligned} & \text { Total method }=5^3 \\ & \text { faverable }={ }^5 \mathrm{C}_2\left(2^3-2\right)=60 \\ & \text { probability }=\frac{60}{125}=\frac{12}{25}\end{aligned}$

</details>

---

### Q18. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The coefficients $a, b, c$ in the quadratic equation $a x^2+b x+c=0$ are from the set $\{1,2,3,4,5,6\}$. If the probability of this equation having one real root bigger than the other is $p$, then 216 p equals :

**Options:**

- **(A)** 57
- **(B)** 76
- **(C)** 38
- **(D)** 19

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 38**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{D}>0 \\
& \mathrm{~b}^2>4 \mathrm{ac} \\
& \mathrm{b}=3:(\mathrm{a}, \mathrm{c})=(1,1)(1,2)(2,1) \\
& \mathrm{b}=4:(\mathrm{a}, \mathrm{c})=(1,1)(1,2)(2,1)(1,3)(3,1) \\
& \mathrm{b}=5:(\mathrm{a}, \mathrm{c})=(1,1)(1,2)(2,1)(1,3)(3,1)(1,4)(4,1) \\
&(1,5)(5,1)(1,6)(6,1)(2,3)(3,2)(2,2) \\
& \mathrm{b}=6:(\mathrm{a}, \mathrm{c})=(1,1)(1,2)(2,1)(1,3)(3,1)(1,4)(4,1) \\
&(1,5)(5,1)(1,6)(6,1)(2,3)(3,2)(2,4)(4,2)(2,2)
\end{aligned}$
fav. cases $=38$
Prob. : $\frac{38}{6 \times 6 \times 6}$

</details>

---

### Q19. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The coefficients $a, b, c$ in the quadratic equation $a x^2+b x+c=0$ are chosen from the set $\{1,2,3,4,5,6,7,8\}$. The probability of this equation having repeated roots is :

**Options:**

- **(A)** $\frac{1}{128}$
- **(B)** $\frac{1}{64}$
- **(C)** $\frac{3}{256}$
- **(D)** $\frac{3}{128}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{64}$**

**Detailed Solution:**

$\begin{aligned} & a x^2+b x+c=0 \\ & a, b, c \in\{1,2,3,4,5,6,7,8\} \\ & \text { Repeated roots } D=0 \\ & \Rightarrow b^2-4 a c=0 \Rightarrow b^2=4 a c \\ & \text { Prob }=\frac{8}{8 \times 8 \times 8}=\frac{1}{64} \\ & \Rightarrow(a, b, c) \\ & (1,2,1) ;(2,4,2) ;(1,4,4) ;(4,4,1) ;(3,6,3) ; \\ & (2,8,8) ;(8,8,2) ;(4,8,4) \\ & 8 \text { case }\end{aligned}$

</details>

---

### Q20. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A coin is biased so that a head is twice as likely to occur as a tail. If the coin is tossed <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> times, then the probability of getting two tails and one head is-

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>27</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>27</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>H</mi></mfenced><mo>=</mo><mn>2</mn><mi>P</mi><mfenced><mi>T</mi></mfenced></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>H</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>T</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>P</mi><mfenced><mi>T</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>T</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mi>T</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo> </mo><mtext>and</mtext><mo> </mo><mi>P</mi><mfenced><mi>H</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mn>2</mn><mo> </mo><mtext>tails and</mtext><mo> </mo><mn>1</mn><mo> </mo><mtext>head</mtext></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>×</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>×</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>×</mo><mfrac><mrow><mn>3</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mfenced><mtext>for arrangements</mtext></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mn>2</mn><mo> </mo><mtext>tails and</mtext><mo> </mo><mn>1</mn><mo> </mo><mtext>head</mtext></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q21. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two marbles are drawn in succession from a box containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> red, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> white, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> blue and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> orange marbles, with replacement being made after each drawing. Then the probability, that first drawn marble is red and second drawn marble is white, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>25</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>25</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>75</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>75</mn></mfrac></math>**

**Detailed Solution:**

<p>Given marbles are:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>→</mo><mi>R</mi><mo>,</mo><mo> </mo><mn>30</mn><mo>→</mo><mi>W</mi><mo>,</mo><mo> </mo><mn>20</mn><mo>→</mo><mi>B</mi><mo>,</mo><mo> </mo><mn>15</mn><mo>→</mo><mi>O</mi></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mtext>Number of favourable outcomes</mtext><mtext>Total number of outcomes</mtext></mfrac></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>×</mo><mi>P</mi><mfenced><mi>B</mi></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>B</mi></math> are independent events.</p><p>Probability of drawing first marble red and then white is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mn>10</mn><mn>75</mn></mfrac><mo>×</mo><mfrac><mn>30</mn><mn>75</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>75</mn></mfrac></math></p>

</details>

---

### Q22. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A bag contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> white and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> black balls. A die is rolled once and the number of balls equal to the number obtained on the die are drawn from the bag at random. The probability that all the balls drawn are white is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>50</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>50</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Bag have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> white and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> black balls</p><p>Now also given die is rolled and the number denotes the number of ball drawn from the bag,</p><p>So, probability all drawn balls are white will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>6</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>15</mn><mn>45</mn></mfrac><mo>+</mo><mfrac><mn>20</mn><mn>120</mn></mfrac><mo>+</mo><mfrac><mn>15</mn><mn>210</mn></mfrac><mo>+</mo><mfrac><mn>6</mn><mn>252</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>210</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>504</mn><mn>2520</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math></p></blockquote>

</details>

---

### Q23. JEE Main 2023 (11 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let the probability of getting head for a biased coin be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>. It is tossed repeatedly until a head appears. Let  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> be the number of tosses required. If the probability that the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>N</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> has no real root is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>p</mi><mi>q</mi></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> are co-prime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>-</mo><mi>p</mi></math> is equal to..........

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27**

**Detailed Solution:**

<p>Given a quadratic equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>n</mi><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> has no real roots, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>25</mn><msup><mi>N</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>64</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>N</mi><mo>&#60;</mo><mfrac><mn>16</mn><mn>5</mn></mfrac><mo>&#8658;</mo><mi>N</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math></p><p>And, For a biased coin, the probability of getting head is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo></math> and probability of getting tail will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>So, required probability is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><msup><mfenced><mfrac><mstyle displaystyle="true"><mn>3</mn></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac></mfenced><mn>2</mn></msup><mo>&#183;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>+</mo><msup><mfenced><mfrac><mstyle displaystyle="true"><mn>3</mn></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac></mfenced><mn>3</mn></msup><mo>&#183;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac><mo>=</mo><mfrac><mi>p</mi><mi>q</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>4</mn></mfrac></mstyle></mfenced><mn>3</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></mrow></mfrac><mo>=</mo><mfrac><mi>p</mi><mi>q</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>=</mo><mfrac><mi>p</mi><mi>q</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mfrac><mn>27</mn><mn>64</mn></mfrac><mo>=</mo><mfrac><mi>p</mi><mi>q</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>p</mi><mi>q</mi></mfrac><mo>=</mo><mfrac><mn>37</mn><mn>64</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>-</mo><mi>p</mi><mo>=</mo><mn>27</mn></math></p>

</details>

---

### Q24. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>M</mi><mo>=</mo><mfenced open="[" close="]"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math> be a sample space and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced close="}" open="{"><mrow><mi>M</mi><mo>&#8712;</mo><mi>S</mi><mo>:</mo><mi>M</mi><mo>&#160;</mo><mtext>is&#160;invertible</mtext></mrow></mfenced></math> be an even. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>27</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>47</mn><mn>81</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>49</mn><mn>81</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>50</mn><mn>81</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>50</mn><mn>81</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>M</mi><mo>=</mo><mfenced close="]" open="["><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math> </p><p>So, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>So, total sample space will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>4</mn></msup><mo>=</mo><mn>81</mn></math></p><p>Now we will find <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mover><mi>A</mi><mo>&#175;</mo></mover></mfenced></math> or possibilities for <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>M</mi><mo>|</mo><mo>=</mo><mn>0</mn></math></p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>M</mi><mo>|</mo><mo>=</mo><mn>0</mn></math> cases will be,</p><p>1.<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>&#8594;</mo></math> Total matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math>
2. Two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#39;</mo><mi>s</mi></math> and Two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#39;</mo><mi>s</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo></math> Total matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math>
3. Two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#39;</mo><mi>s</mi></math> and Two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#39;</mo><mi>s</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo></math> Total matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math>
4. Two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#39;</mo><mi>s</mi></math> and Two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#39;</mo><mi>s</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo></math> Total matrix<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math>
5. One <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and three <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mo>&#39;</mo><mi>s</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo></math> Total matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math>
6. One <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and Three <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#39;</mo><mi>s</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo></math> Total matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math>
7. One <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and one <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#39;</mo><mi>s</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo></math> Total matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn></math></p><p>So, total cases for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>M</mi></mfenced><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math>,</p><p>So probability will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mover><mi>A</mi><mo>&#175;</mo></mover></mfenced><mo>=</mo><mfrac><mn>31</mn><mn>81</mn></mfrac></math>
Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>31</mn><mn>81</mn></mfrac><mo>=</mo><mfrac><mn>50</mn><mn>81</mn></mfrac></math></p>

</details>

---

### Q25. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> denote the sum of the numbers obtained when two dice are rolled. If the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>N</mi></msup><mo>&#60;</mo><mi>N</mi><mo>!</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>m</mi><mi>n</mi></mfrac></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are coprime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>m</mi><mo>-</mo><mn>3</mn><mi>n</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>N</mi></msup><mo>&#60;</mo><mi>N</mi><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> is the sum of numbers of two dice.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#8804;</mo><mi>N</mi><mo>&#8804;</mo><mn>12</mn></math></p><p>Let us check the given condition <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>N</mi></msup><mo>&#60;</mo><mi>N</mi><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mn>1</mn></math> (not possible) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mn>2</mn></math> (not possible) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mn>3</mn></math> (not possible) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mn>4</mn></math> (possible)</p><p>We need to find the probability for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>&#8805;</mo><mn>4</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>N</mi><mo>&#8805;</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced><mrow><mi>N</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><mi>N</mi><mo>=</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>36</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>11</mn><mn>12</mn></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p>Now let us find <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>m</mi><mo>-</mo><mn>3</mn><mi>n</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>11</mn><mo>-</mo><mn>3</mn><mo>&#215;</mo><mn>12</mn><mo>=</mo><mn>8</mn></math>.</p><p>Hence, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>.</p></blockquote>

</details>

---

### Q26. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Three dice are rolled. If the probability of getting different numbers on the three dice is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>p</mi><mi>q</mi></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> are co-prime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>-</mo><mi>p</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that three dice are thrown.</p><p>The total number of outcomes when three dice are thrown together is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mn>3</mn></msup><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn></math>.</p><p>The number of outcomes such that all the outcomes are different is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn></math>.</p><p>For ex: If the outcome in dice <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mo>&#34;</mo></msup><msup><mn>6</mn><mo>&#34;</mo></msup></math> then the number of outcomes for dice <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> should be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>)</mo></math> which excludes the outcome <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mo>&#34;</mo></msup><msup><mn>6</mn><mo>&#34;</mo></msup></math>.</p><p>Hence, the required probability is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>20</mn><mn>36</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mi>p</mi><mi>q</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>-</mo><mi>p</mi><mo>=</mo><mn>9</mn><mo>-</mo><mn>5</mn><mo>=</mo><mn>4</mn></math></p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>.</p></blockquote>

</details>

---

### Q27. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><msub><mi>w</mi><mn>1</mn></msub><mo>,</mo><msub><mi>w</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo></mrow></mfenced></math> be the sample space associated to a random experiment. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>w</mi><mi>n</mi></msub></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><msub><mi>w</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></mfenced></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8805;</mo><mn>2</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>3</mn><mi>l</mi><mo>;</mo><mo>&#160;</mo><mi>k</mi><mo>,</mo><mo>&#160;</mo><mi>l</mi><mo>&#8712;</mo><mi>&#8469;</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="{" close="}"><mrow><msub><mi>w</mi><mi>n</mi></msub><mo>;</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>A</mi></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>B</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>32</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>64</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>16</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>32</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>64</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>w</mi><mi>n</mi></msub></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><msub><mi>w</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></mfenced></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8805;</mo><mn>2</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>w</mi><mn>1</mn></msub></mfenced><mo>=</mo><mi>&#955;</mi></math> then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>w</mi><mn>2</mn></msub></mfenced><mo>=</mo><mfrac><mi>&#955;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>P</mi><mfenced><msub><mi>w</mi><mn>3</mn></msub></mfenced><mo>=</mo><mfrac><mi>&#955;</mi><msup><mn>2</mn><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"></mspace><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>w</mi><mi>n</mi></msub></mfenced><mo>=</mo><mfrac><mi>&#955;</mi><msup><mn>2</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mfrac></math></p><p>As</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mi>P</mi><mfenced><msub><mi>w</mi><mi>k</mi></msub></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>+</mo><mfrac><mi>&#955;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#955;</mi><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mi>&#955;</mi><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#955;</mi><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfrac><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>w</mi><mi>n</mi></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>3</mn><mi>l</mi><mo>;</mo><mo>&#160;</mo><mi>k</mi><mo>,</mo><mo>&#160;</mo><mi>l</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced><mo>=</mo><mfenced close="}" open="{"><mrow><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>10</mn><mo>&#8230;</mo><mo>&#8230;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><msub><mi>w</mi><mi>n</mi></msub><mo>:</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>A</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><msub><mi>w</mi><mn>5</mn></msub><mo>,</mo><msub><mi>w</mi><mn>7</mn></msub><mo>,</mo><msub><mi>w</mi><mn>8</mn></msub><mo>,</mo><msub><mi>w</mi><mn>9</mn></msub><mo>,</mo><msub><mi>w</mi><mn>10</mn></msub><mo>,</mo><msub><mi>w</mi><mn>11</mn></msub><mo>,</mo><mo>&#8230;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>&#8469;</mi><mo>-</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfenced close="]" open="["><mrow><mi>P</mi><mfenced><msub><mi>w</mi><mn>1</mn></msub></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>w</mi><mn>2</mn></msub></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>w</mi><mn>3</mn></msub></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>w</mi><mn>4</mn></msub></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>w</mi><mn>6</mn></msub></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>64</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfenced><mfrac><mrow><mn>32</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>1</mn></mrow><mn>64</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>64</mn></mfrac></math></p>

</details>

---

### Q28. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Fifteen football players of a club-team are given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> T-shirts with their names written on the backside. If the players pick up the T-shirts randomly, then the probability that at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> players pick the correct T-shirt is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>24</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>15</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>36</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p>Fifteen football players of a club-team are given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> T-shirts with their names written on the backside</p><p>So, total sample space will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>!</mo></math></p><p>Now for at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> players pick the correct T-shirt, </p><p>Required probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><msub><mi>D</mi><mfenced><mn>15</mn></mfenced></msub><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>&#183;</mo><msub><mi>D</mi><mfenced><mn>14</mn></mfenced></msub><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><msub><mi>D</mi><mfenced><mn>13</mn></mfenced></msub></mrow><mrow><mn>15</mn><mo>!</mo></mrow></mfrac></math></p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>n</mi></msub></math> is de-arrangement and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>n</mi></msub><mo>&#8776;</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mi>e</mi></mfrac><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>where&#160;</mtext><mi>e</mi><mo>&#8776;</mo><mn>2</mn><mo>.</mo><mn>73</mn></mrow></mfenced></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mfenced><mn>15</mn></mfenced></msub></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>15</mn><mtext>&#160;!&#160;</mtext></mrow><mi>e</mi></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mrow><mo>(</mo><mn>14</mn><mo>)</mo></mrow></msub></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>14</mn><mo>!</mo></mrow><mi>e</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mrow><mo>(</mo><mn>13</mn><mo>)</mo></mrow></msub></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><mo>!</mo></mrow><mi>e</mi></mfrac></math></p><p>We get , <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfenced><mfrac><mrow><mfrac><mrow><mn>15</mn><mo>!</mo></mrow><mi>e</mi></mfrac><mo>+</mo><mn>15</mn><mo>&#183;</mo><mfrac><mrow><mn>14</mn><mo>!</mo></mrow><mi>e</mi></mfrac><mo>+</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>14</mn></mrow><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>13</mn><mo>!</mo></mrow><mi>e</mi></mfrac></mrow><mrow><mn>15</mn><mo>!</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>5</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac><mo>&#8776;</mo><mo>.</mo><mn>08</mn></math></p><p>Note- This question was bonus as NTA as calculated the answer as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>&#215;</mo><mn>12</mn><mo>!</mo></mrow><mrow><mn>15</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math>, they have not considered the repetation cases.</p>

</details>

---

### Q29. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> be the sum of the numbers appeared when two fair dice are rolled and let the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi><mo>-</mo><mn>2</mn><mo>,</mo><msqrt><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></msqrt><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>+</mo><mn>2</mn></math> are in geometric progression be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mn>48</mn></mfrac></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>Two fair dices are rolled,</p><p>So total sample space will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mfenced><mi mathvariant="normal">s</mi></mfenced><mo>=</mo><mn>36</mn></math></p><p>Now given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msqrt><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">N</mi></msqrt><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>+</mo><mn>2</mn></math> are in G.P.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi mathvariant="normal">N</mi><mo>=</mo><mfenced><mrow><mi mathvariant="normal">N</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi mathvariant="normal">N</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi mathvariant="normal">N</mi><mo>=</mo><msup><mi mathvariant="normal">N</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi mathvariant="normal">N</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi mathvariant="normal">N</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi mathvariant="normal">N</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi mathvariant="normal">N</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">N</mi><mo>=</mo><mn>4</mn></math>  or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> (rejected)</p><p>Now favourable cases for sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mo>&#8801;</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>36</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>48</mn></mfrac><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q30. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let M be the maximum value of the product of two positive integers when their sum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math> . Let the sample space <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>x</mi><mo>&#8712;</mo><mi>Z</mi><mo>:</mo><mi>x</mi><mo>(</mo><mn>66</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>&#8805;</mo><mfrac><mn>5</mn><mn>9</mn></mfrac><mi>M</mi></mrow></mfenced></math> and the event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mo>{</mo><mi mathvariant="normal">x</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi><mo>:</mo><mi mathvariant="normal">x</mi></math> is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>}. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">A</mi><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>44</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>22</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p>Sum of two integer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>, so one number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and other will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn><mo>-</mo><mi>x</mi></math>,</p><p>And given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is maximum value of their product,</p><p>So let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi><mfenced><mrow><mn>66</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>66</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>Now differentiating to find maxima and minima we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>66</mn><mo>-</mo><mn>2</mn><mi>x</mi></math></p><p>Now equating with zero to find point of maxima as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>66</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></math> represents a downward parabola so it will give maxima,</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>66</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>33</mn></math>,</p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mn>33</mn><mo>&#215;</mo><mn>33</mn><mo>=</mo><mn>1089</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mn>66</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mfrac><mrow><mn>5</mn><mi>M</mi></mrow><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><mn>66</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><mn>1089</mn></mrow><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><mn>66</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mn>605</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>66</mn><mi>x</mi><mo>+</mo><mn>605</mn><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>11</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>55</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>11</mn><mo>,</mo><mn>55</mn></mrow></mfenced><mo>&#8594;</mo></math>total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math> numbers,</p><p>Now for probability of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, favourable outcomes will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mi>k</mi><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>12</mn><mo>,</mo><mn>15</mn><mo>,</mo><mn>18</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>54</mn></mrow></mfenced><mo>&#8594;</mo></math> total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> numbers,</p><p>So probability will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>45</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q31. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#937;</mi></math> be the sample space and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8838;</mo><mi>&#937;</mi></math> be an event. Given below are two statements:</p><p>(S1): If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>&#981;</mi></math></p><p>(S2): If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>&#937;</mi></math></p><p>Then</p>

**Options:**

- **(A)** only (S1) is true
- **(B)** only (S2) is true
- **(C)** both (S1) and (S2) are true
- **(D)** both (S1) and (S2) are false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) both (S1) and (S2) are true**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#937;</mi><mo>=</mo></math>sample space</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo></math>be an event</p><p>So, </p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mi>&#981;</mi></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mi>&#937;</mi></math></p><p>Hence, both statements are true.</p>

</details>

---

### Q32. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>2022</mn></mrow></mfenced></math>. Then the probability, that a randomly chosen number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mi>C</mi><mi>F</mi><mfenced><mrow><mi>n</mi><mo>,</mo><mn>2022</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>128</mn><mn>1011</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>166</mn><mn>1011</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>127</mn><mn>337</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>112</mn><mn>337</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>112</mn><mn>337</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>2022</mn></mrow></mfenced></math></p><p>So, total number of elements<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2022</mn></math></p><p>Now factors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2022</mn><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>337</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>HCF</mo><mfenced><mrow><mi>n</mi><mo>,</mo><mn>2022</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math> is feasible only when the value of &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>&#39; and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2022</mn></math> has no common factor.</p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo></math>Number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>2022</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>1011</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo></math>Number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>2022</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mn>674</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo></math>Number which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></p><p>Now from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>2022</mn></mrow></mfenced></math> number multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>18</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>2022</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>337</mn></math></p><p>Now applying the formula we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>-</mo><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1011</mn><mo>+</mo><mn>674</mn><mo>-</mo><mn>337</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1348</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo></math>Number which divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>337</mn></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>1022</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d3264e5a-b24a-4181-a70f-f7942bb2711a-image.png" style="width: 302px; height: 170px;" /></p><p>Total elements which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>337</mn><mo>=</mo><mn>1348</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>1350</mn></math></p><p>Favourable cases<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>elements which are neither divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>337</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2022</mn><mo>-</mo><mn>1350</mn><mo>=</mo><mn>672</mn></math></p><p>Required probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>672</mn><mn>2022</mn></mfrac><mo>=</mo><mfrac><mn>112</mn><mn>337</mn></mfrac></math></p></blockquote>

</details>

---

### Q33. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Out of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>%</mo></math> female and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>%</mo></math> male candidates appearing in an exam, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>%</mo></math> candidates qualify it. The number of females qualifying the exam is twice the number of males qualifying it. A candidate is randomly chosen from the qualified candidates. The probability, that the chosen candidate is a female, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>16</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>23</mn><mn>32</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>16</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Out of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>%</mo></math> female and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>%</mo></math> male candidates appearing in an exam, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>%</mo></math> candidates qualify it. The number of females qualifying the exam is twice the number of males qualifying it. A candidate is randomly chosen from the qualified candidates. The probability, that the chosen candidate is a female, is</p><p>Now plotting the given value we have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ffbf396b-9e9b-4838-832a-c3bd10ccbb9e-image.png" style="width: 331px; height: 180px;" /></p><p>Now probability that chosen candidate is female <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>40</mn><mn>60</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p> </p><p>Note: we have modified the option, as this question of 28th july 2022 jee mains was a bonus.</p></blockquote>

</details>

---

### Q34. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the sample space of all five digit numbers. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is the probability that a randomly selected number from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>, is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> but not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>p</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>0146</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>2085</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>0285</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>1521</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>0285</mn></math>**

**Detailed Solution:**

<blockquote><p>Given, five-digit number,</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>S</mi></mfenced><mo>=</mo></math>total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit number will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>:</mo></math> number is multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> but not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></p><p>Smallest <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10003</mn></math></p><p>Largest <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99995</mn></math></p><p>Now by using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of A.P formula we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>99995</mn><mo>=</mo><mn>10003</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>12857</mn></math></p><p>Now finding number which is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math></p><p>Again using A.P formula we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99995</mn><mo>=</mo><mn>10010</mn><mo>+</mo><mfenced><mrow><mi>P</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>35</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>=</mo><mn>2572</mn></math></p><p>Now number divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> but not by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math> are</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12857</mn><mo>-</mo><mn>2572</mn><mo>=</mo><mn>10285</mn></math></p><p>So, probability will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><mn>10285</mn><mn>90000</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>P</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>0285</mn></math></p></blockquote>

</details>

---

### Q35. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the numbers appeared on the two throws of a fair six faced die are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>, then the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>36</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>36</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>36</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Total sample space of two dice will be equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>36</mn></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math> its discriminant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> must be less than zero,</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi><mo>&#60;</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#946;</mi><mo>&#60;</mo><mn>0</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>&#60;</mo><mn>4</mn><mi>&#946;</mi></math> </p><p>Now, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#946;</mi></math> can take values <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#946;</mi></math> can take values <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi>&#946;</mi></math> can take values <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>4</mn><mo>,</mo><mi>&#946;</mi></math> can take values <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>6</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, no value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> possible</p><p>So number of favourable ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>17</mn></math></p><p>Required probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mtext>favourable&#160;ways</mtext><mtext>total&#160;sample&#160;space</mtext></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>17</mn><mn>36</mn></mfrac></math></p></blockquote>

</details>

---

### Q36. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced></math> is both symmetric and transitive, is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>16</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>16</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>16</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>16</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>16</mn></mfrac></math>**

**Detailed Solution:**

<p>Total number of elements in the Cartesian product will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, so total possible relations will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>4</mn></msup><mo>=</mo><mn>16</mn></math></p><p>The relations which will be symmetric and transitive both will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mi>x</mi><mo>,</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mi>y</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>y</mi><mo>,</mo><mi>y</mi></mrow></mfenced></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>x</mi><mo>,</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mi>y</mi><mo>,</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mi>y</mi><mo>,</mo><mi>y</mi></mrow></mfenced></mrow></mfenced></math></p><p> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> relations</p><p>Hence, required probability will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>16</mn></mfrac></math></p>

</details>

---

### Q37. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The probability, that in a randomly selected <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>-digit number at least two digits are odd, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>36</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>36</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>33</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>36</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>36</mn></mfrac></math>**

**Detailed Solution:**

<p>Total No of 3-digit Number <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>900</mn></math></p><p>Case -1 When there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> odd digit and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> even digit</p><p>(i) Even odd odd <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>100</mn></math></p><p>{As <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> cannot come at <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mi>st</mi></msup></math> place}</p><p>(ii) Odd even odd <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>125</mn></math></p><p>(iii) Odd odd even <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>125</mn></math></p><p>Case-2</p><p>All <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> odd digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>125</mn></math></p><p>So total number of selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>-digit number having atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> odd digit will be addition of both cases which is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>100</mn><mo>+</mo><mn>125</mn><mo>+</mo><mn>125</mn><mo>+</mo><mn>125</mn><mo>=</mo><mn>475</mn></math></p><p>So probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>475</mn><mn>900</mn></mfrac><mo>=</mo><mfrac><mn>19</mn><mn>36</mn></mfrac></math></p>

</details>

---

### Q38. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Five numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><msub><mi>x</mi><mn>4</mn></msub><mo>,</mo><msub><mi>x</mi><mn>5</mn></msub></math> are randomly selected from the numbers<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>18</mn></math>  and are arranged in the increasing order <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>4</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>2</mn></msub></mrow></mfenced></math>. The probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>4</mn></msub><mo>=</mo><mn>11</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>136</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>68</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>68</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>68</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>68</mn></mfrac></math>**

**Detailed Solution:**

<p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>&#60;</mo><mn>7</mn><mo>&#60;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>&#60;</mo><mn>11</mn><mo>&#60;</mo><msub><mi>x</mi><mn>5</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>3</mn></msub><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>5</mn></msub><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>12</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>14</mn><mo>,</mo><mn>15</mn><mo>,</mo><mn>16</mn><mo>,</mo><mn>17</mn><mo>,</mo><mn>18</mn></mrow></mfenced></math></p><p>Required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>18</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>68</mn></mfrac></math></p>

</details>

---

### Q39. JEE Main 2022 (26 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

If the probability that a randomly chosen <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>-digit number formed by using digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> only is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn><mi>p</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **33**

**Detailed Solution:**

<p>We have to choose <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> digit number by using <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>8</mn></math> and it must be divisible by 21,</p><p>So, equal number of digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> should be used to form a number divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>. (Or all the digits are either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>)</p><p>In all cases whatever number is formed using six <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mo>&#39;</mo></msup></math> or six <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mo>&#39;</mo></msup></math>s or three <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mo>&#39;</mo></msup></math>s <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math> three <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mo>&#39;</mo></msup></math>s, that number can be splited into sum of multiples of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1001</mn><mo>,</mo><mn>1008</mn><mo>,</mo><mn>8001</mn><mo>,</mo><mn>8008</mn></math> (all of them are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>). So, all the numbers thus formed will be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>,</p><p>Example: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>811188</mn><mo>=</mo><mn>8001</mn><mo>&#215;</mo><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><mn>1008</mn><mo>&#215;</mo><mn>10</mn><mo>+</mo><mn>1008</mn></math></p><p>Number of such numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mn>2</mn><mo>=</mo><mn>22</mn></math></p><p>Required Probability, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>22</mn><msup><mn>2</mn><mn>6</mn></msup></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>32</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>96</mn><mi>p</mi><mo>=</mo><mfrac><mn>11</mn><mn>22</mn></mfrac><mo>&#215;</mo><mn>96</mn><mo>=</mo><mn>33</mn></math></p>

</details>

---

### Q40. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Two squares are chosen at random on a chessboard (see figure). The probability that they have a side in common is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f24da50c-1bca-49e3-8233-876270f8b013-image.png" style="width: 355px; height: 218px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>7</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>18</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>18</mn></mfrac></math>**

**Detailed Solution:**

<p>Total ways of choosing 2 squares <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>64</mn></mmultiscripts><mo>=</mo><mn>32</mn><mo>&#215;</mo><mn>63</mn></math></p><p>Now, each corners has two neighbours, and each <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>  squares across the outer edge of the chess board has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> neighbours, and remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math> squares have four neighbours</p><p>Favorable ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>4</mn><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>24</mn><mo>(</mo><mn>3</mn><mo>)</mo><mo>+</mo><mn>36</mn><mo>(</mo><mn>4</mn><mo>)</mo></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]"><mn>224</mn></mfenced><mo>=</mo><mn>112</mn><mo>.</mo></math>Since, every pair counted twice. </p><p>Required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>112</mn><mrow><mn>32</mn><mo>&#215;</mo><mn>63</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>18</mn></mfrac></math></p>

</details>

---

### Q41. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>}</mo><mo>.</mo></math> Then the probability that a randomly chosen onto function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>g</mi><mfenced><mn>1</mn></mfenced></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>15</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>30</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>10</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>10</mn></mfrac></math>**

**Detailed Solution:**

<p>Given:<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math></p><p>Total number of onto functions from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> tto <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>!</mo></math></p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>2</mn><mi>g</mi><mfenced><mn>1</mn></mfenced></math>:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnlines="solid none" frame="solid" rowlines="solid solid solid none"><mtr><mtd><mi>g</mi><mfenced><mn>3</mn></mfenced></mtd><mtd><mi>g</mi><mfenced><mn>1</mn></mfenced></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mtable><mtr><mtd><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo></mtd><mtd><mn>2</mn><mi>g</mi><mfenced><mn>1</mn></mfenced></mtd></mtr></mtable></math>can be defined in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> ways.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mn>2</mn></mfenced><mo>,</mo><mi>g</mi><mfenced><mn>4</mn></mfenced><mo>,</mo><mi>g</mi><mfenced><mn>5</mn></mfenced><mo>&#160;</mo><mtext>&#38;</mtext><mo>&#160;</mo><mi>g</mi><mfenced><mn>6</mn></mfenced></math> can be anything and can be defined in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>!</mo></math> ways.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>Number of onto functions for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>g</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>g</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced><mo>=</mo><mn>3</mn><mo>.</mo><mn>4</mn><mo>!</mo></math></p><p>Now required probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mo>.</mo><mn>4</mn><mo>!</mo></mrow><mrow><mn>6</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>!</mo></mrow><mrow><mn>30</mn><mo>&#215;</mo><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></math></p>

</details>

---

### Q42. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a randomly selected <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo></math>digit number belongs to the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="" open="{"><mrow><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>:</mo><mfenced><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math> is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>}</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Total two-digit numbers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math></p><p>So, total number of cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>90</mn></mmultiscripts><mo>=</mo><mn>90</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>n</mi></msup><mo>-</mo><mn>2</mn><mo>=</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>&#183;</mo><msup><mn>3</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mn>3</mn><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mn>3</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mi>n</mi><msup><mn>3</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#183;</mo><mi>n</mi></mrow></mfenced><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mo>-</mo><mn>2</mn></math></p><p>Here, the term <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><mo>-</mo><mn>2</mn></math> should be multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>-</mo><mn>2</mn></mrow></mfenced></math> is multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> only when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is odd.</p><p>There are total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math> odd two-digit numbers.</p><p>Hence, the required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>45</mn></mmultiscripts><mn>90</mn></mfrac><mo>=</mo><mfrac><mn>45</mn><mn>90</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q43. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> distinct balls be distributed among <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> boxes, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>1</mn></msub><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>B</mi></mrow><mn>2</mn></msub><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>B</mi></mrow><mn>3</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>4</mn></msub></math>. If the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>3</mn></msub></math> contains exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> balls is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>9</mn></msup></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> lies in the set :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>&#60;</mo><mn>1</mn><mo>}</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>|</mo><mo>&#8804;</mo><mn>1</mn><mo>}</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>|</mo><mo>&#60;</mo><mn>1</mn><mo>}</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>5</mn><mo>|</mo><mo>&#8804;</mo><mn>1</mn><mo>}</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>:</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>&#60;</mo><mn>1</mn><mo>}</mo></math>**

**Detailed Solution:**

<p>The number of ways in which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> distinct balls can be distributed among <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> boxes is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mn>9</mn></msup></math></p><p>The number of ways in which <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>3</mn></msub></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> balls is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mo>&#183;</mo><msup><mn>3</mn><mn>6</mn></msup></math></p><p>Using the classical definition of probability we can say the required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mo>&#183;</mo><msup><mn>3</mn><mn>6</mn></msup></mrow><msup><mn>4</mn><mn>9</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mn>27</mn></mfrac><mo>&#183;</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>9</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>28</mn><mn>9</mn></mfrac><mo>&#183;</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>9</mn></msup><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mn>28</mn><mn>9</mn></mfrac><mo>&#8776;</mo><mn>3</mn><mo>.</mo><mn>11</mn></math></p><p>Now, consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>k</mi></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>&#60;</mo><mn>1</mn></math></p>

</details>

---

### Q44. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Four dice are thrown simultaneously and the numbers shown on these dice are recorded in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> matrices. The probability that such formed matrices have all different entries and are non-singular, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>45</mn><mn>162</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>23</mn><mn>81</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>22</mn><mn>81</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>43</mn><mn>162</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>43</mn><mn>162</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let, the outcomes of the four dice are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></mrow></mfenced><mo>.</mo></math></p><p>Then, we have the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>.</mo></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi></math></p><p>Now, for each of the numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>d</mi></math> there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> possibilities, hence total cases<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>6</mn><mn>4</mn></msup><mo>.</mo></math></p><p>For a non-singular matrix, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mo>&#8800;</mo><mi>b</mi><mi>c</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi></math> are all different numbers from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>}</mo><mo>,</mo></math> thus we have total <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>P</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>=</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mfenced><mrow><mn>6</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>360</mn><mo>.</mo></math></p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>=</mo><mi>b</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mn>6</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>,</mo></math> here we have two cases possible.</p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>,</mo></math> thus, we can choose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>d</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>P</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>=</mo><mn>2</mn></math> ways and the same we can do for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo></math> and hence, we have total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>4</mn></math> ways.</p><p>Similarly, we can take  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>1</mn><mo>,</mo></math> and for this also we have total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> ways.</p><p>Thus, we have total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>8</mn></math> ways.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced><mo>&#160;</mo><mn>6</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>,</mo></math> again here also, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> cases possible.</p><p>Thus, the favourable cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>P</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>-</mo><mn>16</mn><mo>=</mo><mn>360</mn><mo>-</mo><mn>16</mn><mo>=</mo><mn>344</mn></math></p><p>And, hence the required probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>344</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>344</mn><mn>1296</mn></mfrac><mo>=</mo><mfrac><mn>43</mn><mn>162</mn></mfrac><mo>.</mo></math></p></blockquote>

</details>

---

### Q45. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Words with or without meaning are to be formed using all the letters of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>EXAMINATION</mi></math>. The probability that the letter <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> appears at the fourth position in any such word is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>66</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>11</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>11</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>11</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>EXAMINATION</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AAEIIMNNOTX</mi></math></p><p>Given word has <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>'</mo><mi>s</mi><mo>&#8594;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>I</mi><mo>'</mo><mi>s</mi><mo>&#8594;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>N</mi><mo>'</mo><mi>s</mi><mo>&#8594;</mo><mn>2</mn></math> and rest other are distinct alphabets.</p><p>Total number of ways to form words using the alphabets of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>EXAMINATION</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>11</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>2</mn><mo>!</mo></mrow></mfrac></math></p><p>Now, putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mi>th</mi></msup></math> position</p><p>.<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mi>M</mi><mo>-</mo><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mo>-</mo></math></p><p>Total words with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> at fourth Place <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>&#160;</mo><mn>2</mn><mo>!</mo><mo>&#160;</mo><mn>2</mn><mo>!</mo></mrow></mfrac></math></p><p>Required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mn>11</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>11</mn></mfrac></math></p>

</details>

---

### Q46. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two dices are rolled. If both dices have six faces numbered <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>,</mo></math> then the probability that the sum of the numbers on the top faces is less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>36</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>12</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>36</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>S</mi></mfenced><mo>=</mo><mn>36</mn></math></p><p>The possible ordered pairs are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mspace linebreak="newline"/><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mspace linebreak="newline"/><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mspace linebreak="newline"/><mfenced><mrow><mn>5</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>5</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mspace linebreak="newline"/><mfenced><mrow><mn>7</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mn>5</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>17</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mn>17</mn><mn>36</mn></mfrac></math></p>

</details>

---

### Q47. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"></math>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> denote the event that a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>-digit integer formed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></math> without repetitions, be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> . Then probability of event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is equal to :<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>56</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>27</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p>Total cases : <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="bottom"><mn>6</mn></menclose><mo>&#183;</mo><menclose notation="bottom"><mn>6</mn></menclose><mo>&#183;</mo><menclose notation="bottom"><mn>5</mn></menclose><mo>&#183;</mo><menclose notation="bottom"><mn>4</mn></menclose><mo>&#183;</mo><menclose notation="bottom"><mn>3</mn></menclose><mo>&#183;</mo><menclose notation="bottom"><mn>2</mn></menclose></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>s</mi></mfenced><mo>=</mo><mn>6</mn><mo>&#183;</mo><mn>6</mn><mo>&#160;</mo><mo>!</mo></math></p><p>Favourable cases :</p><p>Number divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#8801;</mo></math> Sum of digits must be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p>Case-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></math></p><p>Number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>!</mo></math></p><p>Case-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></math></p><p>Number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#183;</mo><mn>5</mn><mo>&#160;</mo><mo>!</mo></math></p><p>Case-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>III</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math></p><p>Number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#183;</mo><mn>5</mn><mo>&#160;</mo><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>(</mo></math> favourable <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>!</mo><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>5</mn><mo>&#183;</mo><mn>5</mn><mo>&#160;</mo><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#160;</mo><mo>!</mo><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>5</mn><mo>&#183;</mo><mn>5</mn><mo>&#160;</mo><mo>!</mo></mrow><mrow><mn>6</mn><mo>&#183;</mo><mn>6</mn><mo>&#160;</mo><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q48. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A seven digit number is formed using digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn></math>. The probability, that number so formed is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>7</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mn>7</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac></math>**

**Detailed Solution:**

<p>Digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn></math></p><p>Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> digit numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo><mn>3</mn><mo>!</mo></mrow></mfrac></math></p><p>Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> digit number divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>last digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c850d89b-bd77-48ba-98dc-5180bfb02526-image.png" style="width: 416px; height: 120px;" /></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> digit numbers which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac></math>
Required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mstyle displaystyle="true"><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>7</mn></mfrac></math></p>

</details>

---

### Q49. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a set of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> -digit natural numbers whose exactly one digit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>. Then the probability that a randomly chosen element of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> leaves remainder <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> when divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>122</mn><mn>297</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>97</mn><mn>297</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>97</mn><mn>297</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>s</mi></mfenced><mo>=</mo><mi>n</mi></math>( when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> appears on thousands place ) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>n</mi></math>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> does not appear on thousands place)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>9</mn><mo>+</mo><mn>8</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>33</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mi>n</mi></math>( last digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>7</mn></math> appears once)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>n</mi></math>( last digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> appears once)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>9</mn><mo>+</mo><mfenced><mrow><mn>9</mn><mo>&#215;</mo><mn>9</mn><mo>+</mo><mn>8</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mrow><mn>8</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>9</mn><mo>+</mo><mn>9</mn><mo>&#215;</mo><mn>25</mn></mrow><mrow><mn>33</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>9</mn></mrow></mfrac><mo>=</mo><mfrac><mn>97</mn><mn>297</mn></mfrac></math></p>

</details>

---

### Q50. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The coefficients <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> of the quadratic equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> are obtained by throwing a dice three times. The probability that this equation has equal roots is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>72</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>36</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>54</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>216</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>216</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#8712;</mo><mo>{</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>}</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>(</mo><mi>s</mi><mo>)</mo><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>216</mn></math></p><p>For equal root <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>c</mi></math></p><p>Case I: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Case II: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>c</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>Case-III: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>c</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mn>216</mn></mfrac></math></p>

</details>

---

### Q51. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability that two randomly selected subsets of the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>}</mo></math> have exactly two elements in their intersection, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>65</mn><msup><mn>2</mn><mn>8</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>65</mn><msup><mn>2</mn><mn>7</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>35</mn><msup><mn>2</mn><mn>7</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>135</mn><msup><mn>2</mn><mn>9</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>135</mn><msup><mn>2</mn><mn>9</mn></msup></mfrac></math>**

**Detailed Solution:**

<p>Total subsets<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>5</mn></msup><mo>=</mo><mn>32</mn></math></p><p>Probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#215;</mo><msup><mn>3</mn><mn>3</mn></msup></mrow><mrow><mn>32</mn><mo>&#215;</mo><mn>32</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>27</mn></mrow><msup><mn>2</mn><mn>10</mn></msup></mfrac><mo>=</mo><mfrac><mn>135</mn><msup><mn>2</mn><mn>9</mn></msup></mfrac></math></p>

</details>

---

### Q52. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

An ordinary dice is rolled for a certain number of times. If the probability of getting an odd number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> times is equal to the probability of getting an even number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> times, then the probability of getting an odd number for odd number of times is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>32</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>16</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>16</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi mathvariant="italic">n</mi></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>n</mi><mo>=</mo><mn>5</mn></math></p><p>Probability of getting an odd number for odd number of times is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>5</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>5</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>5</mn></msup><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><mfenced><mrow><mn>5</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q53. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Out of 11 consecutive natural number if three numbers are selected at random (without repetition), then the probability that they are in A.P. with positive common difference is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>101</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>101</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>33</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>99</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>33</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi><mo>&#8658;</mo></math>sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mtext>&#38;</mtext><mo>&#160;</mo><mi>c</mi></math> is even and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> depends on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mtext>&#38;</mtext><mo>&#160;</mo><mi>c</mi></math></p><p>Thus, we can not choose all three independently, but we can choose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mtext>&#38;</mtext><mo>&#160;</mo><mi>c</mi></math></p><p>Moreover, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>c</mi></math> should be both either even or odd as their sum is even.</p><p>Out of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> consecutive natural numbers, either five are even and six are odd or six are even and five are odd.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>33</mn></mfrac></math></p>

</details>

---

### Q54. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a randomly chosen <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>- digit number is made from exactly two digits is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>135</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>150</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>134</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>121</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>135</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></math>**

**Detailed Solution:**

<p>Total number of five-digit numbers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mfenced><msup><mn>10</mn><mn>4</mn></msup></mfenced></math>.</p><p>Case I : Choosing two non-zero digits i.e. in <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts></math> ways.</p><p>So, number of five-digit numbers containing both digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>5</mn></msup><mo>-</mo><mn>2</mn></math>.</p><p>Case II : Choose one non-zero and one zero as digit i.e. in <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts></math> ways.</p><p>So, number of five-digit numbers containing one non-zero and one zero both <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>4</mn></msup><mo>-</mo><mn>1</mn></math>.</p><p>So, favourable number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mfenced><mrow><msup><mn>2</mn><mn>5</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mfenced><mrow><msup><mn>2</mn><mn>4</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>36</mn><mfenced><mn>30</mn></mfenced><mo>+</mo><mn>9</mn><mfenced><mn>15</mn></mfenced><mo>=</mo><mn>1080</mn><mo>+</mo><mn>135</mn><mo>=</mo><mn>1215</mn></math></p><p>Thus, required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1215</mn><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>135</mn><msup><mn>10</mn><mn>4</mn></msup></mfrac></math>.</p>

</details>

---

### Q55. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mn>10</mn></math> different balls are to be placed in <math><mn>4</mn></math> distinct boxes at random, then the probability that two of these boxes contain exactly <math><mn>2</mn></math> and <math><mn>3</mn></math> balls is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>965</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>11</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>965</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>945</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>945</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>11</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>945</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>Total number of ways in which 10 balls can be placed in 4 boxes =<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>4</mn><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mn>20</mn></msup></math></p><p> Exactly two box contain <math><mn>2</mn><mo>,</mo><mi></mi><mn>3</mn></math> balls </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>&#215;</mo><msup><mn>2</mn><mn>5</mn></msup></math></p><p>Probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>&#215;</mo><msup><mn>2</mn><mn>5</mn></msup></mrow><msup><mn>2</mn><mn>20</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>945</mn><msup><mn>2</mn><mn>10</mn></msup></mfrac></math></p>

</details>

---

### Q56. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>In a random experiment, a fair die is rolled until two fours are obtained in succession. The probability that the experiment will end in the fifth throw of the die is equal to :</p>

**Options:**

- **(A)** <math><mfrac><mrow><mn>150</mn></mrow><mrow><msup><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>175</mn></mrow><mrow><msup><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>225</mn></mrow><mrow><msup><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>200</mn></mrow><mrow><msup><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>175</mn></mrow><mrow><msup><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>The probability of getting a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> in a throw of a die is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>.</p><p>The probability of getting other than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mn>4</mn></menclose></math> i.e. numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>&#38;</mo><mo>&#160;</mo><mn>6</mn></math> in a single throw of a die is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac></math>.</p><p>Total throws done <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math>.</p><p>For the event to be completed in <math><msup><mrow><mn>5</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> throw, <math><msup><mrow><mn>4</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> and <math><msup><mrow><mn>5</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> throw must be <math><mn>4</mn></math> . Also, <math><msup><mrow><mn>3</mn></mrow><mrow><mi>r</mi><mi>d</mi></mrow></msup></math> throw must be other than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mn>4</mn></menclose></math>. Hence, cases for the first two position can be :</p><p>Case I : <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mrow><mi>s</mi><mi>t</mi></mrow></msup></math> throw must be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mi>n</mi><mi>d</mi></mrow></msup></math> throw must not be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mn>4</mn></menclose></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mn>4</mn><mover><mn>4</mn><mo>-</mo></mover><mover><mn>4</mn><mo>-</mo></mover><mn>44</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>25</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac></math>.</p><p>Case II : <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mrow><mi>s</mi><mi>t</mi></mrow></msup></math> throw must not be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> i.e.  <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mn>4</mn></menclose></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mi>n</mi><mi>d</mi></mrow></msup></math> throw must not be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mn>4</mn></menclose></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mover><mn>4</mn><mo>-</mo></mover><mover><mn>4</mn><mo>-</mo></mover><mover><mn>4</mn><mo>-</mo></mover><mn>44</mn></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>125</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac></math>.</p><p>Case III : <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mrow><mi>s</mi><mi>t</mi></mrow></msup></math> throw must not be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mn>4</mn></menclose></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mi>n</mi><mi>d</mi></mrow></msup></math> throw must be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mover><mn>4</mn><mo>-</mo></mover><mn>4</mn><mover><mn>4</mn><mo>-</mo></mover><mn>44</mn></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>.</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>25</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac></math>.</p><p>Therefore, probability that experiment will end in the fifth throw given that two fours occurred in succession will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>4</mn><mover><mn>4</mn><mo>-</mo></mover><mover><mn>4</mn><mo>-</mo></mover><mn>44</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mover><mn>4</mn><mo>-</mo></mover><mn>4</mn><mover><mn>4</mn><mo>-</mo></mover><mn>44</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mover><mn>4</mn><mo>-</mo></mover><mover><mn>4</mn><mo>-</mo></mover><mover><mn>4</mn><mo>-</mo></mover><mn>44</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>25</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>25</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>125</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>175</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac></math>.</p>

</details>

---

### Q57. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{S}=\{1,2, \ldots . ., 20\}$. A subset $\mathrm{B}$ of $\mathrm{S}$ is said to be "nice", if the sum of the elements of $\mathrm{B}$ is 203 . Than the probability that a randomly chosen subset of $S$ is "nice" is :

**Options:**

- **(A)** $\frac{7}{2^{20}}$
- **(B)** $\frac{5}{2^{20}}$
- **(C)** $\frac{4}{2^{20}}$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{2^{20}}$**

**Detailed Solution:**

Since total number of subsets of the set $S=2^{20}$

Now, the sum of all number from 1 to $20=\frac{20 \times 21}{2}=210$ Then, find the sets which has sum 7 .

(1) $\{7\}$

(2) $\{1,6\}$

(3) $\{2,5\}$

(4) $\{3,4\}$

(5) $\{1,2,4\}$

Then, there is only 5 sets which has sum 203

Hence required probability $=\frac{5}{2^{20}}$

</details>

---

### Q58. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>&#160;</mi><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> be three events, which are pair-wise independent and <math><mover accent="false"><mrow><mi>E</mi></mrow><mo>&#175;</mo></mover></math> denotes the complement of an event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>&#8745;</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mi>C</mi></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#8745;</mo><mover><mi>B</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>|</mo><mi>C</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mover><mi>A</mi><mo>&#175;</mo></mover></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>B</mi></mfenced></math>
- **(B)** <math><mi>P</mi><mfenced separators="|"><mrow><mover accent="false"><mrow><mi>A</mi></mrow><mo>&#175;</mo></mover></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mover accent="false"><mrow><mi>B</mi></mrow><mo>&#175;</mo></mover></mrow></mfenced></math>
- **(C)** <math><mi>P</mi><mfenced separators="|"><mrow><mover accent="false"><mrow><mi>A</mi></mrow><mo>&#175;</mo></mover></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mover accent="false"><mrow><mi>B</mi></mrow><mo>&#175;</mo></mover></mrow></mfenced></math>
- **(D)** <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mover accent="false"><mrow><mi>B</mi></mrow><mo>¯</mo></mover></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mover><mi>A</mi><mo>&#175;</mo></mover></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>B</mi></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#8745;</mo><mover><mi>B</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>|</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#8745;</mo><mover><mi>B</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>&#8745;</mo><mi>C</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mi>C</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mi>C</mi></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>C</mi></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mi>B</mi><mo>&#8745;</mo><mi>C</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>&#8745;</mo><mi>C</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mi>C</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mi>C</mi></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>A</mi></mfenced><mi>P</mi><mfenced separators="|"><mi>C</mi></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>B</mi></mfenced><mi>P</mi><mfenced separators="|"><mi>C</mi></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mi>C</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>A</mi></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>B</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi><mfenced separators="|"><mover><mi>A</mi><mo>&#175;</mo></mover></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>B</mi></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mover><mi>B</mi><mo>&#175;</mo></mover></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>A</mi></mfenced></math></p>

</details>

---

### Q59. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

A bag contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> red and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> black balls. A ball is drawn at random from the bag, its color is observed and this ball along with two additional balls of the same color are returned to the bag. If now a ball is drawn at random from the bag, then the probability that this drawn ball is red, is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/36c40418-2253-4ab9-a4cd-84f89e6770f3-image.png" style="width: 163px; height: 150px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/464f14ce-8d2e-4860-8106-10f32b9b479e-image.png" style="width: 327px; height: 150px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2fdf165d-686f-4300-9810-f62cc8752397-image.png" style="width: 444px; height: 150px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bfc6497a-9861-4d0f-8ccc-2c00157a333f-image.png" style="width: 460px; height: 150px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>:</mo></math> Ball drawn from bag is observed to be Red after <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> has occurred.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fc2ac4dd-6be9-472e-b63e-769d5816a867-image.png" style="width: 205px; height: 180px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>A</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>A</mi></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>B</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mfrac><mn>4</mn><mn>10</mn></mfrac></mfenced><mfenced><mfrac><mn>6</mn><mn>12</mn></mfrac></mfenced><mo>+</mo><mfenced><mfrac><mn>6</mn><mn>10</mn></mfrac></mfenced><mfenced><mfrac><mn>4</mn><mn>12</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>48</mn><mn>120</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p>

</details>

---

### Q60. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

From a group of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> men and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> women, four member committees are to be formed each of which must contain at least one women. Then the probability for these committees to have more women than men, is :

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>11</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>23</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>11</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>220</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>11</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Total number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mn>7</mn><mo>!</mo><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>3</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mn>8</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mn>9</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>8</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>9</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mn>10</mn><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>8</mn><mo>+</mo><mn>5</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>9</mn><mo>+</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>600</mn><mo>+</mo><mn>450</mn><mo>+</mo><mn>100</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>1155</mn></math></p><p>Total no. of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1155</mn></math>
No. of ways to form a committee having more women than men
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><msub><mi>c</mi><mn>1</mn></msub><mo>&#215;</mo><mn>10</mn><msub><mi>c</mi><msub><mi>c</mi><mn>1</mn></msub></msub><mo>+</mo><mn>5</mn><msub><mi>c</mi><mn>4</mn></msub><mo>=</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mn>9</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>105</mn></math></p><p>probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>105</mn><mn>1155</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>11</mn></mfrac></math></p>

</details>

---

### Q61. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If two different numbers are taken from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mn>10</mn></mrow></mfenced></math>; then the probability that their sum as well as absolute difference are both multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>55</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>12</mn></mrow><mrow><mn>55</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>14</mn></mrow><mrow><mn>45</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>55</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>55</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Required favourable cases are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p>So, favourable cases <math><mo>=</mo><mn>6</mn></math></p><p>Total cases <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>11</mn></msup><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>11</mn><mo>&#215;</mo><mn>10</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>55</mn></math></p><p>Hence, the required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>6</mn><mn>55</mn></mfrac></math></p>

</details>

---

### Q62. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> are any two events such that <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math> and <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>,</mo></math> then the conditional probability, <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow><mrow><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mo>&#8746;</mo><msup><mrow><mi>B</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></mrow></mfenced></mrow></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mo>'</mo></msup></math> denotes the complement of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math>, is equal to :

**Options:**

- **(A)** <math><mfrac><mrow><mn>11</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/546515465.jpg" style="width: 160px; height: 113px;" />

Given <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math> &amp; <math><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mrow><msup><mi>A</mi><mo>&#39;</mo></msup><mo>&#8746;</mo><msup><mi>B</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>=</mo><mi>P</mi><msup><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>&#39;</mo></msup></math>

<math><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math>

<math><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mfenced separators="|"><mrow><msup><mi>A</mi><mo>'</mo></msup><mo>&#8746;</mo><msup><mi>B</mi><mo>'</mo></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mo>'</mo></msup></mrow></mfenced></math>

<math><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mi>A</mi><mfenced separators="|"><mrow><msup><mi>A</mi><mo>'</mo></msup><mo>&#8746;</mo><msup><mi>B</mi><mo>'</mo></msup></mrow></mfenced></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mfenced separators="|"><mrow><msup><mi>A</mi><mo>'</mo></msup><mo>&#8746;</mo><msup><mi>B</mi><mo>'</mo></msup></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mrow><msup><mi>A</mi><mo>'</mo></msup><mo>&#8746;</mo><msup><mi>B</mi><mo>'</mo></msup></mrow></mfenced></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>20</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>17</mn></mrow><mrow><mn>20</mn></mrow></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>

</details>

---

### Q63. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If the lengths of the sides of a triangle are decided by the three throws of a single fair die, then the probability that the triangle is of maximum area given that it is an isosceles triangle, is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>69</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>26</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>21</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>69</mn></mrow></mfrac></math>**

**Detailed Solution:**

In a <math><mi mathvariant="normal">&#916;</mi></math> sum of two sides should be greater then the third side

It is given that <math><mi mathvariant="normal">&#916;</mi></math> is isosceles

<math><mo>&#8756;</mo></math> Total cases in which isosceles <math><mi mathvariant="normal">&#916;</mi></math> will come is

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>

Total cases <math> <mrow> <mo>=</mo><mn>27</mn><mo>&#215;</mo><mn>3</mn><mo>&#8722;</mo><mn>12</mn><mo>=</mo><mn>69</mn></mrow> </math>

Favorable cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math> 

Probability = <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>69</mn></mrow></mfrac><mo>.</mo></math>

</details>

---

### Q64. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">X</mi></math> be a set containing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> elements and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mfenced><mi mathvariant="normal">X</mi></mfenced></math> be its power set. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> are picked up at random from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mfenced><mi mathvariant="normal">X</mi></mfenced></math>, with replacement, then the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> have equal number of elements is:

**Options:**

- **(A)** <math><mfrac><mrow><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><msup><mrow></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>10</mn></mrow></msub></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msup><mrow/><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>10</mn></mrow></msub></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><msup><mrow></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>10</mn></mrow></msub></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>The power set of X will contain <math><msup><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></msup></math> elements where each element is subset of A in which 
<math><msup><mrow></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub></math> will contain <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>  element.
<math><msup><mrow></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> will contain <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> element.
<math><msup><mrow></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub></math> will contain <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> elements.
<math><mo>&#8942;</mo></math>

<math><mo>&#8942;</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>10</mn></msup><msub><mi>C</mi><mn>10</mn></msub></math>     will contain <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> elements.
So total numbers of ways in which we can select two sets with replacement is 
And favorable cases would be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mn>10</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mo>&#8901;</mo><mn>10</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mo>+</mo><mn>10</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>.</mo><mn>10</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mi>&#160;</mi><mo>&#8230;</mo><mo>&#8230;</mo><msup><mo>+</mo><mn>10</mn></msup><msub><mi>C</mi><mn>10</mn></msub><msup><mo>.</mo><mn>10</mn></msup><msub><mi>C</mi><mn>10</mn></msub><msup><mo>=</mo><mn>20</mn></msup><msub><mi>C</mi><mn>10</mn></msub></math>
Hence, Probability would be  <math><mo>=</mo><mi>&#160;</mi><mfrac><mrow><msup><mrow></mrow><mrow><mn>20</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>10</mn></mrow></msub></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup></mrow></mfrac></math>
 </p>

</details>

---

### Q65. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> be any two events with positive probabilities 

<strong>Statement I:</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>E</mi><mo>/</mo><mi>A</mi></mrow></mfenced><mo>&#8805;</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>.</mo></math>

<strong>Statement II:</strong> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>&#8805;</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>E</mi></mrow></mfenced><mo>.</mo></math>

**Options:**

- **(A)** Both the statements are false
- **(B)** Both the statements are true
- **(C)** Statement - <strong>I</strong> is false, Statement - <strong>II</strong> is true
- **(D)** Statement - <strong>I</strong> is true, Statement - <strong>II</strong> is false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Both the statements are true**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>E</mi><mo>/</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>A</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>A</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>/</mo><mi>A</mi></mrow></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>A</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>E</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>E</mi><mo>/</mo><mi>A</mi></mrow></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced></math></p><p>Now, since <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>/</mo><mi>A</mi></mrow></mfenced><mo>&#8805;</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced></math></p><p>Again, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>A</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>E</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>A</mi></mrow></mfenced></math></p><p>Now, since <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>&#8805;</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>E</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Both the statements are true.</p>

</details>

---

### Q66. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A number $\mathrm{x}$ is chosen at random from the set $\{1$, $2,3,4, \ldots ., 100\}$. Define the event: $\mathrm{A}=$ the chosen number $x$ satisfies $\frac{(x-10)(x-50)}{(x-30)} \geq 0$
Then $\mathrm{P}(\mathrm{A})$ is:

**Options:**

- **(A)** $0.71$
- **(B)** $0.70$
- **(C)** $0.51$
- **(D)** $0.20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.71$**

**Detailed Solution:**

Given $\frac{(x-10)(x-50)}{(x-30)} \geq 0$
Let $x \geq 10, x \geq 50$ equation will be true $\forall x \geq 50$ as $\left(\frac{x-50}{x-30}\right) \geq 0, \forall x \in[10,30)$
$$
\frac{(x-10)(x-50)}{x-30} \geq 0 \quad \forall x \in[10,30)
$$
Total value of $x$ between 10 to 30 is 20 . Total values of $x$ between 50 to 100 including 50 and 100 is 51 .
Total values of $x=51+20=71$
$$
P(\mathrm{~A})=\frac{71}{100}=0.71
$$

</details>

---

### Q67. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A set $\mathrm{S}$ contains 7 elements. A non-empty subset $A$ of $S$ and an element $x$ of $S$ are chosen at random. Then the probability that $\mathrm{x} \in \mathrm{A}$ is:

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{64}{127}$
- **(C)** $\frac{63}{128}$
- **(D)** $\frac{31}{128}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{64}{127}$**

**Detailed Solution:**

Let $\mathrm{S}=\left\{x_1, x_2, x_3, x_4, x_5, x_6, x_7\right\}$
Let the chosen element be $\mathrm{x}_{\mathrm{i}}$.
Total number of subsets of $\mathrm{S}=2^7=128$
No. of non-empty subsets of S $=128-1$ $=127$
We need to find number of those subsets that contains $x_i$.
\begin{array}{|l|l|l|l|l|l|l|}
\hline 2 & 2 & 2 & 2 & 1 & 2 & 2 \\
\hline
\end{array}
$x_1 x_2$-—- $x_i=-x_7$
For those subsets containing $x_i$, each element has 2 choices.
i.e., (included or not included) in subset, However as the subset must contain $x_i$, $x_i$ has only one choice. (included one)
So, total no. of subsets containing $x_i=2 \times 2 \times 2 \times 2 \times 1 \times 2 \times 2=64$
Required prob
$$
=\frac{\text { No. of subsets containing } x_i}{\text { Total no. of non-empty subsets }}
$$

$$
=\frac{64}{127}
$$

</details>

---

### Q68. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are two events such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math>, then the incorrect statement amongst the following statements is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mo>'</mo></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8201;</mo><mo>&#38;</mo><mo>&#8201;</mo><mi>B</mi></math> are equally likely
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>A</mi><mo>'</mo></msup><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math></p><p>Using the addition theorem of probability, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math></p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6549646263.png" style="width: 250px; height: 182px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mi>A</mi></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mi>B</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mi mathvariant="normal">&#39;</mi></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><msup><mi>A</mi><mi mathvariant="normal">&#39;</mi></msup><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are equally likely.</p><p>But we can&#39;t say that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mi>A</mi></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mi>B</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>&#8800;</mo><mn>1</mn></math></p>

</details>

---

### Q69. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `3`

A number $n$ is randomly selected from the set $\{1,2,3, \ldots ., 1000\}$. The probability that $\frac{\sum_{i=1}^n i^2}{\sum_{i=1}^n i}$ is an integer is

**Options:**

- **(A)** $0.331$
- **(B)** $0.333$
- **(C)** $0.334$
- **(D)** $0.332$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.334$**

**Detailed Solution:**

$\frac{\sum_{i=1}^n i^2}{\sum_{i=1}^n i}=\frac{\frac{n(n+1)(2 n+1)}{6}}{\frac{n(n+1)}{2}}=\frac{2 n+1}{3}$ For $n=1,2,3, \ldots . ., 1000$ Value of $\frac{2 n+1}{3}=\frac{3}{3}, \frac{5}{3}, \frac{7}{3}, \ldots \ldots \ldots, \frac{2001}{3}$ respectively. Out of $\frac{3}{3}, \frac{5}{3}, \frac{7}{3}, \ldots \ldots \ldots, \frac{2001}{3}$ only first term $\left(\frac{3}{3}=1\right)$, fourth term $\left(\frac{9}{3}=3\right), 667^{\text {th }}$ term $\left(\frac{2001}{3}=667\right)$ are integers.
Hence, out of 1000 values of $\frac{2 n+1}{3}$, total number of integral values of $\frac{2 n+1}{3}$ $=333+1=334$
$\therefore \quad$ Required probability $=\frac{334}{1000}=0.334$

</details>

---

### Q70. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

Three numbers are chosen at random without replacement from $\{1,2,3, \ldots . .8\}$. The probability that their minimum is $3$ , given that their maximum is $6$ , is

**Options:**

- **(A)** $\frac{3}{8}$
- **(B)** $\frac{1}{5}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{5}$**

**Detailed Solution:**

Let $A$ be the event that maximum is $6$. 
$B$ be event that minimum is $3$
$P(A)=\frac{{ }^5 C_2}{{ }^8 C_3}$ (the numbers $ < 6$ are $5$)
$P(B)=\frac{{ }^5 C_2}{{ }^8 C_3}$ (the numbers $>3$ are $5$)
$P(A \cap B)=\frac{{ }^2 C_1}{{ }^8 C_3}$
Required probability is $\mathrm{P}\left(\frac{\mathrm{B}}{\mathrm{A}}\right)=\frac{\mathrm{P}(\mathrm{A} \cap \mathrm{B})}{\mathrm{P}(\mathrm{A})}=\frac{{ }^2 \mathrm{C}_1}{{ }^5 \mathrm{C}_2}=\frac{2}{10}=\frac{1}{5}$.

</details>

---

### Q71. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `1`

If $C$ and $D$ are two events such that $C \subset D$ and $P(D) \neq 0$, then the correct statement among the following is

**Options:**

- **(A)** $P(C \mid D) \geq P(C)$
- **(B)** $P(C \mid D) < P(C)$
- **(C)** $P(C \mid D)=\frac{P(D)}{P(C)}$
- **(D)** $P(C \mid D)=P(C)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $P(C \mid D) \geq P(C)$**

**Detailed Solution:**

$\mathrm{C} \cap \mathrm{D}=\mathrm{C} \Rightarrow \mathrm{P}(\mathrm{C} \cap \mathrm{D})=\mathrm{P}(\mathrm{C}) \Rightarrow \mathrm{P}\left(\frac{\mathrm{C}}{\mathrm{D}}\right)=\frac{\mathrm{P}(\mathrm{C} \cap \mathrm{D})}{\mathrm{P}(\mathrm{D})} \geq \mathrm{P}(\mathrm{C})$

</details>

---

### Q72. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

Four numbers are chosen at random (without replacement) from the set $\{1,2,3, \ldots ., 20\}$.
Statement-1: The probability that the chosen numbers when arranged in some order will form an AP is $\frac{1}{85}$.
Statement-2: If the four chosen numbers from an AP, then the set of all possible values of common difference is $\{\pm 1, \pm 2, \pm 3, \pm 4, \pm 5\}$.

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is not the correct explanation for Statement-1
- **(B)** Statement-1 is true, Statement-2 is false
- **(C)** Statement-1 is false, Statement-2 is true
- **(D)** Statement-1 is true, Statement-2 is true; Statement-2 is the correct explanation for Statement-1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement-1 is true, Statement-2 is false**

**Detailed Solution:**

$$
\mathrm{N}(\mathrm{S})={ }^{20} \mathrm{C}_4
$$
Statement-1: common difference is 1 ; total number of cases $=17$ common difference is 2 ; total number of cases $=14$ common difference is 3 ; total number of cases $=11$ common difference is 4 ; total number of cases $=8$ common difference is 5 ; total number of cases $=5$ common difference is 6 ; total number of cases $=2$
$$
\text { Prob. }=\frac{17+14+11+8+5+2}{{ }^{20} \mathrm{C}_4}=\frac{1}{85} \text {. }
$$

</details>

---

### Q73. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

One ticket is selected at random from 50 tickets numbered $00,01,02, \ldots, 49$. Then the probability that the sum of the digits on the selected ticket is 8 , given that the product of these digits is zero, equals

**Options:**

- **(A)** $\frac{1}{14}$
- **(B)** $\frac{1}{7}$
- **(C)** $\frac{5}{14}$
- **(D)** $\frac{1}{50}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{14}$**

**Detailed Solution:**

$$
S=\{00,01,02, \ldots .49\}
$$
Let $A$ be the even that sum of the digits on the selected ticket is 8 then
$$
A=\{08,17,26,35,44\}
$$
Let $B$ be the event that the product of the digits is zero
$$
B=\{00,01,02,03, \ldots .09,10,20,30,40\}
$$
$A \cap B=\{8\}$
$$
\text { Required probability }=P(A / B)=\frac{P(A \cap B)}{P(B)}=\frac{\frac{1}{50}}{\frac{14}{50}}=\frac{1}{14}
$$

</details>

---

### Q74. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

It is given that the events $A$ and $B$ are such that $P(A)=\frac{1}{4}, P\left(\frac{A}{B}\right)=\frac{1}{2}$ and $P\left(\frac{B}{A}\right)=\frac{2}{3}$. Then $P(B)$ is

**Options:**

- **(A)** $\frac{1}{6}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}$**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{P(A \cap B)}{P(B)}=\frac{1}{2}, \frac{P(A \cap B)}{P(A)}=\frac{2}{3} \\
& \text { Hence } \frac{P(A)}{P(B)}=\frac{3}{4} . \quad(\text { But } P(A)=1 / 4) \\
& \Rightarrow P(B)=\frac{1}{3} .
\end{aligned}
$$

</details>

---

### Q75. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

A pair of fair dice is thrown independently three times. The probability of getting a score of exactly $9$ twice is

**Options:**

- **(A)** $1 / 729$
- **(B)** $8 / 9$
- **(C)** $8 / 729$
- **(D)** $8 / 243$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $8 / 243$**

**Detailed Solution:**

Probability of getting score $9$ in a single throw $=\frac{4}{36}=\frac{1}{9}$
Probability of getting score $9$ exactly twice $={ }^3 \mathrm{C}_2 \times\left(\frac{1}{9}\right)^2 \times \frac{8}{9}=\frac{8}{243}$.

</details>

---

### Q76. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

Three houses are available in a locality. Three persons apply for the houses. Each applies for one house without consulting others. The probability that all the three apply for the same house is

**Options:**

- **(A)** $\frac{2}{9}$
- **(B)** $\frac{1}{9}$
- **(C)** $\frac{8}{9}$
- **(D)** $\frac{7}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{9}$**

**Detailed Solution:**

For a particular house being selected
Probability $=\frac{1}{3}$
Prob(all the persons apply for the same house) $=\left(\frac{1}{3} \times \frac{1}{3} \times \frac{1}{3}\right) 3=\frac{1}{9}$

</details>

---

### Q77. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

Five horses are in a race. Mr. A selects two of the horses at random and bets on them. The probability that Mr. A selected the winning horse is

**Options:**

- **(A)** $\frac{2}{5}$
- **(B)** $\frac{4}{5}$
- **(C)** $\frac{3}{5}$
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{5}$**

**Detailed Solution:**

$\mathrm{n}(\mathrm{S})={ }^5 \mathrm{C}_2 ; \mathrm{n}(\mathrm{E})={ }^2 \mathrm{C}_1+{ }^2 \mathrm{C}_1$
$\mathrm{p}(\mathrm{E})=\frac{\mathrm{n}(\mathrm{E})}{\mathrm{n}(\mathrm{S})}=\frac{{ }^2 \mathrm{C}_1+{ }^2 \mathrm{C}_1}{{ }^5 \mathrm{C}_2}=\frac{2}{5}$

</details>

---

### Q78. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$A$ and $B$ are events such that $P(A \cup B)=3 / 4, P(A \cap B)=1 / 4, P(\bar{A})=2 / 3$ then $P(\bar{A} \cap B)$ is

**Options:**

- **(A)** 5/12
- **(B)** 3/8
- **(C)** 5/8
- **(D)** 1/4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5/12**

**Detailed Solution:**

$P(A \cup B)=P(A)+P(B)-P(A \cap B) \Rightarrow \frac{3}{4}=1-P(\bar{A})+P(B)-\frac{1}{4}$
$\Rightarrow 1=1-\frac{2}{3}+P(B) \Rightarrow P(B)=\frac{2}{3} ; \quad$ Now, $P(\bar{A} \cap B)=P(B)-P(A \cap B)=\frac{2}{3}-\frac{1}{4}=\frac{5}{12}$

</details>

---

