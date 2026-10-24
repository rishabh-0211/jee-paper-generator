# MHT CET Mathematics - Definite Integration

## Topic 6: Definite as Limit of Sum

**Total Questions:** 1

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\lim\limits_{n \to \infty} \left(\dfrac{n}{(n+1)\sqrt{2n+1}} + \dfrac{n}{(n+2)\sqrt{2(2n+2)}} + \dfrac{n}{(n+3)\sqrt{3(2n+3)}} + \cdots + \dfrac{1}{2n\sqrt{3}}\right)$ is:

**Options:**

- **(A)** $\pi/3$
- **(B)** $\pi/2$
- **(C)** $\pi/4$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\pi/3$**

**Detailed Solution:**

The given limit can be written as the sum of a series:

$L = \lim\limits_{n \to \infty} \sum\limits_{r=1}^{n} \dfrac{n}{(n+r)\sqrt{r(2n+r)}}$

To convert this into a definite integral, we divide the numerator and the denominator by $n^2$:

$L = \lim\limits_{n \to \infty} \sum\limits_{r=1}^{n} \dfrac{1}{n} \dfrac{1}{\left(1 + \dfrac{r}{n}\right)\sqrt{\dfrac{r}{n}\left(2 + \dfrac{r}{n}\right)}}$

This is a Riemann sum. By substituting $\dfrac{r}{n} = x$ and $\dfrac{1}{n} = dx$, the limit as $n \to \infty$ becomes the definite integral from $0$ to $1$:

$L = \int_{0}^{1} \dfrac{dx}{(1+x)\sqrt{x(2+x)}}$

$L = \int_{0}^{1} \dfrac{dx}{(1+x)\sqrt{x^2+2x}}$

Completing the square inside the square root, we get:

$L = \int_{0}^{1} \dfrac{dx}{(1+x)\sqrt{(x+1)^2 - 1}}$

Let $x + 1 = t$, then $dx = dt$. The limits of integration change from $x = 0 \implies t = 1$ to $x = 1 \implies t = 2$.

$L = \int_{1}^{2} \dfrac{dt}{t\sqrt{t^2 - 1}}$

Using the standard integral formula $\int \dfrac{dt}{t\sqrt{t^2-1}} = \sec^{-1}(t)$, we get:

$L = \left[ \sec^{-1}(t) \right]_{1}^{2}$

$L = \sec^{-1}(2) - \sec^{-1}(1)$

$L = \dfrac{\pi}{3} - 0 = \dfrac{\pi}{3}$

Answer: $\pi/3$

</details>

---

