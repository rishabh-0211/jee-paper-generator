# JEE Advanced Mathematics - Complex Number

## Topic 3: Polar and Euler Form

**Total Questions:** 3

---

### Q1. JEE Advanced 2024 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

Let $S=\{a+b \sqrt{2}: a, b \in \mathbb{Z}\}, T_1=\left\{(-1+\sqrt{2})^n: n \in \mathbb{N}\right\}$, and $T_2=\left\{(1+\sqrt{2})^n: n \in \mathbb{N}\right\}$. Then which of the following statements is (are) TRUE?

**Options:**

- **(A)** $\mathbb{Z} \cup T_1 \cup T_2 \subset S$
- **(B)** $T_1 \cap\left(0, \frac{1}{2024}\right)=\phi$, where $\phi$ denotes the empty set.
- **(C)** $T_2 \cap(2024, \infty) \neq \phi$
- **(D)** For any given $a, b \in \mathbb{Z}, \cos (\pi(a+b \sqrt{2}))+i \sin (\pi(a+b \sqrt{2})) \in \mathbb{Z}$ if and only if $b=0$, where $i=\sqrt{-1}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) For any given $a, b \in \mathbb{Z}, \cos (\pi(a+b \sqrt{2}))+i \sin (\pi(a+b \sqrt{2})) \in \mathbb{Z}$ if and only if $b=0$, where $i=\sqrt{-1}$.**

**Detailed Solution:**

(1)
$\begin{aligned}& (-1+\sqrt{2})^{\mathrm{n}}=\mathrm{m}+\sqrt{2} \mathrm{n}, \mathrm{m}, \text{ where, } \mathrm{n} \in \mathbb{Z} \\ & (1+\sqrt{2})^{\mathrm{n}}=\mathrm{m}_1+\sqrt{2} \mathrm{n}_1, \text{ where, } \mathrm{~m}_1, \mathrm{n}_1 \in \mathbb{Z} \\& \Rightarrow \mathbb{Z} \cup \mathrm{T}_1 \cup \mathrm{T}_2 \subseteq \mathrm{S}\end{aligned}$
but $b \sqrt{2} \in S$ for negative $b \in \mathbb{Z}$.
So $\mathbb{Z} \cup \mathrm{T}_1 \cup \mathrm{T}_2 \subset \mathrm{S}$
(2)
$\begin{aligned} & (\sqrt{2}-1)^{\mathrm{n}}=\frac{1}{(\sqrt{2}+1)^{\mathrm{n}}} < \frac{1}{2024} \\ & \Rightarrow 2024 < (\sqrt{2}+1)^{\mathrm{n}}, \text{ where, } \exists \mathrm{n} \in \mathbb{N} \\ & \Rightarrow \mathrm{T}_1 \cap\left(0, \frac{1}{2024}\right) \neq \phi\end{aligned}$
(3)
$\begin{aligned} & (1+\sqrt{2})^{\mathrm{n}}>2024, \text{ where, } \exists \mathrm{n} \in \mathbb{N} \\ & \Rightarrow \mathrm{T}_2 \cap(2024, \infty) \neq \phi\end{aligned}$
(4)
$\sin (\pi(a+b \sqrt{2})=0) \Rightarrow b=0, \text{ where, } a \in \mathbb{Z}$
$\Rightarrow$ Options (1), (3), (4) are Correct.

</details>

---

### Q2. JEE Advanced 2020 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

Let <math> <mi>S</mi> </math> be the set of all complex numbers <math> <mi>z</mi> </math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>. Then which of the following statements is/are TRUE?

**Options:**

