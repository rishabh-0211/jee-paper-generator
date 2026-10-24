# MHT CET Mathematics - Linear Programming

## Topic 1: Linear Programming

**Total Questions:** 113

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The correct constraints for the given feasible region are ...

<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/20_may_shift_1__q130_d1.png" />

**Options:**

- **(A)** $x + 2y - 2 \geq 0, 3x + 5y - 15 \geq 0, 2x - 3y + 6 \geq 0, x \geq 0, y \geq 0$
- **(B)** $x + 2y - 2 \leq 0, 3x + 5y - 15 \leq 0, 2x - 3y + 6 \leq 0, x \geq 0, y \geq 0$
- **(C)** $x + 2y - 2 \leq 0, 3x + 5y - 15 \geq 0, 2x - 3y + 6 \geq 0, x \geq 0, y \geq 0$
- **(D)** $x + 2y - 2 \geq 0, 3x + 5y - 15 \leq 0, 2x - 3y + 6 \geq 0, x \geq 0, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x + 2y - 2 \geq 0, 3x + 5y - 15 \leq 0, 2x - 3y + 6 \geq 0, x \geq 0, y \geq 0$**

**Detailed Solution:**

The equation of line $L_1$ passing through $(2, 0)$ and $(0, 1)$ is:
$\dfrac{x}{2} + \dfrac{y}{1} = 1 \Rightarrow x + 2y - 2 = 0$
The shaded region lies above $L_1$ (away from the origin), so the constraint is $x + 2y - 2 \geq 0$.

The equation of line $L_2$ passing through $(5, 0)$ and $(0, 3)$ is:
$\dfrac{x}{5} + \dfrac{y}{3} = 1 \Rightarrow 3x + 5y - 15 = 0$
The shaded region lies below $L_2$ (towards the origin), so the constraint is $3x + 5y - 15 \leq 0$.

The equation of line $L_3$ passing through $(-3, 0)$ and $(0, 2)$ is:
$\dfrac{x}{-3} + \dfrac{y}{2} = 1 \Rightarrow -2x + 3y = 6 \Rightarrow 2x - 3y + 6 = 0$
The shaded region lies below $L_3$ (towards the origin), so the constraint is $2x - 3y + 6 \geq 0$.

Since the shaded region is restricted to the first quadrant, we also have the non-negativity constraints $x \geq 0$ and $y \geq 0$.

Combining all these, the correct system of constraints is:
$x + 2y - 2 \geq 0, 3x + 5y - 15 \leq 0, 2x - 3y + 6 \geq 0, x \geq 0, y \geq 0$.

Answer: $x + 2y - 2 \geq 0, 3x + 5y - 15 \leq 0, 2x - 3y + 6 \geq 0, x \geq 0, y \geq 0$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $Z = 4x + 6y$, subject to constraint $x + 2y \geq 80, 3x + y \geq 75, x \geq 0, y \geq 0$ is:

**Options:**

- **(A)** $320$
- **(B)** $450$
- **(C)** $254$
- **(D)** $180$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $254$**

**Detailed Solution:**

The given constraints are $x + 2y \geq 80$, $3x + y \geq 75$, $x \geq 0$, $y \geq 0$.

The corner points of the feasible region are the intersection points of the boundary lines with each other and with the axes.

Solving $x + 2y = 80$ and $3x + y = 75$:

Multiplying the second equation by $2$, we get $6x + 2y = 150$.

Subtracting the first equation from this gives $5x = 70 \Rightarrow x = 14$.

Substituting $x = 14$ in the first equation gives $14 + 2y = 80 \Rightarrow 2y = 66 \Rightarrow y = 33$.

The corner points of the unbounded feasible region are $(0, 75)$, $(14, 33)$, and $(80, 0)$.

Evaluating $Z = 4x + 6y$ at these corner points:

At $(0, 75)$, $Z = 4(0) + 6(75) = 450$

At $(14, 33)$, $Z = 4(14) + 6(33) = 56 + 198 = 254$

At $(80, 0)$, $Z = 4(80) + 6(0) = 320$

The minimum value of $Z$ is $254$.

Answer: $254$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The linear programming problem:
Maximize : $Z = x + y$
Subject to :
$x + 2y \leq 200,\,x + y \leq 150,\,0 \leq y \leq 60,\,x \geq 0$ has:

**Options:**

- **(A)** a finite number of optimal solutions
- **(B)** a unique optimal solution
- **(C)** infinite number of optimal solutions
- **(D)** no feasible solution

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) infinite number of optimal solutions**

**Detailed Solution:**

The given constraints are $x + 2y \leq 200$, $x + y \leq 150$, $0 \leq y \leq 60$, and $x \geq 0$.

To find the feasible region, we determine the corner points by finding the intersections of the boundary lines:
1) Intersection of $x + y = 150$ and $y = 0$ gives $(150, 0)$.
2) Intersection of $x + 2y = 200$ and $x + y = 150$ gives $(100, 50)$.
3) Intersection of $x + 2y = 200$ and $y = 60$ gives $(80, 60)$.
4) Intersection of $x = 0$ and $y = 60$ gives $(0, 60)$.
5) Intersection of $x = 0$ and $y = 0$ gives $(0, 0)$.

All these points satisfy all the given constraints, so they are the corner points of the feasible region.

Now, we evaluate the objective function $Z = x + y$ at each corner point:
At $(0, 0)$, $Z = 0 + 0 = 0$
At $(150, 0)$, $Z = 150 + 0 = 150$
At $(100, 50)$, $Z = 100 + 50 = 150$
At $(80, 60)$, $Z = 80 + 60 = 140$
At $(0, 60)$, $Z = 0 + 60 = 60$

The maximum value of $Z$ is $150$, which occurs at two adjacent corner points, $(150, 0)$ and $(100, 50)$.

Since the maximum value occurs at two distinct corner points, it will also occur at every point on the line segment joining these two points. Because a line segment contains an infinite number of points, the linear programming problem has an infinite number of optimal solutions.

Answer: infinite number of optimal solutions

</details>

---

### Q4. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The L.P.P. Maximize $Z = 0.75x + 0.5y$ subject to $3x + 2y \leq 6$, $x + 4y \leq 4$, $x \geq 0$, $y \geq 0$ has

**Options:**

- **(A)** unique solution
- **(B)** no solution
- **(C)** two solutions
- **(D)** infinite solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) infinite solutions**

**Detailed Solution:**

The given linear programming problem is to maximize $Z = 0.75x + 0.5y$ subject to the constraints:
$3x + 2y \leq 6$
$x + 4y \leq 4$
$x \geq 0, y \geq 0$

First, we find the corner points of the feasible region by solving the equations of the boundary lines.
The x-intercepts of the lines $3x + 2y = 6$ and $x + 4y = 4$ are $x = 2$ and $x = 4$ respectively. The valid corner point on the x-axis is $(2, 0)$.
The y-intercepts of the lines are $y = 3$ and $y = 1$ respectively. The valid corner point on the y-axis is $(0, 1)$.

To find the intersection of $3x + 2y = 6$ and $x + 4y = 4$, we substitute $x = 4 - 4y$ into the first equation:
$3(4 - 4y) + 2y = 6$
$12 - 12y + 2y = 6$
$10y = 6 \Rightarrow y = 0.6$
$x = 4 - 4(0.6) = 1.6$
So, the intersection point is $(1.6, 0.6)$.

The corner points of the feasible region are $(0, 0)$, $(2, 0)$, $(1.6, 0.6)$, and $(0, 1)$.

Now, we evaluate the objective function $Z = 0.75x + 0.5y$ at each corner point:
At $(0, 0)$: $Z = 0.75(0) + 0.5(0) = 0$
At $(2, 0)$: $Z = 0.75(2) + 0.5(0) = 1.5$
At $(1.6, 0.6)$: $Z = 0.75(1.6) + 0.5(0.6) = 1.2 + 0.3 = 1.5$
At $(0, 1)$: $Z = 0.75(0) + 0.5(1) = 0.5$

The maximum value of $Z$ is $1.5$, which occurs at two adjacent corner points, $(2, 0)$ and $(1.6, 0.6)$.

Since the maximum value is attained at two distinct corner points, it will also be attained at all points on the line segment joining these two points. Therefore, the problem has infinite solutions.

Answer: infinite solutions

</details>

---

### Q5. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The point at which the maximum value of $3x + 2y$ subject to the constraints $x + y \leq 2, x \geq 0, y \geq 0$ is obtained is

**Options:**

- **(A)** $(0, 0)$
- **(B)** $(1.5, 1.5)$
- **(C)** $(2, 0)$
- **(D)** $(0, 2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(2, 0)$**

**Detailed Solution:**

The objective function to be maximized is $Z = 3x + 2y$.

The given constraints are $x + y \leq 2$, $x \geq 0$, and $y \geq 0$.

The feasible region is bounded by the lines $x + y = 2$, $x = 0$, and $y = 0$. The corner points of this feasible region are $(0, 0)$, $(2, 0)$, and $(0, 2)$.

Evaluating the objective function $Z$ at each corner point:

At $(0, 0)$, $Z = 3(0) + 2(0) = 0$

At $(2, 0)$, $Z = 3(2) + 2(0) = 6$

At $(0, 2)$, $Z = 3(0) + 2(2) = 4$

The maximum value of $Z$ is $6$, which is obtained at the point $(2, 0)$.

Answer: $(2, 0)$

</details>

---

### Q6. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $z = 5x + 8y$ subject to the constraints $0 \leq x \leq 4,\ 0 \leq y \leq 2,\ x + y \geq 5$ is

**Options:**

- **(A)** $28$
- **(B)** $30$
- **(C)** $31$
- **(D)** $24$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $28$**

**Detailed Solution:**

The given constraints are $0 \leq x \leq 4$, $0 \leq y \leq 2$, and $x + y \geq 5$.

The feasible region is bounded by the lines $x = 4$, $y = 2$, and $x + y = 5$.

The vertices of the feasible region are obtained by solving the equations of the boundary lines pairwise:

Solving $x = 4$ and $x + y = 5$, we get the point $(4, 1)$.

Solving $y = 2$ and $x + y = 5$, we get the point $(3, 2)$.

Solving $x = 4$ and $y = 2$, we get the point $(4, 2)$.

Evaluating the objective function $z = 5x + 8y$ at these vertices:

At $(4, 1)$, $z = 5(4) + 8(1) = 28$

At $(3, 2)$, $z = 5(3) + 8(2) = 31$

At $(4, 2)$, $z = 5(4) + 8(2) = 36$

The minimum value of $z$ is $28$.

Answer: $28$

</details>

---

### Q7. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $z = 4x + 2y$ subject to the constraints $3x + y \geq 27, x + y \geq 21, x + 2y \geq 30, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** $0$
- **(B)** $48$
- **(C)** $60$
- **(D)** $80$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $48$**

**Detailed Solution:**

The given constraints are:

$3x + y \geq 27$

$x + y \geq 21$

$x + 2y \geq 30$

$x \geq 0, y \geq 0$

The corner points of the feasible region are the intersections of the boundary lines and the axes. Let us find the relevant intersection points:

Solving $3x + y = 27$ and $x + y = 21$, we get $x = 3, y = 18$. The point is $(3, 18)$.

Solving $x + y = 21$ and $x + 2y = 30$, we get $x = 12, y = 9$. The point is $(12, 9)$.

The y-intercept of the feasible region is the maximum of the y-intercepts of the three lines, which is $(0, 27)$.

The x-intercept of the feasible region is the maximum of the x-intercepts of the three lines, which is $(30, 0)$.

Evaluating the objective function $z = 4x + 2y$ at these corner points:

At $(0, 27)$, $z = 4(0) + 2(27) = 54$

At $(3, 18)$, $z = 4(3) + 2(18) = 48$

At $(12, 9)$, $z = 4(12) + 2(9) = 66$

At $(30, 0)$, $z = 4(30) + 2(0) = 120$

Since the feasible region is unbounded, we verify if the open half-plane $4x + 2y < 48$ has any points in common with the feasible region. As $4x + 2y < 48 \Rightarrow 2x + y < 24$, and the minimum value occurs at the intersection of lines with slopes $-3$ and $-1$, the slope of the objective function ($-2$) lies between them, confirming that $48$ is indeed the global minimum.

The minimum value of $z$ is $48$.

Answer: $48$

</details>

---

### Q8. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $Z = 7x - 6y$ subject to $0 \leq x \leq 5$ and $0 \leq y \leq 3$ is...

**Options:**

- **(A)** $17$
- **(B)** $18$
- **(C)** $35$
- **(D)** $53$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $35$**

**Detailed Solution:**

The given objective function is $Z = 7x - 6y$.

The constraints are $0 \leq x \leq 5$ and $0 \leq y \leq 3$.

The feasible region is a rectangle with corner points $(0,0)$, $(5,0)$, $(5,3)$, and $(0,3)$.

Evaluating $Z$ at each corner point:
At $(0,0)$, $Z = 7(0) - 6(0) = 0$
At $(5,0)$, $Z = 7(5) - 6(0) = 35$
At $(5,3)$, $Z = 7(5) - 6(3) = 17$
At $(0,3)$, $Z = 7(0) - 6(3) = -18$

The maximum value of $Z$ is $35$.

Answer: $35$

</details>

---

### Q9. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The minimum and maximum values of the objective function $Z = 3x + 9y$, subject to $x + 3y \leq 60, x + y \geq 10, x \leq y, x \geq 0, y \geq 0$ are respectively...

**Options:**

- **(A)** $90$ and $190$
- **(B)** $60$ and $180$
- **(C)** $30$ and $120$
- **(D)** $40$ and $220$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $60$ and $180$**

**Detailed Solution:**

The feasible region is determined by the constraints $x + 3y \leq 60$, $x + y \geq 10$, $x \leq y$, $x \geq 0$, and $y \geq 0$.

The corner points of the bounded feasible region are obtained by finding the intersection points of the corresponding lines:
Intersection of $x + y = 10$ and $x = y$ gives $(5, 5)$.
Intersection of $x + 3y = 60$ and $x = y$ gives $(15, 15)$.
Intersection of $x + y = 10$ and $x = 0$ gives $(0, 10)$.
Intersection of $x + 3y = 60$ and $x = 0$ gives $(0, 20)$.

Evaluating the objective function $Z = 3x + 9y$ at these corner points:
At $(5, 5)$, $Z = 3(5) + 9(5) = 15 + 45 = 60$
At $(15, 15)$, $Z = 3(15) + 9(15) = 45 + 135 = 180$
At $(0, 10)$, $Z = 3(0) + 9(10) = 0 + 90 = 90$
At $(0, 20)$, $Z = 3(0) + 9(20) = 0 + 180 = 180$

The minimum value of $Z$ is $60$ and the maximum value of $Z$ is $180$.

Answer: $60$ and $180$

</details>

---

### Q10. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A company sells two types of notebooks, A and B. Each notebook requires two processes: printing and binding. Notebook A requires $2$ minutes for printing and $1$ minute for binding. Notebook B requires $4$ minutes for printing and $2$ minutes for binding. The company can spend $6$ hours on printing and $2$ hours on binding. If the profit made on notebooks A and B is Rs. $2$ and Rs. $5$ respectively, then the Linear Programming Problem (LPP) to maximize the total profit $z$ is ...

**Options:**

- **(A)** maximize $z=2x+5y$ subject to $2x+y\leq 360, 4x+2y\leq 120, x\geq 0, y\geq 0$
- **(B)** maximize $z=2x+5y$ subject to $2x+y\leq 120, 4x+2y\leq 360, x\geq 0, y\geq 0$
- **(C)** maximize $z=2x+5y$ subject to $2x+4y\leq 360, x+2y\leq 120, x\geq 0, y\geq 0$
- **(D)** maximize $z=2x+5y$ subject to $2x+4y\leq 120, x+2y\leq 360, x\geq 0, y\geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) maximize $z=2x+5y$ subject to $2x+4y\leq 360, x+2y\leq 120, x\geq 0, y\geq 0$**

**Detailed Solution:**

Let $x$ be the number of notebooks of type A and $y$ be the number of notebooks of type B.

The objective is to maximize the total profit $z$. Since the profit on notebook A is Rs. $2$ and on notebook B is Rs. $5$, the objective function is:

Maximize $z = 2x + 5y$

The time required for printing notebook A is $2$ minutes and for notebook B is $4$ minutes. The maximum time available for printing is $6$ hours, which is $6 \times 60 = 360$ minutes. This gives the printing constraint:

$2x + 4y \leq 360$

The time required for binding notebook A is $1$ minute and for notebook B is $2$ minutes. The maximum time available for binding is $2$ hours, which is $2 \times 60 = 120$ minutes. This gives the binding constraint:

$x + 2y \leq 120$

Since the number of notebooks cannot be negative, we have the non-negativity constraints:

$x \geq 0, y \geq 0$

Combining all these, the LPP is to maximize $z = 2x + 5y$ subject to $2x + 4y \leq 360$, $x + 2y \leq 120$, $x \geq 0$, $y \geq 0$.

Answer: maximize $z=2x+5y$ subject to $2x+4y\leq 360, x+2y\leq 120, x\geq 0, y\geq 0$

</details>

---

### Q11. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The LPP maximize $z = 2x + 5y$ subject to $x + 3y \leq 6$, $2x + 6y \leq 18$, $x \geq 0$, $y \geq 0$ has

**Options:**

- **(A)** Unique solution
- **(B)** Infinite solutions
- **(C)** No solution
- **(D)** Unbounded feasible region

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Unique solution**

**Detailed Solution:**

The given constraints are:
$x + 3y \leq 6$
$2x + 6y \leq 18 \Rightarrow x + 3y \leq 9$
$x \geq 0, y \geq 0$

The second constraint $x + 3y \leq 9$ is redundant since $x + 3y \leq 6$ is a stricter condition. The feasible region is bounded by $x + 3y \leq 6$ in the first quadrant, which forms a triangle.

The vertices of the feasible region are $(0,0)$, $(6,0)$, and $(0,2)$.

Evaluating the objective function $z = 2x + 5y$ at these vertices:
At $(0,0)$, $z = 2(0) + 5(0) = 0$
At $(6,0)$, $z = 2(6) + 5(0) = 12$
At $(0,2)$, $z = 2(0) + 5(2) = 10$

The maximum value of $z$ is $12$, which occurs exactly at one vertex $(6,0)$.

Therefore, the LPP has a unique solution.

Answer: Unique solution

</details>

---

### Q12. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The difference between the maximum value and the minimum value of the objective function $z = 3x + y$ subject to the constraints $2x + 3y \leq 6$, $x + y \geq 1$, $x \geq 0$, $y \geq 0$ is....

**Options:**

- **(A)** $7$
- **(B)** $3$
- **(C)** $8$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8$**

**Detailed Solution:**

The given objective function is $z = 3x + y$.

The constraints are $2x + 3y \leq 6$, $x + y \geq 1$, $x \geq 0$, and $y \geq 0$.

The feasible region is bounded by the lines $2x + 3y = 6$, $x + y = 1$, $x = 0$, and $y = 0$. The corner points of this feasible region can be found by finding the intersections of these lines with the coordinate axes.

For $2x + 3y = 6$, the intercepts are $(3, 0)$ and $(0, 2)$.
For $x + y = 1$, the intercepts are $(1, 0)$ and $(0, 1)$.

The corner points of the bounded feasible region are $(1, 0)$, $(3, 0)$, $(0, 2)$, and $(0, 1)$.

Evaluating the objective function $z = 3x + y$ at these corner points:
At $(1, 0)$, $z = 3(1) + 0 = 3$
At $(3, 0)$, $z = 3(3) + 0 = 9$
At $(0, 2)$, $z = 3(0) + 2 = 2$
At $(0, 1)$, $z = 3(0) + 1 = 1$

The maximum value of $z$ is $9$ and the minimum value is $1$.

The difference between the maximum and minimum values is $9 - 1 = 8$.

Answer: $8$

</details>

---

### Q13. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An airplane can carry a maximum of $250$ passengers. A profit of Rs $1500$ is made on each executive class ticket and a profit of Rs $900$ is made on each economy class ticket. The airline reserves at least $30$ seats for executive class. However at least $4$ times as many passengers prefer to travel by economy class than by executive class. Let $x_1$ be the number of passengers of executive class and $x_2$ be the number of passengers of economy class. Formulate the LPP in order to maximize the profit for the airline...

**Options:**

