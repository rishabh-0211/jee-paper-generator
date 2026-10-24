# JEE Advanced Mathematics - Differentiation

## Topic 2: Differentiation of implicit functions

**Total Questions:** 2

---

### Q1. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Consider the function $f:(-\infty, \infty) \rightarrow(-\infty, \infty)$ defined by $f(x)=\frac{x^2-a x+1}{x^2+a x+1} ; 0 < a < 2$<strong>Question:</strong>
Which of the following is true ?

**Options:**

- **(A)** $(2+a)^2 f^{\prime \prime}(1)+(2-a)^2 f^{\prime \prime}(-1)=0$
- **(B)** $(2-a)^2 f^{\prime \prime}(1)-(2+a)^2 f^{\prime \prime}(-1)=0$
- **(C)** $f^{\prime}(1) f^{\prime}(-1)=(2-a)^2$
- **(D)** $f^{\prime}(1) f^{\prime}(-1)=-(2+a)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(2+a)^2 f^{\prime \prime}(1)+(2-a)^2 f^{\prime \prime}(-1)=0$**

**Detailed Solution:**

\because f(x)= & \frac{\left(x^2+a x+1\right)-2 a x}{x^2+a x+1}=1-\frac{2 a x}{x^2+a x+1} \\
\therefore \quad f^{\prime}(x) & =-\left[\frac{\left(x^2+a x+1\right) \cdot 2 a-2 a x(2 x+a)}{\left(x^2+a x+1\right)^2}\right] \\
& =-\left[\frac{-2 a x^2+2 a}{\left(x^2+a x+1\right)^2}\right]=2 a\left[\frac{\left(x^2-1\right)}{\left(x^2+a x+1\right)^2}\right]
\end{aligned}
$$

$$
\begin{aligned}
& \text { and } \begin{aligned}
f^{\prime \prime}(x) & =2 a\left[\frac{\left(x^2+a x+1\right)^2(2 x)-2\left(x^2-1\right)\left(x^2+a x+1\right)(2 x+a)}{\left(x^2+a x+1\right)^4}\right] \\
& =2 a\left[\frac{2 x\left(x^2+a x+1\right)-2\left(x^2-1\right)(2 x+a)}{\left(x^2+a x+1\right)^3}\right]
\end{aligned} \\
& \text { Now, } f^{\prime \prime}(1)=\frac{4 a(a+2)}{(a+2)^3}=\frac{4 a}{(a+2)^2}
\end{aligned}
$$
and $f(-1)=\frac{4 a(a-2)}{(2-a)^3}=-\frac{4 a}{(a-2)^2}$
$$
\therefore(2+a)^2 f^{\prime \prime}(1)+(2-a)^2 f^{\prime \prime}(-1)=4 a-4 a=0
$$

</details>

---

### Q2. JEE Advanced 2008 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Consider the functions defined implicitly by the equation $y^3-3 y+x=0$ on various intervals in the real line. If $x \in(-\infty,-2) \cup(2, \infty)$, the equation implicitly defines a unique real valued differentiable function $y=f(x)$. If $x \in(-2,2)$, the equation implicitly defines a unique real valued differentiable function $y=g(x)$, satisfying $g(0)=0$.<strong>Question:</strong>
If $f(-10 \sqrt{2})=2 \sqrt{2}$, then $f^{\prime \prime}(-10 \sqrt{2})$ is equal to

**Options:**

- **(A)** $\frac{4 \sqrt{2}}{7^3 \cdot 3^2}$
- **(B)** $-\frac{4 \sqrt{2}}{7^3 \cdot 3^2}$
- **(C)** $\frac{4 \sqrt{2}}{7^3 \cdot 3}$
- **(D)** $-\frac{4 \sqrt{2}}{7^3 \cdot 3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{4 \sqrt{2}}{7^3 \cdot 3^2}$**

**Detailed Solution:**

Given, $y^3-3 y+x=0 \Rightarrow 3 y^2 \frac{d y}{d x}-3 \frac{d y}{d x}+1=0$
$$
\Rightarrow \quad 3 y^2\left(\frac{d^2 y}{d x^2}\right)+6 y\left(\frac{d y}{d x}\right)^2-3 \frac{d^2 y}{d x^2}=0
$$
On substituting $x=-10 \sqrt{2}, y=2 \sqrt{2}$ in Eq. (i), we get
$$
3(2 \sqrt{2})^2 \cdot \frac{d y}{d x}-3 \cdot \frac{d y}{d x}+1=0 \Rightarrow \frac{d y}{d x}=\frac{-1}{21}
$$
Again on substituting $x=-10 \sqrt{2}, y=2 \sqrt{2}$ in Eq. (ii), we get
$$
\begin{aligned}
& 3(2 \sqrt{2})^2 \frac{d^2 y}{d x^2}+6(2 \sqrt{2}) \cdot\left(\frac{-1}{21}\right)^2-3 \cdot \frac{d^2 y}{d x^2}=0 \\
& \Rightarrow \quad 21 \cdot \frac{d^2 y}{d x^2}=-\frac{12 \sqrt{2}}{(21)^2} \Rightarrow \frac{d^2 y}{d x^2}=-\frac{12 \sqrt{2}}{(21)^3}=-\frac{4 \sqrt{2}}{7^3 \cdot 3^2}
\end{aligned}
$$

</details>

---

