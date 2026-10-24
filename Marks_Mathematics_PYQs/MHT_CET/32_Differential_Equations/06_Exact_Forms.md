# MHT CET Mathematics - Differential Equations

## Topic 6: Exact Forms

**Total Questions:** 4

---

### Q1. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The particular solution of the differential equation $\frac{d y}{d x}=\frac{x+y+1}{x+y-1}$ when $\mathrm{x}=\frac{2}{3}$ and $\mathrm{y}=\frac{1}{3}$ is

**Options:**

- **(A)** $2 x+2 y-2=\log |x+y|$
- **(B)** $\mathrm{y}-\mathrm{x}+\frac{1}{3}=\log |\mathrm{x}+\mathrm{y}|$
- **(C)** $x+y-1=\log |x+y|$
- **(D)** $4 x-5 y-1=\log |x+y|$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{y}-\mathrm{x}+\frac{1}{3}=\log |\mathrm{x}+\mathrm{y}|$**

**Detailed Solution:**

$$
\frac{d y}{d x}=\frac{x+y+1}{x+y-1}
$$
Put $x+y=v \Rightarrow 1+\frac{d y}{d x}=\frac{d v}{d x}$
$$
\begin{aligned}
& \therefore \frac{d v}{d x}-1=\frac{v+1}{v-1} \Rightarrow \frac{d v}{d x}=\frac{v+1}{v-1}+1=\frac{2 v}{v-1} \\
& \therefore \int \frac{(v-1) d v}{2 v}=\int d x \\
& \therefore \int \frac{1}{2} d V-\int \frac{1}{2 v} d v=\int d x=\frac{v}{2}-\frac{1}{2} \log |v|=x+c \\
& \therefore \frac{x+y}{2}-\frac{1}{2} \log |x+y|=x+c
\end{aligned}
$$
We have $\mathrm{x}=\frac{2}{3}, \mathrm{y}=\frac{1}{3}$
$$
\begin{aligned}
& \therefore \frac{1}{2}-\frac{1}{2} \log |1|=\frac{2}{3}+c \Rightarrow c=\frac{1}{2}-\frac{2}{3}=\frac{-1}{6} \\
& \therefore \frac{x+y}{2}-\frac{1}{2} \log |x+y|=x-\frac{1}{6}
\end{aligned}
$$
$\begin{aligned} & \therefore \frac{x+y}{2}-\frac{1}{2} \log |x+y|=x-\frac{1}{6} \\ & \therefore(x+y)-\log |x+y|=2 x-\frac{2}{6} \Rightarrow y-x+\frac{1}{3}=\log |x+y|\end{aligned}$

</details>

---

### Q2. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $\left(y+x \cdot \frac{d y}{d x}\right) \cdot \sin x y=\cos x$
at $x=0$ is

**Options:**

- **(A)** $\sin x+\cos x y=1$
- **(B)** $\cos x-\sin x y=1$
- **(C)** $\sin x-\cos x y=1$
- **(D)** $\cos x+\sin x y=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin x+\cos x y=1$**

**Detailed Solution:**

We have $\left(y+x \frac{d y}{d x}\right) \sin x y=\cos x$
Put $x y=u \Rightarrow x \frac{d y}{d x}+y=\frac{d u}{d x}$
$\therefore\left(\frac{\mathrm{du}}{\mathrm{dx}}\right) \sin \mathrm{u}=\cos \mathrm{x}$
$\therefore \int \sin u d u=\int \cos x d x \Rightarrow-\cos u=\sin x+c \Rightarrow-\cos x y=\sin x+c$
When $x=0$, we get
$-\cos 0=0+c \Rightarrow c=-1$
$\therefore-\cos x y=\sin x-1 \Rightarrow \sin x+\cos x y=1$

</details>

---

### Q3. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation <math><mi>y</mi><mi></mi><mi>d</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi></mi><mi>d</mi><mi>y</mi><mo>=</mo><mi>x</mi><mi>y</mi><mi></mi><mi>d</mi><mi>x</mi></math> is ….

**Options:**

- **(A)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mi>x</mi><mo>=</mo><mi>y</mi><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>
- **(C)** <math><mi>x</mi><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>
- **(D)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>x</mi><mo>=</mo><mi>y</mi><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>**

**Detailed Solution:**

We have differential equation <math><mi>y</mi><mi>d</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>d</mi><mi>y</mi><mo>=</mo><mi>x</mi><mi>y</mi><mi>d</mi><mi>x</mi></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mi>y</mi><mi>d</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>d</mi><mi>y</mi></mrow><mrow><mi>x</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mi>d</mi><mi>x</mi></math>  
<math><mo>&#8658;</mo><mi>d</mi><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>d</mi><mi>x</mi></math>  
On integrating both sides, we get 
<math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mi>x</mi><mo>&#8658;</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>  
<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>y</mi><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>

</details>

---

### Q4. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of the differential equation <math><mi>x</mi><mi>d</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>y</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math>, when <math><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi> </mi><mi>y</mi><mo>=</mo><mn>1</mn></math> is

**Options:**

- **(A)** <math><mi>x</mi><mi>y</mi><mo>=</mo><mn>4</mn></math>
- **(B)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi><mo>=</mo><mn>4</mn></math>
- **(C)** <math><mi>x</mi><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn></math>
- **(D)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi><mo>=</mo><mn>4</mn></math>**

**Detailed Solution:**

<math><mi>x</mi><mi>d</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>y</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>d</mi><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> 
On integrating
 <math><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mrow></mrow></mrow></math> 
 <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>y</mi><mo>+</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow><mi> </mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>C</mi></mrow></mrow></math> 
 <math><mo>∴</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi><mo>=</mo><mi>C</mi></math> 
When  <math><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi> </mi><mi>y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>C</mi><mo>=</mo><mn>4</mn></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi></math>  Particular solution is  <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi><mo>=</mo><mn>4</mn></math>

</details>

---

