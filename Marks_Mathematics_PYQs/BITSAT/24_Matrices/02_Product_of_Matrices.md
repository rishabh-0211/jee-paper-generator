# BITSAT Mathematics - Matrices

## Topic 2: Product of Matrices

**Total Questions:** 6

---

### Q1. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}1 & 0 \\ 0 & -1\end{array}\right], P=\left[\begin{array}{ll}1 & 1 \\ 0 & 1\end{array}\right]$ and $X=A P A^T$, then $A^T X^{50} A=$

**Options:**

- **(A)** $\left[\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}2 & 1 \\ 0 & -1\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}25 & 1 \\ 1 & -25\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}1 & 50 \\ 0 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{cc}1 & 50 \\ 0 & 1\end{array}\right]$**

**Detailed Solution:**

Since $A A^T=I$ therefore matrix $A$ is orthogonal matrix.
Now, $A^T X^{50} A=A^T X^{49}\left(A P A^T\right) A$
$=A^T X^{49} A P\left(A^T A\right)=A^T X^{49} A P$
$=A^T X^{48}\left(A P A^T\right) A P=A^T X^{48} A P^2 \ldots \ldots$.
$=A^T A P^{50}=I P^{50}=P^{50}$
$\because \quad P=\left[\begin{array}{ll}1 & 1 \\ 0 & 1\end{array}\right] \Rightarrow P^2=\left[\begin{array}{ll}1 & 2 \\ 0 & 1\end{array}\right]$
$\Rightarrow P^3=\left[\begin{array}{ll}1 & 3 \\ 0 & 1\end{array}\right] \ldots .$.
$\Rightarrow \quad P^{50}=\left[\begin{array}{cc}1 & 50 \\ 0 & 1\end{array}\right]$
So, $A^T X^{50} A=P^{50}=\left[\begin{array}{cc}1 & 50 \\ 0 & 1\end{array}\right]$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

$$
\text { If } A=\left[\begin{array}{ccc}
0 & c & -b \\
-c & 0 & a \\
b & -a & 0
\end{array}\right] \text { and } B=\left[\begin{array}{ccc}
a^2 & a b & a c \\
a b & b^2 & b c \\
a c & b c & c^2
\end{array}\right] \text {, }
$$
then $A B$ is equal to

**Options:**

- **(A)** B
- **(B)** A
- **(C)** O
- **(D)** I

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) O**

**Detailed Solution:**

$\begin{aligned} &\quad A B=\left[\begin{array}{ccc}0 & c & -b \\ -c & 0 & a \\ b & -a & 0\end{array}\right]\left[\begin{array}{ccc}a^2 & a b & a c \\ a b & b^2 & b c \\ a c & b c & c^2\end{array}\right] \\ & A B=\left[\begin{array}{ccc}a b c-a b c & b^2 c-b^2 c & b c^2-b c^2 \\ -a^2 c+a^2 c & -a b c+a b c & -a c+a c \\ a^2 b-a^2 b & a b^2-a b^2 & a b c-a b c\end{array}\right] \\ & =\left[\begin{array}{lll}0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right]=\mathrm{O} \\ & \end{aligned}$

</details>

---

### Q3. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}=\left[\begin{array}{ll}1 & 1 \\ 1 & 1\end{array}\right]$ then $\mathbf{A}^{100}$ :

**Options:**

- **(A)** $2^{100} \mathrm{~A}$
- **(B)** $2^{99} \mathrm{~A}$
- **(C)** $2^{101} \mathrm{~A}$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2^{99} \mathrm{~A}$**

**Detailed Solution:**

Let $A=\left[\begin{array}{ll}1 & 1 \\ 1 & 1\end{array}\right]$

$$

\begin{array}{l}

\mathrm{A}^{2}=\left[\begin{array}{ll}

1 & 1 \\

1 & 1

\end{array}\right]\left[\begin{array}{ll}

1 & 1 \\

1 & 1

\end{array}\right]=2\left[\begin{array}{ll}

1 & 1 \\

1 & 1

\end{array}\right]=2 \mathrm{~A} \\

\mathrm{~A}^{3}=2^{2}\left[\begin{array}{ll}

1 & 1 \\

1 & 1

\end{array}\right], \mathrm{A}^{4}=2^{3}\left[\begin{array}{ll}

1 & 1 \\

1 & 1

\end{array}\right] \\

\mathrm{A}^{3}=2^{2} \mathrm{~A}, \quad \mathrm{~A}^{4}=2^{3} \mathrm{~A} \\

\therefore \mathrm{A}^{\mathrm{n}}=2^{\mathrm{n}-1}\left[\begin{array}{ll}

1 & 1 \\

1 & 1

\end{array}\right] \\

