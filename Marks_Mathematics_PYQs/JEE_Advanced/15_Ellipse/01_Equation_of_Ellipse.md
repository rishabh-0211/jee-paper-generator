# JEE Advanced Mathematics - Ellipse

## Topic 1: Equation of Ellipse

**Total Questions:** 8

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

Consider the ellipse $E$ given by $\dfrac{x^2}{18} + \dfrac{y^2}{12} = 1$. Let $H$ be the hyperbola whose eccentricity is the reciprocal of the eccentricity of $E$ and whose foci are the same as that of $E$. Let $P$ and $Q$ be the points of intersection of $H$ and the parabola $\sqrt{5}\, y = x^2$ in the first quadrant. Let $d$ be the distance between $P$ and $Q$.
If $a$ and $b$ are the integers such that $d^2 = a + b\sqrt{5}$, then the value of $a - b$ is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

For the ellipse $E: \dfrac{x^2}{18} + \dfrac{y^2}{12} = 1$, we have $a_E^2 = 18$ and $b_E^2 = 12$.

The eccentricity $e_E$ is given by:
$e_E = \sqrt{1 - \dfrac{b_E^2}{a_E^2}} = \sqrt{1 - \dfrac{12}{18}} = \dfrac{1}{\sqrt{3}}$

The foci of the ellipse $E$ are $(\pm a_E e_E, 0) = \left(\pm \sqrt{18} \times \dfrac{1}{\sqrt{3}}, 0\right) = (\pm \sqrt{6}, 0)$.

For the hyperbola $H$, the eccentricity $e_H$ is the reciprocal of $e_E$, so $e_H = \sqrt{3}$.
Since $H$ has the same foci as $E$, its foci are $(\pm \sqrt{6}, 0)$.
Let the equation of $H$ be $\dfrac{x^2}{A^2} - \dfrac{y^2}{B^2} = 1$.
The foci are $(\pm A e_H, 0)$, which gives $A \sqrt{3} = \sqrt{6} \Rightarrow A = \sqrt{2} \Rightarrow A^2 = 2$.
Also, $B^2 = A^2(e_H^2 - 1) = 2(3 - 1) = 4$.
Thus, the equation of the hyperbola $H$ is $\dfrac{x^2}{2} - \dfrac{y^2}{4} = 1$.

To find the points of intersection of $H$ and the parabola $\sqrt{5}y = x^2$, we substitute $x^2 = \sqrt{5}y$ into the equation of $H$:
$\dfrac{\sqrt{5}y}{2} - \dfrac{y^2}{4} = 1$

Multiplying by $4$, we get:
$2\sqrt{5}y - y^2 = 4 \Rightarrow y^2 - 2\sqrt{5}y + 4 = 0$

Solving for $y$ using the quadratic formula:
$y = \dfrac{2\sqrt{5} \pm \sqrt{20 - 16}}{2} = \sqrt{5} \pm 1$

Let $y_1 = \sqrt{5} - 1$ and $y_2 = \sqrt{5} + 1$. Both are positive.
The corresponding $x^2$ values are:
$x_1^2 = \sqrt{5}(\sqrt{5} - 1) = 5 - \sqrt{5}$
$x_2^2 = \sqrt{5}(\sqrt{5} + 1) = 5 + \sqrt{5}$

Since the points $P$ and $Q$ lie in the first quadrant, $x > 0$. Thus, $x_1 = \sqrt{5 - \sqrt{5}}$ and $x_2 = \sqrt{5 + \sqrt{5}}$.

The square of the distance $d$ between $P$ and $Q$ is:
$d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$

First, we evaluate $(x_2 - x_1)^2$:
$(x_2 - x_1)^2 = x_2^2 + x_1^2 - 2x_1x_2$
$x_2^2 + x_1^2 = (5 + \sqrt{5}) + (5 - \sqrt{5}) = 10$
$x_1x_2 = \sqrt{(5 - \sqrt{5})(5 + \sqrt{5})} = \sqrt{25 - 5} = \sqrt{20} = 2\sqrt{5}$
So, $(x_2 - x_1)^2 = 10 - 4\sqrt{5}$.

Next, we evaluate $(y_2 - y_1)^2$:
$(y_2 - y_1)^2 = ((\sqrt{5} + 1) - (\sqrt{5} - 1))^2 = 2^2 = 4$