- **(A)** Maximize $z = 1500x_1 + 900x_2$ subject to $x_1 + x_2 \leq 250$, $x_1 \leq 30$, $x_2 \leq 4x_1$, $x_1 \geq 0, x_2 \geq 0$.
- **(B)** Minimize $z = 150x_1 + 90x_2$ subject to $x_1 + x_2 \leq 250$, $x_1 \geq 30$, $x_2 \geq 4x_1$, $x_1 \geq 0, x_2 \geq 0$.
- **(C)** Minimize $z = 1500x_1 + 900x_2$ subject to $x_1 + x_2 \leq 250$, $x_1 \geq 30$, $x_2 \geq 4x_1$, $x_1 \geq 0, x_2 \geq 0$.
- **(D)** Maximize $z = 1500x_1 + 900x_2$ subject to $x_1 + x_2 \leq 250$, $x_1 \geq 30$, $x_2 \geq 4x_1$, $x_1 \geq 0, x_2 \geq 0$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Maximize $z = 1500x_1 + 900x_2$ subject to $x_1 + x_2 \leq 250$, $x_1 \geq 30$, $x_2 \geq 4x_1$, $x_1 \geq 0, x_2 \geq 0$.**

**Detailed Solution:**

Let $x_1$ be the number of executive class passengers and $x_2$ be the number of economy class passengers.

The profit on each executive class ticket is Rs $1500$ and on each economy class ticket is Rs $900$. The objective is to maximize the total profit $z$, which is given by:
Maximize $z = 1500x_1 + 900x_2$

The airplane can carry a maximum of $250$ passengers, which gives the constraint:
$x_1 + x_2 \leq 250$

The airline reserves at least $30$ seats for executive class, which gives:
$x_1 \geq 30$

At least $4$ times as many passengers prefer to travel by economy class than by executive class, which gives:
$x_2 \geq 4x_1$

Since the number of passengers cannot be negative, we have the non-negativity constraints:
$x_1 \geq 0, x_2 \geq 0$

Combining all these, the Linear Programming Problem is formulated as:
Maximize $z = 1500x_1 + 900x_2$ subject to $x_1 + x_2 \leq 250$, $x_1 \geq 30$, $x_2 \geq 4x_1$, $x_1 \geq 0, x_2 \geq 0$.

Answer: Maximize $z = 1500x_1 + 900x_2$ subject to $x_1 + x_2 \leq 250$, $x_1 \geq 30$, $x_2 \geq 4x_1$, $x_1 \geq 0, x_2 \geq 0$.

</details>

---

### Q14. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The shaded region in the provided graph represents the solution set for which of the following systems of linear inequalities?
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_1__q130_d1.png" />

**Options:**

- **(A)** $2x + y \geq 2,\ x - y \geq 1,\ x + 2y \leq 8,\ x \geq 0,\ y \geq 0$
- **(B)** $x + 2y \geq 2,\ x - y \geq 1,\ x + 2y \leq 8,\ x \geq 0,\ y \geq 0$
- **(C)** $2x + y \geq 2,\ x - y \leq 1,\ x + 2y \leq 8,\ x \geq 0,\ y \geq 0$
- **(D)** $2x + y \geq 2,\ x - y \leq 1,\ 2x + y \leq 8,\ x \geq 0,\ y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2x + y \geq 2,\ x - y \leq 1,\ x + 2y \leq 8,\ x \geq 0,\ y \geq 0$**

**Detailed Solution:**

The equations of the lines forming the boundaries of the shaded region are determined as follows.

The line passing through the points $E(0, 2)$ and $A(1, 0)$ has the equation $\dfrac{x}{1} + \dfrac{y}{2} = 1$, which simplifies to $2x + y = 2$. The shaded region lies away from the origin relative to this line. Testing a point inside the region, such as $(1, 2)$, gives $2(1) + 2 = 4 \geq 2$. Thus, the corresponding inequality is $2x + y \geq 2$.

The line passing through the points $D(0, 4)$ and $B\left(\dfrac{10}{3}, \dfrac{7}{3}\right)$ has a slope $m = \dfrac{\dfrac{7}{3} - 4}{\dfrac{10}{3} - 0} = -\dfrac{1}{2}$. Its equation is $y - 4 = -\dfrac{1}{2}(x - 0)$, which simplifies to $x + 2y = 8$. The shaded region lies towards the origin relative to this line. Testing the point $(1, 2)$ gives $1 + 2(2) = 5 \leq 8$. Thus, the corresponding inequality is $x + 2y \leq 8$.

The line passing through the points $A(1, 0)$ and $B\left(\dfrac{10}{3}, \dfrac{7}{3}\right)$ has a slope $m = \dfrac{\dfrac{7}{3} - 0}{\dfrac{10}{3} - 1} = 1$. Its equation is $y - 0 = 1(x - 1)$, which simplifies to $x - y = 1$. The shaded region lies towards the origin relative to this line. Testing the point $(1, 2)$ gives $1 - 2 = -1 \leq 1$. Thus, the corresponding inequality is $x - y \leq 1$.

The shaded region is bounded by the y-axis on the left, which means $x \geq 0$. It also lies entirely in the first quadrant, so $y \geq 0$.

Combining all these conditions, the system of linear inequalities is $2x + y \geq 2$, $x - y \leq 1$, $x + 2y \leq 8$, $x \geq 0$, $y \geq 0$.

Answer: $2x + y \geq 2,\ x - y \leq 1,\ x + 2y \leq 8,\ x \geq 0,\ y \geq 0$

</details>

---

### Q15. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of $z = 4x + y$ subject to the constraints $x + y \leq 5, 2x + y \leq 7, 3x + 2y \leq 11, x \geq 0, y \geq 0$ is $\ldots$

**Options:**

- **(A)** $13$
- **(B)** $8$
- **(C)** $11$
- **(D)** $14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $14$**

**Detailed Solution:**

The given constraints are:
$x + y \leq 5$
$2x + y \leq 7$
$3x + 2y \leq 11$
$x \geq 0, y \geq 0$

To find the corner points of the feasible region, we determine the intersection points of the boundary lines with each other and with the coordinate axes, and check if they satisfy all constraints.

1) Intersection of $2x + y = 7$ with the x-axis ($y = 0$) gives $x = 3.5$. The point is $(3.5, 0)$.
Checking in other constraints: $3.5 + 0 = 3.5 \leq 5$ (True), $3(3.5) + 0 = 10.5 \leq 11$ (True).

2) Intersection of $x + y = 5$ with the y-axis ($x = 0$) gives $y = 5$. The point is $(0, 5)$.
Checking in other constraints: $2(0) + 5 = 5 \leq 7$ (True), $3(0) + 2(5) = 10 \leq 11$ (True).

3) Intersection of $x + y = 5$ and $3x + 2y = 11$:
Multiplying the first equation by 2 gives $2x + 2y = 10$. Subtracting this from the second equation gives $x = 1$, and substituting back gives $y = 4$. The point is $(1, 4)$.
Checking in $2x + y \leq 7$: $2(1) + 4 = 6 \leq 7$ (True).

4) Intersection of $2x + y = 7$ and $3x + 2y = 11$:
Multiplying the first equation by 2 gives $4x + 2y = 14$. Subtracting the second equation gives $x = 3$, and substituting back gives $y = 1$. The point is $(3, 1)$.
Checking in $x + y \leq 5$: $3 + 1 = 4 \leq 5$ (True).

The corner points of the feasible region are $(0, 0)$, $(3.5, 0)$, $(3, 1)$, $(1, 4)$, and $(0, 5)$.

Evaluating the objective function $z = 4x + y$ at these corner points:
At $(0, 0)$, $z = 4(0) + 0 = 0$
At $(3.5, 0)$, $z = 4(3.5) + 0 = 14$
At $(3, 1)$, $z = 4(3) + 1 = 13$
At $(1, 4)$, $z = 4(1) + 4 = 8$
At $(0, 5)$, $z = 4(0) + 5 = 5$

The maximum value of $z$ is $14$.

Answer: $14$

</details>

---

### Q16. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of $Z = 4x + 5y$, subject to the constraints $3x + y \leq 15, 3x + 4y \leq 24, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** $31$
- **(B)** $30$
- **(C)** $42$
- **(D)** $47$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $31$**

**Detailed Solution:**

The given constraints are $3x + y \leq 15$, $3x + 4y \leq 24$, $x \geq 0$, $y \geq 0$.

To find the corner points of the feasible region, we solve the equations of the boundary lines:
$3x + y = 15$
$3x + 4y = 24$

Subtracting the first equation from the second gives:
$3y = 9 \Rightarrow y = 3$

Substituting $y = 3$ in the first equation:
$3x + 3 = 15 \Rightarrow 3x = 12 \Rightarrow x = 4$

The intersection point is $(4, 3)$.

The corner points of the feasible region are the origin $(0, 0)$, the valid x-intercept $(5, 0)$, the intersection point $(4, 3)$, and the valid y-intercept $(0, 6)$.

Evaluating the objective function $Z = 4x + 5y$ at these corner points:
At $(0, 0)$, $Z = 4(0) + 5(0) = 0$
At $(5, 0)$, $Z = 4(5) + 5(0) = 20$
At $(4, 3)$, $Z = 4(4) + 5(3) = 16 + 15 = 31$
At $(0, 6)$, $Z = 4(0) + 5(6) = 30$

The maximum value of $Z$ is $31$.

Answer: $31$

</details>

---

### Q17. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the following figure, the shaded region represents the system of constraints:
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_2__q130_d1.png" />

**Options:**

- **(A)** $2x + y \leq 12, x + 2y \leq 12, x + 1.25y \geq 5, x \leq 0, y \geq 0$
- **(B)** $2x + y \leq 12, x + 2y \leq 12, x + 1.25y \geq 5, x \geq 0, y \leq 0$
- **(C)** $2x + y \leq 12, x + 2y \leq 12, x + 1.25y \leq 5, x \geq 0, y \geq 0$
- **(D)** $2x + y \leq 12, x + 2y \leq 12, x + 1.25y \geq 5, x \geq 0, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2x + y \leq 12, x + 2y \leq 12, x + 1.25y \geq 5, x \geq 0, y \geq 0$**

**Detailed Solution:**

From the given graph, the shaded region is bounded by three given lines and the coordinate axes.

The shaded region lies below the line $x + 2y = 12$ (towards the origin), which gives the inequality $x + 2y \leq 12$.

The shaded region lies below the line $2x + y = 12$ (towards the origin), which gives the inequality $2x + y \leq 12$.

The shaded region lies above the line $x + 1.25y = 5$ (away from the origin), which gives the inequality $x + 1.25y \geq 5$.

Since the shaded region is in the first quadrant, the non-negativity constraints are $x \geq 0$ and $y \geq 0$.

Combining all these inequalities, the system of constraints is $2x + y \leq 12$, $x + 2y \leq 12$, $x + 1.25y \geq 5$, $x \geq 0$, $y \geq 0$.

Answer: $2x + y \leq 12, x + 2y \leq 12, x + 1.25y \geq 5, x \geq 0, y \geq 0$

</details>

---

### Q18. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the linear programming problem, $x + 2y \leq 10,\ 3x + y \leq 12,\ x, y \geq 0$, the maximum value of $z = 5x + 10y$ occurs at every point on the line segment joining the points..

**Options:**

- **(A)** $(0,0)$ and $(4,0)$
- **(B)** $(0,0)$ and $(0,5)$
- **(C)** $(4,0)$ and $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$
- **(D)** $(0,5)$ and $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(0,5)$ and $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$**

**Detailed Solution:**

The given constraints are:
$x + 2y \leq 10$
$3x + y \leq 12$
$x, y \geq 0$

To find the corner points of the feasible region, we solve the equations of the boundary lines:
$x + 2y = 10$
$3x + y = 12$

Multiplying the second equation by 2, we get $6x + 2y = 24$. Subtracting the first equation from this gives:
$5x = 14 \Rightarrow x = \dfrac{14}{5}$

Substituting $x$ back into the first equation:
$\dfrac{14}{5} + 2y = 10 \Rightarrow 2y = \dfrac{36}{5} \Rightarrow y = \dfrac{18}{5}$

The intersection point is $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$.

The corner points of the feasible region are $(0, 0)$, $(4, 0)$, $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$, and $(0, 5)$.

Now, we evaluate the objective function $z = 5x + 10y$ at each corner point:
At $(0, 0)$: $z = 5(0) + 10(0) = 0$
At $(4, 0)$: $z = 5(4) + 10(0) = 20$
At $(0, 5)$: $z = 5(0) + 10(5) = 50$
At $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$: $z = 5\left(\dfrac{14}{5}\right) + 10\left(\dfrac{18}{5}\right) = 14 + 36 = 50$

The maximum value of $z$ is $50$, which occurs at two adjacent corner points: $(0, 5)$ and $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$.

Since the maximum value is the same at these two points, it occurs at every point on the line segment joining $(0, 5)$ and $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$.

Answer: $(0,5)$ and $\left(\dfrac{14}{5}, \dfrac{18}{5}\right)$

</details>

---

### Q19. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The region satisfying the inequalities $y - x \geq 2,\ x + y \leq 5,\ x \geq 0$ and $y \geq 0$ is

**Options:**

- **(A)** <img style="width: 180px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q129_d2.png" />
- **(B)** <img style="width: 180px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q129_d3.png" />
- **(C)** <img style="width: 180px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q129_d4.png" />
- **(D)** <img style="width: 180px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q129_d5.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img style="width: 180px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q129_d2.png" />**

**Detailed Solution:**

The given inequalities are:
$y - x \geq 2$
$x + y \leq 5$
$x \geq 0$
$y \geq 0$

Let us plot the corresponding lines to find the bounded region:
1. The line $y - x = 2$ intersects the y-axis at $(0, 2)$ and the x-axis at $(-2, 0)$. The inequality $y - x \geq 2$ (or $y \geq x + 2$) represents the region above this line.
2. The line $x + y = 5$ intersects the y-axis at $(0, 5)$ and the x-axis at $(5, 0)$. The inequality $x + y \leq 5$ (or $y \leq -x + 5$) represents the region below this line.
3. $x \geq 0$ represents the region to the right of the y-axis.
4. $y \geq 0$ represents the region above the x-axis.

Finding the point of intersection of the two lines:
$y - x = 2$
$y + x = 5$
Adding the two equations, we get $2y = 7 \Rightarrow y = 3.5$.
Substituting $y$ in the second equation, $x = 1.5$.
The lines intersect at $(1.5, 3.5)$.

The region satisfying all these conditions is bounded by the y-axis ($x = 0$), the line $y - x = 2$, and the line $x + y = 5$.
This forms a triangular region with vertices at $(0, 2)$, $(0, 5)$, and $(1.5, 3.5)$.

Looking at the given options, the first image correctly shows this shaded triangular region resting on the y-axis between $y = 2$ and $y = 5$.

Answer: <img style="width: 180px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q129_d2.png" />

</details>

---

### Q20. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $z = 3x + 5y$, subject to constraints $x \leq 80$, $y \geq 60$, $x + y \leq 200$ & $x, y \geq 0$ occurs at the point...

**Options:**

- **(A)** $(0, 200)$
- **(B)** $(60, 0)$
- **(C)** $(0, 60)$
- **(D)** $(80, 60)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(0, 60)$**

**Detailed Solution:**

The given objective function is $z = 3x + 5y$.

The constraints are $x \leq 80$, $y \geq 60$, $x + y \leq 200$, $x \geq 0$, and $y \geq 0$.

The feasible region is a polygon bounded by the vertices $(0, 60)$, $(80, 60)$, $(80, 120)$, and $(0, 200)$.

Evaluating the objective function $z$ at each of these corner points:
At $(0, 60)$, $z = 3(0) + 5(60) = 300$
At $(80, 60)$, $z = 3(80) + 5(60) = 240 + 300 = 540$
At $(80, 120)$, $z = 3(80) + 5(120) = 240 + 600 = 840$
At $(0, 200)$, $z = 3(0) + 5(200) = 1000$

The minimum value of $z$ is $300$, which occurs at the point $(0, 60)$.

Answer: $(0, 60)$

</details>

---

### Q21. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The feasible region represented by the constraints $y - 2x \leq 4, x + y \geq 5, x \leq 4, y \geq 2, x, y \geq 0$ is ...........

**Options:**

- **(A)** a convex bounded region with 4 corner points
- **(B)** an unbounded region
- **(C)** a convex bounded region with 5 corner points
- **(D)** no feasible region

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a convex bounded region with 4 corner points**

**Detailed Solution:**

The given constraints are:
$y - 2x \leq 4$
$x + y \geq 5$
$x \leq 4$
$y \geq 2$
$x \geq 0, y \geq 0$

To find the corner points of the feasible region, we solve the boundary equations pairwise and check if the intersection points satisfy all other constraints.

1. Intersection of $y - 2x = 4$ and $x + y = 5$:
Substituting $y = 5 - x$ into the first equation:
$5 - x - 2x = 4 \Rightarrow 3x = 1 \Rightarrow x = \dfrac{1}{3}$
$y = 5 - \dfrac{1}{3} = \dfrac{14}{3}$
Point: $\left(\dfrac{1}{3}, \dfrac{14}{3}\right)$. This satisfies $x \leq 4$ and $y \geq 2$.

2. Intersection of $y - 2x = 4$ and $x = 4$:
$y - 2(4) = 4 \Rightarrow y = 12$
Point: $(4, 12)$. This satisfies $x + y = 16 \geq 5$ and $y \geq 2$.

3. Intersection of $x = 4$ and $y = 2$:
Point: $(4, 2)$. This satisfies $y - 2x = 2 - 8 = -6 \leq 4$ and $x + y = 6 \geq 5$.

4. Intersection of $y = 2$ and $x + y = 5$:
$x + 2 = 5 \Rightarrow x = 3$
Point: $(3, 2)$. This satisfies $y - 2x = 2 - 6 = -4 \leq 4$ and $x \leq 4$.

The constraints $x \geq 0$ and $y \geq 0$ do not form any additional boundary since the minimum values in the region are $x = \dfrac{1}{3}$ and $y = 2$.

The feasible region is bounded by these four points: $\left(\dfrac{1}{3}, \dfrac{14}{3}\right)$, $(4, 12)$, $(4, 2)$, and $(3, 2)$. Since it is formed by the intersection of linear inequalities (half-planes), it is a convex polygon.

Thus, the feasible region is a convex bounded region with 4 corner points.

Answer: a convex bounded region with 4 corner points

</details>

---

### Q22. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The difference between the maximum and minimum values of the objective function $Z = 3x + 5y$, subject to the constraints $x + 3y \leq 60$, $x + y \geq 10$, $x - y \leq 0$, $x, y \geq 0$ is

**Options:**

- **(A)** $50$
- **(B)** $60$
- **(C)** $70$
- **(D)** $80$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $80$**

**Detailed Solution:**

The feasible region is bounded by the lines $x + 3y = 60$, $x + y = 10$, $x = y$, and the y-axis ($x = 0$).

The corner points of the feasible region are obtained by solving the equations of the lines pairwise:
1. Intersection of $x = y$ and $x + y = 10$ gives $(5, 5)$.
2. Intersection of $x = y$ and $x + 3y = 60$ gives $(15, 15)$.
3. Intersection of $x = 0$ and $x + y = 10$ gives $(0, 10)$.
4. Intersection of $x = 0$ and $x + 3y = 60$ gives $(0, 20)$.

Evaluating the objective function $Z = 3x + 5y$ at these corner points:
At $(5, 5)$, $Z = 3(5) + 5(5) = 40$
At $(15, 15)$, $Z = 3(15) + 5(15) = 120$
At $(0, 10)$, $Z = 3(0) + 5(10) = 50$
At $(0, 20)$, $Z = 3(0) + 5(20) = 100$

The maximum value of $Z$ is $120$ and the minimum value is $40$.

The difference between the maximum and minimum values is $120 - 40 = 80$.

Answer: $80$

</details>

---

### Q23. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $Z = 3x + y$, subject to the constraints $2x + 3y \leq 6, x + y \geq 1, x \geq 0, y \geq 0$ is....

**Options:**

- **(A)** $5$
- **(B)** $2$
- **(C)** $1$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

The objective function is $Z = 3x + y$.

The given constraints are:
$2x + 3y \leq 6$
$x + y \geq 1$
$x \geq 0, y \geq 0$

The feasible region is bounded by the lines $2x + 3y = 6$, $x + y = 1$, $x = 0$, and $y = 0$.

The corner points of the feasible region are the intersections of these lines with the coordinate axes:
For $x + y = 1$, the intercepts are $(1, 0)$ and $(0, 1)$.
For $2x + 3y = 6$, the intercepts are $(3, 0)$ and $(0, 2)$.

Thus, the vertices of the feasible region are $(1, 0)$, $(3, 0)$, $(0, 2)$, and $(0, 1)$.

Evaluating $Z = 3x + y$ at each corner point:
At $(1, 0)$: $Z = 3(1) + 0 = 3$
At $(3, 0)$: $Z = 3(3) + 0 = 9$
At $(0, 2)$: $Z = 3(0) + 2 = 2$
At $(0, 1)$: $Z = 3(0) + 1 = 1$

