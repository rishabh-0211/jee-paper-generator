# MHT CET Mathematics - Trigonometric Ratios & Identities

## Topic 5: T-Ratios of Multiple & sub multiple angles

**Total Questions:** 13

---

### Q1. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\cos\left(\dfrac{\pi}{5}\right)$ is ...

**Options:**

- **(A)** $\dfrac{-1 + \sqrt{5}}{4}$
- **(B)** $\dfrac{-1 + \sqrt{5}}{2}$
- **(C)** $\dfrac{1 + \sqrt{5}}{4}$
- **(D)** $\dfrac{1 - \sqrt{5}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1 + \sqrt{5}}{4}$**

**Detailed Solution:**

Let $x = \dfrac{\pi}{5}$.

$5x = \pi \Rightarrow 2x = \pi - 3x$

Taking sine on both sides:

$\sin(2x) = \sin(\pi - 3x)$

$\sin(2x) = \sin(3x)$

$2\sin x \cos x = 3\sin x - 4\sin^3 x$

Since $\sin x \neq 0$, dividing by $\sin x$ gives:

$2\cos x = 3 - 4\sin^2 x$

$2\cos x = 3 - 4(1 - \cos^2 x)$

$4\cos^2 x - 2\cos x - 1 = 0$

Solving the quadratic equation for $\cos x$:

$\cos x = \dfrac{2 \pm \sqrt{4 - 4(4)(-1)}}{2(4)} = \dfrac{2 \pm \sqrt{20}}{8} = \dfrac{1 \pm \sqrt{5}}{4}$

Since $x = \dfrac{\pi}{5}$ lies in the first quadrant, $\cos x > 0$.

Therefore, $\cos\left(\dfrac{\pi}{5}\right) = \dfrac{1 + \sqrt{5}}{4}$

Answer: $\dfrac{1 + \sqrt{5}}{4}$

</details>

---

### Q2. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of
$\begin{aligned}
& \cos \left(18^{\circ}-\mathrm{A}\right) \cos \left(18^{\circ}+\mathrm{A}\right) \\
& -\cos \left(72^{\circ}-\mathrm{A}\right) \cos \left(72^{\circ}+\mathrm{A}\right) \text { is equal to }
\end{aligned}$

**Options:**

- **(A)** $\cos 54^{\circ}$
- **(B)** $\cos 72^{\circ}$
- **(C)** $\sin 54^{\circ}$
- **(D)** $\sin 36^{\circ}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sin 54^{\circ}$**

**Detailed Solution:**

Using the trigonometric identity $\cos(x - y) \cos(x + y) = \cos^2 x - \sin^2 y$, the given expression can be simplified as follows:

$\cos(18^{\circ} - \mathrm{A}) \cos(18^{\circ} + \mathrm{A}) - \cos(72^{\circ} - \mathrm{A}) \cos(72^{\circ} + \mathrm{A})$

$= (\cos^2 18^{\circ} - \sin^2 \mathrm{A}) - (\cos^2 72^{\circ} - \sin^2 \mathrm{A})$

$= \cos^2 18^{\circ} - \cos^2 72^{\circ}$

Since $\cos 72^{\circ} = \sin(90^{\circ} - 72^{\circ}) = \sin 18^{\circ}$, substituting this into the expression gives:

$= \cos^2 18^{\circ} - \sin^2 18^{\circ}$

Using the double angle formula $\cos^2 \theta - \sin^2 \theta = \cos 2\theta$:

$= \cos(2 \times 18^{\circ})$

$= \cos 36^{\circ}$

Using the complementary angle identity $\cos \theta = \sin(90^{\circ} - \theta)$, we get:

$\cos 36^{\circ} = \sin(90^{\circ} - 36^{\circ}) = \sin 54^{\circ}$

Answer: $\sin 54^{\circ}$

</details>

---

### Q3. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\left(1+\cos \dfrac{\pi}{8}\right)\left(1+\cos \dfrac{3 \pi}{8}\right)\left(1+\cos \dfrac{5 \pi}{8}\right)\left(1+\cos \dfrac{7 \pi}{8}\right)$ is

