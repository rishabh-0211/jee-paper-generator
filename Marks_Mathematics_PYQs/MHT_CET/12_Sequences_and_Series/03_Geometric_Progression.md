# MHT CET Mathematics - Sequences and Series

## Topic 3: Geometric Progression

**Total Questions:** 9

---

### Q1. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\frac{1}{6} \sin \theta, \cos \theta, \tan \theta$ are in G.P., then the general solution of $\theta$ is

**Options:**

- **(A)** $2 n \pi \pm \frac{\pi}{3}, n \in \mathbb{Z}$
- **(B)** $\mathrm{n} \pi+\frac{\pi}{3}, \mathrm{n} \in \mathbb{Z}$
- **(C)** $\mathrm{n} \pi+\frac{\pi}{4}, \mathrm{n} \in \mathbb{Z}$
- **(D)** $2 \mathrm{n} \pi \pm \frac{\pi}{6}, \mathrm{n} \in \mathbb{Z}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 n \pi \pm \frac{\pi}{3}, n \in \mathbb{Z}$**

**Detailed Solution:**

Given that $\dfrac{1}{6} \sin \theta, \cos \theta, \tan \theta$ are in G.P.

$\cos^2 \theta = \dfrac{1}{6} \sin \theta \cdot \tan \theta$

$\cos^2 \theta = \dfrac{1}{6} \sin \theta \cdot \dfrac{\sin \theta}{\cos \theta}$

$6 \cos^3 \theta = \sin^2 \theta$

$6 \cos^3 \theta = 1 - \cos^2 \theta$

$6 \cos^3 \theta + \cos^2 \theta - 1 = 0$

$(2 \cos \theta - 1)(3 \cos^2 \theta + 2 \cos \theta + 1) = 0$

For the quadratic factor $3 \cos^2 \theta + 2 \cos \theta + 1 = 0$, the discriminant is $D = 2^2 - 4(3)(1) = -8 < 0$, so it has no real roots.

Therefore, we must have:

$2 \cos \theta - 1 = 0$

$\cos \theta = \dfrac{1}{2}$

$\cos \theta = \cos \left(\dfrac{\pi}{3}\right)$

The general solution is:

$\theta = 2n\pi \pm \dfrac{\pi}{3}, n \in \mathbb{Z}$

Answer: $2 n \pi \pm \frac{\pi}{3}, n \in \mathbb{Z}$

</details>

---

### Q2. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The money invested in a company is compounded continuously. ₹400 invested today becomes $₹ 800$ in 6 years, then at the end of 33 years, it will become $_{-}(\sqrt{2} = 1.4142)$

**Options:**

- **(A)** $9050.88$
- **(B)** $18101.76$
- **(C)** $6788.16$
- **(D)** $12067.84$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $18101.76$**

**Detailed Solution:**

Let $P$ be the principal amount and $A$ be the amount at time $t$.

Since the money is compounded continuously, the rate of growth is proportional to the amount present, which gives $A = P e^{rt}$.

Given $P = 400$ and $A = 800$ when $t = 6$.

$800 = 400 e^{6r}$

$e^{6r} = 2$

We need to find the amount $A$ when $t = 33$.

$A = 400 e^{33r}$

$A = 400 (e^{6r})^{\dfrac{33}{6}}$

$A = 400 (2)^{\dfrac{11}{2}}$

$A = 400 \times 2^5 \times 2^{\dfrac{1}{2}}$

$A = 400 \times 32 \times \sqrt{2}$

$A = 12800 \sqrt{2}$

Substituting $\sqrt{2} = 1.4142$:

$A = 12800 \times 1.4142 = 18101.76$

Answer: $18101.76$

</details>

---

### Q3. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Rate of increase of bacteria in a culture is proportional to the number of bacteria present at that instant and it is found that the number doubles in 6 hours. The number of bacteria becomes times at the end of 18 hours.

**Options:**

- **(A)** 9
- **(B)** 6
- **(C)** 8
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8**

**Detailed Solution:**

