# JEE Advanced Mathematics - Functions

## Topic 2: Types of Function (Mapping)

**Total Questions:** 8

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

Let $\mathbb{N}$ denote the set of all positive integers. Consider the sets
$A = \{1, 2, 3, 4, 5\}$ and $B = \{1, 2, 3, 4, 5, 6, 7\}$.
Let $S$ be the set of all functions $f: A \rightarrow B$ such that $f(2) \neq 2$ and $f(4) \neq 4$. Consider the set
$T = \{f \in S : \text{there exists a function } g : B \rightarrow \mathbb{N} \text{ such that } g(f(x)) = 2^x \text{ for all } x \in A\}$.
Then the number of elements in the set $T$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1860**

**Detailed Solution:**

The condition $g(f(x)) = 2^x$ for all $x \in A$ implies that if $f(x_1) = f(x_2)$, then $g(f(x_1)) = g(f(x_2))$, which gives $2^{x_1} = 2^{x_2} \Rightarrow x_1 = x_2$.

Thus, $f$ must be an injective (one-to-one) function. Conversely, if $f$ is injective, such a function $g$ can always be constructed. Therefore, $T$ is the set of all injective functions $f: A \rightarrow B$ such that $f(2) \neq 2$ and $f(4) \neq 4$.

The total number of injective functions from $A$ to $B$ is $^{7}P_{5} = 7 \times 6 \times 5 \times 4 \times 3 = 2520$.

Let $E_2$ be the set of injective functions where $f(2) = 2$. The number of such functions is $^{6}P_{4} = 6 \times 5 \times 4 \times 3 = 360$.

Let $E_4$ be the set of injective functions where $f(4) = 4$. The number of such functions is $^{6}P_{4} = 360$.

Let $E_2 \cap E_4$ be the set of injective functions where both $f(2) = 2$ and $f(4) = 4$. The number of such functions is $^{5}P_{3} = 5 \times 4 \times 3 = 60$.

Using the Principle of Inclusion-Exclusion, the number of injective functions where $f(2) = 2$ or $f(4) = 4$ is:

$|E_2 \cup E_4| = |E_2| + |E_4| - |E_2 \cap E_4| = 360 + 360 - 60 = 660$

The number of elements in the set $T$ is the number of injective functions where $f(2) \neq 2$ and $f(4) \neq 4$, which is:

$|T| = 2520 - 660 = 1860$