Adding these together gives $d^2$:
$d^2 = 10 - 4\sqrt{5} + 4 = 14 - 4\sqrt{5}$

Comparing this with $d^2 = a + b\sqrt{5}$, we get $a = 14$ and $b = -4$.

Therefore, $a - b = 14 - (-4) = 18$.

Answer: $18$

</details>

---

### Q2. JEE Advanced 2025 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Let $P\left(x_1, y_1\right)$ and $Q\left(x_2, y_2\right)$ be two distinct points on the ellipse
$\frac{x^2}{9}+\frac{y^2}{4}=1$
such that $y_1>0$, and $y_2>0$. Let C denote the circle $x^2+y^2=9$, and $M$ be the point $(3,0)$.
Suppose the line $x=x_1$ intersects $C$ at $R$, and the line $x=x_2$ intersects $C$ at $S$, such that the $y$-coordinates of $R$ and $S$ are positive. Let $\angle R O M=\frac{\pi}{6}$ and $\angle S O M=\frac{\pi}{3}$, where $O$ denotes the origin $(0,0)$. Let $|X Y|$ denote the length of the line segment $X Y$.
Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** The equation of the line joining $P$ and $Q$ is $2 x+3 y=3(1+\sqrt{3})$
- **(B)** The equation of the line joining $P$ and $Q$ is $2 x+y=3(1+\sqrt{3})$
- **(C)** If $N_2=\left(x_2, 0\right)$, then $3\left|N_2 Q\right|=2\left|N_2 S\right|$
- **(D)** If $N_1=\left(x_1, 0\right)$, then $9\left|N_1 P\right|=4\left|N_1 R\right|$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) If $N_2=\left(x_2, 0\right)$, then $3\left|N_2 Q\right|=2\left|N_2 S\right|$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/rAeZ-9qneWj0US_G7jJak86SVvCeF1Opv2isaizY2no.original.fullsize.png">
$\begin{aligned} & \mathrm{P} \equiv\left(3 \cos 30^{\circ}, 2 \sin 30^{\circ}\right) \equiv\left(\frac{3 \sqrt{3}}{2}, 1\right) \\ & \mathrm{Q} \equiv\left(3 \cos 60^{\circ}, 2 \sin 60^{\circ}\right) \equiv\left(\frac{3}{2}, \sqrt{3}\right) \\ & \mathrm{R}\left(\frac{3 \sqrt{3}}{2}, \frac{3}{2}\right), \mathrm{S}\left(\frac{3}{2}, \frac{3 \sqrt{3}}{2}\right)\end{aligned}$
Slope of $\mathrm{PQ}=\mathrm{m}_{\mathrm{PQ}}=\frac{\sqrt{3}-1}{\frac{3}{2}-\frac{3 \sqrt{3}}{2}}=-\frac{2}{3}$
Equation of line PQ
$\mathrm{y}-\sqrt{3}=-\frac{2}{3}\left(\mathrm{x}-\frac{3}{2}\right)$
$\Rightarrow 2 x+3 y=3(\sqrt{3}+1) \quad$ option (A) is correct
Now
$\begin{aligned} & \text { if } \mathrm{N}_2=\left(\mathrm{x}_2, 0\right)=\left(\frac{3}{2}, 0\right) \\ & \left|\mathrm{N}_2 \mathrm{Q}\right|=\sqrt{3} \text { and }\left|\mathrm{N}_2 \mathrm{~S}\right|=\frac{3 \sqrt{3}}{2}\end{aligned}$
$\Rightarrow 3\left|\mathrm{~N}_2 \mathrm{Q}\right|=2\left|\mathrm{~N}_2 \mathrm{~S}\right| \quad$ option (C) is correct
Now, if $\mathrm{N}_1=\left(\mathrm{x}_1, 0\right) \Rightarrow \mathrm{N}_1=\left(\frac{3 \sqrt{3}}{2}, 0\right)$
$\Rightarrow\left|\mathrm{N}_1 \mathrm{P}\right|=1,\left|\mathrm{~N}_1 \mathrm{R}\right|=\frac{3}{2} \quad$ option (D) is incorrect

</details>

---

