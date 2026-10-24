# JEE Advanced Mathematics - Definite Integration

## Topic 8: Miscellaneous

**Total Questions:** 5

---

### Q1. JEE Advanced 2011 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

$$
\text { Match the statements given in Column I with the values given in Column II. }
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/whLuoe5en1AhyDekxTeAe0GHJFttO-ylB8P6jVIZtEg.original.fullsize.png">

**Options:**

- **(A)** (A) q, (B) p, (C) s, (D) s
- **(B)** (A) p, (B) p, (C) r, (D) q
- **(C)** (A) q, (B) r, (C) s, (D) q
- **(D)** (A) p, (B) s, (C) r, (D) s

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (A) q, (B) p, (C) s, (D) s**

**Detailed Solution:**

(A) $\therefore|\mathbf{a}|=\sqrt{1+3}=2$ $|\mathbf{b}|=\sqrt{1+3}=2$ $|\mathbf{c}|=\sqrt{12}=2 \sqrt{3}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/RGdCdtVHJH1U8RZNrjguZqUUsjiCKu2UqCzCxQh8vWA.original.fullsize.png">

Using cosine law,
$$
\begin{aligned}
\cos C & =\frac{|\mathbf{a}|^2+|\mathbf{b}|^2-|\mathbf{c}|^2}{2|\mathbf{a}||\mathbf{b}|} \\
& =\frac{4+4-12}{2 \times 2 \times 2}=\frac{-4}{8}=\frac{-1}{2} \\
\Rightarrow \quad \angle C & =120^{\circ}=\frac{2 \pi}{3}
\end{aligned}
$$
(B)
$$
\begin{aligned}
& \int_a^b f(x) d x-3\left(\frac{x^2}{2}\right)_a^b=\left(a^2-b^2\right) \\
& \Rightarrow \int_a^b f(x) d x-\frac{3}{2}\left(b^2-a^2\right)=\left(a^2-b^2\right) \\
& \Rightarrow \int_a^b f(x) d x=\left(a^2-b^2\right)+\frac{3}{2}\left(b^2-a^2\right) \\
& =\frac{b^2-a^2}{2} \\
& \Rightarrow \int_a^b f(x) d x=\frac{b^2-a^2}{2} \\
&
\end{aligned}
$$

$$
f(x)=x \Rightarrow f\left(\frac{\pi}{6}\right)=\frac{\pi}{6}
$$
(C)
$$
\begin{aligned}
& \frac{\pi^2}{\log _e 3} \int_{7 / 6}^{5 / 6} \sec (\pi x) d x \\
& \Rightarrow \frac{\pi^2}{\log _e 3}\left\{\frac{\log |\sec \pi x+\tan \pi x|}{\pi}\right\}_{7 / 6}^{5 / 6} \\
& \Rightarrow \frac{\pi}{\log 3}\left\{\log \left|\sec \frac{5 \pi}{6}+\tan \frac{5 \pi}{6}\right|\right. \\
& \left.\quad-\log \left|\sec \frac{7 \pi}{6}+\tan \frac{7 \pi}{6}\right|\right\} \\
& \Rightarrow \frac{\pi}{\log 3}\left\{\log |\sqrt{3}|-\log \left|\frac{1}{\sqrt{3}}\right|\right\} \\
& \Rightarrow \frac{\pi}{\log 3}\{\log 3\}=\pi
\end{aligned}
$$

(D) $$
\begin{aligned}
& \left|\arg \frac{1}{(1-z)}\right|, \text { for }|z|=1 \\
& \Rightarrow\left|\arg (1-z)^{-1}\right| \\
& \Rightarrow|-\arg (1-z)| \Rightarrow|\arg (1-z)|
\end{aligned}
$$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/HSJMw5sIZCbFDqS37hzW91eRYY39SwiowxyUXRxah4U.original.fullsize.png">

From figure, $\arg (z-1)$ is maximum $=\pi$.

</details>

---

### Q2. JEE Advanced 2010 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

The value(s) of $\int_0^1 \frac{x^4(1-x)^4}{1+x^2} d x$ is (are)

**Options:**

