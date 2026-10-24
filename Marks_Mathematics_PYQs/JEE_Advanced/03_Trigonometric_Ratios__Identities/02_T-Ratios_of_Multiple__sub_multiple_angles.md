# JEE Advanced Mathematics - Trigonometric Ratios & Identities

## Topic 2: T-Ratios of Multiple & sub multiple angles

**Total Questions:** 1

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `numerical` | *Level:* `3`

Let

$\alpha = \left(1 - 2\cos\left(\dfrac{\pi}{11}\right)\right)\left(1 - 2\cos\left(\dfrac{3\pi}{11}\right)\right)\left(1 - 2\cos\left(\dfrac{9\pi}{11}\right)\right)\left(1 - 2\cos\left(\dfrac{27\pi}{11}\right)\right)\left(1 - 2\cos\left(\dfrac{81\pi}{11}\right)\right)$.

Then the value of $5 - \alpha^2$ is _____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

Let the given expression be $\alpha$. First, we simplify the angles in the product.

$\cos\left(\dfrac{27\pi}{11}\right) = \cos\left(2\pi + \dfrac{5\pi}{11}\right) = \cos\left(\dfrac{5\pi}{11}\right)$

$\cos\left(\dfrac{81\pi}{11}\right) = \cos\left(7\pi + \dfrac{4\pi}{11}\right) = -\cos\left(\dfrac{4\pi}{11}\right) = \cos\left(\pi - \dfrac{4\pi}{11}\right) = \cos\left(\dfrac{7\pi}{11}\right)$

Thus, the angles are $\dfrac{\pi}{11}, \dfrac{3\pi}{11}, \dfrac{5\pi}{11}, \dfrac{7\pi}{11}, \dfrac{9\pi}{11}$, which can be written as $\theta_k = \dfrac{(2k-1)\pi}{11}$ for $k = 1, 2, 3, 4, 5$.

The expression becomes:
$\alpha = \prod_{k=1}^{5} \left(1 - 2\cos\theta_k\right)$

Using the trigonometric identity $1 - 2\cos\theta = 1 - 2(2\cos^2(\theta/2) - 1) = 3 - 4\cos^2(\theta/2)$.
Multiplying and dividing by $\cos(\theta/2)$, we get:
$1 - 2\cos\theta = \dfrac{3\cos(\theta/2) - 4\cos^3(\theta/2)}{\cos(\theta/2)} = -\dfrac{\cos(3\theta/2)}{\cos(\theta/2)}$

Applying this identity to the product:
$\alpha = \prod_{k=1}^{5} \left( -\dfrac{\cos(3\theta_k/2)}{\cos(\theta_k/2)} \right) = (-1)^5 \dfrac{\prod_{k=1}^{5} \cos(3\theta_k/2)}{\prod_{k=1}^{5} \cos(\theta_k/2)}$

The terms in the denominator are $\cos\left(\dfrac{\pi}{22}\right), \cos\left(\dfrac{3\pi}{22}\right), \cos\left(\dfrac{5\pi}{22}\right), \cos\left(\dfrac{7\pi}{22}\right), \cos\left(\dfrac{9\pi}{22}\right)$.

The terms in the numerator are $\cos\left(\dfrac{3\pi}{22}\right), \cos\left(\dfrac{9\pi}{22}\right), \cos\left(\dfrac{15\pi}{22}\right), \cos\left(\dfrac{21\pi}{22}\right), \cos\left(\dfrac{27\pi}{22}\right)$.

We can simplify the larger angles in the numerator:
$\cos\left(\dfrac{15\pi}{22}\right) = \cos\left(\pi - \dfrac{7\pi}{22}\right) = -\cos\left(\dfrac{7\pi}{22}\right)$

$\cos\left(\dfrac{21\pi}{22}\right) = \cos\left(\pi - \dfrac{\pi}{22}\right) = -\cos\left(\dfrac{\pi}{22}\right)$

$\cos\left(\dfrac{27\pi}{22}\right) = \cos\left(\pi + \dfrac{5\pi}{22}\right) = -\cos\left(\dfrac{5\pi}{22}\right)$

Substituting these back into the numerator product:
$\prod_{k=1}^{5} \cos(3\theta_k/2) = \cos\left(\dfrac{3\pi}{22}\right) \cos\left(\dfrac{9\pi}{22}\right) \left(-\cos\left(\dfrac{7\pi}{22}\right)\right) \left(-\cos\left(\dfrac{\pi}{22}\right)\right) \left(-\cos\left(\dfrac{5\pi}{22}\right)\right)$

$\prod_{k=1}^{5} \cos(3\theta_k/2) = - \left[ \cos\left(\dfrac{\pi}{22}\right) \cos\left(\dfrac{3\pi}{22}\right) \cos\left(\dfrac{5\pi}{22}\right) \cos\left(\dfrac{7\pi}{22}\right) \cos\left(\dfrac{9\pi}{22}\right) \right]$

Notice that the term in the brackets is exactly the denominator product. Therefore, the ratio of the numerator product to the denominator product is $-1$.

$\alpha = (-1)^5 \times (-1) = (-1) \times (-1) = 1$

We need to find the value of $5 - \alpha^2$:
$5 - (1)^2 = 5 - 1 = 4$

Answer: $4$

</details>

---

