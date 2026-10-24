# BITSAT Mathematics - Continuity and Differentiability

## Topic 3: Both Continuity and Differentiability

**Total Questions:** 1

---

### Q1. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\left\{\begin{array}{cc}\frac{x^2 \log (\cos x)}{\log (1+x)}, & x \neq 0 \\ 0, & x=0\end{array}\right.$, then at $x=0, f(x)$ is

**Options:**

- **(A)** not continuous
- **(B)** continuous but not differentiable
- **(C)** differentiable
- **(D)** not continuous, but differentiable

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) differentiable**

**Detailed Solution:**

$\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0} \frac{x^2 \log (\cos x)}{\log (1+x)}$
$=\lim _{x \rightarrow 0}-\frac{x \cdot \log (\cos x)}{\frac{\log (1+x)}{x}}$
$=\lim _{x \rightarrow 0} x \cdot \log (\cos x)=0 \cdot \log 1=0$
$\because \lim _{x \rightarrow 0} f(x)=f(0)$
$\therefore f(x)$ is continuous at $x=0$
Now, $\lim _{x \rightarrow 0} \frac{f(x+h)-f(x)}{h}$
$\lim _{h \rightarrow 0} \frac{f(h)-f(0)}{h}=\lim _{h \rightarrow 0} \frac{h^2 \log \cos h-0}{\log (1+h)}$
$\lim _{h \rightarrow 0} \frac{h^2 \log (\cos h)}{1}=0$
$\therefore f(x)$ is differentiable at $x=0$

</details>

---