- **(A)** <math> <mrow> <mfenced close="|" open="|"> <mrow> <mi>z</mi><mo>+</mo><mfrac> <mn>1</mn> <mn>2</mn> </mfrac> </mrow> </mfenced><mo>&#8804;</mo><mfrac> <mn>1</mn> <mn>2</mn> </mfrac> </mrow> </math> for all <math> <mrow> <mi>z</mi><mo>&#8712;</mo><mi>S</mi></mrow> </math>
- **(B)** <math> <mrow>  <mfenced close="|" open="|">   <mi>z</mi>  </mfenced><mo>&#8804;</mo><mn>2</mn></mrow></math> for all <math> <mrow>  <mi>z</mi><mo>&#8712;</mo><mi>S</mi></mrow></math>
- **(C)** <math> <mrow> <mfenced close="|" open="|"> <mrow> <mi>z</mi><mo>+</mo><mfrac> <mn>1</mn> <mn>2</mn> </mfrac> </mrow> </mfenced><mo>&#8805;</mo><mfrac> <mn>1</mn> <mn>2</mn> </mfrac> </mrow> </math> for all <math> <mrow> <mi>z</mi><mo>&#8712;</mo><mi>S</mi></mrow> </math>
- **(D)** The set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> has exactly four elements

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math> <mrow> <mfenced close="|" open="|"> <mrow> <mi>z</mi><mo>+</mo><mfrac> <mn>1</mn> <mn>2</mn> </mfrac> </mrow> </mfenced><mo>&#8805;</mo><mfrac> <mn>1</mn> <mn>2</mn> </mfrac> </mrow> </math> for all <math> <mrow> <mi>z</mi><mo>&#8712;</mo><mi>S</mi></mrow> </math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn><mo>=</mo><msup><mi>e</mi><mrow><mi>i</mi><mi>&#952;</mi></mrow></msup><mtext>&#8195;</mtext><mi>&#952;</mi><mo>&#8712;</mo><mo>(</mo><mo>&#8722;</mo><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mi>&#960;</mi><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>z</mi><mn>2</mn></msup><mo>+</mo><mi>z</mi><mo>+</mo><mn>1</mn><mo>&#8722;</mo><msup><mi>e</mi><mrow><mi>i</mi><mi>&#952;</mi></mrow></msup><mo>=</mo><mn>0</mn></math></p><p>By quadratic formula, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mrow><mo>&#8722;</mo><mn>1</mn><mo>&#177;</mo><msqrt><mn>4</mn><msup><mi>e</mi><mrow><mi>i</mi><mi>&#952;</mi></mrow></msup><mo>&#8722;</mo><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mo>&#177;</mo><msqrt><mfenced><mrow><mn>4</mn><mi>cos</mi><mi>&#952;</mi><mo>&#8722;</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mi>i</mi><mn>4</mn><mi>sin</mi><mi>&#952;</mi></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mi>z</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><msup><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><mn>4</mn><mi>cos</mi><mi>&#952;</mi><mo>&#8722;</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>4</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mi>z</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>&#8712;</mo><mfenced open="[" close="]"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><msqrt><mn>7</mn></msqrt></mrow></mfenced></math></p><p>Option (C) is correct
By equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mn>2</mn><mi>z</mi></mrow></mfenced><mo>&#8804;</mo><mn>1</mn><mo>+</mo><msqrt><mfenced open="|" close="|"><mrow><mn>4</mn><msup><mi>e</mi><mrow><mi>i</mi><mi>&#952;</mi></mrow></msup><mo>&#8722;</mo><mn>3</mn></mrow></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mn>2</mn><mi>Z</mi></mrow></mfenced><mo>&#8804;</mo><mn>1</mn><mo>+</mo><msup><mrow><mo>(</mo><mn>25</mn><mo>&#8722;</mo><mn>24</mn><mi>cos</mi><mi>&#952;</mi><mo>)</mo></mrow><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mn>2</mn><mi>Z</mi></mrow></mfenced><mo>&#8804;</mo><mn>1</mn><mo>+</mo><msqrt><mn>7</mn></msqrt><mo>&#60;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mi>Z</mi></mfenced><mo>&#8804;</mo><mn>2</mn></math></p><p>Option (B) is correct.</p>

</details>

---

### Q3. JEE Advanced 2009 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $z=\cos \theta+i \sin \theta$. Then, the value of $\sum_{m=1}^{15} \operatorname{Im}\left(z^{2 m-1}\right)$ at $\theta=2^{\circ}$ is

**Options:**

- **(A)** $\frac{1}{\sin 2^{\circ}}$
- **(B)** $\frac{1}{3 \sin 2^{\circ}}$
- **(C)** $\frac{1}{2 \sin 2^{\circ}}$
- **(D)** $\frac{1}{4 \sin 2^{\circ}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{4 \sin 2^{\circ}}$**

**Detailed Solution:**

Given that $z=\cos \theta+i \sin \theta=e^{i \theta}$
$$
\begin{aligned}
\therefore \sum_{m=1}^{15} \operatorname{Im}\left(z^{2 m-1}\right) & =\sum_{m=1}^{15} \operatorname{Im}\left(e^{i \theta}\right)^{2 m-1}=\sum_{m=1}^{15} \operatorname{Im} e^{i(2 m-1) \theta} \\
& =\sin \theta+\sin 3 \theta+\sin 5 \theta+\ldots+\sin 29 \theta \\
& =\frac{\sin \left(\frac{\theta+29 \theta}{2}\right) \sin \left(\frac{15 \times 2 \theta}{2}\right)}{\sin \left(\frac{2 \theta}{2}\right)}=\frac{\sin (15 \theta) \sin (15 \theta)}{\sin \theta}=\frac{1}{4 \sin 2^{\circ}}
\end{aligned}
$$

</details>

---

