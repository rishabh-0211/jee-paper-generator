# JEE Advanced Mathematics - Three Dimensional Geometry

## Topic 2: Line in Space

**Total Questions:** 10

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Let $L$ be the straight line joining the points $P(1, 2, -1)$ and $Q(2, 3, 1)$. Let $S$ be the foot of the perpendicular drawn from the point $R(4, -1, 5)$ to the line $L$. Another line passing through $R$ intersects $L$ at a point $T$ such that the point $S$ divides the line segment $PT$ internally in the ratio $|PS| : |ST| = 1 : 2$, where $|PS|$ and $|ST|$ are the lengths of the line segments $PS$ and $ST$, respectively.
Then which of the following statements is (are) TRUE ?

**Options:**

- **(A)** The orthocentre of the triangle $PRT$ is $\left(\dfrac{23}{5}, -4, \dfrac{31}{5}\right)$
- **(B)** The orthocentre of the triangle $PRT$ is $(4, 3, 5)$
- **(C)** The area of the triangle $PRT$ is $6\sqrt{5}$
- **(D)** The area of the triangle $PRT$ is $18\sqrt{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The area of the triangle $PRT$ is $18\sqrt{5}$**

**Detailed Solution:**

The direction ratios of line $L$ passing through $P(1, 2, -1)$ and $Q(2, 3, 1)$ are $(2-1, 3-2, 1-(-1)) = (1, 1, 2)$.

The equation of line $L$ is $\dfrac{x-1}{1} = \dfrac{y-2}{1} = \dfrac{z+1}{2} = \lambda$.

Any point on $L$ can be written as $S(\lambda+1, \lambda+2, 2\lambda-1)$.

Since $S$ is the foot of the perpendicular from $R(4, -1, 5)$ to $L$, the direction ratios of $RS$ are $(\lambda-3, \lambda+3, 2\lambda-6)$.

As $RS \perp L$, the dot product of their direction ratios is zero:

$1(\lambda-3) + 1(\lambda+3) + 2(2\lambda-6) = 0$

$6\lambda - 12 = 0 \Rightarrow \lambda = 2$

Thus, the coordinates of $S$ are $(3, 4, 3)$.

The length of $PS$ is $\sqrt{(3-1)^2 + (4-2)^2 + (3-(-1))^2} = \sqrt{4+4+16} = 2\sqrt{6}$.

The length of the altitude $RS$ is $\sqrt{(3-4)^2 + (4-(-1))^2 + (3-5)^2} = \sqrt{1+25+4} = \sqrt{30}$.

Since $S$ divides $PT$ internally in the ratio $1:2$, we have:

$S = \dfrac{T + 2P}{3} \Rightarrow T = 3S - 2P$

$T = 3(3, 4, 3) - 2(1, 2, -1) = (7, 8, 11)$

The length of the base $PT$ is $3|PS| = 6\sqrt{6}$.

The area of $\triangle PRT$ is $\dfrac{1}{2} \times |PT| \times |RS| = \dfrac{1}{2} \times 6\sqrt{6} \times \sqrt{30} = 18\sqrt{5}$.

The orthocentre $H$ lies on the altitude $RS$. The line $RS$ passes through $S(3, 4, 3)$ and has direction ratios proportional to $R-S = (1, -5, 2)$.

Let the coordinates of $H$ be $(3+t, 4-5t, 3+2t)$.

Since $H$ is the orthocentre, $PH \perp RT$.

The direction ratios of $RT$ are $(7-4, 8-(-1), 11-5) = (3, 9, 6)$, which is proportional to $(1, 3, 2)$.

The direction ratios of $PH$ are $(3+t-1, 4-5t-2, 3+2t-(-1)) = (t+2, 2-5t, 2t+4)$.

Taking the dot product of $PH$ and $RT$:

$1(t+2) + 3(2-5t) + 2(2t+4) = 0$

$t + 2 + 6 - 15t + 4t + 8 = 0$

$16 - 10t = 0 \Rightarrow t = \dfrac{8}{5}$

Substituting $t = \dfrac{8}{5}$ into the coordinates of $H$, we get:

$H = \left(3 + \dfrac{8}{5}, 4 - 5\left(\dfrac{8}{5}\right), 3 + 2\left(\dfrac{8}{5}\right)\right) = \left(\dfrac{23}{5}, -4, \dfrac{31}{5}\right)$

Answer: The orthocentre of the triangle $PRT$ is $\left(\dfrac{23}{5}, -4, \dfrac{31}{5}\right)$; The area of the triangle $PRT$ is $18\sqrt{5}$

</details>

---

### Q2. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\gamma \in \mathbb{R}$ be such that the lines $\mathrm{L}_1: \frac{x+11}{1}=\frac{\mathrm{y}+21}{2}=\frac{\mathrm{z}+29}{3}$ and $L_2: \frac{x+16}{3}=\frac{y+11}{2}=\frac{z+4}{\gamma}$ intersect. Let $\mathrm{R}_1$ be the point of intersection of $\mathrm{L}_1$ and $\mathrm{L}_2$. Let $\mathrm{O}=(0,0,0)$, and $\hat{\mathrm{n}}$ denote a unit normal vector to the plane containing both the lines $\mathrm{L}_1$ and $\mathrm{L}_2$.
Match each entry in List-I to the correct entry in List-II.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/tSIfQmaG02M7mTsqTk7o7erkFcFnvVyY3a7VDxrUb6A.original.fullsize.png"/>
 The correct option is

**Options:**

- **(A)** $(\mathrm{P}) \rightarrow(3) \quad(\mathrm{Q}) \rightarrow(4) \quad(\mathrm{R}) \rightarrow(1) \quad(\mathrm{S}) \rightarrow(2)$
- **(B)** $(\mathrm{P}) \rightarrow(5) \quad(\mathrm{Q}) \rightarrow(4) \quad(\mathrm{R}) \rightarrow(1) \quad(\mathrm{S}) \rightarrow(2)$
- **(C)** $(\mathrm{P}) \rightarrow(3) \quad(\mathrm{Q}) \rightarrow(4) \quad(\mathrm{R}) \rightarrow(1) \quad(\mathrm{S}) \rightarrow(5)$
- **(D)** $(\mathrm{P}) \rightarrow(3) \quad(\mathrm{Q}) \rightarrow(1) \quad(\mathrm{R}) \rightarrow(4) \quad(\mathrm{S}) \rightarrow(5)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\mathrm{P}) \rightarrow(3) \quad(\mathrm{Q}) \rightarrow(4) \quad(\mathrm{R}) \rightarrow(1) \quad(\mathrm{S}) \rightarrow(5)$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{L}_1: \frac{\mathrm{x}+11}{1}=\frac{\mathrm{y}+21}{2}=\frac{\mathrm{z}+29}{3}=\mathrm{a} \\ & \mathrm{L}_2: \frac{\mathrm{x}+16}{3}=\frac{\mathrm{y}+11}{2}=\frac{\mathrm{z}+4}{\gamma}=\mathrm{b}\end{aligned}$
$\begin{aligned} & x=a-11=3 b-16 \Rightarrow a-3 b=-5...(1) \\ & y=2 a-21=2 b-11 \Rightarrow 2 a-2 b=10...(2) \\ & z=3 a-29=b r-4 \Rightarrow 3 a-b \gamma=25...(3)\end{aligned}$
from (1) & (2)
$\mathrm{a}=10, \mathrm{~b}=5$
Now from (3)
$3(10)-5 \gamma=25 \quad \therefore \gamma=1$
$\begin{aligned} & \mathrm{R}_1 \equiv(-1,-1,1) \\ & \mathrm{OR}_1=-\hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{n}}=\left|\begin{array}{lrr}\mathrm{i} & \mathrm{j} & \mathrm{k} \\ 1 & 2 & 3 \\ 3 & 2 & 1\end{array}\right|=-4 \hat{\mathrm{i}}-(-8) \hat{\mathrm{j}}-4 \hat{\mathrm{k}} \\ & \overrightarrow{\mathrm{n}}=-4 \hat{\mathrm{i}}+8 \hat{\mathrm{j}}+4 \hat{\mathrm{k}}=-4(\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}}) \\ & \hat{\mathrm{n}}= \pm \frac{4(\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}})}{4 \sqrt{6}}= \pm \frac{(\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}})}{\sqrt{6}} \\ & \overrightarrow{\mathrm{OR}}_1 \cdot \hat{\mathrm{n}}= \pm(-\hat{\mathrm{i}}-\hat{\mathrm{j}}+\hat{\mathrm{k}})\left(\frac{\hat{\mathrm{i}}-2 \hat{\mathrm{j}}+\hat{\mathrm{k}}}{\sqrt{6}}\right)= \pm \frac{2}{\sqrt{6}}= \pm \sqrt{\frac{4}{6}}= \pm \sqrt{\frac{2}{3}}\end{aligned}$