**Options:**

- **(A)** $\dfrac{1}{8}$
- **(B)** $\dfrac{-1}{8}$
- **(C)** $\dfrac{1}{16}$
- **(D)** $\dfrac{-1}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{8}$**

**Detailed Solution:**

Using the property $\cos(\pi - \theta) = -\cos \theta$, we can write:

$\cos \dfrac{7\pi}{8} = \cos \left(\pi - \dfrac{\pi}{8}\right) = -\cos \dfrac{\pi}{8}$

$\cos \dfrac{5\pi}{8} = \cos \left(\pi - \dfrac{3\pi}{8}\right) = -\cos \dfrac{3\pi}{8}$

Substituting these into the given expression:

$\left(1+\cos \dfrac{\pi}{8}\right)\left(1+\cos \dfrac{3 \pi}{8}\right)\left(1-\cos \dfrac{3 \pi}{8}\right)\left(1-\cos \dfrac{\pi}{8}\right)$

Grouping the terms and using $(a+b)(a-b) = a^2 - b^2$:

$\left(1-\cos^2 \dfrac{\pi}{8}\right) \left(1-\cos^2 \dfrac{3 \pi}{8}\right)$

Using $1-\cos^2 \theta = \sin^2 \theta$:

$\sin^2 \dfrac{\pi}{8} \sin^2 \dfrac{3 \pi}{8}$

Since $\dfrac{3\pi}{8} = \dfrac{\pi}{2} - \dfrac{\pi}{8}$, we have $\sin \dfrac{3\pi}{8} = \cos \dfrac{\pi}{8}$. The expression becomes:

$\sin^2 \dfrac{\pi}{8} \cos^2 \dfrac{\pi}{8}$

Multiplying and dividing by $4$:

$\dfrac{1}{4} \left(2 \sin \dfrac{\pi}{8} \cos \dfrac{\pi}{8}\right)^2$

Using the double angle formula $\sin 2\theta = 2 \sin \theta \cos \theta$:

$\dfrac{1}{4} \left(\sin \dfrac{\pi}{4}\right)^2$

Substituting $\sin \dfrac{\pi}{4} = \dfrac{1}{\sqrt{2}}$:

$\dfrac{1}{4} \left(\dfrac{1}{\sqrt{2}}\right)^2 = \dfrac{1}{4} \times \dfrac{1}{2} = \dfrac{1}{8}$

Answer: $\dfrac{1}{8}$

</details>

---

### Q4. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of the expression $\sqrt{3} \operatorname{cosec} 20^{\circ}-\sec 20^{\circ}$ is equal to

**Options:**

