# JEE Main Mathematics - Parabola

## Topic 2: standard equation of parabola

**Total Questions:** 38

---

### Q1. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the directrix of the parabola $P: y^2 = 8x$, cut $x$-axis at the point $A$. Let $B(\alpha, \beta)$, $\alpha > 1$, be a point on $P$ such that the slope of $AB$ is $3/5$. If $BC$ is a focal chord of $P$, then six times the area of $\triangle ABC$ is :

**Options:**

- **(A)** $80$
- **(B)** $160$
- **(C)** $174$
- **(D)** $192$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $160$**

**Detailed Solution:**

For the parabola $P: y^2 = 8x$, we have $4a = 8 \Rightarrow a = 2$.

The equation of the directrix is $x = -a \Rightarrow x = -2$. Since the directrix cuts the $x$-axis at $A$, the coordinates of $A$ are $(-2, 0)$.

Let the coordinates of point $B$ on the parabola be $(2t_1^2, 4t_1)$.
The slope of $AB$ is given as $\dfrac{3}{5}$.

$\dfrac{4t_1 - 0}{2t_1^2 - (-2)} = \dfrac{3}{5}$

$\dfrac{2t_1}{t_1^2 + 1} = \dfrac{3}{5}$

$10t_1 = 3t_1^2 + 3 \Rightarrow 3t_1^2 - 10t_1 + 3 = 0$

$(3t_1 - 1)(t_1 - 3) = 0 \Rightarrow t_1 = \dfrac{1}{3}$ or $t_1 = 3$.

For $t_1 = \dfrac{1}{3}$, $\alpha = 2\left(\dfrac{1}{3}\right)^2 = \dfrac{2}{9}$, which is rejected since $\alpha > 1$.

For $t_1 = 3$, $\alpha = 2(3)^2 = 18 > 1$. Thus, $B$ is $(18, 12)$.

Since $BC$ is a focal chord, the parameter for $C$ is $t_2 = -\dfrac{1}{t_1} = -\dfrac{1}{3}$.

The coordinates of $C$ are $\left(2\left(-\dfrac{1}{3}\right)^2, 4\left(-\dfrac{1}{3}\right)\right) = \left(\dfrac{2}{9}, -\dfrac{4}{3}\right)$.

The area of $\triangle ABC$ is given by:
$\Delta = \dfrac{1}{2} \left| x_A(y_B - y_C) + x_B(y_C - y_A) + x_C(y_A - y_B) \right|$

$\Delta = \dfrac{1}{2} \left| -2\left(12 - \left(-\dfrac{4}{3}\right)\right) + 18\left(-\dfrac{4}{3} - 0\right) + \dfrac{2}{9}(0 - 12) \right|$

$\Delta = \dfrac{1}{2} \left| -2\left(\dfrac{40}{3}\right) - 24 - \dfrac{24}{9} \right|$

$\Delta = \dfrac{1}{2} \left| -\dfrac{80}{3} - 24 - \dfrac{8}{3} \right| = \dfrac{1}{2} \left| -\dfrac{88}{3} - \dfrac{72}{3} \right| = \dfrac{1}{2} \left| -\dfrac{160}{3} \right| = \dfrac{80}{3}$

Six times the area of $\triangle ABC = 6 \times \dfrac{80}{3} = 160$.

Answer: $160$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the point $P$ be the vertex of the parabola $y = x^2 - 6x + 12$. If a line passing through the point $P$ intersects the circle $x^2 + y^2 - 2x - 4y + 3 = 0$ at the points $R$ and $S$, then the maximum value of $(PR + PS)^2$ is :

**Options:**

- **(A)** $10$
- **(B)** $20$
- **(C)** $25$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $20$**

**Detailed Solution:**

The equation of the parabola is $y = x^2 - 6x + 12$, which can be rewritten as $y - 3 = (x - 3)^2$.

The vertex of the parabola is $P(3, 3)$.

The equation of the circle is $x^2 + y^2 - 2x - 4y + 3 = 0$, which can be rewritten as $(x - 1)^2 + (y - 2)^2 = 2$.

The center of the circle is $C(1, 2)$ and its radius is $r = \sqrt{2}$.

The distance between the point $P$ and the center $C$ is:

$PC = \sqrt{(3 - 1)^2 + (3 - 2)^2} = \sqrt{4 + 1} = \sqrt{5}$

Since $PC = \sqrt{5} > r = \sqrt{2}$, the point $P$ lies outside the circle.

Let the line through $P$ intersect the circle at $R$ and $S$, and let $M$ be the midpoint of the chord $RS$. The perpendicular distance from the center $C$ to the chord is $CM$.

Using the right-angled triangle $\triangle PCM$, the distance from $P$ to the midpoint $M$ is $PM = \sqrt{PC^2 - CM^2}$.

The lengths of the segments are $PR = PM - RM$ and $PS = PM + RM$.

Therefore, the sum of the distances is:

$PR + PS = (PM - RM) + (PM + RM) = 2PM = 2\sqrt{PC^2 - CM^2}$

To maximize $(PR + PS)^2$, we need to maximize $PC^2 - CM^2$. This occurs when $CM$ is minimized, which means $CM = 0$. This happens when the line passes through the center $C$ of the circle.

Substituting $CM = 0$, we get the maximum sum:

$PR + PS = 2PC = 2\sqrt{5}$

Thus, the maximum value of $(PR + PS)^2$ is:

$(2\sqrt{5})^2 = 4 \times 5 = 20$

Answer: $20$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $A,B$ and $C$ be the vertices of a variable right angled triangle inscribed in the parabola $y^2=16x$. Let the vertex $B$ containing the right angle be $(4,8)$ and the locus of the centroid of $\triangle ABC$ be a conic $C_o$. Then three times the length of latus rectum of $C_o$ is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

The equation of the parabola is $y^2 = 16x$, which gives $a = 4$. Any point on the parabola can be taken as $(4t^2, 8t)$.

The vertex $B$ is given as $(4,8)$, which corresponds to the parameter $t = 1$. Let the parameters for vertices $A$ and $C$ be $t_1$ and $t_2$ respectively. Thus, $A \equiv (4t_1^2, 8t_1)$ and $C \equiv (4t_2^2, 8t_2)$.

The slope of $AB$ is:
$m_{AB} = \dfrac{8t_1 - 8}{4t_1^2 - 4} = \dfrac{2(t_1 - 1)}{(t_1 - 1)(t_1 + 1)} = \dfrac{2}{t_1 + 1}$

Similarly, the slope of $BC$ is:
$m_{BC} = \dfrac{2}{t_2 + 1}$

Since $\triangle ABC$ is right-angled at $B$, $AB \perp BC$. Therefore, $m_{AB} \times m_{BC} = -1$:
$\dfrac{2}{t_1 + 1} \times \dfrac{2}{t_2 + 1} = -1$
$(t_1 + 1)(t_2 + 1) = -4$
$t_1t_2 + t_1 + t_2 + 5 = 0$

Let the centroid of $\triangle ABC$ be $(h, k)$. Then:
$h = \dfrac{4 + 4t_1^2 + 4t_2^2}{3} \Rightarrow t_1^2 + t_2^2 = \dfrac{3h}{4} - 1$
$k = \dfrac{8 + 8t_1 + 8t_2}{3} \Rightarrow t_1 + t_2 = \dfrac{3k}{8} - 1$

