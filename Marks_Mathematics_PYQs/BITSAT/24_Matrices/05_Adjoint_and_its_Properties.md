# BITSAT Mathematics - Matrices

## Topic 5: Adjoint and its Properties

**Total Questions:** 3

---

### Q1. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A$ is a square matrix of order 3 , then $\mid \operatorname{Adj}(\operatorname{Adj}$ $\left.A^2\right) \mid=$

**Options:**

- **(A)** $|A|^2$
- **(B)** $|A|^4$
- **(C)** $|A|^8$
- **(D)** $|\mathrm{A}|^{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $|A|^8$**

**Detailed Solution:**

$\left|\operatorname{adj}\left(\operatorname{adj} A^2\right)\right|=$
$|\operatorname{adj} \mathrm{A}|=|\mathrm{A}|^{n-1}=|\mathrm{A}|^2$
$\left|\operatorname{adj} A^2\right|=|\operatorname{adj} A|^2=\left(|A|^2\right)^2=|A|^4$
$\left|\operatorname{adj}\left(\operatorname{adj} A^2\right)\right|=\left(|A|^4\right)^{3-1}$
$=\left(|A|^4\right)^2=|A|^8$

</details>

---

### Q2. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `2`

Let M bea $3 \times 3 \mathrm{n} \times \mathrm{n}$ -singular matrix with $\operatorname{det}(\mathrm{M})$ $=\alpha$. If $\left[\mathrm{M}^{-1}\right.$ adj $(\mathrm{adj} (\mathrm{M})]=\mathrm{KI}$, then the value of $\mathrm{K}$ is

**Options:**

- **(A)** 1
- **(B)** $\alpha$
- **(C)** $\alpha^{2}$
- **(D)** $\alpha^{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\alpha$**

**Detailed Solution:**

We know that, $M(\operatorname{adj} M)=|M|$ I

Replacing $\mathrm{M}$ by adj $\mathrm{M},$ we get $\operatorname{adj} M[\operatorname{adj}(\operatorname{adj} M)=\operatorname{det}(\operatorname{adj} M) I$

$=\operatorname{det}(M) M^{-1}\left[\operatorname{adj}(\operatorname{adj} M)=\alpha^{2} 1\right.$

$$

\left[\because \mathrm{M}^{-1}=\frac{1}{|\mathrm{M}|} \operatorname{adj}(\mathrm{M})\right]

$$

$\Rightarrow \alpha \mathrm{M}^{-1}[\operatorname{adj}(\operatorname{adj} M)]=\alpha^{2} \mathrm{I}$

$\Rightarrow \mathrm{M}^{-1}[\mathrm{adj}(\operatorname{adj} \mathrm{M})]=\alpha \mathrm{I}$

But $M^{-1}[\operatorname{adj}(\operatorname{adj} M)]=K I$

Hence, $\mathrm{K}=\alpha$

</details>

---

### Q3. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `2`

If \(A=\left[\begin{array}{lll}2 & 0 & 0 \\ 2 & 2 & 0 \\ 2 & 2 & 2\end{array}\right]\), then \(\operatorname{adj}(\operatorname{adj} A)\) is equal to -

**Options:**

- **(A)** \(8\left[\begin{array}{lll}1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1\end{array}\right]\)
- **(B)** \(16\left[\begin{array}{lll}1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1\end{array}\right]\)
- **(C)** \(64\left[\begin{array}{lll}1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1\end{array}\right]\)
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) \(16\left[\begin{array}{lll}1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1\end{array}\right]\)**

**Detailed Solution:**

\(|A|=\left[\begin{array}{lll}
2 & 0 & 0 \\
2 & 2 & 0 \\
2 & 2 & 2
\end{array}\right]=(2)(2)(2)=8\)
Now adj \((\operatorname{adj} A)=|\mathrm{A}|^{3-2} \mathrm{~A}\)
\(=8\left[\begin{array}{lll}
2 & 0 & 0 \\
2 & 2 & 0 \\
2 & 2 & 2
\end{array}\right]=16\left[\begin{array}{ccc}
1 & 0 & 0 \\
1 & 1 & 0 \\
1 & 1 & 1
\end{array}\right]\)

</details>

---

