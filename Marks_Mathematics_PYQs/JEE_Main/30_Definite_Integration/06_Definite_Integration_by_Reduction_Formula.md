# JEE Main Mathematics - Definite Integration

## Topic 6: Definite Integration by Reduction Formula

**Total Questions:** 1

---

### Q1. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of $k \in \mathrm{N}$ for which the integral $I_n=\int_0^1\left(1-x^k\right)^n d x, n \in \mathbb{N}$, satisfies $147 I_{20}=148 I_{21}$ is

**Options:**

- **(A)** 14
- **(B)** 8
- **(C)** 10
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7**

**Detailed Solution:**

$\begin{aligned} & I_n=\int_0^1\left(1-x^k\right)^n \cdot 1 d x \\ & I_n=\left(1-x^k\right)^n \cdot x-n k \int_0^1\left(1-x^k\right)^{n-1} \cdot x^{k-1} \cdot d x \\ & I_n=n k \int_0^1\left[\left(1-x^k\right)^n-\left(1-x^k\right)^{n-1}\right] d x \\ & I_n=n k I_n-n k I_n \\ & \frac{I_n}{I_{n-1}}=\frac{n k}{n k+1} \\ & \frac{I_{21}}{I_{20}}=\frac{21 k}{1+21 k} \\ & =\frac{147}{148} \Rightarrow k=7\end{aligned}$

</details>

---