From the perpendicularity condition, we can express $t_1t_2$ as:
$t_1t_2 = -5 - (t_1 + t_2) = -5 - \left(\dfrac{3k}{8} - 1\right) = -4 - \dfrac{3k}{8}$

Using the algebraic identity $t_1^2 + t_2^2 = (t_1 + t_2)^2 - 2t_1t_2$, we substitute the expressions in terms of $k$:
$\dfrac{3h}{4} - 1 = \left(\dfrac{3k}{8} - 1\right)^2 - 2\left(-4 - \dfrac{3k}{8}\right)$
$\dfrac{3h}{4} - 1 = \dfrac{9k^2}{64} - \dfrac{3k}{4} + 1 + 8 + \dfrac{3k}{4}$
$\dfrac{3h}{4} - 1 = \dfrac{9k^2}{64} + 9$
$\dfrac{3h}{4} = \dfrac{9k^2}{64} + 10$
$3h = \dfrac{9k^2}{16} + 40$
$\dfrac{9k^2}{16} = 3h - 40$
$k^2 = \dfrac{16}{9}(3h - 40) = \dfrac{16}{3}\left(h - \dfrac{40}{3}\right)$

Replacing $(h, k)$ with $(x, y)$, the locus $C_o$ is the parabola:
$y^2 = \dfrac{16}{3}\left(x - \dfrac{40}{3}\right)$

The length of the latus rectum of this parabola is $\dfrac{16}{3}$.

Three times the length of the latus rectum is $3 \times \dfrac{16}{3} = 16$.

Answer: $16$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 1)

*Type:* `numerical` | *Level:* `3`

Consider the parabola $P : y^2 = 4kx$ and the ellipse $E : \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$. Let the line segment joining the points of intersection of $P$ and $E$, be their latus rectums. If the eccentricity of $E$ is $e$, then $e^2 + 2\sqrt{2}$ is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

The latus rectum of the parabola $P: y^2 = 4kx$ is the line segment $x = k$. The endpoints of this latus rectum are $(k, 2k)$ and $(k, -2k)$.

The latus rectum of the ellipse $E: \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ is the line segment $x = ae$ (taking the one in the positive $x$-axis). The endpoints of this latus rectum are $\left(ae, \dfrac{b^2}{a}\right)$ and $\left(ae, -\dfrac{b^2}{a}\right)$.

Since the line segment joining the points of intersection of $P$ and $E$ is the latus rectum for both curves, their endpoints must coincide. Comparing the coordinates, we get:
$k = ae$
$2k = \dfrac{b^2}{a}$

Substituting $k = ae$ into the second equation:
$2ae = \dfrac{b^2}{a}$
$2a^2e = b^2$

For an ellipse, the relation between $a, b,$ and $e$ is $b^2 = a^2(1 - e^2)$. Substituting this into the equation above:
$2a^2e = a^2(1 - e^2)$

Since $a \neq 0$, we can divide by $a^2$:
$2e = 1 - e^2$
$e^2 + 2e - 1 = 0$

Solving for $e$ using the quadratic formula:
$e = \dfrac{-2 \pm \sqrt{4 - 4(1)(-1)}}{2} = \dfrac{-2 \pm 2\sqrt{2}}{2} = -1 \pm \sqrt{2}$

Since the eccentricity of an ellipse must satisfy $0 < e < 1$, we take the positive root:
$e = \sqrt{2} - 1$

We need to find the value of $e^2 + 2\sqrt{2}$. First, calculate $e^2$:
$e^2 = (\sqrt{2} - 1)^2 = 2 - 2\sqrt{2} + 1 = 3 - 2\sqrt{2}$

Therefore:
$e^2 + 2\sqrt{2} = (3 - 2\sqrt{2}) + 2\sqrt{2} = 3$

Answer: $3$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the parabola $y = x^2 + px + q$ passing through the point $(1, -1)$ be such that the distance between its vertex and the $x$-axis is minimum. Then the value of $p^2 + q^2$ is:

**Options:**

- **(A)** $2$
- **(B)** $4$
- **(C)** $5$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4$**

**Detailed Solution:**

Given the equation of the parabola $y = x^2 + px + q$.

Since it passes through $(1, -1)$, we have:

$-1 = 1 + p + q \Rightarrow q = -p - 2$

The vertex of the parabola $y = x^2 + px + q$ occurs at $x = -\dfrac{p}{2}$.

The $y$-coordinate of the vertex is:

$y_v = \left(-\dfrac{p}{2}\right)^2 + p\left(-\dfrac{p}{2}\right) + q = -\dfrac{p^2}{4} + q$

The distance between the vertex and the $x$-axis is $|y_v|$. Substituting $q = -p - 2$ into the expression for $y_v$:

$|y_v| = \left|-\dfrac{p^2}{4} - p - 2\right| = \dfrac{1}{4}|p^2 + 4p + 8| = \dfrac{1}{4}|(p+2)^2 + 4|$

To minimize this distance, the term $(p+2)^2$ must be minimum. Since $(p+2)^2 \ge 0$ for all real $p$, the minimum value occurs at $p = -2$.

Substituting $p = -2$ into $q = -p - 2$, we get:

$q = -(-2) - 2 = 0$

Therefore, the value of $p^2 + q^2$ is:

$p^2 + q^2 = (-2)^2 + 0^2 = 4$

Answer: $4$

</details>

---

### Q6. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let P be the parabola, whose focus is $(-2,1)$ and directrix is $2 x+y+2=0$. Then the sum of the ordinates of the points on P , whose abscissa is -2 , is

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{5}{2}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{2}$**

**Detailed Solution:**

Equation of parabola
$(x+2)^2+(y-1)^2=\left(\frac{2 x+y+2}{\sqrt{5}}\right)^2$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qZ3Y8sfiWupYB2A7M7C8hxcWRQvBpUEFE3t7VgevHOM.original.fullsize.png"/>
$5\left[(x+2)^2+(y-1)^2\right]=(2 x+y+2)^2$
Put $x=-2,5(y-1)^2=(y-2)^2$
$\begin{aligned}
& 5\left(y^2-2 y+1\right)=y^2-4 y+4 \\
& \Rightarrow 4 y^2-6 y+1=0 \Rightarrow y_1+y_2=\frac{3}{2}
\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The axis of a parabola is the line $y=x$ and its vertex and focus are in the first quadrant at distances $\sqrt{2}$ and $2 \sqrt{2}$ units from the origin, respectively. If the point $(1, \mathrm{k})$ lies on the parabola, then a possible value of $k$ is :-

**Options:**