### Q3. JEE Advanced 2019 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Define the collections <math><mfenced close="}" open="{" separators="|"><mrow><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></math> of ellipses and <math><mfenced close="}" open="{" separators="|"><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></math> of rectangles as follows:
<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>:</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>;</mo></math>
<math><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>:</mo></math> rectangle of largest area, with sides parallel to the axes, inscribed in <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>;</mo></math>
<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow></msub><mo>:</mo></math> ellipse <math><mfrac><mrow><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msubsup><mrow><mi mathvariant="normal">a</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi mathvariant="normal">y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msubsup><mrow><mi mathvariant="normal">b</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mn>1</mn></math> of largest area inscribed in <math><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><mi mathvariant="normal">n</mi><mo>&#62;</mo><mn>1</mn><mo>;</mo></math>
<math><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow></msub><mo>:</mo></math> rectangle of largest area, with sides parallel to the axes, inscribed in <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><mi mathvariant="normal">n</mi><mo>&#62;</mo><mn>1</mn><mo>.</mo></math>
Then which of the following options is/are correct?

**Options:**

- **(A)** The eccentricities of  <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>18</mn></mrow></msub></math>  and  <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>19</mn></mrow></msub></math>  are NOT equal
- **(B)** The distance of a focus from the centre in <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>9</mn></mrow></msub></math> is <math><mfrac><mrow><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>32</mn></mrow></mfrac></math>
- **(C)** The length of latus rectum of  <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>9</mn></mrow></msub></math>  is  <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi mathvariant="normal">n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi mathvariant="normal">N</mi></mrow></munderover><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mtext>&#8201;</mtext><mi mathvariant="normal">o</mi><mi mathvariant="normal">f</mi><mtext>&#8201;</mtext><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow></msub></mrow></mfenced><mo>&#60;</mo><mn>24</mn><mo>,</mo></mrow></mrow></math> for each positive integer <math><mi mathvariant="normal">N</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi mathvariant="normal">n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi mathvariant="normal">N</mi></mrow></munderover><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mtext>&#8201;</mtext><mi mathvariant="normal">o</mi><mi mathvariant="normal">f</mi><mtext>&#8201;</mtext><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow></msub></mrow></mfenced><mo>&#60;</mo><mn>24</mn><mo>,</mo></mrow></mrow></math> for each positive integer <math><mi mathvariant="normal">N</mi></math>**

**Detailed Solution:**

