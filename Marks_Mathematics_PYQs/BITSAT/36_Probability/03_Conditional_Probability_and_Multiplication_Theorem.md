# BITSAT Mathematics - Probability

## Topic 3: Conditional Probability and Multiplication Theorem

**Total Questions:** 6

---

### Q1. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

For two events A and B , if $\mathrm{P}(\mathrm{A})=\mathrm{P}\left(\frac{\mathrm{A}}{\mathrm{B}}\right)=\frac{1}{4}$ and $P\left(\frac{B}{A}\right)=\frac{1}{2}$, then which of the following is not true?

**Options:**

- **(A)** A and B are independent
- **(B)** $\mathrm{P}\left(\frac{\mathrm{A}^{\prime}}{\mathrm{B}}\right)=\frac{3}{4}$
- **(C)** $\mathrm{P}\left(\frac{\mathrm{B}^{\prime}}{\mathrm{A}^{\prime}}\right)=\frac{1}{2}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

$\mathrm{P}\left(\frac{\mathrm{B}}{\mathrm{A}}\right)=\frac{1}{2} \Rightarrow \frac{\mathrm{P}(\mathrm{B} \cap \mathrm{A})}{\mathrm{P}(\mathrm{A})}=\frac{1}{2} \Rightarrow \mathrm{P}(\mathrm{B} \cap \mathrm{A})=\frac{1}{8}$
$\mathrm{P}\left(\frac{\mathrm{A}}{\mathrm{B}}\right)=\frac{1}{4} \Rightarrow \frac{\mathrm{P}(\mathrm{A} \cap \mathrm{B})}{\mathrm{P}(\mathrm{B})}=\frac{1}{4} \Rightarrow \mathrm{P}(\mathrm{B})=\frac{1}{2}$
$\mathrm{P}(\mathrm{A} \cap \mathrm{B})=\frac{1}{8}=\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B})$
$\therefore$ Events A and B are independent.
Now, $\mathrm{P}\left(\frac{\mathrm{A}^{\prime}}{\mathrm{B}}\right)=\frac{\mathrm{P}(\mathrm{A} \cap \mathrm{B})}{\mathrm{P}(\mathrm{B})}=\frac{\mathrm{P}(\mathrm{A}) \mathrm{P}(\mathrm{B})}{\mathrm{P}(\mathrm{B})}=\frac{3}{4}$
and $\mathrm{P}\left(\frac{\mathrm{B}^{\prime}}{\mathrm{A}^{\prime}}\right)=\frac{\mathrm{P}\left(\mathrm{B}^{\prime} \cap \mathrm{A}^{\prime}\right)}{\mathrm{P}\left(\mathrm{A}^{\prime}\right)}=\frac{\mathrm{P}\left(\mathrm{B}^{\prime}\right) \mathrm{P}\left(\mathrm{A}^{\prime}\right)}{\mathrm{P}\left(\mathrm{A}^{\prime}\right)}=\frac{1}{2}$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{P}(\mathrm{B})=\frac{3}{5}, \mathrm{P}(\mathrm{A} \mid \mathrm{B})=\frac{1}{2}$ and $\mathrm{P}(\mathrm{A} \cup \mathrm{B})=\frac{4}{5}$, then $\mathrm{P}(\mathrm{A} \cup \mathrm{B})^{\prime}+\mathrm{P}\left(\mathrm{A}^{\prime} \cup \mathrm{B}\right)=$

**Options:**

- **(A)** $\frac{1}{5}$
- **(B)** $\frac{4}{5}$
- **(C)** $\frac{1}{2}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$P(B)=\frac{3}{5}, P(A \mid B)=\frac{1}{2}$ and $P(A \cup B)=\frac{4}{5}$
$P(A \cap B)=P(A \mid B) P(B)=\frac{1}{2} \cdot \frac{3}{5}=\frac{3}{10}$
$\mathrm{P}(\mathrm{A} \cup \mathrm{B})=\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A} \cap \mathrm{B})$
$\mathrm{P}(\mathrm{A})=\frac{4}{5}-\frac{3}{10}=\frac{1}{2} . \quad \mathrm{P}\left(\mathrm{A}^{\prime}\right)=1-\mathrm{P}(\mathrm{A})=\frac{1}{2}$
We know, $\mathrm{P}(\mathrm{A} \cap \mathrm{B})+\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}\right)=\mathrm{P}(\mathrm{B})$
[as $A \cap B$ and $A^{\prime} \cap B$ are mutually exclusive events]
$\Rightarrow \quad \frac{3}{10}+\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}\right)=\frac{3}{5}$
$\Rightarrow \mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}\right)=\frac{3}{5}-\frac{3}{10}=\frac{3}{10}$
Now, $\mathrm{P}\left(\mathrm{A}^{\prime} \cup \mathrm{B}\right)=\mathrm{P}\left(\mathrm{A}^{\prime}\right)+\mathrm{P}(\mathrm{B})-\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}\right)$
$=\frac{1}{2}+\frac{3}{5}-\frac{3}{10}=\frac{5+6-3}{10}=\frac{4}{5}$
$\mathrm{P}\left((\mathrm{A} \cup \mathrm{B})^{\prime}\right)=1-\mathrm{P}(\mathrm{A} \cup \mathrm{B})=1-\frac{4}{5}=\frac{1}{5}$
$\therefore \mathrm{P}\left((\mathrm{A} \cup \mathrm{B})^{\prime}\right)+\mathrm{P}\left(\mathrm{A}^{\prime} \cup \mathrm{B}\right)=\frac{1}{5}+\frac{4}{5}=1$

