# JEE Advanced Mathematics - Inverse Trigonometric Functions

## Topic 3: Converting one Inverse T function to other Inverse T

**Total Questions:** 2

---

### Q1. JEE Advanced 2011 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let $f(\theta)=\sin \left[\tan ^{-1}\left(\frac{\sin \theta}{\sqrt{\cos 2 \theta}}\right)\right]$, where $-\frac{\pi}{4} < \theta < \frac{\pi}{4}$. Then, the value of $\frac{d}{d(\tan \theta)}(f(\theta))$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

$f(\theta)=\sin \left(\tan ^{-1} \frac{\sin \theta}{\sqrt{\cos 2 \theta}}\right),-\frac{\pi}{4} < \theta < \frac{\pi}{4}$
Let $\tan ^{-1} \frac{\sin \theta}{\sqrt{\cos 2 \theta}}=\phi$
$$
\Rightarrow \quad \tan \phi=\frac{\sin \theta}{\sqrt{\cos 2 \theta}}
$$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/bbRBtOL8gHVb5FgMH9HblcPKawLYnY879QtTMljq-9M.original.fullsize.png">

$$
\begin{aligned}
\therefore \quad \sin \phi & =\frac{\sin \theta}{\sqrt{\sin ^2 \theta+\cos 2 \theta}} \\
& =\frac{\sin \theta}{\sqrt{1-\sin ^2 \theta}}=\frac{\sin \theta}{\cos \theta}=\tan \theta
\end{aligned}
$$

$$
\begin{array}{ll}
\therefore & f(\theta)=\sin \phi=\tan \theta \\
\Rightarrow & \frac{d f(\theta)}{d(\tan \theta)}=1
\end{array}
$$

</details>

---

### Q2. JEE Advanced 2008 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

If $0 < x < 1$, then $\sqrt{1+x^2}\left[\left\{x \cos \left(\cot ^{-1} x\right)+\sin \left(\cot ^{-1} x\right)\right\}^2-1\right]^{\frac{1}{2}}$ is equal to

**Options:**

- **(A)** $\frac{x}{\sqrt{1+x^2}}$
- **(B)** $x$
- **(C)** $x \sqrt{1+x^2}$
- **(D)** $\sqrt{1+x^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x \sqrt{1+x^2}$**

**Detailed Solution:**

We have, $0 < x < 1$
Let $\quad \cot ^{-1} x=\theta$
$\Rightarrow \quad \cot \theta=x$
$\therefore \quad \sin \theta=\frac{1}{\sqrt{1+x^2}}=\sin \left(\cot ^{-1} x\right)$
and $\quad \cos \theta=\frac{x}{\sqrt{1+x^2}}=\cos \left(\cot ^{-1} x\right)$
Now, $\sqrt{1+x^2}\left[\left\{x \cos \left(\cot ^{-1} x\right)+\sin \left(\cot ^{-1} x\right)\right\}^2-1\right]^{1 / 2}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/gdRdKnY4ku1SFC16FGAuw3rwedtFLoTtWorYa_mxRmU.original.fullsize.png">

$$
\text { Now, } \begin{aligned}
& \sqrt{1+x^2}\left[\left\{x \cos \left(\cot ^{-1} x\right)+\sin \left(\cot ^{-1} x\right)\right\}^2-1\right]^{1 / 2} \\
&=\sqrt{1+x^2}\left[\left\{x \frac{x}{\sqrt{1+x^2}}+\frac{1}{\sqrt{1+x^2}}\right\}^2-1\right]^{1 / 2} \\
&=\sqrt{1+x^2}\left[\left(\frac{1+x^2}{\sqrt{1+x^2}}\right)^2-1\right]^{1 / 2} \\
&=\sqrt{1+x^2}\left[1+x^2-1\right]^{1 / 2} \\
&=x \sqrt{1+x^2}
\end{aligned}
$$

</details>

---

