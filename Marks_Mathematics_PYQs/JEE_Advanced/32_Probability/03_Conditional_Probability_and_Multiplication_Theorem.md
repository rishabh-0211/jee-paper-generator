# JEE Advanced Mathematics - Probability

## Topic 3: Conditional Probability and Multiplication Theorem

**Total Questions:** 23

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Suppose that Box I contains $6$ red balls and $9$ green balls, and Box II contains $8$ red balls and $12$ green balls. All the balls of Box I and Box II are mixed together and a ball is chosen at random from them. Let $E_1$ be the event that the ball chosen belonged to Box I and let $E_2$ be the event that the ball chosen belonged to Box II. Let $F_1$ be the event that the ball chosen is red and let $F_2$ be the event that the ball chosen is green.

Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** The events $E_1$ and $F_1$ are independent
- **(B)** The events $E_2$ and $F_2$ are dependent
- **(C)** The conditional probability $P(F_1 \mid E_1)$ is equal to the conditional probability $P(F_1 \mid E_2)$
- **(D)** The conditional probability $P(F_1 \mid E_1)$ is greater than the conditional probability $P(F_2 \mid E_2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) The conditional probability $P(F_1 \mid E_1)$ is equal to the conditional probability $P(F_1 \mid E_2)$**

**Detailed Solution:**

Total balls in Box I $= 6 + 9 = 15$
Total balls in Box II $= 8 + 12 = 20$
Total balls in the mixture $= 15 + 20 = 35$
Total red balls $= 6 + 8 = 14$
Total green balls $= 9 + 12 = 21$

The probabilities of the given events are:
$P(E_1) = \dfrac{15}{35} = \dfrac{3}{7}$
$P(E_2) = \dfrac{20}{35} = \dfrac{4}{7}$
$P(F_1) = \dfrac{14}{35} = \dfrac{2}{5}$
$P(F_2) = \dfrac{21}{35} = \dfrac{3}{5}$

The joint probabilities are:
$P(E_1 \cap F_1) = \dfrac{6}{35}$
$P(E_2 \cap F_2) = \dfrac{12}{35}$

For statement (A):
$P(E_1) P(F_1) = \dfrac{3}{7} \times \dfrac{2}{5} = \dfrac{6}{35} = P(E_1 \cap F_1)$
Thus, $E_1$ and $F_1$ are independent. Statement (A) is TRUE.

For statement (B):
$P(E_2) P(F_2) = \dfrac{4}{7} \times \dfrac{3}{5} = \dfrac{12}{35} = P(E_2 \cap F_2)$
Thus, $E_2$ and $F_2$ are independent. Statement (B) is FALSE.

For statement (C):
$P(F_1 \mid E_1) = \dfrac{P(E_1 \cap F_1)}{P(E_1)} = \dfrac{6/35}{15/35} = \dfrac{2}{5}$
$P(F_1 \mid E_2) = \dfrac{P(E_2 \cap F_1)}{P(E_2)} = \dfrac{8/35}{20/35} = \dfrac{2}{5}$
Since $P(F_1 \mid E_1) = P(F_1 \mid E_2)$, statement (C) is TRUE.

For statement (D):
$P(F_2 \mid E_2) = \dfrac{P(E_2 \cap F_2)}{P(E_2)} = \dfrac{12/35}{20/35} = \dfrac{3}{5}$
Since $\dfrac{2}{5} < \dfrac{3}{5}$, $P(F_1 \mid E_1)$ is not greater than $P(F_2 \mid E_2)$. Statement (D) is FALSE.

Answer: The events $E_1$ and $F_1$ are independent; The conditional probability $P(F_1 \mid E_1)$ is equal to the conditional probability $P(F_1 \mid E_2)$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Three students $S_1, S_2$ and $S_1$ are given a problem to solve. Consider the following events :
$U:$ At least one of $S_1, S_2$ and $S_3$ can solve the problem,
$V: S_1$ can solve the problem, given that neither $\mathrm{S}_2$ nor $\mathrm{S}_3$ can solve the problem,
$W: S_2$ can solve the problem and $S_3$ cannot solve the problem,
$T: S_3$ can solve the problem.
For any event $E$, let $P(E)$ denote the probability of $E$.
If $P(U)=\frac{1}{2}, P(V)=\frac{1}{10}$ and $P(W)=\frac{1}{12}$, then $P(T)$ is equal to

**Options:**