- **(A)** 2
- **(B)** $\dfrac{2 \sin 20^{\circ}}{\sin 40^{\circ}}$
- **(C)** 4
- **(D)** $4 \dfrac{\sin 20^{\circ}}{\sin 40^{\circ}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

The given expression is $\sqrt{3} \operatorname{cosec} 20^{\circ} - \sec 20^{\circ}$.

Converting to sine and cosine, we get:

$\dfrac{\sqrt{3}}{\sin 20^{\circ}} - \dfrac{1}{\cos 20^{\circ}}$

Taking the common denominator:

$\dfrac{\sqrt{3} \cos 20^{\circ} - \sin 20^{\circ}}{\sin 20^{\circ} \cos 20^{\circ}}$

Multiplying and dividing the numerator by $2$, and the denominator by $2$:

$\dfrac{2 \left( \dfrac{\sqrt{3}}{2} \cos 20^{\circ} - \dfrac{1}{2} \sin 20^{\circ} \right)}{\dfrac{1}{2} (2 \sin 20^{\circ} \cos 20^{\circ})}$

Substituting $\sin 60^{\circ} = \dfrac{\sqrt{3}}{2}$ and $\cos 60^{\circ} = \dfrac{1}{2}$ in the numerator, and using $\sin 2\theta = 2 \sin \theta \cos \theta$ in the denominator:

$\dfrac{4 (\sin 60^{\circ} \cos 20^{\circ} - \cos 60^{\circ} \sin 20^{\circ})}{\sin 40^{\circ}}$

Using the identity $\sin(A - B) = \sin A \cos B - \cos A \sin B$:

$\dfrac{4 \sin(60^{\circ} - 20^{\circ})}{\sin 40^{\circ}}$

$\dfrac{4 \sin 40^{\circ}}{\sin 40^{\circ}}$

$4$

Answer: 4

</details>

---

### Q5. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\tan \left(\frac{\pi}{8}\right)$ is

**Options:**

- **(A)** $\sqrt{2}-1$
- **(B)** $1-\sqrt{2}$
- **(C)** $\sqrt{2}$
- **(D)** $\sqrt{2}+1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{2}-1$**

**Detailed Solution:**

Since, $\tan \frac{A}{2}=\frac{1-\cos A}{\sin A}$ Putting $\frac{\mathrm{A}}{2}=\frac{\pi}{8}$, we get
$\begin{aligned} \tan \left(\frac{\pi}{8}\right) & =\frac{1-\cos \frac{\pi}{4}}{\sin \frac{\pi}{4}} \\ & =\frac{1-\frac{1}{\sqrt{2}}}{\left(\frac{1}{\sqrt{2}}\right)} \\ \therefore \quad \tan \left(\frac{\pi}{8}\right) & =\sqrt{2}-1\end{aligned}$

</details>

---

### Q6. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In a triangle $\mathrm{ABC}$, with usual notations, if $\mathrm{c}=4$, then value of $(a-b)^2 \cos ^2 \frac{C}{2}+(a+b)^2 \sin ^2 \frac{C}{2}$ is

**Options:**

- **(A)** $4$
- **(B)** $16$
- **(C)** $9$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $16$**

**Detailed Solution:**

$\begin{aligned} & (a-b)^2 \cos ^2 \frac{C}{2}+(a+b)^2 \sin ^2 \frac{C}{2} \\ & =\left(a^2-2 a b+b^2\right) \cos ^2 \frac{C}{2}+\left(a^2+2 a b+b^2\right) \sin ^2 \frac{C}{2} \\ & =\left(a^2+b^2\right)\left(\cos ^2 \frac{C}{2}+\sin ^2 \frac{C}{2}\right) \\ & \quad-2 a b \cos ^2 \frac{C}{2}+2 a b \sin ^2 \frac{C}{2} \\ & =a^2+b^2-2 a b\left(\cos ^2 \frac{C}{2}-\sin ^2 \frac{C}{2}\right) \\ & =a^2+b^2-2 a b \cdot \cos C \\ & =a^2+b^2-\left(a^2+b^2-c^2\right) \quad \ldots[\text { By Cosine rule }] \\ & =c^2=4^2=16\end{aligned}$

</details>

---

### Q7. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\cos 2 B-\frac{\cos (A+C)}{\cos (A-C)}$, Then $\tan A, \tan B, \tan C$ are in

**Options:**

- **(A)** Geometric Progression.
- **(B)** Arithmetic Progression.
- **(C)** Harmonic Progression.
- **(D)** Arithmetico-Geometric Progression.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Geometric Progression.**

**Detailed Solution:**

$\begin{aligned} & \cos 2 B=\frac{\cos (A+C)}{\cos (A-C)} \\ & \frac{1-\tan ^2 B}{1+\tan ^2 B}=\frac{\cos A \cos C-\sin A \sin C}{\cos A \cos C+\sin A \sin C} \\ & \frac{1-\tan ^2 B}{1+\tan ^2 B}=\frac{\cos A \cos C(1-\tan A \tan C)}{\cos A \cos C(1+\tan A \tan C)} \\ & \frac{1-\tan ^2 B}{1+\tan ^2 B}=\frac{(1-\tan A \tan C)}{(1+\tan A \tan C)}\end{aligned}$
$\begin{aligned} &\left(1-\tan ^2 \mathrm{~B}\right)(1+\tan \mathrm{A} \tan \mathrm{C}) \\ & \quad=(1-\tan \mathrm{A} \tan \mathrm{C})\left(1+\tan ^2 \mathrm{~B}\right) \\ & \quad 1+\tan \mathrm{A} \tan \mathrm{C}-\tan ^2 \mathrm{~B}-\tan ^2 \mathrm{~B} \tan \mathrm{A} \tan \mathrm{C} \\ & \quad=1+\tan ^2 \mathrm{~B}-\tan \mathrm{A} \tan \mathrm{C}-\tan \mathrm{A} \tan \mathrm{C} \tan ^2 \mathrm{~B} \\ & \quad 2 \tan \mathrm{A} \tan \mathrm{C}=2 \tan ^2 \mathrm{~B} \\ & \quad \tan ^2 \mathrm{~B}=\tan \mathrm{A} \cdot \tan \mathrm{C} \\ & \therefore \quad \tan \mathrm{A}, \tan \mathrm{B}, \tan \mathrm{C} \text { are in G.P. }\end{aligned}$

</details>

---

### Q8. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan \theta=\frac{a}{b}$, then $b \cos 2 \theta+a \sin 2 \theta=$

**Options:**

- **(A)** b
- **(B)** a
- **(C)** 0
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) b**

