# BITSAT Mathematics - Indefinite Integration

## Topic 4: Integration using Partial Fraction

**Total Questions:** 2

---

### Q1. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \frac{x^3-1}{x^3+x} d x=$

**Options:**

- **(A)** $x+\log |x|+\frac{1}{2} \log \left(x^2+1\right)+\sin ^{-1}(x)+c$
- **(B)** $x-\log |x|+\frac{1}{2} \log \left(x^2+1\right)-\sin ^{-1}(x)+c$
- **(C)** $x+\log |x|-\frac{1}{2} \log \left(x^2+1\right)+\tan ^{-1}(x)+c$
- **(D)** $x-\log |x|+\frac{1}{2} \log \left(x^2+1\right)-\tan ^{-1}(x)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x-\log |x|+\frac{1}{2} \log \left(x^2+1\right)-\tan ^{-1}(x)+c$**

**Detailed Solution:**

$I=\int\left(\frac{x^3-1}{x^3+x}\right) d x=\int\left(1-\frac{x+1}{x^3+x}\right) d x$
$\begin{aligned}
& \Rightarrow I=\int 1 \cdot d x-\int \frac{(x+1)}{x^3+x} d x \\
& =x-\int \frac{(x+1)}{x\left(x^2+1\right)} d x
\end{aligned}$
$\begin{aligned}
& \text { Let } \frac{x+1}{x\left(x^2+1\right)}=\frac{A}{x}+\frac{B x+C}{x^2+1} \\
& \Rightarrow(x+1)=A\left(x^2+1\right)+(B x+C) x \\
& \Rightarrow(x+1)=(A+B) x^2+C x+A
\end{aligned}$
On comparing coefficient, we get
$\begin{aligned}
& A+B=0, C=1, A=1 \\
& \Rightarrow B=-1 \\
& \therefore I=x-\int \frac{1}{x} d x-\int \frac{(1-x)}{x^2+1} d x \\
& \Rightarrow I=x-\log |x|-\int \frac{1}{x^2+1} d x+\frac{1}{2} \int \frac{2 x}{x^2+1} d x \\
& \Rightarrow I=x-\log |x|-\tan ^{-1} x+\frac{1}{2} \log \left(x^2+1\right)+c
\end{aligned}$

</details>

---

### Q2. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

If $\int \frac{3 x+1}{(x-3)(x-5)} d x=\int \frac{-5}{(x-3)} d x+\int \frac{B}{(x-5)} d x$ then the value of $B$ is

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 6
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8**

**Detailed Solution:**

We have,

$\begin{array}{l}

\frac{3 x+1}{(x-3)(x-5)}=\frac{-5}{x-3}+\frac{\mathrm{B}}{x-5} \\

3 x+1=-5(x-5)+\mathrm{B}(x-3) \\

\text { Put } x=5 \\

3(5)+1=\mathrm{B}(5-3) \\

16=2 \mathrm{~B} \text { or } \mathrm{B}=8

\end{array}$

</details>

---

