# BITSAT Mathematics - Limits

## Topic 4: Exponential and logarithmic limits

**Total Questions:** 1

---

### Q1. BITSAT 2015

*Type:* `singleCorrect` | *Level:* `2`

$$\lim _{x \rightarrow \infty} \frac{\int_{0}^{2 x} x e^{x^{2}} d x}{e^{4 x^{2}}} \text { equals }$$

**Options:**

- **(A)** $\underline{0}$
- **(B)** $\infty$
- **(C)** 2
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2}$**

**Detailed Solution:**

Consider $\lim _{x \rightarrow \infty} \frac{\int_{0}^{2 x} x e^{x^{2}} d x}{e^{4 x^{2}}}$

$$

\begin{array}{l}

=\lim _{x \rightarrow \infty} \frac{2 \int_{0}^{2 x} x e^{x^{2}} d x}{2 e^{4 x^{2}}} \\

=\lim _{x \rightarrow \infty} \frac{2 \int_{0}^{2 x} e^{x^{2}} d\left(x^{2}\right)}{2 e^{4 x^{2}}} \\

=\lim _{x \rightarrow \infty} \frac{\left[e^{x^{2}}\right]_{0}^{2 x}}{e^{4 x^{2}}}=\lim _{x \rightarrow \infty} \frac{e^{4 x^{2}}-1}{2 e^{4 x^{2}}} \\

=\lim _{x \rightarrow \infty}\left(\frac{1}{2}-\frac{1}{2 e^{4 x^{2}}}\right)=\frac{1}{2}

\end{array}

$$

</details>

---