</details>

---

### Q3. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> be the cube with the set of vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub></mrow></mfenced><mo>&#8712;</mo><msup><mi mathvariant="normal">&#8477;</mi><mn>3</mn></msup><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> be the set of all twelve lines containing the diagonals of the six faces of the cube <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all four lines containing the main diagonals of the cube <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>; for instance, the line passing through the vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math> is in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>. For lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>2</mn></msub></math>, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced><mrow><msub><mi>&#8467;</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow></mfenced></math> denote the shortest distance between them. Then the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced><mrow><msub><mi>&#8467;</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow></mfenced></math>, as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>1</mn></msub></math> varies over <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>2</mn></msub></math> varies over <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>8</mn></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>12</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Plotting the diagram of cube we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/d3959b9c-b97b-44bd-b5eb-ac81b7d4b1b3.png" style="width: 300px; height: 252px;" /></p><p>Now equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>D</mi></math> line will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mn>0</mn><mo>&#8594;</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>And equation of diagonal <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>E</mi></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>r</mi><mo>&#8594;</mo></mover><mn>1</mn></msub><mo>=</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math></p><p>Now finding the shortest distance between line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>D</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>B</mi><mi>E</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>.</mo><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mfenced><mrow><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>0</mn></mrow></mfenced><mo>&#183;</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></mrow><mrow><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>0</mn><mn>2</mn></msup></msqrt><mo>&#183;</mo><msqrt><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>.</mo><mi>D</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mover><mi>j</mi><mo>^</mo></mover><mo>&#183;</mo><mfenced><mrow><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow><msqrt><mn>6</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac></math></p><p>Now in other case shortest distance will be zero.</p></blockquote>

</details>

---

### Q4. JEE Advanced 2020 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><mrow><msub><mi>L</mi><mn>1</mn></msub></mrow></math> and <math><mrow><msub><mi>L</mi><mn>2</mn></msub></mrow></math> be the following straight lines.
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>&#8722;</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow><mrow><mo>&#8722;</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>&#8722;</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math>
Suppose the straight line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mi>&#945;</mi></mrow><mi>l</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>&#8722;</mo><mn>1</mn></mrow><mi>m</mi></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>&#8722;</mo><mi>&#947;</mi></mrow><mrow><mo>&#8722;</mo><mn>2</mn></mrow></mfrac></math> lies in the plane containing <math><mrow><msub><mi>L</mi><mn>1</mn></msub></mrow></math> and <math><mrow><msub><mi>L</mi><mn>2</mn></msub></mrow></math>, and passes through the point of intersection of <math><mrow><msub><mi>L</mi><mn>1</mn></msub></mrow></math> and <math><mrow><msub><mi>L</mi><mn>2</mn></msub></mrow></math>. If the line <math><mi>L</mi></math> bisects the acute angle between the lines <math><mrow><msub><mi>L</mi><mn>1</mn></msub></mrow></math> and <math><mrow><msub><mi>L</mi><mn>2</mn></msub></mrow></math>, then which of the following statements is/are TRUE?

