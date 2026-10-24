# MHT CET Physics - Work Power Energy

## Topic 3: Power

**Total Questions:** 6

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A body is moved along a straight line by a machine delivering constant power. The distance moved by the body in time $t$ is proportional to

**Options:**

- **(A)** $t^{1/2}$
- **(B)** $t^{3/4}$
- **(C)** $t^{3/2}$
- **(D)** $t^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $t^{3/2}$**

**Detailed Solution:**

Power $P = Fv = m \left(\dfrac{dv}{dt}\right) v$

Since power is constant, integrating both sides gives:

$m \int v \, dv = \int P \, dt$

$\dfrac{1}{2} m v^2 = Pt$

$v = \left(\dfrac{2P}{m}\right)^{1/2} t^{1/2}$

Since $v = \dfrac{dx}{dt}$, we have:

$\dfrac{dx}{dt} = \left(\dfrac{2P}{m}\right)^{1/2} t^{1/2}$

Integrating both sides with respect to time $t$ from $t=0$ to $t$:

$x = \int \left(\dfrac{2P}{m}\right)^{1/2} t^{1/2} \, dt$

$x = \left(\dfrac{2P}{m}\right)^{1/2} \dfrac{t^{3/2}}{3/2}$

Therefore, $x \propto t^{3/2}$

Answer: $t^{3/2}$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the force acting on a body is inversely proportional to its speed, the kinetic energy of the body is

**Options:**

- **(A)** constant
- **(B)** directly proportional to time
- **(C)** inversely proportional to time
- **(D)** directly proportional to square of time

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) directly proportional to time**

**Detailed Solution:**

Given that force is inversely proportional to speed:

$F \propto \dfrac{1}{v}$

$F = \dfrac{c}{v}$

Power $P = Fv = \left(\dfrac{c}{v}\right)v = c$

Since power is constant, the rate of change of kinetic energy is constant.

$P = \dfrac{dK}{dt} = c$

$dK = c \, dt$

Integrating both sides:

$K = ct + K_0$

Assuming the initial kinetic energy is zero, $K = ct$.

Therefore, the kinetic energy of the body is directly proportional to time.

Answer: directly proportional to time

</details>

---

### Q3. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A body of mass 1kg begins to move under the action of a time dependent force $\vec{F} = (t\hat{i} + 3t^2\hat{j})\ \text{N}$ where $\hat{i}$ and $\hat{j}$ are the unit vectors along x and y axis. The power developed by the above force at time $t = 2\ \text{s}$ will be (in watt)

**Options:**

- **(A)** $100$
- **(B)** $50$
- **(C)** $25$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $100$**

**Detailed Solution:**

Given $\vec{F} = t\hat{i} + 3t^2\hat{j}$ and $m = 1\ \text{kg}$.

Acceleration $\vec{a} = \dfrac{\vec{F}}{m} = t\hat{i} + 3t^2\hat{j}$

Velocity $\vec{v} = \int \vec{a} dt = \dfrac{t^2}{2}\hat{i} + t^3\hat{j}$ (since the body begins to move from rest, $\vec{v}(0) = 0$).

At $t = 2\ \text{s}$:

$\vec{F} = 2\hat{i} + 3(2)^2\hat{j} = 2\hat{i} + 12\hat{j}$

$\vec{v} = \dfrac{2^2}{2}\hat{i} + (2)^3\hat{j} = 2\hat{i} + 8\hat{j}$

Power $P = \vec{F} \cdot \vec{v} = (2\hat{i} + 12\hat{j}) \cdot (2\hat{i} + 8\hat{j})$

$P = (2 \times 2) + (12 \times 8) = 4 + 96 = 100\ \text{W}$

Answer: $100$

</details>

---

### Q4. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A body of mass 1 kg begins to move under the action of a time dependent force $\vec{F}=\left(t \hat{i}+2 t^2 \hat{j}\right) N$, where $\hat{i}$ and $\hat{j}$ are unit vectors along $x$ and $y$ axis. The power developed by above force at time $t=3$ second will be

**Options:**

