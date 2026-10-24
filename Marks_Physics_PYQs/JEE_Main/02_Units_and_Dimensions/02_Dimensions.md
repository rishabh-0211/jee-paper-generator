# JEE Main Physics - Units and Dimensions

## Topic 2: Dimensions

**Total Questions:** 131

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the equation $H = \dfrac{x^p \epsilon^q E^r}{t^s}$, where $H=$ magnetic field; $E=$ electric field, $\epsilon=$ permittivity, $x=$ distance, $t=$ time. The values of $p, q, r$ and $s$ respectively are:

**Options:**

- **(A)** $1, 1, 1, 1$
- **(B)** $-1, 1, 2, 1$
- **(C)** $1, -1, -2, 1$
- **(D)** $-1, -2, -2, 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1, 1, 1, 1$**

**Detailed Solution:**

The dimensional formulas for the given physical quantities are:

Magnetic field intensity $[H] = [M^0 L^{-1} T^0 A^1]$

Distance $[x] = [M^0 L^1 T^0 A^0]$

Permittivity $[\epsilon] = [M^{-1} L^{-3} T^4 A^2]$

Electric field $[E] = [M^1 L^1 T^{-3} A^{-1}]$

Time $[t] = [M^0 L^0 T^1 A^0]$

Given the equation $H = \dfrac{x^p \epsilon^q E^r}{t^s}$, we can write it in terms of dimensions as:

$[M^0 L^{-1} T^0 A^1] = [L]^p [M^{-1} L^{-3} T^4 A^2]^q [M L T^{-3} A^{-1}]^r [T]^{-s}$

Combining the powers of $M, L, T$, and $A$ on the right side:

$[M^0 L^{-1} T^0 A^1] = [M^{-q+r} L^{p-3q+r} T^{4q-3r-s} A^{2q-r}]$

Equating the powers of corresponding fundamental quantities from both sides:

For $M$: $0 = -q + r \implies q = r$

For $A$: $1 = 2q - r$

Substituting $r = q$ into the equation for $A$:

$1 = 2q - q \implies q = 1$

Since $q = r$, we get $r = 1$.

For $L$: $-1 = p - 3q + r$

Substituting $q = 1$ and $r = 1$:

$-1 = p - 3(1) + 1 \implies -1 = p - 2 \implies p = 1$

For $T$: $0 = 4q - 3r - s$

Substituting $q = 1$ and $r = 1$:

$0 = 4(1) - 3(1) - s \implies 0 = 1 - s \implies s = 1$

Thus, the values are $p = 1$, $q = 1$, $r = 1$, and $s = 1$.

Answer: $1, 1, 1, 1$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Match List - I with List - II.<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><th style="border: 1px solid black; padding: 5px;">List - I</th><th style="border: 1px solid black; padding: 5px;">List - II</th></tr><tr><td style="border: 1px solid black; padding: 5px;">A. Boltzmann constant</td><td style="border: 1px solid black; padding: 5px;">I. $[M^{-1}L^3T^{-2}]$</td></tr><tr><td style="border: 1px solid black; padding: 5px;">B. Stefan's constant</td><td style="border: 1px solid black; padding: 5px;">II. $[ML^2T^{-1}]$</td></tr><tr><td style="border: 1px solid black; padding: 5px;">C. Planck's constant</td><td style="border: 1px solid black; padding: 5px;">III. $[ML^2T^{-2}K^{-1}]$</td></tr><tr><td style="border: 1px solid black; padding: 5px;">D. Gravitational constant</td><td style="border: 1px solid black; padding: 5px;">IV. $[ML^0T^{-3}K^{-4}]$</td></tr></table>Choose the correct answer from the options given below :

**Options:**

- **(A)** A-I, B-II, C-III, D-IV
- **(B)** A-IV, B-III, C-II, D-I
- **(C)** A-III, B-IV, C-II, D-I
- **(D)** A-II, B-I, C-IV, D-III

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A-III, B-IV, C-II, D-I**

**Detailed Solution:**

Boltzmann constant $k$: $E = k T \Rightarrow [k] = \dfrac{[ML^2T^{-2}]}{[K]} = [ML^2T^{-2}K^{-1}]$

Stefan's constant $\sigma$: $\dfrac{E}{At} = \sigma T^4 \Rightarrow [\sigma] = \dfrac{[ML^2T^{-2}]}{[L^2][T][K^4]} = [ML^0T^{-3}K^{-4}]$

Planck's constant $h$: $E = h\nu \Rightarrow [h] = \dfrac{[ML^2T^{-2}]}{[T^{-1}]} = [ML^2T^{-1}]$

Gravitational constant $G$: $F = \dfrac{Gm_1m_2}{r^2} \Rightarrow [G] = \dfrac{[MLT^{-2}][L^2]}{[M^2]} = [M^{-1}L^3T^{-2}]$

Thus, A-III, B-IV, C-II, D-I.

Answer: A-III, B-IV, C-II, D-I

</details>

---

### Q3. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The potential energy of a particle changes with distance $x$ from a fixed origin as $V = \dfrac{A\sqrt{x}}{x + B}$, where $A$ and $B$ are constant with appropriate dimensions. The dimensions of $AB$ are _______.

**Options:**

- **(A)** $[M^1 L^{5/2} T^{-2}]$
- **(B)** $[M^{3/2} L^{5/2} T^{-2}]$
- **(C)** $[M^1 L^2 T^{-2}]$
- **(D)** $[M^1 L^{7/2} T^{-2}]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $[M^1 L^{7/2} T^{-2}]$**

**Detailed Solution:**

By the principle of dimensional homogeneity, quantities added or subtracted must have the same dimensions. In the denominator, $B$ is added to $x$ (distance).

$[B] = [x] = [L]$

The dimensions of potential energy $V$ are $[M^1 L^2 T^{-2}]$.

From the given equation $V = \dfrac{A\sqrt{x}}{x + B}$, we can write the dimensional formula as:

$[V] = \dfrac{[A][x]^{1/2}}{[x + B]}$

$[M^1 L^2 T^{-2}] = \dfrac{[A][L]^{1/2}}{[L]}$

$[M^1 L^2 T^{-2}] = [A][L]^{-1/2}$

$[A] = [M^1 L^2 T^{-2}][L]^{1/2} = [M^1 L^{5/2} T^{-2}]$

Now, the dimensions of $AB$ are:

$[AB] = [A][B] = [M^1 L^{5/2} T^{-2}][L] = [M^1 L^{7/2} T^{-2}]$

Answer: $[M^1 L^{7/2} T^{-2}]$

</details>

---

### Q4. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Match List-I with List-II.
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><th style="border: 1px solid black; padding: 5px;">List-I</th><th style="border: 1px solid black; padding: 5px;">List-II</th></tr><tr><td style="border: 1px solid black; padding: 5px;">A. Meter (L)</td><td style="border: 1px solid black; padding: 5px;">I. $\sqrt{\dfrac{hc}{G}}$</td></tr><tr><td style="border: 1px solid black; padding: 5px;">B. Second (S)</td><td style="border: 1px solid black; padding: 5px;">II. $\sqrt{\dfrac{Gh}{c^5}}$</td></tr><tr><td style="border: 1px solid black; padding: 5px;">C. Kilogram (M)</td><td style="border: 1px solid black; padding: 5px;">III. $\sqrt{\dfrac{K^2L^2c^3}{Gh}}$</td></tr><tr><td style="border: 1px solid black; padding: 5px;">D. Kelvin (K)</td><td style="border: 1px solid black; padding: 5px;">IV. $\sqrt{\dfrac{Gh}{c^3}}$</td></tr></table>
where $h$ (Planck's constant), $G$ (gravitational constant) and $c$ (speed of light in vacuum) as fundamental units.
Choose the correct answer from the options given below :

**Options:**

- **(A)** A-II, B-IV, C-I, D-III
- **(B)** A-IV, B-II, C-I, D-III
- **(C)** A-IV, B-I, C-II, D-III
- **(D)** A-III, B-I, C-II, D-IV

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A-IV, B-II, C-I, D-III**

**Detailed Solution:**

The dimensional formulas for the given fundamental constants are:
$[h] = M L^2 T^{-1}$
$[c] = L T^{-1}$
$[G] = M^{-1} L^3 T^{-2}$

Evaluating the dimensions of the expressions in List-II:

For I: $\sqrt{\dfrac{hc}{G}} = \sqrt{\dfrac{(M L^2 T^{-1})(L T^{-1})}{M^{-1} L^3 T^{-2}}} = \sqrt{M^2} = M$ (Kilogram).
Thus, C $\rightarrow$ I.

For II: $\sqrt{\dfrac{Gh}{c^5}} = \sqrt{\dfrac{(M^{-1} L^3 T^{-2})(M L^2 T^{-1})}{(L T^{-1})^5}} = \sqrt{\dfrac{L^5 T^{-3}}{L^5 T^{-5}}} = \sqrt{T^2} = T$ (Second).
Thus, B $\rightarrow$ II.

For IV: $\sqrt{\dfrac{Gh}{c^3}} = \sqrt{\dfrac{(M^{-1} L^3 T^{-2})(M L^2 T^{-1})}{(L T^{-1})^3}} = \sqrt{\dfrac{L^5 T^{-3}}{L^3 T^{-3}}} = \sqrt{L^2} = L$ (Meter).
Thus, A $\rightarrow$ IV.

For III: Substituting $L^2 = \dfrac{Gh}{c^3}$ from IV into the expression gives $\sqrt{\dfrac{K^2 L^2 c^3}{Gh}} = \sqrt{K^2 \left(\dfrac{Gh}{c^3}\right) \dfrac{c^3}{Gh}} = \sqrt{K^2} = K$ (Kelvin).
Thus, D $\rightarrow$ III.

The correct matching is A-IV, B-II, C-I, D-III.

Answer: A-IV, B-II, C-I, D-III

</details>

---

### Q5. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$L$, $C$ and $R$ represents physical quantities inductance, capacitance and resistance respectively. The dimensional formula $ML^2 T^{-4} A^{-2}$ corresponds to __________.

**Options:**

- **(A)** $\dfrac{R}{\sqrt{LC}}$
- **(B)** $\dfrac{R}{LC}$
- **(C)** $\dfrac{C}{\sqrt{LR}}$
- **(D)** $\dfrac{1}{R}\sqrt{\dfrac{L}{C}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{R}{\sqrt{LC}}$**

**Detailed Solution:**

Dimensional formula of inductance $L$ is obtained from $E = \dfrac{1}{2}LI^2$:

$[L] = \dfrac{[E]}{[I]^2} = \dfrac{ML^2T^{-2}}{A^2} = ML^2T^{-2}A^{-2}$

Dimensional formula of capacitance $C$ is obtained from $E = \dfrac{1}{2}\dfrac{Q^2}{C}$:

$[C] = \dfrac{[Q]^2}{[E]} = \dfrac{A^2T^2}{ML^2T^{-2}} = M^{-1}L^{-2}T^4A^2$

Dimensional formula of resistance $R$ is obtained from $P = I^2R$:

$[R] = \dfrac{[P]}{[I]^2} = \dfrac{ML^2T^{-3}}{A^2} = ML^2T^{-3}A^{-2}$

The dimensional formula of $\sqrt{LC}$ is:

$[\sqrt{LC}] = \sqrt{(ML^2T^{-2}A^{-2})(M^{-1}L^{-2}T^4A^2)} = \sqrt{T^2} = T$

Evaluating the dimensional formula of $\dfrac{R}{\sqrt{LC}}$:

$\left[\dfrac{R}{\sqrt{LC}}\right] = \dfrac{ML^2T^{-3}A^{-2}}{T} = ML^2T^{-4}A^{-2}$

This matches the given dimensional formula.

Answer: $\dfrac{R}{\sqrt{LC}}$

</details>

---

### Q6. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Dimensions of universal gravitational constant $(G)$ in terms of Planck's constant $(h)$, distance $(L)$, mass $(M)$ and time $(T)$ are _______.

**Options:**

- **(A)** $[hTLM^{-2}]$
- **(B)** $[hT^{-1}LM^{-2}]$
- **(C)** $[hTL^2 M^{-2}]$
- **(D)** $[h^{-1}T^{-1}LM^{-2}]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $[hT^{-1}LM^{-2}]$**

**Detailed Solution:**

The dimensional formula of the universal gravitational constant $G$ is obtained from Newton's law of gravitation $F = \dfrac{G m_1 m_2}{r^2}$.

$[G] = \dfrac{[F][r^2]}{[m_1 m_2]} = \dfrac{[MLT^{-2}][L^2]}{[M^2]} = [M^{-1}L^3T^{-2}]$

The dimensional formula of Planck's constant $h$ is obtained from the energy of a photon $E = h\nu$.

$[h] = \dfrac{[E]}{[\nu]} = \dfrac{[ML^2T^{-2}]}{[T^{-1}]} = [ML^2T^{-1}]$

Let the dimensions of $G$ be expressed as $[G] = [h]^a [L]^b [M]^c [T]^d$.

Substituting the dimensions, we get:

$[M^{-1}L^3T^{-2}] = [ML^2T^{-1}]^a [L]^b [M]^c [T]^d$

$[M^{-1}L^3T^{-2}] = [M^{a+c} L^{2a+b} T^{-a+d}]$

Equating the powers of $M$, $L$, and $T$ on both sides:

$a + c = -1$

$2a + b = 3$

$-a + d = -2$

Assuming $a = 1$ (as per the given options), we get:

$c = -1 - 1 = -2$

$b = 3 - 2(1) = 1$

$d = -2 + 1 = -1$

Therefore, the dimensions of $G$ are $[h^1 L^1 M^{-2} T^{-1}]$, which can be written as $[hT^{-1}LM^{-2}]$.

Answer: $[hT^{-1}LM^{-2}]$

</details>

---

### Q7. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Match List - I with List - II. 
 \(\begin{array}{llll} & \text{List - I} & & \text{List - II} \\ A. & \text{Coefficient of viscosity} & I. & [M L^{-1} T^{-1}] \\ B. & \text{Surface tension} & II. & [M L^{0} T^{-2}] \\ C. & \text{Pressure} & III. & [M L^{-1} T^{-2}] \\ D. & \text{Surface energy} & IV. & [M L^{2} T^{-2}] \end{array}\) 
 Choose the correct answer from the options given below :

**Options:**

- **(A)** A-I, B-II, C-IV, D-III
- **(B)** A-IV, B-I, C-II, D-III
- **(C)** A-I, B-II, C-III, D-IV
- **(D)** A-I, B-III, C-II, D-IV

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A-I, B-II, C-III, D-IV**

**Detailed Solution:**

(A) Coefficient of viscosity:
$\eta = \frac{F \cdot dr}{A \cdot dv} = \frac{[MLT^{-2}][L]}{[L^2][LT^{-1}]} = [ML^{-1}T^{-1}]$ → I
(B) Surface tension:
$S = \frac{F}{L} = \frac{[MLT^{-2}]}{[L]} = [MT^{-2}] = [ML^0T^{-2}]$ → II
(C) Pressure:
$P = \frac{F}{A} = \frac{[MLT^{-2}]}{[L^2]} = [ML^{-1}T^{-2}]$ → III
(D) Surface energy:
$E = S \times A = [MT^{-2}][L^2] = [ML^2T^{-2}]$ → IV
Hence, A-I, B-II, C-III, D-IV.

</details>

---

### Q8. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Match the LIST-I with LIST-II 
 \(\begin{array}{||c|l||c|l||} \hline & \text{List-I} & & \text{List-II} \\ \hline \text{A.} & \text{Magnetic induction} & \text{I.} & \mathrm{M\,L\,T^{-2}\,A^{-2}} \\ \hline \text{B.} & \text{Magnetic flux} & \text{II.} & \mathrm{M\,L^{2}\,T^{-2}\,A^{-2}} \\ \hline \text{C.} & \text{Magnetic permeability} & \text{III.} & \mathrm{M\,L^{0}\,T^{-2}\,A^{-1}} \\ \hline \text{D.} & \text{Self inductance} & \text{IV.} & \mathrm{M\,L^{2}\,T^{-2}\,A^{-1}} \\ \hline \end{array}\) 
 Choose the correct answer from the options given below:

**Options:**

- **(A)** A-III, B-IV, C-II, D-I
- **(B)** A-III, B-IV, C-I, D-II
- **(C)** A-IV, B-III, C-I, D-II
- **(D)** A-I, B-III, C-IV, D-II

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A-III, B-IV, C-I, D-II**

**Detailed Solution:**

Match physical quantities with dimensional formulas using fundamental principles.
Magnetic Induction (A): From $F = qvB$, $[B] = \frac{MLT^{-2}}{AT \cdot LT^{-1}} = MT^{-2}A^{-1} = $ III
Magnetic Flux (B): $\Phi = BA$, $[\Phi] = MT^{-2}A^{-1} \cdot L^2 = ML^2T^{-2}A^{-1} = $ IV
Magnetic Permeability (C): From $B = \mu H$ with $[H] = ALT^{-1}$, $[\mu] = \frac{MT^{-2}A^{-1}}{AL^{-1}T^{-1}} = MLT^{-2}A^{-2} = $ I
Self Inductance (D): From $\varepsilon = L\frac{dI}{dt}$, $[L] = \frac{ML^2T^{-3}A^{-1}}{AT^{-1}} = ML^2T^{-2}A^{-2} = $ II
Correct matching: A-III, B-IV, C-I, D-II

</details>

---

### Q9. JEE Main 2026 (23 January Shift 2)

*Type:* `numerical` | *Level:* `2`

A ball of radius $r$ and density $\rho$ dropped through a viscous liquid of density $\sigma$ and viscosity $\eta$ attains its terminal velocity at time $t$, given by $t=A \rho^{a} r^{b} \eta^{\mathrm{c}} \sigma^{d}$, where $A$ is a constant and $a, b, c$ and $d$ are integers. The value of $\frac{b+c}{a+d}$ is $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

Using dimensional analysis on $t = A\rho^a r^b \eta^c \sigma^d$:
the dimensions are [T] = $[M L^{-3}]^a [L]^b [M L^{-1} T^{-1}]^c [M L^{-3}]^d$.
Expanding: [T] = $M^{a+c+d} L^{-3a+b-c-3d} T^{-c}$.
Comparing powers: For T: $1 = -c$, giving $c = -1$.
For M: $0 = a + c + d$, so $a + d = 1$.
For L: $0 = -3a + b - c - 3d = -3a + b + 1 - 3d$, giving $b = 3(a+d) - 1 = 3(1) - 1 = 2$.
Therefore $(b+c)/(a+d) = (2-1)/1 = 1$.

</details>

---

### Q10. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\epsilon, E$ and $t$ represent the free space permittivity, electric field and time respectively, then the unit of $\frac{\epsilon E}{t}$ will be :

**Options:**

- **(A)** $\mathrm{Am}^{2}$
- **(B)** Am
- **(C)** $\mathrm{A} / \mathrm{m}^{2}$
- **(D)** A/m

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{A} / \mathrm{m}^{2}$**

**Detailed Solution:**

We need to find the unit of $\frac{\epsilon E}{t}$.
From Maxwell's equations, the displacement current density is given by $J_d = \epsilon \frac{\partial E}{\partial t}$.
The term $\frac{\epsilon E}{t}$ has the same dimensions as displacement current density $J_d$.
Current density $J$ is defined as current per unit area, $J = \frac{I}{A}$.
The SI unit of current $I$ is Ampere (A) and the SI unit of area $A$ is $m^2$.
Therefore, the unit of current density is $A/m^2$.
Alternatively, using dimensions:
$[\epsilon] = M^{-1}L^{-3}T^4A^2$
$[E] = MLT^{-3}A^{-1}$
$[t] = T$
Dimension of $\frac{\epsilon E}{t} = \frac{(M^{-1}L^{-3}T^4A^2)(MLT^{-3}A^{-1})}{T} = L^{-2}A$.
This corresponds to the unit $A/m^2$.

</details>

---

### Q11. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Match the LIST-I with LIST-II 
 \(\begin{array}{||c|l||c||l||} \hline & \textbf{List-I} & & \textbf{List-II} \\ \hline A. & \text{Spring constant} & I. & \mathrm{M L^{2} T^{-2} K^{-1}} \\ \hline B. & \text{Thermal conductivity} & II. & \mathrm{M L^{0} T^{-2}} \\ \hline C. & \text{Boltzmann constant} & III. & \mathrm{M L^{2} T^{-3} A^{-2}} \\ \hline D. & \text{Inductive reactance} & IV. & \mathrm{M L T^{-3} K^{-1}} \\ \hline \end{array}\) 
 Choose the correct answer from the options given below:

**Options:**

- **(A)** A-II, B-IV, C-I, D-III
- **(B)** A-I, B-IV, C-II, D-III
- **(C)** A-II, B-I, C-IV, D-III
- **(D)** A-III, B-II, C-IV, D-I

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A-II, B-IV, C-I, D-III**

**Detailed Solution:**

A. Spring constant: $F = kx \Rightarrow [k] = MLT^{-2}/L = ML^0T^{-2}$ $\rightarrow$ II
B. Thermal conductivity: $Q/t = KA(dT/dx) \Rightarrow [K] = ML^2T^{-3}/(L^2 \cdot K/L) = MLT^{-3}K^{-1}$ $\rightarrow$ IV
C. Boltzmann constant: $E = k_BT \Rightarrow [k_B] = ML^2T^{-2}K^{-1}$ $\rightarrow$ I
D. Inductive reactance: same dimension as resistance $= ML^2T^{-3}A^{-2}$ $\rightarrow$ III
Matching: A-II, B-IV, C-I, D-III.

</details>

---

### Q12. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider a modified Bernoulli equation. 
 $\left(\mathrm{P}+\frac{A}{B t^{2}}\right)+\rho g(h+B t)+\frac{1}{2} \rho V^{2}=$ constant 
 If $t$ has the dimension of time then the dimensions of $A$ and $B$ are $\_\_\_\_$, $\_\_\_\_$ respectively.

**Options:**

- **(A)** $\left[\mathrm{ML}^{0} \mathrm{~T}^{-2}\right]$ and $\left[\mathrm{M}^{0} \mathrm{LT}^{-2}\right]$
- **(B)** $\left[\mathrm{ML}^{0} \mathrm{~T}^{-2}\right]$ and $\left[\mathrm{M}^{0} \mathrm{LT}^{-1}\right]$
- **(C)** $\left[\mathrm{ML}^{0} \mathrm{~T}^{-1}\right]$ and $\left[\mathrm{M}^{0} \mathrm{LT}\right]$
- **(D)** $\left[\mathrm{ML}^{0} \mathrm{~T}^{-1}\right]$ and $\left[\mathrm{M}^{0} \mathrm{LT}^{-1}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\mathrm{ML}^{0} \mathrm{~T}^{-1}\right]$ and $\left[\mathrm{M}^{0} \mathrm{LT}^{-1}\right]$**

**Detailed Solution:**

All terms must have dimension of pressure $[ML^{-1}T^{-2}]$.
For $(h + Bt)$: Since $\rho gh$ has dimension of pressure, $[h] = [L]$.
For dimensional consistency: $[Bt] = [L]$, so $[B] = [LT^{-1}] = [M^0LT^{-1}]$
For $\frac{A}{Bt^2}$: $\frac{[A]}{[B][T^2]} = [ML^{-1}T^{-2}]$
$[A] = [B][T^2][ML^{-1}T^{-2}] = [LT^{-1}][T^2][ML^{-1}T^{-2}] = [ML^0T^{-1}]$
$[A] = [ML^0T^{-1}]$ and $[B] = [M^0LT^{-1}]$

</details>

---

### Q13. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Match List-I with List-II.
$\begin{array}{|l|l|l|l|} \hline & \text{List-I} & & \text{List-II} \\ \hline \text{(A)} & \text{Mass density} & \text{(I)} & {\left[\mathrm{ML}^2 \mathrm{~T}^{-3}\right]} \\ \hline \text{(B)} & \text{Impulse} & \text{(II)} & {\left[\mathrm{MLT}^{-1}\right]} \\ \hline \text{(C)} & \text{Power} & \text{(III)} & {\left[\mathrm{ML}^2 \mathrm{~T}^0\right]} \\ \hline \text{(D)} & \text{Moment of inertia} & \text{(IV)} & {\left[\mathrm{ML}^{-3} \mathrm{~T}^0\right]} \\ \hline\end{array}$
Choose the correct answer from the options given below :

**Options:**

- **(A)** (A)-(IV), (B)-(II), (C)-(III), (D)-(I)
- **(B)** (A)-(I), (B)-(III), (C)-(IV), (D)-(II)
- **(C)** (A)-(IV), (B)-(II), (C)-(I), (D)-(III)
- **(D)** (A)-(II), (B)-(III), (C)-(IV), (D)-(I)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (A)-(IV), (B)-(II), (C)-(I), (D)-(III)**

**Detailed Solution:**

(A) Mass density $=\frac{M}{V}=M^1 L^{-3}$...(iv)
(B) Impulse $=\mathrm{M} \times \mathrm{u}=\mathrm{M}^1 \mathrm{~L}^1 \mathrm{~T}^{-1}$....(ii)
(C) Power $=\mathrm{F}. \mathrm{V}=\mathrm{M}^1 \mathrm{~L}^2 \mathrm{~T}^{-3}$....(i)
(D) Moment of inertia $=\mathrm{Mr}^2=\mathrm{M}^1 \mathrm{~L}^2$...(iii)

</details>

---

### Q14. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The dimension of $\sqrt{\frac{\mu_0}{\epsilon_0}}$ is equal to that of :
( $\mu_0=$ Vacuum permeability and $\epsilon_0=$ Vacuum permittivity)

**Options:**

- **(A)** Voltage
- **(B)** Capacitance
- **(C)** Inductance
- **(D)** Resistance

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Resistance**

**Detailed Solution:**

$\begin{aligned} & L=\frac{\mu_0 N A}{\ell} \\ & C=\frac{A \epsilon_0}{d} \\ & \frac{L}{C} \propto \frac{\mu_0}{\epsilon_0} \\ & \sqrt{\frac{\mu_0}{\epsilon_0}} \propto \sqrt{\frac{L}{C}} \\ & \frac{L}{C}=\frac{\tau R}{(\tau / R)}=R^2 \\ & \sqrt{\frac{\mu_0}{\epsilon_0}}=R\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\epsilon_0$ denotes the permittivity of free space and $\Phi_{\mathrm{E}}$ is the flux of the electric field through the area bounded by the closed surface, then dimension of $\left(\epsilon_0 \frac{\mathrm{~d} \phi_{\mathrm{E}}}{\mathrm{dt}}\right)$ are that of :

**Options:**

- **(A)** Electric field
- **(B)** Electric potential
- **(C)** Electric charge
- **(D)** Electric current

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Electric current**

**Detailed Solution:**

We know that formula for displacement current is given by
$\mathrm{id}=\varepsilon_0 \frac{\mathrm{~d} \phi_{\varepsilon}}{\mathrm{dt}}$

</details>

---

### Q16. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an electromagnetic system, a quantity defined as the ratio of electric dipole moment and magnetic dipole moment has dimension of $\left[M^P L^{\circ} \mathrm{T}^{\mathrm{R}} \mathrm{A}^{\mathrm{S}}\right]$. The value of P and Q are :

**Options:**

- **(A)** $-1,0$
- **(B)** $-1,1$
- **(C)** $1,-1$
- **(D)** $0,-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0,-1$**

**Detailed Solution:**

Electric dipole moment $(\overrightarrow{\mathrm{P}})=\mathrm{q} \times 2 \ell$
Magnetic dipole moment $(\overrightarrow{\mathrm{M}})=\mathrm{IA}$
$\left[\frac{\mathrm{P}}{\mathrm{M}}\right]=\left[\frac{\mathrm{LTA}}{\mathrm{~L}^2 \mathrm{~A}}\right]=\mathrm{L}^{-1} \mathrm{~T}=\mathrm{M}^0 \mathrm{~L}^{-1} \mathrm{~T}^1 \mathrm{~A}^0$
After compering values of $\mathrm{P} \& \mathrm{Q}$ are $0,-1$ Correct Answer : Option 4

</details>

---

### Q17. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given below are two statements :
Statement (I) : The dimensions of Planck's constant and angular momentum are same.
Statement (II) : In Bohr's model electron revolve around the nucleus only in those orbits for which angular momentum is integral multiple of Planck's constant.
In the light of the above statements, choose the most appropriate answer from the options given below :

**Options:**

- **(A)** Both Statement I and Statement II are correct
- **(B)** Statement I is incorrect but Statement II is correct
- **(C)** Statement I is correct but Statement II is incorrect
- **(D)** Both Statement I and Statement II are incorrect

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement I is correct but Statement II is incorrect**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{E}=\mathrm{hf} \\
& \mathrm{ML}^2 \mathrm{~T}^{-2}=[\mathrm{h}] \times\left[\mathrm{T}^{-1}\right] \\
& {[\mathrm{h}]=\left[\mathrm{ML}^2 \mathrm{~T}^{-1}\right]} \\
& \mathrm{L}=[\mathrm{MVR}]=\left[\mathrm{ML}^2 \mathrm{~T}^{-1}\right] \\
& \mathrm{L}=\frac{\mathrm{nh}}{2 \pi}
\end{aligned}$
L is integral multiple of $\frac{\mathrm{h}}{2 \pi}$

</details>

---

### Q18. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an electromagnetic system, the quantity representing the ratio of electric flux and magnetic flux has dimension of $\mathrm{M}^{\mathrm{P}} \mathrm{L}^{\mathrm{Q}} \mathrm{T}^{\mathrm{R}} \mathrm{A}^{\mathrm{S}}$, where value of ' Q ' and ' R ' are

**Options:**

- **(A)** $(3,-5)$
- **(B)** $(-2,2)$
- **(C)** $(-2,1)$
- **(D)** $(1,-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(1,-1)$**

**Detailed Solution:**

$\begin{aligned} & \frac{\phi_{\mathrm{E}}}{\phi_{\mathrm{M}}}=\frac{\mathrm{EA}}{\mathrm{BA}}=\frac{E}{B} \\ & \mathrm{~B}=\frac{\mathrm{M} \ell \mathrm{T}^{-2}}{\mathrm{ATLT}^{-1}} \\ & \text { So }\left[\frac{\mathrm{E}}{\mathrm{B}}\right]=\frac{\mathrm{ML}^{-3} \mathrm{~A}^{-1}}{\mathrm{MT}^{-2} \mathrm{~A}^{-1}}=\mathrm{LT}^{-1}\end{aligned}$
$\begin{aligned} & \text { Or } \\ & E=c \cdot B \\ & {\left[\frac{E}{B}\right]=L T^{-1}}\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Match the <strong>LIST-I</strong> with<strong>LIST-II</strong><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TmywOzrj9gPYGabRn7L_tsdGgqlSahTii4KjjlxDcVM.original.fullsize.png"/>
Choose the<strong> <i>correct</i></strong> answer from the options given below :

**Options:**

- **(A)** A-III, B-IV, C-I, D-II
- **(B)** A-II, B-III, C-IV, D-I
- **(C)** A-III, B-II, C-I, D-IV
- **(D)** A-III, B-IV, C-II, D-I

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A-III, B-IV, C-I, D-II**

**Detailed Solution:**

(A) $[\mathrm{k}]=\frac{\mathrm{PV}}{\mathrm{NT}}=\frac{\mathrm{ML}^2 \mathrm{~T}^{-2}}{\mathrm{~K}}=\mathrm{ML}^2 \mathrm{~T}^{-2} \mathrm{~K}^{-1}$
(B) $[\eta]=\frac{\mathrm{F}}{6 \pi \mathrm{rv}}=\frac{\mathrm{MLT}^{-2}}{\mathrm{~L}^2 \mathrm{~T}^{-1}}=\mathrm{ML}^{-1} \mathrm{~T}^{-1}$
(C) $[\mathrm{h}]=\frac{\mathrm{E}}{\mathrm{f}}=\frac{\mathrm{ML}^2 \mathrm{~T}^{-2}}{\mathrm{~T}^{-1}}=\mathrm{ML}^2 \mathrm{~T}^{-1}$
(D) $\frac{\mathrm{dQ}}{\mathrm{dt}}=\mathrm{k} \frac{\mathrm{AdT}}{\mathrm{dx}}$
$\mathrm{k}=\frac{\left(\mathrm{ML}^2 \mathrm{~T}^{-3}\right) \mathrm{L}}{\mathrm{L}^2 \cdot \mathrm{~K}}=\mathrm{MLT}^{-3} \mathrm{~K}^{-1}$

</details>

---

### Q20. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Match the LIST-I with LIST-II
$\begin{array}{|l|l|l|l|}\hline & \text{LIST-I} & & \text{LIST-II} \\ \hline \text{A.} & \text{Gravitational constant} & \text{I.} & {\left[\mathrm{LT}^{-2}\right]} \\ \hline \text{B.} & \begin{array}{l} \text{Gravitational potential} \\ \text{energy} \end{array} & \text{II.} & {\left[\mathrm{L}^2 \mathrm{~T}^{-2}\right]} \\ \hline \text{C.} & \text{Gravitational potential} & \text{III.} & {\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right]} \\ \hline \text{D.} & \begin{array}{l} \text{Acceleration due to} \\ \text{gravity} \end{array} & \text{IV.} & {\left[\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}\right]} \\ \hline \end{array}$
Choose the correct answer from the options given below :

**Options:**

- **(A)** A-IV, B-III, C-II, D-I
- **(B)** A-III, B-II, C-I, D-IV
- **(C)** A-II, B-IV, C-III, D-I
- **(D)** A-I, B-III, C-IV, D-II

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A-IV, B-III, C-II, D-I**

**Detailed Solution:**

$\begin{aligned}
& \text { (A) } \mathrm{G}=\frac{\mathrm{Fr}^2}{\mathrm{~m}^2} \\
& {[\mathrm{G}]=\frac{\left[\mathrm{MLT}^{-2}\right]\left[\mathrm{L}^2\right]}{\left[\mathrm{M}^2\right]}=\left[\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}\right](\mathrm{IV})}
\end{aligned}$
(B)
$\begin{aligned}
& \text { P.E. }=\mathrm{mgh}=\left[\mathrm{MLT}^{-2} \mathrm{~L}\right] \\
& =\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right] \text { (III) }
\end{aligned}$
(C) Gravitational Potential $=\frac{\mathrm{GM}}{\mathrm{r}}$
$=\frac{\left[\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}\right][\mathrm{M}]}{[\mathrm{L}]}=\left[\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-2}\right]=\left[\mathrm{L}^2 \mathrm{~T}^{-2}\right](\mathrm{II})$
(D) Acceleration due to gravity $=[\mathrm{g}]=\left[\mathrm{LT}^{-2}\right](\mathrm{I})$