- **(A)** $4$
- **(B)** $9$
- **(C)** $3$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $9$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jT64Tsn54xcawd5yrqU2pWfVNTSzeGLQOfWy0mGyCJk.original.fullsize.png"/>
Directrix $x+y=0$
$\begin{aligned}
& \mathrm{PS}=\mathrm{PM} \\
& \sqrt{(1-2)^2+(\mathrm{K}-2)^2}=\frac{(1+\mathrm{K})}{\sqrt{2}} \\
& 2 \mathrm{~K}^2+8-8 \mathrm{~K}+2=\mathrm{K}^2+1+2 \mathrm{~K} \\
& \mathrm{~K}^2-10 \mathrm{~K}+9=0 \\
& \mathrm{~K}=9 \\
& \text { option (2) }
\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two parabolas have the same focus \((4,3)\) and their directrices are the \(x\)-axis and the \(y\)-axis, respectively. If these parabolas intersects at the points \(A\) and \(B\), then \((A B)^2\) is equal to :

**Options:**

- **(A)** 392
- **(B)** 384
- **(C)** 192
- **(D)** 96

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 192**

**Detailed Solution:**

The parabolas are
$(x-4)^2+(y-3)^2=x^2$ ...(i)
and $(x-4)^2+(y-3)^2=y^2$...
If point of intersection are $A\left(x_1, y_1\right)$ and $B\left(x_2, y_2\right)$ By solving (i) and (ii), we get
$\begin{aligned}
& x_1+x_2=14 \text { and } x_1 x_2=25 \\
& (A B)^2=2\left(\left(x_1+x_2\right)^2-4 x_1 x_2\right)=192
\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (28 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let A and B be the two points of intersection of the line $y+5=0$ and the mirror image of the parabola $y^2=4 x$ with respect to the line $x+y+4=0$. If d denotes the distance between A and B , and a denotes the area of $\triangle S A B$, where $S$ is the focus of the parabola $y^2=4 x$, then the value of $(a+d)$ is $\qquad$ -

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3phf8FKCXWENoPsupnGTtuUzi5h_cVrhSOtne9RCNmk.original.fullsize.png">

To find image of $P\left(t^2, 2 t\right)$
$\begin{aligned}
& \frac{x-t^2}{1}=\frac{y-2 t}{1}=\frac{-2\left(t^2+2 t+4\right)}{1^2+1^2}=-(t+1)^2-3 \\
& x=t^2-(t+1)^2-3=-2 t-4 \\
& y=2 t-(t+1)^2-3=-t^2-4 \\
& t=\frac{-x-4}{2} \\
& \Rightarrow y+4=-\left(\frac{-x-4}{2}\right)^2 \\
& \Rightarrow(y+4)=-\frac{(x+4)^2}{4} \\
& \Rightarrow x^2=-4 y \\
& \Rightarrow \text { Focus }(-4,-5)
\end{aligned}$
$\text { Also, } y=-5 \text { intersect }$
$\begin{aligned} & \therefore(-4)(-1)=(x+4)^2 \\ & 4=(x+4)^2 \\ & x+4= \pm 2 \\ & x=-2,-6 \\ & \Rightarrow d=4 \\ & a=\frac{1}{2}\left|\begin{array}{ccc}1 & 0 & 1 \\ -2 & -5 & 1 \\ -6 & -5 & 1\end{array}\right| \\ & =\frac{1}{2}|[1(-5+5)+1(10-30)]| \\ & =\frac{1}{2}(20) \\ & a=10 \\ & \therefore \quad a+d=14\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (23 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

The focus of the parabola $y^2=4 x+16$ is the centre of the circle $C$ of radius 5 . If the values of $\lambda$, for which C passes through the point of intersection of the lines $3 x-y=0$ and $x+\lambda y=4$, are $\lambda_1$ and $\lambda_2, \lambda_1 \lt \lambda_2$, then $12 \lambda_1+29 \lambda_2$ is equal to $\qquad$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **15**

**Detailed Solution:**

$y^2=4(x+4)$

Equation of circle
$(x+3)^2+y^2=25$
Passes through the point of intersection of two lines $3 x-y=0$ and $x+\lambda y=4$
$\left(\frac{4}{3 \lambda+1}, \frac{12}{3 \lambda+1}\right) \text {, we get }$
$\begin{aligned}
& \lambda=-\frac{7}{6}, 1 \\
& 12 \lambda_1+29 \lambda_2 \\
& -14+29=15
\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the shortest distance from $(\mathrm{a}, 0), \mathrm{a}\gt0$, to the parabola $y^2=4 x$ be 4 . Then the equation of the circle passing through the point $(a, 0)$ and the focus of the parabola, and having its centre on the axis of the parabola is :

**Options:**

- **(A)** $x^2+y^2-10 x+9=0$
- **(B)** $x^2+y^2-6 x+5=0$
- **(C)** $x^2+y^2-4 x+3=0$
- **(D)** $x^2+y^2-8 x+7=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2+y^2-6 x+5=0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Rx3Bg8shiVG3WR4vGZQwIGxvwGEtAKB2r_vscht4F8I.original.fullsize.png">



Normal at P
$\begin{aligned}
& y+ t x=2 t+t^3 \\
& \uparrow \\
&(\mathrm{a}, 0) \\
& \mathrm{at}= 2 \mathrm{t}+\mathrm{t}^3 \\
& \mathrm{a}= 2+\mathrm{t}^2 \\
& \mathbb{R}\left(2+\mathrm{t}^2, 0\right)
\end{aligned}$

$\begin{aligned}
& \mathrm{PR}=4 \Rightarrow 4+4 \mathrm{t}^2=16 \\
& 4 \mathrm{t}^2=12 \Rightarrow \mathrm{t}^2=3 \\
& \mathrm{a}=5 \mathbb{R}(5,0)
\end{aligned}$

Focus $(1,0)$
$(1,0) \&(5,0)$ will be tha end pts. of diameter
$\Rightarrow \mathrm{Eg}^{\mathrm{n}}$ of circle is
$\begin{aligned}
& (x-1)(x-5)+y^2=0 \\
& x^2+y^2-6 x+5=0
\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the parabola $y=x^2+\mathrm{p} x-3$, meet the coordinate axes at the points $\mathrm{P}, \mathrm{Q}$ and R . If the circle C with centre at $(-1,-1)$ passes through the points $P, Q$ and $R$, then the area of $\triangle P Q R$ is :

**Options:**

- **(A)** $7$
- **(B)** $4$
- **(C)** $6$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6$**

**Detailed Solution:**

$\mathrm{y}=\mathrm{x}^2+\mathrm{px}-3$

Let $\mathrm{P}(\alpha, 0), \mathrm{Q}(\beta, 0), \mathrm{R}(0,-3)$
Circle with centre $(-1,-1)$ is $(x+1)^2+(y+1)^2=r^2$
Passes through $(0,-3)$
$\begin{aligned}
& \left.1^2+(-2)^2=r^2\right] \\
& \mathrm{r}^2=5
\end{aligned}$
$(x+1)^2+(y+1)^2=5$

Put $\mathrm{y}=0$
$\begin{aligned}
& (x+1)^2=5-1 \\
& (x+1)^2=4 \\
& x+1= \pm 2 \\
& x=1 \text { or } x=-3 \\
& \therefore P(1,0) \text { and } Q(-3,0)
\end{aligned}$

Area of $\triangle \mathrm{PQR}=\frac{1}{2}\left|\begin{array}{ccc}1 & 0 & 1 \\ -3 & 0 & 1 \\ 0 & -3 & 1\end{array}\right|=6$

</details>

---

### Q13. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $A, B$ and $C$ be three points on the parabola $y^2=6 x$ and let the line segment $A B$ meet the line $L$ through $C$ parallel to the $x$-axis at the point $D$. Let $M$ and $N$ respectively be the feet of the perpendiculars from $A$ and $B$ on $L$. Then $\left(\frac{A M \cdot B N}{C D}\right)^2$ is equal to _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZyG7UMS1qhz2co-hkd4swvxIOdvaGhq7H-jUzofyC60.original.fullsize.png">
$\begin{aligned} & \mathrm{m}_{\mathrm{AB}}=\mathrm{m}_{\mathrm{AD}} \\ & \Rightarrow \quad \frac{2}{\mathrm{t}_1+\mathrm{t}_2}=\frac{2 \mathrm{a}\left(\mathrm{t}_1-\mathrm{t}_3\right)}{\mathrm{at}_1^2-\alpha} \\ & \Rightarrow \quad \mathrm{at}_1^2-\alpha=\mathrm{a}\left\{\mathrm{t}_1^2-\mathrm{t}_1 \mathrm{t}_3+\mathrm{t}_1 \mathrm{t}_2-\mathrm{t}_2 \mathrm{t}_3\right\} \\ & \Rightarrow \quad \alpha=\mathrm{a}\left(\mathrm{t}_1 \mathrm{t}_3+\mathrm{t}_2 \mathrm{t}_3-\mathrm{t}_1 \mathrm{t}_2\right) \\ & \mathrm{AM}=\left|2 \mathrm{a}\left(\mathrm{t}_1-\mathrm{t}_3\right)\right|, \mathrm{BN}=\left|2 \mathrm{a}\left(\mathrm{t}_2-\mathrm{t}_3\right)\right|, \\ & \mathrm{CD}=\left|\mathrm{at}_3^2-\alpha\right|\end{aligned}$
$\begin{aligned} & \mathrm{CD}=\left|\mathrm{at}_3^2-\mathrm{a}\left(\mathrm{t}_1 \mathrm{t}_3+\mathrm{t}_2 \mathrm{t}_3-\mathrm{t}_1 \mathrm{t}_2\right)\right| \\ &=\mathrm{a}\left|\mathrm{t}_3^2-\mathrm{t}_1 \mathrm{t}_3-\mathrm{t}_2 \mathrm{t}_3+\mathrm{t}_1 \mathrm{t}_2\right| \\ &=\mathrm{a}\left|\mathrm{t}_3\left(\mathrm{t}_3-\mathrm{t}_1\right)-\mathrm{t}_2\left(\mathrm{t}_3-\mathrm{t}_1\right)\right| \\ & \mathrm{CD}=\mathrm{a}\left|\left(\mathrm{t}_3-\mathrm{t}_2\right)\left(\mathrm{t}_3-\mathrm{t}_1\right)\right| \\ &\left(\frac{\mathrm{AM} \cdot \mathrm{BN}}{\mathrm{CD}}\right)^2=\left\{\frac{2 \mathrm{a}\left(\mathrm{t}_1-\mathrm{t}_3\right) \cdot 2 \mathrm{a}\left(\mathrm{t}_2-\mathrm{t}_3\right)}{\mathrm{a}\left(\mathrm{t}_3-\mathrm{t}_2\right)\left(\mathrm{t}_3-\mathrm{t}_1\right)}\right\}^2 \\ & 16 \mathrm{a}^2=16 \times \frac{9}{4}=36\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let a conic $C$ pass through the point $(4,-2)$ and $P(x, y), x \geq 3$, be any point on $C$. Let the slope of the line touching the conic $C$ only at a single point $P$ be half the slope of the line joining the points $P$ and $(3,-5)$. If the focal distance of the point $(7,1)$ on $C$ is $d$, then $12 d$ equals ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **75**

**Detailed Solution:**

$P(x, y) \& x \geq 3$
Slope of line at $P(x, y)$ will be $\frac{d y}{d x}=\frac{1}{2}\left(\frac{y+5}{x-3}\right)$
$\begin{aligned}
& \Rightarrow 2 \frac{d y}{(y+5)}=\frac{1}{(x-3)} d x \\
& \Rightarrow 2 \ln (y+5)=\ln (x-3)+C
\end{aligned}$
Passes through $(4,-2)$
$\begin{aligned}
& \Rightarrow 2 \ln (3)=\ln (1)+C \\
& \Rightarrow C=2 \ln (3) \\
& \Rightarrow 2 \ln (y+5)=\ln (x-3)+2 \ln (3) \\
& \Rightarrow 2\left(\ln \left(\frac{y+5}{3}\right)\right)=\ln (x-3) \\
& \Rightarrow\left(\frac{y+5}{3}\right)^2=(x-3)
\end{aligned}$
$\Rightarrow(y+5)^2=9(x-3)$
Parabola
$\begin{gathered}
4 a=9 \\
a=\frac{9}{4}
\end{gathered}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9_FUufYi5OdJD2shrSf9IGblPs6QBkRduUJObbXkFz4.original.fullsize.png">
$\begin{aligned} & d=\sqrt{\left(\frac{7}{4}\right)^2+6^2} \\ & d=\frac{\sqrt{625}}{4} \\ & d=\frac{25}{4} \\ & 12 d=75\end{aligned}$

</details>

---

### Q15. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Suppose $A B$ is a focal chord of the parabola $y^2=12 x$ of length $l$ and slope $\mathrm{m} < \sqrt{3}$. If the distance of the chord $\mathrm{AB}$ from the origin is $\mathrm{d}$, then $l \mathrm{~d}^2$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **108**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KaNcBfk-1NFUAGKeJHmCIOo3woxKXuvc6Ii9JoeSrFQ.original.fullsize.png">
$\begin{aligned} & \ell=4 \mathrm{a} \operatorname{cosec}^2 \theta \\ & \ell=12 \times \frac{9}{\mathrm{~d}^2} \\ & \ell \mathrm{d}^2=108\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let PQ be a chord of the parabola $y^2=12 x$ and the midpoint of PQ be at $(4,1)$. Then, which of the following point lies on the line passing through the points $\mathrm{P}$ and Q?

**Options:**

- **(A)** $(3,-3)$
- **(B)** $(2,-9)$
- **(C)** $\left(\frac{3}{2},-16\right)$
- **(D)** $\left(\frac{1}{2},-20\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{1}{2},-20\right)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/22L_aALeywfJli70giskXIWSZaRFlN-oklqkbZD-Mk0.original.fullsize.png">
$\begin{aligned}
& T=S_1 \\
& y-6(x+4) \\
& =1-48 \\
& 6 x-y=23
\end{aligned}$
Option $4\left(\frac{1}{2},-20\right)$ will satisfy

</details>

---

### Q17. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let the length of the focal chord PQ of the parabola $y^2=12 x$ be 15 units. If the distance of $\mathrm{PQ}$ from the origin is $\mathrm{p}$, then $10 \mathrm{p}^2$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **72**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_jCi2vyl1VFn5VM-Zr1--6uJmoXfJK943N1Gzl-r_eI.original.fullsize.png">
$\begin{aligned} & \text { length of focal chord }=4 a \operatorname{cosec}^2 \theta=15 \\ & 12 \operatorname{cosec}^2 \theta=15 \\ & \sin ^2 \theta=\frac{4}{5} \\ & \tan ^2 \theta=4 \\ & \tan \theta=2 \\ & \text { equation } \frac{y-0}{x-3}=2 \\ & y=2 x-6 \\ & 2 x-y-6=0 \\ & P=\frac{6}{\sqrt{5}} \\ & 10 p^2=10 \cdot \frac{36}{5}=72\end{aligned}$

</details>

---

### Q18. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The maximum area of a triangle whose one vertex is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo></math> and the other two vertices lie on the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>54</mn></math> at points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mo> </mo><mi>y</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mi>x</mi><mo>,</mo><mo> </mo><mi>y</mi><mo>)</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>&gt;</mo><mn>0</mn></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>88</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>122</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>92</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1158eab9-e058-4564-acfe-84ef34e2137d.png" style="width: 250px; height: 171px;"/></p><p>Let, area of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi></math> be denoted by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mn>0</mn><mo>-</mo><mn>0</mn><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mi>x</mi><mfenced><mrow><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>54</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mo>=</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>54</mn><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>P</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>54</mn></mrow></mfenced></math></p><p>For critical points, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>P</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>54</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mo>±</mo><mn>3</mn></math></p><p>So, the maximum area will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>3</mn><mo>(</mo><mo>-</mo><mn>2</mn><mo>×</mo><mn>9</mn><mo>+</mo><mn>54</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>A</mi><mo>=</mo><mn>108</mn></math></p>

</details>

---

### Q19. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the shortest distance of the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi></math> from the centre of the circle <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>16</mn><mi>y</mi><mo>+</mo><mn>64</mn><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>**

**Detailed Solution:**

<p>Given: Equation of parabola is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi></math>  and the equation of circle is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>16</mn><mi>y</mi><mo>+</mo><mn>64</mn><mo>=</mo><mn>0</mn></math>.</p><p>We know that, equation of normal to parabola is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>m</mi><mo>-</mo><msup><mi>m</mi><mn>3</mn></msup></math>.</p><p>Also, the centre of given circle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>8</mn></mrow></mfenced></math>.</p><p>The normal of parabola is passing through center of circle.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>8</mn><mo>=</mo><mn>2</mn><mi>m</mi><mo>-</mo><mn>2</mn><mi>m</mi><mo>-</mo><msup><mi>m</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>So point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> on parabola is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>am</mi><mn>2</mn></msup><mo>,</mo><mo>-</mo><mn>2</mn><mi>am</mi></mrow></mfenced><mo>=</mo><mo>(</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>)</mo></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi><mo>=</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>8</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mi>C</mi><mo>=</mo><msqrt><mn>4</mn><mo>+</mo><mn>16</mn></msqrt><mo>=</mo><msqrt><mn>20</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mo>=</mo><mn>20</mn></math>.</p>

</details>

---

### Q20. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The parabolas : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>e</mi><mi>x</mi><mo>+</mo><mi>f</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> intersect on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>,</mo><mo>&#160;</mo><mi>e</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi></math> are positive real numbers and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>,</mo><mi>e</mi><mo>,</mo><mi>f</mi></math> are in A.P.
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mi>a</mi></mfrac><mo>,</mo><mfrac><mi>e</mi><mi>b</mi></mfrac><mo>,</mo><mfrac><mi>f</mi><mi>c</mi></mfrac></math> are in G.P.
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mi>a</mi></mfrac><mo>,</mo><mfrac><mi>e</mi><mi>b</mi></mfrac><mo>,</mo><mfrac><mi>f</mi><mi>c</mi></mfrac></math> are in A.P.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>,</mo><mi>e</mi><mo>,</mo><mi>f</mi></math> are in G.P.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mi>a</mi></mfrac><mo>,</mo><mfrac><mi>e</mi><mi>b</mi></mfrac><mo>,</mo><mfrac><mi>f</mi><mi>c</mi></mfrac></math> are in A.P.**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>e</mi><mi>x</mi><mo>+</mo><mi>f</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> intersect on the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math>,</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math> are in G.P.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mi>a</mi><mi>c</mi></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>and taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>ax</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msqrt><mi>ac</mi><mi>x</mi></msqrt><mo>+</mo><mi mathvariant="normal">c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup><mo>=</mo><mi>ac</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>x</mi><msqrt><mi>a</mi></msqrt><mo>+</mo><msqrt><mi>c</mi></msqrt><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><msqrt><mi>c</mi></msqrt><msqrt><mi>a</mi></msqrt></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><mi>c</mi><mi>a</mi></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now, putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>e</mi><mi>x</mi><mo>+</mo><mi>f</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> and taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mfenced><mfrac><mi>c</mi><mi>a</mi></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>e</mi><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><msqrt><mi>c</mi></msqrt><msqrt><mi>a</mi></msqrt></mfrac></mrow></mfenced><mo>+</mo><mi>f</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>c</mi></mrow><mi>a</mi></mfrac><mo>+</mo><mi>f</mi><mo>=</mo><mn>2</mn><mi>e</mi><msqrt><mfrac><mi>c</mi><mi>a</mi></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>d</mi><mi>a</mi></mfrac><mo>+</mo><mfrac><mi>f</mi><mi>c</mi></mfrac><mo>=</mo><mn>2</mn><mi>e</mi><msqrt><mfrac><mn>1</mn><mrow><mi>a</mi><mi>c</mi></mrow></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>d</mi><mi>a</mi></mfrac><mo>+</mo><mfrac><mi>f</mi><mi>c</mi></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>e</mi></mrow><mi>b</mi></mfrac></math>  as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>b</mi><mo>=</mo><msqrt><mi>a</mi><mi>c</mi></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mi>d</mi><mi>a</mi></mfrac><mo>,</mo><mfrac><mi>e</mi><mi>b</mi></mfrac><mo>,</mo><mfrac><mi>f</mi><mi>c</mi></mfrac></math>are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math></p>

</details>

---

### Q21. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the length of the latus rectum of a parabola, whose focus is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced></math> and the tangent at its vertex is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mi>a</mi></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>a</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given the equation of tangent at vertex is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mi>a</mi></math></p><p>and the focus is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>a</mi></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/957085c2-8e98-4eb5-80fc-448d1775f7a2-image.png" style="width: 199px; height: 200px;" /></p><p>Now the perpendicular distance from focus to tangent is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|"><mrow><mi>a</mi><mo>+</mo><mi>a</mi><mo>-</mo><mi>a</mi></mrow></mfenced><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mfrac><mfenced close="|" open="|"><mi>a</mi></mfenced><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Also given length of latus rectum<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mi>a</mi><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>=</mo><mfrac><mn>16</mn><mn>4</mn></mfrac><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>a</mi></mfenced><mo>=</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></math></p></blockquote>

</details>

---

### Q22. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If vertex of parabola is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math> and equation of its directrix is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>=</mo><mn>21</mn></math>, then the length of latus rectum is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<p>Plotting the graph with given data we have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9551faae-7bef-4bb2-b424-06c621bb12f9-image.png" style="width: 255px; height: 180px;" /></p><p>We know that, in any parabola, the length of the latus rectum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>a</mi></math> and perpendicular distance from vertex to the directrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>a</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mn>8</mn><mo>+</mo><mn>3</mn><mo>-</mo><mn>21</mn></mrow><msqrt><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mo>-</mo><mn>10</mn></mrow><mn>5</mn></mfrac></mfenced><mo>=</mo><mn>2</mn></math> </p><p>Therefore, the length of the latus rectum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>a</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q23. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the equation of the parabola, whose vertex is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and the directrix is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>29</mn><mo>=</mo><mn>0</mn></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mi>y</mi><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mi>d</mi><mi>y</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>575</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>575</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>576</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>576</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>576</mn></math>**

**Detailed Solution:**

<p>Given the equation of the parabola whose vertex is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and equation of directrix is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>29</mn><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mi>y</mi><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mi>d</mi><mi>y</mi><mo>+</mo><mi>e</mi><mo>=</mo><mn>0</mn></math></p><p>Let focus be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced></math></p><p>Let equation of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mi>V</mi></math> which is perpendicular to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>29</mn><mo>=</mo><mn>0</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>k</mi><mo>=</mo><mn>0</mn></math> and it passes through point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>.  So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>7</mn></math> and equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mi>V</mi></math> become <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math></p><p>Now the intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>29</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>7</mn><mo>=</mo><mn>0</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mo>=</mo><mfenced><mrow><mn>8</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p>Now plotting the diagram we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/93cb329f-f8e1-4906-85ee-f88cbac96d43-image.png" style="width: 250px; height: 175px;" /></p><p>So, foot of perpendicular from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>29</mn><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math></p><p>Now using the midpoint formula we will find the focus of parabola<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mn>8</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>5</mn><mo>,</mo><mfrac><mrow><mi>&#946;</mi><mo>+</mo><mn>5</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Focus is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> and directrix is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>29</mn><mo>=</mo><mn>0</mn></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>P</mi><mi>S</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>P</mi><mi>M</mi></mrow></mfenced><mn>2</mn></msup></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>29</mn></mrow></mfenced><mn>2</mn></msup></mstyle><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>134</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>711</mn><mo>=</mo><mn>0</mn></math></p><p>Comparing with<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mi>y</mi><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mi>d</mi><mi>y</mi><mo>+</mo><mi>e</mi><mo>=</mo><mn>0</mn></math> , we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>9</mn><mo>-</mo><mn>6</mn><mo>+</mo><mn>134</mn><mo>-</mo><mn>2</mn><mo>-</mo><mn>711</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>576</mn></math></p>

</details>

---

### Q24. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mi>t</mi><mo>,</mo><mi>y</mi><mo>=</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>3</mn></mfrac></math> be a conic. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the focus and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be the point on the axis of the conic such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mi>A</mi><mo>&#8869;</mo><mi>B</mi><mi>A</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is any point on the conic. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is the ordinate of the centroid of the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>S</mi><mi>A</mi><mi>B</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>18</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>18</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>18</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>18</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>18</mn></mfrac></math>**

**Detailed Solution:**

<p>The parametric form <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mi>t</mi><mo>,</mo><mi>y</mi><mo>=</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>3</mn></mfrac></math> represents the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>12</mn><mi>y</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/848931ac-c584-4fcd-b126-5ab03623bfce-image.png" style="width: 300px; height: 243px;" /></p><p> </p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>S</mi><mo>&#8869;</mo><mi>A</mi><mi>B</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mrow><mi>A</mi><mi>S</mi></mrow></msub><mo>&#183;</mo><msub><mi>m</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfenced><mrow><mn>3</mn><mo>-</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mfenced><mrow><mn>0</mn><mo>-</mo><mn>2</mn><mi>t</mi></mrow></mfenced></mfrac><mo>&#183;</mo><mfrac><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mfenced><mrow><mn>0</mn><mo>-</mo><mn>2</mn><mi>t</mi></mrow></mfenced></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mn>27</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><msup><mi>t</mi><mn>4</mn></msup></mrow><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfrac></math></p><p>Ordinate of centroid of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>S</mi><mi>A</mi><mi>B</mi><mo>=</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mo>+</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>+</mo><mn>3</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>9</mn><mo>+</mo><mn>3</mn><mi>&#945;</mi><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mi>k</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mn>1</mn></mrow></munder><mfrac><mn>1</mn><mn>9</mn></mfrac><mfenced><mrow><mn>9</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><mrow><mn>27</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><msup><mi>t</mi><mn>4</mn></msup></mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfenced></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>13</mn><mn>18</mn></mfrac></math></p>

</details>

---

### Q25. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math> be a parabola with vertex <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> and focus <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> be its mirror image with respect to the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>6</mn></math>. Then the directrix of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo></math> _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p>Plotting the diagram as per given data we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bb1eff35-b792-43c9-9980-83a3b14f65f9-9722974.png" style="width: 310px; height: 197px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math>: Directrix</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>-</mo><mi>k</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><mn>3</mn><mo>+</mo><mn>4</mn><mo>-</mo><mi>K</mi></mrow><msqrt><mn>5</mn></msqrt></mfrac></mfenced><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>7</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mn>7</mn><mo>-</mo><mi>K</mi><mo>=</mo><mn>5</mn></mtd><mtd><mn>7</mn><mo>-</mo><mi>K</mi><mo>=</mo><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mi>k</mi><mo>=</mo><mn>2</mn></mtd><mtd><mi>k</mi><mo>=</mo><mn>12</mn></mtd></mtr><mtr><mtd><mi>Accepted</mi></mtd><mtd><mi>Rejected</mi><mo>&#160;</mo><mi>Passes</mi><mo>&#160;</mo><mi>through</mi><mo>&#160;</mo><mi>focus</mi></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open=""><mtable columnalign="left"><mtr><mtd><msub><mi>D</mi><mn>1</mn></msub><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>6</mn></mtd></mtr><mtr><mtd><msub><mi>D</mi><mn>2</mn></msub><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mi>C</mi></mtd></mtr></mtable></mfenced><mo>&#8658;</mo><mi>d</mi><mo>&#8658;</mo><mi>d</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q26. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The length of the latus rectum of a parabola, whose vertex and focus are on the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>(</mo><mo>&#62;</mo><mi mathvariant="normal">R</mi><mo>)</mo></math> respectively from the origin, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>(</mo><mo>&#160;</mo><mi>S</mi><mo>-</mo><mi>R</mi><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>(</mo><mi>S</mi><mo>+</mo><mi>R</mi><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>S</mi><mo>-</mo><mi>R</mi><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>S</mi><mo>+</mo><mi>R</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>S</mi><mo>-</mo><mi>R</mi><mo>)</mo></math>**

**Detailed Solution:**

A parabola, whose vertex and focus are on the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>- axis at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>(</mo><mo>&#62;</mo><mi mathvariant="normal">R</mi><mo>)</mo></math> respectively from the origin.<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mo>(</mo><mi>x</mi><mo>-</mo><mi>R</mi><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>(</mo><mi>S</mi><mo>-</mo><mi>R</mi><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mi>R</mi><mo>)</mo></math>
Length of Latus rectum<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>(</mo><mi>S</mi><mo>-</mo><mi>R</mi><mo>)</mo></math></p>

</details>

---

### Q27. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math> be a point on the parabola, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>12</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> be the foot of the perpendicular drawn from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> , on the axis of the parabola. A line is now drawn through the mid-point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>N</mi></math>, parallel to its axis which meets the parabola at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>. If the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>intercept of the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NQ</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo></math> then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>N</mi><mo>=</mo><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>N</mi><mo>=</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Comparing the equation of the parabola, with standard equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn></math>.</p><p>Figure is drawn on the basis of the given information.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8436dc67-a9c2-48a5-ba9c-13ab46ac02f3-Q6JEEMAINSEP3SFT1(2).png" style="width: 307px; height: 264px;" /></p><p>Parametric form of parabola is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>a</mi><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>a</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>P</mi><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>6</mn><mi>t</mi></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>0</mn></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>3</mn><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Q</mi><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>,</mo><mn>3</mn><mi>t</mi></mrow></mfenced></math></p><p>Equation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mi>Q</mi></math>:  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mn>0</mn><mo>=</mo><mfenced><mfrac><mrow><mn>3</mn><mi>t</mi><mo>-</mo><mn>0</mn></mrow><mstyle displaystyle="true"><mfrac><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>-</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mstyle></mfrac></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></math></p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>t</mi></mrow></mfrac><mo>&#183;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mrow><mn>3</mn><mi>t</mi></mrow></mfrac><mo>&#183;</mo><mi>x</mi><mo>+</mo><mn>4</mn><mi>t</mi><mspace linebreak="newline"></mspace></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>t</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>N</mi><mo>=</mo><mn>6</mn><mi>t</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mi>Q</mi><mo>=</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mn>9</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p> </p>

</details>

---

### Q28. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area (in sq. units) of an equilateral triangle inscribed in the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>,</mo></math> with one of its vertices on the vertex of this parabola is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>256</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>192</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>128</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>192</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/51c72584-b035-4bfb-973c-9415b48e7b59-image.png" style="width: 262px; height: 223px;" /> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>x</mi><mo>,</mo><mi>a</mi><mo>=</mo><mn>2</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>2</mn><mo>(</mo><mn>2</mn><mo>)</mo><mi>t</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>4</mn><mi>t</mi></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mn>30</mn><mo>&#176;</mo><mo>=</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn><msup><mi mathvariant="normal">t</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mi mathvariant="normal">t</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math> </p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>OAB</mi><mo>=</mo><mn>2</mn><mo>&#183;</mo><mi>&#916;</mi><mi>OMA</mi><mo>=</mo><mn>2</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfenced><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mo>(</mo><mn>4</mn><mi mathvariant="normal">t</mi><mo>)</mo><mo>=</mo><mn>8</mn><msup><mi>t</mi><mn>3</mn></msup><mo>=</mo><mn>8</mn><mo>(</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><msup><mo>)</mo><mn>3</mn></msup><mo>=</mo><mn>192</mn><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q29. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced separators="|"><mrow><mn>9</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> be two points on the parabola, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi></math> and let <math><mi>X</mi></math> be any point on the arc <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>O</mi><mi>Q</mi></math> of this parabola, where <math><mi>O</mi></math> is the vertex of this parabola, such that the area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>P</mi><mi>X</mi><mi>Q</mi></math> is maximum. Then this maximum area (in sq. units) is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>625</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>75</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>125</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>125</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>125</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/07655107-5938-44bf-897f-5c59b36b5fb5-image.png" style="width: 280px; height: 231px;" /><p>Two different approaches we can use here.</p><p><b>Approach 1:</b></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>t</mi></mrow></mfenced></math>, then</p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mi>P</mi><mi>X</mi><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|" separators="|"><mtable><mtr><mtd><msup><mi>t</mi><mn>2</mn></msup></mtd><mtd><mn>2</mn><mi>t</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo><mn>10</mn><mfenced close="|" open="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>-</mo><mn>6</mn></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>For maxima, differentiating both the sides with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> and equating it to  zero, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#916;</mi><mi>&#8242;</mi></msup><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>5</mn><mfenced><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Hence, area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>P</mi><mi>X</mi><mi>Q</mi><mo>=</mo><mn>5</mn><mfenced close="|" open="|"><mrow><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>6</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mfenced close="|" open="|"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mn>6</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mo>-</mo><mn>24</mn></mrow><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>125</mn><mn>4</mn></mfrac></math> sq.units (using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>)</p><p><b>Approach 2:</b></p><p>For maximum area tangent to the parabola at <math><mi>X</mi></math> must be parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>t</mi></mrow></mfenced></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mi>y</mi></mfrac><mo>&#8658;</mo><msub><mfenced separators="|"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mfenced separators="|"><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>2</mn><mi>t</mi></mrow></mfenced></msub><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></math></p><p>Also, slope of line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mfrac><mrow><mn>6</mn><mo>+</mo><mn>4</mn></mrow><mrow><mn>9</mn><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mn>2</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p>Since, both the slopes are equal.</p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>X</mi><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math></p><p>Therefore, area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>P</mi><mi>X</mi><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>4</mn></mfrac></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mn>9</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>9</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="|" open="|"><mrow><mo>-</mo><mn>20</mn><mo>-</mo><mn>35</mn><mo>-</mo><mfrac><mn>15</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>125</mn><mn>4</mn></mfrac></math> sq.units.</p>

</details>

---

### Q30. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the area of the triangle whose one vertex is at the vertex of the parabola, $y^{2}+4\left(x-a^{2}\right)=0$ and the other two vertices are the points of intersection of the parabola and $y$ -axis, is 250 sq. units, then a value of 'a' is :

**Options:**

- **(A)** $5 \sqrt{5}$
- **(B)** $5\left(2^{1 / 3}\right)$
- **(C)** $(10)^{33}$
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

$y^{t}=-4\left(x-a^{2}\right)$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0pFWq6xYy6euRwfWHifO2c-ZqETw7H3Bt9DZMpw2PCI.original.fullsize.png">


$\mathrm{Area}=\frac{1}{2}(4 a)\left(a^{2}\right)=2 a^{3}$

Since $2 a^{3}=250 \Rightarrow a=5$

</details>

---

### Q31. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>A</mi><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced separators="|"><mrow><mn>9</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> be points on the parabola, <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn><mi>x</mi><mo>.</mo></math> Let <math><mi>C</mi></math> be chosen on the arc <math><mi>A</mi><mi>O</mi><mi>B</mi></math> of the parabola, where <math><mi>O</mi></math> is the origin, such that the area of <math><mi mathvariant="normal">&#916;</mi><mi>A</mi><mi>C</mi><mi>B</mi></math> is maximum. Then, the area (in sq. units) of <math><mi mathvariant="normal">&#916;</mi><mi>A</mi><mi>C</mi><mi>B</mi></math> , is:

**Options:**

- **(A)** <math><mn>32</mn></math>
- **(B)** <math><mn>31</mn><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi> </mi></math>
- **(C)** <math><mn>30</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mn>31</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>31</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let the coordinates of <math><mi>C</mi></math> be <math><mfenced separators="|"><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>,</mo><mi>&#160;</mi><mn>2</mn><mi>t</mi></mrow></mfenced></math>.

Area of <math><mo>&#8710;</mo><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>2</mn><mi>t</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fxxbaheoukaahekknvirjtznwxhovcyerjqkiutjvxiatyvuff.png" />

<math><mo>&#8710;</mo><mo>=</mo><mn>5</mn><mfenced close="|" open="|" separators="|"><mrow><mfenced separators="|"><mrow><mn>6</mn><mo>+</mo><mi>t</mi><mo>-</mo><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfenced><mo>,</mo></math> <math><mi>t</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn></mrow></mfenced></math>

<math><mfrac><mrow><mi>d</mi><mo>&#8710;</mo></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>t</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mo>&#9651;</mo></mrow><mrow><mi>d</mi><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math>, hence area is maximum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msub><mrow><mi mathvariant="normal">&#916;</mi></mrow><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>125</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mn>31</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math></p>

</details>

---

### Q32. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Axis of a parabola lies along <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis. If its vertex and focus are at distances <math><mn>2</mn></math> and <math><mn>4</mn></math> respectively from the origin, on the positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis then which of following points does not lie on it?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>6</mn><mo>,</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>5</mn><mo>,</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>8</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mo>-</mo><mn>4</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>8</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/349c74d7-e331-4ba8-ad0d-ca8257f0b0b8-image.png" style="width: 305px; height: 250px;" />
Clearly vertex is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> and focus is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn></math> .</p><p>Hence, the equation of parabola is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>2</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>8</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math> does not lie on the parabola.</p>

</details>

---

### Q33. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Two parabolas with a common vertex and with axes along the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis respectively, intersect each other in the first quadrant. If the length of the latus rectum of each parabola is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, then the equation of the common tangent to the two parabolas is :

**Options:**

- **(A)** <math><mi> </mi><mn>3</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math><mn>8</mn><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math><mn>4</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>4</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Equation of two parabola are <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>y</mi></math>.</p><p>Let equation of tangent to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>m</mi><mi>x</mi><mo>+</mo><mfrac><mn>3</mn><mrow><mn>4</mn><mi>m</mi></mrow></mfrac></math> is also tangent to <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>3</mn><mi>y</mi></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>3</mn><mi>m</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn><mi>m</mi></mrow></mfrac></math></p><p><math><mo>&#8658;</mo><mn>4</mn><mi>m</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>12</mn><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>-</mo><mn>9</mn><mo>=</mo><mn>0</mn></math> have equal roots</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>D</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>144</mn><msup><mi>m</mi><mn>4</mn></msup><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mn>4</mn><mi>m</mi></mrow></mfenced><mo>(</mo><mo>-</mo><mn>9</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>m</mi><mn>4</mn></msup><mo>+</mo><mi>m</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Hence, common tangent is <math><mi>y</mi><mo>=</mo><mo>-</mo><mi>x</mi><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q34. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> be a double ordinate of the parabola, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> lies in the second quadrant. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#160;</mo></math>divides <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math> in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn><mo>,</mo></math> then the locus of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>x</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fca2a67b-66a5-4409-87d5-19b8c44d5873-image.png" style="width: 221px; height: 200px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mn>2</mn><mi>t</mi></mrow></mfenced><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>Q</mi><mfenced><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mo>-</mo><mn>2</mn><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> divides in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mo>-</mo><mn>4</mn><mi>t</mi><mo>+</mo><mn>2</mn><mi>t</mi></mrow><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>t</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>t</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>9</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi></math></p>

</details>

---

### Q35. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi></math> be the vertex and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> be any point on the parabola, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>y</mi></math>. If the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> divides the line segment <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>Q</mi></math> internally in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>3</mn></math>, then the locus of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>y</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>x</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi></math>**

**Detailed Solution:**

General point on <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>8</mn><mi>y</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mfenced><mrow><mn>4</mn><mi>t</mi><mo>,</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></math><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced></math> divide <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>Q</mi></math> in ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>h</mi><mo>,</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mfenced separators="|"><mrow><mn>4</mn><mi>t</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mn>0</mn></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mfenced separators="|"><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>3</mn><mfenced><mn>0</mn></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo mathvariant="italic">h</mo><mo>,</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>t</mi><mi>,</mi><mfrac><mrow><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mi>t</mi><mo>&#160;&#38;&#160;</mo><mi>k</mi><mo>=</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mfrac><msup><mi>h</mi><mn>2</mn></msup><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>y</mi></math>  is the required locus. </p>

</details>

---

### Q36. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The area of triangle formed by the lines joining the vertex of the parabola, $x^2=8 y$, to the extremities of its latus rectum is

**Options:**

- **(A)** 2
- **(B)** 8
- **(C)** 1
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

Given parabola is $\mathrm{x}^2=8 \mathrm{y}$ $\Rightarrow 4 a=8 \Rightarrow a=2$
To find: Area of $\triangle A B C$
$$
\begin{aligned}
& A=(-2 a, a)=(-4,2) \\
& B=(2 a, a)=(4,2) \\
& \mathrm{C}=(0,0)
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Yz2Uv0WUGVOfGSeCURexp3HcJM5gWCWgpQGyQKo-Urs.original.fullsize.png">

$$
\begin{aligned}
& \therefore \text { Area }=\frac{1}{2}\left|\begin{array}{ccc}
-4 & 2 & 1 \\
4 & 2 & 1 \\
0 & 0 & 1
\end{array}\right| \\
& =\frac{1}{2}[-4(2)-2(4)+1(0)] \\
& =\frac{-16}{2}=-8 \approx 8 \text { sq. unit } \\
& (\because \text { area cannot be negative })
\end{aligned}
$$

</details>

---

### Q37. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

A parabola has the origin as its focus and the line $x=2$ as the directrix. Then the vertex of the parabola is at

**Options:**

- **(A)** $(0,2)$
- **(B)** $(1,0)$
- **(C)** $(0,1)$
- **(D)** $(2,0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(1,0)$**

**Detailed Solution:**

Vertex is $(1,0)$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qWYnBhCfjXbClRkPR9uq6cV0yscSbPmq4Oy5TemvFZM.original.fullsize.png">

</details>

---

### Q38. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

Let $P$ be the point $(1,0)$ and $Q$ a point on the locus $y^2=8 x$. The locus of mid point of $P Q$ is

**Options:**

- **(A)** $y^2-4 x+2=0$
- **(B)** $y^2+4 x+2=0$
- **(C)** $x^2+4 y+2=0$
- **(D)** $x^2-4 y+2=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y^2-4 x+2=0$**

**Detailed Solution:**

$\mathrm{P}=(1,0)$
$Q=(h, k)$ such that $k^2=8 h$
Let $(\alpha, \beta)$ be the midpoint of PQ
$$
\begin{aligned}
& \alpha=\frac{\mathrm{h}+1}{2}, \quad \beta=\frac{\mathrm{k}+0}{2} \\
& 2 \alpha-1=\mathrm{h}, \quad 2 \beta=\mathrm{k} . \\
& (2 \beta)^2=8(2 \alpha-1) \Rightarrow \beta^2=4 \alpha-2 \\
& \Rightarrow \mathrm{y}^2-4 \mathrm{x}+2=0 .
\end{aligned}
$$

</details>

---