- **(A)** $\frac{13}{36}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{19}{60}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{13}{36}$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{P}(\mathrm{U})=1-\mathrm{P}\left(\mathrm{~S}_1^{\prime} \cap \mathrm{S}_2^{\prime} \cap \mathrm{S}_3^{\prime}\right)=\frac{1}{2} \\
& \Rightarrow \mathrm{P}\left(\mathrm{~S}_1^{\prime} \cap \mathrm{S}_2^{\prime} \cap \mathrm{S}_3^{\prime}\right)=\frac{1}{2} ; \mathrm{P}\left(\mathrm{~S}_1^{\prime}\right) \cdot \mathrm{P}\left(\mathrm{~S}_2^{\prime}\right) \cdot \mathrm{P}\left(\mathrm{~S}_3^{\prime}\right)=\frac{1}{2} \\
& \Rightarrow\left(1-\mathrm{P}\left(\mathrm{~S}_1\right)\right)\left(1-\mathrm{P}\left(\mathrm{~S}_2\right)\right)\left(1-\mathrm{P}\left(\mathrm{~S}_3\right)\right)=\frac{1}{2} \quad \ldots(1)
\end{aligned}$
$\begin{aligned} & \mathrm{P}(\mathrm{V})=\frac{\mathrm{P}\left(\mathrm{S}_1 \cap \mathrm{~S}_2^{\prime} \cap \mathrm{S}_3^{\prime}\right)}{\mathrm{P}\left(\mathrm{S}_2^{\prime} \cap \mathrm{S}_3^{\prime}\right)}=\frac{1}{10} \\ & \Rightarrow \mathrm{P}\left(\mathrm{S}_1\right) \cdot \mathrm{P}\left(\mathrm{S}_2^{\prime}\right) \mathrm{P}\left(\mathrm{S}_3^{\prime}\right)=\frac{1}{10} \mathrm{P}\left(\mathrm{S}_2^{\prime}\right) \cdot \mathrm{P}\left(\mathrm{S}_3^{\prime}\right) \\ & \Rightarrow \mathrm{P}\left(\mathrm{S}_1\right)=\frac{1}{10}\end{aligned}$
$\begin{aligned}
& \mathrm{P}(\mathrm{~W})=\mathrm{P}\left(\mathrm{~S}_2 \cap \mathrm{~S}_3^{\prime}\right)=\frac{1}{12} \\
& \mathrm{P}\left(\mathrm{~S}_2\right) \cdot \mathrm{P}\left(\mathrm{~S}_3^{\prime}\right)=\frac{1}{12} \\
& \mathrm{P}\left(\mathrm{~S}_2\right)\left(1-\mathrm{P}\left(\mathrm{~S}_3\right)\right)=\frac{1}{12}...(2)
\end{aligned}$
Eq. (1)
$\left(1-\frac{1}{10}\right)\left(1-\mathrm{P}\left(\mathrm{~S}_2\right)\right)\left(1-\mathrm{P}\left(\mathrm{~S}_3\right)\right)=\frac{1}{2}$
$\left(1-\mathrm{P}\left(\mathrm{~S}_2\right)\right)\left(1-\mathrm{P}\left(\mathrm{~S}_3\right)\right)=\frac{5}{9}....(3)$
$\begin{aligned}
& \frac{\text { Eq. }(2)}{\text { Eq. }(3)} \Rightarrow \frac{\mathrm{P}\left(\mathrm{~S}_2\right)}{1-\mathrm{P}\left(\mathrm{~S}_2\right)}=\frac{1}{12} \times \frac{9}{5} \\
& \mathrm{P}\left(\mathrm{~S}_2\right)=\frac{3}{23}
\end{aligned}$
Put in Eq. (2)
$\begin{aligned}
& \frac{3}{23}\left(1-\mathrm{P}\left(\mathrm{~S}_3\right)\right)=\frac{1}{12} \\
& 1-\mathrm{P}\left(\mathrm{~S}_3\right)=\frac{23}{36} \\
& \mathrm{P}\left(\mathrm{~S}_3\right)=\frac{13}{36} \\
& \mathrm{P}(\mathrm{~T})=\frac{13}{36}
\end{aligned}$

</details>

---

### Q3. JEE Advanced 2024 (Paper 2)

*Type:* `numerical` | *Level:* `2`

A bag contains $N$ balls out of which 3 balls are white, 6 balls are green, and the remaining balls are blue. Assume that the balls are identical otherwise. Three balls are drawn randomly one after the other without replacement. For $i=1,2,3$, let $W_i, G_i$, and $B_i$ denote the events that the ball drawn in the $i^{\text {th }}$ draw is a white ball, green ball, and blue ball, respectively. If the probability $P\left(W_1 \cap G_2 \cap B_3\right)=\frac{2}{5 N}$ and the conditional probability $P\left(B_3 \mid W_1 \cap G_2\right)=\frac{2}{9}$, then $N$ equals ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/f7tSqEqBZsB0ppVs8efBEGWvpewRd8MPyr9pM2Xg2kk.original.fullsize.png">
Given $\mathrm{P}\left(\mathrm{W}_1 \cap \mathrm{G}_2 \cap \mathrm{B}_3\right)=\frac{2}{5 \mathrm{~N}}$
and $\mathrm{P}\left(\mathrm{B}_3 \mid \mathrm{W}_1 \cap \mathrm{G}_2\right)=\frac{2}{9}$
$\begin{aligned} & \Rightarrow \frac{\mathrm{P}\left(\mathrm{B}_3 \cap \mathrm{W}_1 \cap \mathrm{G}_2\right)}{\mathrm{P}\left(\mathrm{W}_1 \cap \mathrm{G}_2\right)}=\frac{2}{9} \\ & \Rightarrow \frac{2}{5 \mathrm{~N}} \times \frac{\mathrm{N} \times(\mathrm{N}-1)}{3 \times 6}=\frac{2}{9} \\ & \Rightarrow \mathrm{N}=11\end{aligned}$

</details>

---

### Q4. JEE Advanced 2022 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Two players, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math>, play a game against each other. In every round of the game, each player rolls a fair die once, where the six faces of the die have six distinct numbers. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> denote the readings on the die rolled by <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math>, respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mi>y</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> scores <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> points and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> scores <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> point. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>y</mi></math>, then each player scores <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> points. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mi>y</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> scores <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> point and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> scores <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> points. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>i</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Y</mi><mi>i</mi></msub></math> be the total scores of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math>, respectively, after playing the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>i</mi><mi>th</mi></msup></math> round.</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math></td>			<td> </td>			<td>List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced></math></td>			<td>Probability of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>X</mi><mn>2</mn></msub><mo>&#8805;</mo><msub><mi>Y</mi><mn>2</mn></msub></mrow></mfenced></math> is</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">P</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>8</mn></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>II</mi></mfenced></math></td>			<td>Probability of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>X</mi><mn>2</mn></msub><mo>&#62;</mo><msub><mi>Y</mi><mn>2</mn></msub></mrow></mfenced></math> is</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">Q</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>16</mn></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>III</mi></mfenced></math></td>			<td>Probability of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>X</mi><mn>3</mn></msub><mo>=</mo><msub><mi>Y</mi><mn>3</mn></msub></mrow></mfenced></math> is</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">R</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>16</mn></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>IV</mi></mfenced></math></td>			<td>Probability of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>X</mi><mn>3</mn></msub><mo>&#62;</mo><msub><mi>Y</mi><mn>3</mn></msub></mrow></mfenced></math> is</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">S</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>355</mn><mn>864</mn></mfrac></math></td>		</tr>		<tr>			<td> </td>			<td> </td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">T</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>77</mn><mn>432</mn></mfrac></math></td>		</tr>	</tbody></table><p>The correct option is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">T</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">T</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">T</mi></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">P</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">T</mi></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">Q</mi></mfenced><mo>;</mo><mfenced><mi>II</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">R</mi></mfenced><mo>;</mo><mfenced><mi>III</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">T</mi></mfenced><mo>;</mo><mfenced><mi>IV</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">S</mi></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(draw in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> round)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>6</mn><mn>36</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(win in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> round) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(loss in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> round) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac></math></p><p>Now finding the probability of all we get,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>X</mi><mn>2</mn></msub><mo>&#62;</mo><msub><mi>Y</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mn>10</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mn>7</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mn>2</mn><mo>=</mo><mfrac><mn>45</mn><mn>144</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>16</mn></mfrac><mo>&#8594;</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>X</mi><mn>2</mn></msub><mo>=</mo><msub><mi>Y</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>&#215;</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mrow><mn>25</mn><mo>+</mo><mn>2</mn></mrow><mn>72</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>X</mi><mn>2</mn></msub><mo>&#8805;</mo><msub><mi>Y</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>16</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>16</mn></mfrac><mo>&#8594;</mo><mi>Q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>X</mi><mn>3</mn></msub><mo>=</mo><msub><mi>Y</mi><mn>3</mn></msub></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mn>7</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn></mrow></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>12</mn></mfrac><mo>&#215;</mo><mn>6</mn><mo>=</mo><mfrac><mn>2</mn><mn>432</mn></mfrac><mo>+</mo><mfrac><mn>75</mn><mn>432</mn></mfrac><mo>=</mo><mfrac><mn>77</mn><mn>432</mn></mfrac><mo>&#8594;</mo><mi>T</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>X</mi><mn>3</mn></msub><mo>&#62;</mo><msub><mi>Y</mi><mn>3</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>77</mn><mn>432</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>355</mn><mn>864</mn></mfrac><mo>&#8594;</mo><mi>S</mi></math></p></blockquote>