</details>

---

### Q3. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `1`

A six faced die is a biased one. It is thrice more likely to show an odd numbers than show an even number. It is thrown twice. The probability that the sum of the numbers in two throws is even, is

**Options:**

- **(A)** $\frac{5}{9}$
- **(B)** $\frac{5}{8}$
- **(C)** $\frac{1}{2}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{8}$**

**Detailed Solution:**

Let $P$ be the probability of getting an even number. Then by hypothesis the probability of getting an odd number is $3 P$. Since the events of getting an even number and an odd number are mutually exclusive and exhaustive.
$$
\therefore \quad P+3 P=1 \Rightarrow P=1 / 4
$$
Thus, the probability of getting an odd number in a single throw is $\frac{3}{4}$ and that of an even number is $\frac{1}{4}$.
If the die is thrown twice, then the sum of the numbers in two throws is even if both the numbers are even or both are odd.
$$
\therefore \text { Required probability }=\frac{3}{4} \times \frac{3}{4}+\frac{1}{4} \times \frac{1}{4}=\frac{10}{16}=\frac{5}{8}
$$

</details>

---

### Q4. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `3`

If the papers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> students can be checked by any one of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> teachers, then the probability that all the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> papers are checked by exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> teachers, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><mn>49</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mn>49</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>49</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>49</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mn>49</mn></mfrac></math>**

**Detailed Solution:**

<p>Total ways in which papers can be checked is equal <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>4</mn></msup></math>. Now, two teachers who have to check all the papers can be selected in <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></math> ways and papers can be checked by them is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mn>2</mn><mn>4</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced></math> favourable ways.</p><p>Thus, required probability</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>7</mn></mmultiscripts><mfenced><mrow><msup><mn>2</mn><mn>4</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><msup><mn>7</mn><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>49</mn></mfrac></math></p>

</details>

---

### Q5. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `2`

For $k=1,2,3$ the box $\mathrm{B}_{k}$ contains $k$ red balls and $(k+1)$ white balls. Let $\mathrm{P}\left(\mathrm{B}_{1}\right)=\frac{1}{2}, \mathrm{P}\left(\mathrm{B}_{2}\right)=\frac{1}{3}$ and

$\mathrm{P}\left(\mathrm{B}_{3}\right)=\frac{1}{6} . \mathrm{A}$ box is selected at random and a ball is drawn from it. If a red ball is drawn, then the probability that it has come from box $\mathrm{B}_{2},$ is

**Options:**

- **(A)** $\frac{35}{78}$
- **(B)** $\frac{14}{39}$
- **(C)** $\frac{10}{13}$
- **(D)** $\frac{12}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{14}{39}$**

**Detailed Solution:**

$\operatorname{In}$ a box, $B_{1}=1 R, 2 W ; B_{2}=2 R, 3 W$ and $B_{3}=3 R, 4 W$

Also, given that, $\mathrm{P}\left(\mathrm{B}_{1}\right)=\frac{1}{2}, \mathrm{P}\left(\mathrm{B}_{2}\right)=\frac{1}{3}$

$$

\begin{aligned}

& \text { and } P\left(B_{3}\right)=\frac{1}{6} \\

\therefore \quad & P\left(\frac{B_{2}}{R}\right)=\frac{P\left(B_{2}\right) P\left(\frac{R}{B_{2}}\right)}{P\left(B_{1}\right) P\left(\frac{R}{B_{1}}\right)+P\left(B_{2}\right) P\left(\frac{R}{B_{2}}\right)+P\left(B_{3}\right) P\left(\frac{R}{B_{3}}\right)} \\

=& \frac{\frac{1}{3} \times \frac{2}{5}}{\frac{1}{2} \times \frac{1}{3}+\frac{1}{3} \times \frac{2}{5}+\frac{1}{6} \times \frac{3}{7}}=\frac{\frac{2}{15}}{\frac{1}{6}+\frac{2}{15}+\frac{1}{14}}=\frac{14}{39} .

\end{aligned}

$$

</details>

---

### Q6. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `2`

A line segment has length 63 and direction ratios are \(3,-2,6\). If the line makes an obtuse angle with \(\mathrm{x}\)-axis, the components of the line vector are

**Options:**

- **(A)** \(27,-18,54\)
- **(B)** \(-27,18,54\)
- **(C)** \(-27,18,-54\)
- **(D)** \(27,-18,-54\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \(-27,18,-54\)**

**Detailed Solution:**

Let the components of the line vector be a, b, c. Then \(\mathrm{a}^2+\mathrm{b}^2+\mathrm{c}^2=(63)^2\) ...(i)
Also \(\frac{\mathrm{a}}{3}=\frac{\mathrm{b}}{-2}=\frac{\mathrm{c}}{6}=\lambda\) (say), then \(\mathrm{a}=3 \lambda\), \(\mathrm{b}=-2 \lambda\) and \(\mathrm{c}=6 \lambda\) and from (i) we have \(9 \lambda^2+4 \lambda^2+36 \lambda^2=(63)^2\)
\(\Rightarrow 49 \lambda^2=(63)^2\)
\(\Rightarrow \lambda= \pm \frac{63}{7}= \pm 9\)
Since \(a=3 \lambda  < 0\) as the line makes an obtuse angle with \(x\)-axis, \(\lambda=-9\) and the required components are \(-27,18,-54\).

</details>

---

