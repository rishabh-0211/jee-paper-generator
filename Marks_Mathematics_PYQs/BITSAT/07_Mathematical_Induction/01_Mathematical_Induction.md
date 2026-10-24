# BITSAT Mathematics - Mathematical Induction

## Topic 1: Mathematical Induction

**Total Questions:** 3

---

### Q1. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

For all $n \in N$, the sum of $\frac{n^5}{5}+\frac{n^3}{3}+\frac{7 n}{15}$ is

**Options:**

- **(A)** a negative integer
- **(B)** a whole number
- **(C)** a real number
- **(D)** a natural number

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a natural number**

**Detailed Solution:**

Let the statement $\mathrm{P}(\mathrm{n})$ be defined as $P(n): \frac{n^5}{5}+\frac{n^3}{3}+\frac{7 n}{15}$ is a natural number for all $n \in N$ :
Step I : For $\mathrm{n}=1, \mathrm{P}(1): \frac{1}{5}+\frac{1}{3}+\frac{7}{15}=1 \in \mathrm{N}$
Hence, it is true for $\mathrm{n}=1$.
Step II : Let it is true for $n=k$,
i.e. $\frac{k^5}{5}+\frac{k^3}{3}+\frac{7 k}{15}=\lambda \in N$ $\ldots$ (i)
Step III : For $\mathrm{n}=\mathrm{k}+1$,
$\frac{(\mathrm{k}+1)^5}{5}+\frac{(\mathrm{k}+1)^3}{3}+\frac{7(\mathrm{k}+1)}{15}$
$=\frac{1}{5}\left(k^5+5 k^4+10 k^3+10 k^2+3 k+1\right)$ $+\frac{1}{3}\left(k^3+3 k^2+3 k+1\right)+\frac{7}{15} k+\frac{7}{15}$
$=\left(\frac{k^5}{5}+\frac{k^3}{3}+\frac{7}{15} k\right)+\left(k^4+2 k^3+3 k^2+2 k\right)$ $+\frac{1}{5}+\frac{1}{3}+\frac{7}{15}$
$=\lambda+\mathrm{k}^4+2 \mathrm{k}^3+3 \mathrm{k}^2+2 \mathrm{k}+1$ [using equation (i)]
which is a natural number, since $\lambda \mathrm{k} \in \mathrm{N}$. Therefore, $P(k+1)$ is true, when $P(k)$ is true. Hence, from the principle of mathematical induction, the statement is true for all natural numbers $\mathrm{n}$

</details>

---

### Q2. BITSAT 2017

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>13</mn><mi>y</mi></math> subject to constraints <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>&#8804;</mo><mn>18</mn><mo>,</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#8804;</mo><mn>10</mn><mo>,</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>&#8805;</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>130</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>79</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>79</mn></math>**

**Detailed Solution:**

<blockquote><p>Given, constraints are<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>&#8804;</mo><mn>18</mn><mo>,</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#8804;</mo><mn>10</mn><mo>,</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>&#8805;</mo><mn>0</mn></math>.</p><p>The feasible region is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>A</mi><mi>B</mi><mi>C</mi><mi>O</mi></math>.</p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>13</mn><mi>y</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/c2f3790a-5526-4e70-a0ca-9837eb432ade-d62.png" style="width: 326px; height: 230px;" /></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mo>(</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mi>z</mi><mo>=</mo><mn>0</mn></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mn>5</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mi>z</mi><mo>=</mo><mn>45</mn></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mi>z</mi><mo>=</mo><mn>27</mn><mo>+</mo><mn>52</mn><mo>=</mo><mn>79</mn></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>(</mo><mn>0</mn><mo>,</mo><mn>6</mn><mo>)</mo><mo>,</mo><mi>z</mi><mo>=</mo><mn>78</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>79</mn></math>.</p></blockquote>

</details>

---

### Q3. BITSAT 2012

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{T}(k)$ be the statement $1+3+5+\ldots+$ $(2 k-1)=k^{2}+10$
Which of the following is correct?

**Options:**

- **(A)** $\mathrm{T}(1)$ is true
- **(B)** $\mathrm{T}(k)$ is true $\Rightarrow \mathrm{T}(k+1)$ is true
- **(C)** $\mathrm{T}(n)$ is true for all $n \in \mathbf{N}$
- **(D)** All above are correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{T}(k)$ is true $\Rightarrow \mathrm{T}(k+1)$ is true**

**Detailed Solution:**

When $\mathrm{k}=1, \mathrm{LHS}=1$ but $\mathrm{RHS}=1+10=11$
$\therefore \mathrm{T}(1)$ is not true Let $\mathrm{T}(k)$ is true. That is
$\begin{array}{l}
1+3+5+\ldots .+(2 k-1)=k^{2}+10 \\
\text { Now, } 1+3+5+\ldots . .+(2 k-1)+(2 k+1) \\
=k^{2}+10+2 k+1=(k+1)^{2}+10
\end{array}$
$\therefore \mathrm{T}(k+1)$ is true.
That is $\mathrm{T}(k)$ is true $\Rightarrow \mathrm{T}(k+1)$ is true.
But $\mathrm{T}(n)$ is not true for all $n \in \mathbf{N},$ as $\mathrm{T}(1)$ is not true.

</details>

---