<p>As given:
<math><msub><mrow><mi>E</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math> (Here <math><mi>a</mi><mo>=</mo><mn>3</mn></math> and <math><mi>b</mi><mo>=</mo><mn>2</mn></math> )
Semi major axis <math><mo>=</mo><mi>a</mi></math> and semi minor axis <math><mo>=</mo><mi>b</mi></math>
Let a vertex of <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math> be <math><mfenced separators="|"><mrow><mi>a</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi><mo>,</mo><mi>b</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></mrow></mfenced></math>
Then area of <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mi>a</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>θ</mi><mo>×</mo><mn>2</mn><mi>b</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>θ</mi></math>
<math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mi>a</mi><mi>b</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>θ</mi></math>
Maximum area of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>,</mo></math></p><p>when <math><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mn>2</mn><mi>θ</mi><mo>=</mo><mn>1</mn></math>
or, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>θ</mi><mo>=</mo><mfrac><mi>π</mi><mn>2</mn></mfrac></math>
<math><mi>θ</mi><mo>=</mo><mfrac><mrow><mi>π</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
Maximum area of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mi>a</mi><mi>b</mi></math> ....(i)
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/akloqbgqpbohzxzokfhiqtzcxhgxaiegqspfcliktkbppqtbvz.png"/>
Now, ellipse <math><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn></mrow></msub></math> will have semi major axis <math><mfrac><mrow><mi>a</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> and semi minor axis <math><mfrac><mrow><mi>b</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
<math><mo>∵</mo><mtext> </mtext><msub><mrow><mi>E</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>b</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>1</mn><mo>,</mo></math></p><p>hence maximum area of <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mi>b</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></math>
Similarly, ellipse <math><msub><mrow><mi>E</mi></mrow><mrow><mn>3</mn></mrow></msub></math> will have semi major axis <math><mfrac><mrow><mi>a</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> and semi minor axis <math><mfrac><mrow><mi>b</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
<math><msub><mrow><mi>E</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>:</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>b</mi></mrow><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>1</mn></math>
And maximum area of
<math><msub><mrow><mi>R</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mfrac><mrow><mi>a</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mi>b</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>:</mo></math>
All ellipse will have some eccentricity as the ratios of semi major axis and semi minor axis is same for all ellipse.
<math><mi>e</mi><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><msubsup><mrow><mi>b</mi></mrow><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><msubsup><mrow><mi>a</mi></mrow><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac></msqrt><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><mfrac><mrow><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></msqrt><mo>=</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math>

Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>4</mn><mo>)</mo><mo>:</mo></math>
<math><mrow><munderover><mo stretchy="true">∑</mo><mrow><mi>n</mi><mtext> </mtext><mo>=</mo><mtext> </mtext><mn>1</mn></mrow><mrow><mi>m</mi></mrow></munderover><mrow><mtext>area of rectangle</mtext></mrow></mrow><mtext> </mtext><msub><mrow><mi>R</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>…</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mi>m</mi></mrow></msub></math>
Area of <math><mi>m</mi></math> rectangle will be lesser than area of infinite
Rectangle <math><mo>⇒</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>…</mo><mo>.</mo><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mi>m</mi></mrow></msub><mo><</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><mo>…</mo><mo>.</mo><mo>.</mo><mi>∞</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mtext>area of rectangle</mtext><mo><</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>+</mo><mn>2</mn><mfenced separators="|"><mfrac><mi>a</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mfenced separators="|"><mfrac><mi>b</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>∞</mi><mo>=</mo><mn>2</mn><mi>a</mi><mi>b</mi><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mfenced separators="|"><msqrt><mn>2</mn></msqrt></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>∞</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>m</mi></munderover><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal">e</mi><mi> </mi><msub><mi>R</mi><mi>n</mi></msub><mo><</mo><mn>2</mn><mi>a</mi><mi>b</mi><mfenced close="]" open="[" separators="|"><mfrac><mtext>1</mtext><mrow><mtext>1-</mtext><mfrac><mtext>1</mtext><mtext>2</mtext></mfrac></mrow></mfrac></mfenced></math>
<math><mrow><munderover><mo stretchy="true">∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>m</mi></mrow></munderover><mrow><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal">e</mi><mi> </mi><msub><mrow><mi>R</mi></mrow><mrow><mi>n</mi></mrow></msub><mo><</mo><mn>4</mn><mi>a</mi><mi>b</mi></mrow></mrow></math>
<math><mrow><munderover><mo stretchy="true">∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>m</mi></mrow></munderover><mrow><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal">e</mi><mi> </mi><msub><mrow><mi>R</mi></mrow><mrow><mi>n</mi></mrow></msub><mo><</mo><mn>4</mn><mo>×</mo><mn>3</mn><mo>×</mo><mn>2</mn></mrow></mrow></math>
<math><mrow><munderover><mo stretchy="true">∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>m</mi></mrow></munderover><mrow><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">f</mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal">e</mi><mi> </mi><msub><mrow><mi>R</mi></mrow><mrow><mi>n</mi></mrow></msub><mo><</mo><mn>24</mn></mrow></mrow></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>)</mo><mo>:</mo></math>
Length of latus rectum of <math><msub><mrow><mi>E</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><msubsup><mrow><mi>b</mi></mrow><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><msubsup><mrow><mi>a</mi></mrow><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>a</mi><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfrac></math>
<math><mi>L</mi><mo>.</mo><mi>R</mi><mo>.</mo><mtext> </mtext><mi>o</mi><mi>f</mi><mtext> </mtext><msub><mrow><mi>E</mi></mrow><mrow><mi>g</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>a</mi><msup><mrow><mfenced separators="|"><mrow><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mrow><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><mo>×</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo><mo>:</mo></math>
Distance between focus and centre of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>9</mn></msub><mo>=</mo><msub><mi>a</mi><mn>9</mn></msub><mi>e</mi></math>
<math><mo>=</mo><mfrac><mrow><mi>a</mi></mrow><mrow><msup><mrow><mo>(</mo><msqrt><mn>2</mn></msqrt><mo>)</mo></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>×</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>16</mn></mrow></mfrac></math></p>

</details>

---

### Q4. JEE Advanced 2018 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Consider two straight lines, each of which is tangent to both the circle <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> and the parabola <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>x</mi></math> . Let these lines intersect at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>. Consider the ellipse whose center is at the origin <math><mi>O</mi><mo>(</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>)</mo></math> and whose semi-major axis is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>Q</mi></math>. If the length of the minor axis of this ellipse is <math><msqrt><mn>2</mn></msqrt></math>, then the which of the following statement(s) is (are) TRUE?

