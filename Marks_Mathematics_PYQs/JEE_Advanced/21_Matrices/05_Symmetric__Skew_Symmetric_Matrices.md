# JEE Advanced Mathematics - Matrices

## Topic 5: Symmetric & Skew Symmetric Matrices

**Total Questions:** 5

---

### Q1. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\alpha$ and $\beta$ be the distinct roots of the equation $x^2+x-1=0$. Consider the set $T=\{1, \alpha, \beta\}$. For a $3 \times 3$ matrix $M=\left(a_{i j}\right)_{3 \times 3}$, define $R_i=a_{i 1}+a_{i 2}+a_{i 3}$ and $C_j=a_{1 j}+a_{2 j}+a_{3 j}$ for $i=1,2,3$ and $j=1,2,3$.
Match each entry in List-I to the correct entry in List-II.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/J0FVDqX6LCy_bvJ2UQfQFH9zM_8m9tjPV3jFoG4Wa1o.original.fullsize.png"/>
The correct option is

**Options:**

- **(A)** $(\mathrm{P}) \rightarrow(4) \quad(\mathrm{Q}) \rightarrow(2) \quad(\mathrm{R}) \rightarrow(5) \quad(\mathrm{S}) \rightarrow(1)$
- **(B)** $(\mathrm{P}) \rightarrow(2) \quad(\mathrm{Q}) \rightarrow(4) \quad(\mathrm{R}) \rightarrow(1) \quad(\mathrm{S}) \rightarrow(5)$
- **(C)** $(\mathrm{P}) \rightarrow(2) \quad(\mathrm{Q}) \rightarrow(4) \quad(\mathrm{R}) \rightarrow(3) \quad(\mathrm{S}) \rightarrow(5)$
- **(D)** $(\mathrm{P}) \rightarrow(1) \quad(\mathrm{Q}) \rightarrow(5) \quad(\mathrm{R}) \rightarrow(3) \quad(\mathrm{S}) \rightarrow(4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\mathrm{P}) \rightarrow(2) \quad(\mathrm{Q}) \rightarrow(4) \quad(\mathrm{R}) \rightarrow(3) \quad(\mathrm{S}) \rightarrow(5)$**

**Detailed Solution:**

$\begin{aligned} & \alpha, \beta \text { are roots of } \mathrm{x}^2+\mathrm{x}-1=0 \\ & \therefore \alpha+\beta=-1 \Rightarrow 1+\alpha+\beta=0 \\ & M=\left[\begin{array}{lll}\mathrm{a}_{11} & \mathrm{a}_{12} & \mathrm{a}_{13} \\ \mathrm{a}_{21} & \mathrm{a}_{22} & \mathrm{a}_{23} \\ \mathrm{a}_{31} & \mathrm{a}_{32} & \mathrm{a}_{33}\end{array}\right]\end{aligned}$
(P)
$M=\left[\begin{array}{lll}1 & \alpha & \beta \\\alpha & \beta & 1 \\\beta & 1 & \alpha\end{array}\right] \Rightarrow 3!\times 2=12$
For one arrangement of row 1 we can arrange other two rows exactly in two ways and row 1 can be arranged in 3 ! ways
$\therefore 3!\times 2=12 \text { ways }$
(Q)
$M=\left[\begin{array}{lll}x & a & b \\ a & y & c \\ b & c & z\end{array}\right] \Rightarrow$ Consider one such arrangement with $a=\alpha, b=\beta, c=1$
$M=\left[\begin{array}{lll}1 & \alpha & \beta \\ \alpha & \beta & 1 \\ \beta & 1 & \alpha\end{array}\right]$
a, b, c can be arranged in $3 !$ ways and corresponding entries can be arranged in 1 way.
(R)
$\left[\begin{array}{ccc}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right]\left[\begin{array}{l}x \\ y \\ z\end{array}\right]=\left[\begin{array}{c}a \\ 0 \\ -c\end{array}\right]$
$\begin{aligned}& a y+b z=a \\& -a x+c z=0 \\& -b x-c y=-c\end{aligned}$
It is observed that $\mathrm{D}=\mathrm{D}_{\mathrm{x}}=\mathrm{D}_{\mathrm{y}}=\mathrm{D}_{\mathrm{z}}=0$
$\therefore$ infinite solution
(S)
$\left[\begin{array}{lll}1 & \alpha & \beta \\ \beta & \alpha & 1 \\ \alpha & 1 & \beta\end{array}\right]$
$\Rightarrow \alpha \beta-1-\alpha \beta^2+\alpha^2+\beta^2-\alpha^2 \beta=0 \quad($ since $\alpha \beta=\alpha+\beta=-1$ )

</details>

---