Answer: $1860$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let $\mathbb{N}$ denote the set of all natural numbers, and $\mathbb{Z}$ denote the set of all integers. Consider the functions $f: \mathbb{N} \rightarrow \mathbb{Z}$ and $g: \mathbb{Z} \rightarrow \mathbb{N}$ defined by
$f(n)= \begin{cases}(n+1) / 2 & \text { if } n \text { is odd } \\ (4-n) / 2 & \text { if } n \text { is even }\end{cases}$ And
$g(n)=\left\{\begin{array}{cc}3+2 n & \text { if } n \geq 0 \\ -2 n & \text { if } n <0\end{array}\right.$
Define $(g \circ f)(n)=g(f(n))$ for all $n \in \mathbb{N}$, and $(f \circ g)(n)=f(g(n))$ for all $n \in \mathbb{Z}$.
Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** $g \circ f$ is NOT one-one and $g \circ f$ is NOT onto
- **(B)** $f \circ \mathrm{~g}$ is NOT one-one but $f \circ g$ is onto
- **(C)** $g$ is one-one and $g$ is onto
- **(D)** $f$ is NOT one-one but $f$ is onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $f$ is NOT one-one but $f$ is onto**

**Detailed Solution:**

$\begin{aligned}
& f(n)= \begin{cases}(n+1) / 2 & \text { if } n \text { is odd } \\
(4-n) / 2 & \text { if } n \text { is even }\end{cases} \\
& f(n)=\{(1,1),(2,1),(3,2),(4,0),(5,3),(6,-1), \ldots\}
\end{aligned}$
$\therefore \mathrm{f}(\mathrm{n})$ is many one and onto function
$\begin{aligned}
& \mathrm{g}(\mathrm{n})=\left\{\begin{array}{cc}
3+2 \mathrm{n} & \text { if } \mathrm{n} \geq 0 \\
-2 \mathrm{n} & \text { if } \mathrm{n} <0
\end{array}\right. \\
& \mathrm{g}(\mathrm{n})=\{(-3,6),(-2,4),(-1,2),(0,3),(1,5),(2,7),(3,9),(4,15), \ldots\}
\end{aligned}$
$\therefore \mathrm{g}(\mathrm{n})$ is one-one and into function
$\mathrm{f}(\mathrm{~g}(\mathrm{n}))=2+\mathrm{n}, \mathrm{n} \in \mathrm{~N}$
fog is one-one and into
$g(f(n))= \begin{cases}4+n & \text { if } n \text { is odd natural number } \\ 7-n & \text { if } n=2,4 \\ n-4 & \text { if } n \text { is even natural number and } n \geq 6\end{cases}$
$g(f(2))=g(f(1))=5$
$\therefore$ gof is many one and into

</details>

---

### Q3. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \rightarrow \mathbb{R}$ be functions defined by
$f(x)=\left\{\begin{array}{ll}x|x| \sin \left(\frac{1}{x}\right), & x \neq 0, \\ 0, & x=0,\end{array} \quad\right.$ and $g(x)= \begin{cases}1-2 x, & 0 \leq x \leq \frac{1}{2} \\ 0, & \text { otherwise }\end{cases}$
Let $a, b, c, d \in \mathbb{R}$. Define the function $h: \mathbb{R} \rightarrow \mathbb{R}$ by
$h(x)=a f(x)+b\left(g(x)+g\left(\frac{1}{2}-x\right)\right)+c(x-g(x))+d g(x), x \in \mathbb{R}$
Match each entry in List-I to the correct entry in List-II.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/nrkrO606_pYoz9NDZdy0NvwQoPvGnP3KN4DANL3H2vg.original.fullsize.png"/>
The correct option is :

**Options:**

- **(A)** $(\mathrm{P}) \rightarrow(4) \quad(\mathrm{Q}) \rightarrow(3) \quad(\mathrm{R}) \rightarrow(1) \quad(\mathrm{S}) \rightarrow(2)$
- **(B)** $(\mathrm{P}) \rightarrow(5) \quad(\mathrm{Q}) \rightarrow(2) \quad(\mathrm{R}) \rightarrow(4) \quad(\mathrm{S}) \rightarrow(3)$
- **(C)** $(\mathrm{P}) \rightarrow(5) \quad(\mathrm{Q}) \rightarrow(3) \quad(\mathrm{R}) \rightarrow(2) \quad(\mathrm{S}) \rightarrow(4)$
- **(D)** $(\mathrm{P}) \rightarrow(4) \quad(\mathrm{Q}) \rightarrow(2) \quad(\mathrm{R}) \rightarrow(1) \quad(\mathrm{S}) \rightarrow(3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\mathrm{P}) \rightarrow(5) \quad(\mathrm{Q}) \rightarrow(3) \quad(\mathrm{R}) \rightarrow(2) \quad(\mathrm{S}) \rightarrow(4)$**

**Detailed Solution:**

$f(x)=\left\{\begin{array}{ccc}x|x| \sin \frac{1}{x} & ; & x \neq 0 \\ 0 & ; & x=0\end{array} \quad g(x)=\left\{\begin{array}{ccc}1-2 x & ; & 0 \leq x \leq \frac{1}{2} \\ 0 & ; & \text { otherwise }\end{array}\right.\right.$
$g\left(\frac{1}{2}-x\right)=\left\{\begin{array}{ccc}2 x & ; & 0 \leq \frac{1}{2}-x \leq \frac{1}{2} \\ 0 & ; & \text { otherwise }\end{array}=\left\{\begin{array}{ccc}2 x & ; & 0 \leq x \leq \frac{1}{2} \\ 0 & ; & \text { otherwise }\end{array}\right\}\right.$
$g(x)+g\left(\frac{1}{2}-x\right)=\left\{\begin{array}{lll}1 & ; & 0 \leq x \leq \frac{1}{2} \\ 0 & ; & \text { otherwise }\end{array}\right\}$
(P)
Now $\mathrm{a}=0, \mathrm{~b}=1, \mathrm{c}=0, \mathrm{~d}=0$
$\because \mathrm{h}(\mathrm{x})=\mathrm{g}(\mathrm{x})+\mathrm{g}\left(\frac{1}{2}-\mathrm{x}\right)=\left\{\begin{array}{lll}1 & ; & 0 \leq \mathrm{x} \leq \frac{1}{2} \\ 0 & ; & \text { otherwise }\end{array}\right.$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/FU6ErKJcw1b6Ugc_uZHdOCy-0-4eCSNlNENZ6ZlOVA0.original.fullsize.png">
Hence Range of $\mathrm{h}(\mathrm{x})$ is $\{0,1\}$
(Q)
$\begin{aligned} & \mathrm{a}=1, \mathrm{~b}=0, \mathrm{c}=0, \mathrm{~d}=0 \\ & \mathrm{~h}(\mathrm{x})=\mathrm{f}(\mathrm{x})=\left\{\begin{array}{cll}\mathrm{x}|\mathrm{x}| \sin \frac{1}{x} & ; & x \neq 0 \\ 0 & ; & x=0\end{array}\right. \\ & \text { RHD }=\lim _{x \rightarrow 0} \frac{x^2 \sin \frac{1}{x}-0}{x}=0 \\ & \text { LHD }=\lim _{x \rightarrow 0} \frac{-x^2 \sin \frac{1}{x}-0}{x}=0\end{aligned}$
Hence $\mathrm{h}(\mathrm{x})$ is differentiable on $\mathrm{R}$
(R)
$\begin{aligned} & \mathrm{a}=0, \mathrm{~b}=0, \mathrm{c}=1, \mathrm{~d}=0 \\ & h(x)=x-g(x)=\left\{\begin{array}{ccc}3 \mathrm{x}-1 & ; & 0 \leq x \leq \frac{1}{2} \\ 0 & ; & \text { otherwise }\end{array}\right.\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/QgpDEfXIpt5R3dnZQTjioqVT4T3ntKxfyEsxy0Wkopg.original.fullsize.png">
$\therefore \mathrm{h}(\mathrm{x})$ is ONTO
(S)
$\begin{aligned} & \mathrm{a}=0, \mathrm{~b}=0, \mathrm{c}=0, \mathrm{~d}=1 \\ & \mathrm{~h}(\mathrm{x})=\mathrm{g}(\mathrm{x})=\left\{\begin{array}{ccl}1-2 \mathrm{x} & ; & 0 \leq \mathrm{x} \leq \frac{1}{2} \\ 0 & ; & \text { otherwise }\end{array}\right.\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/DMQd_tpu8Cx0ZbSA5HdTO_YFmXkclNMDfXBlZ6bGPbI.original.fullsize.png">
Range of $h(x)$ is $[0,1]$

</details>

---

### Q4. JEE Advanced 2020 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> is defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mfenced><mrow><mi>x</mi><mo>&#8722;</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></math>, then which of the following statements is TRUE?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is one-one, but NOT onto
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is onto, but NOT one-one
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is BOTH one-one and onto
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is NEITHER one-one NOR onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> is BOTH one-one and onto**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mfenced><mrow><mi>x</mi><mo>−</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></math> is odd function <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>∵</mo><mi>f</mi><mfenced><mrow><mo>−</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>−</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mi>x</mi><mi>sin</mi><mi>x</mi><mo>∀</mo><mo> </mo><mi>x</mi><mo>≥</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>−</mo><mi>x</mi><mi>cos</mi><mi>x</mi><mo>−</mo><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>−</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>x</mi><mfenced><mrow><mn>1</mn><mo>−</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>></mo><mn>0</mn></math></p><p><math> <mo>∴</mo> </math>Graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/49bbc940-7a45-4925-a495-8090a37655b5-image.png"/></p><p>From graph, it's one-one and onto both.</p>

</details>

---

### Q5. JEE Advanced 2018 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be a set with exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> elements and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> be a set with exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> elements. If <math><mi>&#945;</mi></math> is the number of one-one functions from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#8594;</mo><mi>Y</mi></math> and <math><mi>&#946;</mi></math> is the number of onto functions from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>&#8594;</mo><mi>X</mi></math>, then the value of <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mfenced separators="|"><mrow><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math> is _____-.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **119**

**Detailed Solution:**

<math><mi>n</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math>
<math><mi>n</mi><mfenced separators="|"><mrow><mi>Y</mi></mrow></mfenced><mo>=</mo><mn>7</mn></math>
<math><mi>α</mi><mo>→</mo></math> Number of one-one function <math><mo>=</mo><msup><mrow></mrow><mrow><mn>7</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>×</mo><mn>5</mn><mo>!</mo></math>
<math><mi>β</mi><mo>→</mo></math> Number of onto function Y to X
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/posqcetnvugxkkjgrjmbvthrbwhctnnjlqdhseyzhvrlmfqpcb.png"/>
So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>4</mn><mo>!</mo></mrow></mfrac><mo>×</mo><mn>5</mn><mo>!</mo><mo>+</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><msup><mfenced separators="|"><mrow><mn>2</mn><mo>!</mo></mrow></mfenced><mn>3</mn></msup><mn>3</mn><mo>!</mo></mrow></mfrac><mo>×</mo><mn>5</mn><mo>!</mo><mo>=</mo><mfenced separators="|"><mrow><msup><mrow></mrow><mn>7</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>+</mo><mn>3</mn><mo>.</mo><msup><mi> </mi><mn>7</mn></msup><msub><mi>C</mi><mn>3</mn></msub></mrow></mfenced><mn>5</mn><mo>!</mo><mo>=</mo><mn>4</mn><msup><mo>×</mo><mn>7</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>×</mo><mn>5</mn><mo>!</mo></math>
<math><mfrac><mrow><mi>β</mi><mo>-</mo><mi>α</mi></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>4</mn><mo>×</mo><msup><mrow></mrow><mrow><mn>7</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>-</mo><msup><mrow></mrow><mrow><mn>7</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><mn>4</mn><mo>×</mo><mn>35</mn><mo>-</mo><mn>21</mn><mo>=</mo><mn>119</mn></math>

</details>

---

### Q6. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

let <math><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mi>&#160;</mi><mo>:</mo><mfenced open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>&#8594;</mo><mi>R</mi><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>f</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>&#160;</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>f</mi></mrow><mrow><mn>4</mn></mrow></msub><mi>&#160;</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mo>[</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi><mo>)</mo></math> be defined by
<math><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mi>&#160;</mi><mo>;</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>;</mo><msub><mrow><mi>f</mi></mrow><mrow><mn>3</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>f</mi></mrow><mrow><mn>4</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>x</mi><mo>&#60;</mo><mn>0</mn></mtd></mtr><mtr><mtd><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced><mo>-</mo><mn>1</mn></mtd><mtd><mi>i</mi><mi>f</mi></mtd><mtd><mi>x</mi><mo>&#8805;</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
 <table border="1">	<tbody>		<tr>			<td> </td>			<td>List &ndash; I</td>			<td> </td>			<td>List &ndash; II</td>		</tr>		<tr>			<td>(A)</td>			<td><math><msub><mrow><mi>f</mi></mrow><mrow><mn>4</mn></mrow></msub></math> is</td>			<td>(P)</td>			<td>Onto but not one &ndash; one</td>		</tr>		<tr>			<td>(B)</td>			<td><math><msub><mrow><mi>f</mi></mrow><mrow><mn>3</mn></mrow></msub></math> is</td>			<td>(Q)</td>			<td>neither continuous nor one-one</td>		</tr>		<tr>			<td>(C)</td>			<td><math><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub></math> of <math><msub><mrow><mi>f</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is</td>			<td>(R)</td>			<td>differentiable but not one-one</td>		</tr>		<tr>			<td>(D)</td>			<td><math><msub><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is</td>			<td>(S)</td>			<td>continuous and one-one</td>		</tr>	</tbody></table>

**Options:**

- **(A)** a-q;b-r;c-s;d-p;
- **(B)** a-p;b-r;c-q;d-s;
- **(C)** a-q;b-s;c-r;d-p;
- **(D)** a-q;b-p;c-r;d-s;

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a-p;b-r;c-q;d-s;**

**Detailed Solution:**

<p><math><msub><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo><</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">x</mi></mrow></msup></mtd><mtd><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>≥</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><msub><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>:</mo><mi mathvariant="normal">R</mi><mo>→</mo><mo>[</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal"> </mi><mi mathvariant="normal">∞</mi><mo>)</mo></math>
<math><msub><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mn>4</mn></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><msub><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi></mrow></mfenced></mrow></mfenced></mtd><mtd><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo><</mo><mn>0</mn></mtd></mtr><mtr><mtd><msub><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi mathvariant="normal">f</mi></mrow><mrow><mn>1</mn></mrow></msub><mfenced separators="|"><mrow><mi mathvariant="normal">x</mi></mrow></mfenced></mrow></mfenced><mo>-</mo><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>≥</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo><</mo><mn>0</mn></mtd></mtr><mtr><mtd><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mn>2</mn><mi mathvariant="normal">x</mi></mrow></msup><mo>-</mo><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mi mathvariant="normal">x</mi><mo>≥</mo><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image2-b02e0f52-9809-46c1-bd93-0d6a920101fb.jpg"/>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image3-a37b2d3e-7ac2-4f93-a117-7d3a8b7b04fc.jpg"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced></math> is continuous and one-one.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image4-66b7280a-9b26-4633-ab53-ea0fe347f513.jpg"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>3</mn></msub><mfenced><mi>x</mi></mfenced></math> is differentiable but not one-one.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image5-411eee2e-6be6-4460-8885-46e17ada6323.jpg"/></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>2</mn></msub><mfenced><mrow><msub><mi>f</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced></mrow></mfenced></math> is neither one one nor continuous.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image6-7fc5df5d-2648-4296-b9ab-727f68f8ed76.jpg"/> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mn>4</mn></msub><mfenced><mi>x</mi></mfenced></math> is onto but not one-one.</p>

</details>

---

### Q7. JEE Advanced 2014 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mi>&#160;</mi><mo>:</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be given by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>.</mo></math> Then

**Options:**

- **(A)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is an odd function
- **(B)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is a one - one function
- **(C)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is an onto function
- **(D)** <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>  is an even function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is an onto function**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="italic">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="italic">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mi> </mi><mo>&forall;</mo><mi> </mi><mi>x</mi><mi> </mi><mo>&isin;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&pi;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&pi;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi> </mi><mo>-</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>,</mo></math> hence <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is odd function
Let <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mi> </mi><mo>&forall;</mo><mi> </mi><mi>x</mi><mi> </mi><mo>&isin;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&pi;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&pi;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>&rArr;</mo></math> <math><msup><mrow><mi>g</mi></mrow><mrow><mi>&prime;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>&gt;</mo><mn>0</mn><mi> </mi><mo>&forall;</mo><mi> </mi><mi>x</mi><mi> </mi><mo>&isin;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&pi;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&pi;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>&rArr;</mo></math> <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is one - one function
Hence <math><msup><mrow><mfenced separators="|"><mrow><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mrow></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></math> is one - one function.
And <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi> </mi><mo>&isin;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mi>&infin;</mi></mrow></mfenced><mi> </mi><mo>&forall;</mo><mi> </mi><mi>x</mi><mo>&isin;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&pi;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi>&pi;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>&rArr;</mo></math> <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></mrow><mi> </mi><mo>&isin;</mo><mi>R</mi></math> Hence <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is an onto function.

</details>

---

### Q8. JEE Advanced 2012 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The function $f:[0,3] \rightarrow[1,29]$, defined by $f(x)=2 x^{3}-15 x^{2}+36 x+1$, is

**Options:**

- **(A)** one-one and onto
- **(B)** onto but not one-one
- **(C)** one-one but not onto
- **(D)** neither one-one nor onto

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) onto but not one-one**

**Detailed Solution:**

Given : $f(x)=2 x^{3}-15 x^{2}+36 x+1$

$\Rightarrow f^{\prime}(x)=6 x^{2}-30 x+36$

$=6\left(x^{2}-5 x+6\right)=6(x-2)(x-3)$

$\because f^{\prime}(x)>0 \forall x \in[0,2)$ and $f^{\prime}(x) < 0 \forall x \in(2,3)$

$\therefore f(x)$ is increasing on $[0,2)$ and decreasing

on $(2,3)$

$\therefore \quad f(x)$ is many one on $[0,3]$

Also $f(0)=1, f(2)=29, f(3)=28$

$\therefore \quad$ Absolute min $=1$ and Absolute max $=29$

$\therefore \quad$ Range of $f=[1,29]=$ codomain

Hence $f$ is onto.

</details>

---