**Options:**

- **(A)** For the ellipse, the eccentricity is <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> and the length of the latus rectum is 1
- **(B)** For the ellipse, the eccentricity is  <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>  and the length of the latus rectum is  <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** The area of the region bounded by the ellipse between the lines <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> and <math><mi>x</mi><mo>=</mo><mn>1</mn></math> is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced separators="|"><mrow><mi>π</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** The area of the region bounded by the ellipse between the lines  <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>  and  <math><mi>x</mi><mo>=</mo><mn>1</mn></math>  is  <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mfenced separators="|"><mrow><mi>π</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) The area of the region bounded by the ellipse between the lines <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> and <math><mi>x</mi><mo>=</mo><mn>1</mn></math> is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><mfenced separators="|"><mrow><mi>π</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

Let equation of common tangent is \(\mathrm{y}=\mathrm{m} \mathrm{x}+\frac{1}{\mathrm{~m}}\)

\(\therefore\left|\frac{0+0+\frac{1}{\mathrm{~m}}}{\sqrt{1+\mathrm{m}^{2}}}\right|=\frac{1}{\sqrt{2}} \Rightarrow \mathrm{m}^{4}+\mathrm{m}^{2}-2=0 \Rightarrow \mathrm{m}=\pm 1\) Equation of common tangents are \(\mathrm{y}=\mathrm{x}+1\) and \(\mathrm{y}=-\mathrm{x}+1\)

point \(Q\) is \((-1,0)\)

\(\therefore\) Equation of ellipse is \(\frac{x^{2}}{1}+\frac{y^{2}}{1 / 2}=1\)

(A) \(\mathrm{e}=\sqrt{1-\frac{1}{2}}=\frac{1}{\sqrt{2}}\) and \(\mathrm{LR}=\frac{2 \mathrm{~b}^{2}}{\mathrm{a}}=1\)

(C) Area \(2 \cdot \int_{1 / \sqrt{2}}^{1} \frac{1}{\sqrt{2}} \cdot \sqrt{1-\mathrm{x}^{2}} \mathrm{dx}=\sqrt{2}\left[\frac{\mathrm{x}}{2} \sqrt{1-\mathrm{x}^{2}}+\frac{1}{2} \sin ^{-1} \mathrm{x}\right]_{1 / \sqrt{2}}^{1}\) \(=\sqrt{2}\left[\frac{\pi}{4}-\left(\frac{1}{4}+\frac{\pi}{8}\right)\right]=\sqrt{2}\left(\frac{\pi}{8}-\frac{1}{4}\right]=\frac{\pi-2}{4 \sqrt{2}}\)

Correct answers are (A) and (C).<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/oghhitiwazeanccemntdxcszwhahcxlzbyimzrhmorziuctvmm.png"/>

</details>

---

### Q5. JEE Advanced 2012 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The ellipse $E_{1}: \frac{x^{2}}{9}+\frac{y^{2}}{4}=1$ is inscribed in a rectangle $R$ whose sides are parallel to the coordinate axes. Another ellipse $E_{2}$ passing through the point $(0,4)$ circumscribes the rectangle $R$. The eccentricity of the ellipse $E_{2}$ is

**Options:**

- **(A)** $\frac{\sqrt{2}}{2}$
- **(B)** $\frac{\sqrt{3}}{2}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

As rectangle $A B C D$ circumscribed the ellipse $\frac{x^{2}}{9}+\frac{y^{2}}{4}=1, \quad \therefore A=(3,2)$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/aet9wmBJVgdIkqK5Yu0olFJanD-DZd2Mf-55gTg95GY.original.fullsize.png">


Let the ellipse circumscribing the rectangle $A B C D$ is $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1...(i)$

Given that ellipse (i) passes through $(a, 4)$ $\therefore b^{2}=16$

Also ellipse (i) passes through $A(3,2)$

$\therefore \quad \frac{9}{a^{2}}+\frac{4}{16}=1 \Rightarrow a^{2}=12$

$\therefore \quad e=\sqrt{1-\frac{12}{16}}=\sqrt{\frac{1}{4}}=\frac{1}{2}$

</details>

---

### Q6. JEE Advanced 2009 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