- **(A)** $\frac{22}{7}-\pi$
- **(B)** $\frac{2}{105}$
- **(C)** 0
- **(D)** $\frac{71}{15}-\frac{3 \pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{22}{7}-\pi$**

**Detailed Solution:**

Let $I=\int_0^1 \frac{x^4(1-x)^4}{1+x^2} d x$
$$
\begin{aligned}
& =\int_0^1 \frac{\left(x^4-1\right)(1-x)^4+(1-x)^4}{\left(1+x^2\right)} d x \\
& =\int_0^1\left(x^2-1\right)(1-x)^4 d x \\
& +\int_0^1 \frac{\left(1+x^2-2 x\right)^2}{\left(1+x^2\right)} d x \\
& =\int_0^1\left\{\left(x^2-1\right)(1-x)^4+\left(1+x^2\right)-4 x\right. \\
& \left.+\frac{4 x^2}{\left(1+x^2\right)}\right\} d x \\
& =\int_0^1\left(\left(x^2-1\right)(1-x)^4+\left(1+x^2\right)-4 x\right. \\
& \left.+4-\frac{4}{1-x^2}\right) d x \\
& =\int_0^1\left(x^6-4 x^5+5 x^4-4 x^2\right. \\
& \left.+4-\frac{4}{1+x^2}\right) d x \\
& =\left[\frac{x^7}{7}-\frac{4 x^6}{6}+\frac{5 x^5}{5}\right. \\
&
\end{aligned}
$$

$$
\begin{aligned}
& \left.\quad-\frac{4 x^3}{3}+4 x-4 \tan ^{-1} x\right]_0^1 \\
= & \frac{1}{7}-\frac{4}{6}+\frac{5}{5}-\frac{4}{3}+4-4\left(\frac{\pi}{4}-0\right) \\
= & \frac{22}{7}-\pi
\end{aligned}
$$

</details>

---

### Q3. JEE Advanced 2009 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

$$
\text { Match the statements/expressions in Column I with the open intervals in Column II. }
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YSS353722UU7V-kPU9gVFl_hn_aTbFqHT6L7rH7xHFg.original.fullsize.png">

**Options:**

- **(A)** (A) p,q,t, (B) q,t, (C) r,s, (D) p,s
- **(B)** (A) p,q,s, (B) p,t, (C) p,q,r,t, (D) s
- **(C)** (A) p,q,s, (B) q,t, (C) r,s,t, (D) p,s
- **(D)** (A) p,q,t, (B) p,t, (C) p,q,r,t, (D) s

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (A) p,q,s, (B) p,t, (C) p,q,r,t, (D) s**

**Detailed Solution:**

(a) Given, $(x-3)^2 \cdot y^{\prime}+y=0$
$$
\begin{array}{rlrl}
\Rightarrow & \frac{d y}{d x} & =-\frac{y}{(x-3)^2} \\
\Rightarrow & & \int \frac{d y}{y} & =-\int \frac{d x}{(x-3)^3} \\
\Rightarrow & & \ln y & =\frac{1}{(x-3)}+\ln C \\
\Rightarrow & & y & =C e^{\frac{1}{x-3}}, C \neq 0
\end{array}
$$
$\therefore$ Domain of $y$ is $x \in R-\{3\}$
Aliter Given differential equation is homogeneous linear differential equation and has $x=3$ as a singular point, hence $x=3$ cannot be in domain of solution.
(b) Let $I=\int_1^5(x-1)(x-2)(x-3)(x-4)$ $(x-5) d x$
Let $x-3=t \Rightarrow d x=d t$
$\therefore I=\int_{-2}^2(t+2)(t+1) t(t-1)(t-2) d t$
$\because$ Integrand is an odd function.
$\therefore \quad I=0$
Aliter Let
$I=\int_1^5(x-1)(x-2)(x-3)(x-4)$
$(x-5) d x$
Using, $\int_a^b f(x) d x=\int_a^b f(a+b-x) d x$ $I=\int_1^5(5-x)(4-x)(3-x)(2-x)$ $(1-x) d x$
On adding Eqs. (i) and (ii) we get 2I $=0 \Rightarrow I=0$
(c) Let $f(x)=\cos ^2 x+\sin x$
$\Rightarrow f^{\prime}(x)=-2 \cos x \sin x+\cos x$ $=\cos x(1-2 \sin x)=0$ (say)
Sign scheme for first derivative
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/TLmS4uc2BFsrzGpUJe2DJ2LMHFf6yxl77ASJG4WjUWY.original.fullsize.png">

Points of local maxima are $\frac{\pi}{6}, \frac{5 \pi}{6}$.
Aliter $y=\cos ^2 x+\sin x$
$$
\Rightarrow \quad y=\frac{5}{4}-\left(\sin x-\frac{1}{2}\right)^2
$$
For $y$ to be maximum,
$$
\begin{aligned}
& \left(\sin x-\frac{1}{2}\right)^2=0 \Rightarrow \sin x=\frac{1}{2} \\
\Rightarrow \quad & x=n \pi+(-1)^n \frac{\pi}{6}, n \in I
\end{aligned}
$$
(d) Let $y=\tan ^{-1}(\sin x+\cos x)$
$$
\Rightarrow \quad \frac{d y}{d x}=\frac{\cos x-\sin x}{1+(\sin x+\cos x)^2}
$$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/QXVtSrn6Dj_MC10OOrVKBH-PujNlc9ggm4Rte2x4G1M.original.fullsize.png">

Clearly, by graph, $\cos x>\sin x$ is true for option(s).

</details>

---

### Q4. JEE Advanced 2008 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Consider the functions defined implicitly by the equation $y^3-3 y+x=0$ on various intervals in the real line. If $x \in(-\infty,-2) \cup(2, \infty)$, the equation implicitly defines a unique real valued differentiable function $y=f(x)$. If $x \in(-2,2)$, the equation implicitly defines a unique real valued differentiable function $y=g(x)$, satisfying $g(0)=0$.<strong>Question:</strong>
$\int_{-1}^1 g^{\prime}(x) d x$ is equal to

**Options:**

- **(A)** $2 g(-1)$
- **(B)** 0
- **(C)** $-2 g(1)$
- **(D)** $2 g(1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 g(1)$**

**Detailed Solution:**

Let $I=\int_{-1}^1 g^{\prime}(x) d x=[g(x)]_{-1}^1=g(1)-g(-1)$
Since, $\quad y^3-3 y+x=0$ and $\quad y=g(x)$
$$
\therefore(g(x))^3-3 g(x)+x=0
$$
[by Eq. (i)]
At $\quad x=1$,
$$
\begin{aligned}
(g(1))^3-3 g(1)+1 & =0 \\
\text { At } \quad x & =-1, \\
(g(-1))^3-3 g(-1)-1 & =0
\end{aligned}
$$
On adding Eqs. (i) and (ii), we get
$$
\begin{array}{rlrl} 
& & (g(1))^3+(g(-1))^3-3(g(1)+g(-1))=0 \\
\Rightarrow & & {[g(1)+g(-1)]\left[(g(1))^2+(g(-1))^2-g(1) g(-1)-3\right]=0} \\
\Rightarrow & g(1)+g(-1)=0 \\
\Rightarrow & g(1) & =-g(-1) \\
& \therefore & I & =g(1)-g(-1)=g(1)-(-g(1))=2 g(1)
\end{array}
$$

</details>

---

### Q5. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
Read the following passage and answer the questions.
For every function $f(x)$ which is twice differentiable, these will be good approximation of $\int_a^b f(x) d x \cong\left(\frac{b-a}{2}\right)\{f(a)+f(b)\}$. Now, if we take $c=\frac{a+b}{2}$, then using above again, we get $\int_a^b f(x) d x=\int_a^c f(x) d x+\int_c^b f(x) d x \cong \frac{b-a}{4}\{f(a)+f(b)+2 f(c)\}$ and so on.
We get approximation for value of $\int_a^b f(x) d x$.<strong>Question:</strong>
Good approximation of $\int_0^{\pi / 2} \sin x d x$, is

**Options:**

- **(A)** $\frac{\pi}{4}$
- **(B)** $\frac{\pi}{4}(\sqrt{2}+1)$
- **(C)** $\frac{\pi}{8}(\sqrt{2}+1)$
- **(D)** $\frac{\pi}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{8}(\sqrt{2}+1)$**

**Detailed Solution:**

$\int_0^{\pi / 2} \sin x d x=\frac{\frac{\pi}{2}-0}{4}\left(\sin 0+\sin \left(\frac{\pi}{2}\right)+2 \sin \left(\frac{0+\frac{\pi}{2}}{2}\right)\right)=\frac{\pi}{8}(1+\sqrt{2})$.

</details>

---

