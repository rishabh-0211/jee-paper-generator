# BITSAT Mathematics - Matrices

## Topic 4: Types of Matrices

**Total Questions:** 2

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\frac{1}{3}\left[\begin{array}{ccc}1 & 2 & 2 \\ 2 & 1 & -2 \\ a & 2 & b\end{array}\right]$ is an orthogonal matrix, then

**Options:**

- **(A)** $a=-2, b=-1$
- **(B)** $a=2, b=1$
- **(C)** $a=2, b=-1$
- **(D)** $a=-2, b=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a=-2, b=-1$**

**Detailed Solution:**

We know that, if $A$ is an orthogonal matrix, then
$\begin{gathered}
\Rightarrow \quad \ AA^T=I \\
\Rightarrow \\
\Rightarrow \quad\left[\begin{array}{ccc}
1 & 2 & 2 \\
2 & 1 & -2 \\
a & 2 & b
\end{array}\right] \cdot \frac{1}{3}\left[\begin{array}{ccc}
1 & 2 & a \\
2 & 1 & 2 \\
2 & -2 & b
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
\Rightarrow\left[\begin{array}{ccc}
1 & 2 & 2 \\
2 & 1 & -2 \\
a & 2 & b
\end{array}\right]\left[\begin{array}{ccc}
1 & 2 & a \\
2 & 1 & 2 \\
2 & -2 & b
\end{array}\right]=\left[\begin{array}{lll}
9 & 0 & 0 \\
0 & 9 & 0 \\
0 & 0 & 9
\end{array}\right] \\
\left[\begin{array}{ccc}
9 & 0 & a+4+2 b \\
0+4+2 b & 9 & 2 a+2-2 b \\
2 a+2-2 b & a^2+4+b^2
\end{array}\right] \\
\quad=\left[\begin{array}{ccc}
9 & 0 & 0 \\
0 & 9 & 0 \\
0 & 0 & 9
\end{array}\right] \\
\Rightarrow \quad a+4+2 b=0 \text { and } 2 a+2-2 b=0 \\
a+2 b=-4 \ldots(i)\\
a-b=-1 \ldots(ii)
\end{gathered}$
By solving Eqs. (i) and (ii), we get
$a=-2, b=-1$

</details>

---

### Q2. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `2`

If $\left[\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}\right]$ is square root of identity matrix of order 2 then -

**Options:**

- **(A)** $1+\alpha^{2}+\beta \gamma=0$
- **(B)** $1+\alpha^{2}-\beta \gamma=0$
- **(C)** $1-\alpha^{2}+\beta \gamma=0$
- **(D)** $\alpha^{2}+\beta \gamma=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\alpha^{2}+\beta \gamma=1$**

**Detailed Solution:**

$\left[\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}\right]=\sqrt{\mathrm{I}_{2}}$;

$\left[\begin{array}{lc}\alpha & \beta \\ \gamma & -\alpha\end{array}\right]\left[\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}\right]=\left[\begin{array}{cc}1 & 0 \\ 0 & 1\end{array}\right]$

$\Rightarrow \alpha^{2}+\beta \gamma=1$

</details>

---

