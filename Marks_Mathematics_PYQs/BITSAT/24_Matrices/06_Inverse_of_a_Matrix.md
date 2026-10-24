# BITSAT Mathematics - Matrices

## Topic 6: Inverse of a Matrix

**Total Questions:** 4

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `1`

If matrix $A=\left[\begin{array}{ccc}3 & -2 & 4 \\ 1 & 2 & -1 \\ 0 & 1 & 1\end{array}\right]$ and $A^{-1}=\frac{1}{k} \operatorname{adj}(A)$, then $k$ is

**Options:**

- **(A)** 7
- **(B)** -7
- **(C)** 15
- **(D)** -11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 15**

**Detailed Solution:**

Given, $A=\left[\begin{array}{ccc}3 & -2 & 4 \\ 1 & 2 & -1 \\ 0 & 1 & 1\end{array}\right]$
and
$A^{-1}=\frac{1}{k} \operatorname{adj}(A)$....(i)
We know that, $A^{-1}=\frac{\operatorname{adj}(A)}{|A|}$...(ii)
By comparing Eqs. (i) and (iii),
$k=|A|$
So,
$\begin{aligned}
|A| & =\left|\begin{array}{ccc}
3 & -2 & 4 \\
1 & 2 & -1 \\
0 & 1 & 1
\end{array}\right| \\
& =3(2+1)+2(1+0)+4(1-0)=15
\end{aligned}$

</details>

---

### Q2. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

$\text { If }\left[\begin{array}{cc}
1 & -\tan \theta \\
\tan \theta & 1
\end{array}\right]\left[\begin{array}{cc}
1 & \tan \theta \\
-\tan \theta & 1
\end{array}\right]^{-1}=\left[\begin{array}{cc}
a & -b \\
b & a
\end{array}\right],$ 
then

**Options:**

- **(A)** $a=1, b=1$
- **(B)** $a=\sin 2 \theta, b=\cos 2 \theta$
- **(C)** $a=\cos 2 \theta, b=\sin 2 \theta$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a=\cos 2 \theta, b=\sin 2 \theta$**

**Detailed Solution:**

Given,
$\left[\begin{array}{cc}1 & -\tan \theta \\ \tan \theta & 1\end{array}\right]\left[\begin{array}{cc}1 & \tan \theta \\ -\tan \theta & 1\end{array}\right]^{-1}=\left[\begin{array}{cc}a & -b \\ b & a\end{array}\right]$
$\Rightarrow\left[\begin{array}{cc}1 & -\tan \theta \\ \tan \theta & 1\end{array}\right] \cdot \frac{1}{1+\tan ^2 \theta}\left[\begin{array}{cc}1 & -\tan \theta \\ \tan \theta & 1\end{array}\right]$
$=\left[\begin{array}{cc}a & -b \\ b & a\end{array}\right]$
$\Rightarrow \frac{1}{1+\tan ^2 \theta}\left[\begin{array}{cc}1-\tan ^2 \theta & -2 \tan \theta \\ 2 \tan \theta & 1-\tan ^2 \theta\end{array}\right]=\left[\begin{array}{cc}a & -b \\ b & a\end{array}\right]$
$\Rightarrow \quad\left[\begin{array}{cc}\frac{1-\tan ^2 \theta}{1+\tan ^2 \theta} & \frac{2 \tan \theta}{1+\tan ^2 \theta} \\ \frac{2 \tan \theta}{1+\tan ^2 \theta} & \frac{1-\tan ^2 \theta}{1+\tan ^2 \theta}\end{array}\right]=\left[\begin{array}{cc}a & -b \\ b & a\end{array}\right]$
$\Rightarrow\left[\begin{array}{cc}\cos 2 \theta & -\sin 2 \theta \\ \sin 2 \theta & \cos 2 \theta\end{array}\right]=\left[\begin{array}{cc}a & -b \\ b & a\end{array}\right]$
$\Rightarrow \quad a=\cos 2 \theta, b=\sin 2 \theta$

</details>

---

### Q3. BITSAT 2022

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 1 & 1\end{array}\right]$ and $10 B=\left[\begin{array}{ccc}4 & 2 & 2 \\ -5 & 0 & \alpha \\ 1 & -2 & 3\end{array}\right]$
If $B$ is the inverse of $A$, then the value of $\alpha$ is

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** $-4$
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

$A=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 1 & 1\end{array}\right]$
$\therefore|A|=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 1 & 1\end{array}\right]$
$=1(1+3)+1(2+3)+1(2-1)=4+5+1=10$
$\Rightarrow \operatorname{Adj} A=\left[\begin{array}{ccc}4 & -5 & 1 \\ 2 & 0 & -2 \\ 2 & 5 & 3\end{array}\right]^T=\left[\begin{array}{ccc}4 & 2 & 2 \\ -5 & 0 & 5 \\ 1 & -2 & 3\end{array}\right]$
$\Rightarrow \quad B=A^{-1}=\frac{1}{10}\left[\begin{array}{ccc}4 & 2 & 2 \\ -5 & 0 & 5 \\ 1 & -2 & 3\end{array}\right]\left[\because A^{-1}=\frac{1}{|A|} \operatorname{Adj} A\right]$
$\Rightarrow 10 B=\left[\begin{array}{ccc}4 & 2 & 2 \\ -5 & 0 & 5 \\ 1 & -2 & 3\end{array}\right]$
Hence, $\alpha=5$

</details>

---

### Q4. BITSAT 2019

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is an <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> non- singular matrix, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>A</mi><mo>'</mo></msup><mo>=</mo><msup><mi>A</mi><mo>'</mo></msup><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mo>'</mo></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><msup><mi>B</mi><mo>'</mo></msup></math> equals to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msup><mi>B</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>'</mo></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>+</mo><mi>B</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>A</mi><mo>'</mo></msup><mo>=</mo><msup><mi>A</mi><mo>'</mo></msup><mi>A</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mo>'</mo></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><msup><mi>B</mi><mo>'</mo></msup><mo>=</mo><mfenced><mrow><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mo>'</mo></msup></mrow></mfenced><msup><mfenced><mrow><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mo>'</mo></msup></mrow></mfenced><mo>'</mo></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mo>'</mo></msup></mrow></mfenced><mfenced open="[" close="]"><mrow><msup><mfenced><msup><mi>A</mi><mo>'</mo></msup></mfenced><mo>'</mo></msup><msup><mfenced><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>'</mo></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mo>'</mo></msup></mrow></mfenced><mfenced open="[" close="]"><mrow><mi>A</mi><msup><mfenced><msup><mi>A</mi><mo>'</mo></msup></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mo>&#160;</mo><msup><mfenced><msup><mi>A</mi><mo>'</mo></msup></mfenced><mo>'</mo></msup><mo>=</mo><mi>A</mi><mo>,</mo><msup><mfenced><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>'</mo></msup><mo>=</mo><msup><mfenced><msup><mi>A</mi><mo>'</mo></msup></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msup><mi>A</mi><mo>'</mo></msup><mi>A</mi></mrow></mfenced><msup><mfenced><msup><mi>A</mi><mo>'</mo></msup></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close=""><mrow><mi>A</mi><msup><mi>A</mi><mo>'</mo></msup><msup><mfenced><msup><mi>A</mi><mo>'</mo></msup></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi></mrow></mfenced><msup><mfenced><mrow><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>A</mi></mrow></mfenced><mo>'</mo></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>I</mi><mo>&#183;</mo><mi>I</mi><mo>=</mo><mi>I</mi></math></p>

</details>

---

