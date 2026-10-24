# BITSAT Mathematics - Application of Derivatives

## Topic 2: Rate Measure Error and Approximation

**Total Questions:** 6

---

### Q1. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

The maximum volume (in cu. units) of the cylinder which can be inscribed in a sphere of radius 12 units is

**Options:**

- **(A)** $384 \sqrt{3} \pi$
- **(B)** $768 \sqrt{3} \pi$
- **(C)** $\frac{768 \pi}{\sqrt{3}}$
- **(D)** $\frac{1152 \pi}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $768 \sqrt{3} \pi$**

**Detailed Solution:**

$12^2=r^2+\left(\frac{h}{2}\right)^2 \Rightarrow V=\pi r^2 h$
$\Rightarrow \quad V=\pi\left(144-\frac{h^2}{4}\right) h$
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/iz6kZkvCfLIqhDLfZ-07Sf825wujqkWx95TpgxB0YRk.original.fullsize.png"/>
$\Rightarrow \quad V=144 \pi h-\frac{\pi}{4} h^3 \Rightarrow \frac{d V}{d h}=144 \pi-\frac{3 \pi}{4} h^2$
$\Rightarrow \frac{d V}{d h}=0 \Rightarrow 144 \pi=\frac{3 \pi}{4} h^2$
$\Rightarrow \quad h^2=48 \times 4 \Rightarrow h=8 \sqrt{3}$
$\therefore \quad 12^2=r^2+48 \Rightarrow r^2=96$
Volume $=\pi r^2 h=\pi \times 96 \times 8 \sqrt{3}=768 \sqrt{3} \pi \mathrm{~cm}^3$.

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

The population $p(t)$ at time $t$ of a certain mouse species satisfies the differential equation $\frac{d p(t)}{d t}=0.5 \mathrm{p}(\mathrm{t})-450$. If $p(0)=850$, then the time at which the population becomes zero is :

**Options:**

- **(A)** $2 \ln 18$
- **(B)** $\ln 9$
- **(C)** $\frac{1}{2} \ln 18$
- **(D)** $\ln 18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \ln 18$**

**Detailed Solution:**

Given differential equation is
$\frac{d p(t)}{d t}=0.5 p(t)-450$
$\Rightarrow \frac{d p(t)}{d t}=\frac{1}{2} p(t)-450$
$\Rightarrow \quad \frac{d p(t)}{d t}=\frac{p(t)-900}{2}$
$\Rightarrow \quad 2 \frac{d p(t)}{d t}=-[900-p(t)]$
$\Rightarrow \quad 2 \frac{d p(t)}{900-p(t)}=-d t$
Integrate both the side, we get :
$-2 \int \frac{d p(t)}{900-p(t)}=\int d t$
Let $900-p(t)=u \Rightarrow-d p(t)=d u$
$\therefore \quad$ We have; $2 \int \frac{d u}{u}=\int d t \Rightarrow 2 \ln u=t+c$
$\Rightarrow \quad 2 \ln [900-p(t)]=t+c$ when $t=0, p(0)=850$
$2 \ln (50)=c \quad \Rightarrow 2\left[\ln \left(\frac{900-p(t)}{50}\right)\right]=t$
$\Rightarrow \quad 900-p(t)=50 e^{\frac{t}{2}}$
$\Rightarrow \quad p(t)=900-50 e^{\frac{t}{2}}$
let $p\left(t_1\right)=0$
$0=900-50 e^{\frac{t_1}{2}} \quad \therefore t_1=2 \ln 18$

</details>

---

### Q3. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

The altitude of a cone is 20 cm and its semivertical angle is $30^{\circ}$. If the semi-vertical angle is increasing at the rate of $2^{\circ}$ per second, then the radius of the base is increasing at the rate of

**Options:**

- **(A)** $30 \mathrm{~cm} / \mathrm{sec}$
- **(B)** $\frac{160}{3} \mathrm{~cm} / \mathrm{sec}$
- **(C)** $10 \mathrm{~cm} / \mathrm{sec}$
- **(D)** $160 \mathrm{~cm} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{160}{3} \mathrm{~cm} / \mathrm{sec}$**

**Detailed Solution:**

Let $\theta$ be the semi-vertical angle and $r$ be the radius of the cone at time $t$.
the radius of the cone at time $t$.
Then, $r=20 \tan \theta$
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/NE02Q4z9X8qvOISoepQbHctTBA4BIo362VuUkZhwL7s.original.fullsize.png"/>
$\Rightarrow \quad \frac{d r}{d t}=20 \sec ^2 \theta \frac{d \theta}{d t}$
$\Rightarrow \quad \frac{d r}{d t}=20 \sec ^2 30^{\circ} \times 2$
$\left[\because \theta=30^{\circ}\right.$ and $\left.\frac{d \theta}{d t}=2\right]$
$\Rightarrow \quad \frac{d r}{d t}=20 \times \frac{4}{3} \times 2 \mathrm{~cm} / \mathrm{s}=\frac{160}{3} \mathrm{~cm} / \mathrm{s}$

</details>

---

### Q4. BITSAT 2021

*Type:* `singleCorrect` | *Level:* `1`

If the radius of a sphere is measured as $9 \mathrm{~cm}$ with an error of $0.03 \mathrm{~cm}$, then find the approximating error in calculating its volume.