</details>

---

### Q21. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A person measures mass of 3 different particles as $435.42 \mathrm{~g}, 226.3 \mathrm{~g}$ and 0.125 g. According to the rules for arithmetic operations with significant figures, the additions of the masses of 3 particles will be.

**Options:**

- **(A)** 661.845 g
- **(B)** 662 g
- **(C)** 661.8 g
- **(D)** 661.84 g

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 661.8 g**

**Detailed Solution:**

$\mathrm{m}_1+\mathrm{m}_2+\mathrm{m}_3=435.42+226.3+0.125$
According to least significant digits $\mathrm{m}=661.8 \mathrm{~g}$

</details>

---

### Q22. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given a charge $q$, current I and permeability of vacuum $\mu_0$. Which of the following quantity has the dimension of momentum?

**Options:**

- **(A)** $\mathrm{qI} / \mu_0$
- **(B)** $q \mu_0 I$
- **(C)** $q^2 \mu_0 I$
- **(D)** $q \mu_0 / I$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $q \mu_0 I$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{Q}=\mathrm{AT} \\ & \mathrm{I}=\mathrm{A} \\ & \mu_0=\mathrm{MLT}^{-2} \mathrm{~A}^{-2} \\ & \mathrm{P}=\mathrm{Q}^{\mathrm{x}} \mu_0^{\mathrm{y}} \mathrm{I}^{\mathrm{z}}=[\mathrm{AT}]^{\mathrm{x}}\left[\mathrm{MLT}^{-2} \mathrm{~A}^{-2}\right]^{\mathrm{y}}[\mathrm{A}]^{\mathrm{z}} \\ & \mathrm{MLT}^{-1}=\mathrm{M}^{\mathrm{y}} \mathrm{L}^{\mathrm{y}} \mathrm{T}^{\mathrm{x}-2 \mathrm{y}} \mathrm{A}^{-2 \mathrm{y}+\mathrm{z+x}} \\ & \text { Now; } \mathrm{y}=1 \\ & \mathrm{x}-2 \mathrm{y}=-1 \\ & -2 \mathrm{y}+\mathrm{z}=0 \\ & \therefore \mathrm{x}=\mathrm{y}=\mathrm{z}=1\end{aligned}$

</details>

---

### Q23. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mu_0$ and $\varepsilon_0$ are the permeability and permittivity of free space, respectively, then the dimension of $\left(\frac{1}{\mu_0 \varepsilon_0}\right)$ is :

**Options:**

- **(A)** $\mathrm{L} / \mathrm{T}^2$
- **(B)** $L^2 / T^2$
- **(C)** $T^2 / L$
- **(D)** $\mathrm{T}^2 / \mathrm{L}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $L^2 / T^2$**

**Detailed Solution:**

$\mathrm{C}=\frac{1}{\sqrt{\mu_0 \varepsilon_0}} \Rightarrow \frac{1}{\mu_0 \varepsilon_0}=\mathrm{C}^2=\mathrm{L}^2 \mathrm{~T}^{-2}$

</details>

---

### Q24. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Match List-I with List-II.
$\begin{array}{ll} \text{List-I} & \text{List-II} \\ \text{(A) Coefficient of viscosity} & \text{(I) } \left[\mathrm{ML}^0 \mathrm{~T}^{-3}\right] \\ \text{(B) Intensity of wave} & \text{(II) } \left[\mathrm{ML}^{-2} \mathrm{~T}^{-2}\right] \\ \text{(C) Pressure gradient} & \text{(III) } \left[\mathrm{M}^{-1} \mathrm{LT}^2\right] \\ \text{(D) Compressibility} & \text{(IV) } \left[\mathrm{ML}^{-1} \mathrm{~T}^{-1}\right]\end{array}$
Choose the correct answer from the options given below :

**Options:**

- **(A)** $(\mathrm{A})-(\mathrm{I}),(\mathrm{B})-(\mathrm{IV}),(\mathrm{C})-(\mathrm{III}),(\mathrm{D})-(\mathrm{II})$
- **(B)** (A)-(IV), (B)-(I), (C)-(II), (D)-(III)
- **(C)** $(\mathrm{A})-(\mathrm{IV}),(\mathrm{B})-(\mathrm{II}),(\mathrm{C})-(\mathrm{I}),(\mathrm{D})-(\mathrm{III})$
- **(D)** (A)-(II), (B)-(III), (C)-(IV), (D)-(I)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (A)-(IV), (B)-(I), (C)-(II), (D)-(III)**

**Detailed Solution:**

(A) Coefficient of viscosity
$[\eta]=\left[\mathrm{M}^1 \mathrm{~L}^{-1} \mathrm{~T}^{-1}\right]$
(B) Intensity $[\mathrm{I}]=\left[\mathrm{M}^1 \mathrm{~L}^0 \mathrm{~T}^{-3}\right]$
(C) Pressure gradient $=\left[\mathrm{ML}^{-2} \mathrm{~T}^{-2}\right]$
(D) Compressibility $[\mathrm{K}]=\left[\mathrm{M}^{-1} \mathrm{~L}^1 \mathrm{~T}^2\right]$

</details>

---

### Q25. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The equation for real gas is given by $\left(\mathrm{P}+\frac{\mathrm{a}}{\mathrm{V}^2}\right)(\mathrm{V}-\mathrm{b})=\mathrm{RT}$, where $\mathrm{P}, \mathrm{V}, \mathrm{T}$ and R are the pressure, volume, temperature and gas constant, respectively. The dimension of $\mathrm{ab}^{-2}$ is equivalent to that of :

**Options:**

- **(A)** Planck's constant
- **(B)** Compressibility
- **(C)** Strain
- **(D)** Energy density

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Energy density**

**Detailed Solution:**

$\begin{aligned} & {\left[\mathrm{P}+\frac{\mathrm{a}}{\mathrm{V}^2}\right](\mathrm{V}-\mathrm{b})=\mathrm{RT}} \\ & \therefore[\mathrm{a}]=[\mathrm{P}]\left[\mathrm{V}^2\right]=\mathrm{ML}^{-1} \mathrm{~T}^{-2} \mathrm{~L}^6=\mathrm{ML}^5 \mathrm{~T}^{-2} \\ & {[\mathrm{~b}]=[\mathrm{V}]=\mathrm{L}^3} \\ & {\left[\mathrm{ab}^{-2}\right]=\mathrm{ML}^5 \mathrm{~T}^{-2} \mathrm{~L}^{-6}=\mathrm{ML}^{-1} \mathrm{~T}^{-2}}\end{aligned}$
Dimension of energy density.

</details>

---

### Q26. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Match List - I with List - II.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/YtlGG04R91hVY1cL4q_g_e-NlTvFEVkC6ZVygqwlFFk.original.fullsize.png"/>

Choose the correct answer from the options given below :

**Options:**

- **(A)** (A)-(I), (B)-(III), (C)-(II), (D)-(IV)
- **(B)** (A)-(IV), (B)-(II), (C)-(III), (D)-(I)
- **(C)** (A)-(II), (B)-(IV), (C)-(I), (D)-(III)
- **(D)** (A)-(II), (B)-(I), (C)-(IV), (D)-(III)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (A)-(II), (B)-(IV), (C)-(I), (D)-(III)**

**Detailed Solution:**

(A) $[\mathrm{Y}]=\frac{\mathrm{F}}{\mathrm{A}\left(\frac{\Delta \ell}{\ell}\right)} \Rightarrow \frac{\mathrm{MLT}^{-2}}{\mathrm{~L}^2}=\mathrm{ML}^{-1} \mathrm{~T}^{-2}$
(B) Torque $(\vec{\tau})=\overrightarrow{\mathrm{r}} \times \overrightarrow{\mathrm{F}}$
$(\vec{\tau})=\mathrm{L} \times \mathrm{MLT}^{-2}=\mathrm{ML}^2 \mathrm{~T}^{-2}(\mathrm{IV})$
(C) Coefficient of viscosity $\Rightarrow F=\eta A \frac{d V}{d t}$
$\eta \rightarrow \mathrm{Pa} \cdot \mathrm{sec}$
$[\eta]=\frac{\mathrm{MLT}^{-2}}{\mathrm{~L}^2} \times \mathrm{T}=\mathrm{ML}^{-1} \mathrm{~T}^{-1}$
(D) Gravitational constant (G)
$\begin{aligned}
& \mathrm{F}=\frac{\mathrm{GM}_1 \mathrm{M}_2}{\mathrm{r}^2} \\
& {[\mathrm{G}]=\frac{\mathrm{F} \cdot \mathrm{r}^2}{\mathrm{~m}_1 \mathrm{~m}_2}=\frac{\mathrm{MLT}^{-2} \times \mathrm{L}^2}{\mathrm{M}^2}=\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}}
\end{aligned}$

</details>

---

### Q27. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The pair of physical quantities not having same dimensions is :

**Options:**

- **(A)** Pressure and Young's modulus
- **(B)** Surface tension and impulse
- **(C)** Torque and energy
- **(D)** Angular momentum and Planck's constant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Surface tension and impulse**

**Detailed Solution:**

[Angular momentum $]=\mathrm{ML}^2 \mathrm{~T}^{-1}$
[Planck's Constant] $=\mathrm{ML}^2 \mathrm{~T}^{-1}$
[Torque] $=\mathrm{ML}^2 \mathrm{~T}^{-2}$
[Energy] $=\mathrm{ML}^2 \mathrm{~T}^{-2}$
[Surface tension] $=\mathrm{MT}^{-2}$
[Impulse]= MLT $^{-1}$
[Pressure $]=\mathrm{ML}^{-1} \mathrm{~T}^{-2}$
[Young's modulus] $=\mathrm{ML}^{-1} \mathrm{~T}^{-2}$

</details>

---

### Q28. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The expression given below shows the variation of velocity \((v)\) with time (t), \(v=\mathrm{At}^2+\frac{\mathrm{Bt}}{\mathrm{C}+\mathrm{t}}\). The dimension of ABC is :

**Options:**

- **(A)** \(\left[\mathrm{M}^0 \mathrm{~L}^1 \mathrm{~T}^{-3}\right]\)
- **(B)** \(\left[\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-2}\right]\)
- **(C)** \(\left[\mathrm{M}^0 \mathrm{~L}^1 \mathrm{~T}^{-2}\right]\)
- **(D)** \(\left[\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-3}\right]\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) \(\left[\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-3}\right]\)**

**Detailed Solution:**

$\begin{aligned} & {\left[\mathrm{LT}^{-1}\right]=[\mathrm{A}]\left[\mathrm{T}^2\right]=\frac{[\mathrm{B}][\mathrm{T}]}{[\mathrm{C}]+[\mathrm{T}]}} \\ & {[\mathrm{C}]=[\mathrm{T}]} \\ & {[\mathrm{A}]=\left[\mathrm{LT}^{-3}\right]} \\ & {[\mathrm{B}]=\left[\mathrm{LT}^{-1}\right]} \\ & {[\mathrm{ABC}]=\left[\mathrm{L}^2 \mathrm{~T}^{-3}\right]}\end{aligned}$

</details>

---

### Q29. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Match List - I with List - II.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Qi3LXFkvEaW9b7_GVVMkdeJK96g4i7e8hb3MCDlb2Cg.original.fullsize.png"/>

**Options:**

- **(A)** (A)-(II), (B)-(I), (C)-(IV), (D)-(III)
- **(B)** (A)-(I), (B)-(III), (C)-(IV), (D)-(II)
- **(C)** (A)-(III), (B)-(I), (C)-(II), (D)-(IV)
- **(D)** (A)-(III), (B)-(I), (C)-(IV), (D)-(II)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (A)-(III), (B)-(I), (C)-(IV), (D)-(II)**

**Detailed Solution:**

$\begin{aligned} & \text { Angular impulse }=\left[\mathrm{M} \mathrm{L}^2 \mathrm{~T}^{-1}\right] \\ & \text { Latent Heat }=\left[\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-2}\right] \\ & \text { Electrical resistivity }=\left[\mathrm{M} \mathrm{L}^3 \mathrm{~T}^{-3} \mathrm{~A}^{-2}\right] \\ & \text { Electromotive force }=\left[\mathrm{M} \mathrm{L}^2 \mathrm{~T}^{-3} \mathrm{~A}^{-1}\right]\end{aligned}$

</details>

---

### Q30. JEE Main 2025 (28 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

In a measurement, it is asked to find modulus of elasticity per unit torque applied on the system. The measured quantity has dimension of $\left[M^a L^b T^c\right]$. If $b=-3$, the value of $c$ is ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

[Modulus of elasticity] $=\mathrm{ML}^{-1} \mathrm{~T}^{-2}$
[Torque] $=$ ML $^2 \mathrm{~T}^{-2}$
[Modulus of elasticity per unit torque]
$=\frac{\mathrm{ML}^{-1} \mathrm{~T}^{-2}}{\mathrm{ML}^2 \mathrm{~T}^{-2}}=\mathrm{L}^{-3}$

</details>

---

### Q31. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The electric flux is $\phi=\alpha \sigma+\beta \lambda$ where $\lambda$ and $\sigma$ are linear and surface charge density, respectively. $\left(\frac{\alpha}{\beta}\right)$ represents

**Options:**

- **(A)** electric field
- **(B)** area
- **(C)** charge
- **(D)** displacement

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) displacement**

**Detailed Solution:**

$\begin{aligned} & \alpha \equiv \frac{\phi}{\sigma} \\ & \beta=\frac{\phi}{\lambda} \\ & \frac{\alpha}{\beta} \equiv \frac{\lambda}{\sigma} \equiv \text { displacement }\end{aligned}$

</details>

---

### Q32. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The position of a particle moving on $x$-axis is given by $x(t)=A \sin t+B \cos ^2 t+C t^2+D$, where $t$ is time. The dimension of $\frac{A B C}{D}$ is

**Options:**

- **(A)** $L^2 T^{-2}$
- **(B)** $L^2$
- **(C)** $L$
- **(D)** $L^3 \mathrm{~T}^{-2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $L^2 T^{-2}$**

**Detailed Solution:**

$\begin{aligned} & \text { Dimension }[\mathrm{x}(\mathrm{t})]=[\mathrm{L}] \\ & {[\mathrm{A}]=[\mathrm{L}]} \\ & {[\mathbf{B}]=[\mathrm{L}]} \\ & {[\mathbf{C}]=\left[\mathrm{LT}^{-2}\right]} \\ & {[\mathrm{D}]=[\mathrm{L}]} \\ & {\left[\frac{\mathrm{ABC}}{\mathrm{D}}\right]=\left[\frac{\mathrm{L} \times \mathrm{L} \times \mathrm{LT}^{-2}}{\mathrm{~L}}\right]=\left[\mathrm{L}^2 \mathrm{~T}^{-2}\right]}\end{aligned}$

</details>

---

### Q33. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which one of the following is the correct dimensional formula for the capacitance in F ? $\mathrm{M}, \mathrm{L}, \mathrm{T}$ and C stand for unit of mass, length, time and charge,

**Options:**

- **(A)** $[\mathrm{F}]=\left[\mathrm{C}^2 \mathrm{M}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^2\right]$
- **(B)** $[\mathrm{F}]=\left[\mathrm{C}^2 \mathrm{M}^{-2} \mathrm{~L}^2 \mathrm{~T}^2\right]$
- **(C)** $[\mathrm{F}]=\left[\mathrm{CM}^{-2} \mathrm{~L}^{-2} \mathrm{~T}^{-2}\right]$
- **(D)** $[\mathrm{F}]=\left[\mathrm{CM}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^2\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $[\mathrm{F}]=\left[\mathrm{C}^2 \mathrm{M}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^2\right]$**

**Detailed Solution:**

$\begin{aligned} & \text { Energy }=\frac{Q^2}{2 C} \\ & \begin{aligned} \therefore \quad[\mathrm{F}] & =\frac{\left[\mathrm{C}^2\right]}{\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right]} \\ & =\left[\mathrm{C}^2 \mathrm{M}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^{+2}\right]\end{aligned}\end{aligned}$

</details>

---

### Q34. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $B$ is magnetic field and $\mu_0$ is permeability of free space, then the dimensions of $\left(B / \mu_0\right)$ is

**Options:**

- **(A)** $\mathrm{ML}^2 \mathrm{~T}^{-2} \mathrm{~A}^{-1}$
- **(B)** $\mathrm{MT}^{-2} \mathrm{~A}^{-1}$
- **(C)** $\mathrm{L}^{-1} \mathrm{~A}$
- **(D)** $\mathrm{LT}^{-2} \mathrm{~A}^{-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{L}^{-1} \mathrm{~A}$**

**Detailed Solution:**

For a current carrying loop at centre
$\begin{aligned}
& B=\frac{\mu_0 i}{2 R} \\
& \therefore \quad \frac{B}{\mu_0} \equiv \frac{i}{R} \equiv\left[\mathrm{AL}^{-1}\right]
\end{aligned}$

</details>

---

### Q35. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The de-Broglie wavelength associated with a particle of mass $m$ and energy $E$ is $h / \sqrt{2 m E}$. The dimensional formula for Planck's constant is :

**Options:**

- **(A)** $\left[\mathrm{ML}^2 \mathrm{~T}^{-1}\right]$
- **(B)** $\left[\mathrm{ML}^{-1} \mathrm{~T}^{-2}\right]$
- **(C)** $\left[\mathrm{MLT}^{-2}\right]$
- **(D)** $\left[\mathrm{M}^2 \mathrm{~L}^2 \mathrm{~T}^{-2}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\mathrm{ML}^2 \mathrm{~T}^{-1}\right]$**

**Detailed Solution:**

$\begin{aligned} & \lambda=\frac{\mathrm{h}}{\sqrt{2 \mathrm{mE}}} \text { or } \mathrm{E}=\mathrm{h} \nu \\ & {\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right]=\mathrm{h}\left[\mathrm{T}^{-1}\right]} \\ & \mathrm{h}=\left[\mathrm{ML}^2 \mathrm{~T}^{-1}\right]\end{aligned}$

</details>

---

### Q36. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The dimensional formula of latent heat is :

**Options:**

- **(A)** $\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right]$
- **(B)** $\left[\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-2}\right]$
- **(C)** $\left[\mathrm{MLT}^{-2}\right]$
- **(D)** $\left[\mathrm{M}^{\circ} \mathrm{LT}^{-2}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-2}\right]$**

**Detailed Solution:**

Latent heat is specific heat
$\Rightarrow \frac{\mathrm{ML}^2 \mathrm{~T}^{-2}}{\mathrm{M}}=\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-2}$

</details>