**Detailed Solution:**

$\begin{aligned} & b \cos 2 \theta+a \sin 2 \theta=b \times \frac{1-\tan ^2 \theta}{1+\tan ^2 \theta}+a \times \frac{2 \tan \theta}{1+\tan ^2 \theta} \\ & =b \times \frac{1-\frac{a^2}{b^2}}{1+\frac{a^2}{b^2}}+a \times \frac{2 \times \frac{a}{b}}{1+\frac{a^2}{b^2}} \\ & =\frac{b\left(b^2-a^2\right)}{b^2+a^2}+\frac{2 a^2 b}{b^2+a^2} \\ & =\frac{b\left(b^2+a^2\right)}{b^2+a^2}=b\end{aligned}$

</details>

---

### Q9. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\tan A+2 \tan 2 A+4 \tan 4 A+8 \cot 8 A=$

**Options:**

- **(A)** $\tan 2 \mathrm{~A}$
- **(B)** $\cot \mathrm{A}$
- **(C)** $\tan \mathrm{A}$
- **(D)** $\cot 2 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\cot \mathrm{A}$**

**Detailed Solution:**

$\begin{aligned} & \tan A+2 \tan 2 A+4 \tan 4 A+8 \cot 8 A \\ & =\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+4 \tan 4 \mathrm{~A}+\frac{8}{\left(\frac{2 \tan 4 \mathrm{~A}}{1-\tan ^2 4 \mathrm{~A}}\right)} \\ & =\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+4 \tan 4 \mathrm{~A}+\frac{8\left(1-\tan ^2 \mathrm{~A}\right)}{2 \tan 4 \mathrm{~A}} \\ & =\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+\frac{(4 \tan 4 \mathrm{~A})(2 \tan 4 \mathrm{~A})+8\left(1-\tan ^2 4 \mathrm{~A}\right)}{2 \tan 4 \mathrm{~A}} \\ & =\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+\frac{8}{2 \tan 4 \mathrm{~A}} \\ & =\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+\frac{8}{2\left(\frac{2 \tan \mathrm{A}}{1-\tan ^2 2 \mathrm{~A}}\right)} \\ & =\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+\frac{8\left(1-\tan ^2 2 \mathrm{~A}\right)}{4 \tan 2 \mathrm{~A}} \\ & =\tan \mathrm{A}+\frac{(2 \tan 2 \mathrm{~A})(4 \tan 2 \mathrm{~A})+8\left(1-\tan ^2 2 \mathrm{~A}\right)}{4 \tan 2 \mathrm{~A}}=\tan \mathrm{A}+\frac{8}{4 \tan 2 \mathrm{~A}} \\ & =\tan \mathrm{A}+\frac{8}{4\left(\frac{2 \tan \mathrm{A}}{1-\tan ^2 \mathrm{~A}}\right)}=\tan \mathrm{A}+\frac{8\left(1-\tan ^2 \mathrm{~A}\right)}{8 \tan \mathrm{A}} \\ & \end{aligned}$
$=\frac{\tan \mathrm{A}(8 \tan \mathrm{A})+8\left(1-\tan ^2 \mathrm{~A}\right)}{8 \tan \mathrm{A}}=\frac{8}{8 \tan \mathrm{A}}=\cot \mathrm{A}$

