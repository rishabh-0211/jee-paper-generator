# JEE Advanced Physics - Rotational Motion

## Topic 5: Collisions in rotation

**Total Questions:** 1

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

<strong>Passage:</strong> A uniform circular disk of radius $0.2$ m and mass $1$ kg is pivoted at its top point $C$ such that it can rotate freely around $C$ in the $XY$ plane, as shown in the figure. Initially, when the disk is at rest, a particle of mass $20$ g, travelling along negative $x$ direction in the $XY$ plane with speed $100$ ms$^{-1}$, hits the circumference of the disk at a point $P$. After collision the particle moves along negative $y$ direction at a speed of $90$ ms$^{-1}$.
[Given: the acceleration due to gravity $(g) = -10\hat{j}$ ms$^{-2}$]
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p2_english__q35_d1.png" />

<strong>Question:</strong> Amount of energy loss (in J) in the collision is:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17.47**

**Detailed Solution:**

Let the center of the uniform circular disk be the origin $O(0,0)$. The disk is pivoted at its top point $C(0, R)$.

Radius of disk $R = 0.2$ m, Mass $M = 1$ kg.
Mass of particle $m = 20$ g = $0.02$ kg.
Initial velocity of particle $\vec{v}_i = -100\hat{i}$ ms$^{-1}$.
Final velocity of particle $\vec{v}_f = -90\hat{j}$ ms$^{-1}$.

The particle hits the disk at point $P$. From the figure, the line $OP$ makes an angle of $45^{\circ}$ with the negative y-axis.
Coordinates of $P$ with respect to $O$ are $(R\sin 45^{\circ}, -R\cos 45^{\circ})$.
Position vector of $P$ with respect to the pivot $C$ is:
$\vec{r}_{P/C} = (R\sin 45^{\circ} - 0)\hat{i} + (-R\cos 45^{\circ} - R)\hat{j} = \dfrac{R}{\sqrt{2}}\hat{i} - R\left(1 + \dfrac{1}{\sqrt{2}}\right)\hat{j}$

Angular momentum is conserved about the pivot $C$ during the collision.
Initial angular momentum of the system about $C$ is only due to the particle:
$\vec{L}_i = \vec{r}_{P/C} \times (m\vec{v}_i) = \left[ \dfrac{R}{\sqrt{2}}\hat{i} - R\left(1 + \dfrac{1}{\sqrt{2}}\right)\hat{j} \right] \times (-100m\hat{i})$
$\vec{L}_i = -100mR\left(1 + \dfrac{1}{\sqrt{2}}\right)(\hat{j} \times \hat{i}) = -100mR\left(1 + \dfrac{1}{\sqrt{2}}\right)\hat{k}$
Substituting $m = 0.02$ kg and $R = 0.2$ m:
$\vec{L}_i = -100(0.02)(0.2)\left(1 + \dfrac{1}{\sqrt{2}}\right)\hat{k} = -0.4\left(1 + \dfrac{1}{\sqrt{2}}\right)\hat{k} = -\left(0.4 + 0.2\sqrt{2}\right)\hat{k}$ kg m$^2$s$^{-1}$

Final angular momentum of the particle about $C$:
$\vec{L}_{f,p} = \vec{r}_{P/C} \times (m\vec{v}_f) = \left[ \dfrac{R}{\sqrt{2}}\hat{i} - R\left(1 + \dfrac{1}{\sqrt{2}}\right)\hat{j} \right] \times (-90m\hat{j})$
$\vec{L}_{f,p} = -90m\dfrac{R}{\sqrt{2}}(\hat{i} \times \hat{j}) = -\dfrac{90mR}{\sqrt{2}}\hat{k}$
$\vec{L}_{f,p} = -\dfrac{90(0.02)(0.2)}{\sqrt{2}}\hat{k} = -\dfrac{0.36}{\sqrt{2}}\hat{k} = -0.18\sqrt{2}\hat{k}$ kg m$^2$s$^{-1}$

Let $\omega$ be the angular velocity of the disk after collision. Its moment of inertia about $C$ is:
$I_C = I_{cm} + MR^2 = \dfrac{1}{2}MR^2 + MR^2 = \dfrac{3}{2}MR^2 = \dfrac{3}{2}(1)(0.2)^2 = 0.06$ kg m$^2$

Final angular momentum of the disk is $\vec{L}_{f,d} = I_C\omega\hat{k} = 0.06\omega\hat{k}$

By conservation of angular momentum about $C$:
$\vec{L}_i = \vec{L}_{f,p} + \vec{L}_{f,d}$
$-(0.4 + 0.2\sqrt{2}) = -0.18\sqrt{2} + 0.06\omega$
$0.06\omega = -0.4 - 0.02\sqrt{2} \Rightarrow \omega = -\dfrac{40 + 2\sqrt{2}}{6} = -\dfrac{20 + \sqrt{2}}{3}$ rad s$^{-1}$

Initial kinetic energy of the system:
$E_i = \dfrac{1}{2}mv_i^2 = \dfrac{1}{2}(0.02)(100)^2 = 100$ J

Final kinetic energy of the system:
$E_f = \dfrac{1}{2}mv_f^2 + \dfrac{1}{2}I_C\omega^2 = \dfrac{1}{2}(0.02)(90)^2 + \dfrac{1}{2}(0.06)\left(\dfrac{20 + \sqrt{2}}{3}\right)^2$
$E_f = 81 + 0.03\left(\dfrac{400 + 2 + 40\sqrt{2}}{9}\right) = 81 + \dfrac{402 + 40\sqrt{2}}{300} = 81 + \dfrac{201 + 20\sqrt{2}}{150}$

Amount of energy loss:
$\Delta E = E_i - E_f = 100 - \left(81 + \dfrac{201 + 20\sqrt{2}}{150}\right) = 19 - \dfrac{201 + 20\sqrt{2}}{150}$
$\Delta E = \dfrac{2850 - 201 - 20\sqrt{2}}{150} = \dfrac{2649 - 20\sqrt{2}}{150}$
Using $\sqrt{2} \approx 1.414$,
$\Delta E \approx \dfrac{2649 - 28.28}{150} = \dfrac{2620.72}{150} \approx 17.47$ J

</details>

---