</details>

---

### Q5. JEE Advanced 2021 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Three numbers are chosen at random, one after another with replacement, from the set $S=\{1,2,3, \ldots, 100\}$. Let $p_{1}$ be the probability that the maximum of chosen numbers is at least 81 and $p_{2}$ be the probability that the minimum of chosen numbers is at most 40 .
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>125</mn><mn>4</mn></mfrac><msub><mi>p</mi><mn>2</mn></msub></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24.5**

**Detailed Solution:**

<p>Minimum of the chosen numbers is at most <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math></p><p>It means we have to choose all the numbers from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math> only
from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>41</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></p><p>Total number of possible selections <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>100</mn><mo>&#215;</mo><mn>100</mn><mo>&#215;</mo><mn>100</mn><mo>=</mo><msup><mn>100</mn><mn>3</mn></msup></math></p><p>Favourable cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> Unfavourable cases</p><p>Unfavourable cases are those in which we have selected all the three numbers form <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>41</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn><mo>&#215;</mo><mn>60</mn><mo>&#215;</mo><mn>60</mn><mo>=</mo><msup><mn>60</mn><mn>3</mn></msup></math></p><p>Total number of favourable cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>100</mn><mn>3</mn></msup><mo>-</mo><msup><mn>60</mn><mn>3</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><msup><mn>100</mn><mn>3</mn></msup><mo>-</mo><msup><mn>60</mn><mn>3</mn></msup></mrow><msup><mn>100</mn><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>20</mn><mn>3</mn></msup><mfenced><mrow><msup><mn>5</mn><mn>3</mn></msup><mo>-</mo><msup><mn>3</mn><mn>3</mn></msup></mrow></mfenced></mrow><mrow><msup><mn>20</mn><mn>3</mn></msup><mo>&#215;</mo><msup><mn>5</mn><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>98</mn><mn>125</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>125</mn><mn>4</mn></mfrac><msub><mi>p</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>125</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>98</mn><mn>125</mn></mfrac><mo>=</mo><mn>24</mn><mo>.</mo><mn>50</mn></math></p>

</details>

---

### Q6. JEE Advanced 2021 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Three numbers are chosen at random, one after another with replacement, from the set $S=\{1,2,3, \ldots, 100\}$. Let $p_{1}$ be the probability that the maximum of chosen numbers is at least 81 and $p_{2}$ be the probability that the minimum of chosen numbers is at most 40 .
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>625</mn><mn>4</mn></mfrac><msub><mi>p</mi><mn>1</mn></msub></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **76.25**

**Detailed Solution:**

<p>Maximum of the chosen numbers is at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math></p><p>It means we have to choose at least one number from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></p><p>Total number of possible selections <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>100</mn><mo>&#215;</mo><mn>100</mn><mo>&#215;</mo><mn>100</mn><mo>=</mo><msup><mn>100</mn><mn>3</mn></msup></math></p><p>Favourable cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> unfavourable cases</p><p>Unfavourable cases are those in which we have selected all the three numbers form <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>&#160;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>80</mn><mo>&#215;</mo><mn>80</mn><mo>&#215;</mo><mn>80</mn><mo>=</mo><msup><mn>80</mn><mn>3</mn></msup></math></p><p>Total number of favourable cases <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>100</mn><mn>3</mn></msup><mo>-</mo><msup><mn>80</mn><mn>3</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><msup><mn>100</mn><mn>3</mn></msup><mo>-</mo><msup><mn>80</mn><mn>3</mn></msup></mrow><msup><mn>100</mn><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>20</mn><mn>3</mn></msup><mfenced><mrow><msup><mn>5</mn><mn>3</mn></msup><mo>-</mo><msup><mn>4</mn><mn>3</mn></msup></mrow></mfenced></mrow><mrow><msup><mn>20</mn><mn>3</mn></msup><mo>&#215;</mo><msup><mn>5</mn><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>125</mn><mo>-</mo><mn>64</mn></mrow><mn>125</mn></mfrac><mo>=</mo><mfrac><mn>61</mn><mn>125</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>625</mn><mn>4</mn></mfrac><msub><mi>p</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>625</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>61</mn><mn>125</mn></mfrac><mo>=</mo><mn>76</mn><mo>.</mo><mn>25</mn></math></p>

</details>

---

### Q7. JEE Advanced 2021 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Consider three sets <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>}</mo><mo>,</mo><msub><mi>F</mi><mn>1</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>G</mi><mn>1</mn></msub><mo>=</mo><mo>{</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>}</mo></math>. Two elements are chosen at random, without replacement, from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math>, and let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math> denote the set of these chosen elements. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo><msub><mi>E</mi><mn>1</mn></msub><mo>-</mo><msub><mi>S</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub><mo>=</mo><msub><mi>F</mi><mn>1</mn></msub><mo>&#8746;</mo><msub><mi>S</mi><mn>1</mn></msub></math>. Now two elements are chosen at random, without replacement, from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> denote the set of these chosen elements.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>G</mi><mn>2</mn></msub><mo>=</mo><msub><mi>G</mi><mn>1</mn></msub><mo>&#8746;</mo><msub><mi>S</mi><mn>2</mn></msub></math>. Finally, two elements are chosen at random, without replacement, from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>G</mi><mn>2</mn></msub></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub></math> denote the set of these chosen elements.
Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>3</mn></msub><mo>=</mo><msub><mi>E</mi><mn>2</mn></msub><mo>&#8746;</mo><msub><mi>S</mi><mn>3</mn></msub></math>. Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><msub><mi>E</mi><mn>3</mn></msub></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> be the conditional probability of the event <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>}</mo></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>**

