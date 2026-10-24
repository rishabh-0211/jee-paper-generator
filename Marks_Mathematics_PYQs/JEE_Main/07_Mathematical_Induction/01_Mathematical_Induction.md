# JEE Main Mathematics - Mathematical Induction

## Topic 1: Mathematical Induction

**Total Questions:** 3

---

### Q1. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{ll}1 & 0 \\ 1 & 1\end{array}\right]$ and $I=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$, then which one of the following holds for all $n \geq 1$, by the principle of mathematical indunction

**Options:**

- **(A)** $A^n=n A-(n-1) I$
- **(B)** $A^n=2^{n-1} A-(n-1) I$
- **(C)** $A^n=n A+(n-1) I$
- **(D)** $A^n=2^{n-1} A+(n-1) I$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $A^n=n A-(n-1) I$**

**Detailed Solution:**

By the principle of mathematical induction (A) is true.

</details>

---

### Q2. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Let $S(K)=1+3+5+\ldots+(2 K-1)=3+K^2$. Then which of the following is true?

**Options:**

- **(A)** $S(1)$ is correct
- **(B)** Principle of mathematical induction can be used to prove the formula
- **(C)** $S(K) \neq S(K+1)$
- **(D)** $\mathrm{S}(\mathrm{K}) \Rightarrow \mathrm{S}(\mathrm{K}+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{S}(\mathrm{K}) \Rightarrow \mathrm{S}(\mathrm{K}+1)$**

**Detailed Solution:**

$$
\begin{aligned}
& S(k)=1+3+5+\ldots \ldots . .+(2 k-1)=3+k^2 \\
& S(k+1)=1+3+5+\ldots \ldots \ldots+(2 k-1)+(2 k+1) \\
& =\left(3+k^2\right)+2 k+1=k^2+2 k+4\left[\text { from } S(k)=3+k^2\right] \\
& =3+\left(k^2+2 k+1\right)=3+(k+1)^2=S(k+1)
\end{aligned}
$$
Although $S(k)$ in itself is not true but it considered true will always imply towards $S(k+1)$.

</details>

---

### Q3. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `3`

If $a_n=\sqrt{7+\sqrt{7+\sqrt{7+\ldots .}}}$ having $\mathrm{n}$ radical signs then by methods of mathematical induciton which is true

**Options:**

- **(A)** $a_n>7 \forall n \geq 1$
- **(B)** $\mathrm{a}_{\mathrm{n}}>7 \forall \mathrm{n} \geq 1$
- **(C)** $a_n < 4 \forall n \geq 1$
- **(D)** $a_n < 3 \forall \mathrm{n} \geq 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{a}_{\mathrm{n}}>7 \forall \mathrm{n} \geq 1$**

**Detailed Solution:**

$\mathrm{a}_1=\sqrt{7} < 7$. Leta $_{\mathrm{m}} < 7$. Then $\mathrm{a}_{\mathrm{m}}+1=\sqrt{7+\mathrm{a}_{\mathrm{m}}} \Rightarrow \mathrm{a}_{\mathrm{m}+1}^2=7+\mathrm{a}_{\mathrm{m}} < 7+7 < 14$
$\Rightarrow \mathrm{a}_{\mathrm{m}+1} < \sqrt{14} < 7 ;$ So $\mathrm{a}_{\mathrm{n}} < 7 \forall \mathrm{n} \therefore \mathrm{a}_{\mathrm{n}}>3$

</details>

---