The minimum value of $Z$ is $1$.

</details>

---

### Q24. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The difference between the maximum value and minimum value of the objective function $z = 3x + 5y$ of a linear programming problem subject to constraints $5x + 10y \leq 50$, $x + y \geq 1$, $y \leq 4$ and $x \geq 0, y \geq 0$ is $3\lambda$. Then the value of $\lambda$ is

**Options:**

- **(A)** $3$.
- **(B)** $6$.
- **(C)** $9$.
- **(D)** $27$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $9$.**

**Detailed Solution:**

The given constraints are:
$5x + 10y \leq 50 \Rightarrow x + 2y \leq 10$
$x + y \geq 1$
$y \leq 4$
$x \geq 0, y \geq 0$

The feasible region is bounded by the lines $x + 2y = 10$, $x + y = 1$, $y = 4$, $x = 0$, and $y = 0$. Let us find the corner points of this feasible region:
Intersection of $x = 0$ and $x + y = 1 \Rightarrow (0, 1)$
Intersection of $x = 0$ and $y = 4 \Rightarrow (0, 4)$
Intersection of $y = 4$ and $x + 2y = 10 \Rightarrow x + 8 = 10 \Rightarrow x = 2 \Rightarrow (2, 4)$
Intersection of $y = 0$ and $x + 2y = 10 \Rightarrow x = 10 \Rightarrow (10, 0)$
Intersection of $y = 0$ and $x + y = 1 \Rightarrow x = 1 \Rightarrow (1, 0)$

Now, we evaluate the objective function $z = 3x + 5y$ at each of these corner points:
At $(0, 1)$, $z = 3(0) + 5(1) = 5$
At $(0, 4)$, $z = 3(0) + 5(4) = 20$
At $(2, 4)$, $z = 3(2) + 5(4) = 26$
At $(10, 0)$, $z = 3(10) + 5(0) = 30$
At $(1, 0)$, $z = 3(1) + 5(0) = 3$

From the above values, the maximum value of $z$ is $30$ and the minimum value of $z$ is $3$.

The difference between the maximum and minimum values is:
$30 - 3 = 27$

Given that this difference is equal to $3\lambda$, we have:
$3\lambda = 27 \Rightarrow \lambda = 9$

Answer: $9$.

</details>

---

### Q25. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In L.P.P., the corner points of the feasible region for the constraints $3x - y \geq 6, x \leq 3, y \leq 2, y \geq 0, x \geq 0$ are .....

**Options:**

- **(A)** $(3, 2), (3, 0), (2, 0)$
- **(B)** $\left(\dfrac{8}{3}, 2\right), (3, 2), (3, 0), (2, 0)$
- **(C)** $(0, 0), (2, 0), \left(\dfrac{8}{3}, 2\right), (0, 2)$
- **(D)** $(3, 2), (0, 3), (0, 2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\dfrac{8}{3}, 2\right), (3, 2), (3, 0), (2, 0)$**

**Detailed Solution:**

The given constraints are $3x - y \geq 6$, $x \leq 3$, $y \leq 2$, $x \geq 0$, $y \geq 0$.

The boundary lines for the feasible region are $3x - y = 6$, $x = 3$, $y = 2$, $x = 0$, and $y = 0$.

Finding the intersection points of the line $3x - y = 6$ with the other boundary lines:
Intersection with $y = 0$: $3x - 0 = 6 \Rightarrow x = 2$. The point is $(2, 0)$.
Intersection with $y = 2$: $3x - 2 = 6 \Rightarrow 3x = 8 \Rightarrow x = \dfrac{8}{3}$. The point is $\left(\dfrac{8}{3}, 2\right)$.

The other corner points are formed by the intersection of the remaining boundary lines $x = 3$, $y = 2$, and $y = 0$ that satisfy $3x - y \geq 6$:
Intersection of $x = 3$ and $y = 0$ is $(3, 0)$.
Intersection of $x = 3$ and $y = 2$ is $(3, 2)$.

Checking these points against all constraints:
For $(2, 0)$: $3(2) - 0 = 6 \geq 6$, $2 \leq 3$, $0 \leq 2$. (Satisfies all)
For $\left(\dfrac{8}{3}, 2\right)$: $3\left(\dfrac{8}{3}\right) - 2 = 6 \geq 6$, $\dfrac{8}{3} \leq 3$, $2 \leq 2$. (Satisfies all)
For $(3, 2)$: $3(3) - 2 = 7 \geq 6$, $3 \leq 3$, $2 \leq 2$. (Satisfies all)
For $(3, 0)$: $3(3) - 0 = 9 \geq 6$, $3 \leq 3$, $0 \leq 2$. (Satisfies all)

Thus, the corner points of the feasible region are $\left(\dfrac{8}{3}, 2\right), (3, 2), (3, 0), (2, 0)$.

Answer: $\left(\dfrac{8}{3}, 2\right), (3, 2), (3, 0), (2, 0)$

</details>

---

### Q26. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The corner points of the feasible region determined by a system of linear constraints are $(0, 3), (1, 1)$ and $(3, 0)$. If the objective function is $z = px + qy$, where $p, q > 0$, then the condition on p and q such that the minimum of z occurs at both $(3, 0)$ and $(1, 1)$ is _____

**Options:**

- **(A)** $p = 3q$
- **(B)** $3p = q$
- **(C)** $p = \dfrac{q}{2}$
- **(D)** $p = 2q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $p = \dfrac{q}{2}$**

**Detailed Solution:**

The objective function is $z = px + qy$.

The value of $z$ at the corner point $(3, 0)$ is $z = 3p + 0 = 3p$.

The value of $z$ at the corner point $(1, 1)$ is $z = p + q$.

Since the minimum of $z$ occurs at both $(3, 0)$ and $(1, 1)$, the values of $z$ at these points must be equal.

$3p = p + q$

$2p = q$

$p = \dfrac{q}{2}$

Checking the value at $(0, 3)$, $z = 3q = 6p$. Since $p > 0$, $3p < 6p$, confirming the minimum is indeed at $(3, 0)$ and $(1, 1)$.

Answer: $p = \dfrac{q}{2}$

</details>

---

### Q27. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The point at which the maximum value of $x + y$ subject to constraints $x + 2y \leq 70$ and $2x + y \leq 95, x \geq 0, y \geq 0$ is.

**Options:**

- **(A)** $(47.5, 0)$
- **(B)** $(0, 95)$
- **(C)** $(0, 35)$
- **(D)** $(40, 15)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(40, 15)$**

**Detailed Solution:**

The objective function to be maximized is $Z = x + y$.

The given constraints are:
$x + 2y \leq 70$
$2x + y \leq 95$
$x \geq 0, y \geq 0$

The corner points of the feasible region are determined by the intersections of the boundary lines $x + 2y = 70$, $2x + y = 95$, and the coordinate axes.

Solving $x + 2y = 70$ and $2x + y = 95$:
Multiplying the second equation by $2$ gives $4x + 2y = 190$.
Subtracting the first equation from this gives $3x = 120 \Rightarrow x = 40$.
Substituting $x = 40$ into $x + 2y = 70$ gives $40 + 2y = 70 \Rightarrow 2y = 30 \Rightarrow y = 15$.
The intersection point is $(40, 15)$.

The corner points of the bounded feasible region are $(0, 0)$, $(47.5, 0)$, $(40, 15)$, and $(0, 35)$.

Evaluating $Z = x + y$ at each corner point:
At $(0, 0)$, $Z = 0 + 0 = 0$
At $(47.5, 0)$, $Z = 47.5 + 0 = 47.5$
At $(40, 15)$, $Z = 40 + 15 = 55$
At $(0, 35)$, $Z = 0 + 35 = 35$

The maximum value of $Z$ is $55$, which occurs at the point $(40, 15)$.

Answer: $(40, 15)$

</details>

---

### Q28. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The feasible region for the constraints $x-\mathrm{y} \geqslant 0, x-5 \mathrm{y} \leqslant-5, x \geqslant 0, \mathrm{y} \geqslant 0$ is shown by the figure:

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/bRQ6czsLH-QMNRQLwgdHMb4IUKn0mBWTvKR53F1EG0g.original.fullsize.png">
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/jgvrR4ggdliqfh1PZwMve8RKltNOvj_Z0jSvJL1D0bs.original.fullsize.png">
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/1wH-Z-2rTgK3-v2xBpF4P7OlnRQuOkYRE6tb4Ffeqy4.original.fullsize.png">
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/z9lSKgjU_AvXMGm9ZJN9vqUc9MEZW37nAiUOwpRjvPk.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/1wH-Z-2rTgK3-v2xBpF4P7OlnRQuOkYRE6tb4Ffeqy4.original.fullsize.png">**

**Detailed Solution:**

The given constraints are:
$x - y \ge 0 \Rightarrow y \le x$
$x - 5y \le -5 \Rightarrow 5y \ge x + 5 \Rightarrow y \ge \dfrac{x + 5}{5}$
$x \ge 0, y \ge 0$

The line $x - y = 0$ passes through the origin $(0,0)$ and has a slope of $1$. The inequality $y \le x$ represents the region below or on this line.

The line $x - 5y = -5$ has an $x$-intercept of $-5$ and a $y$-intercept of $1$, with a slope of $\dfrac{1}{5}$. The inequality $y \ge \dfrac{x + 5}{5}$ represents the region above or on this line.

The intersection point of the two lines is obtained by solving $x = y$ and $x - 5y = -5$, which gives $\left(\dfrac{5}{4}, \dfrac{5}{4}\right)$.

For $x > \dfrac{5}{4}$, the line $x - y = 0$ (slope $1$) is steeper and lies above the line $x - 5y = -5$ (slope $1/5$).

The feasible region must satisfy both $y \le x$ (below the steeper line) and $y \ge \dfrac{x + 5}{5}$ (above the less steep line). Thus, the region is bounded between the two lines in the first quadrant, extending infinitely to the right from their intersection point.

This corresponds to the third graph.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/1wH-Z-2rTgK3-v2xBpF4P7OlnRQuOkYRE6tb4Ffeqy4.original.fullsize.png">

</details>

---

### Q29. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The difference between the maximum and minimum values of the objective function $\mathrm{Z}=3 x+5 \mathrm{y}$, subject to the constraints $x+3 \mathrm{y} \leqslant 60, x+\mathrm{y} \geqslant 10$, $x-\mathrm{y} \leqslant 0, x, \mathrm{y} \geqslant 0$ is

**Options:**

- **(A)** 80
- **(B)** 40
- **(C)** 60
- **(D)** 100

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 80**

**Detailed Solution:**

The given objective function is $\mathrm{Z} = 3x + 5y$.

The constraints are:
$x + 3y \leqslant 60$
$x + y \geqslant 10$
$x - y \leqslant 0 \Rightarrow x \leqslant y$
$x \geqslant 0, y \geqslant 0$

To find the corner points of the feasible region, we solve the equations of the boundary lines:
1) Intersection of $x + 3y = 60$ and $x = y$:
$x + 3x = 60 \Rightarrow 4x = 60 \Rightarrow x = 15, y = 15$. Point is $(15, 15)$.

2) Intersection of $x + y = 10$ and $x = y$:
$x + x = 10 \Rightarrow 2x = 10 \Rightarrow x = 5, y = 5$. Point is $(5, 5)$.

3) Intersection of $x + 3y = 60$ and the y-axis ($x = 0$):
$0 + 3y = 60 \Rightarrow y = 20$. Point is $(0, 20)$.

4) Intersection of $x + y = 10$ and the y-axis ($x = 0$):
$0 + y = 10 \Rightarrow y = 10$. Point is $(0, 10)$.

Now, we evaluate the objective function $\mathrm{Z} = 3x + 5y$ at these corner points:
At $(15, 15)$: $\mathrm{Z} = 3(15) + 5(15) = 45 + 75 = 120$
At $(5, 5)$: $\mathrm{Z} = 3(5) + 5(5) = 15 + 25 = 40$
At $(0, 20)$: $\mathrm{Z} = 3(0) + 5(20) = 0 + 100 = 100$
At $(0, 10)$: $\mathrm{Z} = 3(0) + 5(10) = 0 + 50 = 50$

The maximum value of $\mathrm{Z}$ is $120$ and the minimum value is $40$.

The difference between the maximum and minimum values is:
$120 - 40 = 80$

Answer: 80

</details>

---

### Q30. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Maximum value of $\mathrm{z}=3 x+4 \mathrm{y}$ subject to $x-\mathrm{y} \leqslant-1, \quad-x+\mathrm{y} \leqslant 0, \quad x, \mathrm{y} \geqslant 0$ is given by

**Options:**

- **(A)** does not exist
- **(B)** 1
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) does not exist**

**Detailed Solution:**

The given constraints are $x - y \leqslant -1$ and $-x + y \leqslant 0$.

These inequalities can be rewritten as $y \geqslant x + 1$ and $y \leqslant x$.

Combining these two inequalities, we get $x + 1 \leqslant y \leqslant x$, which implies $x + 1 \leqslant x$, or $1 \leqslant 0$.

This is a contradiction, which means there are no points $(x, y)$ that satisfy all the given constraints simultaneously.

Since the feasible region is empty, the maximum value of the objective function $\mathrm{z} = 3x + 4y$ does not exist.

Answer: does not exist

</details>

---

### Q31. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A manufacturing company produces two items, A and B. Each toy should be processed by two machines, I and II. Machine I can be operated for maximum 10 hours 40 minutes. It takes 20 minutes for an item A and 15 minutes for B. Machine II can be operated for a total time at 8 hours 20 minutes. It takes 5 minutes for an item $A$ and 8 minutes for $B$. The profit per item of $A$ is $₹ 25$ and per item of $B$ is ₹18. The formulation of an L.P.P. to maximize the profit (where $x$ is number of items $A$ and $y$ is the number of item $B$ ) is _____

**Options:**

- **(A)** $\begin{aligned}
& \text { Maximize } \mathrm{z}=25 x+18 \mathrm{y} \\
& \text { subject to } 20 x+15 y \leqslant 640 \\
& \qquad \begin{array}{r}
5 x+8 y \geqslant 500 \\
x, y \geqslant 0
\end{array}
\end{aligned}$
- **(B)** $\begin{array}{r}\text { Maximize } \mathrm{z}=25 x+18 \mathrm{y} \\ \text { subject to } 20 x+15 y \leqslant 640 \\ \qquad 5 x+8 y \leqslant 500 \\ \qquad x, y \geqslant 0\end{array}$
- **(C)** $\begin{aligned} & \text { Maximize } \mathrm{z}=25 x+18 \mathrm{y} \\ & \text { subject to } 20 x+5 y \leqslant 8 \\ & \qquad 5 x+8 y \leqslant 10 \\ & x, y \geqslant 0\end{aligned}$
- **(D)** $\begin{array}{r}\text { Maximize } \mathrm{z}=25 x+18 \mathrm{y} \\ \text { subject to } 4 x+3 y \leqslant 128 \\ \qquad \begin{array}{r}5 x+8 y \geqslant 500 \\ x, y \geqslant 0\end{array}\end{array}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\begin{array}{r}\text { Maximize } \mathrm{z}=25 x+18 \mathrm{y} \\ \text { subject to } 20 x+15 y \leqslant 640 \\ \qquad 5 x+8 y \leqslant 500 \\ \qquad x, y \geqslant 0\end{array}$**

**Detailed Solution:**

Let $x$ be the number of items A and $y$ be the number of items B.

The profit per item A is ₹25 and per item B is ₹18. The total profit to be maximized is:
$Z = 25x + 18y$

For Machine I, the time taken by item A is 20 minutes and by item B is 15 minutes. The maximum available time is 10 hours 40 minutes, which is $10 \times 60 + 40 = 640$ minutes. The constraint is:
$20x + 15y \leqslant 640$

For Machine II, the time taken by item A is 5 minutes and by item B is 8 minutes. The maximum available time is 8 hours 20 minutes, which is $8 \times 60 + 20 = 500$ minutes. The constraint is:
$5x + 8y \leqslant 500$

Since the number of items cannot be negative, we have the non-negativity constraints:
$x \geqslant 0, y \geqslant 0$

Thus, the L.P.P. is formulated as:
Maximize $Z = 25x + 18y$
subject to $20x + 15y \leqslant 640$
$5x + 8y \leqslant 500$
$x, y \geqslant 0$

Answer: $\begin{array}{r}\text { Maximize } \mathrm{z}=25 x+18 \mathrm{y} \\ \text { subject to } 20 x+15 y \leqslant 640 \\ \qquad 5 x+8 y \leqslant 500 \\ \qquad x, y \geqslant 0\end{array}$

</details>

---

### Q32. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution for minimizing the function $\mathrm{z}=x+\mathrm{y}$ under an L.P.P. with constraints $x+\mathrm{y} \geqslant 2, x+2 \mathrm{y} \leqslant 8, \mathrm{y} \leqslant 3, x, \mathrm{y} \geqslant 0$ is

**Options:**

- **(A)** at the point $(0,3)$
- **(B)** at the point ( 8,0 )
- **(C)** at infinite number of points but bounded set
- **(D)** at unbounded set

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) at infinite number of points but bounded set**

**Detailed Solution:**

The given constraints are $x+y \geqslant 2$, $x+2y \leqslant 8$, $y \leqslant 3$, $x, y \geqslant 0$.

The corner points of the feasible region are obtained by solving the equations of the boundary lines:
$A(0, 2)$ from $x=0$ and $x+y=2$
$B(0, 3)$ from $x=0$ and $y=3$
$C(2, 3)$ from $y=3$ and $x+2y=8$
$D(8, 0)$ from $y=0$ and $x+2y=8$
$E(2, 0)$ from $y=0$ and $x+y=2$

Evaluating the objective function $z = x + y$ at these corner points:
At $A(0, 2)$, $z = 0 + 2 = 2$
At $B(0, 3)$, $z = 0 + 3 = 3$
At $C(2, 3)$, $z = 2 + 3 = 5$
At $D(8, 0)$, $z = 8 + 0 = 8$
At $E(2, 0)$, $z = 2 + 0 = 2$

The minimum value of $z$ is $2$, which occurs at two adjacent corner points $A(0, 2)$ and $E(2, 0)$.

Since the minimum value occurs at two distinct points, it will occur at all points on the line segment joining $A(0, 2)$ and $E(2, 0)$. This line segment contains an infinite number of points and forms a bounded set.

Answer: at infinite number of points but bounded set

</details>

---

### Q33. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In L.P.P. , the maximum value of objective function $\mathrm{Z}=6 \mathrm{x}+3 \mathrm{y}$ subject to constraints $x+\mathrm{y} \leq 5, x+2 \mathrm{y} \geqslant 4,4 x+\mathrm{y} \leq 12, x, \mathrm{y} \geqslant 0$ is

**Options:**

- **(A)** $\frac{132}{7}$
- **(B)** 22
- **(C)** 15
- **(D)** $\frac{122}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 22**

**Detailed Solution:**

The given objective function is $\mathrm{Z} = 6x + 3y$.

The given constraints are:
$x + y \leq 5$
$x + 2y \geq 4$
$4x + y \leq 12$
$x, y \geq 0$

To find the feasible region, we determine the corner points by finding the points of intersection of the boundary lines that satisfy all constraints.

1. Intersection of $x + y = 5$ and $4x + y = 12$:
Subtracting the first from the second gives $3x = 7 \Rightarrow x = \dfrac{7}{3}$.
Substituting $x$ in the first equation gives $y = 5 - \dfrac{7}{3} = \dfrac{8}{3}$.
Point: $\left(\dfrac{7}{3}, \dfrac{8}{3}\right)$.
Checking the second constraint: $\dfrac{7}{3} + 2\left(\dfrac{8}{3}\right) = \dfrac{23}{3} \geq 4$ (Satisfied).

2. Intersection of $x + 2y = 4$ and $4x + y = 12$:
From the first equation, $x = 4 - 2y$.
Substituting into the second gives $4(4 - 2y) + y = 12 \Rightarrow 16 - 7y = 12 \Rightarrow 7y = 4 \Rightarrow y = \dfrac{4}{7}$.
Then $x = 4 - 2\left(\dfrac{4}{7}\right) = \dfrac{20}{7}$.
Point: $\left(\dfrac{20}{7}, \dfrac{4}{7}\right)$.
Checking the first constraint: $\dfrac{20}{7} + \dfrac{4}{7} = \dfrac{24}{7} \leq 5$ (Satisfied).

3. Intersections with the y-axis ($x = 0$):
For $x + y = 5$, $y = 5$. Point: $(0, 5)$.
For $x + 2y = 4$, $y = 2$. Point: $(0, 2)$.
Both points satisfy all constraints.