**Detailed Solution:**

<p>We need to find <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math>, the conditional probability of the event <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>}</mo></math>, given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><msub><mi>E</mi><mn>3</mn></msub></math>.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><msub><mi>S</mi><mn>1</mn></msub><mo>&#8745;</mo><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><msub><mi>E</mi><mn>3</mn></msub></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo><msub><mi>E</mi><mn>3</mn></msub></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></msub></mfenced></mrow><mrow><mi>P</mi><mo>(</mo><mi>B</mi><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>B</mi><mo>)</mo><mo>=</mo><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></msub></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></msub></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></msub></mfenced><mo>&#8594;</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>}</mo></math> chosen in the beginning </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></msub></mfenced><mo>&#8594;</mo></math>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>}</mo></math> chosen in the beginning</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></msub></mfenced><mo>&#8594;</mo></math>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>}</mo></math> chosen in the beginning</p><p><strong>(i)</strong> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>}</mo></math> is chosen in the begining, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> must contain <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>G</mi><mn>2</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>}</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></math></p><p><strong>(ii)</strong> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>}</mo></math> is chosen in the begining, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> must contain <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>G</mi><mn>2</mn></msub><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>}</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></math></p><p><strong>(iii)</strong> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>}</mo></math> is chosen in the begining, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>F</mi><mn>2</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>}</mo></math>, then two cases are possible</p><p>1. <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> may contain <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mn>1</mn></mfenced></math> and getting <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub><mo>=</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>G</mi><mn>2</mn></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>)</mo></math></p><p>2.  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub></math> does not contain <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mn>1</mn></mfenced></math> and getting <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>G</mi><mn>2</mn></msub><mo>=</mo><mo>{</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>]</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfenced close="]" open="["><mrow><mfrac><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>&#215;</mo><mn>1</mn></mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>&#215;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts></mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></msub></mfenced></mrow><mrow><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></msub></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></msub></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>B</mi><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></msub></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></mrow><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math></p>

</details>

---

### Q8. JEE Advanced 2020 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Two fair dice, each with faces numbered <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, are rolled together and the sum of the numbers on the faces is observed. This process is repeated till the sum is either a prime number or a perfect square. Suppose the sum turns out to be a perfect square before it turns out to be a prime number. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is the probability that this perfect square is an odd number, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mi>p</mi></math> is_____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Perfect Square can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>, which can be obtained by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math>.</p><p>Prime Number can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>, which can be obtained by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(square or prime)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>22</mn><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mfenced><mfrac><mtext>&#160;Perfect square&#160;is&#160;odd&#160;</mtext><mtext>&#160;perfect square&#160;before prime&#160;</mtext></mfrac></mfenced><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>36</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>14</mn><mn>36</mn></mfrac></mstyle><mo>.</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>36</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>14</mn><mn>36</mn></mfrac></mstyle><mo>.</mo><mstyle displaystyle="true"><mfrac><mn>14</mn><mn>36</mn></mfrac></mstyle><mo>.</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>36</mn></mfrac></mstyle><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow><mrow><mstyle displaystyle="true"><mfrac><mn>7</mn><mn>36</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>14</mn><mn>36</mn></mfrac></mstyle><mo>.</mo><mstyle displaystyle="true"><mfrac><mn>7</mn><mn>36</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>14</mn><mn>36</mn></mfrac></mstyle><mo>.</mo><mstyle displaystyle="true"><mfrac><mn>14</mn><mn>36</mn></mfrac></mstyle><mo>.</mo><mstyle displaystyle="true"><mfrac><mn>7</mn><mn>36</mn></mfrac></mstyle><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced><mstyle displaystyle="true"><mfrac><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>36</mn></mfrac></mstyle><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>14</mn><mn>36</mn></mfrac></mstyle></mrow></mfrac></mstyle></mfenced><mfenced><mfrac><mstyle displaystyle="true"><mfrac><mn>7</mn><mn>36</mn></mfrac></mstyle><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>14</mn><mn>36</mn></mfrac></mstyle></mrow></mfrac></mfenced></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>7</mn></mfrac><mo>=</mo><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>14</mn><mo>&#160;</mo><mi>P</mi><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q9. JEE Advanced 2020 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math> <mrow> <msub> <mi>C</mi> <mn>1</mn> </msub> </mrow> </math> and <math> <mrow> <msub> <mi>C</mi> <mn>2</mn> </msub> </mrow> </math> be two biased coins such that the probabilities of getting head in a single toss are <math> <mrow> <mfrac> <mn>2</mn> <mn>3</mn> </mfrac> </mrow> </math> and <math> <mrow> <mfrac> <mn>1</mn> <mn>3</mn> </mfrac> </mrow> </math>, respectively. Suppose <math> <mi>&#945;</mi> </math> is the number of heads that appear when <math> <mrow> <msub> <mi>C</mi> <mn>1</mn> </msub> </mrow> </math> is tossed twice, independently, and suppose <math> <mi>&#946;</mi> </math> is the number of heads that appear when <math> <mrow> <msub> <mi>C</mi> <mn>2</mn> </msub> </mrow> </math> is tossed twice, independently. Then the probability that the roots of the quadratic polynomial <math> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>&#8722;</mo><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>&#946;</mi></mrow> </math> are real and equal, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>40</mn><mn>81</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mn>81</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mn>81</mn></mfrac></math>**

**Detailed Solution:**