**Options:**

- **(A)** <math><mrow><mi>&#945;</mi><mo>&#8722;</mo><mi>&#947;</mi><mo>=</mo><mn>3</mn></mrow></math>
- **(B)** <math><mrow><mi>l</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>2</mn></mrow></math>
- **(C)** <math><mrow><mi>&#945;</mi><mo>&#8722;</mo><mi>&#947;</mi><mo>=</mo><mn>1</mn></mrow></math>
- **(D)** <math><mrow><mi>l</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>0</mn></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mrow><mi>l</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>2</mn></mrow></math>**

**Detailed Solution:**

<p>Given the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>&#8722;</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>&#8722;</mo><mn>1</mn></mrow><mn>1</mn></mfrac></math>.</p><p>From the given lines, we can say that both the lines pass through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>.</p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover></math> be the direction vector of line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>=</mo><mi>i</mi><mo>-</mo><mi>j</mi><mo>+</mo><mn>3</mn><mi>k</mi></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover></math> be the direction vector of line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mn>3</mn><mi>i</mi><mo>-</mo><mi>j</mi><mo>+</mo><mi>k</mi></math>.</p><p>We also know that the angle bisectors lie in the direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mfenced><mrow><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>-</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></mrow></mfenced></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>.</mo><mover><mi>b</mi><mo>&#8594;</mo></mover><mo>=</mo><mfenced><mrow><mn>1</mn><mo>&#215;</mo><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>&#215;</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mo>&#215;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>1</mn><mo>&#62;</mo><mn>0</mn></math>.</p><p>So, direction ratios of the acute angle bisector between two lines will be in the direction of <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>a</mi><mo>&#8594;</mo></mover><mo>+</mo><mover><mi>b</mi><mo>&#8594;</mo></mover></math> i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>&#8722;</mo><mn>2</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mo>&#8722;</mo><mn>2</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math>.</p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>:</mo><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mi>&#945;</mi></mrow><mi>l</mi></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>&#8722;</mo><mn>1</mn></mrow><mi>m</mi></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>&#8722;</mo><mi>&#947;</mi></mrow><mrow><mo>&#8722;</mo><mn>2</mn></mrow></mfrac></math> is the acute angle bisector between the lines <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>L</mi><mn>2</mn></msub></math>.</p><p>So, by comparing the direction ratios, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>2</mn></math></p><p>So, equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>&#8722;</mo><mi>&#945;</mi></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mo>&#8722;</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>&#8722;</mo><mi>&#947;</mi></mrow><mrow><mo>&#8722;</mo><mn>2</mn></mrow></mfrac></math>.</p><p>Given that the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>.</p><p>Putting the point in line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mi>&#945;</mi></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mn>0</mn><mo>&#8722;</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mi>&#947;</mi></mrow><mrow><mo>&#8722;</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#8722;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mi>&#947;</mi></mrow><mrow><mo>&#8722;</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#8722;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mrow><mn>1</mn><mo>&#8722;</mo><mi>&#947;</mi></mrow><mrow><mo>&#8722;</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>&#8722;</mo><mi>&#947;</mi><mo>=</mo><mn>3</mn></math></p><p>So, options <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>B</mi></mfenced></math> are correct.</p>

</details>

---

### Q5. JEE Advanced 2019 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Three lines
<math><msub><mrow><mi>L</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>:</mo><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>,</mo><mi>&#160;</mi><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math>
<math><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>:</mo><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>,</mo><mi>&#160;</mi><mi>&#956;</mi><mo>&#8712;</mo><mi>R</mi></math> and
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>3</mn></msub><mo>:</mo><mi>&#160;</mi><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#957;</mi><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mi>&#160;</mi><mi>&#957;</mi><mo>&#8712;</mo><mi>R</mi></math>
are given. For which point(s) <math><mi>Q</mi></math> and <math><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub></math> can we find a point <math><mi>P</mi></math> on <math><msub><mrow><mi>L</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and a point <math><mi>R</mi></math> on <math><msub><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msub></math> so that <math><mi>P</mi><mo>,</mo><mi>&#160;</mi><mi>Q</mi></math> and <math><mi>R</mi></math> are collinear?

**Options:**

- **(A)** <math><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math>
- **(B)** <math><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math>
- **(C)** <math><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math>
- **(D)** <math><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover></math>**

**Detailed Solution:**