4. Intersections with the x-axis ($y = 0$):
For $4x + y = 12$, $x = 3$. But $x + 2(0) = 3 \not\geq 4$.
For $x + 2y = 4$, $x = 4$. But $4(4) + 0 = 16 \not\leq 12$.
Thus, there are no feasible corner points on the x-axis.

Now, we evaluate the objective function $\mathrm{Z} = 6x + 3y$ at the feasible corner points:
At $(0, 5)$: $\mathrm{Z} = 6(0) + 3(5) = 15$
At $\left(\dfrac{7}{3}, \dfrac{8}{3}\right)$: $\mathrm{Z} = 6\left(\dfrac{7}{3}\right) + 3\left(\dfrac{8}{3}\right) = 14 + 8 = 22$
At $\left(\dfrac{20}{7}, \dfrac{4}{7}\right)$: $\mathrm{Z} = 6\left(\dfrac{20}{7}\right) + 3\left(\dfrac{4}{7}\right) = \dfrac{120}{7} + \dfrac{12}{7} = \dfrac{132}{7} \approx 18.86$
At $(0, 2)$: $\mathrm{Z} = 6(0) + 3(2) = 6$

The maximum value of $\mathrm{Z}$ is $22$.

Answer: 22

</details>

---

### Q34. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution set of the constraints $|x-y| \leqslant 1, x, y \geqslant 0$ is

**Options:**

- **(A)** a finite set
- **(B)** an unbounded set
- **(C)** a convex polygon
- **(D)** such that feasible region does not exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) an unbounded set**

**Detailed Solution:**

The given constraints are $|x-y| \leqslant 1$ and $x, y \geqslant 0$.

The inequality $|x-y| \leqslant 1$ can be rewritten as $-1 \leqslant x-y \leqslant 1$, which gives two inequalities:
$x - y \leqslant 1$ and $x - y \geqslant -1$.

These represent the region between the parallel lines $x - y = 1$ and $x - y = -1$.

The conditions $x \geqslant 0$ and $y \geqslant 0$ restrict the solution to the first quadrant.

Since the parallel lines $x - y = 1$ and $x - y = -1$ extend infinitely in the first quadrant, the region bounded by them is not closed. For example, points of the form $(k, k)$ for any arbitrarily large positive number $k$ satisfy all the given constraints.

Thus, the feasible region extends infinitely and the solution set is an unbounded set.

Answer: an unbounded set

</details>

---

### Q35. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The difference between the maximum value and minimum value of objective function $\mathrm{z}=3 x+5 y$ subject to constraints $x+3 y \leqslant 60$, $x+\mathrm{y} \geqslant 10, x-\mathrm{y}=0, x, \mathrm{y} \geqslant 0$ is

**Options:**

- **(A)** 60
- **(B)** 20
- **(C)** 80
- **(D)** 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 80**

**Detailed Solution:**

Given the objective function $z = 3x + 5y$ and the constraint $x - y = 0$, we have $y = x$.

Substituting $y = x$ into the given inequalities, we get:

$x + 3x \le 60 \Rightarrow 4x \le 60 \Rightarrow x \le 15$

$x + x \ge 10 \Rightarrow 2x \ge 10 \Rightarrow x \ge 5$

Since $x, y \ge 0$, the feasible range for $x$ is $5 \le x \le 15$.

Substituting $y = x$ into the objective function:

$z = 3x + 5x = 8x$

The maximum value of $z$ occurs at $x = 15$:

$z_{\max} = 8 \times 15 = 120$

The minimum value of $z$ occurs at $x = 5$:

$z_{\min} = 8 \times 5 = 40$

The difference between the maximum and minimum values is:

$120 - 40 = 80$

Answer: 80

</details>

---

### Q36. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The graph with correct feasible region of L.P.P. for the constraints $2 x+\mathrm{y} \leqslant 10, \mathrm{y} \leqslant x, \mathrm{y} \leqslant 2, x, \mathrm{y} \geqslant 0$ is $\ldots$

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/LqvnNfiDVmvnuu972FUiL6GalTkmDtmajCS9LHn6pAM.original.fullsize.png">
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/U74BWRAKKgy98g8tGkh4rze2FSOZ1QGug0V4nus4uW4.original.fullsize.png">
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/zpPcCEZKz8qFdHvXjIBp6Z1HWkFLkCZQV0ycrqr-S0o.original.fullsize.png">
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/HmNIfIwfypfViQqVcUgO_w7ea4c2TlRBB34C52gYrhw.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/LqvnNfiDVmvnuu972FUiL6GalTkmDtmajCS9LHn6pAM.original.fullsize.png">**

**Detailed Solution:**

For $2x + y \le 10$, substituting $(0, 0)$ gives $0 \le 10$, which is true, so the region lies on the origin side of the line $2x + y = 10$, which passes through $(5, 0)$ and $(0, 10)$.

For $y \le x$, the region lies below the line $y = x$.

For $y \le 2$, the region lies below the line $y = 2$.

With $x, y \ge 0$, the region lies in the first quadrant.

The line $y = x$ meets $y = 2$ at $(2, 2)$, and the line $2x + y = 10$ meets $y = 2$ at $(4, 2)$.

Hence the feasible region is the quadrilateral with vertices $(0, 0)$, $(5, 0)$, $(4, 2)$ and $(2, 2)$, bounded by the X-axis, the line $2x + y = 10$, the line $y = 2$ and the line $y = x$.

Only graph A shades exactly this region, so graph A shows the correct feasible region.

</details>

---

### Q37. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The correct constraints for the given feasible region are ....
<img width=300px src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/AxIJ9CDdwfcMP2FcAMZv9LKLykvuJxDvaIWMluXKSGM.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{y}-x \geqslant 1, x+5 \mathrm{y} \leqslant 10, x+\mathrm{y} \geqslant 2, \quad x, \mathrm{y} \geqslant 0$
- **(B)** $y-x \leqslant 1,2 x+5 y \leqslant 10, x+y \geqslant 1, x, y \geqslant 0$
- **(C)** $y-x \geqslant 1,2 x+5 y \leqslant 10, x+y \geqslant 1, x, y \geqslant 0$
- **(D)** $x-\mathrm{y} \leqslant 1,2 x+5 \mathrm{y} \geqslant 10, x+\mathrm{y} \leqslant 1, x, \mathrm{y} \geqslant 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y-x \geqslant 1,2 x+5 y \leqslant 10, x+y \geqslant 1, x, y \geqslant 0$**

**Detailed Solution:**

From the given graph, we can determine the equations of the three lines $L_1$, $L_2$, and $L_3$ by identifying their intercepts on the coordinate axes.

Line $L_1$ passes through the points $(-1, 0)$ and $(0, 1)$.
Using the two-point form or intercept form, the equation of $L_1$ is:
$\dfrac{x}{-1} + \dfrac{y}{1} = 1 \Rightarrow -x + y = 1 \Rightarrow y - x = 1$

Line $L_2$ passes through the points $(5, 0)$ and $(0, 2)$.
The equation of $L_2$ is:
$\dfrac{x}{5} + \dfrac{y}{2} = 1 \Rightarrow 2x + 5y = 10$

Line $L_3$ passes through the points $(1, 0)$ and $(0, 1)$.
The equation of $L_3$ is:
$\dfrac{x}{1} + \dfrac{y}{1} = 1 \Rightarrow x + y = 1$

Now, let's analyze the shaded feasible region:
1. The region lies in the first quadrant and is bounded by the Y-axis on the left, so $x \geqslant 0$ and $y \geqslant 0$.
2. The region is above the line $L_1$. We can verify this by taking a test point inside the region, for example, $(0.5, 1.6)$. Substituting into $y - x$, we get $1.6 - 0.5 = 1.1 \geqslant 1$. Thus, the constraint is $y - x \geqslant 1$.
3. The region is below the line $L_2$. Using the same test point $(0.5, 1.6)$, we get $2(0.5) + 5(1.6) = 1 + 8 = 9 \leqslant 10$. Thus, the constraint is $2x + 5y \leqslant 10$.
4. The region is above the line $L_3$. Since $y \geqslant x + 1$ and $x \geqslant 0$, it follows that $y \geqslant 1$, which implies $x + y \geqslant 1$. Thus, the constraint $x + y \geqslant 1$ is also satisfied.

Combining all these inequalities, the correct constraints for the feasible region are:
$y - x \geqslant 1, 2x + 5y \leqslant 10, x + y \geqslant 1, x, y \geqslant 0$

Answer: $y-x \geqslant 1,2 x+5 y \leqslant 10, x+y \geqslant 1, x, y \geqslant 0$

</details>

---

### Q38. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the difference between the maximum and minimum values of the objective function $\mathrm{z}=7 x-8 \mathrm{y}$ subject to the constraints $x+y \leqslant 20$, $y \geqslant 5, x, y \geqslant 0$ is $5 k+200$, then the value of $k$ is

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $5$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

The given objective function is $z = 7x - 8y$.

The constraints are:
$x + y \leqslant 20$
$y \geqslant 5$
$x \geqslant 0$

The feasible region is bounded by the lines $x = 0$, $y = 5$, and $x + y = 20$. The corner points (vertices) of the feasible region are the intersections of these lines:
1. Intersection of $x = 0$ and $y = 5$ is $(0, 5)$.
2. Intersection of $x = 0$ and $x + y = 20$ is $(0, 20)$.
3. Intersection of $y = 5$ and $x + y = 20$ is $(15, 5)$.

Now, we evaluate the objective function $z = 7x - 8y$ at each of these corner points:
At $(0, 5)$: $z = 7(0) - 8(5) = -40$
At $(0, 20)$: $z = 7(0) - 8(20) = -160$
At $(15, 5)$: $z = 7(15) - 8(5) = 105 - 40 = 65$

The maximum value of $z$ is $65$ and the minimum value of $z$ is $-160$.

The difference between the maximum and minimum values is:
$65 - (-160) = 65 + 160 = 225$

According to the given condition, this difference is equal to $5k + 200$.

$5k + 200 = 225$

$5k = 25$

$k = 5$

Answer: $5$

</details>

---

### Q39. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution set for minimizing the function $\mathrm{z}=x+\mathrm{y}$ with constraints $x+\mathrm{y} \geqslant 2, x+2 \mathrm{y} \leqslant 8, \mathrm{y} \leqslant 3, x, \mathrm{y} \geqslant 0$ contains

**Options:**

- **(A)** $x=0, y=3$
- **(B)** $x=8, \mathrm{y}=0$
- **(C)** infinitely many points
- **(D)** $x=2, \mathrm{y}=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) infinitely many points**

**Detailed Solution:**

The objective function to be minimized is $\mathrm{z} = x + \mathrm{y}$.

The given constraints are:
$x + \mathrm{y} \geqslant 2$
$x + 2\mathrm{y} \leqslant 8$
$\mathrm{y} \leqslant 3$
$x \geqslant 0, \mathrm{y} \geqslant 0$

The feasible region is bounded by the vertices obtained by the intersection of the lines corresponding to the constraints. Let us find the corner points of the feasible region:
Intersection of $x + \mathrm{y} = 2$ and $x = 0$ gives $(0, 2)$.
Intersection of $x + \mathrm{y} = 2$ and $\mathrm{y} = 0$ gives $(2, 0)$.
Intersection of $x + 2\mathrm{y} = 8$ and $\mathrm{y} = 0$ gives $(8, 0)$.
Intersection of $x + 2\mathrm{y} = 8$ and $\mathrm{y} = 3$ gives $(2, 3)$.
Intersection of $x = 0$ and $\mathrm{y} = 3$ gives $(0, 3)$.

All these points satisfy the given constraints, so they are the vertices of the feasible region.

Now, we evaluate the objective function $\mathrm{z} = x + \mathrm{y}$ at each of these vertices:
At $(0, 2)$, $\mathrm{z} = 0 + 2 = 2$
At $(2, 0)$, $\mathrm{z} = 2 + 0 = 2$
At $(8, 0)$, $\mathrm{z} = 8 + 0 = 8$
At $(2, 3)$, $\mathrm{z} = 2 + 3 = 5$
At $(0, 3)$, $\mathrm{z} = 0 + 3 = 3$

The minimum value of $\mathrm{z}$ is $2$, which occurs at two distinct corner points, $(0, 2)$ and $(2, 0)$.

Since the minimum value occurs at two vertices, it will also occur at all points on the line segment joining these two vertices. Therefore, the solution set contains infinitely many points.

Answer: infinitely many points

</details>

---

### Q40. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The L.P.P. , minimize $z=30 x+20 y, \quad x+y \leqslant 8, \quad x+2 y \geqslant 4, \quad 6 x+4 y \geqslant 12$, $x \geqslant 0, y \geqslant 0$ has

**Options:**

- **(A)** a unique solution
- **(B)** infinitely many solutions
- **(C)** minimum value at $(4,0)$
- **(D)** minimum value at $(8,0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) infinitely many solutions**

**Detailed Solution:**

The objective function to be minimized is $z = 30x + 20y$.

The given constraints are:
$x + y \leqslant 8$
$x + 2y \geqslant 4$
$6x + 4y \geqslant 12 \Rightarrow 3x + 2y \geqslant 6$
$x \geqslant 0, y \geqslant 0$

To find the feasible region, we determine the corner points by solving the boundary equations:
1) Intersection of $x + 2y = 4$ and $3x + 2y = 6$:
Subtracting the first from the second gives $2x = 2 \Rightarrow x = 1$.
Substituting $x = 1$ in $x + 2y = 4$ gives $2y = 3 \Rightarrow y = 1.5$.
So, one corner point is $(1, 1.5)$.

2) Intersection of $3x + 2y = 6$ with the $y$-axis ($x = 0$):
$2y = 6 \Rightarrow y = 3$.
So, another corner point is $(0, 3)$.

3) Intersection of $x + 2y = 4$ with the $x$-axis ($y = 0$):
$x = 4$.
So, a corner point is $(4, 0)$.

4) Intersections of $x + y = 8$ with the axes are $(8, 0)$ and $(0, 8)$.

The corner points of the feasible region are $(0, 8)$, $(8, 0)$, $(4, 0)$, $(1, 1.5)$, and $(0, 3)$.

Now, we evaluate the objective function $z = 30x + 20y$ at each corner point:
At $(0, 8)$: $z = 30(0) + 20(8) = 160$
At $(8, 0)$: $z = 30(8) + 20(0) = 240$
At $(4, 0)$: $z = 30(4) + 20(0) = 120$
At $(1, 1.5)$: $z = 30(1) + 20(1.5) = 60$
At $(0, 3)$: $z = 30(0) + 20(3) = 60$

The minimum value of $z$ is $60$, which occurs at two adjacent corner points, $(1, 1.5)$ and $(0, 3)$. 

Since the minimum value is the same at two distinct corner points, it will be the same at all points on the line segment joining them. Therefore, the L.P.P. has infinitely many solutions.

Answer: infinitely many solutions

</details>

---

### Q41. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A scholarship amount is given by $z=550 x+300 y$ and is to be distributed among $x$ boys and y girls. From the graph given below the maximum amount of scholarship is _________.
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/MMh6YtjnXC124qoRDYKwFaA8PU9uhKxt0LYleefKs-U.original.fullsize_3.png">

**Options:**

- **(A)** $7250$
- **(B)** $9250$
- **(C)** $4250$
- **(D)** $5750$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $7250$**

**Detailed Solution:**

From the given graph, the feasible region is the shaded quadrilateral $ABCD$. The equations of the lines bounding this region are $x = 5$, $y = 4$, $x + y = 10$, and $x + y = 15$.

Let us find the coordinates of the vertices $A, B, C,$ and $D$ by solving the equations of the intersecting lines:
1. Point $A$ is the intersection of $x = 5$ and $x + y = 10$. Substituting $x = 5$, we get $5 + y = 10 \Rightarrow y = 5$. So, $A = (5, 5)$.
2. Point $B$ is the intersection of $x = 5$ and $x + y = 15$. Substituting $x = 5$, we get $5 + y = 15 \Rightarrow y = 10$. So, $B = (5, 10)$.
3. Point $C$ is the intersection of $y = 4$ and $x + y = 15$. Substituting $y = 4$, we get $x + 4 = 15 \Rightarrow x = 11$. So, $C = (11, 4)$.
4. Point $D$ is the intersection of $y = 4$ and $x + y = 10$. Substituting $y = 4$, we get $x + 4 = 10 \Rightarrow x = 6$. So, $D = (6, 4)$.

Now, we evaluate the objective function $z = 550x + 300y$ at each of these vertices to find the maximum value:
At $A(5, 5)$: $z = 550(5) + 300(5) = 2750 + 1500 = 4250$
At $B(5, 10)$: $z = 550(5) + 300(10) = 2750 + 3000 = 5750$
At $C(11, 4)$: $z = 550(11) + 300(4) = 6050 + 1200 = 7250$
At $D(6, 4)$: $z = 550(6) + 300(4) = 3300 + 1200 = 4500$

Comparing the values, the maximum amount of scholarship is $7250$, which occurs at point $C(11, 4)$.

Answer: $7250$

</details>

---

### Q42. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The feasible region for the constraints $x-2 \leqslant y, x \geqslant y-1, x \geqslant 2, y \leqslant 4$, $x, y \geqslant 0$, is ...

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/tKYp2f1nv6GLcAGUlrj3EXps7L3zelDOLaB5DFq8af4.original.fullsize.png">
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/D1kRVXLEp5RqoKC549M5NOjh5FsxozWt6MzdG3eSAtU.original.fullsize.png">
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/s037V4kvVL05HYCT_R-rUn1utAzVclmG2OnEI2XB6Ik.original.fullsize.png">
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/l4-aLtRp80iz7LkVQPnWFiCDAMqkIywdmNStjscFVrs.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/D1kRVXLEp5RqoKC549M5NOjh5FsxozWt6MzdG3eSAtU.original.fullsize.png">**

**Detailed Solution:**

The given constraints can be rewritten to identify the feasible region:

$x - 2 \leqslant y \Rightarrow y \geqslant x - 2$ (The region lies above or on the line $y = x - 2$)

$x \geqslant y - 1 \Rightarrow y \leqslant x + 1$ (The region lies below or on the line $y = x + 1$)

$x \geqslant 2$ (The region lies to the right of or on the vertical line $x = 2$)

$y \leqslant 4$ (The region lies below or on the horizontal line $y = 4$)

$x, y \geqslant 0$ (The region is restricted to the first quadrant)

By finding the intersection of these inequalities, the feasible region is bounded by $x = 2$ on the left, $y = 4$ on the top, $y = x + 1$ on the top-left, and $y = x - 2$ on the bottom-right.

The vertices of this bounded region are $(2, 0)$, $(2, 3)$, $(3, 4)$, and $(6, 4)$.

This exactly matches the shaded area shown in the second image.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/D1kRVXLEp5RqoKC549M5NOjh5FsxozWt6MzdG3eSAtU.original.fullsize.png">

</details>

---

### Q43. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The feasible region represented by the given constraints $2 x+3 \mathrm{y} \geqslant 12,-x+\mathrm{y} \leqslant 3, x \leqslant 4, \mathrm{y} \geqslant 3$ is denoted by
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/hXnDFY_fzvSXfrj21DO9Y6vD_mryLtu43IXJZa6KObo.original.fullsize.png">

**Options:**

- **(A)** $S_1$
- **(B)** $\mathrm{S}_2$
- **(C)** $\mathrm{S}_3$
- **(D)** $\mathrm{S}_4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $S_1$**

**Detailed Solution:**

The feasible region is the set of points that satisfy all four constraints simultaneously.

For $2x + 3y \ge 12$, substituting $(0, 0)$ gives $0 \ge 12$, which is false. So the region lies on the non-origin side of the line $2x + 3y = 12$, which passes through $(6, 0)$ and $(0, 4)$.

For $-x + y \le 3$, substituting $(0, 0)$ gives $0 \le 3$, which is true. So the region lies on the origin side of $-x + y = 3$, that is, below the line $y = x + 3$.

For $x \le 4$, the region lies to the left of the line $x = 4$.

For $y \ge 3$, the region lies above the line $y = 3$.

Hence the feasible region lies above $y = 3$, above $2x + 3y = 12$, below $y = x + 3$ and to the left of $x = 4$. Its corner points are $\left(\dfrac{3}{2}, 3\right)$, $(4, 3)$, $(4, 7)$ and $\left(\dfrac{3}{5}, \dfrac{18}{5}\right)$.

In the figure, $S_2$ and $S_3$ lie below $y = 3$, and $S_4$ lies on the origin side of $2x + 3y = 12$. Only $S_1$ lies above $y = 3$, above $2x + 3y = 12$, below $y = x + 3$ and to the left of $x = 4$.