---

### Q37. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\epsilon_0$ is the permittivity of free space and $\mathrm{E}$ is the electric field, then $\epsilon_0 \mathrm{E}^2$ has the dimensions :

**Options:**

- **(A)** $\left[\mathrm{M}^{-1} \mathrm{~L}^{-3} \mathrm{~T}^4 \mathrm{~A}^2\right]$
- **(B)** $\left[\mathrm{M} \mathrm{L}^2 \mathrm{~T}^{-2}\right]$
- **(C)** $\left[\mathrm{M}^{\circ} \mathrm{L}^{-2} \mathrm{TA}\right]$
- **(D)** $\left[\mathrm{M} \mathrm{L}^{-1} \mathrm{~T}^{-2}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\mathrm{M} \mathrm{L}^{-1} \mathrm{~T}^{-2}\right]$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{E}=\frac{\mathrm{KQ}}{\mathrm{R}^2} \\ & \mathrm{E}=\frac{\mathrm{Q}}{4 \pi \varepsilon_0 \mathrm{R}^2} \\ & \varepsilon_0=\frac{\mathrm{Q}}{4 \pi \mathrm{R}^2 \mathrm{E}} \\ & \text { Now, } \varepsilon_0 \mathrm{E}^2=\frac{\mathrm{Q}}{4 \pi \mathrm{R}^2 \mathrm{E}} \cdot \mathrm{E}^2=\frac{\mathrm{Q}}{4 \pi \mathrm{R}^2} \cdot \mathrm{E} \\ & {\left[\varepsilon_0 \mathrm{E}^2\right]=\left[\frac{\mathrm{QE}}{\mathrm{R}^2}\right]=\frac{[\mathrm{Q}][\mathrm{E}]}{\left[\mathrm{R}^2\right]}=\frac{[\mathrm{Q}]}{\left[\mathrm{R}^2\right]} \frac{[\mathrm{W}]}{[\mathrm{Q}][\mathrm{R}]}} \\ & =\frac{[\mathrm{W}]}{\left[\mathrm{R}^3\right]}=\frac{\mathrm{ML}^2 \mathrm{~T}^{-2}}{\mathrm{~L}^3}=\mathrm{ML}^{-1} \mathrm{~T}^{-2}\end{aligned}$

</details>

---

### Q38. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Given below are two statements :
Statement (I) : Dimensions of specific heat is $\left[\mathrm{L}^2 \mathrm{~T}^{-2} \mathrm{~K}^{-1}\right]$.
Statement (II) : Dimensions of gas constant is $\left[\mathrm{M} \mathrm{L}^2 \mathrm{~T}^{-1} \mathrm{~K}^{-1}\right]$.
In the light of the above statements, choose the most appropriate answer from the options given below.

**Options:**

- **(A)** Both statement (I) and statement (II) are correct
- **(B)** Statement (I) is correct but statement (II) is incorrect
- **(C)** Both statement (I) and statement (II) are incorrect Statement (I) is incorrect but statement (II) is correct
- **(D)** Statement (I) is incorrect but statement (II) is correct

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement (I) is correct but statement (II) is incorrect**

**Detailed Solution:**

$\begin{aligned}
& \Delta \mathrm{Q}=\mathrm{mS} \Delta \mathrm{T} \\
& \mathbf{s}=\frac{\Delta \mathrm{Q}}{\mathrm{m} \Delta \mathrm{T}} \\
& {[\mathrm{s}]=\left[\frac{\mathrm{ML}^2 \mathrm{~T}^{-2}}{\mathrm{MK}}\right]} \\
& {[\mathrm{s}]=\left[\mathrm{L}^2 \mathrm{~T}^{-2} \mathrm{~K}^{-1}\right]}
\end{aligned}$
Statement-(I) is correct
$\begin{aligned}
& \mathrm{PV}=\mathrm{nRT} \Rightarrow \mathrm{R}=\frac{\mathrm{PV}}{\mathrm{nT}} \\
& {[\mathrm{R}]=\frac{\left[\mathrm{ML}^{-1} \mathrm{~T}^{-2}\right]\left[\mathrm{L}^3\right]}{[\mathrm{mol}][\mathrm{K}]}} \\
& {[\mathrm{R}]=\left[\mathrm{ML}^2 \mathrm{~T}^{-2} \mathrm{~mol}^{-1} \mathrm{~K}^{-1}\right]}
\end{aligned}$
Statement-II is incorrect

</details>

---

### Q39. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Match List I with List II
$\begin{array}{|l|l|r|l|}
\hline \text{ LIST I } & \text{ LIST II } \\
\hline \text{A.} & \text{Torque} & \text{I.} & {\left[M^1 L^1 T^{-2} A^{-2}\right]} \\
\hline \text{B.} & \text{Magnetic field} & \text{II.} & {\left[L^2 A^1\right]} \\
\hline \text{C.} & \text{Magnetic moment} & \text{III.} & {\left[M^1 T^{-2} A^{-1}\right]} \\
\hline \text{D.} & \text{Permeability of free space} & \text{IV.} & {\left[M^1 L^2 T^{-2}\right]} \\
\hline
\end{array}$
Choose the correct answer from the options given below:

**Options:**

- **(A)** A-III, B-I, C-II, D-IV
- **(B)** A-IV, B-II, C-III, D-I
- **(C)** A-IV, B-III, C-II, D-I
- **(D)** A-I, B-III, C-II, D-IV

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A-IV, B-III, C-II, D-I**

**Detailed Solution:**

$\begin{aligned} & {[\vec{\tau}]=[\overrightarrow{\mathrm{r}} \times \overrightarrow{\mathrm{F}}]=\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right]} \\ & {[\mathrm{F}]=[\mathrm{qVB}]} \\ & \Rightarrow \mathrm{B}=\left(\frac{\mathrm{F}}{\mathrm{qV}}\right)=\left[\frac{\mathrm{MLT}^{-2}}{\mathrm{ATLT}^{-1}}\right]=\left[\mathrm{MA}^{-1} \mathrm{~T}^{-2}\right] \\ & {[\mathrm{M}]=[\mathrm{I} \times \mathrm{A}]=\left[\mathrm{AL}^2\right]} \\ & \mathrm{B}=\frac{\mu_0}{4 \pi} \frac{\mathrm{Idl} \sin \theta}{\mathrm{r}^2} \\ & \Rightarrow[\mu]=\left[\frac{\mathrm{Br}^2}{\mathrm{Idl}}\right]=\left[\frac{\mathrm{MT}^{-2} \mathrm{~A}^{-1} \times \mathrm{L}^2}{\mathrm{AL}}\right] \\ & =\left[\mathrm{MLT}^{-2} \mathrm{~A}^{-2}\right]\end{aligned}$

</details>

---

### Q40. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

What is the dimensional formula of $a b^{-1}$ in the equation $\left(\mathrm{P}+\frac{\mathrm{a}}{\mathrm{V}^2}\right)(\mathrm{V}-\mathrm{b})=\mathrm{RT}$, where letters have their usual meaning.

**Options:**

- **(A)** $\left[\mathrm{M}^{-1} \mathrm{~L}^5 \mathrm{~T}^3\right]$
- **(B)** $\left[\mathrm{M}^6 \mathrm{~L}^7 \mathrm{~T}^4\right]$
- **(C)** $\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right]$
- **(D)** $\left[\mathrm{M}^0 \mathrm{~L}^3 \mathrm{~T}^{-2}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right]$**

**Detailed Solution:**

$\because[\mathrm{V}]=[\mathrm{b}]$
$\therefore$ Dimension of $b=\left[\mathrm{L}^3\right]$
$\begin{aligned}
& \&[\mathrm{P}]=\left[\frac{\mathrm{a}}{\mathrm{V}^2}\right] \\
& {[\mathrm{a}]=\left[\mathrm{PV}^2\right]=\left[\mathrm{ML}^{-1} \mathrm{~T}^{-2}\right]\left[\mathrm{L}^6\right]}
\end{aligned}$
Dimension of $\mathrm{a}=\left[\mathrm{ML}^5 \mathrm{~T}^{-2}\right]$
$\therefore \mathrm{ab}^{-1}=\frac{\left[\mathrm{ML}^5 \mathrm{~T}^{-2}\right]}{\left[\mathrm{L}^3\right]}=\left[\mathrm{ML}^2 \mathrm{~T}^{-2}\right]$

</details>

---

### Q41. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{G}$ be the gravitational constant and $\mathrm{u}$ be the energy density then which of the following quantity have the dimensions as that of the $\sqrt{\mathrm{uG}}$ :

**Options:**

- **(A)** pressure gradient per unit mass
- **(B)** Gravitational potential
- **(C)** Energy per unit mass
- **(D)** Force per unit mass

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Force per unit mass**

**Detailed Solution:**

$\begin{aligned}
& {[\mathrm{uG}]=\left[\left(\mathrm{M}^1 \mathrm{~L}^{-1} \mathrm{~T}^{-2}\right)\left(\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}\right)\right]} \\
& {[\mathrm{uG}]=\left[\mathrm{M}^0 \mathrm{~L}^2 \mathrm{~T}^{-4}\right]} \\
& {[\sqrt{\mathrm{uG}}]=\left[\mathrm{L}^1 \mathrm{~T}^{-2}\right]}
\end{aligned}$

</details>

---

### Q42. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Applying the principle of homogeneity of dimensions, determine which one is correct,
where $T$ is time period, $G$ is gravitational constant, $M$ is mass, $r$ is radius of orbit.

**Options:**

- **(A)** $T^2=\frac{4 \pi^2 r^2}{G M}$
- **(B)** $T^2=\frac{4 \pi^2 r}{G M^2}$
- **(C)** $T^2=\frac{4 \pi^2 r^3}{G M}$
- **(D)** $T^2=4 \pi^2 r^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $T^2=\frac{4 \pi^2 r^3}{G M}$**

**Detailed Solution:**

According to principle of homogeneity dimension of LHS should be equal to dimensions of RHS so option (3) is correct.
$\begin{aligned}
& \mathrm{T}^2=\frac{4 \pi^2 \mathrm{r}^3}{\mathrm{GM}} \\
& {\left[\mathrm{T}^2\right]=\frac{\left[\mathrm{L}^3\right]}{\left[\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}\right][\mathrm{M}]}}
\end{aligned}$
(Dimension of $\mathrm{G}$ is $\left[\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}\right]$ )
$\left[\mathrm{T}^2\right]=\frac{\left[\mathrm{L}^3\right]}{\left[\mathrm{L}^3 \mathrm{~T}^{-2}\right]}=\left[\mathrm{T}^2\right]$

</details>

---

### Q43. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The equation of stationary wave is :
$y=2 a \sin \left(\frac{2 \pi n t}{\lambda}\right) \cos \left(\frac{2 \pi x}{\lambda}\right) \text {. }$
Which of the following is NOT correct :

**Options:**

- **(A)** The dimensions of $n / \lambda$ is [T]
- **(B)** The dimensions of $\mathrm{n}$ is $\left[\mathrm{LT}^{-1}\right]$
- **(C)** The dimensions of $x$ is [L]
- **(D)** The dimensions of $\mathrm{nt}$ is [L]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) The dimensions of $n / \lambda$ is [T]**

**Detailed Solution:**

Comparing the given equation with standard equation of standing $\frac{2 \pi n}{\lambda}=\omega \& \frac{2 \pi}{\lambda}=k$
$\begin{aligned}
& {\left[\frac{\mathrm{n}}{\lambda}\right]=[\omega]=\mathrm{T}^{-1}} \\
& {[\mathrm{nt}]=[\lambda]=\mathrm{L}} \\
& {[\mathrm{n}]=[\lambda \omega]=\mathrm{LT}^{-1}} \\
& {[\mathrm{x}]=[\lambda]=\mathrm{L}}
\end{aligned}$

</details>

---

### Q44. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The dimensional formula of angular impulse is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">M</mi><mo> </mo><msup><mi mathvariant="normal">L</mi><mrow><mo>–</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo> </mo><mo>–</mo><mn>1</mn></mrow></msup><mo>]</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">M</mi><mo> </mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo> </mo><mi mathvariant="normal">T</mi><msup><mo> </mo><mrow><mo>–</mo><mn>2</mn></mrow></msup><mo> </mo><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">M</mi><mo> </mo><mi mathvariant="normal">L</mi><mo> </mo><mi mathvariant="normal">T</mi><msup><mo> </mo><mrow><mo>–</mo><mn>1</mn></mrow></msup><mo>]</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">M</mi><mo> </mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo> </mo><mi mathvariant="normal">T</mi><msup><mo> </mo><mrow><mo>–</mo><mn>1</mn></mrow></msup><mo> </mo><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">M</mi><mo> </mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo> </mo><mi mathvariant="normal">T</mi><msup><mo> </mo><mrow><mo>–</mo><mn>1</mn></mrow></msup><mo> </mo><mo>]</mo></math>**

**Detailed Solution:**

<p>Angular impulse = change in angular momentum.</p><p>[Angular impulse] = [Angular momentum] <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>[</mo><mi>m</mi><mi>v</mi><mi>r</mi><mo>]</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>[</mo><mi mathvariant="normal">M</mi><mo> </mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo> </mo><mi mathvariant="normal">T</mi><msup><mo> </mo><mrow><mo>–</mo><mn>1</mn></mrow></msup><mo> </mo><mo>]</mo></math></p>

</details>

---

### Q45. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider two physical quantities <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> related to each other as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mi>B</mi><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mi>A</mi><mi>t</mi></mrow></mfrac></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>,</mo><mo> </mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> have dimensions of energy, length and time respectively. The dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>L</mi><mrow><mo>−</mo><mn>2</mn></mrow></msup><msup><mi>M</mi><mn>1</mn></msup><msup><mi>T</mi><mn>0</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>L</mi><mn>2</mn></msup><msup><mi>M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mn>1</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>L</mi><mrow><mo>−</mo><mn>2</mn></mrow></msup><msup><mi>M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mn>1</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>L</mi><mn>0</mn></msup><msup><mi>M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mn>1</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>L</mi><mn>2</mn></msup><msup><mi>M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mn>1</mn></msup></math>**

**Detailed Solution:**

<p>From the dimensional checking of the equation, we can say the dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>B</mi></mfenced><mo>=</mo><mfenced close="]" open="["><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>=</mo><mfenced close="]" open="["><msup><mi>L</mi><mn>2</mn></msup></mfenced></math></p><p>And dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>A</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><msup><mi>x</mi><mn>2</mn></msup></mfenced><mfenced close="]" open="["><mrow><mi>t</mi><mi>E</mi></mrow></mfenced></mfrac><mo>=</mo><mfrac><mfenced close="]" open="["><msup><mi>L</mi><mn>2</mn></msup></mfenced><mrow><mfenced close="]" open="["><mi>T</mi></mfenced><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>−</mo><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>T</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup></mrow></mfenced></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>A</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>M</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>T</mi></mrow></mfenced></math></p><p>Required value, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>A</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>L</mi><mn>2</mn></msup><msup><mi>M</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mn>1</mn></msup></mrow></mfenced></math></p>

</details>

---

### Q46. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A force is represented by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo></math> distance and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo></math> time. The dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>b</mi><mn>2</mn></msup><mi>a</mi></mfrac></math> are :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mi>L</mi><mn>3</mn></msup><mo> </mo><mi>T</mi><msup><mo> </mo><mrow><mo>–</mo><mn>3</mn></mrow></msup><mo>]</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>–</mo><mn>2</mn></mrow></msup><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mi>L</mi><mrow><mo>–</mo><mn>1</mn></mrow></msup><mo> </mo><msup><mi>T</mi><mrow><mo>–</mo><mn>1</mn></mrow></msup><mo>]</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><mo> </mo><msup><mi>T</mi><mrow><mo>–</mo><mn>3</mn></mrow></msup><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mi>L</mi><mn>3</mn></msup><mo> </mo><mi>T</mi><msup><mo> </mo><mrow><mo>–</mo><mn>3</mn></mrow></msup><mo>]</mo></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><msup><mi>t</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p>Dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>a</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>F</mi></mfenced><mfenced close="]" open="["><msup><mi>x</mi><mn>2</mn></msup></mfenced></mfrac><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><msup><mi>L</mi><mn>2</mn></msup></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>M</mi><mn>1</mn></msup><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>b</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>F</mi></mfenced><mfenced close="]" open="["><msup><mi>t</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></msup></mfenced></mfrac><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><msup><mi>T</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></msup></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>M</mi><mn>1</mn></msup><msup><mi>L</mi><mn>1</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></msup></mrow></mfenced></math></p><p>Required value, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><msup><mi>b</mi><mn>2</mn></msup><mi>a</mi></mfrac></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><msup><mi>M</mi><mn>2</mn></msup><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><mrow><msup><mi>M</mi><mn>1</mn></msup><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>M</mi><mn>1</mn></msup><msup><mi>L</mi><mn>3</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q47. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If mass is written as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mi>k</mi><msup><mi>c</mi><mi>P</mi></msup><msup><mi>G</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo> </mo><msup><mi>h</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> will be : (Constants have their usual meaning with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> a dimensionless constant)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo mathvariant="italic">=</mo><mi>k</mi><msup><mi>c</mi><mi>P</mi></msup><msup><mi>G</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo mathvariant="italic"> </mo><msup><mi>h</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math></p><p>Writing dimensions on both sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mo> </mo><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced><mo>=</mo><msup><mfenced close="]" open="["><msup><mi>LT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mi mathvariant="normal">P</mi></msup><msup><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo> </mo><msup><mi mathvariant="normal">L</mi><mn>3</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math></p><p>By comparing exponent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> on both the sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mi>P</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mspace linebreak="newline"></mspace><mo>⇒</mo><mi>P</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q48. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Match List-I with List-II. </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="center left center left" columnlines="solid" frame="solid" rowlines="solid"><mtr><mtd></mtd><mtd><mtext> List-I </mtext></mtd><mtd></mtd><mtd><mtext> List-II </mtext></mtd></mtr><mtr><mtd><mtext> A. </mtext></mtd><mtd><mtext> Coefficient of viscosity </mtext></mtd><mtd><mtext> I. </mtext></mtd><mtd><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mtd></mtr><mtr><mtd><mtext> B. </mtext></mtd><mtd><mtext> Surface Tension </mtext></mtd><mtd><mtext> II. </mtext></mtd><mtd><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mtd></mtr><mtr><mtd><mtext> C. </mtext></mtd><mtd><mtext> Angular momentum </mtext></mtd><mtd><mtext> III. </mtext></mtd><mtd><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mtd></mtr><mtr><mtd><mtext> D. </mtext></mtd><mtd><mtext> Rotational kinetic energy </mtext></mtd><mtd><mtext> IV. </mtext></mtd><mtd><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>0</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mtd></mtr></mtable></math></p>

**Options:**

- **(A)** A-II, B-I, C-IV, D-III
- **(B)** A-I, B-II, C-III, D-IV
- **(C)** A-III, B-IV, C-II, D-I
- **(D)** A-IV, B-III, C-II, D-I

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A-III, B-IV, C-II, D-I**

**Detailed Solution:**

<p>Viscous force is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>η</mi><mi>A</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac></math>.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mo>=</mo><mi>η</mi><mfenced close="]" open="["><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mfenced><mfenced close="]" open="["><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>η</mi><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>Surface tension is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mi>T</mi><mo>=</mo><mfrac><mi>F</mi><mi>ℓ</mi></mfrac></math>.</p><p>Hence, dimension will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="]" open="["><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mrow><mo>[</mo><mi mathvariant="normal">L</mi><mo>]</mo></mrow></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Angular momentum, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mi>m</mi><mi>v</mi><mi>r</mi><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>Rotational kinetic energy, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>.</mo><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>I</mi><msup><mi>ω</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q49. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The equation of state of a real gas is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>P</mi><mo>+</mo><mfrac><mi>a</mi><msup><mi>V</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>(</mo><mi>V</mi><mo>-</mo><mi>b</mi><mo>)</mo><mo>=</mo><mi>R</mi><mi>T</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo><mo> </mo><mi>V</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> are pressure, volume and temperature respectively and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is the universal gas constant. The dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mfrac></math> is similar to that of :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mi>T</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mpadded><mi>R</mi></mpadded></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>**

**Detailed Solution:**