**Options:**

- **(A)** $2.46 \pi \mathrm{cm}^{3}$
- **(B)** $8.62 \pi \mathrm{cm}^{3}$
- **(C)** $9.72 \pi \mathrm{cm}^{3}$
- **(D)** $7.6 \pi \mathrm{cm}^{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $9.72 \pi \mathrm{cm}^{3}$**

**Detailed Solution:**

Let $r$ be the radius of the sphere and $\Delta r$ be the error in measuring the radius. Then, $r=9 \mathrm{~cm}$ and $\Delta r=0.03 \mathrm{~cm}$

Let $V$ be the volume of the sphere. Then,

$\begin{array}{l}

\mathrm{V}=\frac{4}{3} \pi r^{3} \\

\Rightarrow \frac{\mathrm{dV}}{\mathrm{dr}}=4 \pi r^{2} \\

\Rightarrow\left(\frac{\mathrm{dV}}{\mathrm{dr}}\right)_{r=9}=4 \pi \times 9^{2}=324 \pi

\end{array}$

Let $\Delta \mathrm{V}$ be the error in $\mathrm{V}$ due to error $\Delta \mathrm{r}$ in $r$.

Then,

$\begin{array}{l}

\Delta \mathrm{V}=\frac{\mathrm{dV}}{\mathrm{dr}} \Delta r \\

\Rightarrow \Delta \mathrm{V}=324 \pi \times 0.03=9.72 \pi \mathrm{cm}^{3}

\end{array}$

</details>

---

### Q5. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `1`

Let \(\mathrm{f}(\mathrm{x})=\) \(\left\{\begin{array}{l}a x^2+1, x > 1 \\ x+a, x \leq 1\end{array}\right.\). Then \(f(x)\) is derivable at \(x=1\), if

**Options:**

- **(A)** \(a=2\)
- **(B)** \(a=1\)
- **(C)** \(a=0\)
- **(D)** \(a=1 / 2\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) \(a=1 / 2\)**

**Detailed Solution:**

\(\begin{aligned}
& \operatorname{Lf}^{\prime}(1)=\lim _{h \rightarrow 0} \frac{f(1-h)-f(1)}{-h} \\
& =\lim _{h \rightarrow 0} \frac{(1-h+a)-(1+a)}{-h}=\lim _{h \rightarrow 0} \frac{-h}{-h}=1 \\
& \operatorname{Rf}^{\prime}(1)=\lim _{h \rightarrow 0} \frac{f(1+h)-f(1)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\left[a(1+h)^2+1\right]-(1+a)}{h} \\
& =\lim _{h \rightarrow 0}(a h+2 a)=2 a
\end{aligned}\)
Since f' (1) exists, \(\therefore L f^{\prime}(1)=R f^{\prime}(1) \Rightarrow a=1 / 2\)

</details>

---

### Q6. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `1`

If \(M(\alpha)=\left[\begin{array}{ccc}\cos \alpha & -\sin \alpha & 0 \\ \sin \alpha & \cos \alpha & 0 \\ 0 & 0 & 1\end{array}\right]\); \(M(\beta)=\left[\begin{array}{ccc}\cos \beta & 0 & \sin \beta \\ 0 & 1 & 0 \\ -\sin \beta & 0 & \cos \beta\end{array}\right]\) then \([M(\alpha) M(\beta)]^{-1}\) is equal to -

**Options:**

- **(A)** \(\mathrm{M}(\beta) \mathrm{M}(\alpha)\)
- **(B)** \(\mathrm{M}(-\alpha) \mathrm{M}(-\beta)\)
- **(C)** \(\mathrm{M}(-\beta) \mathrm{M}(-\alpha)\)
- **(D)** \(-\mathrm{M}(\beta) \mathrm{M}(\alpha)\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \(\mathrm{M}(-\beta) \mathrm{M}(-\alpha)\)**

**Detailed Solution:**

\(\begin{aligned}
& \left.[\mathrm{M}(\alpha) \mathrm{M}(\beta)]^{-1}=\mathrm{M}(\beta)^{-1} \mathrm{M}(\alpha)^{-1}\right] \\
& \operatorname{Now~M(\alpha )^{-1}}=\left[\begin{array}{ccc}
\cos \alpha & \sin \alpha & 0 \\
-\sin \alpha & \cos \alpha & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
\cos (-\alpha) & -\sin (-\alpha) & 0 \\
\sin (-\alpha) & \cos (-\alpha) & 0 \\
0 & 0 & 1
\end{array}\right]=\mathrm{M}(-\alpha) \\
& M(\beta)^{-1}=\left[\begin{array}{ccc}
\cos \beta & 0 & -\sin \beta \\
0 & 1 & 0 \\
\sin \beta & 0 & \cos \beta
\end{array}\right] \\
& =\left[\begin{array}{ccc}
\cos (-\beta) & 0 & \sin (-\beta) \\
0 & 1 & 0 \\
-\sin (-\beta) & 0 & \cos (-\beta)
\end{array}\right]=\mathrm{M}(-\beta) \\
& {[\mathrm{M}(\alpha) \mathrm{M}(\beta)]^{-1}=\mathrm{M}(-\beta) \mathrm{M}(-\alpha)} \\
&
\end{aligned}\)

</details>

---