Therefore, the feasible region is denoted by $S_1$.

</details>

---

### Q44. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The shaded area in the given figure is a solution set for some system of inequalities. The maximum value of the function $z=4 x+3 y$ subject to linear constraints given by the system is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/NYDB3FsBTGNz25AtrMlNGmliQAXeeiXVjL5oPur4ESw.original.fullsize.png"/>

**Options:**

- **(A)** 38
- **(B)** 36
- **(C)** 33
- **(D)** 34

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 36**

**Detailed Solution:**

From the given graph, we can identify the corner points (vertices) of the shaded feasible region.

The region is bounded by the coordinate axes, a vertical line, and two intersecting straight lines.

The vertical line is $x = 6$.

One of the lines passes through $(0, 10)$ and $(10, 0)$, so its equation is $x + y = 10$.

The other line passes through $(0, 5)$ and intersects the first line at $(3, 7)$.

The intersection of the vertical line $x = 6$ and the line $x + y = 10$ is $(6, 4)$.

Thus, the corner points of the feasible region are $(0, 0)$, $(6, 0)$, $(6, 4)$, $(3, 7)$, and $(0, 5)$.

We evaluate the objective function $z = 4x + 3y$ at each of these corner points:

At $(0, 0)$, $z = 4(0) + 3(0) = 0$

At $(6, 0)$, $z = 4(6) + 3(0) = 24$

At $(6, 4)$, $z = 4(6) + 3(4) = 24 + 12 = 36$

At $(3, 7)$, $z = 4(3) + 3(7) = 12 + 21 = 33$

At $(0, 5)$, $z = 4(0) + 3(5) = 15$

Comparing these values, the maximum value of $z$ is $36$.

Answer: 36

</details>

---

### Q45. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Maximum value of $\mathrm{Z}=100 x+70 y$ Subject to $2 x \geq 4, y \leq 3, x+y \leq 8, x, y \geq 0$ is

**Options:**

- **(A)** 800 .
- **(B)** 940 .
- **(C)** 400 .
- **(D)** 710 .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 800 .**

**Detailed Solution:**

The given constraints are $2x \geq 4 \Rightarrow x \geq 2$, $y \leq 3$, $x + y \leq 8$, $x \geq 0$, and $y \geq 0$.

The feasible region is bounded by the lines $x = 2$, $y = 0$, $x + y = 8$, and $y = 3$.

The corner points of the feasible region are obtained by solving the equations of the intersecting lines:
1) Intersection of $x = 2$ and $y = 0$ is $(2, 0)$.
2) Intersection of $x + y = 8$ and $y = 0$ is $(8, 0)$.
3) Intersection of $x + y = 8$ and $y = 3$ is $(5, 3)$.
4) Intersection of $x = 2$ and $y = 3$ is $(2, 3)$.

Evaluating the objective function $Z = 100x + 70y$ at these corner points:
At $(2, 0)$, $Z = 100(2) + 70(0) = 200$
At $(8, 0)$, $Z = 100(8) + 70(0) = 800$
At $(5, 3)$, $Z = 100(5) + 70(3) = 500 + 210 = 710$
At $(2, 3)$, $Z = 100(2) + 70(3) = 200 + 210 = 410$

The maximum value of $Z$ is $800$.

Answer: 800 .

</details>

---

### Q46. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The graphical solution set of the system of inequations $2 x+3 y \leq 6, x+4 y \geq 4, x \geq 0, y \geq 0$ is given by
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/0kVextUAfEX31JztdYa6s9nDOPkZSArW7nUWqXQYKRc.original.fullsize.png"/>

**Options:**

- **(A)** Fig. 1
- **(B)** Fig. 3
- **(C)** Fig. 2
- **(D)** Fig. 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Fig. 1**

**Detailed Solution:**

Consider the corresponding equations to find the boundary lines:

Line 1: $2x + 3y = 6$
When $x = 0$, $y = 2$. Point is $(0, 2)$.
When $y = 0$, $x = 3$. Point is $(3, 0)$.
For the inequality $2x + 3y \le 6$, substituting the origin $(0,0)$ gives $0 \le 6$, which is true. Thus, the feasible region lies towards the origin (below or on the line).

Line 2: $x + 4y = 4$
When $x = 0$, $y = 1$. Point is $(0, 1)$.
When $y = 0$, $x = 4$. Point is $(4, 0)$.
For the inequality $x + 4y \ge 4$, substituting the origin $(0,0)$ gives $0 \ge 4$, which is false. Thus, the feasible region lies away from the origin (above or on the line).

The non-negativity constraints $x \ge 0$ and $y \ge 0$ restrict the solution to the first quadrant.

The common region satisfying all these conditions must be in the first quadrant, below the line $2x + 3y = 6$, and above the line $x + 4y = 4$. This region is bounded by the Y-axis between the points $(0, 1)$ and $(0, 2)$, and extends to the intersection point of the two lines.

Observing the given graphs, Fig. 1 correctly represents this shaded region.

Answer: Fig. 1

</details>

---

### Q47. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The region represented by the inequations $2 x+3 y \leqslant 18, x+y \geqslant 10, x \geqslant 0, y \geqslant 0$ is

**Options:**

- **(A)** unbounded
- **(B)** bounded region, but not a singleton set
- **(C)** singleton set
- **(D)** null set

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) null set**

**Detailed Solution:**

Given inequations are $2x + 3y \leqslant 18$, $x + y \geqslant 10$, $x \geqslant 0$, $y \geqslant 0$.

Multiplying the second inequation by $2$, we get $2x + 2y \geqslant 20$.

Subtracting this from the first inequation $2x + 3y \leqslant 18$, we get:

$(2x + 3y) - (2x + 2y) \leqslant 18 - 20$

$y \leqslant -2$

However, we are also given that $y \geqslant 0$. The conditions $y \leqslant -2$ and $y \geqslant 0$ cannot be satisfied simultaneously.

Thus, there are no points $(x, y)$ that satisfy all the given inequations. The region is a null set.

Answer: null set

</details>

---

### Q48. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A production unit makes special type of metal chips by combining copper and brass. The standard weight of the chip must be at least 5 gms. The basic ingredients i.e. copper and brass cost ₹8 and ₹5 per gm. The durability considerations dictate that the metal chip must no contain more than 4 gms of brass and should contain minimum 2 gms of copper. Then the minimum cost of the metal chip satisfying the above conditions is

**Options:**

- **(A)** ₹ 36
- **(B)** ₹ 31
- **(C)** ₹ 30
- **(D)** ₹ 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) ₹ 31**

**Detailed Solution:**

Let $x$ be the weight of copper in grams and $y$ be the weight of brass in grams.

The objective is to minimize the cost function:
$Z = 8x + 5y$

Subject to the given constraints:
1. Standard weight must be at least 5 gms: $x + y \ge 5$
2. Maximum 4 gms of brass: $y \le 4$
3. Minimum 2 gms of copper: $x \ge 2$
4. Non-negativity: $y \ge 0$

To find the corner points of the feasible region, we solve the equations of the boundary lines:
$x + y = 5$
$x = 2$
$y = 4$
$y = 0$

The corner points of the feasible region are:
1. Intersection of $x = 2$ and $y = 4$: $A(2, 4)$
2. Intersection of $x = 2$ and $x + y = 5$: $B(2, 3)$
3. Intersection of $x + y = 5$ and $y = 0$: $C(5, 0)$

Now, we evaluate the objective function $Z = 8x + 5y$ at each corner point:
At $A(2, 4)$: $Z = 8(2) + 5(4) = 16 + 20 = 36$
At $B(2, 3)$: $Z = 8(2) + 5(3) = 16 + 15 = 31$
At $C(5, 0)$: $Z = 8(5) + 5(0) = 40 + 0 = 40$

The minimum value of $Z$ is 31 at the point $(2, 3)$. Since the feasible region is unbounded, we verify that the open half-plane $8x + 5y < 31$ has no points in common with the feasible region. Thus, the minimum cost is ₹31.

Answer: ₹ 31

</details>

---

### Q49. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the following shaded region, the linear constraints are
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/F1Y7QJ4QWuHLZKX__paQKOUHJGKWM7PEbg5qzGBss38.original.fullsize.png"/>

**Options:**

- **(A)** $x-y \geq 0,-x+3 y \leq 3, x \geq 0, y \geq 0$
- **(B)** $x-y \leq 0,-x+3 y \leq 3, x \geq 0, y \geq 0$
- **(C)** $x-y \geq 0,-\dot{x}+3 y \geq 3, x \geq 0, y \geq 0$
- **(D)** $x-y \leq 0,-x+3 y=3, x \geq 0, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x-y \geq 0,-x+3 y \leq 3, x \geq 0, y \geq 0$**

**Detailed Solution:**

From the given graph, the shaded region is bounded by the lines $y = x$, $-x + 3y = 3$, and the X-axis ($y = 0$).

Let us consider a test point clearly inside the shaded region, for example, $(3, 1)$.

1. For the line $y = x$ (or $x - y = 0$):
Substituting the test point $(3, 1)$, we get $3 - 1 = 2 \geq 0$.
Thus, the inequality is $x - y \geq 0$.

2. For the line $-x + 3y = 3$:
Substituting the test point $(3, 1)$, we get $-3 + 3(1) = 0 \leq 3$.
Thus, the inequality is $-x + 3y \leq 3$.

3. The shaded region lies in the first quadrant, which means $x \geq 0$ and $y \geq 0$.

Combining all these conditions, the linear constraints for the shaded region are:
$x - y \geq 0, -x + 3y \leq 3, x \geq 0, y \geq 0$

Answer: $x-y \geq 0,-x+3 y \leq 3, x \geq 0, y \geq 0$

</details>

---

### Q50. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The graphical solution set of the system of inequations $x+y \geq 1,7 x+9 y \leq 63, y \leq 5, x \leq 6$, $x \geq 0, y \geq 0$ is represented by
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/rmQdub2XH6ycIOo2zEA9X3-QGs3xTjQ_Gp3SF_MRff0.original.fullsize.png"/>
Fig. 2<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/QDufM6zQUtYZyzf0M6qoU_O0Fw2JweFL16b9UhiCuS8.original.fullsize.png"/>
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/1dx77AHxbQbwevVlp_dMBk20D3VVOXZvZvhT_92i510.original.fullsize.png"/>
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/uCGVdxSeYs-z4xulPQZV2jBxjXIZJ4NzdGa1kPkS_dE.original.fullsize.png"/>

**Options:**

- **(A)** Fig. 1
- **(B)** Fig. 3
- **(C)** Fig. 2
- **(D)** Fig. 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Fig. 1**

**Detailed Solution:**

The given system of inequalities is:
$x + y \geq 1$
$7x + 9y \leq 63$
$y \leq 5$
$x \leq 6$
$x \geq 0, y \geq 0$

The corresponding equations for the boundary lines are:
$x + y = 1$ (passes through $(1,0)$ and $(0,1)$)
$7x + 9y = 63$ (passes through $(9,0)$ and $(0,7)$)
$y = 5$ (horizontal line)
$x = 6$ (vertical line)
$x = 0$ (y-axis)
$y = 0$ (x-axis)

The feasible region must satisfy all these conditions simultaneously:
1. It lies in the first quadrant ($x \geq 0, y \geq 0$).
2. It is above or on the line $x + y = 1$.
3. It is below or on the line $7x + 9y = 63$.
4. It is below or on the line $y = 5$.
5. It is to the left of or on the line $x = 6$.

By finding the intersection points of these boundary lines, the vertices of the feasible region are $(0,1)$, $(0,5)$, $\left(\dfrac{18}{7}, 5\right)$, $\left(6, \dfrac{7}{3}\right)$, $(6,0)$, and $(1,0)$.

Observing the given figures:
- Fig. 1 correctly represents the region bounded by all these conditions.
- Fig. 2 shades regions that violate $y \leq 5$ and $7x + 9y \leq 63$.
- Fig. 3 does not cover the entire feasible region down to the axes.
- Fig. 4 ignores the constraint $7x + 9y \leq 63$.

Thus, Fig. 1 is the correct graphical representation.

Answer: Fig. 1

</details>

---

### Q51. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The function to be maximized is given by $\mathrm{Z}=3 x+2 y$. The feasible region for this function is the shaded region given below, then the linear constraints for this region are given by
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/7ZMCit9oErCjL6yeJuBjAuoBOSmkJApfAkGQVrXqoc0.original.fullsize.png"/>

**Options:**

- **(A)** $3 x+8 y \leq 24,4 x+5 y \leq 20,5 x+3 y \geq 15$, $x \geq 0, y \geq 0$
- **(B)** $3 x+8 y \geq 24,4 x+5 y \geq 20,5 x+3 y \leq 15$, $x \geq 0, y \geq 0$
- **(C)** $3 x+8 y \leq 24,4 x+5 y \geq 20,5 x+3 y \geq 15$, $x \geq 0, y \geq 0$
- **(D)** $3 x+8 y \geq 24,4 x+5 y \leq 20,5 x+3 y \leq 15$, $x \geq 0, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 x+8 y \geq 24,4 x+5 y \leq 20,5 x+3 y \leq 15$, $x \geq 0, y \geq 0$**

**Detailed Solution:**

First, we find the equations of the three lines shown in the graph by identifying their x and y intercepts.

The first line passes through $(8, 0)$ and $(0, 3)$. Its equation is $\dfrac{x}{8} + \dfrac{y}{3} = 1 \Rightarrow 3x + 8y = 24$.

The second line passes through $(5, 0)$ and $(0, 4)$. Its equation is $\dfrac{x}{5} + \dfrac{y}{4} = 1 \Rightarrow 4x + 5y = 20$.

The third line passes through $(3, 0)$ and $(0, 5)$. Its equation is $\dfrac{x}{3} + \dfrac{y}{5} = 1 \Rightarrow 5x + 3y = 15$.

Next, we determine the inequalities that define the shaded region:

The shaded region lies above the line $3x + 8y = 24$ (it does not contain the origin). Therefore, the corresponding constraint is $3x + 8y \geq 24$.

The shaded region lies below the line $4x + 5y = 20$ (it is on the same side as the origin). Therefore, the corresponding constraint is $4x + 5y \leq 20$.

The shaded region lies below the line $5x + 3y = 15$ (it is on the same side as the origin). Therefore, the corresponding constraint is $5x + 3y \leq 15$.

Since the region is restricted to the first quadrant, we also have the non-negativity constraints $x \geq 0$ and $y \geq 0$.

Combining all these conditions, the linear constraints for the feasible region are $3x + 8y \geq 24$, $4x + 5y \leq 20$, $5x + 3y \leq 15$, $x \geq 0$, $y \geq 0$.

Answer: $3 x+8 y \geq 24,4 x+5 y \leq 20,5 x+3 y \leq 15$, $x \geq 0, y \geq 0$

</details>

---

### Q52. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $\mathrm{z}=4 x+2 y$, subject to the constraints $3 x+4 y \geqslant 12, x+y \leqslant 5, x, y \geqslant 0$ is

**Options:**

- **(A)** 8
- **(B)** 20
- **(C)** 24
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 20**

**Detailed Solution:**

The given objective function is $z = 4x + 2y$.

The constraints are $3x + 4y \ge 12$, $x + y \le 5$, $x \ge 0$, $y \ge 0$.

The feasible region is bounded by the lines $3x + 4y = 12$, $x + y = 5$, $x = 0$, and $y = 0$.

The corner points of the feasible region are $(4, 0)$, $(5, 0)$, $(0, 5)$, and $(0, 3)$.

Evaluating $z = 4x + 2y$ at these corner points:
At $(4, 0)$, $z = 4(4) + 2(0) = 16$
At $(5, 0)$, $z = 4(5) + 2(0) = 20$
At $(0, 5)$, $z = 4(0) + 2(5) = 10$
At $(0, 3)$, $z = 4(0) + 2(3) = 6$

The maximum value of $z$ is $20$.

Answer: 20

</details>

---

### Q53. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $\mathrm{z}=x+y$, subjected to $x+y \leq 10,5 x+3 y \geq 15, x \leq 6, x, y \geq 0$

**Options:**

- **(A)** occurs only at unique point.
- **(B)** occurs only at two distinct points.
- **(C)** occurs at infinitely many points.
- **(D)** does not exist.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) occurs at infinitely many points.**

**Detailed Solution:**

The given objective function is $z = x + y$.

The constraints are:
$x + y \leq 10$
$5x + 3y \geq 15$
$x \leq 6$
$x \geq 0, y \geq 0$

The feasible region is a bounded polygon with vertices at the intersections of the boundary lines. Let us find the vertices of the feasible region:
Intersection of $x = 0$ and $x + y = 10$ is $(0, 10)$.
Intersection of $x = 6$ and $x + y = 10$ is $(6, 4)$.
Intersection of $x = 6$ and $y = 0$ is $(6, 0)$.
Intersection of $y = 0$ and $5x + 3y = 15$ is $(3, 0)$.
Intersection of $x = 0$ and $5x + 3y = 15$ is $(0, 5)$.

Evaluating the objective function $z = x + y$ at these vertices:
At $(0, 10)$, $z = 0 + 10 = 10$
At $(6, 4)$, $z = 6 + 4 = 10$
At $(6, 0)$, $z = 6 + 0 = 6$
At $(3, 0)$, $z = 3 + 0 = 3$
At $(0, 5)$, $z = 0 + 5 = 5$

The maximum value of $z$ is $10$, which occurs at two adjacent vertices $(0, 10)$ and $(6, 4)$. Since the objective function is identical to the boundary of the constraint $x + y \leq 10$, the maximum value is attained at all points on the line segment joining $(0, 10)$ and $(6, 4)$.

Thus, the maximum value occurs at infinitely many points.

Answer: occurs at infinitely many points.

</details>

---

### Q54. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of the objective function $\mathrm{z}=4 x+6 y$ subject to $3 x+2 y \leq 12, x+y \geq 4, x$, $y \geq 0$ is

**Options:**

- **(A)** 24
- **(B)** 46
- **(C)** 56
- **(D)** 36

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 36**

**Detailed Solution:**

The given constraints are $3x + 2y \leq 12$, $x + y \geq 4$, $x \geq 0$, $y \geq 0$.

The feasible region is bounded by the lines $3x + 2y = 12$, $x + y = 4$, and the coordinate axes.

Finding the corner points of the feasible region:
Intersection of $3x + 2y = 12$ and $x + y = 4$ is $(4, 0)$.
Intersection of $x + y = 4$ and the y-axis ($x = 0$) is $(0, 4)$.
Intersection of $3x + 2y = 12$ and the y-axis ($x = 0$) is $(0, 6)$.

The corner points of the feasible region are $(4, 0)$, $(0, 4)$, and $(0, 6)$.

Evaluating the objective function $z = 4x + 6y$ at these corner points:
At $(4, 0)$, $z = 4(4) + 6(0) = 16$
At $(0, 4)$, $z = 4(0) + 6(4) = 24$
At $(0, 6)$, $z = 4(0) + 6(6) = 36$

The maximum value of $z$ is $36$.

Answer: 36

</details>

---

### Q55. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shaded area in the figure below is the solution set for a certain linear programming problem, then the linear constraints are given by
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/fvLTZlWlUx4LeoAR0e2E2Pw4iGaoE7vouuK8q5Wx9nE.original.fullsize_2.png"/>

**Options:**

- **(A)** $x \geqslant 1, y \leqslant 3, x-2 y \geqslant 2,6 x+7 \dot{y} \leqslant 42, x \geqslant 0, y \geqslant 0$
- **(B)** $x \geqslant 1, y \leqslant 3, x-2 y \geqslant 2,6 x+7 y \geqslant 42, x \geqslant 0, y \geqslant 0$
- **(C)** $x \leqslant 1, y \geqslant 3, x-2 y \leqslant 2,6 x+7 y \leqslant 42, x \geqslant 0, y \geqslant 0$
- **(D)** $x \geqslant 1, y \leqslant 3, x-2 y \leqslant 2,6 x+7 y \leqslant 42, x \geqslant 0, y \geqslant 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x \geqslant 1, y \leqslant 3, x-2 y \leqslant 2,6 x+7 y \leqslant 42, x \geqslant 0, y \geqslant 0$**

**Detailed Solution:**

From the given figure, the shaded region is bounded by four lines.

The vertical line is $x = 1$. The shaded region lies to the right of this line, giving the constraint $x \ge 1$.

The horizontal line is $y = 3$. The shaded region lies below this line, giving the constraint $y \le 3$.