<p>From the dimensional analysis, it follows that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">P</mi><mo>]</mo><mo>=</mo><mfenced close="]" open="["><mfrac><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">V</mi><mn>2</mn></msup></mfrac></mfenced><mspace linebreak="newline"></mspace><mo>⇒</mo><mo>[</mo><mi mathvariant="normal">a</mi><mo>]</mo><mo>=</mo><mfenced close="]" open="["><msup><mi>PV</mi><mn>2</mn></msup></mfenced><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">V</mi><mo>]</mo><mo>=</mo><mo>[</mo><mi mathvariant="normal">b</mi><mo>]</mo></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfenced close="]" open="["><mfrac><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mfrac></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mfenced close="]" open="["><msup><mi>PV</mi><mn>2</mn></msup></mfenced><mfenced close="]" open="["><msup><mi mathvariant="normal">V</mi><mn>2</mn></msup></mfenced></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mrow><mo>[</mo><mi mathvariant="normal">P</mi><mo>]</mo></mrow></mtd></mtr></mtable></math></p>

</details>

---

### Q50. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Given below are two statements:</p><p>Statement (I) : Planck's constant and angular momentum have the same dimensions.</p><p>Statement (II) : Linear momentum and moment of force have the same dimensions.</p><p>In light of the above statements, choose the correct answer from the options given below :</p>

**Options:**

- **(A)** Statement I is true but Statement II is false
- **(B)** Both Statement I and Statement II are false
- **(C)** Both Statement I and Statement II are true
- **(D)** Statement I is false but Statement II is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement I is true but Statement II is false**

**Detailed Solution:**

<p>The dimensions of the required quantities can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mi>h</mi><mi>ν</mi><mspace linebreak="newline"></mspace><mo>⇒</mo><mfenced close="]" open="["><mi>h</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>E</mi></mfenced><mfenced close="]" open="["><mi>ν</mi></mfenced></mfrac><mspace linebreak="newline"></mspace><mo>⇒</mo><mo>[</mo><mi>h</mi><mo>]</mo><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mo>[</mo><mi>L</mi><mo>]</mo></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mrow><mi>m</mi><mi>v</mi><mi>r</mi></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mi mathvariant="normal">M</mi></mfenced><mfenced close="]" open="["><msup><mi>LT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mfenced close="]" open="["><mi mathvariant="normal">L</mi></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mo>[</mo><mi>p</mi><mo>]</mo></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mrow><mi>m</mi><mi>v</mi></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mi mathvariant="normal">M</mi></mfenced><mfenced close="]" open="["><msup><mi>LT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>1</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mo>[</mo><mi>τ</mi><mo>]</mo></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mrow><mi>F</mi><mi>r</mi></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mfenced close="]" open="["><mi mathvariant="normal">L</mi></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo> </mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mtd></mtr></mtable></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math>  is Planck's constant, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> is angular momentum, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is linear momentum and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>τ</mi></math> is moment of force.</p><p>From the above analysis, it can be concluded that Statement I is true, but statement II is false.</p>

</details>

---

### Q51. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The speed of a wave produced in water is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#957;</mi><mo>=</mo><msup><mi>&#955;</mi><mi>a</mi></msup><msup><mi>g</mi><mi>b</mi></msup><msup><mi>&#961;</mi><mi>c</mi></msup></math>. Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mi>g</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi></math> are wavelength of wave, acceleration due to gravity and density of water respectively. The values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> respectively, are

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>The dimensional form of velocity can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>v</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>&#955;</mi><mi>a</mi></msup><msup><mi>g</mi><mi>b</mi></msup><msup><mi>&#961;</mi><mi>c</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><msup><mi>M</mi><mn>0</mn></msup><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>=</mo><msup><mfenced close="]" open="["><mi>L</mi></mfenced><mi>a</mi></msup><msup><mfenced close="]" open="["><mrow><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mi>b</mi></msup><msup><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mi>c</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math>Comparing the exponents for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>,</mo><mi>L</mi><mo>,</mo><mi>T</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>For</mi><mo>&#160;</mo><mi>M</mi><mo>,</mo><mo>&#160;</mo><mspace linebreak="newline"></mspace><msup><mi>M</mi><mi>c</mi></msup><mo>=</mo><msup><mi>M</mi><mn>0</mn></msup><mspace linebreak="newline"></mspace><mi>For</mi><mo>&#160;</mo><mi>L</mi><mo>,</mo><mspace linebreak="newline"></mspace><msup><mi>L</mi><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>3</mn><mi>c</mi></mrow></msup><mo>=</mo><msup><mi>L</mi><mn>1</mn></msup><mspace linebreak="newline"></mspace><mi>For</mi><mo>&#160;</mo><mi>T</mi><mo>,</mo><mspace linebreak="newline"></mspace><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn><mi>b</mi></mrow></msup><mo>=</mo><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo><mspace linebreak="newline"></mspace><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>3</mn><mi>c</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo><mspace linebreak="newline"></mspace><mo>-</mo><mn>2</mn><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p>From equations (i),(ii),(iii),</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p> </p></blockquote>

</details>

---

### Q52. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>In the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>X</mi><mo>+</mo><mfrac><mi>a</mi><msup><mi>Y</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>[</mo><mi>Y</mi><mo>-</mo><mi>b</mi><mo>]</mo><mo>=</mo><mi>R</mi><mi>T</mi><mo>,</mo><mo>&#160;</mo><mi>X</mi></math> is pressure, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> is volume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is universal gas constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is temperature. The physical quantity equivalent to the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>b</mi></mfrac></math> is:</p><p> </p>

**Options:**

- **(A)** Pressure gradient
- **(B)** Energy
- **(C)** Impulse
- **(D)** Coefficient of viscosity

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Energy**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mi>a</mi><msup><mi>Y</mi><mn>2</mn></msup></mfrac></math> have the same dimensions. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>b</mi></math> also have the same dimensions.</p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><msup><mi>Y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#215;</mo><msup><mi>L</mi><mn>6</mn></msup><mo>=</mo><mi>M</mi><msup><mi>L</mi><mn>5</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><msup><mi>L</mi><mn>3</mn></msup></math>.</p><p>So, the dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>b</mi></mfrac></math> is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>b</mi></mfrac><mo>=</mo><mfrac><mrow><mi>M</mi><msup><mi>L</mi><mn>5</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><msup><mi>L</mi><mn>3</mn></msup></mfrac><mo>=</mo><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>.</p><p>This is the dimensional form of energy. Hence, this is the right option.</p></blockquote>

</details>

---

### Q53. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Match List I with List II</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"> </td>			<td style="text-align: center;">List-I</td>			<td style="text-align: center;"> </td>			<td style="text-align: center;">List-II</td>		</tr>		<tr>			<td style="text-align: center;">A</td>			<td style="text-align: center;">Spring constant</td>			<td style="text-align: center;">I</td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><msup><mi>T</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo></math></td>		</tr>		<tr>			<td style="text-align: center;">B</td>			<td style="text-align: center;">Angular speed</td>			<td style="text-align: center;">II</td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mi>T</mi><mrow><mo>&#8211;</mo><mn>2</mn></mrow></msup><mo>]</mo></math></td>		</tr>		<tr>			<td style="text-align: center;">C</td>			<td style="text-align: center;">Angular momentum</td>			<td style="text-align: center;">III</td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><mo>]</mo></math></td>		</tr>		<tr>			<td style="text-align: center;">D</td>			<td style="text-align: center;">Moment of Inertia</td>			<td style="text-align: center;">IV</td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo><mo>&#160;</mo></math></td>		</tr>	</tbody></table><p>Choose the correct answer from the options given below:</p>

**Options:**

- **(A)** A-I, B-III, C-II, D-IV
- **(B)** A-IV, B-I, C-III, D-II
- **(C)** A-II, B-I, C-IV, D-III
- **(D)** A-II, B-III, C-I, D-IV

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A-II, B-I, C-IV, D-III**

**Detailed Solution:**

<blockquote><p>The formula to calculate the spring constant is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>k</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>The formula to calculate the angular speed is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mi>T</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>The formula to calculate the angular momentum is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mi>m</mi><mi>v</mi><mi>r</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p>The formula to calculate the moment of inertia is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mi>M</mi><msup><mi>R</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>Use the method of dimensional analysis to obtain the dimensions of the required quantities. From above relations, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfenced close="]" open="["><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mi>k</mi></mfenced><mfenced close="]" open="["><mi>L</mi></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>&#8658;</mo></mtd><mtd><mfenced close="]" open="["><mi>k</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd></mtd><mtd></mtd></mtr><mtr><mtd><mfenced close="]" open="["><mi>&#969;</mi></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>1</mn><mfenced close="]" open="["><mi>T</mi></mfenced></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mtd></mtr><mtr><mtd></mtd><mtd></mtd><mtd></mtd></mtr><mtr><mtd><mfenced close="]" open="["><mi>L</mi></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mi>M</mi></mfenced><mfenced close="]" open="["><mrow><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><mi>L</mi></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd></mtd><mtd></mtd></mtr><mtr><mtd><mfenced close="]" open="["><mi>I</mi></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mi>M</mi></mfenced><mfenced close="]" open="["><msup><mi>L</mi><mn>2</mn></msup></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup></mrow></mfenced></mtd></mtr></mtable></math></p></blockquote>

</details>

---

### Q54. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If force <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>F</mi><mo>)</mo></math>, velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>V</mi><mo>)</mo></math> and time <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>T</mi><mo>)</mo></math> are considered as fundamental physical quantity, then dimensional formula of density will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>F</mi><mo>&#160;</mo><msup><mi>V</mi><mn>4</mn></msup><mo>&#160;</mo><msup><mi>T</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>&#160;</mo><msup><mi>V</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mn>2</mn></msup><mo mathvariant="italic">&#160;</mo><msup><mi>V</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi>T</mi><mn>6</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>&#160;</mo><msup><mi>V</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi>T</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>&#160;</mo><msup><mi>V</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<p>The dimensional formula of force is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>The dimensional formula of velocity is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>The formula for density is </p><p> Density <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>M</mi><msup><mi>L</mi><mn>3</mn></msup></mfrac><mo>=</mo><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math></p><p>Comparing the density dimensions with the assumed fundamental quantities in the question,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>=</mo><msup><mfenced open="[" close="]"><mi>F</mi></mfenced><mi>x</mi></msup><msup><mfenced open="[" close="]"><mi>V</mi></mfenced><mi>y</mi></msup><msup><mfenced open="[" close="]"><mi>T</mi></mfenced><mi>z</mi></msup><mspace linebreak="newline"/><mo>&#8658;</mo><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>=</mo><msup><mfenced open="[" close="]"><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mi>x</mi></msup><msup><mfenced open="[" close="]"><mrow><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi>y</mi></msup><mo>[</mo><mi>T</mi><msup><mo>]</mo><mi>z</mi></msup><mspace linebreak="newline"/><mo>&#8658;</mo><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>=</mo><msup><mi>M</mi><mi>x</mi></msup><msup><mi>L</mi><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi></mrow></msup></math></p><p>Comparing the exponents,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo><mspace linebreak="newline"></mspace><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo><mspace linebreak="newline"></mspace><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p>Solving equations (i), (ii) &amp; (iii), we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>.</p><p>The dimensions of density <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>F</mi><msup><mi>V</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>.</p>

</details>

---

### Q55. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Match List I with List II<table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List I</td>			<td> </td>			<td>List II</td>		</tr>		<tr>			<td>A.</td>			<td>Torque</td>			<td>I.</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></td>		</tr>		<tr>			<td>B.</td>			<td>Stress</td>			<td>II.</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></td>		</tr>		<tr>			<td>C.</td>			<td>Pressure gradient</td>			<td>III.</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></td>		</tr>		<tr>			<td>D.</td>			<td>Coefficient of
			viscosity</td>			<td>IV.</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></td>		</tr>	</tbody></table>Choose the correct answer from the options given below :

**Options:**

- **(A)** A-II, B-I, C-IV, D-III
- **(B)** A-IV, B-II, C-III, D-I
- **(C)** A-II, B-IV, C-I, D-III
- **(D)** A-III, B-IV, C-I, D-II

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A-II, B-IV, C-I, D-III**

**Detailed Solution:**

<blockquote><p>The dimensions of the quantities are as follows.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>M</mi><mo>&#160;</mo><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mspace linebreak="newline"></mspace><mi>r</mi><mo>=</mo><mi>L</mi><mspace linebreak="newline"></mspace><mi>v</mi><mo>=</mo><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mspace linebreak="newline"></mspace><mi>A</mi><mo>=</mo><msup><mi>L</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace></math></p><p>The dimensional form of stress is same as pressure.</p><p>Torque <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math> Force <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo></math> distance<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
Stress <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mtext>&#160;Force&#160;</mtext><mtext>&#160;Area&#160;</mtext></mfrac><mo>=</mo><mi mathvariant="normal">M</mi><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
Pressure Gradient <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>d</mi><mi>p</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>ML</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#951;</mi><mo>=</mo><mfrac><mi>F</mi><mrow><mn>6</mn><mi>&#960;</mi><mi>r</mi><mi>v</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mrow><mi mathvariant="normal">L</mi><mo>&#183;</mo><msup><mi>LT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfrac><mo>=</mo><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p></blockquote>

</details>

---

### Q56. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub><msub><mi mathvariant="normal">&#949;</mi><mn>0</mn></msub></mrow></mfrac></math> should be equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">T</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<blockquote><p>The speed of light can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">c</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub><msub><mi mathvariant="normal">&#949;</mi><mn>0</mn></msub></msqrt></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Rearrange equation (1) to obtain the required quantity.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub><msub><mi mathvariant="normal">&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><msup><mi>c</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Use the method of dimensional analysis to obtain the dimension of the required quantity.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfenced close="]" open="["><mfrac><mn>1</mn><mrow><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub><msub><mi mathvariant="normal">&#949;</mi><mn>0</mn></msub></mrow></mfrac></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><msup><mfenced close="]" open="["><mrow><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mtd></mtr></mtable></math></p></blockquote>

</details>

---

### Q57. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the velocity of light <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>, universal gravitational constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math> and planck&#39;s constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> are chosen as fundamental quantities. The dimensions of mass in the new system is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>h</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>c</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>G</mi><mn>1</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mn>1</mn></msup><msup><mi>c</mi><mn>1</mn></msup><msup><mi>G</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>h</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup><msup><mi>c</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>G</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>h</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>c</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>G</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>h</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>c</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><msup><mi>G</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> is energy, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>E</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mfrac><mrow><mi>G</mi><msub><mi>m</mi><mn>1</mn></msub><msub><mi>m</mi><mn>2</mn></msub></mrow><mi>r</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>E</mi></mfenced><mfenced close="]" open="["><mi>r</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>G</mi><msub><mi>m</mi><mn>1</mn></msub><msub><mi>m</mi><mn>2</mn></msub></mrow></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mi>&#955;</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mi>&#955;</mi></mfrac></mfenced><mfenced close="]" open="["><mi>r</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>G</mi><msub><mi>m</mi><mn>1</mn></msub><msub><mi>m</mi><mn>2</mn></msub></mrow></mfenced><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><mfenced close="]" open="["><mrow><mi>h</mi><mi>c</mi></mrow></mfenced><mfenced close="]" open="["><mi>L</mi></mfenced></mfrac><mfenced close="]" open="["><mi>L</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mi>G</mi></mfenced><mfenced close="]" open="["><msup><mi>M</mi><mn>2</mn></msup></mfenced></math></p><p>(both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> have dimensions of length)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="]" open="["><msqrt><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mi>G</mi></mfrac></msqrt></mfenced><mo>=</mo><mfenced close="]" open="["><mi>M</mi></mfenced></math></p>

</details>

---

### Q58. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>P</mi><mo>+</mo><mfrac><mi>a</mi><msup><mi>V</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mfenced><mrow><mi>V</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mi>R</mi><mi>T</mi></math> represents the equation of state of some gases. Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is the pressure, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> is the volume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is the temperature and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>R</mi></math> are the constants. The physical quantity, which has dimensional formula as that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>b</mi><mn>2</mn></msup><mi>a</mi></mfrac></math> , will be :

**Options:**

- **(A)** Bulk modulus
- **(B)** Modulus of rigidity
- **(C)** Compressibility
- **(D)** Energy density

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Compressibility**

**Detailed Solution:**

<p>According to the principle of dimensional homogeneity, the dimensions of each  terms of a dimensional equation on both sides are the same.</p><p>So, dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> will be same,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>b</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mi>V</mi></mfenced></math> </p><p>And dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><msup><mi>V</mi><mn>2</mn></msup></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> will be same, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mi>a</mi><msup><mi>V</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mfenced close="]" open="["><mi>P</mi></mfenced></math></p><p>From above two relations, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mi>a</mi><msup><mi>b</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mfenced close="]" open="["><mi>P</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="]" open="["><mfrac><msup><mi>b</mi><mn>2</mn></msup><mi>a</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced close="]" open="["><mi>P</mi></mfenced></mfrac><mo>=</mo><msup><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi>M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>L</mi><mn>1</mn></msup><msup><mi>T</mi><mn>2</mn></msup></mrow></mfenced></math>  is the dimension of compressibility.</p>

</details>

---

### Q59. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Match List I with List II</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td><strong>List I</strong></td>			<td> </td>			<td><strong>List II</strong></td>		</tr>		<tr>			<td>A</td>			<td>Angular momentum</td>			<td>I</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>B</td>			<td>Torque</td>			<td>II</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>C</td>			<td>Stress</td>			<td>III</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>D</td>			<td>Pressure gradient</td>			<td>IV</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>	</tbody></table><p>Choose the correct answer from the options given below :</p>

**Options:**

- **(A)** A-I, B-IV, C-III, D-II
- **(B)** A-III, B-I, C-IV, D-II
- **(C)** A-II, B-III, C-IV, D-I
- **(D)** A-IV, B-II, C-I, D-III

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A-III, B-I, C-IV, D-II**

**Detailed Solution:**

<p>As we know, angular momentum is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>L</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>p</mi><mo>&#8594;</mo></mover><mspace linebreak="newline"/><mo>&#8658;</mo><mfenced open="[" close="]"><mi mathvariant="normal">L</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>Torque is given by, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>&#964;</mi><mo>&#8594;</mo></mover><mo>=</mo><mover><mi>r</mi><mo>&#8594;</mo></mover><mo>&#215;</mo><mover><mi>F</mi><mo>&#8594;</mo></mover><mspace linebreak="newline"/><mo>&#8658;</mo><mfenced open="[" close="]"><mi>&#964;</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><msup><mi>L</mi><mn>1</mn></msup></mfenced><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Also, Stress <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8801;</mo></math> Pressure <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>F</mi><mi>A</mi></mfrac></math></p><p>Hence, [Stress] <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Pressure Gradient <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>d</mi><mi>P</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> </p><p>Therefore, [Pressure Gradient]<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q60. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>,</mo><mo>&#160;</mo><msub><mi>X</mi><mi>L</mi></msub><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><msub><mi>X</mi><mi>C</mi></msub></math> represent resistance, inductive reactance and capacitive reactance. Then which of the following is dimensionless:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#160;</mo><msub><mi>X</mi><mi>L</mi></msub><mo>&#160;</mo><msub><mi>X</mi><mi>C</mi></msub><mo>&#160;</mo><mo>&#160;</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><msqrt><msub><mi>X</mi><mi>L</mi></msub><msub><mi>X</mi><mi>c</mi></msub></msqrt></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><mrow><msub><mi>X</mi><mi>L</mi></msub><msub><mi>X</mi><mi>c</mi></msub></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mfrac><msub><mi>X</mi><mi>L</mi></msub><msub><mi>X</mi><mi>c</mi></msub></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><msqrt><msub><mi>X</mi><mi>L</mi></msub><msub><mi>X</mi><mi>c</mi></msub></msqrt></mfrac></math>**

**Detailed Solution:**

<p>As resistance, inductive reactance and capacitive reactance have same unit ohm. So, all three have same dimension.</p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><msqrt><msub><mi>X</mi><mi>L</mi></msub><msub><mi>X</mi><mi>C</mi></msub></msqrt></mfrac></math> is dimensionless.</p>

</details>

---

### Q61. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The equation of a circle is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is the radius. If the equation is modified to change the origin other than <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo></math>, then find out the correct dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> in a new equation :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>A</mi><mi>t</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mfrac><mi>t</mi><mi>B</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup></math></p><p>The dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>[</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">T</mi><mo>]</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>[</mo><msup><mi>LT</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mi>LT</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mo>[</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">T</mi><msup><mo>&#160;</mo><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>[</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">T</mi><msup><mo>&#160;</mo><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mo>]</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>[</mo><msup><mi>LT</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo><mo>&#160;</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mo>[</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>&#160;</mo><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mo>[</mo><mi>LT</mi><mo>]</mo><mo>&#160;</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mi>LT</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mo>[</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">T</mi><msup><mo>&#160;</mo><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo></math>**

**Detailed Solution:**

<p>Principle of Homogeneity states that dimensions of each of the terms of a dimensional equation on both sides should be the same. Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>A</mi><mi>t</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mfrac><mi>t</mi><mi>B</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup></math></p><p>For first term, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>A</mi><mi>t</mi></mrow></mfenced><mo>=</mo><mfenced open="[" close="]"><mi>x</mi></mfenced><mspace linebreak="newline"/><mo>&#8658;</mo><mi>A</mi><mo>&#215;</mo><mfrac><mn>1</mn><mi>T</mi></mfrac><mo>=</mo><mi>L</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced open="[" close="]"><mi>A</mi></mfenced><mo>=</mo><msup><mi mathvariant="normal">T</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup></math></p><p>For the second term,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mfrac><mi>t</mi><mi>B</mi></mfrac></mfenced><mo>=</mo><mfenced open="[" close="]"><mi>y</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mi>T</mi><mfenced open="[" close="]"><mi>B</mi></mfenced></mrow></mfrac><mo>=</mo><mi>L</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]"><mi>B</mi></mfenced><mo>=</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q62. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Match List I with List II :</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td><strong>List-I (Physical Quantity)</strong></td>			<td> </td>			<td><strong>List-II (Dimensional Formula)</strong></td>		</tr>		<tr>			<td>A</td>			<td>Pressure gradient</td>			<td>I</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>B</td>			<td>Energy density</td>			<td>II</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>C</td>			<td>Electric Field</td>			<td>III</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td>D</td>			<td>Latent heat</td>			<td>IV</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></td>		</tr>	</tbody></table><p>Choose the correct answer from the options given below:</p>

**Options:**

- **(A)** A-III, B-II, C-I, D-IV
- **(B)** A-II, B-III, C-IV, D-I
- **(C)** A-III, B-II, C-IV, D-I
- **(D)** A-II, B-III, C-I, D-IV

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A-III, B-II, C-IV, D-I**

**Detailed Solution:**

<p>(A) Pressure gradient is stated as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>d</mo><mi>P</mi></mrow><mrow><mo>d</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>F</mi><mrow><mi>A</mi><mi>l</mi></mrow></mfrac><mo>=</mo><mfrac><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mrow><mfenced open="[" close="]"><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mfenced><mfenced open="[" close="]"><mi mathvariant="normal">L</mi></mfenced></mrow></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>   (III)</p><p>(B) Energy density is stated as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>=</mo><mfrac><mi>Energy</mi><mi>Volume</mi></mfrac><mo>=</mo><mfrac><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced open="[" close="]"><msup><mi mathvariant="normal">L</mi><mn>3</mn></msup></mfenced></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>   (II)</p><p>(C) Electric field is stated as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>Force</mi><mi>Charge</mi></mfrac><mo>=</mo><mfrac><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mfenced open="[" close="]"><mi>AT</mi></mfenced></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>   (IV)</p><p>(D) Latent heat is stated as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mfrac><mi>Heat</mi><mi>Mass</mi></mfrac><mo>=</mo><mfrac><mrow><mi>Energy</mi><mo>&#160;</mo></mrow><mi>Mass</mi></mfrac><mo>=</mo><mfrac><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced open="[" close="]"><mi mathvariant="normal">M</mi></mfenced></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>     (I)</p>

</details>

---

### Q63. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Match List I with List II</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List</td>			<td> </td>			<td>List II</td>		</tr>		<tr>			<td>A</td>			<td>Young&#39;s Modulus <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>Y</mi><mo>)</mo></math></td>			<td>I</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><msup><mi>ML</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">T</mi><msup><mo>&#160;</mo><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo></math></td>		</tr>		<tr>			<td>B</td>			<td>Co-efficient of Viscosity <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#951;</mi><mo>)</mo></math></td>			<td>II</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">T</mi><msup><mo>&#160;</mo><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>]</mo></math></td>		</tr>		<tr>			<td>C</td>			<td>Planck&#39;s Constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>h</mi><mo>)</mo></math></td>			<td>III</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><msup><mi>ML</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">T</mi><msup><mo>&#160;</mo><mrow><mo>&#8211;</mo><mn>2</mn></mrow></msup><mo>]</mo></math></td>		</tr>		<tr>			<td>D</td>			<td>Work Function <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>&#981;</mi></mfenced></math></td>			<td>IV</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>&#8211;</mo><mn>2</mn></mrow></msup><mo>]</mo></math></td>		</tr>	</tbody></table><p>Choose the correct answer from the options given below:</p>

**Options:**

- **(A)** A-II, B-III, C-IV, D-I
- **(B)** A-III, B-I, C-II, D-IV
- **(C)** A-I, B-III, C-IV, D-II
- **(D)** A-I, B-II, C-III, D-IV

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A-III, B-I, C-II, D-IV**

**Detailed Solution:**

<p>(A) Young&#39;s modulus is stated as<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Y</mi><mo>=</mo><mfrac><mi>Stress</mi><mi>Strain</mi></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mi>F</mi><mi>A</mi></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mo>&#8710;</mo><mi>l</mi></mrow><mi>l</mi></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mrow><mi>F</mi><mi>l</mi></mrow><mrow><mi>A</mi><mo>&#8710;</mo><mi>l</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mfenced open="[" close="]"><mi mathvariant="normal">L</mi></mfenced></mrow><mrow><mfenced open="[" close="]"><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mfenced><mfenced open="[" close="]"><mi mathvariant="normal">L</mi></mfenced></mrow></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>(B) Coefficient of viscosity is stated as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#951;</mi><mo>=</mo><mfrac><mi>F</mi><mrow><mn>6</mn><mi>&#960;</mi><mi>r</mi><mi>v</mi></mrow></mfrac></math>, here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math> is velocity.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>&#951;</mi></mfenced><mo>=</mo><mfrac><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mrow><mfenced open="[" close="]"><mi mathvariant="normal">L</mi></mfenced><mfenced open="[" close="]"><msup><mi>LT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mrow></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>(C) Planck&#39;s Constant is stated as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mfrac><mtext>Energy</mtext><mtext>Frequency</mtext></mfrac><mo>=</mo><mfrac><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced open="[" close="]"><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>(D) Work function has the same dimension as that of energy, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>&#981;</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Thus, A-III, B-I, C-II, D-IV</p>

</details>

---

### Q64. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>&#957;</mi></mfenced></math> of an oscillating liquid drop may depend upon radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>r</mi></mfenced></math> of the drop, density <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>&#961;</mi></mfenced></math> of liquid and the surface tension <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>s</mi></mfenced></math> of the liquid as: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#957;</mi><mo>=</mo><msup><mi>r</mi><mi>a</mi></msup><msup><mi>&#961;</mi><mi>b</mi></msup><msup><mi>s</mi><mi>c</mi></msup></math>. The values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> respectively are

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mo>,</mo><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Here, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#957;</mi><mo>=</mo><msup><mi>r</mi><mi>a</mi></msup><msup><mi>&#961;</mi><mi>b</mi></msup><msup><mi>s</mi><mi>c</mi></msup></math></p><p>Equating the dimensions of each quantity on both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>=</mo><msup><mfenced close="]" open="["><msup><mi>L</mi><mn>1</mn></msup></mfenced><mi>a</mi></msup><msup><mfenced close="]" open="["><mrow><msup><mi>M</mi><mn>1</mn></msup><msup><mi>L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mi>b</mi></msup><msup><mfenced close="]" open="["><mfrac><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mi>L</mi></mfrac></mfenced><mi>c</mi></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mi>M</mi><mrow><mi>b</mi><mo>+</mo><mi>c</mi></mrow></msup><msup><mi>L</mi><mrow><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn><mi>c</mi></mrow></msup></math></p><p>Comparing the dimensions, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>-</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo></math></p><p>Thus, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>.</p>

</details>

---

### Q65. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Match List I with List II</p><table border="1" cellpadding="1" cellspacing="1" style="width: 450px;">	<tbody>		<tr>			<td colspan="2" rowspan="1" style="text-align: center;">List I</td>			<td colspan="2" rowspan="1" style="text-align: center;">List II</td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo></math></td>			<td>Planck&#39;s constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>h</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>.</mo></math></td>			<td>Stopping potential <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>V</mi><mi>s</mi></msub></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi><mo>.</mo></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi><mo>.</mo></math></td>			<td>Work function <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>&#981;</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>III</mi><mo>.</mo></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">D</mi><mo>.</mo></math></td>			<td>Momentum <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>p</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>IV</mi><mo>.</mo></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></td>		</tr>	</tbody></table><p> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi>III</mi><mo>,</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi>II</mi><mo>,</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>IV</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi>III</mi><mo>,</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi>IV</mi><mo>,</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>II</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi>II</mi><mo>,</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi>IV</mi><mo>,</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi>III</mi><mo>,</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi mathvariant="normal">I</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi>III</mi><mo>,</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi>IV</mi><mo>,</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>II</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>-</mo><mi>III</mi><mo>,</mo><mi mathvariant="normal">B</mi><mo>-</mo><mi>IV</mi><mo>,</mo><mi mathvariant="normal">C</mi><mo>-</mo><mi mathvariant="normal">I</mi><mo>,</mo><mi mathvariant="normal">D</mi><mo>-</mo><mi>II</mi></math>**

**Detailed Solution:**

<p>The dimension of momentum is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>From de Broglie equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>h</mi><mi>p</mi></mfrac><mo>=</mo><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>h</mi><mo>]</mo><mo>=</mo><mo>[</mo><mi>p</mi><mo>]</mo><mfenced close="]" open="["><mi>&#955;</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>The stopping potential is related to maximum kinetic energy of emitted electron as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>s</mi></msub><mo>=</mo><mfrac><mrow><mi>K</mi><msub><mi>E</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub></mrow><mi>e</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><mi>AT</mi></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>From Einstein&#39;s photoelectric equation, the work function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi></math> has dimensions of energy </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>&#981;</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q66. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Given below are two statements: One is labelled as Assertion (A) and other is labelled as Reason (R)</p><p><strong>Assertion (A) :</strong> Time period of oscillation of a liquid drop depends on surface tension <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>S</mi></mfenced></math>, if density of the liquid is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi></math> and radius of the drop is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mi>K</mi><msqrt><mfrac><mrow><mi>&#961;</mi><msup><mi>r</mi><mn>3</mn></msup></mrow><msup><mi>S</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfrac></msqrt></math> is dimensionally correct, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is dimensionless.</p><p><strong>Reason (R) :</strong> Using dimensional analysis we get R.H.S. having different dimension than that of time period. In the light of above statements, choose the correct answer from the options given below.</p>

**Options:**

- **(A)** Both (A) and (R) are true and (R) is the correct explanation of (A)
- **(B)** Both (A) and (R) are true but (R) is not the correct explanation of (A)
- **(C)** (A) is true but (R) is false
- **(D)** (A) is false but (R) is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (A) is false but (R) is true**

**Detailed Solution:**

<blockquote><p>Using dimensional analysis for the given equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><mi>K</mi><msqrt><mfrac><mrow><mi>&#961;</mi><msup><mi>r</mi><mn>3</mn></msup></mrow><msup><mi>S</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfrac></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>K</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced close="]" open="["><mi>T</mi></mfenced><mfenced close="]" open="["><msup><mi>S</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>4</mn></mfrac></mstyle></msup></mfenced></mrow><mrow><mfenced close="]" open="["><msup><mi>&#961;</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></msup></mfenced><mfenced close="]" open="["><msup><mi>r</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfenced></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfenced close="]" open="["><mi>K</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced close="]" open="["><mi mathvariant="normal">T</mi></mfenced><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>4</mn></mfrac></mstyle></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mrow></msup></mrow></mfenced></mrow><mrow><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mrow></msup></mrow></mfenced><mfenced close="]" open="["><msup><mi mathvariant="normal">L</mi><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></msup></mfenced></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfenced close="]" open="["><mi>K</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></mrow></mfenced></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is not dimensionless. Hence, Assertion is false.</p><p>For dimensional validity of the given equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> can not be dimensionless. If it is dimensionless then</p><p>Dimensions of L.H.S <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8800;</mo></math> Dimensions of R.H.S</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Option (D) is correct.</p></blockquote>

</details>

---