As given
<math><msub><mrow><mi>L</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#8658;</mo><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>&#955;</mi><mi>i</mi><mo>,</mo><mi>&#160;</mi><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math>
<math><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#8658;</mo><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>k</mi><mo>+</mo><mi>&#956;</mi><mi>j</mi><mo>,</mo><mi>&#160;</mi><mi>&#956;</mi><mo>&#8712;</mo><mi>R</mi></math>
and <math><msub><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8658;</mo><mover accent="true"><mrow><mi>r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi>i</mi><mo>+</mo><mi>j</mi><mo>+</mo><mi>&#957;</mi><mi>k</mi><mo>,</mo><mi>&#160;</mi><mi>&#957;</mi><mo>&#8712;</mo><mi>R</mi></math>
Let point <math><mi>P</mi><mfenced separators="|"><mrow><mi>&#955;</mi><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mi>Q</mi><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#956;</mi><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math> and <math><mi>R</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>&#957;</mi></mrow></mfenced></math>
and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mi>&#955;</mi><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#956;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover><mo>,</mo><mo>&#160;</mo><mover><mrow><mi>P</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>&#955;</mi></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mi>&#957;</mi><mover><mi>k</mi><mo>^</mo></mover></math>
as <math><mi>P</mi><mo>,</mo><mi>&#160;</mi><mi>Q</mi></math> and <math><mi>R</mi></math> are co-linear
<math><mo>&#8658;</mo><mover accent="true"><mrow><mi>P</mi><mi>Q</mi></mrow><mo>&#8594;</mo></mover></math> is parallel to <math><mover accent="true"><mrow><mi>P</mi><mi>R</mi></mrow><mo>&#8594;</mo></mover></math>
<math><mo>&#8658;</mo><mo>-</mo><mfrac><mrow><mi>&#955;</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>&#955;</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#956;</mi></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>&#957;</mi></mrow></mfrac></math>
<math><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mrow><mi>&#956;</mi></mrow><mrow><mi>&#956;</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math> and <math><mi>&#957;</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>&#956;</mi></mrow></mfrac></math>
hence <math><mtable><mtr><mtd><mi>&#956;</mi><mo>&#8800;</mo><mn>0</mn></mtd><mtd><mi>&#956;</mi><mo>&#8800;</mo><mn>1</mn></mtd></mtr></mtable></math>
<math><mi>Q</mi><mo>&#8800;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math> and <math><mi>Q</mi><mo>&#8800;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>&#8800;</mo><mover><mi>k</mi><mo>^</mo></mover><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi><mo>&#8800;</mo><mfenced separators="|"><mrow><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>

</details>

---

### Q6. JEE Advanced 2019 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msub></math> denotes the lines
<math><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mi mathvariant="normal">&#955;</mi><mfenced separators="|"><mrow><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mtext>&#8201;</mtext><mi mathvariant="normal">&#955;</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math> and <math><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mi mathvariant="normal">&#956;</mi><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mi mathvariant="normal">&#956;</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math>
respectively. If <math><msub><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>3</mn></mrow></msub></math> is a line which is perpendicular to both <math><msub><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msub></math> and cuts both of them, then which of the following options describe(s) <math><msub><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>3</mn></mrow></msub></math> ?

**Options:**

