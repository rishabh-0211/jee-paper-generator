# JEE Advanced Mathematics - Permutation Combination

## Topic 1: Permutation

**Total Questions:** 3

---

### Q1. JEE Advanced 2025 (Paper 1)

*Type:* `numerical` | *Level:* `3`

Let $S$ be the set of all seven-digit numbers that can be formed using the digits 0,1 and 2 . For example, 2210222 is in $S$, but 0210222 is NOT in $S$.
Then the number of elements $x$ in $S$ such that at least one the digits 0 and 1 appears exactly twice in $x$, is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **762**

**Detailed Solution:**

Let $\mathrm{A} \rightarrow$ " 0 " appear exactly twice.
and $\mathrm{B} \rightarrow " 1 "$ appear exactly twice.
$\therefore \mathrm{A} \cap \mathrm{B} \rightarrow$ " 0 " and " 1 " both appears exactly twice.
$\mathrm{n}(\mathrm{A})=-\underbrace{-------}$
$={ }_{\text {placing zero }}^6 \mathrm{C}_2(1)(2)^5=\frac{6 \times 5}{2} \times 2^5=480$ for $\mathrm{n}(\mathrm{B})$
C-I : $1$ at first place
$\underline{1}\underbrace{-------}$
$\text { Number of ways }=\underset{\text { placing } 1}{} \mathrm{}^6{C}_1(1)(2)^5=192$
C-II : 2 at first place
$\underline{2}\underbrace{-------}$
Number of ways $=\underset{\text { placing } 1}{{ }^6 \mathrm{C}_2(1)(2)^4}=\frac{6 \times 5}{2} \times 2^4=240$
$n(B)=240+192$
for $\mathrm{n}(\mathrm{A} \cap \mathrm{B})$
$\underline{}\underbrace{-------}$
for $\mathrm{n}(\mathrm{A} \cap \mathrm{B})=\underset{\text { placing zero }}{{ }^6 \mathrm{C}_2(1)} \times \underset{\text { placing } 1}{{ }^5 \mathrm{C}_2(1)} \times \underset{\text { 2at rest places } 1}{(1)} =\frac{6 \times 5}{2} \times \frac{5 \times 4}{2}=150$
$\begin{aligned} & \therefore \mathrm{n}(\mathrm{A} \cup \mathrm{B})=\mathrm{n}(\mathrm{A})+\mathrm{n}(\mathrm{B})-\mathrm{n}(\mathrm{A} \cap \mathrm{B}) \\ & =480+(192+240)-150 \\ & =762\end{aligned}$

</details>

---

### Q2. JEE Advanced 2022 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> boxes, where each box contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> red balls and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> blue balls. Assume that all <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> balls are distinct. In how many different ways can <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> balls be chosen from these <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> boxes so that from each box at least one red ball and one blue ball are chosen?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21816</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>85536</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12096</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>156816</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21816</mn></math>**

**Detailed Solution:**

<blockquote><p>Let the four boxes be Box-1, Box-2, Box-3 and Box-4. Each of the box has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> red balls and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> blue balls.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/cd4298df-b141-419b-9626-33ce4672e39a-image.png" style="width: 475px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> balls can be chosen in:</p><p>Case I - When exactly one box gives four balls</p><p>Case II - When exactly two boxes gives three balls</p><p>Required number of ways<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Number of ways in Case I <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math> Number of ways in Case II.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mfenced close="]" open="["><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts></mrow></mfenced><msup><mfenced><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mfenced close="]" open="["><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts></mrow></mfenced><mn>2</mn></msup><msup><mfenced close="]" open="["><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfenced><mn>5</mn></mfenced><msup><mfenced><mn>6</mn></mfenced><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mfenced><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mn>6</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4320</mn><mo>+</mo><mn>17496</mn><mo>=</mo><mn>21816</mn></math></p></blockquote>

</details>

---

### Q3. JEE Advanced 2007 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

The letters of the word $\mathrm{COCHIN}$ are permuted and all the permutations are arranged in an alphabetical order as in an English dictionary. The number of words that appear before the word $\mathrm{COCHIN}$ is

**Options:**

- **(A)** 360
- **(B)** 192
- **(C)** 97
- **(D)** 48

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 97**

**Detailed Solution:**

In a word $\mathrm{COCHIN}$, the second place can be filled in ${ }^4 C_1$ ways and the remaining four alphabets can be arranged in $4 !$ ways in four different places. The next $97^{\text {th }}$ word will be COCHIN.

</details>

---