The line intersecting the axes at $(7, 0)$ and $(0, 6)$ has the equation $\dfrac{x}{7} + \dfrac{y}{6} = 1 \Rightarrow 6x + 7y = 42$. The shaded region lies on the side containing the origin $(0, 0)$. Substituting the origin gives $0 \le 42$, which is true. Therefore, the constraint is $6x + 7y \le 42$.

The line passing through $(2, 0)$ and $(4, 1)$ has the equation $x - 2y = 2$. The shaded region lies on the side containing the origin $(0, 0)$ relative to this line. Substituting the origin gives $0 \le 2$, which is true. Therefore, the constraint is $x - 2y \le 2$.

The shaded region is located entirely in the first quadrant, which provides the non-negativity constraints $x \ge 0$ and $y \ge 0$.

Combining all these inequalities, the linear constraints defining the solution set are $x \ge 1$, $y \le 3$, $x - 2y \le 2$, $6x + 7y \le 42$, $x \ge 0$, $y \ge 0$.

</details>

---

### Q56. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The shaded region in the following figure is the solution set of the inequations
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/K0DFEfSLvTP6_RcBbAl6mNTsslvRS_WxzZ7xD9WaDoU.original.fullsize.png"/>

**Options:**

- **(A)** $x+2 y \geq 50,2 x+y \leq 100,2 x-y \leq 0$, $x, y \geq 0$
- **(B)** $x+2 y \leq 50,2 x+y \leq 100,2 x-y \leq 0$, $x, y \geq 0$
- **(C)** $x+2 y \geq 50,2 x+y \geq 100,2 x-y \leq 0$, $x, y \geq 0$
- **(D)** $x+2 y \leq 50,2 x+y \geq 100,2 x-y \leq 0$, $x, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x+2 y \geq 50,2 x+y \leq 100,2 x-y \leq 0$, $x, y \geq 0$**

**Detailed Solution:**

The shaded region is bounded by three lines and the y-axis. Let us find the equations of these lines.

Line 1 passes through the points $(0, 25)$ and $(50, 0)$.
Using the two-point form, the equation is:
$\dfrac{y - 25}{0 - 25} = \dfrac{x - 0}{50 - 0}$
$\Rightarrow \dfrac{y - 25}{-25} = \dfrac{x}{50}$
$\Rightarrow -2(y - 25) = x$
$\Rightarrow x + 2y = 50$
The shaded region lies above this line (away from the origin). Checking with a point in the region, say $(0, 50)$, we get $0 + 2(50) = 100 \geq 50$. Thus, the inequality is $x + 2y \geq 50$.

Line 2 passes through the points $(0, 100)$ and $(50, 0)$.
Using the intercept form, the equation is:
$\dfrac{x}{50} + \dfrac{y}{100} = 1$
$\Rightarrow 2x + y = 100$
The shaded region lies below this line (towards the origin). Checking with a point in the region, say $(0, 50)$, we get $2(0) + 50 = 50 \leq 100$. Thus, the inequality is $2x + y \leq 100$.

Line 3 passes through the points $(10, 20)$ and $(25, 50)$.
The slope is $m = \dfrac{50 - 20}{25 - 10} = \dfrac{30}{15} = 2$.
The equation is $y - 20 = 2(x - 10) \Rightarrow y = 2x \Rightarrow 2x - y = 0$.
The shaded region lies to the left of this line. Checking with a point in the region, say $(0, 50)$, we get $2(0) - 50 = -50 \leq 0$. Thus, the inequality is $2x - y \leq 0$.

Since the region is in the first quadrant, we also have $x \geq 0$ and $y \geq 0$.

Combining all these, the system of inequalities is:
$x + 2y \geq 50$
$2x + y \leq 100$
$2x - y \leq 0$
$x, y \geq 0$

Answer: $x+2 y \geq 50,2 x+y \leq 100,2 x-y \leq 0$, $x, y \geq 0$

</details>

---

### Q57. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The point, at which the maximum value of $10 x+6 y$ subject to the constraints $x+y \leq 12$, $2 x+y \leq 20, x \geq 0, y \geq 0$ occurs, is

**Options:**

- **(A)** $(10,0)$
- **(B)** $(8,4)$
- **(C)** $(0,12)$
- **(D)** $(12,0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(8,4)$**

**Detailed Solution:**

The objective function to be maximized is $Z = 10x + 6y$.

The given constraints are:
$x + y \leq 12$
$2x + y \leq 20$
$x \geq 0, y \geq 0$

To find the corner points of the feasible region, we solve the equations of the boundary lines:
1) $x + y = 12$
2) $2x + y = 20$

Subtracting the first equation from the second gives:
$(2x + y) - (x + y) = 20 - 12 \Rightarrow x = 8$

Substituting $x = 8$ in the first equation gives:
$8 + y = 12 \Rightarrow y = 4$
Thus, the point of intersection is $(8, 4)$.

The other corner points of the bounded feasible region are the origin $(0, 0)$, the x-intercept of $2x + y = 20$ which is $(10, 0)$, and the y-intercept of $x + y = 12$ which is $(0, 12)$.

Now, we evaluate the objective function $Z = 10x + 6y$ at each corner point:
At $(0, 0)$: $Z = 10(0) + 6(0) = 0$
At $(10, 0)$: $Z = 10(10) + 6(0) = 100$
At $(0, 12)$: $Z = 10(0) + 6(12) = 72$
At $(8, 4)$: $Z = 10(8) + 6(4) = 80 + 24 = 104$

The maximum value of $Z$ is $104$, which occurs at the point $(8, 4)$.

Answer: $(8,4)$

</details>

---

### Q58. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The shaded region in the following figure represents the solution set for a certain linear programming problem. Then linear constraints for this region are given by
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Ax4YYFjoecwH0pMt0_fvYwXtkOK06e1nYSubV7fMNrQ.original.fullsize.png">

**Options:**

- **(A)** $\begin{aligned} 2 x+3 y \geq 6,-x+2 y & \geq 2,3 x+6 y \leq 18, \\ x-3 y & \geq 3, x \geq 0, y \geq 0\end{aligned}$
- **(B)** $\begin{aligned} 2 x+3 y \geq 6,-x+2 y & \leq 2, x-3 y \leq 3 \\ x+2 y & \geq 18, x \geq 0, y \geq 0\end{aligned}$
- **(C)** $\begin{aligned} 2 x+3 y \leq 6,-x+2 y & \geq 2,3 x+6 y \leq 18 \\ x-3 y & \leq 3, x \geq 0, y \geq 0\end{aligned}$
- **(D)** $\begin{aligned} 2 x+3 y \geq 6,3 x+6 y & \leq 18, x-3 y \leq 3 \\ -x+2 y & \leq 2, x \geq 0, y \geq 0\end{aligned}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\begin{aligned} 2 x+3 y \geq 6,3 x+6 y & \leq 18, x-3 y \leq 3 \\ -x+2 y & \leq 2, x \geq 0, y \geq 0\end{aligned}$**

**Detailed Solution:**

Shaded region lies on origin side of $3 x+6 y=18, x-3 y=3,-x+2 y=2$ and on non-origin side of $2 x+3 y=6$.
$\begin{aligned}
\therefore \quad & 2 x+3 y \geq 6,3 x+6 y \leq 18, x-3 y \leq 3, \\
& -x+2 y \leq 2, x \geq 0, y \geq 0
\end{aligned}$

</details>

---

### Q59. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The solution set of the inequalities $4 x+3 y \leq 60, y \geq 2 x, x \geq 3, x, y \geq 0$ is represented by region
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/EF_jKbNewBhcPAmb9TH764jmmzrQ8O9hky4PDoNlT0Q.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{S}_2$ region
- **(B)** $\mathrm{S}_1$ region
- **(C)** $\mathrm{S}_3$ region
- **(D)** $\mathrm{S}_4$ region

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{S}_2$ region**

**Detailed Solution:**

Take a test point $(4,10)$ that lies within the $S_2$ region.
$$
\begin{aligned}
& \text { Since } 4(4)+3(10)=46 \leq 60,10 \geq 2(4)=8, \\
& 4 \geq 3,4 \geq 0,10 \geq 0
\end{aligned}
$$
$\therefore \quad$ The solution set is represented by $\mathrm{S}_2$ region.

</details>

---

### Q60. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The shaded area in the given figure is a solution set for some system of inequations. The maximum value of the function $z=10 x+25 y$ subject to the linear constraints given by the system is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/lmBRGspBceSYXH1kvdG5jTsi8Tz9LbaNokOFaMYcsRw.original.fullsize.png">

**Options:**

- **(A)** 80
- **(B)** 100
- **(C)** 95
- **(D)** 105

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 95**

**Detailed Solution:**

$\begin{aligned} & \text { At }(0,0), z=10(0)+25(0)=0 \\ & \text { At }(3,0), z=10(3)+25(0)=30 \\ & \text { At }(3,2), z=10(3)+25(2)=80 \\ & \text { At }(2,3), z=10(2)+25(3)=95 \\ & \text { At }(0,3), z=10(0)+25(3)=75\end{aligned}$
$\therefore \quad$ Maximum value of $\mathrm{z}$ is 95 .

</details>

---

### Q61. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If feasible region is as shown in the figure, then related inequalities are
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/apobd1UzWbzxy9RSq2tZ1rUHQPFbnby_xInlhJluboU.original.fullsize.png">

**Options:**

- **(A)** $$
\begin{aligned}
& 3 x+4 y \geq 12,4 x+7 y \leq 28, y \leq 1, x \geq 0, \\
& y \geq 0
\end{aligned}
$$
- **(B)** $$
\begin{aligned}
& 3 x+4 y \geq 12,4 x+7 y \leq 28, y \geq 1, x \geq 0, \\
& y \geq 0
\end{aligned}
$$
- **(C)** $$
\begin{aligned}
& 3 x+4 y \leq 12,4 x+7 y \leq 28, y \leq 1, x \geq 0, \\
& y \geq 0 \\
& 3 x+4 y \leq 12,4 x+7 y \geq 28, y \geq 1, x \geq 0, \\
& y \geq 0
\end{aligned}
$$
- **(D)** $$
\begin{aligned}
& 3 x+4 y \leq 12,4 x+7 y \geq 28, y \geq 1, x \geq 0, \\
& y \geq 0
\end{aligned}
$$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $$
\begin{aligned}
& 3 x+4 y \geq 12,4 x+7 y \leq 28, y \geq 1, x \geq 0, \\
& y \geq 0
\end{aligned}
$$**

**Detailed Solution:**

Shaded region lies on origin side of $4 x+7 y=28$ and above the line $y=1$, and on non-origin side of $3 x+4 y=12$.
$$
\therefore \quad 3 x+4 y \geq 12,4 x+7 y \leq 28, y \geq 1, x \geq 0, y \geq 0
$$

</details>

---

### Q62. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of $z=7 x+8 y$ subject to the constraints $x+y \leq 20, y \geq 5, x \leq 10, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** $150$
- **(B)** $160$
- **(C)** $110$
- **(D)** $180$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $160$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ZnbWLKQBZpWRokJLG2AdCdky8909p4ZVok_N-VqKICQ.original.fullsize.png">

Feasible region lies on the origin side of lines $x+y=20, x=10$ and on non-origin side of $y=5$.
$\therefore \quad$ Corner points of the feasible region are $\mathrm{A}(0,5), \mathrm{B}(10,5), \mathrm{C}(10,10)$ and $\mathrm{D}(0,20)$
$\mathrm{z}$ at $\mathrm{A}(0,5)=40$
$\mathrm{z}$ at $\mathrm{B}(10,5)=110$
$\mathrm{z}$ at $\mathrm{C}(10,10)=150$
$\mathrm{z}$ at $\mathrm{D}(0,20)=160$
$\therefore \quad$ Maximum value of $\mathrm{z}$ is 160 .

</details>

---

### Q63. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For a feasible region $O C D B O$ given below, the maximum value of the objective function $z=3 x+4 y$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/QIxOZecOlgfqHbc4sM5wzGTPLsJMelJ8EnbPppbsdR8.original.fullsize.png">

**Options:**

- **(A)** 70
- **(B)** 100
- **(C)** 110
- **(D)** 130

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 110**

**Detailed Solution:**

Corner points of the given feasible region are $\mathrm{O}(0,0), \mathrm{C}(10,10), \mathrm{D}(10,20), \mathrm{B}(0,25)$
$\therefore \quad \mathrm{z}$ at $\mathrm{C}(10,10)=70$,
$\mathrm{z}$ at $\mathrm{D}(10,20)=110$,
$\mathrm{z}$ at $\mathrm{B}(0,25)=100$
$\therefore \quad$ The maximum value of $\mathrm{z}$ is 110 .

</details>

---

### Q64. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of $\mathrm{z}=3 x+5 y$ subject to the constraints $3 x+2 y \leq 18, x \leq 4, y \leq 6$, $x, y \geq 0$, is

**Options:**

- **(A)** $27$
- **(B)** $36$
- **(C)** $42$
- **(D)** $30$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $36$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/fGV4EwQNywS3unNiPcDmgStU1JstSmxss1iaRMXCFiE.original.fullsize.png">

Objective function $\mathrm{z}=3 x+5 y$
The comer points of the feasible region are $\mathrm{O}(0,0), \mathrm{A}(4,0), \mathrm{B}(4,3), \mathrm{C}(2,6)$ and $\mathrm{D}(0,6)$
$\therefore \quad \mathrm{Z}$ at $\mathrm{A}(4,0)=12$
$\mathrm{Z}$ at $\mathrm{B}(4,3)=27$
$\mathrm{Z}$ at $\mathrm{C}(2,6)=36$
$\mathrm{Z}$ at $\mathrm{D}(0,6)=30$
$\therefore \quad$ Maximum value of $\mathrm{Z}$ is 36 .

</details>

---

### Q65. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the following shaded area, the linear constraints except $x, y \geq 0$ are
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/N5FmGB2bs4R_BcR1stC8_ZD1tENBQgZ7OiDpTR02TD8.original.fullsize.png">

**Options:**

- **(A)** $2 x+y \leq 2, x-y \leq 1, x+2 y \leq 8$
- **(B)** $2 x+y \geq 2, x-y \leq 1, x+2 y \leq 8$
- **(C)** $2 x+y \geq 2, x-y \geq 1, x+2 y \leq 8$
- **(D)** $2 x+y \geq 2, x-y \geq 1, x+2 y \geq 8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 x+y \geq 2, x-y \leq 1, x+2 y \leq 8$**

**Detailed Solution:**

Shaded region lies on non-origin side of $2 x+y=2$ and on origin side of the lines $x-y=1$ and $x+2 y=8$
$$
\therefore \quad 2 x+y \geq 2, x-y \leq 1, x+2 y \leq 8
$$

</details>

---

### Q66. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The graphical solution set for the system of inequations
$x-2 y \leq 2,5 x+2 y \geq 10,4 x+5 y \leq 20, x \geq 0,$
$y \geq 0$ is given by
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/HKQQabIsBNnVlpAYm_9Ety94-8Hs8ZjorKfFK0oI37A.original.fullsize.png">

**Options:**

- **(A)** Fig.2
- **(B)** Fig.4
- **(C)** Fig.1
- **(D)** Fig.1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Fig.1**

**Detailed Solution:**

Feasible region lies on origin side of $x-2 y=2$, $4 x+5 y=20$ and on non-origin side of $5 x+2 y=10$, in $1^{\text {st }}$ quadrant.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/rgLQ1mQBa15XUkTmm05joPxl6OxAuK7pRh3N04lXyFk.original.fullsize.png">

Fig.3

</details>

---

### Q67. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If feasible region is as shown in the figure, then the related inequalities are
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Pvs80lu6JbwJCFZBWCuBGac0zMMBzaAZqcXtYUftK_I.original.fullsize.png">

**Options:**

- **(A)** $3 x+4 y \geq 12, y-x \geq 0, y \leq 3, x, y \geq 0$
- **(B)** $3 x+4 y \leq 12, y-x \leq 0, y \geq 3, x, y \geq 0$
- **(C)** $3 x+4 y \leq 12, y-x \geq 0, y \leq 3, x, y \geq 0$
- **(D)** $3 x+4 y \geq 12, y-x \leq 0, y \geq 3, x, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3 x+4 y \geq 12, y-x \geq 0, y \leq 3, x, y \geq 0$**

**Detailed Solution:**

The shaded region lies:
on non-origin side of line $3 x+4 y=12$ i.e., $3 x+4 y \geq 12$,
on the side of the line $y-x=0$, where $y \geq x$ i.e., $y-x \geq 0$,
on origin side of line $y=3$
i.e., $y \leq 3$,
and in first quadrant
i.e., $x \geq 0, y \geq 0$.

</details>

---

### Q68. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shaded area in the figure below is the solution set for a Certain Linear Programming problem. The linear constraints are given by
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wqrKHLBSvSkGRc2eJNKIDYR-OPmpqCPXEcM9e-0VI10.original.fullsize.png">

**Options:**

- **(A)** $3 x+4 y \leq 18,2 x+3 y \geq 3, x-6 y \geq 3,-x+2 y \leq 2, x \geq 0, y \geq 0$
- **(B)** $3 x+4 y \leq 18,2 x+3 y \geq 3, x-6 y \leq 3,-x+2 y \leq 2, x \geq 0, y \geq 0$
- **(C)** $3 x+4 y \leq 18,2 x+3 y \geq 3, x-6 y \geq 3,-x+2 y \geq 2, x \geq 0, y \geq 0$
- **(D)** $3 x+4 y \leq 18,2 x+3 y \leq 3, x-6 y \geq 3,-x+2 y \leq 2, x \geq 0, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 x+4 y \leq 18,2 x+3 y \geq 3, x-6 y \leq 3,-x+2 y \leq 2, x \geq 0, y \geq 0$**

**Detailed Solution:**

The shaded region is represented by
$3 x+4 y \leq 18,2 x+3 y \geq 3, x-6 y \leq 3,-x+2 y \leq 2, x \geq 0, y \geq 0$

</details>

---

### Q69. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The feasible region represented by the inequations $2 x+3 y \leq 18$, $x+y^3 10, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** a finite set.
- **(B)** unbounded.
- **(C)** bounded.
- **(D)** an empty set.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) an empty set.**

**Detailed Solution:**

$2 x+3 y \leq 18, x+y \geq 10, x \geq 0, y \geq 0$
Feasible region is an empty set
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/nj_vknyg_1G4gY8qtzDJFJaI1LOE2VN8IcV-xwt1RFk.original.fullsize.png">

</details>

---

### Q70. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the inequalities $x+y \leq 3,2 x+5 y \geq 10, x \geq 0, y \geq 0$, which of the following points lies in the feasible region?

**Options:**

