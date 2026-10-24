# JEE Advanced Mathematics - Definite Integration

## Topic 4: Properties of Periodic Functions

**Total Questions:** 1

---

### Q1. JEE Advanced 2010 (Paper 1)

*Type:* `numerical` | *Level:* `3`

For any real number $x$, let $[x]$ denotes the largest integer less than or equal to $x$. Let $f$ be a real valued function defined on the interval $[-10,10]$ by $f(x)=\left\{\begin{array}{cc}x-[x] & \text { if }[x] \text { is odd } \\ 1+[x]-x & \text { if }[x] \text { is even }\end{array}\right.$.
Then the value of $\frac{\pi^2}{10} \int_{-10}^{10} f(x) \cos \pi x d x$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

Given, $f(x)=\left\{\begin{array}{cc}x-[x] & \text { if }[x] \text { is odd } \\ 1+[x]-x & \text { if }[x] \text { is even }\end{array}\right.$ $f(x)$ and $\cos \pi x$ both are periodic with period 2 and both are even.
$$
\begin{aligned}
\therefore \quad & \int_{-10}^{10} f(x) \cos \pi x d x \\
& =2 \int_0^{10} f(x) \cos \pi x d x
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/38fJZUbYKcCJA8fbhzEPVjPMjiAKOXHpLlVA3ITpe2w.original.fullsize.png">

$$
\begin{aligned}
& =10 \int_0^2 f(x) \cos \pi x d x \\
& \text { Now, } \quad \int_0^1 f(x) \cos \pi x d x \\
& =\int_0^1(1-x) \cos \pi x d x=-\int_0^1 u \cos \pi u d u \\
& \text { and } \int_1^2 f(x) \cos \pi x d x \\
& =\int_1^2(x-1) \cos \pi x d x=-\int_0^1 u \cos \pi u d u \\
& \therefore \quad \int_{-10}^{10} f(x) \cos \pi x d x \\
& =-20 \int_0^1 u \cos \pi u d u=\frac{40}{\pi^2} \\
& \Rightarrow \quad \frac{\pi^2}{10} \int_{-10}^{10} f(x) \cos \pi x d x=4
\end{aligned}
$$

</details>

---