Let $P_0$ be the initial population and let the population after $t$ years be $P$. Then,
$$
\begin{aligned}
& \frac{\mathrm{dP}}{\mathrm{dt}}=\mathrm{kP} \text {, where } \mathrm{k}>0 \\
& \Rightarrow \frac{\mathrm{dP}}{\mathrm{P}}=\mathrm{kdt}
\end{aligned}
$$
Integrating on both sides, we get
$$
\begin{aligned}
& \log \mathrm{P}=\mathrm{kt}+\mathrm{c} \\
& \text { When } \mathrm{t}=0, \mathrm{P}=\mathrm{P}_0 \\
& \therefore \quad \log \mathrm{P}_0=0+\mathrm{c} \\
& \Rightarrow c=\log \mathrm{P}_0 \\
& \log \mathrm{P}=\mathrm{kt}+\log \mathrm{P}_0 \\
& \Rightarrow \log \frac{\mathrm{P}}{\mathrm{P}_0}=\mathrm{kt} \\
& \begin{aligned}
\therefore \quad & \log \mathrm{P}=\mathrm{kt}+\log \mathrm{P}_0 \\
& \Rightarrow \log \frac{\mathrm{P}}{\mathrm{P}_0}=\mathrm{kt} \\
& \text { When } \mathrm{t}=6 \text { hrs, } \mathrm{P}=2 \mathrm{P}_0
\end{aligned} \\
& \therefore \quad \log \frac{2 \mathrm{P}_0}{\mathrm{P}_0}=6 \mathrm{k} \\
& \Rightarrow \mathrm{k}=\frac{\log 2}{6} \\
& \therefore \quad \log \frac{P}{P_0}=\frac{\log 2}{6} t \\
& \text { When } \mathrm{t}=18 \mathrm{hrs} \text {, we have } \\
& \log \frac{P}{P_0}=\frac{\log 2}{6} \times 18 \\
& =3 \log 2 \\
& \therefore \quad \log \frac{P}{P_0}=\log 8 \\
& \Rightarrow \mathrm{P}=8 \mathrm{P}_0 \\
&
\end{aligned}
$$

</details>

---

### Q4. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The sum of first four terms of a G.P. is 160 and the common ratio is 3 , then the $4^{\text {th }}$
term is

**Options:**

- **(A)** 118
- **(B)** 100
- **(C)** 108
- **(D)** 102

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 108**

**Detailed Solution:**

$a, a r, a r^{2}, a r^{3}$
$2=3$
$\frac{a\left(\varepsilon^{4}-1\right)}{(\varepsilon-1)}=160$
Solving these we get $a=4$
$a \varepsilon^{3}=t_{4}=108$

</details>

---

### Q5. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The rational form of a number $1 \cdot \overline{41}$ is

**Options:**

- **(A)** $\frac{154}{99}$
- **(B)** $\frac{55}{99}$
- **(C)** $\frac{140}{99}$
- **(D)** $\frac{41}{99}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{140}{99}$**

**Detailed Solution:**

The rational form of a number $1.41$ is $\frac{140}{99}$.
Let $x=1.414141 \quad$...(i) $100 x=141.414141 \quad$...(ii)
Subtract Eq. (i) from Eq. (ii), we get
$99 x=140$
$x=\frac{140}{99}$ $\therefore 1 . \overline{41}=\frac{140}{99}$

</details>

---

### Q6. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a sequence $\left(t_{n}\right)$ if $s_{n}=7\left(3^{n}-1\right)$, then $t_{n}=$

**Options:**