### Q67. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Consider the efficiency of Carnot&#39;s engine is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#951;</mi><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfrac><mrow><mi>&#946;</mi><mi>x</mi></mrow><mrow><mi>k</mi><mi>T</mi></mrow></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are constants. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is temperature, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is Boltzman constant, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math> is angular displacement and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> has the dimensions of length. Then, choose the incorrect option.

**Options:**

- **(A)** Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> is same as that of force.
- **(B)** Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> is same as that of energy.
- **(C)** Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#951;</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>sin</mi><mi>&#952;</mi></math> is same as that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi></math>
- **(D)** Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is same as that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is same as that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>**

**Detailed Solution:**

<blockquote><p>Given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#951;</mi><mo>=</mo><mfrac><mrow><mi>&#945;</mi><mi>&#946;</mi></mrow><mrow><mi>sin</mi><mi>&#952;</mi></mrow></mfrac><mi>log</mi><mfenced><mfrac><mrow><mi>&#946;</mi><mi>x</mi></mrow><mrow><mi>k</mi><mi>T</mi></mrow></mfrac></mfenced></math>. Since expression inside the logarithm is dimensionless</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>k</mi><mi>T</mi></mrow></mfenced></math></p><p>Since the dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>T</mi></math> are equivalent to that of energy,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>&#946;</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><mi>k</mi><mi>T</mi></mrow></mfenced><mfenced close="]" open="["><mi>x</mi></mfenced></mfrac><mo>=</mo><mfrac><mfenced close="]" open="["><mi>E</mi></mfenced><mfenced close="]" open="["><mi>x</mi></mfenced></mfrac><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><mi mathvariant="normal">L</mi></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> has dimensions of force.</p><p>Since efficiency is a dimensionless ratio,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>&#945;</mi></mfenced><mfenced close="]" open="["><mi>&#946;</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#946;</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced close="]" open="["><mi>&#945;</mi></mfenced></mfrac></math></p><p>Therefore, dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is not same as that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>. Hence option D is incorrect statement and the answer.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="]" open="["><mi>x</mi></mfenced><mfenced close="]" open="["><mi>&#945;</mi></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><mi>&#946;</mi></mfenced><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math> has dimensions of energy.</p></blockquote>

</details>

---

### Q68. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><msup><mi>B</mi><mn>2</mn></msup><msub><mi>&#956;</mi><mn>0</mn></msub></mfrac></mfenced></math> will be</p><p>(if <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mn>0</mn></msub></math>: permeability of free space and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#160;</mo><mo>:</mo></math>magnetic field)</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>MLL</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Energy density in magnetic field is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>=</mo><mfrac><msup><mi>B</mi><mn>2</mn></msup><mrow><mn>2</mn><msub><mi>&#956;</mi><mn>0</mn></msub></mrow></mfrac></math>. Therefore, dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>B</mi><mn>2</mn></msup><msub><mi>&#956;</mi><mn>0</mn></msub></mfrac></math> will be equal to the dimensions of energy per unit volume.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><msup><mi>B</mi><mn>2</mn></msup><msub><mi>&#956;</mi><mn>0</mn></msub></mfrac></mfenced><mo>=</mo><mfenced close="]" open="["><mi>u</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><msup><mi mathvariant="normal">L</mi><mn>3</mn></msup></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p></blockquote>

</details>

---

### Q69. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An expression of energy density is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>=</mo><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mi>sin</mi><mfenced><mfrac><mrow><mi>&#945;</mi><mi>x</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></mfrac></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> are constants, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is displacement, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is Boltzmann constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> is the temperature. The dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> will be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>&#952;</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given that energy density <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi><mo>=</mo><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mi>sin</mi><mfrac><mrow><mi>&#945;</mi><mi>x</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></mfrac></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#945;</mi><mi>x</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></mfrac></math> should be dimensionless, the dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>t</mi></math> should be same.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#945;</mi></mfenced><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mi>k</mi></mfenced><mfenced close="]" open="["><mi>t</mi></mfenced><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#945;</mi></mfenced><mo>=</mo><mfrac><mrow><mfenced close="]" open="["><mi>k</mi></mfenced><mstyle displaystyle="true"><mfenced close="]" open="["><mi>t</mi></mfenced></mstyle></mrow><mfenced close="]" open="["><mi>x</mi></mfenced></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>U</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>&#945;</mi></mfenced><mfenced close="]" open="["><mi>&#946;</mi></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#946;</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>&#945;</mi></mfenced><mfenced close="]" open="["><mi>U</mi></mfenced></mfrac><mo>=</mo><mfrac><mrow><mfenced close="]" open="["><mi>k</mi></mfenced><mfenced close="]" open="["><mi>t</mi></mfenced></mrow><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mfenced close="]" open="["><mfrac><mi>E</mi><mi>V</mi></mfrac></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced close="]" open="["><mfrac><mi>E</mi><mi>t</mi></mfrac></mfenced><mfenced close="]" open="["><mi>t</mi></mfenced></mrow><mrow><mfenced close="]" open="["><mi>x</mi></mfenced><mfenced close="]" open="["><mfrac><mi>E</mi><mi>V</mi></mfrac></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#946;</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><msup><mi>L</mi><mn>3</mn></msup></mfenced><mfenced close="]" open="["><mi>L</mi></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math></p></blockquote>

</details>

---

### Q70. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following physical quantities have the same dimensions?

**Options:**

- **(A)** Electric displacement <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mover><mi mathvariant="normal">D</mi><mo>&#8594;</mo></mover></mfenced></math> and surface charge density
- **(B)** Displacement current and electric field
- **(C)** Current density and surface charge density
- **(D)** Electric potential and energy

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Electric displacement <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mover><mi mathvariant="normal">D</mi><mo>&#8594;</mo></mover></mfenced></math> and surface charge density**

**Detailed Solution:**

<blockquote><p>Electric displacement</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>D</mi><mo>&#8594;</mo></mover><mo>=</mo><msub><mi>&#1013;</mi><mn>0</mn></msub><mover><mi>E</mi><mo>&#8594;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>D</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msub><mi>&#1013;</mi><mn>0</mn></msub><mi>E</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msub><mi>&#1013;</mi><mn>0</mn></msub><mfrac><mi>&#963;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>D</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mi>&#963;</mi></mfenced></math></p><p>And surface charge density <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#963;</mi></math>.</p><p>Thus, electric displacement <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">D</mi></mfenced></math> and surface charge density have same dimension.</p></blockquote>

</details>

---

### Q71. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If momentum <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>P</mi></mfenced></math>, area <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>A</mi></mfenced></math> and time <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>T</mi></mfenced></math> are taken as fundamental quantities, then the dimensional formula for coefficient of viscosity is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>PA</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>PAT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>PA</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">T</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>PA</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>PA</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>We know, Viscosity<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>Pascal<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8208;</mo></math>second</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>&#951;</mi></mfenced><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>x</mi></msup><msup><mi>A</mi><mi>y</mi></msup><msup><mi>T</mi><mi>z</mi></msup><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>+</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi mathvariant="normal">x</mi></msup><msup><mfenced open="[" close="]"><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mfenced><mi>y</mi></msup><msup><mfenced open="[" close="]"><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>1</mn></msup></mfenced><mi>z</mi></msup><mo>=</mo><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">M</mi><mi mathvariant="normal">x</mi></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>+</mo><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">y</mi></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi>z</mi></mrow></msup><mo>=</mo><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>From above, we have </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#160;&#160;</mo><mspace linebreak="newline"/><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#160;&#160;</mo><mspace linebreak="newline"/><mo>-</mo><mi>x</mi><mo>+</mo><mi>z</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Solving above three equations, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">z</mi><mo>=</mo><mn>0</mn></math></p><p>So, Viscosity <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">P</mi><mn>1</mn></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math></p></blockquote>

</details>

---

### Q72. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In van dar Wall equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>P</mi><mo>+</mo><mfrac><mi>a</mi><msup><mi>V</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mfenced open="[" close="]"><mrow><mi>V</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mi>R</mi><mi>T</mi><mo>;</mo><mo>&#160;</mo><mi>P</mi></math> is pressure, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> is volume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is universal gas constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is temperature. The ratio of constants <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>b</mi></mfrac></math> is dimensionally equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>P</mi><mi>V</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>V</mi><mi>P</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msup><mi>V</mi><mn>3</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>V</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>P</mi><mo>+</mo><mfrac><mi>a</mi><msup><mi>V</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mfenced><mrow><mi>V</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mi>R</mi><mi>T</mi></math></p><p>Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> should be equal to dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math>. Similarly, dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> will be equal to dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msup><mi>V</mi><mn>2</mn></msup></math>.</p><p>Therefore, dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mi>a</mi><mi>b</mi></mfrac></mfenced><mo>=</mo><mfenced close="]" open="["><mfrac><mrow><mi>P</mi><msup><mi>V</mi><mn>2</mn></msup></mrow><mi>V</mi></mfrac></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>P</mi><mi>V</mi></mrow></mfenced></math>. </p>

</details>

---

### Q73. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p><strong>Assertion A:</strong> Product of Pressure <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>P</mi></mfenced></math> and time <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>t</mi></mfenced></math> has the same dimension as that of coefficient of viscosity.</p><p><strong>Reason:</strong> Coefficient of viscosity <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#160;</mo><mi>Force</mi><mo>&#160;</mo></mrow><mrow><mo>&#160;</mo><mi>Velocity</mi><mo>&#160;</mo><mi>gradient</mi><mo>&#160;</mo></mrow></mfrac></math></p>

**Options:**

- **(A)** Both A and R true, and R is correct explanation of A.
- **(B)** Both A and R are true but R is NOT the correct explanation of A.
- **(C)** A is true but R is false.
- **(D)** A is false but R is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A is true but R is false.**

**Detailed Solution:**

<p>Viscous force is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>&#951;</mi><mi>A</mi><mfenced><mfrac><mrow><mo>d</mo><mi>v</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></mfenced></math>, here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is area and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>d</mo><mi>v</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></math> is velocity gradient.</p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#951;</mi><mo>=</mo><mfrac><mi>F</mi><mrow><mi>A</mi><mfenced><mstyle displaystyle="true"><mfrac><mrow><mo>d</mo><mi>v</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></mstyle></mfenced></mrow></mfrac></math>.</p><p>Now,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>t</mi><mo>=</mo><mfrac><mi>F</mi><mi>A</mi></mfrac><mi>t</mi><mo>=</mo><mi>&#951;</mi><mfenced><mfrac><mrow><mo>d</mo><mi>v</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac></mfenced><mi>t</mi></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>P</mi><mi>t</mi></mrow></mfenced><mo>=</mo><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfenced close="]" open="["><mi>&#951;</mi></mfenced></math></p><p>Thus, assertion is true but reason is false.</p>

</details>

---

### Q74. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>,</mo><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> are the self inductance, capacitance and resistance respectively, which of the following does not have the dimension of time?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>L</mi><mi>C</mi></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mi>R</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>R</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mi>C</mi></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mi>C</mi></mfrac></math>**

**Detailed Solution:**

<p>Dimensions of L is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>A</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Dimensions of C is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi>M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>L</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>T</mi><mn>4</mn></msup><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced></math></p><p>And dimensions of R is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi>A</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Clearly, dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>L</mi><mi>C</mi></msqrt><mo>=</mo><mfenced close="]" open="["><mi>T</mi></mfenced></math>,</p><p>Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mi>R</mi></mfrac><mo>=</mo><mfenced close="]" open="["><mi>T</mi></mfenced></math>,</p><p>Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>R</mi><mo>=</mo><mfenced close="]" open="["><mi>T</mi></mfenced></math> and</p><p>Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>L</mi><mi>C</mi></mfrac><mo>=</mo><mfrac><mfenced open="[" close="]"><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>A</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced open="[" close="]"><mrow><msup><mi>M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>L</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>T</mi><mn>4</mn></msup><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi>M</mi><mn>2</mn></msup><msup><mi>L</mi><mn>4</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup><msup><mi>A</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfenced><mo>=</mo><msup><mi>R</mi><mn>2</mn></msup></math></p>

</details>

---

### Q75. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The SI unit of a physical quantity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Pascal</mi><mo>&#8208;</mo><mi>sec</mi></math>. The dimensional formula of this quantity will be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>L</mi><mn>3</mn></msup><msup><mi>T</mi><mn>0</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<p>Unit of Pascal is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>.</p><p>So, dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Pascal</mi><mo>&#8208;</mo><mi>sec</mi></math> is </p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><mi mathvariant="normal">s</mi></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><msup><mi>L</mi><mn>2</mn></msup></mfrac><mo>&#215;</mo><mi>T</mi><mo>=</mo><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> </p>

</details>

---

### Q76. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The dimension of mutual inductance is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<p>The formula for mutual inductance is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#949;</mi><mo>=</mo><mi>M</mi><mfrac><mrow><mi>d</mi><mi>I</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>&#160;</mo><mo>&#8658;</mo><mi>M</mi><mo>=</mo><mfrac><mi>&#949;</mi><mfenced><mstyle displaystyle="true"><mfrac><mrow><mi>d</mi><mi>I</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mstyle></mfenced></mfrac></math></p><p>Dimension of emf or voltage is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mi mathvariant="normal">M</mi><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>,
Dimension of current is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi mathvariant="normal">A</mi></mfenced></math>,
Dimension of time <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi mathvariant="normal">T</mi></mfenced></math>.</p><p>Therefore, the dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mrow><mfenced close="]" open="["><mi mathvariant="normal">A</mi></mfenced><msup><mfenced close="]" open="["><mi mathvariant="normal">T</mi></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q77. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An expression for a dimensionless quantity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>k</mi><mi>T</mi></mrow><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfrac></mfenced></math>; where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are constants, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is distance; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is Boltzmann constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is the temperature. Then the dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> will be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac><mi>ln</mi><mfenced><mfrac><mrow><mi>k</mi><mi>T</mi></mrow><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfrac></mfenced></math></p><p>We know that expression inside log is dimensionless.</p><p>Therefore,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mfenced close="]" open="["><mfrac><mrow><mi>k</mi><mi>T</mi></mrow><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfrac></mfenced></math> is dimensionless</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#946;</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mfrac><mrow><mi>k</mi><mi>T</mi></mrow><mi>x</mi></mfrac></mfenced><mo>=</mo><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">K</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#215;</mo><mi mathvariant="normal">K</mi><mo>&#215;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is dimensionless <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced close="]" open="["><mi>p</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mfrac><mi>&#945;</mi><mi>&#946;</mi></mfrac></mfenced><mo>=</mo><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#945;</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mi>&#946;</mi></mfenced></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#945;</mi></mfenced><mo>=</mo><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p>

</details>

---

### Q78. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Identify the pair of physical quantities that have same dimensions:

**Options:**

- **(A)** Velocity gradient and decay constant
- **(B)** Angular frequency and angular momentum
- **(C)** Wave number and Avogadro number
- **(D)** Wein&#39;s constant and Stephan&#39;s constant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Velocity gradient and decay constant**

**Detailed Solution:**

<p>Decay constant is measured per unit time, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><msup><mi>s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>So, its dimension is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>&#955;</mi></mfenced><mo>=</mo><mfenced close="]" open="["><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math></p><p>We know velocity gradient is defined as rate of change in velocity per unit of distance. So, dimension of velocity gradient is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><msup><mi>L</mi><mn>1</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><msup><mi>L</mi><mn>1</mn></msup></mfenced></mfrac><mo>=</mo><mfenced close="]" open="["><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math></p>

</details>

---

### Q79. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Identify the pair of physical quantities which have different dimensions:

**Options:**

- **(A)** Wave number and Rydberg&#39;s constant
- **(B)** Stress and Coefficient of elasticity
- **(C)** Coercivity and  Magnetisation
- **(D)** Specific heat capacity and Latent heat

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Specific heat capacity and Latent heat**

**Detailed Solution:**

The SI unit of specific heat is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi>kg</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">K</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> and the SI unit of latent heat is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi>kg</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. We can see that the quantities in option <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> have different dimensions.

</details>

---

