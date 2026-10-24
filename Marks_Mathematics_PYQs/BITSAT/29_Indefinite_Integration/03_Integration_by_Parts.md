# BITSAT Mathematics - Indefinite Integration

## Topic 3: Integration by Parts

**Total Questions:** 4

---

### Q1. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

$\int \tan ^{-1} \sqrt{\mathrm{x}} \mathrm{dx}$ is equal to

**Options:**

- **(A)** $(x+1) \tan ^{-1} \sqrt{x}-\sqrt{x}+C$
- **(B)** $x \tan ^{-1} \sqrt{x}-\sqrt{x}+C$
- **(C)** $\sqrt{x}-x \tan ^{-1} \sqrt{x}+C$
- **(D)** $\sqrt{x}-(x+1) \tan ^{-1} \sqrt{x}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(x+1) \tan ^{-1} \sqrt{x}-\sqrt{x}+C$**

**Detailed Solution:**

We have, $I=\int 1 \cdot \tan ^{-1} \sqrt{\mathrm{x}} \mathrm{dx}$
Using by parts,
$\begin{aligned}
I & =\tan ^{-1} \sqrt{x} \cdot(x)-\int \frac{1}{1+x} \times \frac{1}{2 \sqrt{x}} \times x d x \\
& =x \tan ^{-1} \sqrt{x} \cdot-\int \frac{x}{(1+x) 2 \sqrt{x}} d x \\
& =x \tan ^{-1} \sqrt{x}-\int\left(\frac{1+x}{(1+x) 2 \sqrt{x}}-\frac{1}{(1+x) 2 \sqrt{x}}\right) d x \\
& =x \tan ^{-1} \sqrt{x}-\int \frac{d x}{2 \sqrt{x}}+\int \frac{d x}{2 \sqrt{x}(1+x)} \\
& =x \tan ^{-1} \sqrt{x}-\sqrt{x}+\tan ^{-1} \sqrt{x}+C \\
& =(x+1) \tan ^{-1} \sqrt{x}-\sqrt{x}+C
\end{aligned}$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int \frac{x+3}{(x+4)^2} e^x d x$ is equal to

**Options:**

- **(A)** $e^x\left(\frac{1}{x+4}\right)+C$
- **(B)** $e^{-x}\left(\frac{1}{x+4}\right)+C$
- **(C)** $e^{-x}\left(\frac{1}{x-4}\right)+C$
- **(D)** $e^{2 x}\left(\frac{1}{x-4}\right)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^x\left(\frac{1}{x+4}\right)+C$**

**Detailed Solution:**

Suppose,
$I=\int \frac{x+3}{(x+4)^2} e^x d x=\int \frac{(x+4) 1}{(x+4)^2} e^x d x$
$=\int \frac{e^x}{(x+4)}-\int \frac{e^x}{(x+4)^2} d x$
$=\int e^x\left(\frac{1}{(x+4)}-\frac{1}{(x+4)^2}\right) d x$
$=e^x \frac{1}{(x+4)}+C$
$\left[\int e^x\left\{f(x)+f^{\prime}(x)\right\} d x=e^x f(x)+C\right]$

</details>

---

### Q3. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\int \frac{\mathrm{e}^{\mathrm{x}}(1+\sin \mathrm{x}) \mathrm{dx}}{1+\cos \mathrm{x}}=\mathrm{e}^{\mathrm{x}} \mathrm{f}(\mathrm{x})+\mathrm{C}$, then $\mathrm{f}(\mathrm{x})$ is equal to

**Options:**

- **(A)** $\sin \frac{x}{2}$
- **(B)** $\cos \frac{x}{2}$
- **(C)** $\tan \frac{x}{2}$
- **(D)** $\log \frac{x}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\tan \frac{x}{2}$**

**Detailed Solution:**

$\int e^x \frac{(1+\sin x)}{(1+\cos x)} d x$
$=\int e^x\left[\frac{1}{2} \sec ^2 \frac{x}{2}+\tan \frac{x}{2}\right] d x$
$=\frac{1}{2} \int e^x \sec ^2 \frac{x}{2} d x+\int e^x \tan \frac{x}{2} d x$
$=\mathrm{e}^{\mathrm{x}} \tan \frac{\mathrm{x}}{2}+\mathrm{C}$
But $\mathrm{I}=\mathrm{e}^{\mathrm{x}} \mathrm{f}(\mathrm{x})+\mathrm{C}$ (given)
$\therefore \mathrm{f}(\mathrm{x})=\tan \frac{\mathrm{x}}{2}$

</details>

---

### Q4. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `3`

If \(\int \frac{2 \cos x-\sin x+\lambda}{\cos x+\sin x-2} d x\) \(=A \ln |\cos x+\sin x-2|+B x+C\).
Then the ordered triplet \(A, B, \lambda\) is -

**Options:**

- **(A)** \(\left(\frac{1}{2}, \frac{3}{2},-1\right)\)
- **(B)** \(\left(\frac{3}{2}, \frac{1}{2},-1\right)\)
- **(C)** \(\left(\frac{1}{2},-1, \frac{3}{2}\right)\)
- **(D)** \(\left(\frac{3}{2},-1, \frac{1}{2}\right)\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) \(\left(\frac{3}{2}, \frac{1}{2},-1\right)\)**

**Detailed Solution:**

\(\begin{aligned}
& \frac{\mathrm{d}}{\mathrm{dx}}(\mathrm{A} \ln |\cos \mathrm{x}+\sin \mathrm{x}-2|+\mathrm{Bx}+\mathrm{C}) \\
&= \mathrm{A} \frac{\cos \mathrm{x}-\sin \mathrm{x}}{\cos \mathrm{x}+\sin \mathrm{x}-2}+\mathrm{B} \\
&= \frac{\mathrm{A} \cos \mathrm{x}-\mathrm{A} \sin \mathrm{x}+\mathrm{B} \cos \mathrm{x}+\mathrm{B} \sin \mathrm{x}-2 \mathrm{~B}}{\cos \mathrm{x}+\sin \mathrm{x}-2} \\
& \therefore 2=\mathrm{A}+\mathrm{B} \text { or }-1=-\mathrm{A}+\mathrm{B} ; \lambda=-2 \mathrm{~B} \\
& \therefore \mathrm{A}=3 / 2, \mathrm{~B}=1 / 2, \lambda=-1
\end{aligned}\)

</details>

---