- **(A)** $(2,2)$
- **(B)** $(4,2)$
- **(C)** $(1,2)$
- **(D)** $(2,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(1,2)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ujLYbt479_v_7PCIe36HpL1UYa9W4KZ-6jVC1lYj9-g.original.fullsize.png">
$(1,2)$ lies in the feasible region

</details>

---

### Q71. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function to be maximized is given by $Z=2 x+y$. The feasible region for this function $Z$ is the shaded region given below. The maximum value of $Z$ is <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/LKODp2gGRpRgqtE4wd9IV-qKSbILARqRcEXwCHWwQKE.original.fullsize.png">

 and occurs at the point<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/x8UmgOfP2StxyFCRE2Fbnk2oZm0cSQHjDQoxG6qJFOw.original.fullsize.png">
.<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_a2BL8a_hpMX6UM0YOKdj6ISJJMuUB3_T0cMSiovssM.original.fullsize.png">

**Options:**

- **(A)** $10,(5,0)$
- **(B)** $12,(6,0)$
- **(C)** $9,(1.5,6)$
- **(D)** $21,(0.5,0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $12,(6,0)$**

**Detailed Solution:**

Corner points are $(0,5),(5,0),(6,0),(0,7)$ and $\left(\frac{3}{2}, 6\right)$ $Z=2 x+y$ is maximum at $(6,0)$
$Z_{\max }=2 \times 6+0=12$

</details>

---

### Q72. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the following shaded region, the linear constraints are
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/CANU9MXusSiH3an4j888DrWmXk_zOioQQCLcOoosgQE.original.fullsize.png">

**Options:**

- **(A)** $x+2 y \leq 6,5 x+3 y \leq 15, x \leq 7, y \leq 6, x, y \geq 0$
- **(B)** $x+2 y \leq 6,5 x+3 y \geq 15, x \leq 7, y \leq 6, x, y \geq 0$
- **(C)** $x+2 y \geq 6,5 x+3 y \leq 15, x \leq 7, y \leq 6, x, y \geq 0$
- **(D)** $x+2 y \geq 6,5 x+3 y \geq 15, x \leq 7, y \leq 6, x, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x+2 y \geq 6,5 x+3 y \geq 15, x \leq 7, y \leq 6, x, y \geq 0$**

**Detailed Solution:**

The shaded region is represented by
$x+2 y \geq 6,5 x+3 y \geq 15, x \leq 7, y \leq 6, x, y \geq 0$

</details>

---

### Q73. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $z=50 x+15 y$ subject to the constraints $x+y \leq 60 ; 5 x+y \leq 100 ; x \geq 0 ; y \geq 0$ is at the point

**Options:**

- **(A)** $2650,(50,10)$
- **(B)** $1000,(20,0)$
- **(C)** $900,(0,60)$
- **(D)** $1250,(10,50)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1250,(10,50)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Km6djyZ-PNVTlfKD0YEl0t--ESrmxPKrOdz8dPvT85g.original.fullsize.png">
$\mathrm{Z}_{\text {max. }}$ at $(10,50)$
$\begin{aligned} & Z_{\text {max. }}=50 \times 10+15 \times 50 \\ & =500+750 \\ & =1250\end{aligned}$

</details>

---

### Q74. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The objective function of L.L.P defined over the convex set attains its optimum value at

**Options:**

- **(A)** all the corner points.
- **(B)** at least two of the corner points.
- **(C)** none of the corner points.
- **(D)** at least one of the corner points.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) at least one of the corner points.**

**Detailed Solution:**

At least one of the corner point.

</details>

---

### Q75. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Maximum value of $Z=5 x+2 y$, subject to $2 x-y \geq 2, x+2 y \leq 8$ and $x, y \geq 0$ is

**Options:**

- **(A)** $28$
- **(B)** $25.6$
- **(C)** $40$
- **(D)** $17.6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $40$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/AXzcNHACXiWEkIWPYI0lWACbks7URpbg2j_hdqKxT-Q.original.fullsize.png">
$\mathrm{z}=5 x+2 y$
$\mathrm{z}_{\text {max. }}=5 \times 8+2 \times 0=40$

</details>

---

### Q76. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Cost function $\mathrm{Z}$ given by $\mathrm{Z}=4 \mathrm{x}+6 \mathrm{y}$ is to be minimized. The fessible region for this function $\mathrm{Z}$ is the shaded region represented in the following figure. Then the minimum value of $\mathrm{Z}$ is and occurs at the point
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/uxPmBi-SBXmqGWn9GFhfckl9YWnRRgjwM_BIFmXagSk.original.fullsize.png"/>)

**Options:**

- **(A)** $260,(20,30)$
- **(B)** $240,(0,40)$
- **(C)** $100,(25,0)$
- **(D)** $254,(14,33)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $254,(14,33)$**

**Detailed Solution:**

Here corner points are $(80,0),(0,80)$ and $(14,33)$
$\mathrm{Z}$ is minimum at $(14,33)$ and $\mathrm{Z}_{\min }=4 \times 14+6 \times 33=254$

</details>

---

### Q77. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of the objective function $\mathrm{z}=4 \mathrm{x}+5 \mathrm{y}$ subject to constraints $2 x+3 y \leq 12,2 x+y \leq 8$ and $x \geq 0, y \geq 0$ is

**Options:**

- **(A)** 24
- **(B)** 23
- **(C)** 22
- **(D)** 21

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 22**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/xH7mE1R9XfuJHM-NytN7XuYIh8_Jho2V2O4p2KtNTzQ.original.fullsize.png">
$z=4 x+5 y$
$\mathrm{z}_{\max }=4 \times 3+5 \times 2=22$

</details>

---

### Q78. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The graphical solution set of the system of in equations $\mathrm{x}+\mathrm{y} \leq 70, \mathrm{x}+2 \mathrm{y} \leq 100,2 \mathrm{x}+\mathrm{y} \leq 120, \mathrm{x} \geq 0, \mathrm{y} \geq 0$ is given by
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/dQCAJcqylS9GY2tdFMjTmalOLqNUWCQL8Q4mCeMmC6U.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/L_ocXuJEEq9UA_VQaRcL1LNK81KCOKi2Ut1KRvSmoPs.original.fullsize.png">

**Options:**

- **(A)** Fig.2
- **(B)** Fig.1
- **(C)** Fig.4
- **(D)** Fig.3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Fig.3**

**Detailed Solution:**

$\because \mathrm{x}+\mathrm{y} \leq 70, \mathrm{x}+2 \mathrm{y} \leq 100$ and $2 \mathrm{x}+\mathrm{y} \leq 120$ all are satisfied by $(0,0)$
Hence, we should take common side containing the origin which is represented by fig. 3

</details>

---

### Q79. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The region represented by the inequalities $x \geq 6, y \geq 3$, $2 x+y \geq 10, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** origin side of all the inequalities
- **(B)** unbounded
- **(C)** polygon
- **(D)** bounded

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) unbounded**

**Detailed Solution:**

Refer figure
Require area is shaded.
Area is unbounded.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/x0rdSl6yi-4m7Wk2-JRLQRLb8P3mKJ7zKQPYxA_7_vs.original.fullsize.png">

</details>

---

### Q80. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The minimum value of the objective function $z=4 x+6 y$ subject to $x+2 y \geq 80,3 x+y \geq 75, x, y \geq 0$ is

**Options:**

- **(A)** 324
- **(B)** 250
- **(C)** 320
- **(D)** 254

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 254**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ejAnBvM_9IUFfp6PBnEYklj5t0Tlrk66UDYnhsqwO14.original.fullsize.png">

Refer figure
Required area is shaded. Vertices of feasible region are $\mathrm{A}=(80,0) ; \mathrm{C}=(0,75)$ and point of intersection of given lines is $\mathrm{B}=(14,33)$
We have to minimize objective function $\mathrm{z}=4 \mathrm{x}+6 \mathrm{y}$
$$
\begin{aligned}
& \therefore \quad \mathrm{Z}_{(\mathrm{A})}=4(80)+6(0)=320 \\
& \mathrm{Z}_{(\mathrm{B})}=4(14)+6(33)=254 \\
& \mathrm{Z}_{(\mathrm{C})}=4(0)+6(75)=450 \\
&
\end{aligned}
$$

</details>

---

### Q81. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of the objective function $\mathrm{z}=2 \mathrm{x}+3 \mathrm{y}$ subject to the constraints $\mathrm{x}+\mathrm{y} \leq 5,2 \mathrm{x}+\mathrm{y} \geq 4$ and $\mathrm{x} \geq 0, \mathrm{y} \geq 0$ is

**Options:**

- **(A)** 15
- **(B)** 10
- **(C)** 20
- **(D)** 25

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 15**

**Detailed Solution:**

Refer Figure
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/pt-Ejs8KkTV8wf5VFETsUnw06SfPPxCyLBrDgarcrBI.original.fullsize.png">

Required part is shaded.
We have $\mathrm{A}=(0,4)$;
$$
\begin{aligned}
& \mathrm{B}=(2,0) ; \mathrm{C}=(5,0) \\
& \mathrm{D}=(0,5)
\end{aligned}
$$
We have to maximize function
$$
\begin{aligned}
\mathrm{Z}=2 \mathrm{x} & +3 \mathrm{y} \\
\therefore \quad \mathrm{z}_{\mathrm{A}} & =2(0)+3(4)=12 \\
\mathrm{Z}_{\mathrm{B}} & =2(2)+3(0)=4 \\
\mathrm{Z}_{\mathrm{C}} & =2(5)+3(0)=10 \\
\mathrm{Z}_{\mathrm{D}} & =2(0)+3(5)=15
\end{aligned}
$$

</details>

---

### Q82. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The common region of the solution of the inequations $x+2 y \geq 4,2 x-y \leq 6$ and $x, y>0$ is

**Options:**

- **(A)** bounded and origin side
- **(B)** unbounded and non-origin side
- **(C)** unbounded and origin side
- **(D)** bounded and non-origin side

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) unbounded and non-origin side**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/fMt-shO1J-9K4ID1q8axbc2oMaoKe9iQVzxPL0jI2XM.original.fullsize.png">

</details>

---

### Q83. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The common region of the solution of the inequations $x+y \geq 5$, $y \leq 4, x \geq 2, x, y \geq 0$ is

**Options:**

- **(A)** unbounded and non-origin side
- **(B)** unbounded and origin side
- **(C)** bounded and origin side
- **(D)** bounded and non-origin side

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) unbounded and non-origin side**

**Detailed Solution:**

Refer Figure
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/yTrVHxWNHLXdSvCZqCM5KJpRUUhkXIYpOzbH1fsJMWc.original.fullsize.png">

Required area is shaded.
It is unbounded and non-origin side.

</details>

---

### Q84. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $z=10 z+25 y$ subject to $0 \leq x \leq 3$, $0 \leq y \leq 3, x+y \leq 5$ occurs at the point.

**Options:**

- **(A)** $(3,2)$
- **(B)** $(2,3)$
- **(C)** $(4,3)$
- **(D)** $(5,4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(2,3)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/R_rcil7xj7qNqc5P2w6RfG80Dbr9YXtT-_VIDMR2vuA.original.fullsize.png">

Required area is shaded.
Vertices of the required region are $0(0,0)$;
$$
\mathrm{A}(3,0) ; \mathrm{B}(3,2) ; \mathrm{C}(2,3) ; \mathrm{D}(0,3)
$$
We have to maximize objective function
$$
\begin{array}{lll}
\mathrm{Z}=10 \mathrm{x}+25 \mathrm{y} & \\
\therefore \quad & \mathrm{Z}_{(\mathrm{O})}=0+0 & =0 \\
\mathrm{Z}_{(\mathrm{A})} & =30+0 & =30 \\
\mathrm{z}_{(\mathrm{B})} & =30+50 & =80 \\
\mathrm{Z}_{(\mathrm{C})} & =20+75 & =95 \\
\mathrm{z}_{(\mathrm{D})} & =0+75 & =75
\end{array}
$$

</details>

---

### Q85. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The objective function $\mathrm{z}=4 \mathrm{z}+5 \mathrm{y}$ subjective to $2 \mathrm{x}+\mathrm{y} \geq 7$; $2 x+3 y \leq 15 ; y \leq 3, x \geq 0 ; y \geq 0$ has minimum value at the point.

**Options:**

- **(A)** on the line $2 x+3 y=15$
- **(B)** on X-axis
- **(C)** on Y-axis
- **(D)** origin

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) on X-axis**

**Detailed Solution:**

We have lines $2 x+y=7,2 x+3 y=15, y=3$ Refer figure
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/7poEkVkaZcHksKT_5d0YzQdx1zfFJeHTaRQIiFdBBIg.original.fullsize.png">

The required region is shaded.
We have $\mathrm{A} \equiv\left(\frac{7}{2}, 0\right), \mathrm{B} \equiv\left(\frac{15}{2}, 0\right)$
Point of intersection of $2 x+y=7$ and $y=3$ is $D=(2,3)$
$$
\begin{aligned}
& \mathrm{z}_{(\mathrm{A})}=4\left(\frac{7}{2}\right)+5(0)=14+0=14 \\
& \mathrm{z}_{(\mathrm{B})}=5\left(\frac{15}{2}\right)+5(0)=30+0=30 \\
& \mathrm{z}_{(\mathrm{C})}=4(3)+5(3)=12+15=27 \\
& \mathrm{z}_{(\mathrm{D})}=4(2)+5(3)=8+15=23
\end{aligned}
$$
Hence minimum value occurs at point a which lies on $\mathrm{X}$ axis.

</details>

---

### Q86. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shaded figure given below is the solution set for the linear inequations. Choose the correct option
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/t1S4Fg4KMEfwprSTxtdfobcKyqUV7He0aYZRXu2wuys.original.fullsize.png">

**Options:**

- **(A)** $$
3 x+4 y \geq 18 ; x-6 y \leq 3 ; 2 x+3 y \geq 3 ; 7 x-14 \leq 14 ; x \geq
$$
$$
0 ; \mathrm{y} \geq 0
$$
- **(B)** $$
3 x+4 y \leq 18 ; x-6 y \leq 3 ; 2 x+3 y \leq 3 ;-7 x+14 \geq 14 ; x \geq
$$
$$
0 ; \mathrm{y} \geq 0
$$
- **(C)** $$
\begin{aligned}
& 3 x+4 y \leq 18 ; x-6 y \leq 3 ; 2 x+3 y \geq 3 ;-7 x+14 \leq 14 ; x \geq \\
& 0 ; y \geq 0
\end{aligned}
$$
- **(D)** $3 \mathrm{x}+4 \mathrm{y} \geq-18 ; \mathrm{x}-6 \mathrm{y} \leq 3 ; 2 \mathrm{x}+3 \mathrm{y} \leq 3 ;-7 \mathrm{x}+14 \geq 14 ; \mathrm{x} \geq 0 ; \mathrm{y} \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $$
\begin{aligned}
& 3 x+4 y \leq 18 ; x-6 y \leq 3 ; 2 x+3 y \geq 3 ;-7 x+14 \leq 14 ; x \geq \\
& 0 ; y \geq 0
\end{aligned}
$$**

**Detailed Solution:**

For the shaded region, inequalities are as follows, $x \geq 0, y \geq 0,2 x+3 y \geq 3, x-6 y \leq 3,3 x+4 y \leq 18,-7 x+14 y \leq 14$ Note:
$$
-7 x+14 y=14 \Rightarrow 7 x-14=-14 \text { and } 0>-14
$$

</details>

---

### Q87. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The solution set for the system of linear inequations $\mathrm{x}+\mathrm{y} \geq 1 ; 7 \mathrm{x}+9 \mathrm{y} \leq 63 ; \mathrm{y} \leq 5 ; \mathrm{x} \leq 6, \mathrm{x} \geq 0$ and $\mathrm{y} \geq 0$ is represented graphically in the figure. What is the correct option?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/WmfWcKZJthflRq0omD_C4doBqzIo06LPa8iuEA_1nW0.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/JpGmTCtY5xmJIR_-bX1g544RbWRufy97UOEKOLyufjU.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/lpmbcY0IKbBRWulOft6t_bHuaNznPldRG07su8-TiDk.original.fullsize.png">
1
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/FgRaCAceKdtFJDWLv3Wg7uYCxDYjMrrjqHOG4BYBlk8.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/WmfWcKZJthflRq0omD_C4doBqzIo06LPa8iuEA_1nW0.original.fullsize.png">**

**Detailed Solution:**

Lines are $x+y=1,7 x+9 y=63, y=5, x=6$
The required area is shaded
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/22s6NmYB-irK2TdnF_SaDK_dtwzEMGjDOUMw_1_CyRM.original.fullsize.png">

</details>

---

### Q88. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The shaded part of the given figure indicates the feasible region. Then the constraints are
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/mdR0uxs6XlYZQxBcSZmIdk2IJvIhsrb06D3B_NgU9w4.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{x}, \mathrm{y} \geq 0 ; \mathrm{x}-\mathrm{y} \geq 0 ; \mathrm{x} \leq 5 ; \mathrm{y} \leq 3$
- **(B)** $x, y \geq 0 ; x-y \geq 0 ; x \leq 5 ; y \geq 3$
- **(C)** $\mathrm{x}, \mathrm{y} \geq 0 ; \mathrm{x}+\mathrm{y} \geq 0 ; \mathrm{x} \geq 5 ; \mathrm{y} \leq 3$
- **(D)** $x, y \geq 0 ; x-y \geq 0 ; x \geq 5 ; y \leq 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{x}, \mathrm{y} \geq 0 ; \mathrm{x}-\mathrm{y} \geq 0 ; \mathrm{x} \leq 5 ; \mathrm{y} \leq 3$**

**Detailed Solution:**

Here equation of line $\mathrm{OC}$ is $\mathrm{y}=\mathrm{x}$ i.e. $\mathrm{x}-\mathrm{y}=0$ and equation of line $\mathrm{AB}$ is $\mathrm{x}=5$ i.e. $\mathrm{x}-5=0$
Equation of line $\mathrm{BC}$ is $\mathrm{y}=3$ i.e. $\mathrm{y}-3=0$
Hence constraints for the shaded region are $x, y \geq 0, x-5 \leq 0, x$
$$
\begin{aligned}
& -y \geq 0, y-\leq 0 \\
& \text { i.e. } x, y \geq 0, x \leq 5, x-y \geq 0, y \leq 3
\end{aligned}
$$

</details>

---

### Q89. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If L. P. P. has optimum solutions at two consecutive corner points of feasible region, then L. P. P. has

**Options:**

- **(A)** infinite solutions
- **(B)** no solution
- **(C)** two solutions
- **(D)** unique solution

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) infinite solutions**

**Detailed Solution:**

This is by definition.

</details>

---

### Q90. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of the objective function $\mathrm{Z}=5 x+8 \mathrm{y}$, subject to $x+\mathrm{y} \geq 5$
$x \leq 4, y \leq 2, x \geq 0, y \geq 0$ occur at the point

**Options:**

- **(A)** $(5,0)$
- **(B)** $(0,5)$
- **(C)** $(4,2)$
- **(D)** $(4,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(4,1)$**

**Detailed Solution:**

Feasible area is shaded.
Vertices of the feasible region are $A \equiv(4,1), B \equiv(4,2), C \equiv(3,2)$
$\therefore Z(A)=(5 \times 4)+(8 \times 1)=20+8=28$
$Z(B)=(5 \times 4)+(8 \times 2)=20+16=36$
$Z(C)=(5 \times 3)+(8 \times 2)=15+16=31$
Minima is at $(4,1)$

</details>

---

### Q91. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The L. P. P. to maximize $\mathrm{Z}=x+y$, subject to $x+y \leq 1,2 x+2 y \geq 6, x \geq 0, y \geq 0$
has

**Options:**

- **(A)** no solution.
- **(B)** infinite solutions.
- **(C)** one solution.
- **(D)** two solutions.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) no solution.**

**Detailed Solution:**

(A)
Thus there is no common feasible area. Hence given L.P.P. has no solution.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/c-1MRDW5c47_jzLkwscBNOW23WXOIvaxgLVcXJcOMm8.original.fullsize.png">

</details>

---

### Q92. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{Z}=10 x+25 y$ subject to $0 \leq x \leq 3,0 \leq y \leq 3, x+y \leq 5, x \geq 0, \mathrm{y} \geq 0$ then $\mathrm{z}$ is
maximum at the point

**Options:**