### Q80. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>V</mi></mfenced></math> time <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>T</mi></mfenced></math> and force <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>F</mi></mfenced></math> are chosen as the base quantities, the dimensions of the mass will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>F</mi><mi>V</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>F</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>V</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>F</mi><msup><mi>T</mi><mn>2</mn></msup><mo>&#160;</mo><mi>V</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>F</mi><mi>T</mi><msup><mi>V</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>F</mi><mi>T</mi><msup><mi>V</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mo>]</mo><mn>1</mn></msup><mo>=</mo><mo>[</mo><mi>V</mi><msup><mo>]</mo><mi>a</mi></msup><mo>[</mo><mi>T</mi><msup><mo>]</mo><mi>b</mi></msup><mo>[</mo><mi>F</mi><msup><mo>]</mo><mi>c</mi></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mo>]</mo><mn>1</mn></msup><mo>=</mo><msup><mfenced close="]" open="["><mrow><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi>a</mi></msup><mo>[</mo><mi>T</mi><msup><mo>]</mo><mi>b</mi></msup><msup><mfenced close="]" open="["><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mi>c</mi></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><msup><mo>]</mo><mn>1</mn></msup><mo>=</mo><mo>[</mo><mi>M</mi><msup><mo>]</mo><mi>c</mi></msup><mo>[</mo><mi>L</mi><msup><mo>]</mo><mrow><mi>a</mi><mo>+</mo><mi>c</mi></mrow></msup><mo>[</mo><mi>T</mi><msup><mo>]</mo><mrow><mo>-</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>c</mi></mrow></msup></math>
Thus,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>c</mi><mo>=</mo><mn>1</mn><mo>,</mo></mtd><mtd><mi>a</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mtext>and</mtext></mtd><mtd><mi>b</mi><mo>-</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>0</mn></mtd></mtr><mtr><mtd/><mtd><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>1</mn></mtd><mtd><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>1</mn></mtd></mtr></mtable></math>
Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>M</mi><mo>]</mo><mo>=</mo><mo>[</mo><mi>V</mi><msup><mo>]</mo><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>[</mo><mo>&#160;</mo><mi>T</mi><msup><mo>]</mo><mn>1</mn></msup><mo>[</mo><mo>&#160;</mo><mi>F</mi><msup><mo>]</mo><mn>1</mn></msup></math></p>

</details>

---

### Q81. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Match List - I with List - II.<table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List - I</td>			<td> </td>			<td>List - II</td>		</tr>		<tr>			<td>a</td>			<td>Torque</td>			<td>i</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></td>		</tr>		<tr>			<td>b</td>			<td>Impulse</td>			<td>ii</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></td>		</tr>		<tr>			<td>c</td>			<td>Tension</td>			<td>iii</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></td>		</tr>		<tr>			<td>d</td>			<td>Surface Tension</td>			<td>iv</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></td>		</tr>	</tbody></table><p>Choose the most appropriate answer from the option given below :</p>

**Options:**

- **(A)** (a)-(iii), (b)-(iv), (c)-(i), (d)-(ii)
- **(B)** (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)
- **(C)** (a)-(i), (b)-(iii), (c)-(iv), (d)-(ii)
- **(D)** (a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)**

**Detailed Solution:**

The torque is defined as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#964;</mi><mo>=</mo><mo>&#8869;</mo><mi>r</mi><mi>F</mi><mi>sin</mi><mi>&#952;</mi><mo>=</mo><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>, the formula of impulse, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8710;</mo><mi>p</mi><mo>=</mo><msup><mi>MLT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> and tension, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> and the formula of surface tension is defined as force per unit length.<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo>=</mo><mfrac><mi>F</mi><mi>l</mi></mfrac><mo>=</mo><mfrac><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mi>L</mi></mfrac><mo>=</mo><mi>M</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>.

</details>

---

### Q82. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Which of the following equations is dimensionally incorrect?</p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo></math>time, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo></math>height, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo>=</mo></math>surface tension, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo></math>angle, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi><mo>=</mo></math>density <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>,</mo><mi>a</mi><mo>,</mo><mi>r</mi><mo>=</mo></math>radius, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>=</mo></math> the acceleration due to gravity, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo></math>volume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo></math>pressure, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi><mo>=</mo></math>work done, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#964;</mi><mo>=</mo></math>torque, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#1013;</mi><mo>=</mo></math>permittivity, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo></math>electric field, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>=</mo></math>current density, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo></math>length.</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi><mo>=</mo><mi>&#964;</mi><mi>&#952;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mi>p</mi><msup><mi>a</mi><mn>4</mn></msup></mrow><mrow><mn>8</mn><mi>&#951;</mi><mi>L</mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>scos</mi><mi>&#952;</mi></mrow><mrow><mi>&#961;</mi><mi>r</mi><mi>g</mi></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi><mo>=</mo><mi>&#1013;</mi><mfrac><mrow><mo>&#8706;</mo><mi>E</mi></mrow><mrow><mo>&#8706;</mo><mi>t</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mi>p</mi><msup><mi>a</mi><mn>4</mn></msup></mrow><mrow><mn>8</mn><mi>&#951;</mi><mi>L</mi></mrow></mfrac></math>**

**Detailed Solution:**

Dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#960;</mi><mi>p</mi><msup><mi>a</mi><mn>4</mn></msup></mrow><mrow><mn>8</mn><mi>&#951;</mi><mi>L</mi></mrow></mfrac></math>(volume flow rate) is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">L</mi><mn>3</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math>.

</details>

---

### Q83. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If force (F), length (L) and time (T) are taken as the fundamental quantities. Then what will be the dimension of density:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>FL</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>2</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>FL</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>3</mn></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>FL</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>2</mn></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi>FL</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>2</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>FL</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>2</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">d</mi><mo>&#8733;</mo><msup><mi>F</mi><mi mathvariant="normal">a</mi></msup><msup><mi mathvariant="normal">L</mi><mi mathvariant="normal">b</mi></msup><msup><mi mathvariant="normal">T</mi><mi mathvariant="normal">c</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>M</mi><msup><mi>L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mo>=</mo><msup><mfenced open="[" close="]"><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mi>a</mi></msup><mfenced open="[" close="]"><msup><mi>L</mi><mi>b</mi></msup></mfenced><mfenced open="[" close="]"><mrow><mi>T</mi><msup><mo>&#160;</mo><mi>c</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>M</mi><mi>a</mi></msup><msup><mi>L</mi><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>c</mi></mrow></msup></mrow></mfenced></math></p><p>comparing :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn></math> ......(i)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>3</mn></math> ....(ii)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>a</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> .......(iii)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">c</mi><mo>=</mo><mn>2</mn><mo>&#160;&#160;</mo><mo>;</mo><mo>&#160;&#160;</mo><mi mathvariant="normal">b</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>&#160;&#160;</mo><mo>;</mo><mo>&#160;&#160;</mo><mo>&#8756;</mo><mo>&#160;&#160;</mo><mo>[</mo><mi mathvariant="normal">d</mi><mo>]</mo><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>FL</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>2</mn></msup></mrow></mfenced></math></p>

</details>

---

### Q84. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following is not a dimensionless quantity?

**Options:**

- **(A)** Power factor
- **(B)** Quality factor
- **(C)** Permeability of free space <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>&#956;</mi><mn>0</mn></msub></mfenced></math>
- **(D)** Relative magnetic permeability <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>&#956;</mi><mi mathvariant="normal">r</mi></msub></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Permeability of free space <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>&#956;</mi><mn>0</mn></msub></mfenced></math>**

**Detailed Solution:**

The power factor is defined as,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>&#981;</mi></math> which is dimensionless, the formula of quality factor, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mi>R</mi></mfrac><msqrt><mfrac><mi>L</mi><mi>C</mi></mfrac></msqrt></math>, which is also dimensionless, and the permeability in free space, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mi>r</mi></msub><mo>=</mo><mfrac><mi>&#956;</mi><msub><mi>&#956;</mi><mn>0</mn></msub></mfrac></math>, but permeability in free space is defined as,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mn>0</mn></msub><mo>=</mo><mfrac><msup><mi>c</mi><mn>2</mn></msup><msub><mi>&#949;</mi><mn>0</mn></msub></mfrac></math>, here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the speed of light in vacuum and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mn>0</mn></msub></math> is the permittivity in free space so this having dimension.

</details>

---

### Q85. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Match List - I with List - II :</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List - I</td>			<td> </td>			<td>List - II</td>		</tr>		<tr>			<td>a</td>			<td>Magnetic induction</td>			<td>i</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></td>		</tr>		<tr>			<td>b</td>			<td>Magnetic flux</td>			<td>ii</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></td>		</tr>		<tr>			<td>c</td>			<td>Magnetic permeability</td>			<td>iii</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></td>		</tr>		<tr>			<td>d</td>			<td>Magnetization</td>			<td>iv</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></td>		</tr>	</tbody></table><p>Choose the most appropriate answer from the options given below :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iii</mi><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iii</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iii</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">b</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math>**

**Detailed Solution:**

<p>The dimension of magnetic induction is, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, the dimension of magnetic flux is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mo>=</mo><mover><mi>B</mi><mo>&#8594;</mo></mover><mo>&#183;</mo><mover><mi>A</mi><mo>&#8594;</mo></mover><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#981;</mi></mfenced><mo>=</mo><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, the dimension of magnetic permeability, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> and, the dimension of magnetization, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.</p>

</details>

---

### Q86. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>,</mo><mo>&#160;</mo><mi>L</mi><mo>,</mo><mo>&#160;</mo><mi>M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math> denote the quantities as energy, angular momentum, mass and constant of gravitation respectively, then the dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> in the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>E</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>M</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><msup><mi>G</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> are:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>0</mn></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mn>2</mn></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mn>0</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>0</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mn>0</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>0</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>E</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>M</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><msup><mi>G</mi><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><msup><mfenced open="[" close="]" separators="|"><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup><mfenced open="[" close="]" separators="|"><msup><mi>M</mi><mrow><mo>&#8722;</mo><mn>5</mn></mrow></msup></mfenced><msup><mfenced open="[" close="]" separators="|"><mrow><msup><mi>M</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><msup><mi>L</mi><mn>3</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><msup><mi>M</mi><mn>0</mn></msup><msup><mi>L</mi><mn>0</mn></msup><msup><mi>T</mi><mn>0</mn></msup></mrow></mfenced></math></p>

</details>

---

### Q87. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Match List I with List II.</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>List-I</td>			<td> </td>			<td>List-II</td>		</tr>		<tr>			<td>a</td>			<td>Capacitance, C</td>			<td>i</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></td>		</tr>		<tr>			<td>b</td>			<td>Permittivity of free space, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mn>0</mn></msub></math></td>			<td>ii</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>4</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mn>2</mn></msup></math></td>		</tr>		<tr>			<td>c</td>			<td>Permeability of free space, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mn>0</mn></msub></math></td>			<td>iii</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>4</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mn>2</mn></msup></math></td>		</tr>		<tr>			<td>d</td>			<td>Electric field, E</td>			<td>iv</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></td>		</tr>	</tbody></table><p>Choose the correct answer from the options given below</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>iii</mi><mo>), (</mo><mi mathvariant="normal">b</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>&#8594;</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>iii</mi><mo>), (</mo><mi mathvariant="normal">b</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>iv</mi><mo>), (</mo><mi mathvariant="normal">c</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>ii</mi><mo>), (</mo><mi mathvariant="normal">d</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>iv</mi><mo>), (</mo><mi mathvariant="normal">b</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>ii</mi><mo>), (</mo><mi mathvariant="normal">c</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>iii</mi><mo>), (</mo><mi mathvariant="normal">d</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>iv</mi><mo>), (</mo><mi mathvariant="normal">b</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>iii</mi><mo>), (</mo><mi mathvariant="normal">c</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>ii</mi><mo>), (</mo><mi mathvariant="normal">d</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi>iii</mi><mo>), (</mo><mi mathvariant="normal">b</mi><mo>)&#160;</mo><mo>&#8594;</mo><mo>(</mo><mi>ii</mi><mo>)</mo><mo>,</mo><mo>(</mo><mi mathvariant="normal">c</mi><mo>)</mo><mo>&#8594;</mo><mo>(</mo><mi>iv</mi><mo>)</mo><mo>,</mo><mo>(</mo><mi mathvariant="normal">d</mi><mo>)</mo><mo>&#8594;</mo><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">q</mi><mo>=</mo><mi>CV</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">C</mi><mo>]</mo><mo>=</mo><mfenced open="[" close="]"><mfrac><mi mathvariant="normal">q</mi><mi mathvariant="normal">V</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mo>(</mo><mi mathvariant="normal">A</mi><mo>&#215;</mo><mi mathvariant="normal">T</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>4</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">E</mi><mo>]</mo><mo>=</mo><mfenced open="[" close="]"><mfrac><mi mathvariant="normal">F</mi><mi mathvariant="normal">q</mi></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi>AT</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>MLT</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi><mo>=</mo><mfrac><mrow><msub><mi mathvariant="normal">q</mi><mn>1</mn></msub><msub><mi mathvariant="normal">q</mi><mn>2</mn></msub></mrow><mrow><mn>4</mn><mi>&#960;</mi><msub><mo>&#8712;</mo><mn>0</mn></msub><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msub><mi>&#1013;</mi><mi mathvariant="normal">o</mi></msub></mfenced><mo>=</mo><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>4</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mn>2</mn></msup></math></p><p>Speed of light <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">c</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msub><mo>&#8712;</mo><mi mathvariant="normal">o</mi></msub></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><msub><mi>&#1013;</mi><mn>0</mn></msub><msup><mi>c</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msub><mi>&#956;</mi><mn>0</mn></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>4</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mn>2</mn></msup></mrow></mfenced><msup><mfenced open="[" close="]"><msup><mi>LT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q88. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The force is given in terms of time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> and displacement <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> by the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mi>A</mi><mi>cos</mi><mi>B</mi><mi>x</mi><mo>+</mo><mi>C</mi><mi>sin</mi><mi>D</mi><mi>t</mi></math></p><p>The dimensional formula of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="italic">A</mi><mi mathvariant="italic">D</mi></mrow><mi mathvariant="italic">B</mi></mfrac></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><mo>&#160;</mo><mi mathvariant="normal">L</mi><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">A</mi><mo>]</mo><mo>=</mo><mfenced close="]" open="["><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">B</mi><mo>]</mo><mo>=</mo><mfenced close="]" open="["><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">D</mi><mo>]</mo><mo>=</mo><mfenced close="]" open="["><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mi>AD</mi><mi mathvariant="normal">B</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mfenced close="]" open="["><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mfenced close="]" open="["><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mrow><mfenced close="]" open="["><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mfrac><mi>AD</mi><mi mathvariant="normal">B</mi></mfrac></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q89. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If time <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>t</mi></mfenced><mo>,</mo></math> velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>v</mi></mfenced><mo>,</mo></math> and angular momentum <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>l</mi></mfenced></math> are taken as the fundamental units. Then the dimension of mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>m</mi><mo>)</mo></math> in terms of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>,</mo><mo>&#160;</mo><mi>v</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>t</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>v</mi><mn>1</mn></msup><msup><mi>l</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>t</mi><mn>1</mn></msup><msup><mi>v</mi><mn>2</mn></msup><msup><mi>l</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>t</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>v</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>l</mi><mn>1</mn></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>t</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>v</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>l</mi><mn>1</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>t</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>v</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>l</mi><mn>1</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#8733;</mo><msup><mi>t</mi><mi>a</mi></msup><msup><mi>v</mi><mi>b</mi></msup><msup><mi>&#8467;</mi><mi>c</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#8733;</mo><mo>[</mo><mi mathvariant="normal">T</mi><msup><mo>]</mo><mi mathvariant="normal">a</mi></msup><msup><mfenced open="[" close="]"><msup><mi>LT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mi mathvariant="normal">b</mi></msup><msup><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi mathvariant="normal">c</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">L</mi></mrow><mn>0</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">T</mi></mrow><mn>0</mn></msup><mo>=</mo><msup><mi mathvariant="normal">M</mi><mi mathvariant="normal">c</mi></msup><msup><mi mathvariant="normal">L</mi><mrow><mi mathvariant="normal">b</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">c</mi></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mi mathvariant="normal">a</mi><mo>-</mo><mi mathvariant="normal">b</mi><mo>-</mo><mi mathvariant="normal">c</mi></mrow></msup></math></p><p>Comparing powers, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#8733;</mo><msup><mi>t</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>v</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>&#8467;</mi><mn>1</mn></msup></math></p>

</details>

---

### Q90. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> represent capacity and voltage respectively then what are the dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>/</mo><mi>V</mi><mo>=</mo><mi>&#955;</mi></math> ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">I</mi><mn>3</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>7</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">I</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>6</mn></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">I</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><msup><mi mathvariant="normal">I</mi><mn>3</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>7</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">I</mi><mn>3</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>7</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mfrac><mi>C</mi><mi>V</mi></mfrac><mo>=</mo><mfrac><mrow><mi>Q</mi><mo>/</mo><mi>V</mi></mrow><mi>V</mi></mfrac><mo>=</mo><mfrac><mi>Q</mi><msup><mi>V</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mrow><mo>&#160;</mo><mi>w</mi><mi>o</mi><mi>r</mi><mi>k</mi><mo>&#160;</mo></mrow><mi>Q</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mfrac><msup><mi>Q</mi><mn>3</mn></msup><msup><mfenced><mrow><mi>w</mi><mi>o</mi><mi>r</mi><mi>k</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><msup><mfenced><mrow><mi>I</mi><mi>t</mi></mrow></mfenced><mn>3</mn></msup><msup><mfenced><mrow><mi>F</mi><mo>.</mo><mi>s</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced open="[" close="]"><mrow><msup><mi>I</mi><mn>3</mn></msup><msup><mi>T</mi><mn>3</mn></msup></mrow></mfenced><msup><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup><msup><mi mathvariant="normal">I</mi><mn>3</mn></msup><msup><mi mathvariant="normal">T</mi><mn>7</mn></msup></mrow></mfenced></math></p>

</details>

---

### Q91. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a typical combustion engine the workdone by a gas molecule is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mi>&#946;</mi><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>&#946;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mi>k</mi><mo>&#160;</mo><mi>T</mi></mrow></mfrac></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is the displacement, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is the Boltzmann constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is the temperature. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are constants, dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>2</mn></msup><msup><mi>LT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi>LT</mi><mn>0</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi>LT</mi><mn>0</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mi>T</mi></math>  has dimension of energy</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#946;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mi>k</mi><mi>T</mi></mrow></mfrac></math> is dimensionless</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>&#946;</mi></mfenced><mfenced open="[" close="]"><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>&#946;</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><msup><mi>MT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mi>&#946;</mi></math> has dimensions of work</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>&#945;</mi><mn>2</mn></msup></mfenced><mfenced open="[" close="]"><msup><mi>MT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>&#945;</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><msup><mi>LT</mi><mn>0</mn></msup></mrow></mfenced></math></p>

</details>

---

### Q92. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math> is the electronic charge, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the speed of light in free space and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> is Planck&#39;s constant, the quantity <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><msup><mfenced open="|" close="|"><mi mathvariant="normal">e</mi></mfenced><mn>2</mn></msup><mrow><mi>h</mi><mi>c</mi></mrow></mfrac></math> has dimensions of :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mn>0</mn></msup></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>LC</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#1013;</mi><mn>0</mn></msub></mrow></mfrac><mfrac><msup><mi>e</mi><mn>2</mn></msup><msup><mi>r</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mi>&#955;</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mfrac><msup><mi>e</mi><mn>2</mn></msup><mrow><mn>4</mn><mi>&#960;</mi><msub><mi>&#949;</mi><mn>0</mn></msub></mrow></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mrow><mi>h</mi><mi>c</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>F</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mrow><mi>E</mi><mi>&#955;</mi></mrow></mfrac><mo>=</mo><mfenced><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math></p>

</details>

---

### Q93. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Match List - I with List - II :</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>List</mi><mo>-</mo><mi mathvariant="normal">I</mi></math></td>			<td> </td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>List</mi><mo>-</mo><mi>II</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">a</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> (Planck&#39;s constant)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msup><mi>MLT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">b</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> (kinetic energy)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">c</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> (electric potential)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iii</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">d</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> (linear momentum)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>iv</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">I</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced></math></td>		</tr>	</tbody></table><p>Choose the correct answer from the options given below:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">a</mi></mfenced><mo>&#8594;</mo><mfenced><mi>ii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">b</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">c</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iv</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">d</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">a</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">b</mi></mfenced><mo>&#8594;</mo><mfenced><mi>ii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">c</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iv</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">d</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iii</mi></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">a</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">b</mi></mfenced><mo>&#8594;</mo><mfenced><mi>ii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">c</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iv</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">d</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">a</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">b</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iv</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">c</mi></mfenced><mo>&#8594;</mo><mfenced><mi>ii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">d</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">a</mi></mfenced><mo>&#8594;</mo><mfenced><mi>ii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">b</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iii</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">c</mi></mfenced><mo>&#8594;</mo><mfenced><mi>iv</mi></mfenced><mo>,</mo><mfenced><mi mathvariant="normal">d</mi></mfenced><mo>&#8594;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math>**

**Detailed Solution:**

<p>By dimensional analysis.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi><mo>.</mo><mi mathvariant="normal">E</mi><mo>.</mo><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> (linear momentum) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><msup><mi>MLT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">h</mi><mo>&#160;</mo><mo>(</mo></math> planck&#39;s constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> (electric potential <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">I</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q94. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The work done by a gas molecule in an isolated system is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi><mo>=</mo><mi>&#945;</mi><msup><mi>&#946;</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mi>&#945;</mi><mi>k</mi><mo>&#160;</mo><mi>T</mi></mrow></mfrac></mrow></msup><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is the displacement, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is the Boltzmann constant and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> is the temperature. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are constants. Then the dimensions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">L</mi><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>2</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">M</mi><mn>0</mn></msup><mo>&#160;</mo><mi mathvariant="normal">L</mi><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mi>&#945;</mi><mi>k</mi><mi>T</mi></mrow></mfrac><mo>&#8594;</mo></math> dimensionless</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]"><mi>&#945;</mi></mfenced><mo>=</mo><mfrac><mfenced open="[" close="]"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mfenced open="[" close="]"><mrow><mi>k</mi><mi>T</mi></mrow></mfenced></mfrac><mo>=</mo><mfrac><msup><mi>L</mi><mn>2</mn></msup><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>2</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>W</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mi>&#945;</mi></mfenced><msup><mfenced open="[" close="]"><mi>&#946;</mi></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>&#946;</mi></mfenced><mo>=</mo><msqrt><mfrac><mrow><msup><mi>ML</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mn>2</mn></msup></mrow></mfrac></msqrt><mo>=</mo><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p>

</details>

---

### Q95. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The quantities <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msub><mo>&#8712;</mo><mn>0</mn></msub></msqrt></mfrac><mo>,</mo><mi>y</mi><mo>=</mo><mfrac><mi>E</mi><mi>B</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mfrac><mi>l</mi><mrow><mi>C</mi><mi>R</mi></mrow></mfrac></math> are defined where C-capacitance, R-Resistance, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#8467;</mi><mo>-</mo></math>length, E-Electric field, B-magnetic field and<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8712;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi><mn>0</mn><mo>,</mo><mo>-</mo></math>free space permittivity and permeability respectively. Then:

**Options:**

- **(A)** x, y and z have the same dimension.
- **(B)** Only x and z have the same dimension
- **(C)** Only x and y have the same dimension
- **(D)** Only y and z have the same dimension.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) x, y and z have the same dimension.**

**Detailed Solution:**

<p>(a) Dimensions of quantity are given bellow</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#956;</mi><mn>0</mn></msub><mo>=</mo><mfenced close="]" open="["><mrow><mi mathvariant="normal">T</mi><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>Wb</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi mathvariant="normal">V</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup></mrow></mfenced><mspace linebreak="newline"></mspace><msub><mi>&#949;</mi><mn>0</mn></msub><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">C</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">N</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Now the dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced open="[" close="]"><msqrt><msub><mi>&#956;</mi><mn>0</mn></msub><msub><mo>&#8712;</mo><mn>0</mn></msub></msqrt></mfenced></mfrac><mo>=</mo><msqrt><mfrac><mn>1</mn><mrow><mfenced open="[" close="]"><mrow><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mn>2</mn></msup></mrow></mfenced><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">C</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">N</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></msqrt><mspace linebreak="newline"/><mfenced open="[" close="]"><mi>x</mi></mfenced><mo>=</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>(b) The dimension of electric and magnetic field is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mi mathvariant="normal">T</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi>Wb</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mi mathvariant="normal">V</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mspace linebreak="newline"></mspace><mi>E</mi><mo>=</mo><mfenced close="]" open="["><mrow><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math></p><p>Now the dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> is given by,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>y</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>E</mi></mfenced><mfenced close="]" open="["><mi>B</mi></mfenced></mfrac><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><mrow><mi mathvariant="normal">V</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mfrac><mo>=</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>(c) The dimension of capacitance and resistance is given by, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfenced close="]" open="["><mrow><mi mathvariant="normal">C</mi><mo>&#160;</mo><msup><mi mathvariant="normal">V</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mspace linebreak="newline"></mspace><mi>R</mi><mo>=</mo><mfenced close="]" open="["><mrow><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow></mfenced></math></p><p>Now the dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> is given by</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>z</mi></mfenced><mo>=</mo><mfrac><mfenced close="]" open="["><mi>l</mi></mfenced><mfenced close="]" open="["><mrow><mi>C</mi><mi>R</mi></mrow></mfenced></mfrac><mo>=</mo><mfrac><mfenced close="]" open="["><mi mathvariant="normal">m</mi></mfenced><mrow><mfenced close="]" open="["><mrow><mi mathvariant="normal">C</mi><mo>&#160;</mo><msup><mi mathvariant="normal">V</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="["><mrow><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>All quantities are having the dimensions of velocity.</p>

</details>

---

### Q96. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A quantity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mi>F</mi><msup><mi>v</mi><mn>2</mn></msup><mo>/</mo><mi>W</mi><msup><mi>L</mi><mn>4</mn></msup><mo>&#160;</mo><mo>)</mo></math> in terms of moment of inertia <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math>, force <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math>, velocity <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi></math>, work <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>. The dimensional formula for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is same as that of :

**Options:**

- **(A)** planck&#39;s constant
- **(B)** force constant
- **(C)** energy density
- **(D)** coefficient of viscosity

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) energy density**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>IFv</mi><mn>2</mn></msup><msup><mi>WL</mi><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><msup><mi mathvariant="normal">M</mi><mo>+</mo></msup><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><msup><mfenced><mrow><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mfenced><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mfenced><msup><mi mathvariant="normal">L</mi><mn>4</mn></msup></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><msup><mi mathvariant="normal">L</mi><mn>3</mn></msup></mfrac><mo>=</mo><msup><mi mathvariant="normal">M</mi><mn>4</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo></math> Energy density

</details>

---

### Q97. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Dimensional formula for thermal conductivity is (here <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext mathvariant="italic">K</mtext></math> denotes the temperature):

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext mathvariant="italic">MLT</mtext><mrow><mo mathvariant="italic">&#8211;</mo><mn mathvariant="italic">2</mn></mrow></msup><mtext mathvariant="italic">K</mtext></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext mathvariant="italic">MLT</mtext><mrow><mo mathvariant="italic">&#8211;</mo><mn mathvariant="italic">2</mn></mrow></msup><msup><mtext mathvariant="italic">K</mtext><mrow><mo mathvariant="italic">&#8211;</mo><mn mathvariant="italic">2</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext mathvariant="italic">MLT</mtext><mrow><mo mathvariant="italic">&#8211;</mo><mn mathvariant="italic">3</mn></mrow></msup><mtext mathvariant="italic">K</mtext></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext mathvariant="italic">MLT</mtext><mrow><mo mathvariant="italic">&#8211;</mo><mn mathvariant="italic">3</mn></mrow></msup><msup><mtext mathvariant="italic">K</mtext><mrow><mo mathvariant="italic">&#8211;</mo><mn mathvariant="italic">1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext mathvariant="italic">MLT</mtext><mrow><mo mathvariant="italic">&#8211;</mo><mn mathvariant="italic">3</mn></mrow></msup><msup><mtext mathvariant="italic">K</mtext><mrow><mo mathvariant="italic">&#8211;</mo><mn mathvariant="italic">1</mn></mrow></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo mathvariant="italic">=</mo><mfrac><mrow><mfenced><mrow><mi mathvariant="italic">Q</mi><mo mathvariant="italic">/</mo><mi mathvariant="italic">t</mi></mrow></mfenced><mi mathvariant="italic">&#916;</mi><mi mathvariant="italic">x</mi></mrow><mrow><mi mathvariant="italic">A</mi><mi mathvariant="italic">&#916;</mi><mi mathvariant="italic">T</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">=</mo><mfrac><mrow><msup><mi mathvariant="italic">M</mi><mn mathvariant="italic">1</mn></msup><msup><mi mathvariant="italic">L</mi><mn mathvariant="italic">2</mn></msup><msup><mi mathvariant="italic">T</mi><mrow><mo mathvariant="italic">&#8722;</mo><mn mathvariant="italic">2</mn></mrow></msup><mfenced><mi mathvariant="italic">L</mi></mfenced></mrow><mrow><msup><mi mathvariant="italic">L</mi><mn mathvariant="italic">2</mn></msup><mi mathvariant="italic">K</mi><mfenced><mi mathvariant="italic">T</mi></mfenced></mrow></mfrac><mo mathvariant="italic">=</mo><msup><mi>M</mi><mn mathvariant="italic">1</mn></msup><msup><mi>L</mi><mn mathvariant="italic">1</mn></msup><msup><mi>T</mi><mrow><mo mathvariant="italic">&#8722;</mo><mn mathvariant="italic">3</mn></mrow></msup><msup><mi>K</mi><mrow><mo mathvariant="italic">&#8722;</mo><mn mathvariant="italic">1</mn></mrow></msup></math></p>

</details>

---

### Q98. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Amount of solar energy received on the earth&#39;s surface per unit area per unit time is defined a solar constant. Dimension of solar constant is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>2</mn></msup><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MLT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ML</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>**

**Detailed Solution:**

<p>Solar constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>Energy</mi><mrow><mi>Time</mi><mo>&#160;</mo><mi>Area</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><msup><mi>TL</mi><mn>2</mn></msup></mfrac><mo>=</mo><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math></p>

</details>

---

### Q99. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If momentum<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">P</mi><mo>)</mo></math>, area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">A</mi><mo>)</mo></math> and time <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">T</mi><mo>)</mo></math> are taken to be the fundamental quantities then the dimensional formula for energy is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi mathvariant="normal">P</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi>AT</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>PA</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi>PA</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>P</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mi>AT</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><msup><mi>PA</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let dimension formula of energy will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><msup><mi>A</mi><mi>a</mi></msup><msup><mi>T</mi><mi>b</mi></msup><msup><mi>P</mi><mi>c</mi></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><msup><mi>M</mi><mn>1</mn></msup><msup><mi>L</mi><mn>1</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mi>L</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>=</mo><msup><mi>T</mi><mn>1</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><msup><mi mathvariant="normal">M</mi><mi mathvariant="normal">C</mi></msup><msup><mi mathvariant="normal">L</mi><mrow><mn>2</mn><mi mathvariant="normal">a</mi><mo>+</mo><mi mathvariant="normal">c</mi></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mi mathvariant="normal">b</mi><mo>-</mo><mi mathvariant="normal">c</mi></mrow></msup></math>
by comparison <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mn>1</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>2</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>-</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>2</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;&#160;</mo><mi>a</mi><mo>=</mo><mn>1</mn><mo>/</mo><mn>2</mn><mo>,</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><msup><mi>A</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>P</mi><mn>1</mn></msup></math></p>

</details>

---

### Q100. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If speed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math>, area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and force <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">F</mi></math> are chosen as fundamental units, then the dimension of Young&#39;s modulus will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>FA</mi><mn>2</mn></msup><msup><mi mathvariant="normal">V</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>FA</mi><mn>2</mn></msup><msup><mi mathvariant="normal">V</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>FA</mi><mn>2</mn></msup><msup><mi mathvariant="normal">V</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>FA</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">V</mi><mn>0</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>FA</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">V</mi><mn>0</mn></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>&#8733;</mo><msup><mi>F</mi><mi>a</mi></msup><msup><mi>V</mi><mi>b</mi></msup><msup><mi>A</mi><mi>c</mi></msup><mo>&#160;&#160;</mo><mi>Y</mi><mo>=</mo><mfenced><mfrac><mi>F</mi><mi>A</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>M</mi><mi>L</mi><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><msup><mi>L</mi><mn>2</mn></msup></mfrac><mo>&#8733;</mo><msup><mfenced><mrow><msup><mi>M</mi><mn>1</mn></msup><msup><mi>L</mi><mn>1</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mi>a</mi></msup><msup><mfenced><mrow><msup><mi>L</mi><mn>1</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi>b</mi></msup><msup><mfenced><msup><mi>L</mi><mn>2</mn></msup></mfenced><mi>c</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#8733;</mo><msup><mi mathvariant="normal">M</mi><mi mathvariant="normal">a</mi></msup><msup><mi>La</mi><mo>+</mo></msup><mi mathvariant="normal">b</mi><mo>+</mo><mn>2</mn><mi>cT</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">a</mi><mo>-</mo><mi mathvariant="normal">b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>b</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>2</mn><mi>c</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mn>2</mn><mi>a</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>b</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>&#8211;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><msup><mi>F</mi><mn>1</mn></msup><msup><mi>V</mi><mn>0</mn></msup><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q101. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A quantity <math><mi>f</mi></math> is given by <math><mi>f</mi><mo>=</mo><msqrt><mfrac><mrow><mi>h</mi><msup><mrow><mi>c</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mi>G</mi></mrow></mfrac></msqrt></math> where <math><mi>c</mi></math> is speed of light, <math><mi>G</mi></math> univasal gravitational constant and <math><mi>h</mi></math> is the Planck&rsquo;s constant. Dimension of <math><mi>f</mi></math> is that of:

**Options:**

- **(A)** area
- **(B)** energy
- **(C)** momentum
- **(D)** volume

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) energy**

**Detailed Solution:**

<p><math><mfenced close="]" open="[" separators="|"><mrow><mi>h</mi><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mi>M</mi><mi>L</mi><mi></mi><mmultiscripts><mrow><mi>T</mi><msup><mrow><mi></mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mprescripts></mprescripts><mrow><mi></mi></mrow><mrow><mn>3</mn></mrow></mmultiscripts></mrow></mfenced></math>
<math><mfenced close="]" open="[" separators="|"><mrow><mi>c</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mi>L</mi><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
<math><mfenced close="]" open="[" separators="|"><mrow><mi>G</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi>M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>Substituting the dimensional formulas in the given formula,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>f</mi></mfenced><mo>=</mo><mfenced open="[" close="]"><mrow><mi>M</mi><msup><mi>L</mi><mn>2</mn></msup><msup><mi>T</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q102. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The dimension of stopping potential <math><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></math> in photoelectric effect in units of Planck&rsquo;s constant &lsquo; <math><mi>h</mi></math> &rsquo;, speed of light &lsquo; <math><mi>c</mi></math> &rsquo; and Gravitational constant &lsquo; <math><mi>G</mi></math> &rsquo; and ampere <math><mi>A</mi></math> is:

**Options:**

- **(A)** <math><msup><mrow><mi>h</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><msup><mrow><mi>G</mi></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><msup><mrow><mi>c</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mn>0</mn></msup><msup><mi>c</mi><mn>5</mn></msup><msup><mi>G</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mi>h</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><msup><mrow><mi>c</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><msup><mrow><mi>G</mi></mrow><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>G</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup><msup><mrow><mi>c</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mn>0</mn></msup><msup><mi>c</mi><mn>5</mn></msup><msup><mi>G</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<math><mi>V</mi><mo>=</mo><mi>K</mi><msup><mrow><mo>(</mo><mi>h</mi><mo>)</mo></mrow><mrow><mi>a</mi></mrow></msup><msup><mrow><mo>(</mo><mi>I</mi><mo>)</mo></mrow><mrow><mi>b</mi></mrow></msup><msup><mrow><mo>(</mo><mi>G</mi><mo>)</mo></mrow><mrow><mi>c</mi></mrow></msup><msup><mrow><mo>(</mo><mi>C</mi><mo>)</mo></mrow><mrow><mi>d</mi></mrow></msup></math> (V is voltage)
We know <math><mo>[</mo><mi>h</mi><mo>]</mo><mo>=</mo><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
<math><mo>[</mo><mi>I</mi><mo>]</mo><mo>=</mo><mi>A</mi></math>
<math><mo>[</mo><mi>G</mi><mo>]</mo><mo>=</mo><msup><mrow><mi>M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
<math><mo>[</mo><mi>C</mi><mo>]</mo><mo>=</mo><mi>L</mi><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
<math><mo>[</mo><mi>V</mi><mo>]</mo><mo>=</mo><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
<math><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mrow><mo>(</mo><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>)</mo></mrow><mrow><mi>a</mi></mrow></msup><msup><mrow><mo>(</mo><mi>A</mi><mo>)</mo></mrow><mrow><mi>b</mi></mrow></msup><msup><mrow><mo>(</mo><msup><mrow><mi>M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>)</mo></mrow><mrow><mi>c</mi></mrow></msup><msup><mrow><mo>(</mo><mi>L</mi><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>)</mo></mrow><mrow><mi>d</mi></mrow></msup></math>
<math><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mrow><mi>M</mi></mrow><mrow><mi>a</mi><mo>-</mo><mi>c</mi></mrow></msup><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>c</mi><mo>+</mo><mi>d</mi></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>c</mi><mo>-</mo><mi>d</mi></mrow></msup><msup><mrow><mi>A</mi></mrow><mrow><mi>b</mi></mrow></msup></math>
<math><mi>a</mi><mo>-</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>&#8201;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math>
<math><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>c</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>2</mn><mo>&#8201;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math>
<math><mo>-</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>c</mi><mo>-</mo><mi>d</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>&#8201;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>3</mn><mo>)</mo></math>
<math><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#8201;</mo><mo>&#8201;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>4</mn><mo>)</mo></math>
On solving
<math><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math><mi>a</mi><mo>=</mo><mn>0</mn></math>
<math><mi>d</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#8201;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>K</mi><msup><mrow><mo>(</mo><mi>h</mi><mo>)</mo></mrow><mn>0</mn></msup><msup><mrow><mo>(</mo><mi>A</mi><mo>)</mo></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>(</mo><mi>G</mi><mo>)</mo></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mo>(</mo><mi>C</mi><mo>)</mo></mrow><mn>5</mn></msup></math>