An ellipse intersects the hyperbola $2 x^2-2 y^2=1$ orthogonally. The eccentricity of the ellipse is reciprocal to that of the hyperbola. If the axes of the ellipse are along the coordinate axes, then

**Options:**

- **(A)** equation of ellipse is $x^2+2 y^2=2$
- **(B)** the foci of ellipse are $(\pm 1,0)$
- **(C)** equation of ellipse is $x^2+2 y^2=4$
- **(D)** the foci of ellipse are $(\pm \sqrt{2}, 0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) the foci of ellipse are $(\pm 1,0)$**

**Detailed Solution:**

Given, $2 x^2-2 y^2=1$
$$
\Rightarrow \quad \frac{x^2}{\left(\frac{1}{2}\right)}-\frac{y^2}{\left(\frac{1}{2}\right)}=1
$$
Eccentricity of hyperbola $=\sqrt{2}$
So, eccentricity of ellipse $=1 / \sqrt{2}$
Let equation of ellipse be
$$
\begin{aligned}
& \frac{x^2}{a^2}+\frac{y^2}{b^2}=1(a>b) \Rightarrow \frac{1}{\sqrt{2}}=\sqrt{1-\frac{b^2}{a^2}} \\
& \Rightarrow \quad \frac{b^2}{a^2}=\frac{1}{2} \Rightarrow a^2=2 b^2 \\
& \therefore \quad x^2+2 y^2=2 b^2 \\
&
\end{aligned}
$$
Let ellipse and hyperbola intersect at
$$
A\left(\frac{1}{\sqrt{2}} \sec \theta, \frac{1}{\sqrt{2}} \tan \theta\right)
$$
On differentiating Eq. (i),
$$
4 x-4 y \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=\frac{x}{y}
$$

$$
\therefore \quad\left(\frac{d y}{d x}\right)_{\text {at } A}=\frac{\sec \theta}{\tan \theta}=\operatorname{cosec} \theta
$$
On differentiating Eq. (ii),
$$
2 x+4 y \frac{d y}{d x}=0
$$

$$
\therefore \quad\left(\frac{d y}{d x}\right)_{\text {at } A}=-\frac{x}{2 y}=-\frac{1}{2} \operatorname{cosec} \theta
$$
Since, ellipse and hyperbola are orthogonal.
$$
\begin{aligned}
& \therefore \quad-\frac{1}{2} \operatorname{cosec}^2 \theta=-1 \\
& \Rightarrow \quad \operatorname{cosec}^2 \theta=2 \Rightarrow \theta=\pm \frac{\pi}{4} \\
& \therefore A\left(1, \frac{1}{\sqrt{2}}\right) \text { or }\left(1,-\frac{1}{\sqrt{2}}\right)
\end{aligned}
$$
From Eq. (i), $1+2\left(\frac{1}{\sqrt{2}}\right)^2=2 b^2$ $\Rightarrow \quad b^2=1$
Equation of ellipse is $x^2+2 y^2=2$
Coordinate of foci $(\pm a e, 0)$
$$
=\left(\pm \sqrt{2} \cdot \frac{1}{\sqrt{2}}, 0\right)=(\pm 1,0)
$$
Hence, options (a) and (b) are correct. If major axis is along $Y$-axis, then

$$
\begin{aligned}
& \frac{1}{\sqrt{2}}=\sqrt{1-\frac{a^2}{b^2}} \Rightarrow b^2=2 a^2 \\
& \therefore 2 x^2+y^2=2 a^2 \Rightarrow y^{\prime}=-\frac{2 x}{y} \\
& \Rightarrow \quad y^{\prime}\left(\frac{1}{\sqrt{2}} \sec \theta \frac{1}{\sqrt{2}} \tan \theta\right)=\frac{-2}{\sin \theta} \\
&
\end{aligned}
$$
As ellipse and hyperbola are orthogonal.
$$
\begin{array}{ll}
\therefore & -\frac{2}{\sin \theta} \cdot \operatorname{cosec} \theta=-1 \\
\Rightarrow & \operatorname{cosec}^2 \theta=1 \Rightarrow \theta=\pm \frac{\pi}{4} \\
\therefore & 2 x^2+y^2=2 a^2 \Rightarrow 2+\frac{1}{2}=2 a^2 \\
\Rightarrow & a^2=\frac{5}{4} \Rightarrow 2 x^2+y^2=\frac{5}{2}
\end{array}
$$
Corresponding foci are $(0, \pm 1)$.