- **(A)** $337.5 \mathrm{~W}$
- **(B)** $228.5 \mathrm{~W}$
- **(C)** $422.5 \mathrm{~W}$
- **(D)** $126.5 \mathrm{~W}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $337.5 \mathrm{~W}$**

**Detailed Solution:**

Given mass $m = 1$ kg and force $\vec{F} = t \hat{i} + 2t^2 \hat{j}$.

Acceleration of the body is given by Newton's second law:

$\vec{a} = \dfrac{\vec{F}}{m} = t \hat{i} + 2t^2 \hat{j}$

Since the body begins to move from rest, its velocity $\vec{v}$ at time $t$ is:

$\vec{v} = \int \vec{a} dt = \int (t \hat{i} + 2t^2 \hat{j}) dt = \dfrac{t^2}{2} \hat{i} + \dfrac{2t^3}{3} \hat{j}$

Power developed by the force is the dot product of force and velocity:

$P = \vec{F} \cdot \vec{v} = (t \hat{i} + 2t^2 \hat{j}) \cdot \left(\dfrac{t^2}{2} \hat{i} + \dfrac{2t^3}{3} \hat{j}\right)$

$P = \dfrac{t^3}{2} + \dfrac{4t^5}{3}$

Substituting $t = 3$ s:

$P = \dfrac{3^3}{2} + \dfrac{4(3^5)}{3} = \dfrac{27}{2} + \dfrac{4 \times 243}{3}$

$P = 13.5 + 4 \times 81 = 13.5 + 324 = 337.5 \mathrm{W}$

Answer: $337.5 \mathrm{~W}$

</details>

---

### Q5. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A body of mass 1 kg starts from rest and moves with uniform acceleration. In 2 seconds, its velocity is $10 \mathrm{~m} / \mathrm{s}$. The power exerted on the body at $t = 1 \mathrm{~s}$ is

**Options:**

- **(A)** 20 W
- **(B)** 25 W
- **(C)** 50 W
- **(D)** 100 W

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 25 W**

**Detailed Solution:**

Given $m = 1 \text{ kg}$, $u = 0$, $v = 10 \text{ m/s}$ at $t = 2 \text{ s}$.

Using the equation of motion $v = u + at$:

$10 = 0 + a(2)$

$a = 5 \text{ m/s}^2$

The force acting on the body is:

$F = ma = 1 \times 5 = 5 \text{ N}$

The velocity of the body at $t = 1 \text{ s}$ is:

$v' = u + at = 0 + 5(1) = 5 \text{ m/s}$

The power exerted on the body at $t = 1 \text{ s}$ is:

$P = Fv' = 5 \times 5 = 25 \text{ W}$

Answer: 25 W

</details>

---

### Q6. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A car of mass ' $m$ ' moving with velocity ' $u$ ' on a straight road in a straight line, doubles its velocity in time $t$. the power delivered by the engine of a car for doubling the velocity is

**Options:**

- **(A)** $\frac{3 \mathrm{mu}^2}{2 \mathrm{t}}$
- **(B)** $\frac{\mathrm{mu}^2}{2 \mathrm{t}}$
- **(C)** $\frac{2 \mathrm{mu}^2}{\mathrm{t}}$
- **(D)** $\frac{3 \mathrm{mu}^2}{\mathrm{t}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \mathrm{mu}^2}{2 \mathrm{t}}$**

**Detailed Solution:**

Initial kinetic energy $\mathrm{k}_1=\frac{1}{2} \mathrm{mu}^2$
Final kinetic energy $\mathrm{k}_2=\frac{1}{2} \mathrm{mu}_2^2=\frac{1}{2} \mathrm{~m}(2 \mathrm{u})^2=\frac{1}{2}\left(4 \mathrm{mu}^2\right)$
$$
\therefore \mathrm{k}_2-\mathrm{k}_1=\frac{3}{2} \mathrm{mu}^2
$$
Change in K.E. is work done
Power, $\mathrm{P}=\frac{\text { workdone }}{\mathrm{t}}=\frac{3 \mathrm{mu}^2}{2 \mathrm{t}}$

</details>

---

