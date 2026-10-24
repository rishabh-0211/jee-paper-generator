# JEE Advanced Mathematics - Differentiation

## Topic 3: Higher order derivatives

**Total Questions:** 2

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Let $\mathbb{R}$ denote the set of all real numbers. Consider the polynomial function $f: \mathbb{R} \rightarrow \mathbb{R}$ defined by
$f(x) = \dfrac{d^{10}}{dx^{10}}\left((x^2 - 1)^{10}\right)$, for all $x \in \mathbb{R}$.
Here $\dfrac{d^{10}}{dx^{10}}\left((x^2 - 1)^{10}\right)$ is the 10th order derivative of the function $(x^2 - 1)^{10}$.
Then which of the following statements is (are) TRUE ?

**Options:**

- **(A)** The coefficient of $x^8$ in the polynomial $f(x)$ is $(-10)\left(\dfrac{18!}{8!}\right)$
- **(B)** The value of $f(1) + f(-1)$ is equal to $10!\, 2^{11}$
- **(C)** The degree of the polynomial $f(x)$ is $10$
- **(D)** The constant term of the polynomial $f(x)$ is $-\left(\dfrac{10!}{5!}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) The degree of the polynomial $f(x)$ is $10$**

**Detailed Solution:**

Given $f(x) = \dfrac{d^{10}}{dx^{10}}\left((x^2 - 1)^{10}\right)$.

Using the binomial expansion, we have:
$(x^2 - 1)^{10} = \sum_{k=0}^{10} (-1)^k \, ^{10}C_{k} x^{20-2k}$

Differentiating $10$ times with respect to $x$, we get:
$f(x) = \sum_{k=0}^{5} (-1)^k \, ^{10}C_{k} \dfrac{(20-2k)!}{(10-2k)!} x^{10-2k}$

For the coefficient of $x^8$, we set $10 - 2k = 8 \Rightarrow k = 1$.
The coefficient is $(-1)^1 \, ^{10}C_{1} \dfrac{18!}{8!} = -10 \left(\dfrac{18!}{8!}\right)$. Thus, statement (A) is true.

The highest power of $x$ in $f(x)$ corresponds to $k = 0$, which gives $x^{10}$ with a non-zero coefficient of $\dfrac{20!}{10!}$.
Therefore, the degree of the polynomial $f(x)$ is $10$. Thus, statement (C) is true.

For the constant term, we set $10 - 2k = 0 \Rightarrow k = 5$.
The constant term is $(-1)^5 \, ^{10}C_{5} \dfrac{10!}{0!} = -\dfrac{10!}{5!5!} 10! = -\left(\dfrac{10!}{5!}\right)^2$.
Thus, statement (D) is false.

To find $f(1)$ and $f(-1)$, we use the Leibniz rule for the $n$-th derivative of a product:
$f(x) = \dfrac{d^{10}}{dx^{10}}\left((x-1)^{10}(x+1)^{10}\right) = \sum_{r=0}^{10} \, ^{10}C_{r} \dfrac{d^{10-r}}{dx^{10-r}}\left((x-1)^{10}\right) \dfrac{d^r}{dx^r}\left((x+1)^{10}\right)$

Evaluating at $x = 1$, all terms in the sum are zero except when $r = 0$ (since $\dfrac{d^{10-r}}{dx^{10-r}}\left((x-1)^{10}\right)$ contains a factor of $(x-1)$ for $r > 0$).
$f(1) = \, ^{10}C_{0} (10!) (1+1)^{10} = 10! \, 2^{10}$

Evaluating at $x = -1$, all terms are zero except when $r = 10$.
$f(-1) = \, ^{10}C_{10} (-1-1)^{10} (10!) = 10! \, 2^{10}$

Adding these values gives:
$f(1) + f(-1) = 10! \, 2^{10} + 10! \, 2^{10} = 10! \, 2^{11}$
Thus, statement (B) is true.

Answer: The coefficient of $x^8$ in the polynomial $f(x)$ is $(-10)\left(\dfrac{18!}{8!}\right)$; The value of $f(1) + f(-1)$ is equal to $10!\, 2^{11}$; The degree of the polynomial $f(x)$ is $10$

</details>

---

### Q2. JEE Advanced 2007 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

$\frac{d^2 x}{d y^2}$ equals

**Options:**

- **(A)** $\left(\frac{d^2 y}{d x^2}\right)^{-1}$
- **(B)** $-\left(\frac{d^2 y}{d x^2}\right)^{-1}\left(\frac{d y}{d x}\right)^{-3}$
- **(C)** $\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-2}$
- **(D)** $-\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-3}$**

**Detailed Solution:**

Since,
$$
\begin{aligned}
\Rightarrow \quad \frac{d}{d y}\left(\frac{d x}{d y}\right) & =\frac{d}{d x}\left(\frac{d y}{d x}\right)^{-1} \frac{d x}{d y} \\
\frac{d^2 x}{d y^2} & =-\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-2}\left(\frac{d x}{d y}\right) \\
& =-\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d y}{d x}\right)^{-3}
\end{aligned}
$$

</details>

---

