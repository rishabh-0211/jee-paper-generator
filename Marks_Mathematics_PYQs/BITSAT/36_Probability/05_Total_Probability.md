# BITSAT Mathematics - Probability

## Topic 5: Total Probability

**Total Questions:** 9

---

### Q1. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability that certain electronic component fails when first used is 0.10 . If it does not fail immediately, the probability that it lasts for one year is 0.99 . The probability that a new component will last for one year is

**Options:**

- **(A)** $0.9$
- **(B)** $0.01$
- **(C)** $0.119$
- **(D)** $0.891$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.891$**

**Detailed Solution:**

$P$ (The electronic component fails when first
$\begin{aligned}
& \text { used })=P(F)=0.10 \\
& \therefore P(\bar{F})=1-P(F)=0.90
\end{aligned}$
Let $E$ be the event that a new component will last for one year, then
$P(E)=P(F) \cdot P\left(\frac{E}{F}\right)+P(\bar{F}) P\left(\frac{E}{\bar{F}}\right)$
[Total probability theorem]
$=0.10 \times 0+0.90 \times 0.99=0.891$

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

A book contains 1000 pages. A page is chosen at random. The probability that the sum of the digits of the marked number on the page is equal to 9 , is

**Options:**

- **(A)** $\frac{23}{500}$
- **(B)** $\frac{11}{200}$
- **(C)** $\frac{7}{100}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{11}{200}$**

**Detailed Solution:**

$n(S)=$ Total number of ways $=1000$
The favourable cases that the sum of the digits of the marked number on the page is equal to 9 are one digit number or two digits numbers or three digits numbers, if three digit number is $a b c$. 
Then,
$a+b+c=9 ; 0 \leq a, b, c \leq 9$.
$\therefore n(E)=$ Number of favourable ways
$=$ Number of solutions of the equation
$={ }^{9+3-1} C_{3-1}={ }^{11} C_2=55$
$\therefore$ Required probability
$=\frac{n(E)}{n(S)}=\frac{55}{1000}=\frac{11}{200}$.

</details>

---

### Q3. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Bag $P$ contains 6 red and 4 blue balls and bag $Q$ contains 5 red and 6 blue balls. A ball is transferred from bag $P$ to bag $Q$ and then a ball is drawn from bag $Q$. What is the probability that the ball drawn is blue?

**Options:**

- **(A)** $\frac{7}{15}$
- **(B)** $\frac{8}{15}$
- **(C)** $\frac{4}{19}$
- **(D)** $\frac{8}{19}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{8}{15}$**

**Detailed Solution:**

Let $E_1, E_2$ and $A$ be the events defined as follows:
$\mathrm{E}_1=$ red ball is transferred from bag $\mathrm{P}$ to bag $\mathrm{Q}$
$\mathrm{E}_2=$ blue ball is transferred from bag $\mathrm{P}$ to bag $\mathrm{Q}$
$\mathrm{A}=$ the ball drawn from bag $\mathrm{Q}$ is blue
As the bag $\mathrm{P}$ contains 6 red and 4 blue balls,
$P\left(E_1\right)=\frac{6}{10}=\frac{3}{5} \text { and } P\left(E_2\right)=\frac{4}{10}=\frac{2}{5}$
Note that $E_1$ and $E_2$ are mutually exclusive and exhaustive events.
When $E_1$ has occurred i.e., a red ball has already been transferred from bag $P$ to $Q$, then bag $Q$ will contain 6 red and 6 blue balls, So, $P\left(A \mid E_1\right)=$$\frac{6}{12}=\frac{1}{2}$
When $E_2$ has occurred i.e., a blue ball has already been transferred from bag $P$ to $Q$, then bag $Q$ will contain 5 red and 7 blue balls, So, $P\left(A \mid E_2\right)=$$\frac{7}{12}$
By using law of total probability, we get
$P(A)=P\left(E_1\right) P\left(A \mid E_1\right)+P\left(E_2\right) P\left(A \mid E_2\right)$
$=\frac{3}{5} \times \frac{1}{2}+\frac{2}{5} \times \frac{7}{12}=\frac{8}{15}$

</details>

---

### Q4. BITSAT 2020

*Type:* `singleCorrect` | *Level:* `3`

The probability that certain electronic component fails when first used is 0.10 . If it does not fail immediately, the probability that it lasts for one year is $0.99 .$ The probability that a new component will last for one year is

**Options:**

- **(A)** 0.99
- **(B)** 0.871
- **(C)** 0.891
- **(D)** 0.762

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0.891**

**Detailed Solution:**

Probability that the electronic component fails when first used is $P(F)=0.10$. Therefore, $P\left(F^{\prime}\right)=1-P(F)=0.90$

Let $E$ be the event that a new component will last for one year.

$\text { Then, } P(E)=P(F) P\left(\frac{E}{F}\right)+P\left(F^{\prime}\right) P\left(\frac{E}{F^{\prime}}\right)$

[total probability theorem] $=0.10 \times 0+0.90 \times 0.99=0.891$

</details>

---

### Q5. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `2`

A bag contains 3 red and 3 white balls. Two balls are drawn one by one. The probability that they are of different colours is.

**Options:**

- **(A)** $3 / 10$
- **(B)** $2 / 5$
- **(C)** $3 / 5$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3 / 5$**

**Detailed Solution:**

Let $\mathrm{A} \equiv$ event that drawn ball is red $\mathrm{B} \equiv$ event that drawn ball is white Then $\mathrm{AB}$ and $\mathrm{BA}$ are two disjoint cases of the given event.

$$

\begin{array}{l}

\therefore P(A B+B A)=P(A B)+P(B A) \\