- **(A)** $(7) 3^{n-1}$
- **(B)** (14) $3^{n+1}$
- **(C)** $(14) 3^{n-1}$
- **(D)** $\quad(7) 3^{n+1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(14) 3^{n-1}$**

**Detailed Solution:**

A sequence; $t_{n} ;$
$$
\begin{aligned}
s_{n} &=7\left(3^{n-1}\right) \\
s_{n-1} &=7\left(3^{n-1}-1\right) \\
&
\end{aligned}
$$
$$
\begin{aligned}
t_{n} &=s_{n}-s_{n-1} \\
t_{n} &=7\left(3^{n}-3^{n-1}\right) \\
&=7 \cdot 3^{n-1} \cdot 2 \\
&=14 \cdot 3^{n-1}
\end{aligned}
$$

</details>

---

### Q7. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a G.P., if <math><msup><mrow><mfenced separators="|"><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></mfenced></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term is <math><mi>p</mi></math> and <math><msup><mrow><mfenced separators="|"><mrow><mi>m</mi><mo>-</mo><mi>n</mi></mrow></mfenced></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term is <math><mi>q</mi><mo>,</mo></math> then <math><msup><mrow><mi>m</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term is ________

**Options:**

- **(A)** <math><mi>p</mi><mi>q</mi></math>
- **(B)** <math><msqrt><mi>p</mi><mi>q</mi></msqrt></math>
- **(C)** <math><mfrac><mrow><mi>p</mi></mrow><mrow><mi>q</mi></mrow></mfrac></math>
- **(D)** <math><mi></mi><mfrac><mrow><mi>q</mi></mrow><mrow><mi>p</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msqrt><mi>p</mi><mi>q</mi></msqrt></math>**

**Detailed Solution:**

In a G.P., each term is G. M. of terms which we are equal distance from it 
Then, <math><msup><mrow><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mi>m</mi></mrow></msub></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msub><mrow><mi>T</mi></mrow><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msub><mo> </mo><msub><mrow><mi>T</mi></mrow><mrow><mi>m</mi><mo>-</mo><mi>n</mi></mrow></msub></math>  
then, <math><mo> </mo><msub><mrow><mi>T</mi></mrow><mrow><mi>m</mi></mrow></msub><mo>=</mo><msqrt><mi>p</mi><mi>q</mi></msqrt></math>

</details>

---

### Q8. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of an infinite GP be 9 and sum of first two terms be 5 then their common ratio is …..

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** 3
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

We have, 
Sum of infinite GP, <math><mfrac><mrow><mi>a</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac><mo>=</mo><mn>9</mn></math>  
<math><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>=</mo><mn>5</mn></math>  
<math><mo>&#8658;</mo><mi>a</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math>  
<math><mo>&#8658;</mo><mn>9</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math>  
<math><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&#8658;</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q9. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If A, B, C are <math><msup><mrow><mi>p</mi></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup><mo>,</mo><msup><mrow><mi>q</mi></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup><mi></mi></math> and <math><msup><mrow><mi>r</mi></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup><mi></mi></math> terms of a GP respectively then <math><msup><mrow><mi>A</mi></mrow><mrow><mi>q</mi><mo>-</mo><mi>r</mi></mrow></msup><mo>.</mo><msup><mrow><mi>B</mi></mrow><mrow><mi>r</mi><mo>-</mo><mi>p</mi></mrow></msup><mo>.</mo><msup><mrow><mi>C</mi></mrow><mrow><mi>p</mi><mo>-</mo><mi>q</mi></mrow></msup><mo>=</mo></math> ….

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 3
- **(D)** – 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let first term and common ratio of a GP are m and n respectively. Then,<math><mi>A</mi><mo>=</mo><mi>m</mi><mfenced separators="|"><mrow><msup><mrow><mi>n</mi></mrow><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mtext>    </mtext><mo>…</mo></math> (i)
<math><mi>B</mi><mo>=</mo><mi>m</mi><mfenced separators="|"><mrow><msup><mrow><mi>n</mi></mrow><mrow><mi>q</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mtext>    </mtext><mo>…</mo></math> (ii)
and <math><mi>C</mi><mo>=</mo><mi>m</mi><mfenced separators="|"><mrow><msup><mrow><mi>n</mi></mrow><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mtext>    </mtext><mo>…</mo></math> (iii)
Now, <math><msup><mrow><mi>A</mi></mrow><mrow><mi>q</mi><mo>-</mo><mi>r</mi></mrow></msup><mo>.</mo><msup><mrow><mi>B</mi></mrow><mrow><mi>r</mi><mo>-</mo><mi>p</mi></mrow></msup><mo>.</mo><msup><mrow><mi>C</mi></mrow><mrow><mi>p</mi><mo>-</mo><mi>q</mi></mrow></msup></math>
<math><mo>=</mo><msup><mrow><mi>m</mi></mrow><mrow><mfenced separators="|"><mrow><mi>q</mi><mo>-</mo><mi>r</mi></mrow></mfenced></mrow></msup><mo>.</mo><msup><mrow><mi>n</mi></mrow><mrow><mfenced separators="|"><mrow><mi>q</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup><mo>.</mo><msup><mrow><mi>m</mi></mrow><mrow><mfenced separators="|"><mrow><mi>r</mi><mo>-</mo><mi>p</mi></mrow></mfenced></mrow></msup><mo>.</mo><msup><mrow><mi>n</mi></mrow><mrow><mfenced separators="|"><mrow><mi>r</mi><mo>-</mo><mi>p</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>q</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup><mo>.</mo><msup><mrow><mi>m</mi></mrow><mrow><mfenced separators="|"><mrow><mi>p</mi><mo>-</mo><mi>q</mi></mrow></mfenced></mrow></msup><mo>.</mo><msup><mrow><mi>n</mi></mrow><mrow><mfenced separators="|"><mrow><mi>p</mi><mo>-</mo><mi>q</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup></math>
<math><mo>=</mo><msup><mrow><mi>m</mi></mrow><mrow><mi>q</mi><mo>-</mo><mi>r</mi><mo>+</mo><mi>r</mi><mo>-</mo><mi>p</mi><mo>+</mo><mi>p</mi><mo>-</mo><mi>q</mi></mrow></msup><mo>.</mo><msup><mrow><mi>n</mi></mrow><mrow><mi>q</mi><mi>p</mi><mo>-</mo><mi>q</mi><mo>-</mo><mi>r</mi><mi>p</mi><mo>+</mo><mi>r</mi><mo>+</mo><mi>r</mi><mi>q</mi><mo>-</mo><mi>r</mi><mo>-</mo><mi>r</mi><mo>-</mo><mi>p</mi><mi>q</mi><mo>+</mo><mi>p</mi><mo>+</mo><mi>p</mi><mi>r</mi><mo>-</mo><mi>p</mi><mo>-</mo><mi>q</mi><mi>r</mi><mo>+</mo><mi>q</mi></mrow></msup></math>
<math><mo>=</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>0</mn></mrow></msup><mo>.</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>0</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>×</mo><mn>1</mn><mo>=</mo><mn>1</mn></math>

</details>

---