### Q2. JEE Advanced 2015 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mi mathvariant="normal">X</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">Y</mi></math> be two arbitrary, <math><mn>3</mn><mi mathvariant="normal">&#160;</mi><mo>&#215;</mo><mn>3</mn></math> , non - zero, skew - symmetric matrices and Z be an arbitrary <math><mn>3</mn><mi mathvariant="normal">&#160;</mi><mo>&#215;</mo><mn>3</mn></math> , non - zero, symmetric matrix. Then which of the following matrices is (are) skew symmetric ?

**Options:**

- **(A)** <math><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
- **(B)** <math><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>44</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>44</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>4</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>23</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>23</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>23</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>23</mn></mrow></msup></math>**

**Detailed Solution:**

<math><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>=</mo><mo>-</mo><mi mathvariant="normal">X</mi><mo>,</mo><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>=</mo><mo>-</mo><mi mathvariant="normal">Y</mi></math>  and  <math><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>=</mo><mi mathvariant="normal">Z</mi></math> 
 <math><mi mathvariant="normal">P</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup></math> 
 <math><msup><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></math> 
 <math><mo>=</mo><mi mathvariant="normal"> </mi><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></math> 
 <math><mo>=</mo><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mo>-</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup></math> 
 <math><mo>=</mo><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup><mi mathvariant="normal"> </mi><mo>–</mo><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>3</mn></mrow></msup><mi mathvariant="normal"> </mi><mo>=</mo><mi mathvariant="normal"> </mi><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">y</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">c</mi><mo>)</mo><mi mathvariant="normal"> </mi></math> 
 <math><mi mathvariant="normal">Q</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>44</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>44</mn></mrow></msup></math> 
 <math><msup><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>44</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>44</mn></mrow></msup><mo>=</mo><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>44</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>44</mn></mrow></msup><mo>=</mo></math>  Q(symmetric)
 <math><msup><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></math> 
 <math><mo>=</mo><mi mathvariant="normal"> </mi><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup><mi mathvariant="normal"> </mi><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></math> 
 <math><mo>=</mo><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal">X</mi></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal">X</mi></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">Z</mi></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></math> 
 <math><mo>=</mo><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mo>-</mo><mi mathvariant="normal">R</mi></math> (Skew Symmetric)
 <math><mi mathvariant="normal">S</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>23</mn></mrow></msup><mo>+</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>23</mn></mrow></msup></math> 
 <math><msup><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>23</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mi mathvariant="normal">T</mi></mrow></msup></mrow></mfenced></mrow><mrow><mn>23</mn></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal">X</mi></mrow></mfenced></mrow><mrow><mn>23</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mi mathvariant="normal">Y</mi></mrow></mfenced></mrow><mrow><mn>23</mn></mrow></msup></math> 
 <math><mo>=</mo><mo>-</mo><msup><mrow><mi mathvariant="normal">X</mi></mrow><mrow><mn>23</mn></mrow></msup><mo>-</mo><msup><mrow><mi mathvariant="normal">Y</mi></mrow><mrow><mn>23</mn></mrow></msup><mo>=</mo><mo>-</mo><mi mathvariant="normal">S</mi></math>  (Skew symmetric)

</details>

---

### Q3. JEE Advanced 2013 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

<p>For 3 x 3 matrices M and N, which of the following statement(s) is (are) not correct?</p>

**Options:**

- **(A)** N<sup>T</sup> MN is symmetric or skew-symmetric, according to as M is symmetric or skew-symmetric
- **(B)** ​MN - NM is skew symmetric for all symmetric matrices M and N
- **(C)** MN is symmetric for all symmetric matrices M and N
- **(D)** adj(M) adj(N) = adj (MN) for all invertible matrices M and N

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) adj(M) adj(N) = adj (MN) for all invertible matrices M and N**

**Detailed Solution:**

<math> <mrow> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mtext>N</mtext> <mtext>T</mtext> </msup> <mtext>MN</mtext> </mrow> </mfenced> </mrow> <mtext>T</mtext> </msup> <mo>=</mo> <msup> <mtext>N</mtext> <mtext>T</mtext> </msup> <msup> <mtext>M</mtext> <mtext>T</mtext> </msup> <mtext>N</mtext> </mrow> </math> is symmetric if M is symmetric and skew-symmetric if M is skew-symmetric.
<math> <mrow> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>MN</mtext> <mo>-</mo> <mtext>NM</mtext> </mrow> </mfenced> </mrow> <mtext>T</mtext> </msup> <mo>=</mo> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>MN</mtext> </mrow> </mfenced> </mrow> <mtext>T</mtext> </msup> <mo>-</mo> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>NM</mtext> </mrow> </mfenced> </mrow> <mtext>T</mtext> </msup> </mrow> </math>
                         <math> <mrow> <mo>=</mo> <mtext>NM</mtext> <mo>-</mo> <mtext>MN</mtext> </mrow> </math>
                         <math> <mrow> <mo>=</mo> <mo>-</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>MN</mtext> <mo>-</mo> <mtext>NM</mtext> </mrow> </mfenced> </mrow> </math>