=P(A) \quad P\left(\frac{B}{A}\right)+P(B) \quad P\left(\frac{A}{B}\right)

\end{array}

$$

$=\frac{3}{6} \cdot \frac{3}{5}+\frac{3}{6} \cdot \frac{3}{5}=\frac{3}{5}$

</details>

---

### Q6. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `2`

A bag contains $(2 n+1)$ coins. It is known that n of these coins have a head on both sides, whereas the remaining $(\mathrm{n}+1)$ coins are fair. A coin is picked up at random from the bag and tossed. If the probability that the toss results in a head is $31 / 42,$ then $\mathrm{n}$ is equal to

**Options:**

- **(A)** 10
- **(B)** 11
- **(C)** 12
- **(D)** 13

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 10**

**Detailed Solution:**

Total number of coins $=2 \mathrm{n}+1$

Consider the following events:

$\mathrm{E}_{1}=$ Getting a coin having head on both

sides from the bag.

$\mathrm{E}_{2}=$ Getting a fair coin from the bag

$\mathrm{A}=$ Toss results in a head

Given: $\mathrm{P}(\mathrm{A})=\frac{31}{42}, \mathrm{P}\left(\mathrm{E}_{1}\right)=\frac{\mathrm{n}}{2 \mathrm{n}+1}$

and $\mathrm{P}\left(\mathrm{E}_{2}\right)=\frac{\mathrm{n}+1}{2 \mathrm{n}+1}$

Then,

$\mathrm{P}(\mathrm{A})=\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\mathrm{A} / \mathrm{E}_{1}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\mathrm{A} / \mathrm{E}_{2}\right)$

$\Rightarrow \frac{31}{42}=\frac{n}{2 n+1} \times 1+\frac{n+1}{2 n+1} \times \frac{1}{2}$

$\frac{31}{42}=\frac{n}{2 n+1}+\frac{n+1}{2(2 n+1)}$

$\Rightarrow \frac{31}{42}=\frac{3 n+1}{2(2 n+1)}$

$\Rightarrow \frac{31}{21}=\frac{3 n+1}{2 n+1}$

$n=10$

</details>

---

### Q7. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `1`

A bag contains $n+1$ coins. It is known that one of these coins shows heads on both sides, whereas the other coins are fair. One coin is selected at random and tossed. If the probability that toss results in heads is $\frac{7}{12},$ then the value of $n$ is.

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 5
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

Let $E_{1}$ denote the event "a coin with head on both sides is selected" and $\mathrm{E}_{2}$ denotes the event " a fair coin is selected". Let $A$ be

the event " he toss, results in heads".

$$

\begin{array}{l}

\therefore \mathrm{P}\left(\mathrm{E}_{1}\right)=\frac{1}{n+1}, \mathrm{P}\left(\mathrm{E}_{2}\right)=\frac{n}{n+1} \text { and } \\

\mathrm{P}\left(\frac{\mathrm{A}}{\mathrm{E}_{1}}\right)=1, \mathrm{P}\left(\frac{\mathrm{A}}{\mathrm{E}_{2}}\right)=\frac{1}{2} \\

\therefore \mathrm{P}(\mathrm{A})=\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\frac{\mathrm{A}}{\mathrm{E}_{1}}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\frac{\mathrm{A}}{\mathrm{E}_{2}}\right) \\

\Rightarrow \frac{7}{12}=\frac{1}{n+1} \times 1+\frac{n}{n+1} \times \frac{1}{2} \\

\Rightarrow 14 n+14=24+12 n \Rightarrow n=5

\end{array}

$$

</details>

---

### Q8. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `1`

A bag contains 5 brown and 4 white socks. $A$ man pulls out 2 socks. Find the probability that they are of the same colour.

**Options:**

- **(A)** $\frac{4}{9}$
- **(B)** $\frac{2}{9}$
- **(C)** $\frac{5}{9}$
- **(D)** $\frac{7}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{9}$**

**Detailed Solution:**

Let $A \equiv$ event of two socks being brown. $\mathrm{B} \equiv$ event of two socks being white.

$$

\text { Then } \begin{aligned}

& P(A)=\frac{{ }^{5} C_{2}}{{ }^{9} C_{2}}=\frac{5.4}{9.8}=\frac{5}{18}, \mathrm{P}(\mathrm{B}) \\

&=\frac{{ }^{4} \mathrm{C}_{2}}{{ }^{9} \mathrm{C}_{2}}=\frac{4.3}{9.8}=\frac{3}{18}

\end{aligned}

$$

Now, since $\mathrm{A}$ and $\mathrm{B}$ are mutually exclusive events, so required probability

$$

=\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})=\frac{5}{18}+\frac{3}{18}=\frac{4}{9}

$$

</details>

---

### Q9. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `2`

The probability of India winning a test match against West Indies is $1 / 2$. Assuming independence from match to match, the probability that in a 5 match series India's second win occurs at the third test, is -

**Options:**

- **(A)** $2 / 3$
- **(B)** $1 / 2$
- **(C)** $1 / 4$
- **(D)** $1 / 8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 / 4$**

**Detailed Solution:**

The sample space is [LWW, WLW]

$$

\therefore P(\mathrm{LWW})+\mathrm{P}(\mathrm{WLW})

$$

= Probability that in 5 match series, it is India's second win

$$

\begin{array}{l}

=P(\mathrm{~L}) \mathrm{P}(\mathrm{W}) \mathrm{P}(\mathrm{W})+\mathrm{P}(\mathrm{W}) \mathrm{P}(\mathrm{L}) \mathrm{P}(\mathrm{W}) \\

=\frac{1}{8}+\frac{1}{8}=\frac{2}{8}=\frac{1}{4}

\end{array}

$$

</details>

---