<p>For tossing two coins independently, maximum and minimum heads that can appear will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>0</mn></math> respectively.</p><p>Roots of equation <math> <mrow> <msup> <mi>x</mi> <mn>2</mn> </msup> <mo>&#8722;</mo><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn></mrow> </math> are real and equal, then discriminant <math> <mrow> <mi>D</mi><mo>=</mo><mn>0</mn></mrow> </math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>4</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn></mrow></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>Thus, the required probability</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>0</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>.</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>0</mn></msup><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>0</mn></msup><mo>.</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>1</mn></msup><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>1</mn></msup></math></p><p><math> <mrow> <mo>=</mo><mfrac> <mn>1</mn> <mn>9</mn> </mfrac> <mo>&#215;</mo><mfrac> <mn>4</mn> <mn>9</mn> </mfrac> <mo>+</mo><mfrac> <mn>4</mn> <mn>9</mn> </mfrac> <mo>&#215;</mo><mfrac> <mn>4</mn> <mn>9</mn> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>20</mn></mrow> <mrow> <mn>81</mn></mrow> </mfrac> </mrow> </math></p>

</details>

---

### Q10. JEE Advanced 2019 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let <math><mi mathvariant="normal">S</mi></math> be the sample space of all <math><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrices with entries from the set <math><mfenced close="}" open="{" separators="|"><mrow><mn>0</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mn>1</mn></mrow></mfenced><mo>.</mo></math> Let the events <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub></math> be given by
<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mi mathvariant="normal">A</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi><mo>:</mo><mtext>&#8201;</mtext><mi mathvariant="normal">d</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">t</mi><mtext>&#8201;</mtext><mi mathvariant="normal">A</mi><mo>=</mo><mn>0</mn></mrow></mfenced></math> and
<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>{</mo><mi mathvariant="normal">A</mi><mo>&#8712;</mo><mi mathvariant="normal">S</mi><mo>:</mo></math> sum of entries of <math><mi mathvariant="normal">A</mi></math> is <math><mn>7</mn><mo>}</mo><mo>.</mo></math>
If a matrix is chosen at random from <math><mi mathvariant="normal">S</mi><mo>,</mo></math> then the conditional probability <math><mi mathvariant="normal">P</mi><mfenced separators="|"><mrow><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced></math> equals____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.5**

**Detailed Solution:**

For sum to be seven, we need seven <math><mn>1</mn><mi mathvariant="normal">s</mi></math> and two <math><mn>0</mn><mi>s</mi></math>
<math></math> Number of different possible matrices= <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><menclose notation="left bottom"><mn>9</mn></menclose><mrow><menclose notation="left bottom"><mn>7</mn></menclose><mtext>&#8201;</mtext><menclose notation="left bottom"><mn>2</mn></menclose></mrow></mfrac><mo>=</mo><mn>36</mn></math>
Eg. <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> {arrangement of seven <math><mn>1</mn><mi>s</mi></math> and two <math><mn>0</mn><mi>s</mi></math> }
Now, for determined of matrix to be zero, both the zero must be in same row or in same column.
Eg. <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> Now, arrangement of 0s and <math><mn>1</mn><mi>s</mi><mo>=</mo><munder><mrow><mn>6</mn></mrow><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mi>S</mi><mi>e</mi><mi>l</mi><mi>e</mi><mi>c</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mtext>&#8201;</mtext><mi>o</mi><mi>f</mi></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>a</mi><mtext>&#8201;</mtext><mrow><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">n</mi></mrow><mo>/</mo><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">w</mi></mrow></mrow></mrow></mtd></mtr></mtable></mrow></munder><mtext>&#8201;</mtext><mo>&#215;</mo><mtext>&#8201;&#8201;</mtext><munder><mrow><mn>3</mn></mrow><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mi>a</mi><mi>r</mi><mi>r</mi><mi>a</mi><mi>n</mi><mi>g</mi><mi>e</mi><mi>m</mi><mi>e</mi><mi>n</mi><mi>t</mi></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>o</mi><mi>f</mi><mtext>&#8201;</mtext><mi>t</mi><mi>w</mi><mi>o</mi><mtext>&#8201;</mtext><mn>0</mn><mi>s</mi></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>a</mi><mi>n</mi><mi>d</mi><mtext>&#8201;</mtext><mi>o</mi><mi>n</mi><mi>e</mi><mtext>&#8201;</mtext><mn>1</mn><mtext>&#8201;</mtext><mi>i</mi><mi>n</mi><mtext>&#8201;</mtext></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>a</mi><mtext>&#8201;</mtext><mrow><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">w</mi></mrow><mo>/</mo><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">n</mi></mrow></mrow></mrow></mtd></mtr></mtable></mrow></munder><mtext>&#8201;&#8201;</mtext><mo>=</mo><mtext>&#8201;&#8201;</mtext><mn>18</mn></math>
Hence, required probability <math><mo>=</mo><mfrac><mrow><mn>18</mn></mrow><mrow><mn>36</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
(Note: If two zero&#39;s lies on different row/column then <math><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mo>+</mo><mn>1</mn><mo>&#8800;</mo><mn>0</mn></math> )

</details>

---

### Q11. JEE Advanced 2019 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

There are three bags <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>.</mo></math> The bag <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>1</mn></mrow></msub></math> contains <math><mn>5</mn></math> red and <math><mn>5</mn></math> green balls, <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msub></math> contains <math><mn>3</mn></math> red and <math><mn>5</mn></math> green balls, and <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>3</mn></mrow></msub></math> contains <math><mn>5</mn></math> red and <math><mn>3</mn></math> green balls, Bags <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>2</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>3</mn></mrow></msub></math> have probabilities <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math> and <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math> respectively of being chosen. A bag is selected at random and a ball is chosen at random from the bag. Then which of the following options is/are correct?

**Options:**

- **(A)** Probability that the selected bag is  <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>3</mn></mrow></msub></math>  and the chosen ball is green equals  <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>
- **(B)** Probability that the chosen ball is green equals  <math><mfrac><mrow><mn>39</mn></mrow><mrow><mn>80</mn></mrow></mfrac></math>
- **(C)** Probability that the chosen ball is green, given that the selected bag is  <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo></math>  equals  <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(D)** Probability that the selected bag is  <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo></math>  given that the chosen balls is green, equals  <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>13</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Probability that the chosen ball is green, given that the selected bag is  <math><msub><mrow><mi mathvariant="normal">B</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo></math>  equals  <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let us define following events
<math><msub><mrow><mi>B</mi></mrow><mrow><mn>1</mn></mrow></msub></math> : Event of selection of bag <math><mn>1</mn></math> ( <math><mn>5</mn></math> Red, <math><mn>5</mn></math> Green)
<math><msub><mrow><mi>B</mi></mrow><mrow><mn>2</mn></mrow></msub><mi>&#160;</mi></math> : Event of selection of bag <math><mn>2</mn></math> ( <math><mn>3</mn></math> Red, <math><mn>5</mn></math> Green)
<math><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></math> : Event of selection of bag <math><mn>3</mn></math> ( <math><mn>5</mn></math> Red, <math><mn>3</mn></math> Green)
<math><mi>R</mi><mo>=</mo></math> Event of selection of Red ball
<math><mi>G</mi><mo>=</mo></math> Event of selection of Green ball
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>C</mi><mo>)</mo></math> :
<math><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>G</mi></mrow><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math> (as bag <math><mn>3</mn></math> has been selected now total balls in bag <math><mn>3</mn><mo>=</mo><mn>8</mn><mo>,</mo></math> green ball <math><mo>=</mo><mn>3</mn></math> )
Option <math><mo>(</mo><mi mathvariant="normal">B</mi><mo>)</mo></math> :
<math><mi>P</mi><mfenced separators="|"><mrow><mi>G</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>G</mi></mrow><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>G</mi></mrow><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfenced><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>G</mi></mrow><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>39</mn></mrow><mrow><mn>80</mn></mrow></mfrac></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>D</mi><mo>)</mo></math> :
<math><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mrow><mi>G</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8745;</mo><mi>G</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>G</mi></mrow></mfenced></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfenced><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>G</mi></mrow><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>P</mi><mo>(</mo><mi>G</mi><mo>)</mo></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mfrac bevelled="true"><mrow><mn>4</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mfrac bevelled="true"><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow><mrow><mfrac bevelled="true"><mrow><mn>35</mn></mrow><mrow><mn>80</mn></mrow></mfrac></mrow></mfrac><mi>&#160;</mi><mfenced separators="|"><mrow><mo>&#8756;</mo><mtext>&#8201;</mtext><mi>P</mi><mfenced separators="|"><mrow><mi>G</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>39</mn></mrow><mrow><mn>80</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>13</mn></mrow></mfrac></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>A</mi><mo>)</mo></math> :
<math><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8745;</mo><mi>G</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfenced><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>G</mi></mrow><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfrac></mrow></mfenced></math>
<math><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8745;</mo><mi>G</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfenced><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>G</mi></mrow><mrow><msub><mrow><mi>B</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math></p>