</details>

---

### Q10. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\frac{1-\sin \theta+\cos \theta}{1-\sin \theta-\cos \theta}=$

**Options:**

- **(A)** $\cot \frac{\theta}{2}$
- **(B)** $-\cot \frac{\theta}{2}$
- **(C)** $\tan \frac{\theta}{2}$
- **(D)** $-\tan \frac{\theta}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\cot \frac{\theta}{2}$**

**Detailed Solution:**

(D)
$\begin{array}{l}
\text { We know } \sin \theta=2 \sin \frac{\theta}{2} \cdot \cos \frac{\theta}{2} \text { and } \cos \theta=2 \cos ^{2} \frac{\theta}{2}-1=1-2 \sin ^{2} \frac{\theta}{2} \\
\frac{1-\sin \theta+\cos \theta}{1-\sin \theta-\cos \theta}=\frac{1-2 \sin \frac{\theta}{2} \cdot \cos \frac{\theta}{2}+\left(2 \cos ^{2} \frac{\theta}{2}-1\right)}{1-2 \sin \frac{\theta}{2} \cdot \cos \frac{\theta}{2}-\left(1-2 \sin ^{2} \frac{\theta}{2}\right)}
\end{array}$
$=\frac{-2 \sin \frac{\theta}{2} \cdot \cos \frac{\theta}{2}+2 \cos ^{2} \frac{\theta}{2}}{-2 \sin \frac{\theta}{2} \cdot \cos \frac{\theta}{2}+2 \sin ^{2} \frac{\theta}{2}}$
$=\frac{-2 \cos \frac{\theta}{2}\left(\sin \frac{\theta}{2}-\cos \frac{\theta}{2}\right)}{-2 \sin \frac{\theta}{2}\left(\cos \frac{\theta}{2}-\sin \frac{\theta}{2}\right)}=-\cot \frac{\theta}{2}$

</details>

---

### Q11. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\tan A+2 \tan 2 A+4 \tan 4 A+8 \operatorname{Cot} 8 A=$

**Options:**

- **(A)** $\tan A$
- **(B)** $\operatorname{Cot} A$
- **(C)** $\tan 2 \mathrm{~A}$
- **(D)** $\operatorname{Cot} 2 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\operatorname{Cot} A$**

**Detailed Solution:**

(C)
$=\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+4 \tan 4 \mathrm{~A}+8 \times \frac{1-\tan ^{2} 4 \mathrm{~A}}{2 \tan 4 \mathrm{~A}}$
$=\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+4 \tan 4 \mathrm{~A}+\frac{4\left(1-\tan ^{2} 4 \mathrm{~A}\right)}{\tan 4 \mathrm{~A}}$
$=\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+\frac{4 \tan ^{2} 4 \mathrm{~A}+4-4 \tan ^{2} 4 \mathrm{~A}}{\tan 4 \mathrm{~A}}$
$=\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+\frac{4}{\tan 4 \mathrm{~A}}=\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+4 \cot 4 \mathrm{~A}$
$=\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+4 \times \frac{1-\tan ^{2} 2 \mathrm{~A}}{2 \tan 2 \mathrm{~A}}=\tan \mathrm{A}+2 \tan 2 \mathrm{~A}+\frac{2\left(1-\tan ^{2} 2 \mathrm{~A}\right)}{\tan 2 \mathrm{~A}}$
$=\tan \mathrm{A}+\frac{2 \tan ^{2} 2 \mathrm{~A}+2-2 \tan ^{2} 2 \mathrm{~A}}{\tan 2 \mathrm{~A}}=\tan \mathrm{A}+\frac{2}{\tan 2 \mathrm{~A}}$
$=\tan \mathrm{A}+2 \cot 2 \mathrm{~A}=\frac{2\left(1-\tan ^{2} \mathrm{~A}\right)}{2 \tan \mathrm{A}}=\tan \mathrm{A}+\frac{1-\tan ^{2} \mathrm{~A}}{\tan \mathrm{A}}$
$=\frac{\tan ^{2} \mathrm{~A}+1-\tan ^{2} \mathrm{~A}}{\tan \mathrm{A}}=\frac{1}{\tan \mathrm{A}}=\cot \mathrm{A}$