- **(A)** $(2,4)$
- **(B)** $(1,6)$
- **(C)** $(2,3)$
- **(D)** $(4,3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(2,3)$**

**Detailed Solution:**

(A)
First we draw the lines $A B, C D$ and $E F$ whose equation are $x=3, y=3$ and $x+y=5$ respectively.
\begin{array}{|c|c|c|c|c|c|}
\hline Line & Equation & Points on the X-axis & Points on the Y-axis & Sign & Region \\
\hline \mathrm{AB} & \mathrm{x}=3 & \mathrm{~A}(3,0) & - & \leq & origin side of line AB \\
\hline \mathrm{CD} & \mathrm{y}=3 & - & \mathrm{D}(0,3) & \leq & origin side of line CD \\
\hline \mathrm{EF} & \mathrm{x}+\mathrm{y}=5 & \mathrm{E}(5,0) & \mathrm{F}(0,5) & \leq & origin side of line EF \\
\hline
\end{array}
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/B4kzN-9ePWEUBFHsHXkSNmOaJWNjiAtxAI2H9WvK8kg.original.fullsize.png">

The feasible region is OAPQDO which is shaded in the graph.
The vertices of the feasible region are $\mathrm{O}(0,0), \mathrm{A}(3,0), \mathrm{P}, \mathrm{Q}$ and $\mathrm{D}(0,3)$.
$P$ is the point of intersection of the lines $x+y=5$ and $x=3 \Rightarrow P \equiv(3,2)$
$Q$ is the point of intersection of the lines $x+y=5$ and $y=3 \Rightarrow Q=(2,3)$
The values of the objective function $Z=10 x+25 y$ at these vertices are
$Z_{(0)}=10(0)+25(0)=0+0=0$
$Z_{(A)}=10(3)+25(0)=30+0=30$
$Z_{(P)}=10(3)+25(2)=30+50=80$
$Z_{(Q)}=10(2)+25(3)=20+75=95$
$Z_{(D)}=10(0)+25(3)=0+75=75$
$\therefore Z$ has maximum value 95, when $x=2$ and $y=3$.

</details>

---

### Q93. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $\mathrm{Z}=3 x+5 \mathrm{y}$, subject to $3 x+2 \mathrm{y} \leq 18, x \leq 4, \mathrm{y} \leq 6$
$x, y \geq 0$ is

**Options:**

- **(A)** 30
- **(B)** 27
- **(C)** 36
- **(D)** 32

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 36**

**Detailed Solution:**

Point of intersection of $x=4$ and $3 x+2 y=18$ is $Q \equiv(4,3)$ Point of intersection of $\mathrm{y}=6$ and $3 \mathrm{x}+2 \mathrm{y}=18$ is $\mathrm{P} \equiv(2,6)$ Point $\mathrm{D} \equiv(4,0)$ and $\mathrm{C} \equiv(0,6)$ are as shown. The feasible region of th given L.P.P. is shaded portion CPQ D O. We have to maximize $Z=3 x+5 y$ Now, $\mathrm{Z}$ at $\mathrm{C}(0,6)=3(0)+5(6)=30$
$\mathrm{Z}$ at $\mathrm{P}(2,6) \quad=3(2)+5(6)=36$
$\mathrm{Z}$ at $\mathrm{Q}(4,3)=3(4)+5(3)=27$
$Z$ at $D(4,0)=3(4)+5(0)=12$
$\mathrm{Z}$ at $\mathrm{O}(0,0)=3(0)+5(0)=0$
Clearly the maximum value of $\mathrm{Z}$ is 36 at $\mathrm{P}(2,6)$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/PeRUuiqIK3hGLzoGDhNv5E1aZjULsVFYRTejA3hFaEU.original.fullsize.png">

</details>

---

### Q94. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value of $\mathrm{Z}=5 x+8 y$ subject to $x+y \geq 5,0 \leq x \leq 4, y \geq 2, x \geq 0$ $y \geq 0$ is

**Options:**

- **(A)** 40
- **(B)** 36
- **(C)** 31
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 31**

**Detailed Solution:**

(C)
Required area is shaded.
Co-ordinates of vertices are $C \equiv(4,1)$;
$D \equiv(4,2)$ and $P \equiv(3,2)$
$\mathrm{Z}=5 \mathrm{x}+8 \mathrm{y}$
$\therefore \quad Z_{(C)}=20+8=28$
$\mathrm{Z}_{(\mathrm{D})}=20+16=36$
$Z_{(P)}=15+16=31$
Minimum value will be 28 .
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/smMOR6OGvSwGKbZkQIka_KJ8GhnxbrTalS8PMhG_c5w.original.fullsize.png">

</details>

---

### Q95. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The optimal solution of the L.P.P. Maximize : $\mathrm{Z}=8 x+3$ y subject to the constraints $x+y \leq 3,4 x+y \leq 6, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** $x=0, y=3$
- **(B)** $x=0, y=0$
- **(C)** $x=\frac{3}{2}, y=0$
- **(D)** $x=1, y=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x=1, y=2$**

**Detailed Solution:**

Here $\mathrm{O} \equiv(0,0), \mathrm{A} \equiv\left(\frac{3}{2}, 0\right), \mathrm{C}=(0,3)$
Point of intersection of given lines is $\mathrm{B} \equiv(1,2)$
$Z=8 x+3 y$ and feasible region is shaded.
$Z_{(0)}=0$
$Z_{(A)}=8\left(\frac{3}{2}\right)=12$
$Z_{(C)}=3(3)=9$
$Z_{(B)}=8(1)+3(2)=14$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/yQEE1AMPko1TkX6vP6inzrEOurWkBiHoKVXlzJCQJh0.original.fullsize.png">

</details>

---

### Q96. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The minimum value for the LPP $\mathrm{Z}=6 x+2 y$, subject to $2 x+y \geq 16, x \geq 6, y \geq 1$ is

**Options:**

- **(A)** $44$
- **(B)** $47$
- **(C)** $24$
- **(D)** $34$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $44$**

**Detailed Solution:**

Here $\mathrm{A}(8,0), \mathrm{B}(0,16)$ lie on $2 \mathrm{x}+\mathrm{y}=16$ When $y=1, x=\frac{15}{2} \quad$ i.e. $E\left(\frac{15}{2}, 1\right)$
When $x=6, y=4 \quad$ i.e. $F(6,4)$
$Z(E)=6 \times \frac{15}{2}+2 \times 1=47$
$Z(F)=6 \times 6+2 \times 4=36+8=44$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/OKuuMRRU4vZICrNIM5XkG29SWS_vbG5UfMgZO9jM020.original.fullsize.png">

</details>

---

### Q97. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $\mathrm{Z}=10 x+25 y$ subject to $0 \leq x \leq 3,0 \leq y \leq 3$,
$x+y \leq 5, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** 110
- **(B)** $100$
- **(C)** $120$
- **(D)** $95$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $95$**

**Detailed Solution:**

Given $\mathrm{Z}=10 \mathrm{x}+25 \mathrm{y}$ subject to $0 \leq \mathrm{x} \leq 3,0 \leq \mathrm{y} \leq 3, \mathrm{x}+\mathrm{y} \leq 5, \mathrm{x} \geq 0, \mathrm{y} \geq 0$
\begin{array}{|l|l|l|}
\hline Line & Point on \mathrm{X}-axis & Point on Y-axis \\
\hline \mathrm{x}+\mathrm{y}=5 & \mathrm{~A}(5,0) & \mathrm{B}(0,5) \\
\hline \mathrm{x}=3 & \mathrm{C}(3,0) & - \\
\hline \mathrm{y}=3 & - & \mathrm{D}(0,3) \\
\hline
\end{array}
Point of intersection of $x+y=5$ and $x=3$ is $F \equiv(3,2)$
Point of intersection of $x+y=5$ and $y=3$ is $G \equiv(2,3) .$
Feasible region OCFGDO is shaded.
We have $Z=10 x+25 y$
$\therefore Z_{(0)}=0+0=0$
$Z_{(C)}=30+0=30$
$Z_{(F)}=30+50=80$
$Z_{(G)}=20+75=95$
$Z_{(D)}=0+75=75$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/lmv5G69SVr7UbHsAQekXuDEhzsanALCpwthHUp75Guw.original.fullsize.png">

</details>

---

### Q98. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $\mathrm{Z}=3 x+5 y$, subject to $x+4 y \leq 24, y \leq 4, x \geq 0, y \geq 0$
is

**Options:**

- **(A)** 20
- **(B)** 120
- **(C)** 72
- **(D)** 44

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 72**

**Detailed Solution:**

\begin{array}{|l|l|l|}
\hlinex+4 y=24 & A(24,0) & B(0,6) \\
\hliney=4 & - & C(0,4) \\
\hline
\end{array}
Feasible region is $\mathrm{OADC}$
Objective function is $Z=3 x+5 y$
$Z(A)=3(24)+0 \quad=72$
$Z(D)=3 \times 8+5 \times 4=24+20=44$
$Z(C)=3 \times 0+5 \times 4=20$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/PEhhLxUwWqqkm_IFhrxJOXRXe7wlD_9OAWfvTCaP3qc.original.fullsize.png">

</details>

---

### Q99. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the following shaded region the linear constraints are
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/LMkeXkPpQCTHwh4e4vOJkCYuN6nNjsckuhx9Xix9LH4.original.fullsize.png">

**Options:**

- **(A)** $5 x+9 y \leq 90, x+y \geq 4, \quad y \geq 8, \quad x, y \geq 0$
- **(B)** $5 x+9 y \geq 90, x+y \leq 4, \quad y \leq 8, \quad x, y \geq 0$
- **(C)** $5 x+9 y \geq 90, x+y \geq 4, \quad y \geq 8, \quad x, y \geq 0$
- **(D)** $5 x+9 y \leq 90, x+y \geq 4, \quad y \leq 8, \quad x, y \geq 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5 x+9 y \leq 90, x+y \geq 4, \quad y \leq 8, \quad x, y \geq 0$**

**Detailed Solution:**

Solution of $5 x+9 y \leq 90$ is origin side, solution of $x+y \geq 4$ is non-origin side and solution of $y \leq 8$ is origin side

</details>

---

### Q100. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The L.P.P. to maximize $z=x+y$, subject to $x+y \leq 30, x \leq 15, y \leq 20, x+y \geq 15$,
$x, y \geq 0$ has

**Options:**

- **(A)** no solution.
- **(B)** a unique solution.
- **(C)** infinite solutions.
- **(D)** unbounded solutions.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) infinite solutions.**

**Detailed Solution:**

\begin{array}{|l|l|l|}
\hline line & Point on X-axis & Point on y-axis \\
\hlinex+y=30^{\circ} & A(30,0) & B(0,30) \\
\hlinex=15 & C(15,0) & - \\
\hliney=20 & - & D(0,20) \\
\hlinex+y=15 & C(15,0) & F(0,15) \\
\hline
\end{array}
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/kaOOWmtMRPSP_JcbVg0NDJf2oSNIi4b6K-yAu2kdvyw.original.fullsize.png">

Point of intersection of $x=15$ and $y=20$ is $E \equiv(15,20)$
Feasible region is FCEDF.
We have to maximize $Z=x+y$
$\begin{array}{l}
Z_{(C)}=15+0=15 \\
Z_{(E)}=15+20=35 \\
Z_{(D)}=0+20=20 \\
Z_{(F)}=0+15=15
\end{array}$
Thus minimum value 15 occurs at two vertices $\mathrm{F}$ and $\mathrm{C}$.
Thus given LPP has infinite solutions.

</details>

---

### Q101. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The feasible region of L. P. P.
Maximize $\mathrm{z}=70 x+50 \mathrm{y}$ subject to $8 x+5 y \leq 60,4 x+5 y \leq 40$ and $x \geq 0, y \geq 0$
is

**Options:**

- **(A)** a triangle
- **(B)** a square
- **(C)** a pentagon
- **(D)** a quadrilateral

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a quadrilateral**

**Detailed Solution:**

\begin{array}{|l|l|l|}
\hline Line & Point on X-axis & Point on Y-axis \\
\hline 8 x+5 y=60 & \mathrm{~A}(7.5,0) & \mathrm{B}(0,12) \\
\hline 4 x+5 y=40 & \mathrm{C}(10,0) & \mathrm{D}(0,8) \\
\hline
\end{array}
Feasible region is shaded. 
Point of intersection $\mathrm{E} \equiv(5,4)$ 
Also $A=(7.5,0)$ and $D \equiv(0,8)$ 
So OAED is a quadrilateral.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/PkAApkzAYkXPtiQcrTJSVgm9Ol0SZmEZjbyLFOOWSOU.original.fullsize.png">

</details>

---

### Q102. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{Z}=7 x+y$ subject to $5 x+y \geq 5, x+y \geq 3, x \geq 0, y \geq 0$, then minimum
value of $\mathrm{Z}$ is

**Options:**

- **(A)** 2
- **(B)** 5
- **(C)** 6
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

Feasible area is shaded.
Point of intersection of given lines is $\mathrm{P} \equiv\left(\frac{1}{2}, \frac{5}{2}\right)$
Co-ordinates of points are as follows :
$C \equiv(3,0) ; P \equiv\left(\frac{1}{2}, \frac{5}{2}\right)$ and $B \equiv(0,5)$
We have $Z=7 x+y$
$Z_{(c)}=21+0=21$
$\therefore \quad Z_{(B)}=0+5=5$
$Z_{(P)}=\frac{7}{2}+\frac{5}{2}=6$
Thus minimum value is 5. 
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/JiZixb6-OJxwy3UUXxHbMFQs3NX7b1A5Sx450GIzPc8.original.fullsize.png">

</details>

---

### Q103. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

The constraints $-x_{1}+x_{2} \leq 1,-x_{1}+3 x_{2} \leq 9$, $x_{1}, x_{2}>, 0$ defines on

**Options:**

- **(A)** bounded feasible space
- **(B)** unbounded feasible space
- **(C)** both bounded and unbounded feasible space
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) unbounded feasible space**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/2YaAuddEnOXk0VFNN6rVaKEGsEIV5wjy2s_s_680RSY.original.fullsize.png">

So, constraints defines unbounded feasible
space.

</details>

---

### Q104. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

A diet of a sick person must contain atleast 4000 unit of vitamins, 50 unit of proteins and 1400 calories. Two foods $\mathrm{A}$ and $\mathrm{B}$ are available at cost of $₹ 4$ and $₹ 3$ per unit respectively. If one unit of A contains 200 unit of vitamins, 1 unit of protein and 40 calories, while one unit of food B contains 100 unit of vitamins, 2 unit of protein and 40 calories. Formulate the problem, so that the diet be cheapest.

**Options:**

- **(A)** $200 x+100 y \geq 4000, x+2 y \geq 50$
$40 x+40 y \geq 1400, x \geq 0$ and $y \geq 0$
$O . F z=4 x+3 y$
- **(B)** $400 x+200 y \geq 100, x+2 y \geq 50$
$40 x+40 y \geq 1400, x \geq 0$ and $y \geq 0$
O. $F z=4 x+3 y$
- **(C)** $100 x+200 y \geq 4000, x+2 y \geq 50$,
$40 x+40 y \geq 1400, x \geq 0$ and $y \geq 0$
O. $F z=4 x+3 y$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $200 x+100 y \geq 4000, x+2 y \geq 50$
$40 x+40 y \geq 1400, x \geq 0$ and $y \geq 0$
$O . F z=4 x+3 y$**

**Detailed Solution:**

$$
\begin{array}{l|c|c|c|c}
\hline \begin{array}{c}
\text { Nutrients } \\
\text { Food }
\end{array} & \begin{array}{c}
\text { Vitamins } \\
\text { (unit) }
\end{array} & \begin{array}{c}
\text { Proteins } \\
\text { (unit) }
\end{array} & \begin{array}{c}
\text { Colories } \\
\text { (unit) }
\end{array} & \begin{array}{c}
\text { Availabil } \\
\text { ity (per } \\
\text { unit) }
\end{array} \\
\hline \text { A } & 200 & 1 & 40 & 4 \text { pes } \\
\text { B } & 100 & 2 & 40 & 3 \text { pes } \\
\text { Requirement } & 4000 & 50 & 1400 & \\
\hline
\end{array}
$$
Let $z$ be the profit function and $x$ and $y$ denote the productivity of food $A$ and $B$ respectively. Then
$$
\begin{array}{c}
200 x+100 y \geq 4000 \\
x+2 y \geq 50 \\
40 x+40 \geq 1400 \\
\text { O.F } z=4 x+3 y, \quad x \geq 0 \text { and } y \geq 0
\end{array}
$$

</details>

---

### Q105. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

Simplify the Boolean function $(x \cdot y)+\left[\left(x+y^{\prime}\right) \cdot y\right]^{\prime}$

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** $x+y$
- **(D)** $x y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

$\begin{array}{rlr} & (x \cdot y)+\left[\left(x+y^{\prime}\right) \cdot y\right]^{\prime} & \\ & =(x \cdot y)+\left[\left(x+y^{\prime}\right)^{\prime}+y^{\prime}\right] & {\left[\because(a \cdot b)^{\prime}=a^{\prime}+b^{\prime}\right]} \\ & =(x \cdot y)+\left[x^{\prime} \cdot\left(y^{\prime}\right)^{\prime}+y^{\prime}\right] & {\left[\because(a+b)^{\prime}=a^{\prime} \cdot b^{\prime}\right]} \\ & =(x \cdot y)+\left[x^{\prime} \cdot y+y^{\prime}\right] & {\left[\because\left(a^{\prime}\right)^{\prime}=a\right]} \\ & =x \cdot y+y^{\prime}+x^{\prime} \cdot y & {[\because a+b=b+a]} \\ & =x \cdot y+\left(y^{\prime}+x^{\prime}\right) \cdot\left(y^{\prime}+y\right)[\text { by distributive law }] \\ & =x \cdot y+\left(y^{\prime}+x^{\prime}\right) \cdot 1 & {\left[\because a+a^{\prime}=1\right]} \\ & =x \cdot y+x^{\prime}+y^{\prime} & \\ & =x \cdot y+(x \cdot y)^{\prime} & {\left[\because a^{\prime}+b^{\prime}=(a \cdot b)^{\prime}\right]} \\ & =1 & {\left[\because a+a^{\prime}=1\right]}\end{array}$

</details>

---

### Q106. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

Dual of $(x+y)\left(x^{\prime} \cdot 1\right)$ is

**Options:**

- **(A)** $(x \cdot y)+\left(x^{\prime}+1\right)$
- **(B)** $(x \cdot y)\left(x^{\prime}+1\right)$
- **(C)** $(x \cdot y)+(x+1)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(x \cdot y)+\left(x^{\prime}+1\right)$**

**Detailed Solution:**

Dual of $(x+y) \cdot\left(x^{\prime} \cdot 1\right)$ is obtained by replacing
$$
+\mathrm{by} \cdot \text { and } \cdot \mathrm{by}+\text { ie dual is }(x \cdot y)+\left(x^{\prime}+1\right) \text { . }
$$

</details>

---

### Q107. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of the objective function $Z=3 x+2 y$ for linear constraints $x+y \leq 7$ $2 x+3 y \leq 16, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** 16
- **(B)** 21
- **(C)** 25
- **(D)** 28

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 21**

**Detailed Solution:**

The feasible region is $O A B C O$.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/rY3xonj2vOiycg2Jvsu8jYeKvzezA0nr8JPz25X7GWQ.original.fullsize.png">

At $O(0,0), Z=0$
At $A\left(0, \frac{16}{3}\right), Z=\frac{32}{3}$
At $B(5,2), Z=15+4=19$
At $C(7,0), Z=21$
$\therefore$ Maximum value of $Z$ is 21 .

</details>

---

### Q108. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

The maximum value of $z=9 x+13 y$ subject to $2 x+3 y \leq 18,2 x+y \leq 10, x \geq 0, y \geq 0$ is

**Options:**

- **(A)** 130
- **(B)** 81
- **(C)** 79
- **(D)** 99

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 79**

**Detailed Solution:**

The feasible region is $O A B C$.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/hsSrLbPHZuH2iCB7G2m195_3Mc1oxA8TwZZL9UYmaBs.original.fullsize.png">

$\begin{array}{ll}\text { At } & A(5,0), z=45 \\ \text { At } & B(3,4), z=27+52=79\end{array}$
At $\quad C(0,6), z=78$
$\therefore$ Maximum value of $z$ is 79 .

</details>

---

### Q109. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

The region represented by the inequation system $x, y \geq 0, y \leq 6, x+y \leq 3$, is

**Options:**

- **(A)** unbounded in first quadrant
- **(B)** unbounded in first and second quadrants
- **(C)** bounded in first quadrant
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) bounded in first quadrant**

**Detailed Solution:**

The given region is bounded in first quadrant.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/8SY5OJABYRixQI80u3gYhXzT3dwJ10aVw_dTzeBqYyE.original.fullsize.png">

</details>

---

### Q110. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

For the LPP Min $z=x_{1}+x_{2}$ such that inequalities $5 x_{1}+10 x_{2} \geq 0, x_{1}+x_{2} \leq 1, x_{2} \leq 4$
and $x_{1}, x_{2} \geq 0$

**Options:**

- **(A)** There is a bounded solution
- **(B)** There is no solution
- **(C)** There are infinite solutions
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) There is a bounded solution**

**Detailed Solution:**

It is clear from the graph that it is bounded solution.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/4E3xdENUnIxjJP74If8tiwbYGkVB3w7pFFiMfE7dDx4.original.fullsize.png">

</details>

---

### Q111. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

A wholesale merchant wants to start the business of cereal with Rs 24000 . Wheat is Rs 400 per quintal and rice is Rs 600 per quintal. He has capacity to store 200 quintal cereal. He earns the profit Rs 25 per quintal on wheat and Rs 40 per quintal on rice. If he stores $x$ quintal rice and $y$ quintal wheat, then for maximum profit the objective function is

**Options:**

- **(A)** $25 x+40 y$
- **(B)** $40 x+25 y$
- **(C)** $400 x+600 y$
- **(D)** $\frac{400}{40} x+\frac{600}{25} y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $40 x+25 y$**

**Detailed Solution:**

For maximum profit $z=40 x+25 y$

</details>

---

### Q112. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

The constraints $-x_{1}+x_{2} \leq 1,-x_{1}+3 x_{2} \leq 9$; $x_{1}, x_{2} \geq 0$ defines on

**Options:**

- **(A)** bounded feasible space
- **(B)** unbounded feasible space
- **(C)** both bounded and unbounded feasible space
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) unbounded feasible space**

**Detailed Solution:**

Given constraints are $-x_{1}+x_{2} \leq 1,-x_{1}+3 x_{2} \leq 9$ and $x_{1}, x_{2} \geq 0 .$
It is clear from the figure that feasible space (shaded portion) is unbounded.

</details>

---

### Q113. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

Which of the terms is not used in a linear programming problem?

**Options:**

- **(A)** Optimal solution
- **(B)** Feasible solution
- **(C)** Concave region
- **(D)** Objective function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Concave region**

**Detailed Solution:**

Concave region term is not used in a linear programming problem.

</details>

---