\Rightarrow \mathrm{A}^{100}=2^{100-1} \mathrm{~A} \therefore \mathrm{A}^{100}=2^{99} \mathrm{~A}

\end{array}

$$

</details>

---

### Q4. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\left[\begin{array}{ll}0 & \alpha \\ 0 & 0\end{array}\right]$ and $(A+I)^{50}-50 A=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$,
find $a b c+a b d+b c d+a c d$

**Options:**

- **(A)** 0
- **(B)** -1
- **(C)** 1
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

As $\mathrm{A}^{2}=0, \mathrm{~A}^{k}=0 \forall k \geq 2$
Thus, $\quad(\mathrm{A}+\mathrm{I})^{50}=\mathrm{I}+50 \mathrm{~A} \Rightarrow(\mathrm{A}+\mathrm{I})^{50}-50 \mathrm{~A}=\mathrm{I}$
$\therefore \quad \mathrm{a}=1, \mathrm{~b}=0, \mathrm{c}=0, \mathrm{~d}=1$
$\mathrm{abc}+\mathrm{abd}+\mathrm{bed}+\mathrm{acd}=0$

</details>

---

### Q5. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `1`

The matrix \(A^2+4 A-5 I\), where \(I\) is identity matrix and \(A=\left[\begin{array}{cc}1 & 2 \\ 4 & -3\end{array}\right]\), equals :

**Options:**

- **(A)** \(4\left[\begin{array}{ll}2 & 1 \\ 2 & 0\end{array}\right]\)
- **(B)** \(4\left[\begin{array}{cc}0 & -1 \\ 2 & 2\end{array}\right]\)
- **(C)** \(32\left[\begin{array}{ll}2 & 1 \\ 2 & 0\end{array}\right]\)
- **(D)** \(32\left[\begin{array}{ll}1 & 1 \\ 1 & 0\end{array}\right]\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \(4\left[\begin{array}{ll}2 & 1 \\ 2 & 0\end{array}\right]\)**

**Detailed Solution:**

\(\begin{aligned}
& A^2+4 A-5 I=A \times A+4 A-5 I \\
= & {\left[\begin{array}{cc}
1 & 2 \\
4 & -3
\end{array}\right] \times\left[\begin{array}{cc}
1 & 2 \\
4 & -3
\end{array}\right]+4\left[\begin{array}{cc}
1 & 2 \\
4 & -3
\end{array}\right]-5\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right] } \\
= & {\left[\begin{array}{cc}
9 & -4 \\
-8 & 17
\end{array}\right]+\left[\begin{array}{cc}
4 & 8 \\
16 & -12
\end{array}\right]-\left[\begin{array}{cc}
5 & 0 \\
0 & 5
\end{array}\right] } \\
= & {\left[\begin{array}{cc}
9+4-5 & -4+8-0 \\
-8+16-0 & 17-12-5
\end{array}\right]=\left[\begin{array}{cc}
8 & 4 \\
8 & 0
\end{array}\right] } \\
= & 4\left[\begin{array}{cc}
2 & 1 \\
2 & 0
\end{array}\right]
\end{aligned}\)

</details>

---

### Q6. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `1`

Find the value of
\(2 \tan ^{-1} \frac{1}{5}+\tan ^{-1} \frac{1}{2}+2 \tan ^{-1} \frac{1}{8}\)

**Options:**

- **(A)** \(\pi / 4\)
- **(B)** \(\pi / 2\)
- **(C)** \(3 \pi / 4\)
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \(\pi / 4\)**

**Detailed Solution:**

\(\begin{aligned}
& 2 \tan ^{-1} \frac{1}{5}+\tan ^{-1} \frac{1}{2}+2 \tan ^{-1} \frac{1}{8} \\
& =2 \tan ^{-1} \frac{\frac{1}{5}+\frac{1}{8}}{1-\frac{1}{5} \cdot \frac{1}{8}}+\tan ^{-1} \frac{1}{7} \\
& =2 \tan ^{-1} \frac{1}{3}+\tan ^{-1} \frac{1}{7}=\tan ^{-1} \frac{2 \cdot \frac{1}{3}}{1-\frac{1}{9}}+\tan ^{-1} \frac{1}{7} \\
& =\tan ^{-1} \frac{3}{4}+\tan ^{-1} \frac{1}{7}=\tan ^{-1} \frac{\frac{3}{4}+\frac{1}{7}}{1-\frac{3}{4} \cdot \frac{1}{7}} \\
& =\tan ^{-1} \frac{25}{25}=\tan ^{-1} 1=45^{\circ}=\frac{\pi}{4}
\end{aligned}\)

</details>

---