</details>

---

### Q103. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given, <math><mi>B</mi></math> is magnetic field induction, and <math><msub><mrow><mi>&#956;</mi></mrow><mrow><mn>0</mn></mrow></msub></math> is the magnetic permeability of vacuum. The dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>B</mi><mn>2</mn></msup><mrow><mn>2</mn><msub><mi>&#956;</mi><mn>0</mn></msub></mrow></mfrac></math> is:

**Options:**

- **(A)** <math><msup><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(B)** <math><msup><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

Energy density in magnetic filed <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>e</mi><mi>n</mi><mi>e</mi><mi>r</mi><mi>g</mi><mi>y</mi></mrow><mrow><mi>v</mi><mi>o</mi><mi>l</mi><mi>u</mi><mi>m</mi><mi>e</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mi mathvariant="normal">B</mi><mn>2</mn></msup><mrow><mn>2</mn><msub><mi mathvariant="normal">&#956;</mi><mn>0</mn></msub></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mi mathvariant="normal">F</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">e</mi><mo>&#215;</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">t</mi></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">t</mi></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>.</mo><mi mathvariant="normal">L</mi></mrow><mrow><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><msup><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

</details>

---

### Q104. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following combinations has the dimension of electrical resistance <math><mo>(</mo><msub><mrow><mi mathvariant="normal">&#1013;</mi></mrow><mrow><mn>0</mn></mrow></msub></math> is the permittivity of vacuum and <math><msub><mrow><mi mathvariant="normal">&#956;</mi></mrow><mrow><mn>0</mn></mrow></msub></math> is the permeability of vacuum)?

**Options:**

- **(A)** <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(B)** <math><msqrt><mfrac><mrow><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></msqrt></math>
- **(C)** <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(D)** <math><msqrt><mfrac><mrow><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msqrt><mfrac><mrow><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<math><mfenced open="[" close="]" separators="|"><mrow><mtext>Resistance</mtext></mrow></mfenced><mtext>=</mtext><mfrac><mrow><mfenced open="[" close="]" separators="|"><mrow><mtext>Volt</mtext></mrow></mfenced></mrow><mrow><mfenced open="[" close="]" separators="|"><mrow><mtext>Ampere</mtext></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">A</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>  
We know, <math><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mtext>    </mtext><msub><mrow><mi mathvariant="normal">ε</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
Hence, 
<math><msqrt><mfrac><mrow><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mrow><mfenced open="[" close="]" separators="|"><mrow><msub><mrow><mi mathvariant="normal">μ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow><mrow><mfenced open="[" close="]" separators="|"><mrow><msub><mrow><mi mathvariant="normal">ε</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow></mfrac></msqrt><mo>=</mo><msup><mrow><mfenced open="[" close="]" separators="|"><mrow><mfrac><mrow><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></mrow></mfenced></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup></math>  
<math><mo>=</mo><msup><mrow><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfenced></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>2</mn></mrow></mrow></mrow></msup><mo>=</mo><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>

</details>

---

### Q105. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the formula <math><mi>&#160;</mi><mi mathvariant="normal">X</mi><mo>=</mo><mn>5</mn><mi mathvariant="normal">Y</mi><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>2</mn></mrow></msup></math> , <math><mi mathvariant="normal">X</mi></math> and <math><mi mathvariant="normal">Z</mi></math> have dimensions of capacitance and magnetic field, respectively. What are the dimensions of <math><mi mathvariant="normal">Y</mi></math> in SI units?

**Options:**

- **(A)** <math><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">T</mi></mrow><mrow><mn>4</mn><mi mathvariant="normal"> </mi></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi mathvariant="normal"> </mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>0</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">T</mi></mrow><mrow><mn>6</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">A</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">T</mi></mrow><mrow><mn>8</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">A</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">T</mi></mrow><mrow><mn>8</mn></mrow></msup><msup><mrow><mi mathvariant="normal"> </mi><mi mathvariant="normal">A</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<math><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">Y</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">X</mi></mrow></mfenced></mrow><mrow><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">Z</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac></math>  
<math><mo>=</mo><mfrac><mrow><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>4</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><msup><mrow><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>0</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>  
<math><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>8</mn></mrow></msup><msup><mrow><mi mathvariant="normal">A</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced></math>

</details>

---

### Q106. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If Surface tension<math><mi>&#160;</mi><mo>(</mo><mi mathvariant="normal">S</mi><mo>)</mo></math>, Moment of Inertia <math><mo>(</mo><mi mathvariant="normal">I</mi><mo>)</mo></math> and Planck&#39;s constant <math><mo>(</mo><mi mathvariant="normal">h</mi><mo>)</mo><mo>,</mo></math> were to be taken as the fundamental units, the dimensional formula for linear momentum would be:

**Options:**

- **(A)** <math><msup><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">h</mi></mrow><mrow><mn>0</mn></mrow></msup></math>
- **(B)** <math><msup><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">h</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">h</mi></mrow><mrow><mn>0</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">h</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msup><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">h</mi></mrow><mrow><mn>0</mn></mrow></msup></math>**

**Detailed Solution:**

<math><mi mathvariant="normal">P</mi><mo>∝</mo><msup><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mi>a</mi></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mi>b</mi></mrow></msup><msup><mrow><mi mathvariant="normal">h</mi></mrow><mrow><mi>c</mi></mrow></msup></math>  
<math><mo>[</mo><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>]</mo><mo>=</mo><msup><mrow><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi>a</mi></mrow></msup><msup><mrow><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi>b</mi></mrow></msup><msup><mrow><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi>C</mi></mrow></msup></math>  
<math><mfenced open="[" close="]" separators="|"><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">L</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>=</mo><mo>[</mo><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>a</mi><mo>-</mo><mi>c</mi></mrow></msup><mo>]</mo></math>  
From comparing the power on both side 
<math><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn></math>  
<math><mn>2</mn><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>1</mn></math>  
<math><mo>-</mo><mn>2</mn><mi>a</mi><mo>-</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>  
From the above three equations we will get 
<math><mi>a</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mi>b</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mtext> </mtext><mo>&amp;</mo><mi> </mi><mi>c</mi><mo>=</mo><mn>0</mn></math>  
<math><mi mathvariant="normal">P</mi><mo>∝</mo><msup><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup><msup><mrow><mi mathvariant="normal">h</mi></mrow><mrow><mn>0</mn></mrow></msup></math>

</details>

---

### Q107. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If speed (V), acceleration (A) and force (F) are considered

as fundamental units, the dimension of Young's modulus

will be :

**Options:**