</details>

---

### Q12. JEE Advanced 2017 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

Let <math><mi>X</mi></math> and <math><mi>Y</mi></math> be two events such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mi>X</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mi>X</mi><mi>Y</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>Y</mi><mo>|</mo><mi>X</mi></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>.</mo></math> Then

**Options:**

- **(A)** <math><mi>P</mi><mfenced separators="|"><mrow><mi>Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
- **(B)** <math><mi>P</mi><mfenced separators="|"><mrow><mover accent="true"> <mi>X</mi> <mo stretchy="true">¯</mo> </mover><mo>|</mo><mi> Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>∩</mo><mi>Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>∪</mo><mi>Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>P</mi><mfenced separators="|"><mrow><mover accent="true"> <mi>X</mi> <mo stretchy="true">¯</mo> </mover><mo>|</mo><mi> Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

Using formula <math> <mrow> <mi>P</mi><mfenced separators="|"><mrow><mi>X </mi><mo>|</mo><mi> Y</mi></mrow></mfenced><mo>=</mo><mfrac> <mrow> <mi>P</mi><mrow><mo>(</mo> <mrow> <mi>X</mi><mo>∩</mo><mi>Y</mi> </mrow> <mo>)</mo></mrow> </mrow> <mrow> <mi>P</mi><mrow><mo>(</mo> <mi>Y</mi> <mo>)</mo></mrow> </mrow> </mfrac> </mrow></math> and <math><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>Y </mi><mo>|</mo><mi> X</mi></mrow></mfenced><mo>=</mo><mfrac> <mrow> <mi>P</mi><mrow><mo>(</mo> <mrow> <mi>Y</mi><mo>∩</mo><mi>X</mi> </mrow> <mo>)</mo></mrow> </mrow> <mrow> <mi>P</mi><mrow><mo>(</mo> <mi>X</mi> <mo>)</mo></mrow> </mrow> </mfrac> </mrow> </math>
<math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>;</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>∩</mo><mi>Y</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>Y</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>;</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>Y</mi><mo>∩</mo><mi>X</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
From this information, we get
<math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>∩</mo><mi>Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mo>;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
Using formula <math> <mrow> <mi>P</mi><mo stretchy="false">(</mo><mi>X</mi><mo>∪</mo><mi>Y</mi><mo stretchy="false">)</mo><mo>=</mo><mi>P</mi><mo stretchy="false">(</mo><mi>X</mi><mo stretchy="false">)</mo><mo>+</mo><mi>P</mi><mo stretchy="false">(</mo><mi>Y</mi><mo stretchy="false">)</mo><mo>−</mo><mi>P</mi><mo stretchy="false">(</mo><mi>X</mi><mo>∩</mo><mi>Y</mi><mo stretchy="false">)</mo> </mrow> </math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>∪</mo><mi>Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
<math><mi>P</mi><mfenced separators="|"><mrow><mover accent="true"> <mi>X</mi> <mo stretchy="true">¯</mo> </mover><mo>|</mo><mi> Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>X</mi></mrow><mo>-</mo></mover><mo>∩</mo><mi>Y</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>Y</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>Y</mi></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>∩</mo><mi>Y</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>Y</mi></mrow></mfenced></mrow></mfrac></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi>P</mi><mfenced separators="|"><mrow><mover accent="true"> <mi>X</mi> <mo stretchy="true">¯</mo> </mover><mo>|</mo><mi> Y</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>15</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q13. JEE Advanced 2016 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong> Paragraph: </strong>

Football teams $T_{1}$ and $T_{2}$ have to play two games against each other. It is assumed that the outcomes of the two games are independent. The probabilities of $T_{1}$ winning, drawing and losing a game against $T_{2}$ are $\frac{1}{2}, \frac{1}{6}$ and $\frac{1}{3}$, respectively. Each team gets $3$ points for a win, $1$ point for a draw and $0$ point for a loss in a game. Let $X$ and $Y$ denote the total points scored by teams $T_{1}$ and $T_{2}$, respectively, after two games.


 <strong> Question: </strong>

$P(X=Y)$ is

**Options:**

