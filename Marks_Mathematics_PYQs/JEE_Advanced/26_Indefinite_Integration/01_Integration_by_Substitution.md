# JEE Advanced Mathematics - Indefinite Integration

## Topic 1: Integration by Substitution

**Total Questions:** 3

---

### Q1. JEE Advanced 2012 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

The integral $\int \frac{\sec ^{2} x}{(\sec x+\tan x)^{\frac{9}{2}}} d x$ equals (for some arbitrary constant $\mathrm{K}$ )

**Options:**

- **(A)** $-\frac{1}{(\sec x+\tan x)^{\frac{11}{2}}}\left\{\frac{1}{11}-\frac{1}{7}(\sec x+\tan x)^{2}\right\}+K$
- **(B)** $\frac{1}{(\sec x+\tan x)^{\frac{11}{2}}}\left\{\frac{1}{11}-\frac{1}{7}(\sec x+\tan x)^{2}\right\}+K$
- **(C)** $-\frac{1}{(\sec x+\tan x)^{\frac{11}{2}}}\left\{\frac{1}{11}+\frac{1}{7}(\sec x+\tan x)^{2}\right\}+K$
- **(D)** $\frac{1}{(\sec x+\tan x)^{\frac{11}{2}}}\left\{\frac{1}{11}+\frac{1}{7}(\sec x+\tan x)^{2}\right\}+K$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{1}{(\sec x+\tan x)^{\frac{11}{2}}}\left\{\frac{1}{11}+\frac{1}{7}(\sec x+\tan x)^{2}\right\}+K$**

**Detailed Solution:**

$\begin{array}{l}

I=\int \frac{\sec ^{2} x}{(\sec x+\tan x)^{9 / 2}} d x \\

\text { Let } \sec x+\tan x=t \Rightarrow \sec x-\tan x=\frac{1}{t} \\

\Rightarrow \sec x=\frac{1}{2}\left(t+\frac{1}{t}\right) \text { and } \sec x(\sec x+\tan x) d x=d t \\

\Rightarrow \sec x d x=\frac{d t}{t} \\

\therefore \quad I=\frac{1}{2} \int \frac{\left(t+\frac{1}{t}\right) d t}{t^{9 / 2} \cdot t}=\frac{1}{2} \int\left(t^{-9 / 2}+t^{-13 / 2}\right) d t \\

=\frac{-1}{7} t^{-7 / 2}-\frac{1}{11} t^{-1 / 2}+K \\

=-\frac{1}{7 t^{7 / 2}}-\frac{1}{11 t^{11 / 2}}+K=-\frac{1}{t^{11 / 2}}\left(\frac{1}{11}+\frac{t^{2}}{7}\right)+K \\

=\frac{-1}{(\sec x+\tan x)^{11 / 2}}\left\{\frac{1}{11}+\frac{1}{7}(\sec x+\tan x)^{2}\right\}+K

\end{array}$

</details>

---

### Q2. JEE Advanced 2007 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $F(x)$ be an indefinite integral of $\sin ^2 x$.
Statement I The function $F(x)$ satisfies $F(x+\pi)=F(x)$ for all real $x$.
Statement II $\sin ^2(x+\pi)=\sin ^2 x$ for all real $x$.

**Options:**

- **(A)** Statement I is true, Statement II is true; Statement II is a correct explanation for Statement I
- **(B)** Statement I is true, Statement II is true; Statement II is not a correct explanation for Statement I.
- **(C)** Statement I is true, Statement II is false
- **(D)** Statement I is false, Statement II is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement I is false, Statement II is true**

**Detailed Solution:**

$$
\begin{aligned}
& F(x)=\int \sin ^2 x d x=\int \frac{1-\cos 2 x}{2} d x \\
& \Rightarrow F(x)=\frac{1}{4}(2 x-\sin 2 x)+c
\end{aligned}
$$
Since, $F(x+\pi) \neq F(x)$.
Hence, Statement I is false.
But Statement II is true as $\sin ^2 x$ is periodic with period $\pi$.

</details>

---

### Q3. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

The value of $\int \frac{\left(x^2-1\right) d x}{x^3 \sqrt{2 x^4-2 x^2+1}}$ is

**Options:**

- **(A)** $2 \sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}+C$
- **(B)** $2 \sqrt{2+\frac{2}{x^2}+\frac{1}{x^4}}+C$
- **(C)** $\frac{1}{2} \sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}+C$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2} \sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}+C$**

**Detailed Solution:**

Let $\quad I=\int \frac{\left(x^2-1\right) d x}{x^3 \sqrt{2 x^4-2 x^2+1}}$,
On dividing numerater and denominator by $x^5$, we get
$$
=\int \frac{\left(\frac{1}{x^3}-\frac{1}{x^5}\right) d x}{\sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}}
$$
put $2-\frac{2}{x^2}+\frac{1}{x^4}=t \Rightarrow\left(\frac{4}{x^3}-\frac{4}{x^5}\right) d x=d t$
$$
\therefore \quad I=\frac{1}{4} \int \frac{d t}{\sqrt{t}}=\frac{1}{4} \cdot \frac{t^{1 / 2}}{1 / 2}=\frac{1}{2} \sqrt{t}+c=\frac{1}{2} \sqrt{2-\frac{2}{x^2}+\frac{1}{x^4}}+C
$$

</details>

---