- **(A)** <math><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi mathvariant="normal">t</mi><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mi mathvariant="normal">t</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math>
- **(B)** <math><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>4</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>+</mo><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi mathvariant="normal">t</mi><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mtext> </mtext><mi mathvariant="normal">t</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math>
- **(C)** <math><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mi mathvariant="normal">t</mi><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mtext> </mtext><mi mathvariant="normal">t</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math>
- **(D)** <math><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>→</mo></mover><mo>=</mo><mi mathvariant="normal">t</mi><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mtext> </mtext><mi mathvariant="normal">t</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mover accent="true"><mrow><mi mathvariant="normal">r</mi></mrow><mo>→</mo></mover><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mi mathvariant="normal">t</mi><mfenced separators="|"><mrow><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">i</mi></mrow><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover accent="true"><mrow><mi mathvariant="normal">j</mi></mrow><mo>^</mo></mover><mo>-</mo><mover accent="true"><mrow><mi mathvariant="normal">k</mi></mrow><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mtext> </mtext><mi mathvariant="normal">t</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>:</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mi>&#955;</mi><mfenced separators="|"><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#955;</mi><mo>&#8712;</mo><mi>R</mi></math></p><p>Let a general point on line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub><mo>:</mo><mover><mi mathvariant="normal">r</mi><mo>&#8594;</mo></mover><mo>=</mo><mi mathvariant="normal">&#956;</mi><mfenced separators="|"><mrow><mn>2</mn><mover><mi mathvariant="normal">i</mi><mo>^</mo></mover><mo>-</mo><mover><mi mathvariant="normal">j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi mathvariant="normal">k</mi><mo>^</mo></mover></mrow></mfenced></math> 
let a general point on line <math><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced separators="|"><mrow><mn>2</mn><mi>&#956;</mi><mo>,</mo><mi>&#160;</mi><mo>-</mo><mi>&#956;</mi><mo>,</mo><mi>&#160;</mi><mn>2</mn><mi>&#956;</mi></mrow></mfenced></math>
Then  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mi>&#956;</mi><mo>+</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mi>&#956;</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mi>&#160;</mi><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mover><mi>k</mi><mo>^</mo></mover></math>
Now, <math><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math> is perpendicular to both <math><msub><mrow><mi>L</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub></math>
Hence, <math><mo>(</mo><mi>a</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mfenced separators="|"><mrow><mo>-</mo><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math> ( If <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover></math> and <math><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover></math> are perpendicular then <math><mover accent="true"><mrow><mi>a</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mover accent="true"><mrow><mi>b</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mn>0</mn></math> )
&amp; <math><mo>(</mo><mi>b</mi><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mfenced separators="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Using 
<math><mo>(</mo><mi>a</mi><mo>)</mo></math> <math><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mfenced separators="|"><mrow><mo>-</mo><mi>i</mi><mo>+</mo><mn>2</mn><mi>j</mi><mo>+</mo><mn>2</mn><mi>k</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>&#956;</mi><mo>+</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mi>&#956;</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mfenced separators="|"><mn>2</mn></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mn>2</mn><mo>=</mo><mn>0</mn></math>
<math><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mi>&#955;</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>4</mn><mi>&#956;</mi><mo>+</mo><mn>4</mn><mi>&#956;</mi><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math>
<math><mn>9</mn><mi>&#955;</mi><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>
From <math><mo>(</mo><mi>b</mi><mo>)</mo></math> we have      <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>&#8901;</mo><mfenced separators="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>&#956;</mi><mo>+</mo><mi>&#955;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mn>2</mn></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mi>&#956;</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>&#956;</mi><mo>-</mo><mn>2</mn><mi>&#955;</mi></mrow></mfenced><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#956;</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>-</mo><mn>2</mn><mo>+</mo><mi>&#956;</mi><mo>+</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>4</mn><mi>&#956;</mi><mo>-</mo><mn>4</mn><mi>&#955;</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>&#956;</mi><mo>=</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math>
Using value of <math><mi>&#955;</mi><mtext>&#8201;</mtext></math> and <math><mtext>&#8201;</mtext><mi>&#956;</mi><mo>&#8658;</mo><mi>A</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfenced><mtext>&#8201;</mtext></math> and <math><mtext>&#8201;</mtext><mi>B</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>,</mo><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mfenced><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></math>
Now, using point <math><mi>A</mi></math> and <math><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math>
Equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>8</mn><mn>9</mn></mfrac><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>&#947;</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mfenced separators="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced></mrow></mfenced></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>B</mi><mo>)</mo></math> :
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mfenced separators="|"><mrow><mn>4</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>t</mi><mfenced separators="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mtext>&#8201;</mtext><mi>t</mi><mo>&#8712;</mo><mi>&#160;</mi><mi>R</mi></math>
Using point <math><mi>B</mi></math> and <math><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#8594;</mo></mover></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>C</mi><mo>)</mo></math> :
Equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mfenced separators="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>-</mo><mover><mi>j</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>t</mi><mfenced separators="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>t</mi><mo>&#8712;</mo><mi>R</mi></math>
Using midpoint of <math><mi>A</mi></math> and <math><mi>B</mi></math> , <math><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>A</mi><mo>)</mo></math> :
<math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced separators="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>+</mo><mi>t</mi><mfenced separators="|"><mrow><mn>2</mn><mover><mi>i</mi><mo>^</mo></mover><mo>+</mo><mn>2</mn><mover><mi>j</mi><mo>^</mo></mover><mo>-</mo><mover><mi>k</mi><mo>^</mo></mover></mrow></mfenced><mo>,</mo><mtext>&#8201;</mtext><mi>t</mi><mo>&#8712;</mo><mi>R</mi></math></p>

</details>

---

### Q7. JEE Advanced 2014 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `1`

From a point <math><mi>P</mi><mfenced separators="|"><mrow><mi>&#955;</mi><mo>,</mo><mi>&#160;</mi><mi>&#955;</mi><mo>,</mo><mi>&#160;</mi><mi>&#955;</mi></mrow></mfenced><mo>,</mo></math> perpendiculars PQ and PR are drawn respectively on the lines <math><mi>y</mi><mo>=</mo><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>z</mi><mo>=</mo><mn>1</mn></math> and <math><mi>y</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>z</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>1</mn></math> . If P is such that <math><mi>&#8736;</mi><mi>Q</mi><mi>P</mi><mi>R</mi></math> is a right angle, then the possible value (s) of <math><mi>&#955;</mi></math> is (are)

**Options:**

- **(A)** <math><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mo>-</mo><mn>1</mn></math>
- **(D)** <math><mo>-</mo><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

Line 1 :  <math><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>0</mn></mrow></mfrac><mo>-</mo><mi>r</mi><mo>,</mo><mi> </mi><mi>Q</mi><mfenced separators="|"><mrow><mi>r</mi><mo>,</mo><mi> </mi><mi>r</mi><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math> 
Line 2 :  <math><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>z</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>0</mn></mrow></mfrac><mo>=</mo><mi>k</mi><mo>,</mo><mi> </mi><mi> </mi><mi>R</mi><mfenced separators="|"><mrow><mi>k</mi><mo>,</mo><mi> </mi><mo>-</mo><mi>k</mi><mo>,</mo><mi> </mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> 
 <math><mover accent="true"><mrow><mi>P</mi><mi>Q</mi></mrow><mo>→</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mi> </mi><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mi> </mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi> </mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> 
And    <math><mi>λ</mi><mo>-</mo><mi>r</mi><mo>+</mo><mi>λ</mi><mo>-</mo><mi>r</mi><mo>=</mo><mn>0</mn></math>  as  <math><mover accent="true"><mrow><mi>P</mi><mi>Q</mi></mrow><mo>→</mo></mover></math>  is  <math><mo>⊥</mo></math>  to  <math><msub><mrow><mi>L</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
 <math><mo>⇒</mo></math>      <math><mn>2</mn><mi>λ</mi><mo>=</mo><mn>2</mn><mi>r</mi><mi> </mi><mo>⇒</mo><mi> </mi><mi> </mi><mi>λ</mi><mo>=</mo><mi>r</mi></math> 
 <math><mover accent="true"><mrow><mi>P</mi><mi>R</mi></mrow><mo>→</mo></mover><mo>=</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>-</mo><mi>k</mi></mrow></mfenced><mover accent="true"><mrow><mi>i</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mi> </mi><mover accent="true"><mrow><mi>j</mi></mrow><mo>^</mo></mover><mo>+</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi> </mi><mover accent="true"><mrow><mi>k</mi></mrow><mo>^</mo></mover></math> 
And   <math><mi>λ</mi><mo>-</mo><mi>k</mi><mo>-</mo><mi>λ</mi><mo>-</mo><mi>k</mi><mo>=</mo><mn>0</mn></math>  as  <math><mover accent="true"><mrow><mi>P</mi><mi>R</mi></mrow><mo>→</mo></mover></math>  is  <math><mo>⊥</mo></math>  to  <math><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub></math> 
 <math><mo>⇒</mo></math>      <math><mi>k</mi><mo>=</mo><mn>0</mn></math> 
So   <math><mi>P</mi><mi>Q</mi><mo>⊥</mo><mi>P</mi><mi>R</mi></math> 
 <math><mfenced separators="|"><mrow><mi>λ</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mi>λ</mi><mo>-</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mi>λ</mi><mo>+</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mi>λ</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mi>λ</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo></math>      <math><mi>λ</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mo>-</mo><mn>1</mn></math> 
For   <math><mi>λ</mi><mo>=</mo><mn>1</mn></math>  as point P and Q coincide
 <math><mo>⇒</mo></math>      <math><mi>λ</mi><mo>=</mo><mi> </mi><mo>-</mo><mn>1</mn><mo>.</mo></math>

</details>

---

### Q8. JEE Advanced 2013 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `1`

Two lines <math> <mrow> <msub> <mtext>L</mtext> <mn>1</mn> </msub> <mtext>&#160;:&#160;</mtext> <mtext>x</mtext> <mo>=</mo> <mn>5</mn> <mtext>,</mtext> <mspace width="0.5em"></mspace> <mfrac> <mrow> <mtext>y</mtext> </mrow> <mrow> <mn>3</mn> <mo>-</mo> <mi>&#945;</mi> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mtext>z</mtext> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> </mrow> </math> and <math> <mrow> <msub> <mtext>L</mtext> <mn>2</mn> </msub> <mtext>&#160;:&#160;</mtext> <mtext>x</mtext> <mo>=</mo> <mi>&#945;</mi> <mtext>,</mtext> <mspace width="0.5em"></mspace> <mfrac> <mrow> <mtext>y</mtext> </mrow> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mtext>z</mtext> </mrow> <mrow> <mn>2</mn> <mo>-</mo> <mi>&#945;</mi> </mrow> </mfrac> </mrow> </math> are coplanar. Then <math> <mrow> <mi>&#945;</mi> </mrow> </math> can take value(s)

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

<math> <mrow> <mfrac> <mrow> <mtext>x</mtext> <mo>-</mo> <mn>5</mn> </mrow> <mrow> <mn>0</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mo>-</mo> <mtext>y</mtext> </mrow> <mrow> <mi>&alpha;</mi> <mo>-</mo> <mn>3</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mtext>z</mtext> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mtext>x</mtext> <mo>-</mo> <mi>&alpha;</mi> </mrow> <mrow> <mn>0</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mtext>y</mtext> </mrow> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mtext>z</mtext> </mrow> <mrow> <mn>2</mn> <mo>-</mo> <mi>&alpha;</mi> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mfenced close="|" open="|" separators=","> <mrow> <mtable> <mtr> <mtd> <mn>5</mn> <mo>-</mo> <mi>&alpha;</mi> </mtd> <mtd> <mn>0</mn> </mtd> <mtd> <mn>0</mn> </mtd> </mtr> <mtr> <mtd> <mn>0</mn> </mtd> <mtd> <mn>3</mn> <mo>-</mo> <mi>&alpha;</mi> </mtd> <mtd> <mo>-</mo> <mn>2</mn> </mtd> </mtr> <mtr> <mtd> <mn>0</mn> </mtd> <mtd> <mo>-</mo> <mn>1</mn> </mtd> <mtd> <mn>2</mn> <mo>-</mo> <mi>&alpha;</mi> </mtd> </mtr> </mtable> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math>
<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>5</mn> <mo>-</mo> <mi>&alpha;</mi> </mrow> </mfenced>  <mfenced close=")" open="(" separators=","> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>-</mo> <mi>&alpha;</mi> </mrow> </mfenced>  <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> <mo>-</mo> <mi>&alpha;</mi> </mrow> </mfenced> <mo>-</mo> <mn>2</mn> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math>
<math><mrow>  <mfenced open="(" close=")" separators=",">    <mrow>      <mi>&alpha;</mi>      <mo>-</mo>      <mn>5</mn>    </mrow>  </mfenced></mrow></math> <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>&alpha;</mi> <mn>2</mn> </msup> <mo>-</mo> <mn>5</mn> <mi>&alpha;</mi> <mo>+</mo> <mn>6</mn> <mo>-</mo> <mn>2</mn> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math>
<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mi>&alpha;</mi> <mo>-</mo> <mn>5</mn> </mrow> </mfenced>  <mfenced close=")" open="(" separators=","> <mrow> <msup> <mi>&alpha;</mi> <mn>2</mn> </msup> <mo>-</mo> <mn>5</mn> <mi>&alpha;</mi> <mo>+</mo> <mn>4</mn> </mrow> </mfenced> <mo>=</mo> <mn>0</mn> </mrow> </math>
<math> <mrow> <mi>&alpha;</mi> <mo>=</mo> <mn>1</mn> <mtext>,</mtext> <mn> 4</mn> <mtext>, </mtext> <mn>5</mn> </mrow> </math>

</details>

---

### Q9. JEE Advanced 2013 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

A line <math> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>&#8289;</mo> </mrow> </math> passing through the origin is perpendicular to the lines
<math> <mrow> <msub> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>&#8289;</mo> </mrow> <mn>1</mn> </msub> <mtext>&#160;:&#160;</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>+</mo> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>i</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>1</mn> <mo>+</mo><mn>2</mn> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>j</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>4</mn> <mo>+</mo> <mn>2</mn> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>k</mtext> <mo>^</mo> </mover> <mtext>,&#160;</mtext> <mo>-</mo> <mo>&#8734;</mo> <mo>&#60;</mo> <mtext>t</mtext> <mo>&#60;</mo> <mo>&#8734;</mo> </mrow> </math>
<math> <mrow> <msub> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>&#8289;</mo> </mrow> <mn>2</mn> </msub> <mtext>&#160;:&#160;</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>+</mo> <mn>2</mn> <mtext>s</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>i</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>+</mo> <mn>2</mn> <mtext>s</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>j</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> <mo>+</mo> <mtext>s</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>k</mtext> <mo>^</mo> </mover> <mtext>,&#160;</mtext> <mo>-</mo> <mo>&#8734;</mo> <mo>&#60;</mo> <mtext>s</mtext> <mo>&#60;</mo> <mo>&#8734;</mo> </mrow> </math>
Then, the coordinate(s) of the point(s) on <math> <mrow> <msub> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>&#8289;</mo> </mrow> <mn>2</mn> </msub> </mrow> </math> at a distance of <math> <mrow> <msqrt> <mn>1</mn> <mn>7</mn> </msqrt> </mrow> </math>  from the point of intersection of <math> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>&#8289;</mo> </mrow> </math> and <math> <mrow> <msub> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>&#8289;</mo> </mrow> <mn>1</mn> </msub> </mrow> </math> is (are)

**Options:**

- **(A)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mtext>, </mtext> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mtext>, </mtext> <mfrac> <mrow> <mn>5</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
- **(B)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>1</mn> <mtext>, </mtext> <mo>-</mo> <mn>1</mn> <mtext>, </mtext> <mn>0</mn> </mrow> </mfenced> </mrow> </math>
- **(C)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mtext>,</mtext> <mn>1</mn> <mtext>,</mtext> <mn>1</mn> </mrow> </mfenced> </mrow> </math>
- **(D)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mtext>,</mtext> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mtext>,</mtext> <mfrac> <mrow> <mn>8</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mtext>,</mtext> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mtext>,</mtext> <mfrac> <mrow> <mn>8</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>**

**Detailed Solution:**

<p>Given 
<math> <mrow> <msub> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>⁡</mo> </mrow> <mn>1</mn> </msub> <mtext> : </mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>+</mo> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>i</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>1</mn> <mo>+</mo><mn>2</mn> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>j</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>4</mn> <mo>+</mo> <mn>2</mn> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>k</mtext> <mo>^</mo> </mover> <mtext>, </mtext> <mo>-</mo> <mo>∞</mo> <mo><</mo> <mtext>t</mtext> <mo><</mo> <mo>∞</mo> </mrow> </math>
<math> <mrow> <msub> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>l</mi><mo>⁡</mo> </mrow> <mn>2</mn> </msub> <mtext> : </mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>+</mo> <mn>2</mn> <mtext>s</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>i</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>+</mo> <mn>2</mn> <mtext>s</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>j</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> <mo>+</mo> <mtext>s</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>k</mtext> <mo>^</mo> </mover> <mtext>, </mtext> <mo>-</mo> <mo>∞</mo> <mo><</mo> <mtext>s</mtext> <mo><</mo> <mo>∞</mo> </mrow> </math>
Direction ratios of line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Let equation of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>l : </mtext><mfrac><mrow><mtext>x</mtext><mo>-</mo><mn>0</mn></mrow><mtext>a</mtext></mfrac><mo>=</mo><mfrac><mrow><mtext>y</mtext><mo>-</mo><mn>0</mn></mrow><mtext>b</mtext></mfrac><mo>=</mo><mfrac><mrow><mtext>z</mtext><mo>-</mo><mn>0</mn></mrow><mtext>c</mtext></mfrac><mo>=</mo><mtext>k</mtext></math>
This line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is perpendicular to given line <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math>.
Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>a</mtext><mo>+</mo><mn>2</mn><mtext>b</mtext><mo>+</mo><mn>2</mn><mtext>c</mtext><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced><mo> </mo><mfenced><mrow><mi>l</mi><mo>⊥</mo><msub><mi>l</mi><mn>1</mn></msub></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mtext>a</mtext><mo>+</mo><mn>2</mn><mtext>b</mtext><mo>+</mo><mtext>c</mtext><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mo> </mo><mfenced><mrow><mi>l</mi><mo>⊥</mo><msub><mi>l</mi><mn>2</mn></msub></mrow></mfenced></math></p><p>Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mo>&</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>
<math> <mrow> <mfrac> <mrow> <mtext>a</mtext> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mtext>b</mtext> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mtext>c</mtext> </mrow> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM00012569_AnsExp_1.jpg"/>
Hence equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mtext>x</mtext><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mtext>y</mtext><mn>3</mn></mfrac><mo>=</mo><mfrac><mtext>z</mtext><mrow><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><munder><munder><msub><mtext>k</mtext><mn>1</mn></msub><mo>↓</mo></munder><msub><mtext>for l</mtext><mn>1</mn></msub></munder><mtext>, </mtext><munder><munder><msub><mtext>k</mtext><mn>2</mn></msub><mo>↓</mo></munder><msub><mtext>for l</mtext><mn>2</mn></msub></munder></math>
Now <math> <mrow> <mtext>A</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>2</mn> <msub> <mtext>k</mtext> <mn>1</mn> </msub> <mtext>, </mtext> <mn>3</mn> <msub> <mtext>k</mtext> <mn>1</mn> </msub> <mtext>, </mtext> <mo>-</mo> <mn>2</mn> <msub> <mtext>k</mtext> <mn>1</mn> </msub> </mrow> </mfenced> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mspace width="0.5em"></mspace> <mtext>B</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>2</mn> <msub> <mtext>k</mtext> <mn>2</mn> </msub> <mtext>, </mtext> <mn>3</mn> <msub> <mtext>k</mtext> <mn>2</mn> </msub> <mtext>, </mtext> <mo>-</mo> <mn>2</mn> <msub> <mtext>k</mtext> <mn>2</mn> </msub> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <mo>-</mo> <mn>2</mn> <msub> <mtext>k</mtext> <mn>1</mn> </msub> <mover accent="true"> <mtext>i</mtext> <mo>^</mo> </mover> <mo>+</mo> <mn>3</mn> <msub> <mtext>k</mtext> <mn>1</mn> </msub> <mover accent="true"> <mtext>j</mtext> <mo>^</mo> </mover> <mo>-</mo> <mn>2</mn> <msub> <mtext>k</mtext> <mn>1</mn> </msub> <mover accent="true"> <mtext>k</mtext> <mo>^</mo> </mover> <mo>=</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mo>+</mo> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>i</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>1</mn> <mo>+</mo> <mn>2</mn> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>j</mtext> <mo>^</mo> </mover> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mn>4</mn> <mo>+</mo> <mn>2</mn> <mtext>t</mtext> </mrow> </mfenced> <mover accent="true"> <mtext>k</mtext> <mo>^</mo> </mover> </mrow> </math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mn>3</mn><mo>+</mo><mtext>t</mtext><mo>=</mo><mo>-</mo><mn>2</mn><msub><mtext>k</mtext><mn>1</mn></msub></mtd><mtd><mo>…</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mtext>t</mtext><mo>=</mo><mn>3</mn><msub><mtext>k</mtext><mn>1</mn></msub></mtd><mtd><mo>…</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></mtd></mtr><mtr><mtd><mn>4</mn><mo>+</mo><mn>2</mn><mtext>t</mtext><mo>=</mo><mo>-</mo><mn>2</mn><msub><mtext>k</mtext><mn>1</mn></msub></mtd><mtd><mo>…</mo><mfenced><mi>v</mi></mfenced></mtd></mtr></mtable></math>
Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced><mo> </mo><mo>&</mo><mo> </mo><mfenced><mi>v</mi></mfenced></math> <math> <mrow> <mo>-</mo> <mn>5</mn> <mo>=</mo> <mn>5</mn> <msub> <mtext>k</mtext> <mn>1</mn> </msub> <mo>⇒</mo> <msub> <mtext>k</mtext> <mn>1</mn> </msub> <mo>=</mo> <mo>-</mo> <mn>1</mn> <mo>⇒</mo> <mtext>A</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> <mtext>,</mtext> <mo>-</mo> <mn>3</mn> <mtext>,</mtext> <mspace width="0.5em"></mspace> <mn>2</mn> </mrow> </mfenced> </mrow> </math>
Let any point on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mtext>S</mtext><mtext>, </mtext><mn>3</mn><mo>+</mo><mn>2</mn><mtext>S</mtext><mtext>, </mtext><mn>2</mn><mo>+</mo><mtext>S</mtext></mrow></mfenced><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>v</mi><mi>i</mi></mrow></mfenced></math>
According to question <math> <mrow> <msqrt> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <mn>2</mn> <mtext>S</mtext> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> <mo>+</mo> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>6</mn> <mo>+</mo> <mn>2</mn> <mtext>S</mtext> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> <mo>+</mo> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mtext>S</mtext> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> </msqrt> <mo>=</mo> <msqrt> <mn>1</mn> <mn>7</mn> </msqrt> </mrow> </math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><msup><mtext>S</mtext><mn>2</mn></msup><mo>+</mo><mn>2</mn><mn>8</mn><mtext>S</mtext><mo>+</mo><mn>3</mn><mn>7</mn><mo>=</mo><mn>1</mn><mn>7</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><msup><mtext>S</mtext><mn>2</mn></msup><mo>+</mo><mn>2</mn><mn>8</mn><mtext>S</mtext><mo>+</mo><mn>2</mn><mn>0</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><msup><mtext>S</mtext><mn>2</mn></msup><mo>+</mo><mn>1</mn><mn>8</mn><mtext>S</mtext><mo>+</mo><mn>1</mn><mn>0</mn><mtext>S</mtext><mo>+</mo><mn>2</mn><mn>0</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>9</mn><mtext>S</mtext><mfenced><mrow><mtext>S</mtext><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mn>0</mn><mfenced><mrow><mtext>S</mtext><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>⇒S</mtext><mo>=</mo><mo>-</mo><mn>2</mn><mtext>,</mtext><mspace width="0.5em"></mspace><mo>-</mo><mn>1</mn><mn>0</mn><mo>/</mo><mn>9</mn></math>
Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>v</mi><mi>i</mi></mrow></mfenced></math></p><p>The required points are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo> </mo><mo>&</mo><mo> </mo><mfenced><mrow><mfrac><mn>7</mn><mn>9</mn></mfrac><mo>,</mo><mfrac><mn>7</mn><mn>9</mn></mfrac><mo>,</mo><mfrac><mn>8</mn><mn>9</mn></mfrac></mrow></mfenced></math> </p>

</details>

---

### Q10. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
Consider the lines: $L_1: \frac{x+1}{3}=\frac{y+2}{1}=\frac{z+1}{2}, L_2: \frac{x-2}{1}=\frac{y+2}{2}=\frac{z-3}{3}$<strong>Question:</strong>
The shortest distance between $L_1$ and $L_2$ is

**Options:**

- **(A)** 0
- **(B)** $17 / \sqrt{3}$
- **(C)** $41 / 5 \sqrt{3}$
- **(D)** $17 / 5 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $17 / 5 \sqrt{3}$**

**Detailed Solution:**

The shortest distance between $L_1$ and $L_2$ is
$$
\begin{array}{r}
\left|\frac{\{(2-(-1)) \hat{\mathbf{i}}+(2-2) \hat{\mathbf{j}}+(3-(-1)) \hat{\mathbf{k}}\} \cdot(-\hat{\mathbf{i}}-7 \hat{\mathbf{j}}+5 \hat{\mathbf{k}})}{5 \sqrt{3}}\right| \\
=\left|\frac{(3 \hat{\mathbf{i}}+4 \hat{\mathbf{k}}) \cdot(-\hat{\mathbf{i}}-7 \hat{\mathbf{j}}+5 \hat{\mathbf{k}})}{5 \sqrt{3}}\right|=\frac{17}{5 \sqrt{3}}
\end{array}
$$

</details>

---