- **(A)** <math><mfrac><mrow><mn>11</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mi>Y</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">w</mi></mrow></mfenced><mi>P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">D</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">w</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mfenced><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mfenced><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>13</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>

</details>

---

### Q14. JEE Advanced 2016 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong> Paragraph: </strong>

Football teams $T_{1}$ and $T_{2}$ have to play two games against each other. It is assumed that the outcomes of the two games are independent. The probabilities of $T_{1}$ winning, drawing and losing a game against $T_{2}$ are $\frac{1}{2}, \frac{1}{6}$ and $\frac{1}{3}$, respectively. Each team gets $3$ points for a win, $1$ point for a draw and $0$ point for a loss in a game. Let $X$ and $Y$ denote the total points scored by teams $T_{1}$ and $T_{2}$, respectively, after two games.


 <strong> Question: </strong>

$P(X>Y)$ is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#62;</mo><mi>Y</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mfenced><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mfenced><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">w</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">w</mi></mrow></mfenced><mo>.</mo><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

</details>

---

### Q15. JEE Advanced 2015 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></math> be the number of red and black balls, respectively, in box I. Let <math><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub></math> be the number of red and black balls, respectively, in box II.
A ball is drawn at random from box I and transferred to box II. If the probability of drawing a red ball from box I, after this transfer, is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> , then the correct options(s) with the possible values of <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is(are)

**Options:**

- **(A)** <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>4</mn><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>6</mn></math>
- **(B)** <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>3</mn></math>
- **(C)** <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>10</mn><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>20</mn></math>
- **(D)** <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>3</mn><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>3</mn><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>6</mn></math>**

**Detailed Solution:**