- **(A)** $\mathrm{V}^{-2} \mathrm{~A}^{2} \mathrm{~F}^{-2}$
- **(B)** $\mathrm{V}^{-2} \mathrm{~A}^{2} \mathrm{~F}^{2}$
- **(C)** $\mathrm{V}^{-4} \mathrm{~A}^{-2} \mathrm{~F}$
- **(D)** $\mathrm{V}^{-4} \mathrm{~A}^{2} \mathrm{~F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{V}^{-4} \mathrm{~A}^{2} \mathrm{~F}$**

**Detailed Solution:**

Let [Y] = [V] $^{a}[\mathrm{~F}]^{\mathrm{b}}[\mathrm{A}]^{\mathrm{c}}$

$\left[\mathrm{ML}^{-1} \mathrm{~T}^{-2}\right]=\left[\mathrm{LT}^{-1}\right]^{\mathrm{a}}\left[\mathrm{MLT}^{-2}\right]^{\mathrm{b}}\left[\mathrm{LT}^{-2}\right]^{\mathrm{c}}$

$\left[\mathrm{ML}^{-1} \mathrm{~T}^{-2}\right]=\left[\mathrm{M}^{b} \mathrm{~L}^{\mathrm{a}+b+\mathrm{c}} \mathrm{T}^{-\mathrm{a}-2 \mathrm{~b}-2 \mathrm{c}}\right]$

Comparing power both side of similar terms we get,

$b=1, a+b+c=-1,-a-2 b-2 c=-2$

solving above equations we get

$a=-4, b=1, c=2$

so $[\mathrm{Y}]=\left[\mathrm{V}^{-4} \mathrm{FA}^{2}\right]=\left[\mathrm{V}^{-4} \mathrm{~A}^{2} \mathrm{~F}\right]$

</details>

---

### Q108. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The force of interaction between two atoms is given by $F=\alpha \beta \exp \left(-\frac{x^{2}}{\alpha k T}\right) ;$ where $x$ is the distance, $\mathrm{k}$ is the

Boltzmann constant and T is temperature and $\alpha$ and $\beta$ are two constants. The dimensions of $\beta$ is:

**Options:**

- **(A)** $\mathrm{M}^{0} \mathrm{~L}^{2} \mathrm{~T}^{-4}$
- **(B)** $\mathrm{M}^{2} \mathrm{LT}^{-4}$
- **(C)** $\mathrm{MLT}^{-2}$
- **(D)** $\mathrm{M}^{2} \mathrm{~L}^{2} \mathrm{~T}^{-2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{M}^{2} \mathrm{LT}^{-4}$**

**Detailed Solution:**

Force of interaction between two atoms,

$\mathrm{F}=\alpha \beta \mathrm{e}^{\left(\frac{-\mathrm{x}^{2}}{\alpha \mathrm{kT}}\right)}$

Since exponential terms are dimensionless $\therefore\left[\frac{\mathrm{x}^{2}}{\alpha \mathrm{k} \mathrm{T}}\right]=\mathrm{M}^{0} \mathrm{~L}^{0} \mathrm{~T}^{0}$

$\Rightarrow \frac{\mathrm{L}^{2}}{[\alpha] \mathrm{ML}^{2} \mathrm{~T}^{-2}}=\mathrm{M}^{0} \mathrm{~L}^{0} \mathrm{~T}^{0}$

$\Rightarrow[\alpha]=\mathrm{M}^{-1} \mathrm{~T}^{2}$

$[\mathrm{F}]=[\alpha][\beta]$

$\mathrm{MLT}^{-2}=\mathrm{M}^{-1} \mathrm{~T}^{2}[\beta]$

$\Rightarrow[\beta]=M^{2} L T^{-4}$

</details>

---

### Q109. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Expression for time in terms of <math><mi>G</mi></math> (universal gravitational constant), <math><mi>h</mi></math> (Planck constant) and <math><mi>c</mi></math> (speed of light) is proportional to:

**Options:**

- **(A)** <math><msqrt><mfrac><mrow><mi>G</mi><mi>h</mi></mrow><mrow><msup><mrow><mi>c</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></msqrt></math>
- **(B)** <math><msqrt><mfrac><mrow><mi>h</mi><msup><mrow><mi>c</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow><mrow><mi>G</mi></mrow></mfrac></msqrt></math>
- **(C)** <math><msqrt><mfrac><mrow><mi>G</mi><mi>h</mi></mrow><mrow><msup><mrow><mi>c</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></msqrt></math>
- **(D)** <math><msqrt><mfrac><mrow><msup><mrow><mi>c</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mi>G</mi><mi>h</mi></mrow></mfrac></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msqrt><mfrac><mrow><mi>G</mi><mi>h</mi></mrow><mrow><msup><mrow><mi>c</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfrac></msqrt></math>**

**Detailed Solution:**

<math><mi>t</mi><mo>=</mo><msup><mrow><mi>G</mi></mrow><mrow><mi>α</mi><mo>.</mo><mi> </mi></mrow></msup><msup><mrow><mi>h</mi></mrow><mrow><mi>β</mi></mrow></msup><mi> </mi><msup><mrow><mi>c</mi></mrow><mrow><mi>r</mi></mrow></msup></math> 

 <math><mfenced close="]" open="[" separators="|"><mrow><mi>T</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi>α</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mi>M</mi><msup><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi>β</mi></mrow></msup><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>L</mi><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mi>γ</mi></mrow></msup></math> 

 <math><mo>=</mo><msup><mrow><mi>M</mi></mrow><mrow><mo>-</mo><mi>α</mi><mo>+</mo><mi>β</mi></mrow></msup><msup><mrow><mi>L</mi></mrow><mrow><mn>3</mn><mi>α</mi><mo>+</mo><mn>2</mn><mi>β</mi><mo>+</mo><mi>γ</mi></mrow></msup><mi> </mi><msup><mrow><mi>T</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>α</mi><mo>-</mo><mi>β</mi><mo>-</mo><mi>γ</mi></mrow></msup></math> 

 <math><mo>-</mo><mi> </mi><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>0</mn></math> 

 <math><mn>3</mn><mi>α</mi><mo>+</mo><mn>2</mn><mi>β</mi><mo>+</mo><mi>γ</mi><mo>=</mo><mn>0</mn></math> 

 <math><mo>-</mo><mn>2</mn><mi>α</mi><mo>-</mo><mi>β</mi><mo>-</mo><mi>γ</mi><mo>=</mo><mn>1</mn></math> 

 <math><mo>∴</mo><mi>α</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>;</mo><mi>β</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>;</mo><mi>γ</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q110. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

The characteristic distance at which quantum gravitational effects are significant, the Planck length, can be determined from a suitable combination of the fundamental physical constants $\mathrm{G}, \mathrm{h}$ and $\mathrm{c}$. Which of the following correctly gives the Planck length?

**Options:**

- **(A)** $\mathrm{G}^2 \mathrm{hc}$
- **(B)** $\left(\frac{\mathrm{Gh}}{\mathrm{c}^3}\right)^{\frac{1}{2}}$
- **(C)** $\mathrm{G}^{\frac{1}{2}} \mathrm{~h}^2 \mathrm{c}$
- **(D)** $G\left(h^2 \mathrm{c}^3\right.$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{\mathrm{Gh}}{\mathrm{c}^3}\right)^{\frac{1}{2}}$**

**Detailed Solution:**

Plank length is a unit of length,
$$
\begin{aligned}
&l_p=1.616229 \times 10^{-35} \mathrm{~m} \\
&l_p=\sqrt{\frac{h G}{c^3}}
\end{aligned}
$$

</details>

---

### Q111. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Time <math><mfenced separators="|"><mrow><mi>T</mi></mrow></mfenced></math>, velocity <math><mfenced separators="|"><mrow><mi>C</mi></mrow></mfenced></math> and angular momentum <math><mfenced separators="|"><mrow><mi>h</mi></mrow></mfenced></math> are chosen as fundamental quantities instead of mass, length and time. In terms of these, the dimensions of mass would be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mi mathvariant="normal">M</mi></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi mathvariant="normal">h</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">M</mi><mo>]</mo><mo>=</mo><mo>[</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">C</mi><mn>2</mn></msup><mi mathvariant="normal">h</mi><mo>]</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mi mathvariant="normal">M</mi></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mi mathvariant="normal">h</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi mathvariant="normal">M</mi><mo>]</mo><mo>=</mo><mo>[</mo><msup><mi>TC</mi><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup><mi mathvariant="normal">h</mi><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mi mathvariant="normal">M</mi></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mrow><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi mathvariant="normal">h</mi></mrow></mfenced></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>&#8733;</mo><msup><mi mathvariant="normal">T</mi><mi mathvariant="normal">x</mi></msup><msup><mi mathvariant="normal">C</mi><mi mathvariant="normal">y</mi></msup><msup><mi mathvariant="normal">h</mi><mi mathvariant="normal">z</mi></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup><mo>=</mo><msup><mfenced separators="|"><msup><mi mathvariant="normal">T</mi><mn>1</mn></msup></mfenced><mi mathvariant="normal">x</mi></msup><msup><mfenced separators="|"><mrow><msup><mi mathvariant="normal">L</mi><mn>1</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi mathvariant="normal">y</mi></msup><msup><mfenced separators="|"><mrow><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mi mathvariant="normal">z</mi></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><msup><mi mathvariant="normal">M</mi><mn>1</mn></msup><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">L</mi><mn>0</mn></msup><msup><mi mathvariant="normal">T</mi><mn>0</mn></msup><mo>]</mo><mo>=[</mo><msup><mi mathvariant="normal">M</mi><mi mathvariant="normal">z</mi></msup><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">L</mi><mrow><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">z</mi></mrow></msup><msup><mi mathvariant="normal">T</mi><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mi mathvariant="normal">y</mi><mo>-</mo><mi mathvariant="normal">z</mi></mrow></msup><mo>]</mo></math>]
<math><mo>&#10233;</mo><mi>z</mi><mo>=</mo><mn>1</mn></math>
<math><mi>y</mi><mo>+</mo><mn>2</mn><mi>z</mi><mo>=</mo><mn>0</mn><mi> </mi><mo>,</mo><mi mathvariant="italic"> x</mi><mo>-</mo><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math>
<math><mi mathvariant="normal">solving</mi></math>
<math><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>
and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>&#8658;</mo><mfenced open="[" close="]"><mrow><mo>&#160;</mo><msup><mi mathvariant="normal">T</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mi mathvariant="normal">&#160;</mi><msup><mi mathvariant="normal">h</mi><mn>1</mn></msup></mrow></mfenced></math>

</details>

---

### Q112. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<math> <mrow> <mi>A</mi><mo>,</mo><mtext>&#8201;</mtext><mi>B</mi><mo>,</mo><mtext>&#8201;</mtext><mi>C</mi></mrow> </math>, and <math> <mi>D</mi> </math> are four different physical quantities having different dimensions. None of them is dimensionless. But we know that the equation <math> <mrow> <mi>A</mi><mi>D</mi><mo>=</mo><mi>C</mi><mtext>&#8201;</mtext><mi>l</mi><mi>n</mi><mrow><mo>(</mo> <mrow> <mi>B</mi><mi>D</mi></mrow> <mo>)</mo></mrow></mrow> </math> holds true. Then which of the combination is not a meaningful quantity?

**Options:**

- **(A)** <math><mfrac><mrow><mi>C</mi></mrow><mrow><mi>B</mi><mi>D</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>C</mi></mrow></mfrac></math>
- **(B)** <math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>B</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><mfrac><mrow><mi>A</mi></mrow><mrow><mi>B</mi></mrow></mfrac><mo>-</mo><mi>C</mi></math>
- **(D)** <math> <mrow> <mfrac> <mrow> <msup> <mi>A</mi> <mn>2</mn> </msup> <mo>−</mo><mi>A</mi><mi>C</mi> </mrow> <mi>D</mi> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mfrac> <mrow> <msup> <mi>A</mi> <mn>2</mn> </msup> <mo>−</mo><mi>A</mi><mi>C</mi> </mrow> <mi>D</mi> </mfrac> </mrow> </math>**

**Detailed Solution:**

The dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is not equal to the dimension of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>

Hence it is not possible to subtract <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup></math>

</details>

---

### Q113. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

In the following <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> refers to current and other symbols have their usual meaning. Choose the option that corresponds to the dimensions of electrical conductivity:

**Options:**

- **(A)** <math><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>3</mn></mrow></msup><mi mathvariant="normal">I</mi></math>
- **(B)** <math><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>3</mn></mrow></msup><mi mathvariant="normal">I</mi></math>
- **(D)** <math><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<math><mi mathvariant="normal">R</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mi mathvariant="normal">&#963;</mi><mi mathvariant="normal">A</mi></mrow></mfrac></math>

<math><mi mathvariant="normal">&#963;</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mi mathvariant="normal">R</mi><mi mathvariant="normal">A</mi></mrow></mfrac></math><math><mi>=</mi></math> <math><mfrac><mrow><mi mathvariant="normal">L</mi><mi mathvariant="normal">I</mi></mrow><mrow><mi mathvariant="normal">A</mi><mi mathvariant="normal">V</mi></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mi mathvariant="normal">L</mi><mi mathvariant="normal">I</mi></mrow><mrow><mi mathvariant="normal">A</mi><mi mathvariant="normal">w</mi></mrow></mfrac><mi mathvariant="normal">I</mi><mi mathvariant="normal">t</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mrow><mfrac><mi mathvariant="normal">L</mi><msup><mi mathvariant="normal">L</mi><mn>2</mn></msup></mfrac><mfrac><mrow><msup><mi mathvariant="normal">I</mi><mn>2</mn></msup><mi mathvariant="normal">T</mi></mrow><mrow><msup><mi>ML</mi><mn>2</mn></msup><msup><mi mathvariant="normal">T</mi><mn>-2</mn></msup></mrow></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">M</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi mathvariant="normal">L</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">T</mi><mn>3</mn></msup><msup><mi mathvariant="normal">I</mi><mn>2</mn></msup></mrow></mfenced></math>

</details>

---

### Q114. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If electronic charge <math><mi>e</mi></math>, electron mass <math><mi>m</mi></math>, speed of light in vacuum <math><mi>c</mi></math> and Planck's constant <math><mi>h</mi></math> are taken as fundamental quantities, the permeability of vacuum <math><msub><mrow><mi>μ</mi></mrow><mrow><mn>0</mn></mrow></msub></math> can be expressed in units of:

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mfrac><mrow><mi>m</mi><msup><mrow><mi>c</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>h</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mi>m</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mrow><mi>m</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mi>c</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mi>c</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

Magnetic potential energy inside a solenoid is

<math><mi>U</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>L</mi><msup><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msup></math> Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo></math>self-inductor<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>U</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><msub><mi>&#956;</mi><mn>0</mn></msub><msup><mi>n</mi><mn>2</mn></msup><mi>A</mi><mi>&#160;</mi><mi>l</mi></mrow></mfenced><msup><mi>I</mi><mn>2</mn></msup></math>

<math><mo>&#8757;</mo><mi>n</mi><mo>=</mo></math> number of turns per unit length

<math><mo>=</mo><mfrac><mrow><mi>N</mi></mrow><mrow><mi>l</mi></mrow></mfrac></math>

<math><mi>U</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msub><mrow><mi>&#956;</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>N</mi></mrow><mrow><mi>l</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mi>A</mi><mi>l</mi><mi>&#160;</mi><msup><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mi>U</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msub><mrow><mi>&#956;</mi></mrow><mrow><mn>0</mn></mrow></msub><mfrac><mrow><msup><mrow><mi>N</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>A</mi><mi>l</mi><mi>&#160;</mi><msup><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi></math>

<math><msub><mrow><mi>&#956;</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>U</mi><mi>l</mi></mrow><mrow><msup><mrow><mi>N</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>A</mi><msup><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

Dimensionally, <math><mfenced close="]" open="[" separators="|"><mrow><mi>U</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mrow><mi>&#955;</mi></mrow></mfrac></mrow></mfenced></math>

<math><mfenced close="]" open="[" separators="|"><mrow><mi>I</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>e</mi></mrow><mrow><mi>T</mi></mrow></mfrac></mrow></mfenced></math>

<math><mfenced close="]" open="[" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>l</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mfenced close="]" open="[" separators="|"><mrow><mi>l</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi>l</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup></mrow></mfenced></math>

<math><mfenced close="]" open="[" separators="|"><mrow><msub><mrow><mi>&#956;</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mrow><mi>&#955;</mi></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mfrac><mrow><mo>[</mo><mi>l</mi><mo>]</mo></mrow><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac><mfrac><mrow><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>e</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mi>&#955;</mi></mrow></mfrac><mfrac><mrow><mi>t</mi></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mi>c</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math>

<math><msub><mrow><mi>&#956;</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi>h</mi></mrow><mrow><mi>c</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

</details>

---

### Q115. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A beaker contains a fluid of density <math><mi>&#961;</mi></math><math><mfrac><mrow><mi>k</mi><mi>g</mi></mrow><mrow><msup><mrow><mi>m</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math> , specific heat <math><mi>S</mi><mfrac><mrow><mi>J</mi></mrow><mrow><mi>k</mi><msup><mrow><mi>g</mi></mrow><mrow><mi>o</mi></mrow></msup><mi>C</mi></mrow></mfrac></math> and viscosity <math><mi>&#951;</mi></math> . The beaker is filled up to height h. To estimate the rate of heat transfer per unit area <math><mfenced separators="|"><mrow><mfrac><mrow><mover accent="true"><mrow><mi>Q</mi></mrow><mo>&#729;</mo></mover></mrow><mrow><mi>A</mi></mrow></mfrac></mrow></mfenced></math> by convection when beaker is put on a hot plate, a student proposes that it should depend on <math><mi>&#951;</mi></math> , <math><mfenced separators="|"><mrow><mfrac><mrow><mi>S</mi><mi mathvariant="normal">&#916;</mi><mi>&#952;</mi></mrow><mrow><mi>h</mi></mrow></mfrac></mrow></mfenced></math> and <math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>&#961;</mi><mi>g</mi></mrow></mfrac></mrow></mfenced></math> when <math><mi mathvariant="normal">&#916;</mi><mi>&#952;</mi></math> ( <math><msup><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mi>o</mi></mrow></msup><mi>C</mi></math> ) is the difference in the temperature between the bottom and top of the fluid. In that situation the correct option for <math><mfenced separators="|"><mrow><mfrac><mrow><mover accent="true"><mrow><mi>Q</mi></mrow><mo>&#729;</mo></mover></mrow><mrow><mi>A</mi></mrow></mfrac></mrow></mfenced></math> is:

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mfrac><mrow><mi>S</mi><mi mathvariant="normal">Δ</mi><mi>θ</mi></mrow><mrow><mi>h</mi></mrow></mfrac></mrow></mfenced><mi>η</mi></math>
- **(B)** <math><mi>η</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>S</mi><mi mathvariant="normal">Δ</mi><mi>θ</mi></mrow><mrow><mi>h</mi></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>ρ</mi><mi> </mi><mi>g</mi></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mfrac><mrow><mi>S</mi><mi mathvariant="normal">Δ</mi><mi>θ</mi></mrow><mrow><mi>η</mi><mi>h</mi></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>ρ</mi><mi>g</mi></mrow></mfrac></mrow></mfenced></math>
- **(D)** <math><mfrac><mrow><mi>S</mi><mi mathvariant="normal">Δ</mi><mi>θ</mi></mrow><mrow><mi>η</mi><mi>h</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced separators="|"><mrow><mfrac><mrow><mi>S</mi><mi mathvariant="normal">Δ</mi><mi>θ</mi></mrow><mrow><mi>h</mi></mrow></mfrac></mrow></mfenced><mi>η</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">Q</mi><mi mathvariant="normal">A</mi></mfrac><mo>=</mo><msup><mi mathvariant="normal">&#951;</mi><mi mathvariant="normal">x</mi></msup><msup><mfenced separators="|"><mfrac><mrow><mi mathvariant="normal">s</mi><mo>&#8710;</mo><mi mathvariant="normal">&#952;</mi></mrow><mi mathvariant="normal">h</mi></mfrac></mfenced><mi mathvariant="normal">y</mi></msup><msup><mfenced separators="|"><mfrac><mn>1</mn><mrow><mi mathvariant="normal">&#961;</mi><mi mathvariant="normal">g</mi></mrow></mfrac></mfenced><mi mathvariant="normal">z</mi></msup></math> . . . (1)

<math><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mi mathvariant="normal">A</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>,</mo><mi mathvariant="normal"></mi><mfenced close="]" open="[" separators="|"><mrow><mi mathvariant="normal">&#951;</mi></mrow></mfenced><mo>=</mo><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<math><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">s</mi><mo>&#8710;</mo><mi mathvariant="normal">&#952;</mi></mrow><mrow><mi mathvariant="normal">h</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">L</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>,</mo><mi mathvariant="normal"></mi><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">&#961;g</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></msup></mrow></mfenced><mi mathvariant="normal"></mi><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mi mathvariant="normal">y</mi></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi mathvariant="normal">y</mi></mrow></msup></mrow></mfenced><mi mathvariant="normal"></mi><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mn>2z</mn></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>2z</mn></mrow></msup></mrow></mfenced></math>

<math><mi mathvariant="normal">M</mi><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>=</mo><msup><mrow><mi mathvariant="normal">M</mi></mrow><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mi mathvariant="normal">z</mi></mrow></msup><msup><mrow><mi mathvariant="normal">L</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">z</mi></mrow></msup><msup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mo>-</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">z</mi></mrow></msup></math>

So <math><mn>1</mn><mo>=</mo><mi mathvariant="normal">x</mi><mo>-</mo><mi mathvariant="normal">z</mi></math> . . . (2)

<math><mo>-</mo><mi mathvariant="normal">x</mi><mo>+</mo><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">z</mi><mo>=</mo><mn>0</mn></math>. . . (3)

<math><mo>-</mo><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">y</mi><mo>+</mo><mn>2</mn><mi mathvariant="normal">z</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>. . . (4)

from 2, 3, 4

<math><mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal"> y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal"> z</mi><mo>=</mo><mi mathvariant="normal">0</mi><mo>,&#160;</mo></math>from (1)

so <math><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mi mathvariant="normal">A</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#951; </mi><mfrac><mrow><mi mathvariant="normal">s</mi><mo>&#8710;</mo><mi mathvariant="normal">&#952;</mi></mrow><mrow><mi mathvariant="normal">h</mi></mrow></mfrac></math>

</details>

---

### Q116. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the capacitance of a nanocapacitor is measured in terms of a unit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi></math>,  made by combining the electronic charge <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>, Bohr radius <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>a</mi><mn>0</mn><mrow/></msubsup><mo>,</mo></math> Planck&#39;s constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> and speed of light <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> then

**Options:**

- **(A)** <math><mi>u</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>a</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>h</mi><mi>c</mi></mrow></mfrac></math>
- **(B)** <math><mi>u</mi><mo>=</mo><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>a</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(C)** <math><mi>u</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>c</mi></mrow><mrow><mi>h</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>
- **(D)** <math><mi>u</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>h</mi></mrow><mrow><mi>c</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>u</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>a</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>h</mi><mi>c</mi></mrow></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>Capacitance</mi><mi>&#160;</mi><mi>C</mi><mo>=</mo><mfrac><mi>Q</mi><mrow><mo>&#8710;</mo><mi>V</mi></mrow></mfrac><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Also</mi><mo>,</mo><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><mi>&#955;</mi></mfrac></mfenced><mo>=</mo><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mfrac><mrow><mi>h</mi><mi>c</mi></mrow><msub><mi>a</mi><mn>0</mn></msub></mfrac></mfenced><mo>=</mo><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mi>Energy</mi></mfenced></math>. 

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mi>C</mi></mfenced><mo>=</mo><mi>&#160;</mi><mfrac><mfenced open="[" close="]" separators="|"><mi>Q</mi></mfenced><mfenced open="[" close="]" separators="|"><mrow><mo>&#8710;</mo><mi>V</mi></mrow></mfenced></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mfenced open="[" close="]" separators="|"><mi>Q</mi></mfenced><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mi>Q</mi></mfenced></mrow><mrow><mfenced open="[" close="]" separators="|"><mrow><mo>&#8710;</mo><mi>V</mi></mrow></mfenced><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mi>Q</mi></mfenced></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>W</mi><mo>=</mo><mi>q</mi><mo>&#8710;</mo><mi>V</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mi>Q</mi></mfenced><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mrow><mo>&#8710;</mo><mi>V</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mi>Energy</mi></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mi>C</mi></mfenced><mo>=</mo><mi>&#160;</mi><mfrac><mfenced open="[" close="]" separators="|"><msup><mi>Q</mi><mn>2</mn></msup></mfenced><mfenced open="[" close="]" separators="|"><mi>Energy</mi></mfenced></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mfenced open="[" close="]" separators="|"><msup><mi>Q</mi><mn>2</mn></msup></mfenced><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><msub><mi>a</mi><mn>0</mn></msub></mfenced></mrow><mfenced open="[" close="]" separators="|"><mrow><mi>h</mi><mi>c</mi></mrow></mfenced></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mi>Capacitance</mi></mfenced><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mfenced open="[" close="]" separators="|"><msup><mi>Q</mi><mn>2</mn></msup></mfenced><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><msub><mi>a</mi><mn>0</mn></msub></mfenced></mrow><mfenced open="[" close="]" separators="|"><mrow><mi>h</mi><mi>c</mi></mrow></mfenced></mfrac></math>

<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>u</mi><mo>=</mo><mi>&#160;</mi><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi>h</mi><mi>c</mi></mrow></mfrac></math>

</details>

---

### Q117. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

From the following combinations of physical constants (expressed through their usual symbols) the only combination, that would have the same value in different systems of units, is:

**Options:**

- **(A)** $\frac{\mathrm{ch}}{2 \pi \varepsilon_{\mathrm{o}}^2}$
- **(B)** $\frac{\mathrm{e}^2}{2 \pi \varepsilon_{\mathrm{o}} \mathrm{Gm}_{\mathrm{e}}^2}$
- **(C)** $\frac{\mu_{\mathrm{o}} \varepsilon_{\mathrm{o}}}{\mathrm{c}^2} \frac{\mathrm{G}}{\mathrm{he}^2}$
- **(D)** $\frac{2 \pi \sqrt{\mu_{\mathrm{o}} \varepsilon_{\mathrm{o}}}}{\mathrm{ce}^2} \frac{\mathrm{h}}{\mathrm{G}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\mathrm{e}^2}{2 \pi \varepsilon_{\mathrm{o}} \mathrm{Gm}_{\mathrm{e}}^2}$**

**Detailed Solution:**

The dimensional formulae of
$$
\begin{aligned}
&\mathrm{e}=\left[\mathrm{M}^0 \mathrm{~L}^0 \mathrm{~T}^1 \mathrm{~A}^1\right] \\
&\varepsilon_0=\left[\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^4 \mathrm{~A}^2\right] \\
&\mathrm{G}=\left[\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}\right] \\
&\text { and } \mathrm{m}_{\mathrm{e}}=\left[\mathrm{M}^1 \mathrm{~L}^0 \mathrm{~T}^0\right] \\
&\text { Now, } \frac{\mathrm{e}^2}{2 \pi \varepsilon_0 \mathrm{Gm}_{\mathrm{e}}^2} \\
&=\frac{\left[\mathrm{M}^0 \mathrm{~L}^0 \mathrm{~T}^1 \mathrm{~A}^1\right]^2}{2 \pi\left[\mathrm{M}^{-1} \mathrm{~L}^{-3} \mathrm{~T}^4 \mathrm{~A}^2\right]\left[\mathrm{M}^{-1} \mathrm{~L}^3 \mathrm{~T}^{-2}\right]\left[\mathrm{M}^1 \mathrm{~L}^0 \mathrm{~T}^0\right]^2}
\end{aligned}
$$

$$
\begin{aligned}
&=\frac{\left[\mathrm{T}^2 \mathrm{~A}^2\right]}{2 \pi\left[\mathrm{M}^{-1-1+2} \mathrm{~L}^{-3+3} \mathrm{~T}^{4-2} \mathrm{~A}^2\right]} \\
&=\frac{\left[\mathrm{T}^2 \mathrm{~A}^2\right]}{2 \pi\left[\mathrm{M}^0 \mathrm{~L}^0 \mathrm{~T}^2 \mathrm{~A}^2\right]}=\frac{1}{2 \pi}
\end{aligned}
$$
$\because \frac{1}{2 \pi}$ is dimensionless thus the combination

$\frac{\mathrm{e}^2}{2 \pi \varepsilon_0 \mathrm{Gm}_{\mathrm{e}}^2}$ would have the same value in different systems of units.

</details>

---

### Q118. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

In terms of resistance $R$ and time $T$, the dimensions of ratio $\frac{\mu}{\varepsilon}$ of the permeability $\mu$ and permittivity $\varepsilon$ is:

**Options:**

- **(A)** $\left[\mathrm{RT}^{-2}\right]$
- **(B)** $\left[\mathrm{R}^2 \mathrm{~T}^{-1}\right]$
- **(C)** $\left[\mathrm{R}^2\right]$
- **(D)** $\left[\mathrm{R}^2 \mathrm{~T}^2\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\mathrm{R}^2\right]$**

**Detailed Solution:**

Dimensions of $\mu=\left[\right.$ MLT $\left.^{-2} \mathrm{~A}^{-2}\right]$
Dimensions of $\in=\left[\mathrm{M}^{-1} \mathrm{~L}^{-3} \mathrm{~T}^4 \mathrm{~A}^2\right]$
Dimensions of $\mathrm{R}=\left[\mathrm{ML}^2 \mathrm{~T}^{-3} \mathrm{~A}^{-2}\right]$
$$
\begin{aligned}
&\therefore \frac{\text { Dimensions of } \mu}{\text { Dimensions of } e}=\frac{\left[\mathrm{MLT}^{-2} \mathrm{~A}^{-2}\right]}{\left[\mathrm{M}^{-1} \mathrm{~L}^{-3} \mathrm{~T}^4 \mathrm{~A}^2\right]} \\
&=\left[\mathrm{M}^2 \mathrm{~L}^4 \mathrm{~T}^{-6} \mathrm{~A}^{-4}\right]=\left[\mathrm{R}^2\right]
\end{aligned}
$$

</details>

---

### Q119. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If the time period $t$ of the oscillation of a drop of liquid of density $d$, radius $r$, vibrating under surface tension $s$ is given by the formula $t=\sqrt{r^{2 b} s^c d^{a / 2}}$. It is observed that the time period is directly proportional to $\sqrt{\frac{d}{s}}$. The value of $b$ should therefore be :

**Options:**

- **(A)** $\frac{3}{4}$
- **(B)** $\sqrt{3}$
- **(C)** $\frac{3}{2}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{2}$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q120. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The dimensions of angular momentum, latent heat and capacitance are, respectively.

**Options:**

- **(A)** $\mathrm{ML}^2 \mathrm{~T}^1 \mathrm{~A}^2, \mathrm{~L}^2 \mathrm{~T}^{-2}, \mathrm{M}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^2$
- **(B)** $\mathrm{ML}^2 \mathrm{~T}^{-2}, \mathrm{~L}^2 \mathrm{~T}^2, \mathrm{M}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^4 \mathrm{~A}^2$
- **(C)** $\mathrm{ML}^2 \mathrm{~T}^{-1}, \mathrm{~L}^2 \mathrm{~T}^{-2}, \mathrm{ML}^2 \mathrm{TA}^2$
- **(D)** $\mathrm{ML}^2 \mathrm{~T}^{-1}, \mathrm{~L}^2 \mathrm{~T}^{-2}, \mathrm{M}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^4 \mathrm{~A}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{ML}^2 \mathrm{~T}^{-1}, \mathrm{~L}^2 \mathrm{~T}^{-2}, \mathrm{M}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^4 \mathrm{~A}^2$**

**Detailed Solution:**

Angular momentum $=\mathrm{m} \times \mathrm{v} \times \mathrm{r}$
$$
=\mathrm{ML}^2 \mathrm{~T}^{-1}
$$
Latent heat $\mathrm{L}=\frac{\mathrm{Q}}{\mathrm{m}}=\frac{\mathrm{ML}^2 \mathrm{~T}^{-2}}{\mathrm{M}}=\mathrm{L}^2 \mathrm{~T}^{-2}$
Capacitance $\mathrm{C}=\frac{\text { Charge }}{\text { P.d. }}=\mathrm{M}^{-1} \mathrm{~L}^{-2} \mathrm{~T}^4 \mathrm{~A}^2$

</details>

---

### Q121. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

From the following, the quantity (constructed from the basic constants of nature), that has the dimensions, as well as correct order of magnitude, vis-a-vis typical atomic size, is:

**Options:**

- **(A)** $\frac{e^2}{4 \pi \varepsilon_0 m c^2}$
- **(B)** $\frac{4 \pi \varepsilon_0 e^2}{m e^2}$
- **(C)** $\frac{m e^2}{4 \pi \varepsilon_0 b^2}$
- **(D)** $\frac{4 \pi \varepsilon_0 m c^2}{e^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{e^2}{4 \pi \varepsilon_0 m c^2}$**

**Detailed Solution:**

As $\mathrm{E}=\mathrm{mc}^2$
also $\mathrm{E}=\mathrm{F} \cdot \mathrm{s}=\frac{\mathrm{kq} \cdot \mathrm{q}}{\mathrm{r}^2} \cdot \mathrm{r}$
Therefore dimensionally
$\begin{aligned}
& \mathrm{mc}^2=\frac{1}{4 \pi \epsilon_0} \frac{\mathrm{q}^2}{\mathrm{r}} \\
& \Rightarrow \mathrm{r}=\frac{\mathrm{e}^2}{4 \pi \epsilon_0 \mathrm{mc}^2}
\end{aligned}$

</details>

---

### Q122. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <msub> <mo>&#8712;</mo> <mn>0</mn> </msub> </mrow> </mfenced> </mrow> </math> denote the dimensional formula of the permittivity of vacuum. If M = mass, L = length, T = time and A = electric current, then :</p>

**Options:**

- **(A)** <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <msub> <mo>&isin;</mo> <mn>0</mn> </msub> </mrow> </mfenced> <mo>=</mo> <mfenced close="]" open="[" separators=","> <mrow> <msup> <mtext>M</mtext> <mn>-1</mn> </msup> <msup> <mtext> L</mtext> <mn>2</mn> </msup> <msup> <mtext> T</mtext> <mn>-1</mn> </msup> <msup> <mtext> A</mtext> <mrow> <mo>-</mo> <mn>2</mn> </mrow> </msup> </mrow> </mfenced> </mrow> </math>
- **(B)** <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <msub> <mo>&isin;</mo> <mn>0</mn> </msub> </mrow> </mfenced> <mo>=</mo> <mfenced close="]" open="[" separators=","> <mrow> <msup> <mtext>M</mtext> <mn>-1</mn> </msup> <msup> <mtext> L</mtext> <mn>2</mn> </msup> <msup> <mtext> T</mtext> <mn>-1</mn> </msup> <mtext> A</mtext> </mrow> </mfenced> </mrow> </math>
- **(C)** <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <msub> <mo>&isin;</mo> <mn>0</mn> </msub> </mrow> </mfenced> <mo>=</mo> <mfenced close="]" open="[" separators=","> <mrow> <msup> <mtext>M</mtext> <mn>-1</mn> </msup> <msup> <mtext> L</mtext> <mrow> <mo>-</mo> <mn>3</mn> </mrow> </msup> <msup> <mtext> T</mtext> <mn>2</mn> </msup> <mtext> A</mtext> </mrow> </mfenced> </mrow> </math>
- **(D)** <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <msub> <mo>&isin;</mo> <mn>0</mn> </msub> </mrow> </mfenced> <mo>=</mo> <mfenced close="]" open="[" separators=","> <mrow> <msup> <mtext>M</mtext> <mn>-1</mn> </msup> <msup> <mtext> L</mtext> <mrow> <mo>-</mo> <mn>3</mn> </mrow> </msup> <msup> <mtext> T</mtext> <mn>4</mn> </msup> <msup> <mtext> A</mtext> <mn>2</mn> </msup> </mrow> </mfenced> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <msub> <mo>&isin;</mo> <mn>0</mn> </msub> </mrow> </mfenced> <mo>=</mo> <mfenced close="]" open="[" separators=","> <mrow> <msup> <mtext>M</mtext> <mn>-1</mn> </msup> <msup> <mtext> L</mtext> <mrow> <mo>-</mo> <mn>3</mn> </mrow> </msup> <msup> <mtext> T</mtext> <mn>4</mn> </msup> <msup> <mtext> A</mtext> <mn>2</mn> </msup> </mrow> </mfenced> </mrow> </math>**

**Detailed Solution:**

<math> <mrow> <mtext>F</mtext> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> <mi>&pi;</mi> <msub> <mi>&epsilon;</mi> <mn>0</mn> </msub> </mrow> </mfrac> <mfrac> <mrow> <msub> <mtext>q</mtext> <mn>1</mn> </msub> <msub> <mtext>q</mtext> <mn>2</mn> </msub> </mrow> <mrow> <msup> <mtext>R</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>

<math> <mrow> <msub> <mi>&epsilon;</mi> <mn>0</mn> </msub> <mo>=</mo> <mfrac> <mrow> <msub> <mtext>q</mtext> <mn>1</mn> </msub> <msub> <mtext>q</mtext> <mn>2</mn> </msub> </mrow> <mrow> <mn>4</mn> <mi>&pi;</mi> <msup> <mtext>FR</mtext> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> </math>

Hence, <math> <mrow> <msub> <mi>&epsilon;</mi> <mn>0</mn> </msub> <mo>=</mo> <mfrac> <mrow> <msup> <mtext>C</mtext> <mn>2</mn> </msup> </mrow> <mrow> <msup> <mtext>N . m</mtext> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <msup> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mtext>AT</mtext> </mrow> </mfenced> </mrow> <mn>2</mn> </msup> </mrow> <mrow> <mtext>ML</mtext><msup> <mtext>T</mtext><mrow> <mo>-</mo> <mn>2</mn> </mrow> </msup> <msup> <mtext>. L</mtext> <mn>2</mn> </msup> </mrow> </mfrac> <mo>=</mo> <mfenced close="]" open="[" separators=","> <mrow> <msup> <mtext>M</mtext> <mn>-1</mn> </msup> <msup> <mtext> L</mtext> <mrow> <mo>-</mo> <mn>3</mn> </mrow> </msup> <msup> <mtext> T</mtext> <mn>4</mn> </msup> <msup> <mtext> A</mtext> <mn>2</mn> </msup> </mrow> </mfenced> </mrow> </math>

</details>

---

### Q123. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `1`

The electrical resistance $R$ of a conductor of length $l$ and area of cross section $a$ is given by $R=\frac{\rho l}{a}$ where ' $\rho$ ' is the electrical resistivity. What is the dimensional formula for electrical conductivity ' $\sigma$ ' which is reciprocal of resistivity?

**Options:**

- **(A)** $\left[M^{-1} L^{-3} T^3 A^2\right]$
- **(B)** $\left[M L^{-3} T^{-3} A^2\right]$
- **(C)** $\left[M L^3 T^{-3} A^{-2}\right]$
- **(D)** $\left[M^{-2} L^3 T^2 A^{-1}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[M^{-1} L^{-3} T^3 A^2\right]$**

**Detailed Solution:**

Dimensional formula for electrical resistivity, $\rho=\left[\mathrm{ML}^3 \mathrm{~T}^{-3} \mathrm{~A}^{-2}\right]$ Dimensional formula for electrical conductivity, $\sigma=\frac{1}{\rho}$ is $\left[\mathrm{M}^{-1} \mathrm{~L}^{-3} \mathrm{~T}^3 \mathrm{~A}^2\right]$

</details>

---

### Q124. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Given that $K=$ energy, $V=$ velocity, $T=$ time. If they are chosen as the fundamental units, then what is dimensional formula for surface tension?

**Options:**

- **(A)** $\left[K V^{-2} \mathrm{~T}^{-2}\right]$
- **(B)** $\left[K^2 V^2 T^{-2}\right]$
- **(C)** $\left[K^2 V^{-2} T^{-2}\right]$
- **(D)** $\left[K V^2 T^2\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[K V^{-2} \mathrm{~T}^{-2}\right]$**

**Detailed Solution:**

Surface tension $=\frac{F}{\ell}=\frac{F}{\ell} \cdot \frac{\ell}{\ell} \cdot \frac{T^2}{T^2}$ (As, $F . \ell=K\left(\right.$ energy) $; \frac{T^2}{\ell^2}=V^{-2}$ ) Therefore, surface tension $=\left[K V^{-2} T^{-2}\right]$

</details>

---

### Q125. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

The dimension of magnetic field in $\mathrm{M}, \mathrm{L}, \mathrm{T}$ and $\mathrm{C}$ (Coulomb) is given as

**Options:**

- **(A)** $\mathrm{MLT}^{-1} \mathrm{C}^{-1}$
- **(B)** $\mathrm{MT}^2 \mathrm{C}^{-2}$
- **(C)** $\mathrm{MT}^{-1} \mathrm{C}^{-1}$
- **(D)** $\mathrm{MT}^{-2} \mathrm{C}^{-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{MT}^{-1} \mathrm{C}^{-1}$**

**Detailed Solution:**

$$
\begin{aligned}
& F=q v B \\
& B=F / q v=M C^{-1} T^{-1}
\end{aligned}
$$

</details>

---

### Q126. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `2`

Which of the following units denotes the dimensions $\mathrm{ML}^2 / \mathrm{Q}^2$, where $\mathrm{Q}$ denotes the electric charge?

**Options:**

- **(A)** Weber $(\mathrm{Wb})$
- **(B)** $\mathrm{Wb} / \mathrm{m}^2$
- **(C)** Henry $(\mathrm{H})$
- **(D)** $\mathrm{H} / \mathrm{m}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Henry $(\mathrm{H})$**

**Detailed Solution:**

Henry $(\mathrm{H})$

</details>

---

### Q127. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

Out of the following pair, which one does NOT have identical dimensions is

**Options:**

- **(A)** angular momentum and Planck's constant
- **(B)** impulse and momentum
- **(C)** moment of inertia and moment of a force
- **(D)** work and torque

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) moment of inertia and moment of a force**

**Detailed Solution:**

Using dimension

</details>

---

### Q128. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

Which one of the following represents the correct dimensions of the coefficient of viscosity?

**Options:**

- **(A)** $\mathrm{ML}^{-1} \mathrm{~T}^{-2}$
- **(B)** $\mathrm{MLT}^{-1}$
- **(C)** $\mathrm{ML}^{-1} \mathrm{~T}^{-1}$
- **(D)** $\mathrm{ML}^{-2} \mathrm{~T}^{-2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{ML}^{-1} \mathrm{~T}^{-1}$**

**Detailed Solution:**

Dimensions of $\eta$ (coefficient of viscosity)
$$
=\frac{\mathrm{MLT}^{-2}}{\mathrm{M}^0 \mathrm{~L}^0 \cdot \mathrm{M}^0 \mathrm{LT}^{-1}}=\mathrm{ML}^{-1} \mathrm{~T}^{-1}
$$

</details>

---

### Q129. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

The physical quantities not having same dimensions are

**Options:**

- **(A)** torque and work
- **(B)** momentum and Planck's constant
- **(C)** stress and Young's modulus
- **(D)** speed and $\left(\mu_0 \varepsilon_0\right)^{-1 / 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) momentum and Planck's constant**

**Detailed Solution:**

$[$ momentum $]=[\mathrm{M}][\mathrm{L}]\left[\mathrm{T}^{-1}\right]=\left[\mathrm{MLT}^{-1}\right]$
(Planck's Constant) $=\frac{E}{\mathrm{u}}=\frac{[\mathrm{M}]\left[\mathrm{LT}^{-1}\right]^2}{\mathrm{~T}^{-1}}=\mathrm{ML}^2 \mathrm{~T}^{-1}$

</details>

---

### Q130. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

Dimension of $\frac{1}{\mu_0 \varepsilon_0}$, where symbols have their usual meaning, are

**Options:**

- **(A)** $\left[\mathrm{L}^{-1} \mathrm{~T}\right]$
- **(B)** $\left[\mathrm{L}^{-2} \mathrm{~T}^2\right]$
- **(C)** $\left[\mathrm{L}^2 \mathrm{~T}^{-2}\right]$
- **(D)** $\left[\mathrm{LT}^{-1}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\mathrm{L}^2 \mathrm{~T}^{-2}\right]$**

**Detailed Solution:**

$\frac{1}{\sqrt{\mu_0 \varepsilon_0}}=\mathrm{C} \Rightarrow \frac{1}{\mu_0 \varepsilon_0}=\mathrm{C}^2 \Rightarrow\left[\frac{1}{\mu_0 \varepsilon_0}\right]=[\mathrm{C}]^2$
$[\mathrm{C}]=\mathrm{LT}^{-1} \quad$ or $\quad[\mathrm{C}]^2=\mathrm{L}^2 \mathrm{~T}^{-2}$

</details>

---

### Q131. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

Identify the pair whose dimensions are equal

**Options:**

- **(A)** torque and work
- **(B)** stress and energy
- **(C)** force and stress
- **(D)** force and work

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) torque and work**

**Detailed Solution:**

Both have the dimension $M^1 L^2 T^{-2}$

</details>

---