</details>

---

### Q7. JEE Advanced 2008 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let $P\left(x_1, y_1\right)$ and $Q\left(x_2, y_2\right), y_1 < 0, y_2 < 0$, be the end points of the latusrectum of the ellipse $x^2+4 y^2=4$. The equations of parabolas with latusrectum $P Q$ are

**Options:**

- **(A)** $x^2+2 \sqrt{3} y=3+\sqrt{3}$
- **(B)** $x^2-2 \sqrt{3} y=3+\sqrt{3}$
- **(C)** $x^2+2 \sqrt{3} y=3-\sqrt{3}$
- **(D)** $x^2-2 \sqrt{3} y=3-\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^2+2 \sqrt{3} y=3-\sqrt{3}$**

**Detailed Solution:**

The equation $x^2+4 y^2=4$ represents an ellipse with 2 and 1 as semi-major and semi-minor axes and eccentricity $\frac{\sqrt{3}}{2}$. Thus, the ends of latusrect are $\left(\sqrt{3}, \frac{1}{2}\right)$ and $\left(\sqrt{3},-\frac{1}{2}\right),\left(-\sqrt{3},-\frac{1}{2}\right)$ and $\left(\sqrt{3},-\frac{1}{2}\right)$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/xEg5w8HkzhfUb5VNonqRlTHouyfpQlt8WmCSapQNpQ8.original.fullsize.png">

According to the question, we consider only $P\left(-\sqrt{3},-\frac{1}{2}\right)$ and $Q\left(\sqrt{3},-\frac{1}{2}\right)$.
Now, $\quad P Q=2 \sqrt{3}$
Thus, the coordinates of the vertex of the parabolas are $A\left(0, \frac{-1+\sqrt{3}}{2}\right)$ and $A^{\prime}\left(0, \frac{-1-\sqrt{3}}{2}\right)$ and corresponding equations are and
$$
(x-0)^2=-4 \cdot \frac{\sqrt{3}}{2}\left(y+\frac{1-\sqrt{3}}{2}\right)
$$
i.e., $(x-0)^2=4 \cdot \frac{\sqrt{3}}{2}\left(y-\frac{-1-\sqrt{3}}{2}\right)$ and
$$
\begin{aligned}
& x^2+2 \sqrt{3} y=3-\sqrt{3} \\
& x^2-2 \sqrt{3} y=3+\sqrt{3}
\end{aligned}
$$

</details>

---

### Q8. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

A hyperbola, having the transverse axis of length $2 \sin \theta$, is confocal with the ellipse $3 x^2+4 y^2=12$. Then, its equation is

**Options:**

- **(A)** $x^2 \operatorname{cosec}^2 \theta-y^2 \sec ^2 \theta=1$
- **(B)** $x^2 \sec ^2 \theta-y^2 \operatorname{cosec}^2 \theta=1$
- **(C)** $x^2 \sin ^2 \theta-y^2 \cos ^2 \theta=1$
- **(D)** $x^2 \cos ^2 \theta-y^2 \sin ^2 \theta=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x^2 \operatorname{cosec}^2 \theta-y^2 \sec ^2 \theta=1$**

**Detailed Solution:**

The given ellipse is
$$
\begin{aligned}
& \frac{x^2}{4}+\frac{y^2}{3}=1 \Rightarrow \alpha=2, \beta=\sqrt{3} \\
& \therefore \quad 3=4\left(1-e^2\right) \Rightarrow e=\frac{1}{2} \\
&
\end{aligned}
$$
$$
\therefore \quad a e=1
$$
Hence the eccentricity $e_1$, of the hyperbola is given by
$$
\begin{array}{rlrl} 
& & 1 & =e_1 \sin \theta \\
\Rightarrow & & e_1 & =\operatorname{cosec} \theta \\
\Rightarrow & b^2 & =\sin ^2 \theta\left(\operatorname{cosec}^2 \theta-1\right)=\cos ^2 \theta
\end{array}
$$
Hence, the hyperbola is
$$
\frac{x^2}{\sin ^2 \theta}-\frac{y^2}{\cos ^2 \theta}=1 \text { or } x^2 \operatorname{cosec}^2 \theta-y^2 \sec ^2 \theta=1
$$

</details>

---