Probability <math><mo>=</mo><mi> </mi><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mi> </mi><mo>&sdot;</mo><mi> </mi><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><mn>1</mn></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi> </mi><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mi> </mi><mo>&sdot;</mo><mi> </mi><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mfenced separators="|"><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced><mo>(</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>10</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>20</mn></math> 
or   <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>3</mn><mo>,</mo><mi> </mi><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>6</mn><mi> </mi></math>

</details>

---

### Q16. JEE Advanced 2011 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Let $U_1$ and $U_2$ be two urns such that $U_1$ contains 3 white and 2 red balls and $U_2$ contains only 1 white ball. A fair coin is tossed. If head appears then 1 ball is drawn at random from $U_1$ and put into $U_2$. However, if tail appears then 2 balls are drawn at random from $U_1$ and put into $U_2$. Now, 1 ball is drawn at random from $U_2$.<strong>Question:</strong>
The probability of the drawn ball from $U_2$ being white is

**Options:**

- **(A)** $\frac{13}{30}$
- **(B)** $\frac{23}{30}$
- **(C)** $\frac{19}{30}$
- **(D)** $\frac{11}{30}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{23}{30}$**

**Detailed Solution:**

Now, probability of the drawn ball from $\mathrm{V}_2$ being white is
$$
\Rightarrow P \text { (white/ } V_2 \text { ) }
$$

$$
\begin{aligned}
& \left.\Rightarrow P \text { (white/ } V_2\right) \\
& =P(H) \cdot\left\{\frac{{ }^3 C_1}{{ }^5 C_1} \times \frac{{ }^2 C_1}{{ }^2 C_1}+\frac{{ }^2 C_1}{{ }^5 C_1} \times \frac{{ }^1 C_1}{{ }^2 C_1}\right\} \\
& +P(T)\left\{\frac{{ }^3 C_2}{{ }^5 C_2} \times \frac{{ }^3 C_2}{{ }^3 C_2}+\frac{{ }^2 C_2}{{ }^5 C_2} \times \frac{{ }^1 C_1}{{ }^3 C_2}\right. \\
& \left.+\frac{{ }^3 C_1 \cdot{ }^2 C_1}{{ }^5 C_2} \times \frac{{ }^2 C_1}{{ }^3 C_2}\right\} \\
& \text { Now, } P\left(\text { white } / V_2\right)=\frac{1}{2}\left\{\frac{3}{5} \times 1+\frac{2}{5} \times \frac{1}{2}\right\} \\
& +\frac{1}{2}\left\{\frac{3}{10} \times 1+\frac{1}{10} \times \frac{1}{3}+\frac{6}{10} \times \frac{2}{3}\right\}=\frac{23}{30} \\
&
\end{aligned}
$$

</details>

---

### Q17. JEE Advanced 2009 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
A fair die is tossed repeatedly until a six is obtained. Let $X$ denotes the number of tosses required.<strong>Question:</strong>
The conditional probability that $X \geq 6$ given $X>3$ equals

**Options:**

- **(A)** $\frac{125}{216}$
- **(B)** $\frac{25}{216}$
- **(C)** $\frac{5}{36}$
- **(D)** $\frac{25}{36}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{25}{36}$**

**Detailed Solution:**

$P((X \geq 6) /(X>3))$

$$
\begin{aligned}
& =\frac{P((X>3) /(X \geq 6)) \cdot P(X \geq 6)}{P(X>3)} \\
& =\frac{1 \cdot\left[\left(\frac{5}{6}\right)^5 \cdot \frac{1}{6}+\left(\frac{5}{6}\right)^6 \cdot \frac{1}{6}+\ldots \infty\right]}{\left[\left(\frac{5}{6}\right)^3 \cdot \frac{1}{6}+\left(\frac{5}{6}\right)^4 \cdot \frac{1}{6}+\ldots \infty\right]}=\frac{25}{36} \\
&
\end{aligned}
$$

</details>

---

### Q18. JEE Advanced 2008 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider the system of equations
where $\quad a, b, c, d \in\{0,1\}$
Statement 1 The probability that the system of equations has a unique solution, is $3 / 8$.
Statement 2 The probability that the system of equations has a solution, is 1 .

**Options:**

- **(A)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is false.
- **(D)** Statement 1 is false, Statement 2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement 1 is true, Statement 2 is true, Statement 2 is not a correct explanation for Statement 1.**

**Detailed Solution:**

The number of all possible deteminants of the form
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/miiF1S9q7HSANsbUETCrPwiWfrn8s-gtqeJ3Wn4bUkI.original.fullsize.png">


Out of which only 10 determinants given by<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/4W-k0G-nLAT2todHF1RbeMvEgzAQgzuWF7dVWZeueic.original.fullsize.png">


vanish and remaining six determinants have non-zero values.
Hence, the required probability $=\frac{6}{16}=\frac{3}{8}$
$\Rightarrow$ Statement 1 is correct.
Statement 2 is also correct as the homogeneous equations have always a solution and Statement 2 is not a correct explanation of Statement 1.

</details>

---

### Q19. JEE Advanced 2007 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $E^c$ denotes the complement of an event $E$. Let $E, F, G$ be pairwise independent events with $P(G)>0$ and $P(E \cap F \cap G)=0$. Then, $P\left(E^c \cap F^c \mid G\right)$ equals

**Options:**

- **(A)** $P\left(E^c\right)+P\left(F^c\right)$
- **(B)** $P\left(E^c\right)-P\left(F^c\right)$
- **(C)** $P\left(E^c\right)-P(F)$
- **(D)** $P(E)-P\left(F^c\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $P\left(E^c\right)-P(F)$**

**Detailed Solution:**

$$
\text { } \begin{aligned}
P\left(\frac{E^c \cap F^c}{G}\right) & =\frac{P\left(E^c \cap F^c \cap G\right)}{P(G)} \\
& =\frac{P(G)-P(E \cap G)-P(G \cap F)}{P(G)} \\
& =\frac{P(G)[1-P(E)-P(F)]}{P(G)} \\
& =1-P(E)-P(F) \\
& =P\left(E^c\right)-P(F) .
\end{aligned}
$$

</details>

---

### Q20. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $H_1, H_2, \ldots, H_n$ be mutually exclusive events with $P\left(H_i\right)>0, i=1,2, \ldots, n$. Let $E$ be any other event with $0 < P(E) < 1$.
Statement I $P\left(H_i / E\right)>P\left(E / H_i\right) P\left(H_i\right)$ for $i=1,2, \ldots, n$.
Statement II $\sum_{i=1}^n P\left(H_i\right)=1$

**Options:**

- **(A)** Statement I is true, Statement II is true; Statement II is a correct explanation for Statement I
- **(B)** Statement I is true, Statement II is true; Statement II is not a correct explanation for Statement II
- **(C)** Statement I is true, Statement II is false
- **(D)** Statement I is false, Statement II is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement I is false, Statement II is true**

**Detailed Solution:**

Statement : I If $P\left(H_i \cap E\right)=0$ for some $i$, then
$$
P\left(\frac{H_i}{E}\right)=P\left(\frac{E}{H_i}\right)=0
$$
If $P\left(H_i \cap E\right) \neq 0$ for $\forall i=1,2, \ldots . n$, then
$$
\begin{aligned}
P\left(\frac{H_i}{E}\right) & =\frac{P\left(H_i \cap E\right)}{P\left(H_i\right)} \times \frac{P\left(H_i\right)}{P(E)} \\
& \left.=\frac{P\left(\frac{E}{H_i}\right) \times P\left(H_i\right)}{P(E)}>P\left(\frac{E}{H_i}\right) \cdot P\left(H_i\right) \quad \text { [as } 0 < P(E) < 1\right]
\end{aligned}
$$
Hence, Statement I may not always be true.
Statement II
Clearly, $H_1 \cup H_2 \cup \ldots . \cup H_n=S$ (sample space)
$$
\Rightarrow \quad P\left(H_1\right)+P\left(H_2\right)+\ldots+P\left(H_n\right)=1 .
$$
Hence, Statement II is true.

</details>

---

### Q21. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

One Indian and four American men and their wives are to be seated randomly around a circular table. Then, the conditional probability that the Indian man is seated adjacent to his wife given that each American man is seated adjacent to his wife, is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{5}$**

**Detailed Solution:**

Let $E=$ event when each American man is seated adjacent to his wife and $A=$ event when Indian man is seated adjacent to his wife.
Now, $n(A \cap E)=(4 !) \times(2 !)^5$
Even when each American man is seated adjacent to his wife.
Again
$$
\begin{aligned}
n(E) & =(5 !) \times(2 !)^4 \\
P\left(\frac{A}{E}\right) & =\frac{n(A \cap E)}{n(E)} \\
& =\frac{(4 !) \times(2 !)^5}{(5 !) \times(2 !)^4}=\frac{2}{5}
\end{aligned}
$$
$$
\Rightarrow \quad P\left(\frac{A}{E}\right)=\frac{n(A \cap E)}{n(E)}
$$
ALITER
Fixing four American couples and one Indian man in between any two couples, we have 5 different ways in which his wife can be seated, of which 2 cases are favourable. $\therefore$ Required probability $=\frac{2}{5}$.

</details>

---

### Q22. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
There are $n$ urns each containing $(n+1)$ balls such that the ith urn contains $i$ white balls and $(n+1-i)$ red balls. Let $u_i$ be the event of selecting ith urn, $i=1,2,3, \ldots, n$ and $W$ denotes the event of getting a white balls.<strong>Question:</strong>
If $n$ is even and $E$ denotes the event of choosing even numbered urn $\left(P\left(u_i\right)=\frac{1}{n}\right)$, then the value of $P(W / E)$ is

**Options:**

- **(A)** $\frac{n+2}{2 n+1}$
- **(B)** $\frac{n+2}{2(n+1)}$
- **(C)** $\frac{n}{n+1}$
- **(D)** $\frac{1}{n+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{n+2}{2(n+1)}$**

**Detailed Solution:**

$P(W / E)=\frac{2+4+6+\ldots}{\frac{n(n+1)}{2}}=\frac{n+2}{2(n+1)}$

</details>

---

### Q23. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
There are $n$ urns each containing $(n+1)$ balls such that the ith urn contains $i$ white balls and $(n+1-i)$ red balls. Let $u_i$ be the event of selecting ith urn, $i=1,2,3, \ldots, n$ and $W$ denotes the event of getting a white balls.<strong>Question:</strong>
If $P\left(u_i\right)=c$, where $c$ is a constant, then $P\left(u_i / W\right)$ is equal to

**Options:**

- **(A)** $\frac{2}{n+1}$
- **(B)** $\frac{1}{n+1}$
- **(C)** $\frac{n}{n+1}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{n+1}$**

**Detailed Solution:**

$P\left(\frac{u_i}{W}\right)=\frac{\frac{n}{n+1}}{\frac{\Sigma i}{n+1}}=\frac{2}{n+1}$

</details>

---