</details>

---

### Q12. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A+B+C=180^{\circ}$, then the value of
$\tan \left(\frac{\mathrm{A}}{2}\right) \tan \left(\frac{\mathrm{B}}{2}\right)+\tan \left(\frac{\mathrm{B}}{2}\right) \tan \left(\frac{\mathrm{C}}{2}\right)+\tan \left(\frac{\mathrm{C}}{2}\right) \tan \left(\frac{\mathrm{A}}{2}\right)$ is

**Options:**

- **(A)** 1
- **(B)** $-1$
- **(C)** $-2$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\ln \Delta A B C, A+B+C=\pi \Rightarrow A+B=\pi-C$
$$
\tan \left(\frac{A+B}{2}\right)=\tan \left(\frac{\pi-C}{2}\right)=\tan \left(\frac{\pi}{2}-\frac{C}{2}\right)
$$
$\therefore \frac{\tan \frac{A}{2}+\tan \frac{B}{2}}{1-\tan \frac{A}{2} \tan \frac{B}{2}}=\cot \frac{C}{2} \Rightarrow \frac{\tan \frac{A}{2}+\tan \frac{B}{2}}{1-\tan \frac{A}{2} \cdot \tan \frac{B}{2}}=\frac{1}{\tan \frac{C}{2}}$
$\therefore \tan \frac{\mathrm{C}}{2}\left(\tan \frac{\mathrm{A}}{2}+\tan \frac{\mathrm{B}}{2}\right) \quad=1-\tan \frac{\mathrm{A}}{2} \tan \frac{\mathrm{B}}{2}$
$\therefore \tan \frac{\mathrm{A}}{2} \tan \frac{\mathrm{B}}{2}+\tan \frac{\mathrm{B}}{2} \tan \frac{\mathrm{C}}{2}+\tan \frac{\mathrm{C}}{2} \tan \frac{\mathrm{A}}{2}=1$

</details>

---

### Q13. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\cos x \cdot \cos 7 x-\cos 5 x \cdot \cos 13 x=$

**Options:**

- **(A)** $2 \cos ^{2} 6 x \cdot \cos 12 x$
- **(B)** $2 \sin ^{2} 6 x \cdot \cos 6 x$
- **(C)** $2 \sin 6 x \cdot \sin 12 x$
- **(D)** $2 \sin 6 x \cdot \cos 12 x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \sin ^{2} 6 x \cdot \cos 6 x$**

**Detailed Solution:**

$\cos x \cos 7 x-\cos 5 x \cos 13 x$
$\begin{array}{l}
=\frac{1}{2}(2 \cos x \cos 7 x-2 \cos 5 x \cos 13 x) \\
=\frac{1}{2}(\cos 8 x+\cos 6 x-\cos 18 x-\cos 8 x) \\
=\frac{1}{2}(\cos 6 x-\cos 18 x)=\frac{1}{2}[(-2) \sin 12 x \sin (-6 x)] \\
=\sin 12 x \sin 6 x=(2 \sin 6 x \cos 6 x) \sin 6 x \\
=2 \sin ^{2} 6 x \cos 6 x
\end{array}$

</details>

---