skew symmetric
<math> <mrow> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>MN</mtext> </mrow> </mfenced> </mrow> <mtext>T</mtext> </msup> <mo>=</mo> <msup> <mtext>N</mtext> <mtext>T</mtext> </msup> <msup> <mtext>M</mtext> <mtext>T</mtext> </msup> </mrow> </math>
<math><mrow><mo>            = </mo> <mtext>NM</mtext> </mrow> </math>
            <math><mrow><mo> ≠ </mo> <mtext>MN</mtext> </mrow> </math> hence not correct
Standard result is
<math> <mrow> <mtext>adj</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mtext>MN</mtext> </mrow> </mfenced> <mo>=</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>adj N</mtext> </mrow> </mfenced> <mfenced close=")" open="(" separators=","> <mrow> <mtext>adj M</mtext> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <mo>≠</mo> <mfenced close=")" open="(" separators=","> <mrow> <mtext>adj M</mtext> </mrow> </mfenced> <mfenced close=")" open="(" separators=","> <mrow> <mtext>adj N</mtext> </mrow> </mfenced> </mrow> </math>

</details>

---

### Q4. JEE Advanced 2011 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let $M$ and $N$ be two $3 \times 3$ non-singular skew-symmetric matrices such that $M N=N M$. If $P^T$ denotes the transpose of $P$, then $M^2 N^2\left(M^T N\right)^{-1}\left(M N^{-1}\right)^T$ is equal to

**Options:**

- **(A)** $M^2$
- **(B)** $-N^2$
- **(C)** $-M^2$
- **(D)** $M N$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-M^2$**

**Detailed Solution:**

Given, $M^T=-M, N^T=-N$
and $\quad M N=N M$
$$
\begin{aligned}
\therefore & M^2 N^2\left(M^T N\right)^{-1}\left(M N^{-1}\right)^T \\
& =M^2 N^2 N^{-1}\left(M^T\right)^{-1}\left(N^{-1}\right)^T \cdot M^T \\
& =M^2 N\left(N N^{-1}\right)(-M)^{-1}\left(N^T\right)^{-1}(-M) \\
& =M^2 N\left(-M^{-1}\right)(-N)^{-1}(-M) \\
& =-M^2 N M^{-1} N^{-1} M \\
& =-M \cdot(M N) M^{-1} N^{-1} M \\
& =-M(N M) M^{-1} N^{-1} M \\
& =-M N\left(N M^{-1}\right) N^{-1} M \\
& =-M\left(N N^{-1}\right) M=-M^2
\end{aligned}
$$
Note Here, non-singular word should not be used, since there is no non-singular $3 \times 3$ skew-symmetric matrix.

</details>

---

### Q5. JEE Advanced 2010 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

<strong>Paragraph:</strong>
Let $p$ be an odd prime number and $T_p$ be the following set of $2 \times 2$ matrices
$$
T_p=\left\{A=\left[\begin{array}{ll}
a & b \\
c & a
\end{array}\right] ; a, b, c \in\{0,1,2, \ldots, p-1\}\right\}
$$<strong>Question:</strong>
The number of $A$ in $T_p$ such that $A$ is either symmetric or skew-symmetric or both, and det $(A)$ is divisible by $p$ is

**Options:**

- **(A)** $(p-1)^2$
- **(B)** $2(p-1)$
- **(C)** $(p-1)^2+1$
- **(D)** $2 p-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 p-1$**

**Detailed Solution:**

Given, $A=\left[\begin{array}{ll}a & b \\ c & a\end{array}\right]$,
$a, b, c \in\{0,1,2, \ldots, p-1\}$
If $A$ is skew-symmetric matrix, then $a=0, b=-c$
$\therefore \quad|A|=-b^2$.
Thus, $P$ divides $|A|$ only when $b=0$...(i)
Again, if $A$ is symmetric matrix, then $b=c$ and $|A|=a^2-b^2$.
Thus, $p$ divides $|A|$ if either $p$ divides $(a-b)$ or $p$ divides $(a+b)$. $p$ divides $(a-b)$, only when $a=b$ ie, $a=b \in\{0,1,2, \ldots,(p-1)\}$
ie, pchoices
$p$ divides $(a+b)$.
$\Rightarrow p$ choices, including $a=b=0$ included in (i)
$\therefore$ Total number of choices are $(p+p-1)=2 p-1$.
Hence, (c) is the correct option.

</details>

---

