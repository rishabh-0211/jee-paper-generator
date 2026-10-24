# MHT CET Mathematics - Differential Equations

## Topic 8: Applications of DE

**Total Questions:** 74

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A body cools from $100^\circ$C to $80^\circ$C in 5 minutes in air at $20^\circ$C. The time taken to cool from $80^\circ$C to $60^\circ$C will be:

**Options:**

- **(A)** Less than 5 minutes
- **(B)** Equal to 5 minutes
- **(C)** Greater than 5 minutes
- **(D)** Cannot be determined

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Greater than 5 minutes**

**Detailed Solution:**

According to Newton's law of cooling, the rate of cooling is given by:

$\dfrac{T_1 - T_2}{t} = K \left( \dfrac{T_1 + T_2}{2} - T_0 \right)$

For the first interval ($100^{\circ}$C to $80^{\circ}$C):

$\dfrac{100 - 80}{5} = K \left( \dfrac{100 + 80}{2} - 20 \right)$

$4 = K(90 - 20) = 70K \Rightarrow K = \dfrac{4}{70}$

For the second interval ($80^{\circ}$C to $60^{\circ}$C):

$\dfrac{80 - 60}{t} = K \left( \dfrac{80 + 60}{2} - 20 \right)$

$\dfrac{20}{t} = K(70 - 20) = 50K$

Substituting the value of $K$:

$\dfrac{20}{t} = 50 \times \dfrac{4}{70} = \dfrac{20}{7}$

$t = 7$ minutes

Since $7 > 5$, the time taken is greater than 5 minutes.

Answer: Greater than 5 minutes

</details>

---

### Q2. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\dfrac{dy}{dx} = \dfrac{a + bx}{c + dy}$ represents a family of circles centered at the origin if...

**Options:**

- **(A)** $a = c = 0,\ b + d = 0$
- **(B)** $a = c = 0,\ b = d$
- **(C)** $b = d = 0,\ a + c = 0$
- **(D)** $b = d = 0,\ a = c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a = c = 0,\ b + d = 0$**

**Detailed Solution:**

The equation of a family of circles centered at the origin is given by $x^2 + y^2 = r^2$, where $r$ is an arbitrary constant.

Differentiating this equation with respect to $x$, we get:

$2x + 2y \dfrac{dy}{dx} = 0$

$\dfrac{dy}{dx} = -\dfrac{x}{y}$

The given differential equation is:

$\dfrac{dy}{dx} = \dfrac{a + bx}{c + dy}$

For this to represent the family of circles centered at the origin, it must be identical to $\dfrac{dy}{dx} = -\dfrac{x}{y}$.

Comparing the two equations, we get:

$\dfrac{a + bx}{c + dy} = \dfrac{-x}{y}$

This requires $a = 0$ and $c = 0$. The equation then becomes:

$\dfrac{bx}{dy} = -\dfrac{x}{y}$

$\dfrac{b}{d} = -1$

$b = -d \Rightarrow b + d = 0$

Thus, the required conditions are $a = c = 0$ and $b + d = 0$.

Answer: $a = c = 0,\ b + d = 0$

</details>

---

### Q3. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A spherical raindrop evaporates at a rate proportional to its surface area. The differential equation involving the rate of change of its radius $r$ with time '$t$' is $\ldots$ (where $k$ is a positive constant)

**Options:**

- **(A)** $\dfrac{dr}{dt} + k = 0$
- **(B)** $\dfrac{dr}{dt} - k = 0$
- **(C)** $\dfrac{dr}{dt} + kr = 0$
- **(D)** $\dfrac{dr}{dt} - kr = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{dr}{dt} + k = 0$**

**Detailed Solution:**

Let $V$ be the volume and $S$ be the surface area of the spherical raindrop of radius $r$.

$V = \dfrac{4}{3}\pi r^3$ and $S = 4\pi r^2$

The rate of evaporation is the rate of decrease of volume, which is given to be proportional to the surface area.

$\dfrac{dV}{dt} \propto -S$

$\dfrac{dV}{dt} = -k S$ (where $k$ is a positive constant of proportionality)

Substituting the expressions for $V$ and $S$:

$\dfrac{d}{dt}\left(\dfrac{4}{3}\pi r^3\right) = -k(4\pi r^2)$

$4\pi r^2 \dfrac{dr}{dt} = -k(4\pi r^2)$

Since $r \neq 0$, dividing both sides by $4\pi r^2$ gives:

$\dfrac{dr}{dt} = -k$

$\dfrac{dr}{dt} + k = 0$

Answer: $\dfrac{dr}{dt} + k = 0$

</details>

---

### Q4. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A body cools from $100^\circ\text{C}$ to $60^\circ\text{C}$ in 20 minutes, the temperature of the surroundings being $20^\circ\text{C}$. The total time taken (in minutes) for the body to cool down to $40^\circ\text{C}$ is ...

**Options:**

- **(A)** $60$
- **(B)** $40$
- **(C)** $50$
- **(D)** $30$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $40$**

**Detailed Solution:**

Using Newton's law of cooling:

$\ln\left(\dfrac{T_1 - T_s}{T_2 - T_s}\right) = kt$

For the first interval, the body cools from $100^\circ\text{C}$ to $60^\circ\text{C}$ in $20$ minutes with $T_s = 20^\circ\text{C}$:

$\ln\left(\dfrac{100 - 20}{60 - 20}\right) = k(20)$

$\ln\left(\dfrac{80}{40}\right) = 20k$

$\ln(2) = 20k$

For the total time $t$ to cool from $100^\circ\text{C}$ to $40^\circ\text{C}$:

$\ln\left(\dfrac{100 - 20}{40 - 20}\right) = kt$

$\ln\left(\dfrac{80}{20}\right) = kt$

$\ln(4) = kt$

$2\ln(2) = kt$

Substituting $20k$ for $\ln(2)$:

$2(20k) = kt$

$t = 40$ minutes

Answer: $40$

</details>

---

### Q5. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If water at $100^\circ\text{C}$ cools in 10 minutes to $80^\circ\text{C}$ and to $65^\circ\text{C}$ in the next 10 minutes, then the room temperature will be ...

**Options:**

- **(A)** $30^\circ\text{C}$
- **(B)** $15^\circ\text{C}$
- **(C)** $25^\circ\text{C}$
- **(D)** $20^\circ\text{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $20^\circ\text{C}$**

**Detailed Solution:**

Using Newton's law of cooling:

$\dfrac{T_1 - T_2}{t} = K \left( \dfrac{T_1 + T_2}{2} - T_0 \right)$

For the first $10$ minutes:

$\dfrac{100 - 80}{10} = K \left( \dfrac{100 + 80}{2} - T_0 \right)$

$2 = K(90 - T_0)$

For the next $10$ minutes:

$\dfrac{80 - 65}{10} = K \left( \dfrac{80 + 65}{2} - T_0 \right)$

$1.5 = K(72.5 - T_0)$

Dividing the two equations:

$\dfrac{2}{1.5} = \dfrac{90 - T_0}{72.5 - T_0}$

$\dfrac{4}{3} = \dfrac{90 - T_0}{72.5 - T_0}$

$4(72.5 - T_0) = 3(90 - T_0)$

$290 - 4T_0 = 270 - 3T_0$

$T_0 = 20^\circ\text{C}$

Answer: $20^\circ\text{C}$

</details>

---

### Q6. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A body cools according to Newton's law of cooling from $100^\circ$C to $60^\circ$C in $20$ minutes. The temperature of the surroundings being $20^\circ$C, then the total time required for the body to cool down to $30^\circ$C is

**Options:**

- **(A)** $90$ minutes
- **(B)** $1$ hour and $10$ minutes
- **(C)** $80$ minutes
- **(D)** $60$ minutes

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $60$ minutes**

**Detailed Solution:**

According to Newton's law of cooling, the temperature of a body at time $t$ is given by:

$T - T_s = (T_0 - T_s) e^{-kt}$

Given $T_0 = 100^\circ$C and $T_s = 20^\circ$C. At $t = 20$ minutes, $T = 60^\circ$C.

Substituting these values into the equation:

$60 - 20 = (100 - 20) e^{-20k}$

$40 = 80 e^{-20k}$

$e^{-20k} = \dfrac{1}{2}$

Taking the natural logarithm on both sides:

$-20k = -\ln 2 \Rightarrow k = \dfrac{\ln 2}{20}$

Let $t$ be the total time required for the body to cool down to $30^\circ$C.

$30 - 20 = (100 - 20) e^{-kt}$

$10 = 80 e^{-kt}$

$e^{-kt} = \dfrac{1}{8} = \left(\dfrac{1}{2}\right)^3$

Taking the natural logarithm again:

$-kt = -3\ln 2 \Rightarrow kt = 3\ln 2$

Substituting the value of $k$:

$\left(\dfrac{\ln 2}{20}\right) t = 3\ln 2$

$t = 60$ minutes.

Answer: $60$ minutes

</details>

---

### Q7. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The population of towns $A$ and $B$ increase at the rate proportional to their population present at that time. At the end of the year 1984, the population of both the towns was 20,000 . At the end of the year 1989, the population of town A was 25,000 and that of town B was 28,000. The difference of populations of towns A and B at the end of 1994 was

**Options:**

- **(A)** 5950
- **(B)** 8000
- **(C)** 7950
- **(D)** 6950

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7950**

**Detailed Solution:**

Let $P$ be the population at time $t$ in years. The rate of increase is proportional to the population, so $\dfrac{dP}{dt} = kP$, which gives $P(t) = P_0 e^{kt}$.

Let $t = 0$ correspond to the end of the year 1984. The initial population for both towns is $P_0 = 20000$.

For town A, at the end of 1989 ($t = 5$), the population is $25000$.

$P_A(5) = 20000 e^{5k_A} = 25000 \Rightarrow e^{5k_A} = \dfrac{25000}{20000} = \dfrac{5}{4}$

For town B, at the end of 1989 ($t = 5$), the population is $28000$.

$P_B(5) = 20000 e^{5k_B} = 28000 \Rightarrow e^{5k_B} = \dfrac{28000}{20000} = \dfrac{7}{5}$

We need to find the populations at the end of 1994, which corresponds to $t = 10$.

For town A:

$P_A(10) = 20000 e^{10k_A} = 20000 (e^{5k_A})^2 = 20000 \left(\dfrac{5}{4}\right)^2 = 20000 \times \dfrac{25}{16} = 31250$

For town B:

$P_B(10) = 20000 e^{10k_B} = 20000 (e^{5k_B})^2 = 20000 \left(\dfrac{7}{5}\right)^2 = 20000 \times \dfrac{49}{25} = 39200$

The difference in the populations of towns A and B at the end of 1994 is:

$P_B(10) - P_A(10) = 39200 - 31250 = 7950$

Answer: 7950

</details>

---

### Q8. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The money invested in a company is compounded continuously. If $₹ 400$ invested today becomes ₹800 in 6 years, then at the end of 30 years, it will become (in ₹)

**Options:**

- **(A)** 18101.76
- **(B)** 12800
- **(C)** 9050.88
- **(D)** 12804

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 12800**

**Detailed Solution:**

Let $P$ be the principal amount and $A$ be the amount at time $t$.

For continuous compounding, the amount is given by $A = P e^{rt}$.

Given $P = 400$ and $A = 800$ when $t = 6$.

$800 = 400 e^{6r}$

$e^{6r} = 2$

We need to find the amount $A$ at the end of $30$ years ($t = 30$).

$A = 400 e^{30r}$

$A = 400 (e^{6r})^5$

Substituting $e^{6r} = 2$, we get:

$A = 400 (2)^5$

$A = 400 \times 32 = 12800$

Answer: 12800

</details>

---

### Q9. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The rate of increase of the population of a city is proportional to the population present at that instant. In the period of 40 years the population increased from 30,000 to 40,000 . At any time $t$ the population is $(a)(b)^{\frac{t}{40}}$. Then the value of $a$ and $b$ are respectively

**Options:**

- **(A)** $30,000, \frac{2}{3}$
- **(B)** $30,000, \frac{4}{3}$
- **(C)** $40,000, \frac{2}{3}$
- **(D)** $40,000, \frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $30,000, \frac{4}{3}$**

**Detailed Solution:**

Let $P$ be the population at time $t$.

$\dfrac{dP}{dt} = kP$

$\int \dfrac{dP}{P} = \int k dt$

$\ln P = kt + C$

$P = e^{kt+C} = A e^{kt}$

At $t = 0$, $P = 30,000$, so $A = 30,000$.

$P = 30,000 e^{kt}$

At $t = 40$, $P = 40,000$.

$40,000 = 30,000 e^{40k}$

$e^{40k} = \dfrac{4}{3}$

The population at any time $t$ is given by:

$P = 30,000 (e^{40k})^{\dfrac{t}{40}}$

$P = 30,000 \left(\dfrac{4}{3}\right)^{\dfrac{t}{40}}$

Comparing with $P = (a)(b)^{\dfrac{t}{40}}$, we get $a = 30,000$ and $b = \dfrac{4}{3}$.

Answer: $30,000, \frac{4}{3}$

</details>

---

### Q10. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The rate at which the population of a city increases varies as the population. In a period of 20 years, the population increased from 4 lakhs to 6 lakhs. In another 20 years the population will be

**Options:**

- **(A)** 8 lakhs
- **(B)** 12 lakhs
- **(C)** 9 lakhs
- **(D)** 10 lakhs

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 9 lakhs**

**Detailed Solution:**

Let $P$ be the population at time $t$.

Given that the rate of increase of population is proportional to the population, we have:

$\dfrac{dP}{dt} \propto P$

$\dfrac{dP}{dt} = kP$

$\int \dfrac{dP}{P} = \int k dt$

$\ln P = kt + C$

At $t = 0$, $P = 4$ lakhs, so $C = \ln 4$.

$\ln P = kt + \ln 4$

$P = 4e^{kt}$

At $t = 20$, $P = 6$ lakhs, so:

$6 = 4e^{20k}$

$e^{20k} = \dfrac{6}{4} = \dfrac{3}{2}$

In another 20 years, the time will be $t = 40$ years. The population will be:

$P = 4e^{40k} = 4(e^{20k})^2$

$P = 4\left(\dfrac{3}{2}\right)^2 = 4 \times \dfrac{9}{4} = 9$ lakhs.

Answer: 9 lakhs

</details>

---

### Q11. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The rate at which a substance cools in moving air, is proportional to the difference between the temperature of the substance and that of air. The temperature of air is 290 K and the substance cools from 370 K to 330 K in 10 minutes. Then the time to cool the substance upto 295 K is

**Options:**

- **(A)** 40 min
- **(B)** 96 min
- **(C)** 50 min
- **(D)** 60 min

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 40 min**

**Detailed Solution:**

According to Newton's law of cooling,

$\dfrac{dT}{dt} = -k(T - T_s)$

Integrating, we get $T - T_s = (T_0 - T_s)e^{-kt}$

Given $T_s = 290$ K, $T_0 = 370$ K, and at $t = 10$ min, $T = 330$ K.

$330 - 290 = (370 - 290)e^{-10k}$

$40 = 80e^{-10k} \Rightarrow e^{-10k} = \dfrac{1}{2}$

Let $t$ be the time when the temperature of the substance is $295$ K.

$295 - 290 = (370 - 290)e^{-kt}$

$5 = 80e^{-kt} \Rightarrow e^{-kt} = \dfrac{1}{16}$

We can write $e^{-kt} = (e^{-10k})^{\dfrac{t}{10}}$

$\left(\dfrac{1}{2}\right)^{\dfrac{t}{10}} = \dfrac{1}{16} = \left(\dfrac{1}{2}\right)^4$

Equating the powers, we get $\dfrac{t}{10} = 4 \Rightarrow t = 40$ min.

Answer: 40 min

</details>

---

### Q12. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The population of a town increases at a rate proportional to the population at that time. If the population increases from forty thousand to eighty thousand in 20 years, then the population in another 40 years will be

**Options:**

- **(A)** $240000$
- **(B)** $160000$
- **(C)** $320000$
- **(D)** $640000$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $320000$**

**Detailed Solution:**

Let $P$ be the population of the town at time $t$.

Given that the rate of increase of population is proportional to the population at that time:

$\dfrac{dP}{dt} = kP$

$\int \dfrac{dP}{P} = \int k \, dt$

$\ln P = kt + C$

$P = e^{kt+C} = P_0 e^{kt}$

At $t = 0$, $P = 40000$.

$40000 = P_0 e^0 \Rightarrow P_0 = 40000$

At $t = 20$, $P = 80000$.

$80000 = 40000 e^{20k}$

$e^{20k} = 2$

We need to find the population in another $40$ years, which means at $t = 20 + 40 = 60$ years.

$P = 40000 e^{60k}$

$P = 40000 (e^{20k})^3$

$P = 40000 (2)^3$

$P = 40000 \times 8 = 320000$

Answer: $320000$

</details>

---

### Q13. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a culture bacteria count is $1,00,000$ initially. The number increases by $10 \%$ in first 2 hours. In how many hours will the count reach $2,00,000$, if the rate of growth of bacteria is proportional to the number present?

**Options:**

- **(A)** $\frac{2 \log \left(\frac{11}{10}\right)}{\log 2}$
- **(B)** $\frac{\log \left(\frac{11}{10}\right)}{\log 2}$
- **(C)** $\frac{2 \log 2}{\log \left(\frac{11}{10}\right)}$
- **(D)** $\frac{\log (2)}{\log \left(\frac{11}{10}\right)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 \log 2}{\log \left(\frac{11}{10}\right)}$**

**Detailed Solution:**

Let $N$ be the number of bacteria at time $t$.

$\dfrac{dN}{dt} \propto N \Rightarrow \dfrac{dN}{dt} = kN$

Integrating, we get $N = N_0 e^{kt}$, where $N_0$ is the initial count.

Given $N_0 = 1,00,000$.

At $t = 2$, the count increases by $10\%$, so $N = 1,00,000 + 10\% \text{ of } 1,00,000 = 1,10,000$.

$1,10,000 = 1,00,000 e^{2k} \Rightarrow e^{2k} = \dfrac{11}{10}$

$2k = \log\left(\dfrac{11}{10}\right) \Rightarrow k = \dfrac{1}{2} \log\left(\dfrac{11}{10}\right)$

We need to find $t$ when $N = 2,00,000$.

$2,00,000 = 1,00,000 e^{kt} \Rightarrow e^{kt} = 2$

$kt = \log 2$

Substituting the value of $k$:

$\dfrac{1}{2} \log\left(\dfrac{11}{10}\right) t = \log 2$

$t = \dfrac{2 \log 2}{\log\left(\dfrac{11}{10}\right)}$

Answer: $\frac{2 \log 2}{\log \left(\frac{11}{10}\right)}$

</details>

---

### Q14. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The assets of a person reduced in his business such that the rate of reduction is proportional to the square root of the existing assets. If the assets were initially ₹ 10 lakhs and due to loss they reduce to $₹ 10000$ after 3 years, then the number of years required for the person to be bankrupt will be

**Options:**

- **(A)** $\frac{20}{3}$ years
- **(B)** $\frac{10}{3}$ years
- **(C)** $\frac{10}{9}$ years
- **(D)** $\frac{20}{9}$ years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{10}{3}$ years**

**Detailed Solution:**

Let $A$ be the assets of the person at time $t$ (in years).

Given that the rate of reduction of assets is proportional to the square root of the existing assets, we can write the differential equation as:

$\dfrac{dA}{dt} = -k\sqrt{A}$

Separating the variables and integrating both sides:

$\int A^{-1/2} dA = -k \int dt$

$2\sqrt{A} = -kt + C$

Initially, at $t = 0$, the assets were $₹ 10$ lakhs, so $A = 10,00,000 = 10^6$. Substituting these values:

$2\sqrt{10^6} = -k(0) + C$

$2(1000) = C \Rightarrow C = 2000$

The equation becomes:

$2\sqrt{A} = -kt + 2000$

After $3$ years, at $t = 3$, the assets reduce to $₹ 10000$, so $A = 10^4$. Substituting these values:

$2\sqrt{10^4} = -k(3) + 2000$

$2(100) = -3k + 2000$

$200 = -3k + 2000$

$3k = 1800 \Rightarrow k = 600$

The equation for the assets at any time $t$ is:

$2\sqrt{A} = -600t + 2000$

For the person to be bankrupt, the assets must be zero, so $A = 0$. Substituting $A = 0$ into the equation:

$2\sqrt{0} = -600t + 2000$

$600t = 2000$

$t = \dfrac{2000}{600} = \dfrac{10}{3}$ years

Answer: $\frac{10}{3}$ years

</details>

---

### Q15. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The rate of reduction of a persons assets is proportional to the square root of the existing assets. The assets reduced from 25 lakhs to 6.25 lakhs in 2 years. This rate of reduction of his assets will make him bankrupt in

**Options:**

- **(A)** 3 years
- **(B)** 5 years
- **(C)** 4 years
- **(D)** 6 years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4 years**

**Detailed Solution:**

Let $A$ be the assets of the person at time $t$ in years.

According to the given condition, the rate of reduction of assets is proportional to the square root of the existing assets.

$\dfrac{dA}{dt} = -k\sqrt{A}$

Separating the variables, we get:

$\dfrac{dA}{\sqrt{A}} = -k dt$

Integrating both sides:

$\int A^{-1/2} dA = -k \int dt$

$2\sqrt{A} = -kt + C$

Initially, at $t = 0$, $A = 25$ lakhs.

$2\sqrt{25} = -k(0) + C$

$C = 2(5) = 10$

The equation becomes:

$2\sqrt{A} = -kt + 10$

At $t = 2$ years, $A = 6.25$ lakhs.

$2\sqrt{6.25} = -k(2) + 10$

$2(2.5) = -2k + 10$

$5 = -2k + 10$

$2k = 5 \Rightarrow k = 2.5$

Substituting the value of $k$ back into the equation:

$2\sqrt{A} = -2.5t + 10$

The person will become bankrupt when his assets $A = 0$.

$2\sqrt{0} = -2.5t + 10$

$2.5t = 10$

$t = \dfrac{10}{2.5} = 4$ years

Answer: 4 years

</details>

---

### Q16. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The principal increases continuously in a newly opened bank at the rate of $10 \%$ per year. An amount of Rs. 2000 is deposited with this bank. How much will it become after 5 years? $\left(e^{0.5}=1.648\right)$

**Options:**

- **(A)** $3926$
- **(B)** $3296$
- **(C)** $3692$
- **(D)** $3269$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3296$**

**Detailed Solution:**

Let $P$ be the principal at any time $t$.

The rate of increase of principal is given by $\dfrac{dP}{dt} = \dfrac{10}{100} P = 0.1 P$

Separating the variables, we get $\dfrac{dP}{P} = 0.1 dt$

Integrating both sides, $\int \dfrac{dP}{P} = \int 0.1 dt$

$\ln P = 0.1 t + c$

Initially, when $t = 0$, $P = 2000$

$\ln 2000 = 0.1(0) + c \Rightarrow c = \ln 2000$

Substituting $c$ back, $\ln P = 0.1 t + \ln 2000$

$\ln \left(\dfrac{P}{2000}\right) = 0.1 t$

$P = 2000 e^{0.1 t}$

To find the amount after $5$ years, substitute $t = 5$

$P = 2000 e^{0.1 \times 5} = 2000 e^{0.5}$

Given $e^{0.5} = 1.648$

$P = 2000 \times 1.648 = 3296$

Answer: $3296$

</details>

---

### Q17. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a bank, the principal increases continuously at a rate of $x \%$ per year. Then the rate, $x$, if ₹100 double itself in 10 years, is
$(\log 2=0.6931)$

**Options:**

- **(A)** $6.93 \%$
- **(B)** $9.63 \%$
- **(C)** $6.09 \%$
- **(D)** $3.69 \%$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6.93 \%$**

**Detailed Solution:**

Let $P$ be the principal at time $t$.

Given that the principal increases continuously at a rate of $x\%$ per year, we have:

$\dfrac{dP}{dt} = \dfrac{x}{100}P$

$\dfrac{dP}{P} = \dfrac{x}{100}dt$

Integrating both sides:

$\int \dfrac{dP}{P} = \int \dfrac{x}{100}dt$

$\log_e P = \dfrac{x}{100}t + C$

At $t = 0$, $P = 100$, so $C = \log_e 100$.

$\log_e P - \log_e 100 = \dfrac{x}{100}t$

$\log_e \left(\dfrac{P}{100}\right) = \dfrac{x}{100}t$

At $t = 10$, the principal doubles, so $P = 200$.

$\log_e \left(\dfrac{200}{100}\right) = \dfrac{x}{100} \times 10$

$\log_e 2 = \dfrac{x}{10}$

$x = 10 \log_e 2$

Given $\log_e 2 = 0.6931$, we get:

$x = 10 \times 0.6931 = 6.931$

Thus, $x \approx 6.93$.

Answer: $6.93 \%$

</details>

---

### Q18. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The order of the differential equation, whose solution is $y=\left(C_1+C_2\right) \mathrm{e}^x+C_3 \mathrm{e}^{x+C_4}$, is

**Options:**

- **(A)** 4
- **(B)** 1
- **(C)** 3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

The given equation is $y = (C_1 + C_2) \mathrm{e}^x + C_3 \mathrm{e}^{x + C_4}$.

This can be simplified using the laws of exponents:

$y = (C_1 + C_2) \mathrm{e}^x + C_3 \mathrm{e}^x \cdot \mathrm{e}^{C_4}$

$y = (C_1 + C_2 + C_3 \mathrm{e}^{C_4}) \mathrm{e}^x$

Since $C_1, C_2, C_3$, and $C_4$ are arbitrary constants, the entire expression $(C_1 + C_2 + C_3 \mathrm{e}^{C_4})$ can be replaced by a single new arbitrary constant, say $A$.

$y = A \mathrm{e}^x$

The number of essential (independent) arbitrary constants in the general solution is $1$.

The order of a differential equation is equal to the number of essential arbitrary constants in its general solution. Therefore, the order of the differential equation is $1$.

Answer: 1

</details>

---

### Q19. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A radio active substance has half-life of $h$ days, then its initial decay rate is given by Note that at $\mathrm{t}=0, \mathrm{M}=\mathrm{m}_{\mathrm{o}}$

**Options:**

- **(A)** $\frac{\mathrm{m}_{\mathrm{o}}}{2\mathrm{h}}(\log 2)$
- **(B)** $\left(\mathrm{m}_0 \mathrm{~h}\right)(\log 2)$
- **(C)** $-\frac{\mathrm{m}_{\mathrm{o}}}{\mathrm{h}}(\log 2)$
- **(D)** $\left(-\mathrm{m}_0 \mathrm{~h}\right)(\log 2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\frac{\mathrm{m}_{\mathrm{o}}}{\mathrm{h}}(\log 2)$**

**Detailed Solution:**

The radioactive decay law is given by $M = m_0 e^{-\lambda t}$.

Differentiating with respect to time $t$, we get the rate of decay:

$\dfrac{dM}{dt} = -m_0 \lambda e^{-\lambda t}$

At $t = 0$, the initial decay rate is:

$\left(\dfrac{dM}{dt}\right)_{t=0} = -m_0 \lambda$

The decay constant $\lambda$ is related to the half-life $h$ by:

$\lambda = \dfrac{\log_e 2}{h}$

Substituting the value of $\lambda$, we get the initial decay rate:

$\left(\dfrac{dM}{dt}\right)_{t=0} = -m_0 \left(\dfrac{\log_e 2}{h}\right) = -\dfrac{m_0}{h}(\log 2)$

Answer: $-\frac{\mathrm{m}_{\mathrm{o}}}{\mathrm{h}}(\log 2)$

</details>

---

### Q20. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation, having general solution as $\mathrm{A} x^2+\mathrm{B} y^2=1$, where A and B are arbitrary constants, is

**Options:**

- **(A)** $\quad x y \frac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}-x\left(\frac{\mathrm{~d} y}{\mathrm{~d} x}\right)^2-y \frac{\mathrm{~d} y}{\mathrm{~d} x}=0$
- **(B)** $x y \frac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}-x\left(\frac{\mathrm{~d} y}{\mathrm{~d} x}\right)^2+y \frac{\mathrm{~d} y}{\mathrm{~d} x}=0$
- **(C)** $x y \frac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}+x\left(\frac{\mathrm{~d} y}{\mathrm{~d} x}\right)^2+y \frac{\mathrm{~d} y}{\mathrm{~d} x}=0$
- **(D)** $\quad x y \frac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}+x\left(\frac{\mathrm{~d} y}{\mathrm{~d} x}\right)^2-y \frac{\mathrm{~d} y}{\mathrm{~d} x}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\quad x y \frac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}+x\left(\frac{\mathrm{~d} y}{\mathrm{~d} x}\right)^2-y \frac{\mathrm{~d} y}{\mathrm{~d} x}=0$**

**Detailed Solution:**

The given equation is $A x^2 + B y^2 = 1$.

Differentiating with respect to $x$, we get

$2Ax + 2By \dfrac{dy}{dx} = 0$

$Ax + By \dfrac{dy}{dx} = 0$

Differentiating again with respect to $x$, we get

$A + B \left( y \dfrac{d^2y}{dx^2} + \left(\dfrac{dy}{dx}\right)^2 \right) = 0$

From the first derivative equation, we have $A = -B \dfrac{y}{x} \dfrac{dy}{dx}$.

Substituting the value of $A$ into the second derivative equation, we get

$-B \dfrac{y}{x} \dfrac{dy}{dx} + B \left( y \dfrac{d^2y}{dx^2} + \left(\dfrac{dy}{dx}\right)^2 \right) = 0$

Dividing by $B$, we get

$-\dfrac{y}{x} \dfrac{dy}{dx} + y \dfrac{d^2y}{dx^2} + \left(\dfrac{dy}{dx}\right)^2 = 0$

Multiplying the entire equation by $x$, we get

$-y \dfrac{dy}{dx} + x y \dfrac{d^2y}{dx^2} + x \left(\dfrac{dy}{dx}\right)^2 = 0$

Rearranging the terms, we get

$x y \dfrac{d^2y}{dx^2} + x \left(\dfrac{dy}{dx}\right)^2 - y \dfrac{dy}{dx} = 0$

Answer: $\quad x y \frac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}+x\left(\frac{\mathrm{~d} y}{\mathrm{~d} x}\right)^2-y \frac{\mathrm{~d} y}{\mathrm{~d} x}=0$

</details>

---

### Q21. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An ice ball melts at the rate which is proportional to the amount of ice at that instant. Half of the quantity of ice melts in 15 minutes. $x_0$ is the initial quantity of ice. If after 30 minutes the amount of ice left is $k x_0$, then the value of $k$ is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4}$**

**Detailed Solution:**

Let $x$ be the amount of ice at time $t$.

Given that the rate of melting is proportional to the amount of ice at that instant:

$\dfrac{dx}{dt} \propto x$

$\dfrac{dx}{dt} = -cx$

$\int \dfrac{dx}{x} = -c \int dt$

$\ln x = -ct + C$

At $t = 0$, $x = x_0$, so $C = \ln x_0$.

$\ln\left(\dfrac{x}{x_0}\right) = -ct$

$x = x_0 e^{-ct}$

At $t = 15$, half of the ice melts, so the amount of ice left is $x = \dfrac{x_0}{2}$.

$\dfrac{x_0}{2} = x_0 e^{-15c}$

$e^{-15c} = \dfrac{1}{2}$

At $t = 30$, the amount of ice left is $x = k x_0$.

$k x_0 = x_0 e^{-30c}$

$k = (e^{-15c})^2$

$k = \left(\dfrac{1}{2}\right)^2 = \dfrac{1}{4}$

Answer: $\frac{1}{4}$

</details>

---

### Q22. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The bacteria increase at the rate proportional to the number of bacteria present. If the original number N doubles in 8 hours, then the number of bacteria in 24 hours will be

**Options:**

- **(A)** 8 N
- **(B)** 16 N
- **(C)** 32 N
- **(D)** 64 N

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8 N**

**Detailed Solution:**

Let $x$ be the number of bacteria at time $t$.

$\dfrac{dx}{dt} \propto x \Rightarrow \dfrac{dx}{dt} = kx$

Integrating both sides, we get:

$x = c e^{kt}$

At $t = 0$, the original number of bacteria is $N$, so $c = N$.

$x = N e^{kt}$

At $t = 8$ hours, the number of bacteria doubles, so $x = 2N$.

$2N = N e^{8k} \Rightarrow e^{8k} = 2$

To find the number of bacteria in 24 hours, substitute $t = 24$ into the equation:

$x = N e^{24k} = N (e^{8k})^3$

Substituting $e^{8k} = 2$:

$x = N (2)^3 = 8N$

Answer: 8 N

</details>

---

### Q23. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A spherical rain drop evaporates at a rate proportional to its surface area. If initially its radius is 3 mm and after 1 second it is reduced to 2 mm , then at any time t its radius is (where $0 \leq \mathrm{t} \lt 3$ )

**Options:**

- **(A)** $3+t$
- **(B)** $3-\mathrm{t}$
- **(C)** $4-\mathrm{t}$
- **(D)** $1+\mathrm{t}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3-\mathrm{t}$**

**Detailed Solution:**

Let $V$ be the volume, $S$ be the surface area, and $r$ be the radius of the spherical rain drop at time $t$.

Given that the rate of evaporation is proportional to the surface area:

$\dfrac{dV}{dt} = -kS$

Using $V = \dfrac{4}{3}\pi r^3$ and $S = 4\pi r^2$:

$\dfrac{d}{dt}\left(\dfrac{4}{3}\pi r^3\right) = -k(4\pi r^2)$

$4\pi r^2 \dfrac{dr}{dt} = -k(4\pi r^2)$

$\dfrac{dr}{dt} = -k$

Integrating both sides with respect to $t$:

$r = -kt + C$

At $t = 0$, $r = 3$, which gives:

$3 = -k(0) + C \Rightarrow C = 3$

The equation becomes:

$r = -kt + 3$

At $t = 1$, $r = 2$, which gives:

$2 = -k(1) + 3 \Rightarrow k = 1$

Therefore, the radius at any time $t$ is:

$r = 3 - t$

Answer: $3-\mathrm{t}$

</details>

---

### Q24. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A radio-active substance has a half-life of h days, then its initial rate of change of mass is given by (where radio-active substance has initial mass $m_0$).

**Options:**

- **(A)** $\dfrac{m_0}{\mathrm{~h}}(\log 2)$
- **(B)** $\left(\mathrm{m}_0 \mathrm{~h}\right)(\log 2)$
- **(C)** $-\dfrac{\mathrm{m}_0}{\mathrm{~h}}(\log 2)$
- **(D)** $-\left(m_0 \mathrm{~h}\right)(\log 2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\dfrac{\mathrm{m}_0}{\mathrm{~h}}(\log 2)$**

**Detailed Solution:**

The mass of a radioactive substance at time $t$ is given by the decay law:

$m = m_0 e^{-\lambda t}$

The rate of change of mass is obtained by differentiating with respect to $t$:

$\dfrac{dm}{dt} = -\lambda m_0 e^{-\lambda t}$

At $t = 0$, the initial rate of change of mass is:

$\left(\dfrac{dm}{dt}\right)_{t=0} = -\lambda m_0$

The decay constant $\lambda$ is related to the half-life $h$ by the relation:

$\lambda = \dfrac{\log_e 2}{h}$

Substituting the value of $\lambda$, the initial rate of change of mass becomes:

$\left(\dfrac{dm}{dt}\right)_{t=0} = -\dfrac{m_0}{h}(\log_e 2)$

Answer: $-\dfrac{\mathrm{m}_0}{\mathrm{~h}}(\log 2)$

</details>

---

### Q25. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In a certain culture of bacteria, the rate of increase is proportional to the number present. If there are $10^4$ at the end of 3 hours and $4 \cdot 10^4$ at the end of 5 hours, then there were $\qquad$ in the beginning.

**Options:**

- **(A)** $10^4$
- **(B)** $\dfrac{10^4}{4^1}$
- **(C)** $410^4$
- **(D)** $\dfrac{10^4}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{10^4}{8}$**

**Detailed Solution:**

Let $N$ be the number of bacteria at time $t$.

Given that the rate of increase is proportional to the number present, we have $\dfrac{dN}{dt} = k N$.

Integrating, we get $N(t) = N_0 e^{kt}$, where $N_0$ is the initial number of bacteria.

According to the given conditions:

$N(3) = N_0 e^{3k} = 10^4$

$N(5) = N_0 e^{5k} = 4 \times 10^4$

Dividing the second equation by the first equation, we get:

$\dfrac{N_0 e^{5k}}{N_0 e^{3k}} = \dfrac{4 \times 10^4}{10^4}$

$e^{2k} = 4$

$e^k = 2$

Substituting $e^k = 2$ into the first equation:

$N_0 (2)^3 = 10^4$

$8 N_0 = 10^4$

$N_0 = \dfrac{10^4}{8}$

Answer: $\dfrac{10^4}{8}$

</details>

---

### Q26. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The decay rate of radium is proportional to the amount present at any time $t$. If initially 60 gms was present and half life period of radium is 1600 years, then the amount of radium present after 3200 years is

**Options:**

- **(A)** 20 grams
- **(B)** 15 grams
- **(C)** 12 grams
- **(D)** 10 grams

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 15 grams**

**Detailed Solution:**

Let $N_0$ be the initial amount of radium and $N$ be the amount present at time $t$.

Given $N_0 = 60$ gms and half-life $T_{1/2} = 1600$ years.

The time elapsed is $t = 3200$ years.

The number of half-lives is $n = \dfrac{t}{T_{1/2}} = \dfrac{3200}{1600} = 2$.

The amount of radium present after $n$ half-lives is given by $N = N_0 \left(\dfrac{1}{2}\right)^n$.

Substituting the values, we get $N = 60 \left(\dfrac{1}{2}\right)^2 = 60 \times \dfrac{1}{4} = 15$ grams.

Answer: 15 grams

</details>

---

### Q27. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the half life of substance is 5 years, then the total amount of the substance left after 15 years, when initial amount is 64 gms is

**Options:**

- **(A)** 6 gm
- **(B)** 8 gm
- **(C)** 10 gm
- **(D)** 12 gm

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8 gm**

**Detailed Solution:**

Given half-life $T_{1/2} = 5$ years and total time $t = 15$ years.

Number of half-lives $n = \dfrac{t}{T_{1/2}} = \dfrac{15}{5} = 3$.

Initial amount $N_0 = 64$ gms.

Amount of substance left after $n$ half-lives is given by $N = N_0 \left(\dfrac{1}{2}\right)^n$.

Substituting the values, $N = 64 \left(\dfrac{1}{2}\right)^3 = 64 \times \dfrac{1}{8} = 8$ gms.

Answer: 8 gm

</details>

---

### Q28. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A body cools according to Newton's law of cooling from $100^{\circ} \mathrm{C}$ to $60^{\circ} \mathrm{C}$ in 15 minutes. If the temperature of the surrounding is $20^{\circ} \mathrm{C}$, then the temperature of the body after cooling down for one hour is

**Options:**

- **(A)** $30^{\circ} \mathrm{C}$
- **(B)** $25^{\circ} \mathrm{C}$
- **(C)** $35^{\circ} \mathrm{C}$
- **(D)** $40^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $25^{\circ} \mathrm{C}$**

**Detailed Solution:**

According to Newton's law of cooling, the temperature $T$ of a body at time $t$ is given by $T = T_s + (T_0 - T_s) e^{-kt}$, where $T_s$ is the surrounding temperature and $T_0$ is the initial temperature.

Given $T_0 = 100^{\circ}\mathrm{C}$, $T_s = 20^{\circ}\mathrm{C}$, and $T = 60^{\circ}\mathrm{C}$ at $t = 15$ minutes.

Substituting these values into the equation:

$60 = 20 + (100 - 20) e^{-15k}$

$40 = 80 e^{-15k}$

$e^{-15k} = \dfrac{1}{2}$

We need to find the temperature $T'$ after cooling down for one hour, which corresponds to $t = 60$ minutes.

$T' = 20 + (100 - 20) e^{-60k}$

$T' = 20 + 80 (e^{-15k})^4$

$T' = 20 + 80 \left(\dfrac{1}{2}\right)^4$

$T' = 20 + 80 \times \dfrac{1}{16}$

$T' = 20 + 5 = 25^{\circ}\mathrm{C}$

Answer: $25^{\circ} \mathrm{C}$

</details>

---

### Q29. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In a certain culture of bacteria, the rate of increase is proportional to the number of bacteria present at that instant. It is found that there are 10,000 bacteria at the end of 3 hours and 40,000 bacteria at the end of 5 hours, then the number of bacteria present in the beginning are

**Options:**

- **(A)** 1250.
- **(B)** 1200.
- **(C)** 1350.
- **(D)** 1300.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1250.**

**Detailed Solution:**

Let $x$ be the number of bacteria present at time $t$.
$\begin{aligned}
& \therefore \quad \frac{\mathrm{d} x}{\mathrm{dt}} \propto x \\
& \therefore \quad \frac{\mathrm{d} x}{\mathrm{dt}}=\mathrm{k} x \\
& \therefore \quad \frac{\mathrm{d} x}{x}=\mathrm{kdt} \\
&
\end{aligned}$
Integrating on both sides, we get
$\log x=\mathrm{kt}+\mathrm{c}... (i)$
When $\mathrm{t}=3, x=10,000$
Equation (i) becomes
$\log (10,000)=3 \mathrm{k}+\mathrm{c}... (ii)$
When $\mathrm{t}=5, x=40,000$
Equation (i) becomes
$\log (40,000)=5 \mathrm{k}+\mathrm{c}... (iii)$
Subtracting (ii) from (iii), we get
$\mathrm{k}=\log 2$
From equation (ii),
$\log (10,000)=3 \log 2+c$
$\therefore \quad c=\log (1250)$
Now, Initially $\mathrm{t}=0$
From (i),
$\log x=\mathrm{k} \times 0+\log (1250)$
$\therefore \quad \log x=\log 1250$
$\therefore \quad x=1250$

</details>

---

### Q30. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The population $\mathrm{P}=\mathrm{P}(\mathrm{t})$ at time $\mathrm{t}$ of certain species follows the differential equation $\frac{\mathrm{dP}}{\mathrm{dt}}=0.5 \mathrm{P}-450$. If $\mathrm{P}(0)=850$, then the time at which population becomes zero is

**Options:**

- **(A)** $2 \log 18$
- **(B)** $\log 9$
- **(C)** $\frac{1}{2} \log 18$
- **(D)** $\log 18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \log 18$**

**Detailed Solution:**

Given differential equation is
$\begin{aligned}
& \quad \frac{\mathrm{dP}}{\mathrm{dt}}=0.5 \mathrm{P}-450 \\
& \quad=\frac{\mathrm{P}}{2}-\frac{900}{2} \\
& \therefore \quad \frac{\mathrm{dP}}{\mathrm{dt}}=\frac{\mathrm{P}-900}{2} \\
& \therefore \quad \frac{2 \mathrm{dP}}{\mathrm{P}-900}=\mathrm{dt} \\
& \quad \text { Integrating on both sides, we get } \\
& 2 \log |\mathrm{P}-900|=\mathrm{t}+\mathrm{c} \\
& \mathrm{P}(0)=850 \text { i.e., } \mathrm{P}=850 \text { when } \mathrm{t}=0 \\
& \mathrm{c}=2 \log 50 \\
& 2 \log |\mathrm{P}-900|=\mathrm{t}+2 \log 50 \\
& \mathrm{When} \mathrm{P}=0, \\
& 2 \log 900=\mathrm{t}+2 \log 50 \\
& \Rightarrow \mathrm{t}=2(\log 900-\log 50) \\
& \quad=2 \log \frac{900}{50}=2 \log 18
\end{aligned}$

</details>

---

### Q31. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A water tank has a shape of inverted right circular cone whose semi-vertical angle is $\tan ^{-1}\left(\frac{1}{2}\right)$. Water is poured into it at constant rate of 5 cubic meter/minute. The rate in meter/minute at which level of water is rising. at the instant when depth of water in the tank is. $10 \mathrm{~m}$ is

**Options:**

- **(A)** $\frac{1}{5 \pi}$
- **(B)** $\frac{1}{15 \pi}$
- **(C)** $\frac{2}{\pi}$
- **(D)** $\frac{1}{10 \pi}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{5 \pi}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/29tgcXGLwISInWjRQYOkRO4ShtEhAQIhyE26NICQrjg.original.fullsize.png">

Semi-vertical angle $=\tan ^{-1}\left(\frac{1}{2}\right)$
Let $\alpha=\tan ^{-1}\left(\frac{1}{2}\right)$
$\tan \alpha=\frac{1}{2}$
$\frac{\mathrm{r}}{\mathrm{h}}=\frac{1}{2}$
$\mathrm{r}=\frac{\mathrm{h}}{2}$
Given, $\frac{d \mathrm{~V}}{\mathrm{dt}}=5 \mathrm{~m}^3 / \mathrm{min}$.
$\mathrm{V}=$ Volume of cone
Volume of cone $=\frac{1}{3} \pi r^2 \mathrm{~h}$
$\mathrm{V}=\frac{1}{3} \pi\left(\frac{\mathrm{h}}{2}\right)^2 \times \mathrm{h}$
$\mathrm{V}=\frac{1}{12} \pi \mathrm{h}^3$
Differentiating w, r.t. t, we get
$\frac{\mathrm{dV}}{\mathrm{dt}}=\frac{1}{12} \times \pi \times 3 \mathrm{~h}^2 \times \frac{\mathrm{dh}}{\mathrm{dt}}$
$5=\frac{1}{4} \pi h^2 \frac{\mathrm{dh}}{\mathrm{dt}}$
$\frac{\mathrm{dh}}{\mathrm{dt}}=\frac{20}{\pi \mathrm{h}^2}$
Now, $\mathrm{h}=10$... [Given]
$\therefore \quad \frac{\mathrm{dh}}{\mathrm{dt}}=\frac{20}{\pi \times(10)^2}$
$\frac{\mathrm{dh}}{\mathrm{dt}}=\frac{1}{5 \pi}$
$\therefore \quad$ Rate of change of water level is $\frac{1}{5 \pi} \mathrm{m} / \mathrm{min}$.

</details>

---

### Q32. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A spherical raindrop evaporates at a rate proportional to its surface area. If originally its radius is $3 \mathrm{~mm}$ and 1 hour later it reduces to $2 \mathrm{~mm}$, then the expression for the radius $\mathrm{R}$ of the raindrop at any time $t$ is

**Options:**

- **(A)** $6R = t + 2$
- **(B)** $R(t+2)=6$
- **(C)** $R = 6(t + 2)$
- **(D)** $6R = t$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $R(t+2)=6$**

**Detailed Solution:**

According to the given conditions, when $\mathrm{t}=0, \mathrm{R}=3$ and when $\mathrm{t}=1, \mathrm{R}=2$
This condition is satisfied by only option (B)

</details>

---

### Q33. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If a body is heated to $110^{\circ} \mathrm{C}$ and placed in air at $10^{\circ} \mathrm{C}$ after 1 hour its temperature is $60^{\circ} \mathrm{C}$, then the additional time required for it to cool to $30^{\circ} \mathrm{C}$ is

**Options:**

- **(A)** $\frac{\log 5}{\log 2} \mathrm{hrs}$
- **(B)** $\frac{\log 2}{\log 5} \mathrm{hrs}$
- **(C)** $\left(\frac{\log 5}{\log 2}-1\right) \mathrm{hrs}$
- **(D)** $\left(\frac{\log 5}{\log 2}+1\right) \mathrm{hrs}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{\log 5}{\log 2}-1\right) \mathrm{hrs}$**

**Detailed Solution:**

$\begin{aligned}
& \frac{\mathrm{d} T}{\mathrm{~d} t}=-K(T-10) \\
& \Rightarrow T-10=e^{-k t+C} \\
& \Rightarrow T=10+e^C \cdot e^{-k t}
\end{aligned}$
For $t=0$,
$\begin{aligned}
& T=110 \\
& \Rightarrow e^C=100 \text { i.e. } \\
& T=10+100 \cdot e^{-k t}
\end{aligned}$
For $t=1$,
$\begin{aligned}
& T=60 \\
& \Rightarrow 60=10+100 \cdot e^{-k \times 1} \\
& \Rightarrow-k=\log \frac{1}{2} \\
& \Rightarrow k=\log 2
\end{aligned}$
$\Rightarrow T=10+100 \cdot e^{-\left(\log _2\right) t}$
Putting $T=30$
$\begin{aligned}
& 30=10+100 \cdot e^{-\left(\log _2\right) t} \\
& \Rightarrow \log \left(\frac{1}{5}\right)=-(\log 2) t \\
& \Rightarrow t=\frac{\log 5}{\log 2}
\end{aligned}$
Additional time $=t-1=\frac{\log 5}{log2}-1$

</details>

---

### Q34. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The assets of a person are increasing at a rate proportional to the square root of the assets at a given time. His assets increase from Rupees 9 crores to Rupees 16 crores in 2 years, then his assets at the end of 5 more years will be

**Options:**

- **(A)** 46.25 cores
- **(B)** 42.25 crores
- **(C)** 30.25 crores
- **(D)** 56.25 crores

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 42.25 crores**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{dx}}{\mathrm{dt}} \propto \sqrt{\mathrm{x}} \\ & \Rightarrow \frac{\mathrm{dx}}{\mathrm{dt}}=\mathrm{k} \sqrt{\mathrm{x}} \\ & \Rightarrow \frac{\mathrm{dx}}{\sqrt{\mathrm{x}}}=\mathrm{kdt} \\ & \Rightarrow 2 \sqrt{\mathrm{x}}=\mathrm{kt}+\mathrm{C}\end{aligned}$
When $\mathrm{t}=0, \mathrm{x}=9$ i.e. $2 \sqrt{9}=\mathrm{k} \times 0+\mathrm{C}$
$$
\begin{aligned}
& \Rightarrow \mathrm{c}=6 \\
& \Rightarrow 2 \sqrt{\mathrm{x}}=\mathrm{kt}+6[\text { Putting } \mathrm{c}=6] \\
& \text { When } \mathrm{t}=2, \mathrm{x}=16 \text { i.e. } 2 \sqrt{16}=\mathrm{k} \times 2+6 \Rightarrow \mathrm{k}=1 \\
& \Rightarrow 2 \sqrt{\mathrm{x}}=\mathrm{t}+6 \text { [Putting } \mathrm{k}=1]
\end{aligned}
After 5 years at $t=7$
$\begin{aligned} & 2 \sqrt{x}=7+6 \\ & \Rightarrow \sqrt{x}=6.5 \\ & \Rightarrow x=42.25\end{aligned}$

</details>

---

### Q35. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A population $\mathrm{P}$ grew at the rate given by the equation $\frac{\mathrm{dp}}{\mathrm{dt}}=0.05 \mathrm{P}$, then the population will become double in

**Options:**

- **(A)** $20(\log 2)$ years
- **(B)** $10(\log 2)$ years
- **(C)** $5(\log 2)$ years
- **(D)** $12(\log 2)$ years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $20(\log 2)$ years**

**Detailed Solution:**

$\begin{aligned}
& \frac{d p}{d t}=0.05 P \\
& \therefore \quad \int \frac{d p}{0.05 p}=\int d t \Rightarrow 20 \int \frac{d p}{P}=\int d t \\
& \therefore \quad 20 \log |P|=t+c \\
& \text { When } t=0, P=P \Rightarrow c=20 \log |P| \\
& \therefore 20 \log |P|=t+20 \log |P|
\end{aligned}$
When $\mathrm{t}=0, \mathrm{P}=\mathrm{P} \Rightarrow \mathrm{c}=20 \log |\mathrm{P}|$
$\therefore 20 \log |\mathrm{P}|=\mathrm{t}+20 \log |\mathrm{P}|$
When population doubles, we write
$\begin{aligned}
& 20 \log |2 \mathrm{P}|=\mathrm{t}+20 \log |\mathrm{P}| \\
& \therefore \quad \mathrm{t}=20 \log |2 \mathrm{P}|-20 \log |\mathrm{P}|=20[\log |2 \mathrm{P}|-\log |\mathrm{P}|] \\
& =20\left[\log \left|\frac{2 \mathrm{P}}{\mathrm{P}}\right|\right] \\
& =20(\log 2 \text { ) years }
\end{aligned}$

</details>

---

### Q36. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Radium decompose at the rate proportional to the amount present at any time. If $\mathrm{P} \%$ of amount disappears in one year, then amount of radium left after 2 years is

**Options:**

- **(A)** $\left(10-\frac{P}{10}\right)^2$
- **(B)** $x_0\left[1+\frac{P}{100}\right]^2$
- **(C)** $x_0\left[1-\frac{P}{100}\right]^2$
- **(D)** $x_0\left[10-\frac{P}{100}\right]^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x_0\left[1-\frac{P}{100}\right]^2$**

**Detailed Solution:**

$\mathrm{P} \%$ amount disappears in one year.
Let initial amount of radium $=\mathrm{x}_0$
$\therefore$ Amount left after 1 year $=\mathrm{x}_0-\frac{\mathrm{P}}{100} \times \mathrm{x}_0=\mathrm{x}_0\left(1-\frac{\mathrm{P}}{100}\right)$
Amount left after 2 years
$$
\begin{aligned}
& =x_0\left(1-\frac{P}{100}\right)-\frac{P}{100} \times x_0\left(1-\frac{P}{100}\right) \\
& =x_0\left(1-\frac{P}{100}\right)\left(1-\frac{P}{100}\right)=x_0\left(1-\frac{P}{100}\right)^2
\end{aligned}
$$

</details>

---

### Q37. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the surrounding air is kept at $25^{\circ} \mathrm{C}$ and a body cools from $80^{\circ} \mathrm{C}$ to $50^{\circ} \mathrm{C}$ in 30 minutes, then temperature of the body after one hour will be

**Options:**

- **(A)** $31.72^{\circ} \mathrm{C}$ approximately
- **(B)** $34.74^{\circ} \mathrm{C}$ approximately
- **(C)** $32.36^{\circ} \mathrm{C}$ approximately
- **(D)** $36.36^{\circ}$ approximately

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $36.36^{\circ}$ approximately**

**Detailed Solution:**

By Newton's law of cooling, we write
$$
\begin{aligned}
& \frac{\mathrm{d} \theta}{\mathrm{dt}} \propto\left(\theta-\theta_0\right) \\
& \therefore \frac{\mathrm{d} \theta}{\mathrm{dt}}=\mathrm{k}\left(\theta-\theta_0\right) \Rightarrow \int\left(\frac{\mathrm{d} \theta}{\theta-\theta_0}\right)=\int \mathrm{kdt} \\
& \therefore \log \left|\theta-\theta_0\right|=\mathrm{kt}+\mathrm{c} \\
& \text { When } \mathrm{t}=0, \theta=80 \text { and } \theta_0=25 \\
& \therefore \log |80-25|=0+\mathrm{c} \quad \Rightarrow \mathrm{c}=\log |55| \\
& \text { When } \mathrm{t}=30, \theta=50 \\
& \therefore \log |50-25|=30 \mathrm{k}+\log |55| \\
& \therefore \mathrm{k}=\frac{1}{30} \log \left|\frac{5}{11}\right|
\end{aligned}
$$
From (1), (2), (3) we write
$$
\log \left|\theta-\theta_0\right|=\frac{1}{30} \log \left|\frac{5}{11}\right| t+\log |55|
$$
When $t=60$, we get
$$
\begin{aligned}
& \log \left|\theta-\theta_0\right|=\frac{60}{30} \log \left|\frac{5}{11}\right|+\log |55| \\
& =\log \left(\left|\frac{5}{11}\right|\right)^2+\log |55|=\log \left|\frac{25}{121} \times 55\right|=\log \left|\frac{125}{11}\right| \\
& \therefore \theta-25=\frac{125}{11} \Rightarrow \theta=36.36^{\circ} \mathrm{C}
\end{aligned}
$$

</details>

---

### Q38. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The velocity of a particle at time $t$ is given by the relation $v=6 \mathrm{t}-\frac{\mathrm{t}^2}{6}$. Its displacement $\mathrm{S}$ is zero at $\mathrm{t}=0$, then the distance travelled in $3 \mathrm{sec}$ is

**Options:**

- **(A)** $\frac{51}{2}$ units
- **(B)** $\frac{39}{2}$ units
- **(C)** $\frac{57}{2}$ units
- **(D)** $\frac{33}{2}$ units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{51}{2}$ units**

**Detailed Solution:**

$\mathrm{v}=6 \mathrm{t}-\frac{\mathrm{t}^2}{6}$ and we know that $\mathrm{v}=\frac{\mathrm{ds}}{\mathrm{dt}}$
$$
\begin{aligned}
& \therefore \int \mathrm{d} s=\int\left(6 \mathrm{t}-\frac{\mathrm{t}^2}{6}\right) \mathrm{dt} \\
& \therefore \mathrm{s}=\frac{6 \mathrm{t}^2}{2}-\frac{\mathrm{t}^3}{6(3)}+\mathrm{c} \Rightarrow \mathrm{s}=3 \mathrm{t}^2-\frac{\mathrm{t}^3}{18}+\mathrm{c}
\end{aligned}
$$
We know that $\mathrm{s}=0$, when $\mathrm{t}=0 \Rightarrow \mathrm{c}=0$
$$
\therefore \mathrm{s}=3 \mathrm{t}^2-\frac{\mathrm{t}^3}{18} \Rightarrow(\mathrm{s})_{\mathrm{t}=3}=3(3)^2-\frac{(3)^3}{18}=\frac{51}{2} \text { units }
$$

</details>

---

### Q39. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Bismuth has half life period of 5 days. A sample originally has a mass of $1000 \mathrm{mg}$, then the mass of Bismuth after 30 days is

**Options:**

- **(A)** 16.625
- **(B)** 13.625
- **(C)** 14.625
- **(D)** 15.625

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 15.625**

**Detailed Solution:**

Half life period of bismuth is 5 days.
Initial mass $=1000 \mathrm{mg}$
$\therefore \quad$ Mass left after 5 days $=500 \mathrm{mg}$
Mass left after 10 days $=250 \mathrm{mg}$
Mass left after 15 days $=125 \mathrm{mg}$
Mass left after 20 days $=62.5 \mathrm{mg}$
Mass left after 25 days $=31.25 \mathrm{mg}$
Mass left after 30 days $=15.625 \mathrm{mg}$

</details>

---

### Q40. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the half life period of a substance is 5 years, then the total amount of the substance left after 15 years, when initial amount is $64 \mathrm{gms}$ is

**Options:**

- **(A)** 8 gms
- **(B)** 16 gms
- **(C)** 2 gms
- **(D)** 32 gms

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8 gms**

**Detailed Solution:**

Half life period $=5$ years
Initial quantity of substance $=64$ grams
$\therefore$ Quantity left after 5 years $=\frac{64}{2}=32$ grams
$\therefore$ Quantity left after 10 years $=\frac{32}{2}=16$ grams
$\therefore$ Quantity left after 15 years $=\frac{16}{2}=8$ grams

</details>

---

### Q41. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A body at an unknow temperature is placed in a room which is held at a constant temperature of $30^{\circ} \mathrm{F}$. If after 10 minutes the temperature of the body is $0^{\circ} \mathrm{F}$ and after 20 minutes the temperature of the body is $15^{\circ} \mathrm{F}$, then the expression for the temperature of the body at any time $t$ is

**Options:**

- **(A)** $\mathrm{T}=-60 \mathrm{e}^{-0.069 \mathrm{t}}-30$
- **(B)** $\mathrm{T}=-60 \mathrm{e}^{-0.03010 \mathrm{t}}+30$
- **(C)** $\mathrm{T}=60 \mathrm{e}^{-0.069 \mathrm{t}}+30$
- **(D)** $\mathrm{T}=60 \mathrm{e}^{-0.069 \mathrm{t}}-30$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{T}=-60 \mathrm{e}^{-0.03010 \mathrm{t}}+30$**

**Detailed Solution:**

We have $\frac{\mathrm{dT}}{\mathrm{dt}} \propto(30-\mathrm{T})$
$$
\begin{aligned}
& \therefore \frac{\mathrm{dT}}{\mathrm{dt}}=-\mathrm{K}(30-\mathrm{T}) \Rightarrow \int \frac{\mathrm{dT}}{30-\mathrm{T}}=\int-\mathrm{Kt} \\
& \therefore \log |30-\mathrm{T}|=-\mathrm{kt}+\mathrm{c}
\end{aligned}
$$
From given data, we write
$$
\begin{aligned}
& \log |30-0|=-10 K+c \\
& \log |30-15|=-20 K+c
\end{aligned}
$$


Solving (2) and (3), we get
$$
\log \left(\frac{30}{15}\right)=10 \mathrm{~K} \Rightarrow \mathrm{K}=\frac{1}{10} \log 2
$$
Substituting value of $\mathrm{K}$ in eq. (2), we get
$$
\log 30=(-10)\left(\frac{\log 2}{10}\right)+\mathrm{c} \Rightarrow \mathrm{c}=\log 60
$$
Thus eq. (1) becomes
$$
\begin{aligned}
& \log |30-\mathrm{T}|=\frac{-\log 2}{10} \mathrm{t}+\log 60 \\
& \therefore \log \left|\frac{30-\mathrm{T}}{60}\right|=\frac{-0.3010}{10} \mathrm{t}=-0.03010 \mathrm{t} \\
& \therefore \frac{30-\mathrm{T}}{60}=\mathrm{e}^{-0.03010 \mathrm{t}} \quad \therefore \mathrm{T}=-60 \mathrm{e}^{-0.03010 \mathrm{t}}+30
\end{aligned}
$$

</details>

---

### Q42. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The population of a city increases at a rate proportional to the population at that time. If the population of the city increase from 20 lakhs to 40 lakhs in 30 years, then after another 15 years the population is

**Options:**

- **(A)** $10 \sqrt{2}$ lakhs
- **(B)** $40 \sqrt{2}$ lakh
- **(C)** $30 \sqrt{2}$ lakhs
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $40 \sqrt{2}$ lakh**

**Detailed Solution:**

We have $\frac{\mathrm{dP}}{\mathrm{dt}} \propto \mathrm{P} \Rightarrow \frac{\mathrm{dP}}{\mathrm{dt}}=\mathrm{kP}$
$$
\therefore \int \frac{\mathrm{dP}}{\mathrm{dt}}=\int \mathrm{k} d t \Rightarrow \log \mathrm{P}=\mathrm{kt}+\mathrm{c}
$$
From given data, we write
$$
\begin{aligned}
& \log 20=\mathrm{k}(0)+\mathrm{c} \Rightarrow \mathrm{c}=\log 20 \\
& \therefore \log \mathrm{P}=\mathrm{kt}+\log 20 \\
& \text { Also } \log 40=30 \mathrm{k}+\log 20 \\
& \therefore \log 40-\log 20=30 \mathrm{k} \Rightarrow \mathrm{k}=\frac{1}{30} \log 2 \\
& \therefore \log \mathrm{P}=\left(\frac{\log 2}{30}\right) \mathrm{t}+\log 20 \\
& \text { When } \mathrm{t}=30+15=45 \\
& \therefore \log \mathrm{P}=\left(\frac{\log 2}{30}\right)(45)+\log 20=(\log 2)\left(\frac{3}{2}\right)+\log 20 \\
& =\log (2)^{\frac{3}{2}}+\log 20=\log (2 \sqrt{2} \times 20) \\
& \therefore \mathrm{P}=40 \sqrt{2} \text { lakhs }
\end{aligned}
$$

</details>

---

### Q43. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An ice ball melts at the rate which is proportional to the amount of ice at that instant. Half the quantity of ice melts in 20 minutes, $\mathrm{x}_0$ is the initial quantity of ice. If after 40 minutes the amount of ice left is $\mathrm{Kx}_0$, then $\mathrm{K}=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{8}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4}$**

**Detailed Solution:**

Half the quantity of ice melts in 20 minutes and $\mathrm{x}_0$ is the initial quantity of ice.
$\therefore$ Quantity after 20 minutes $=\frac{\mathrm{x}_0}{2}$
Quantity after 40 minutes $=\frac{1}{2}\left(\frac{x_0}{2}\right)=\frac{x_0}{4}$

</details>

---

### Q44. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Bismath has half life of 5 days. If sample originally has a mass of $800 \mathrm{mg}$. then the mass remaining after 30 days will be

**Options:**

- **(A)** $10 \mathrm{mg} .$
- **(B)** $10.5 \mathrm{mg} .$
- **(C)** $12 \mathrm{mg} .$
- **(D)** $12.5 \mathrm{mg} .$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12.5 \mathrm{mg} .$**

**Detailed Solution:**

Original mass $=800 \mathrm{mg}$.
Half life $=5$ days.
We have to calculate remaining mass after 30 days. Understand that $30 \div 5=6$.
$\begin{aligned} \therefore \text { Mass remaining } &=\left(\frac{1}{2}\right)^{6} \times 800 \\ &=\frac{800}{64}=\frac{100}{8}=12.5 \end{aligned}$

</details>

---

### Q45. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The population of a village increases at a rate proportional to the population at that time. In a period of 10 years the population grew from 20,000 to 40,000 , then the population after another 20 years is

**Options:**

- **(A)** $1,20,000$
- **(B)** $1,60,000$
- **(C)** $1,00,000$
- **(D)** 80,000

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1,60,000$**

**Detailed Solution:**

We have $\frac{\mathrm{dP}}{\mathrm{dt}} \propto \mathrm{P} \Rightarrow \frac{\mathrm{dP}}{\mathrm{dt}}=\mathrm{kP} \quad \therefore \int \frac{\mathrm{dP}}{\mathrm{P}}=\int \mathrm{kdt} \Rightarrow \log \mathrm{P}=\mathrm{kt}+\log \mathrm{c}$
We have: when $t=0, P=20000$ and when $t=10, P=40000$
$\therefore \quad \log 20000=\log \mathrm{c}$
Now $\log 40000=10 \mathrm{k}+\log 20000$
$\therefore \log \left(\frac{40000}{20000}\right)=10 \mathrm{k} \Rightarrow \mathrm{k}=\frac{1}{10} \log 2$
$\therefore \log P=\left(\frac{1}{10} \log 2\right) t+\log 20000$
When $t=30$, we write
$\log P=\frac{30}{10} \log 2+\log 20000=\log [(8)(20000)]$ $\therefore P=160000$
This problem can also be solved as follows :
From given data, we say that population doubles in 10 years.
$\therefore$ In next 10 years, population changes from 40,000 to 80,000 .
In 10 years after that, population changes from 80000 to 160000

</details>

---

### Q46. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The rate of increase of population of a country is proportional to the number present. If the population doubles in 50 years, then the time taken by it to become four times of it self is

**Options:**

- **(A)** 300 years
- **(B)** 2100 years
- **(C)** 200 years
- **(D)** 400 years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2100 years**

**Detailed Solution:**

We have $\frac{\mathrm{dp}}{\mathrm{dt}} \propto \mathrm{p} \Rightarrow \frac{\mathrm{dp}}{\mathrm{dt}}=\mathrm{kp} \Rightarrow \int \frac{\mathrm{dp}}{\mathrm{p}}=\int \mathrm{kdt}$
$\therefore \log \mathrm{p}=\mathrm{kt}+\mathrm{c}$$\ldots(1)$
When $\mathrm{t}=0, \mathrm{p}=\mathrm{p}_{0}$ (initial population) $\Rightarrow \mathrm{c}=\log \mathrm{p}_{0}$
$\therefore \log \left(\frac{\mathrm{p}}{\mathrm{p}_{0}}\right)=\mathrm{kt}$$\ldots(2)$
When $\mathrm{t}=50, \quad \mathrm{p}=2 \mathrm{p}_{0}$, we get
$\log 2=50 \mathrm{k} \Rightarrow \mathrm{k}=\frac{1}{50} \log 2$
$\therefore \log \left(\frac{\mathrm{p}}{\mathrm{p}_{0}}\right)=\frac{\mathrm{t}}{50} \log 2$
When $\mathrm{p}=4 \mathrm{P}_{0}$
$\log 4=\frac{t}{50} \cdot \log 2 \Rightarrow 2 \log 2=\frac{t}{50} \log 2 \Rightarrow t=100$ years
This problem can also be solved as follows :
Let initial population $=p$
Population doubles in 50 years
$\therefore$ After 50 years, population $=2 \mathrm{p}$
After 100 years, population $=4 \mathrm{p}$

</details>

---

### Q47. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The equation of the curve whose slope at any point is equal to $2 x y$ and which passes through the point $(0,1)$ is

**Options:**

- **(A)** $\cdot \log y=x^{2}$
- **(B)** $\quad \log y=\frac{1}{x}$
- **(C)** $\frac{1}{y}=x$
- **(D)** $\log y=x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\cdot \log y=x^{2}$**

**Detailed Solution:**

We have $\frac{d y}{d x}=2 x y$
$\therefore \int \frac{\mathrm{dy}}{\mathrm{y}}=\int 2 \mathrm{x} \mathrm{dx}$
$\Rightarrow \log y=\frac{2 x^{2}}{2}+C$
$\log y=x^{2}+C$ and curve passes through point $(0,1)$.
At $x=0, y=1$, we get $C=0$
$\therefore \log y=x^{2}$

</details>

---

### Q48. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The rate of disintegration of a radio active element at time $\mathrm{t}$ is proportional to its
mass at that time. Then the time during which the original mass of $1 \cdot 5 \mathrm{gm}$. will
disintegrate into its mass of $0.5 \mathrm{gm}$. is proportional to

**Options:**

- **(A)** $\log 4$
- **(B)** $\log 5$
- **(C)** $\log 3$
- **(D)** $\log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log 3$**

**Detailed Solution:**

(C)
Let $m$ be the mass of the radioactive element at time $t$.
Then the rate of disintegration is $\frac{\mathrm{dm}}{\mathrm{dt}}$ which is proportional to $\mathrm{m}$.
$\therefore \frac{\mathrm{dm}}{\mathrm{dt}} \propto \mathrm{m} \Rightarrow \frac{\mathrm{dm}}{\mathrm{dt}}=-\mathrm{km}$, where $\mathrm{k}>0$ $\therefore \frac{\mathrm{dm}}{\mathrm{m}}=-\mathrm{kdt} \Rightarrow \int \frac{1}{\mathrm{~m}} \mathrm{dm}=-\mathrm{k} \int \mathrm{dt}+\mathrm{c}$
$\therefore \log \mathrm{m}=-\mathrm{kt}+\mathrm{c}$
Initially, i.e. when $\mathrm{t}=0, \mathrm{~m}=1.5$
$\therefore \log (1.5)=-\mathrm{k} \times 0+\mathrm{c} \Rightarrow \mathrm{c}=\log \left(\frac{3}{2}\right)$ $\therefore \log \mathrm{m}=-\mathrm{kt}+\log \left(\frac{3}{2}\right) \Rightarrow \log \mathrm{m}-\log \frac{3}{2}=-\mathrm{kt}$
$\therefore \log \left(\frac{2 m}{3}\right)=-k t$
When $\mathrm{m}=0.5=\frac{1}{2}$, then
$\begin{aligned}
& \log \left(\frac{2 \times \frac{1}{2}}{3}\right)=-\mathrm{kt} \Rightarrow \log \left(\frac{1}{3}\right)=-\mathrm{kt} \Rightarrow-\log 3=-\mathrm{kt} \\
\therefore & t=\frac{1}{k} \log 3
\end{aligned}$
$\therefore$ Thus required time is proportional to $\log 3$.

</details>

---

### Q49. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the population grows at the rate of $8 \%$ per year, then the time taken for the
population to be doubled, is (Given $\log 2=0 \cdot 6912$ )

**Options:**

- **(A)** $6 \cdot 8$ years
- **(B)** $10 \cdot 27$ years
- **(C)** $8 \cdot 64$ years
- **(D)** $4 \cdot 3$ years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8 \cdot 64$ years**

**Detailed Solution:**

(D) $\mathrm{P}_{0}$ be the initial population and let the population after $\mathrm{t}$ years be $2 \mathrm{P}_{0}$. then,
$\begin{aligned}
\frac{\mathrm{dP}}{\mathrm{dt}} &=\frac{8 \mathrm{P}}{100} \Rightarrow \frac{\mathrm{dP}}{\mathrm{dt}}=\frac{2 \mathrm{P}}{25} \\
\therefore \frac{\mathrm{dP}}{\mathrm{P}} &=\frac{2}{25} \mathrm{dt} \Rightarrow \int \frac{1}{\mathrm{P}} \mathrm{dP}=\frac{2}{25} \int \mathrm{dt}
\end{aligned}$
$\log P=\frac{2}{25} t+C$...(1)
At, $t=0, P=P_{0}$
$\log P_{0}=\frac{2 \times 0}{25}+C \Rightarrow C=\log P_{0}$
$\therefore \log P=\frac{2}{25} t+\log P_{0} \Rightarrow \log \frac{P}{P_{0}}=\frac{2}{25} t$
$\therefore t=\frac{25}{2} \cdot \log \left(\frac{P}{P_{0}}\right)$
When $P=2 P_{0}$
$t=\frac{25}{2} \cdot \log \left(\frac{2 P_{0}}{P_{0}}\right)=\frac{25}{2} \log 2=8.64$

</details>

---

### Q50. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A body is heated to $110^{\circ} \mathrm{C}$ and placed in air at $10^{\circ} \mathrm{C}$. After 1 hour its temperature is
$60^{\circ} \mathrm{C}$. The additional time required for it to cool to $30^{\circ} \mathrm{C}$ is

**Options:**

- **(A)** $\left(\frac{\log 2}{\log 5}+1\right)$ hours
- **(B)** $\left(\frac{\log 5}{\log 2}\right)$ hours
- **(C)** $\left(\frac{\log 5}{\log 2}-1\right)$ hours
- **(D)** $\left(\frac{\log 2}{\log 5}\right)$ hours

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{\log 5}{\log 2}-1\right)$ hours**

**Detailed Solution:**

(D)
Let $\theta$ be the temperature of body at time $t$. Temperature of air is given to be $10^{\circ} \mathrm{C}$. $=\theta_{0}$ (say).
$\begin{aligned}
& \frac{\mathrm{d} \theta}{\mathrm{dt}} \propto\left(\theta-\theta_{0}\right) \\
& \frac{\mathrm{d} \theta}{\mathrm{dt}}=-\mathrm{k}\left(\theta-\theta_{0}\right), \mathrm{k}>0 \\
\therefore & \int \frac{\mathrm{d} \theta}{\theta-\theta_{0}}=\int-\mathrm{kt} \quad \Rightarrow \log \left|\theta-\theta_{0}\right|=-\mathrm{kt}+\log \mathrm{c}...(1)
\end{aligned}$
$\therefore\left(\frac{\theta-\theta_{0}}{\mathrm{c}}\right)=\mathrm{e}^{-\mathrm{kt}}$ $\therefore \theta=\theta_{0}+\mathrm{ce}^{-\mathrm{kt}}$ When $\mathrm{t}=0, \theta=110$ and $\theta_{0}=10, \quad \therefore \theta=10+100 \mathrm{e}^{-\mathrm{kt}}$ $\quad 110=10+\mathrm{c} \Rightarrow \mathrm{c}=100 \quad \therefore \quad \mathrm{c}$ When $\theta=60^{\circ} \mathrm{C}, \mathrm{t}=1$ Substituting value in equation (1), $\therefore \quad \log \left(\frac{60-10}{100}\right)=-\mathrm{k} \times 1$ 
$\quad \mathrm{k}=-\log \left(\frac{1}{2}\right)$ 
$\therefore \quad \log \left(\frac{\theta-10}{100}\right)=\mathrm{t} \cdot \log \left(\frac{1}{2}\right)$
When $\theta=30^{\circ} \mathrm{C}$, then
$\log \left(\frac{30-10}{100}\right)=\mathrm{t} \cdot \log \left(\frac{1}{2}\right)$
$\log \left(\frac{20}{100}\right)=t \cdot \log \frac{1}{2}$
$-\log 5=-t \log 2 \Rightarrow t=\frac{\log 5}{\log 2}$
$\therefore$ Additional time required is $\frac{\log 5}{\log 2}-1$

</details>

---

### Q51. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the radius of a circular blot of oil is increasing at the rate of $2 \mathrm{~cm} / \mathrm{min}$, then the rate
of change of its area when its radius is $3 \mathrm{cms}$ is

**Options:**

- **(A)** $10 \pi \mathrm{cm}^{2} / \mathrm{min}$
- **(B)** $12 \pi \mathrm{cm}^{2} / \mathrm{min}$
- **(C)** $14 \pi \mathrm{cm}^{2} / \mathrm{min}$
- **(D)** $16 \pi \mathrm{cm}^{2} / \mathrm{min}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $12 \pi \mathrm{cm}^{2} / \mathrm{min}$**

**Detailed Solution:**

(A)
Given $\frac{\mathrm{dr}}{\mathrm{dt}}=2 \mathrm{~cm} / \mathrm{min}$ and $\mathrm{r}=3 \mathrm{cms}$
Area $=\pi r^{2}$
Differentiating w.r.t. $t$
$\frac{\mathrm{d} \mathrm{A}}{\mathrm{dt}}=\pi \cdot 2 \mathrm{r} \frac{\mathrm{dr}}{\mathrm{dt}}=\pi \times 2(3) \times(2)=12 \pi \mathrm{cm}^{2} / \mathrm{min}$

</details>

---

### Q52. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The bacteria increases at the rate proportional to the number of bacteria present. If
the original number ' $\mathrm{N}^{\prime}$ doubles in 4 hours then the number of bacteria in 12 hours
will be

**Options:**

- **(A)** $3 \mathrm{~N}$
- **(B)** $4 \mathrm{~N}$
- **(C)** $6 \mathrm{~N}$
- **(D)** $8 \mathrm{~N}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 \mathrm{~N}$**

**Detailed Solution:**

(B)
Number of bacteria at the beginning $=N$. The number doubles in every $4 \mathrm{hrs}$.
$\therefore$ Number of bacteria after $4 \mathrm{hrs}=2 \mathrm{~N}$, after $8 \mathrm{hrs}=4 \mathrm{~N}$, after $12 \mathrm{hrs}=8 \mathrm{~N}$

</details>

---

### Q53. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The rate at which the metal cools in moving air is proportional to the difference of tempratures between the metal and air. If the air temperature is $290 \mathrm{~K}$ and the metal temperature drops from $370 \mathrm{~K}$ to $330 \mathrm{~K}$ in 10 minutes, then the time required to drop the temperature upto $295 \mathrm{~K}$ is

**Options:**

- **(A)** 40min
- **(B)** 20min
- **(C)** 35min
- **(D)** 30min

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 40min**

**Detailed Solution:**

(D)
We know that $\frac{\mathrm{dT}}{\mathrm{dt}}=-\mathrm{k}(\mathrm{T}-\mathrm{Tm})$, where
$\mathrm{k}$ is proportionality constant, $\mathrm{T}=$ Temperature of body, $\mathrm{Tm}=$ Temperature of surrounding.
$\therefore \frac{\mathrm{dT}}{\mathrm{dt}}=-\mathrm{k}(\mathrm{T}-290) \Rightarrow \int \frac{\mathrm{dT}}{\mathrm{T}-290}=\int-\mathrm{k} \mathrm{dt}$
$\log |\mathrm{T}-290|=-\mathrm{kt}+\mathrm{C}$
Initially, $\mathrm{t}=0, \mathrm{~T}=370$
$\therefore \log |370-290|=0+C \Rightarrow C=\log |80|$
$\therefore \log |\mathrm{T}-290|=-\mathrm{kt}+\log |80|$
When $\mathrm{t}=10, \mathrm{~T}=330$
$\therefore \log |330-290|=-10 k+\log |80|$
$\therefore \log \left[\left[\frac{40}{80}\right]\right]=-10 \mathrm{k} \Rightarrow \mathrm{k}=\frac{1}{10} \log 2$
$\therefore \log [|T-290|]=-\frac{\log 2}{10} t+\log |80|$
When $\mathrm{T}=295$, we write
$\log [295-290]]=-\frac{\log 2}{10} t+\log 80$
$\therefore \frac{(\log 5-\log 80)}{\log 2} \backslash(-10)=1$
$\frac{\log \left(\frac{1}{10}\right)}{\log 2} \backslash(-10)=1$
$\therefore t=\frac{-4 \log 2}{\log 2} \backslash(-10)$
$=40$

</details>

---

### Q54. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The micro-organisms double themselves in 3 hours. Assuming that the quantity increases at a rate proportional to it self, then the number of times it multiplies themselves in 18 years is

**Options:**

- **(A)** 32
- **(B)** 64
- **(C)** 128
- **(D)** 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 64**

**Detailed Solution:**

(B)
Let initial number of microorganisms be $\mathrm{N}$. The microorganisms double themselves in 3 hours. $\therefore$ Number of microorganisms after
3 hours $=2 \times \mathrm{N}=2 \mathrm{~N}$
o hours $=2 \times 2 \mathrm{~N}=4 \mathrm{~N}$
9 hours $=2 \times 4 \mathrm{~N}=8 \mathrm{~N}$
12 hours $=2 \times 8 \mathrm{~N}=16 \mathrm{~N}$
15 hours $=2 \times 16 \mathrm{~N}=32 \mathrm{~N}$
18 hours $=2 \times 32 \mathrm{~N}=64 \mathrm{~N}$

</details>

---

### Q55. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The rate of decay of certain substance is directly proportional to the amount present at that instant. Initially, there are 27 gms of certain substance and 3 hours later it is found that $8 \mathrm{gms}$ are left, then the amount left after one more hour is

**Options:**

- **(A)** $\frac{19}{3} \mathrm{gms}$
- **(B)** $\frac{20}{3} \mathrm{gmS}$
- **(C)** $\frac{17}{3} \mathrm{gms}$
- **(D)** $\frac{16}{3} \mathrm{gms}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{16}{3} \mathrm{gms}$**

**Detailed Solution:**

(C)
Let $x$ gms be the amount of the substance left at time $t$. Then the rate of decay be $\frac{d x}{d t}$, which is proportional to $x$.
$\begin{array}{l}
\therefore \frac{\mathrm{dx}}{\mathrm{dt}} \propto \mathrm{x} \Rightarrow \frac{\mathrm{dx}}{\mathrm{dt}}=-\mathrm{k} \cdot \mathrm{x}, \text { where } \mathrm{k}>0 \\
\therefore \int \frac{1}{\mathrm{x}} \mathrm{d} \mathrm{x}=\int-\mathrm{k} \cdot \mathrm{dt} \\
\therefore \log \mathrm{x}=-\mathrm{kt}+\mathrm{c} \\
\text { Initially i.e. when } \mathrm{t}=0, \mathrm{x}=27 . \\
\quad \log 27=-\mathrm{k} \times 0+\mathrm{C} \Rightarrow \mathrm{C}=\log 27 \\
\therefore \log \mathrm{x}=-\mathrm{kt}+\log 27 \\
\therefore \log \mathrm{x}-\log 27=-\mathrm{kt} \\
\text { Now, when } \mathrm{t}=3, \mathrm{x}=8
\end{array}$
$\begin{array}{l}
\therefore \quad \log \left(\frac{8}{27}\right)=-3 \mathrm{k} \Rightarrow-3 \mathrm{k}=\log \left(\frac{2}{3}\right)^{3}=3 \log \left(\frac{2}{3}\right) \\
\quad \mathrm{k}=-\log \left(\frac{2}{3}\right) \\
\therefore \quad \log \left(\frac{\mathrm{x}}{27}\right)=\mathrm{t} \cdot \log \left(\frac{2}{3}\right) \\
\text { When } \mathrm{t}=4, \\
\quad \log \left(\frac{\mathrm{x}}{27}\right)=4 \log \left(\frac{2}{3}\right)=\log \left(\frac{2}{3}\right)^{4} \\
\frac{\mathrm{x}}{27}=\frac{16}{81} \Rightarrow \mathrm{x}=\frac{16}{3} \mathrm{gms}
\end{array}$

</details>

---

### Q56. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The bacteria increases at the rate proportional to the number of bacteria present. If the original number 'N' doubles in 4 hours, then the number of bacteria in 12 hours will be

**Options:**

- **(A)** 4N
- **(B)** 3N
- **(C)** 8N
- **(D)** 6N

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8N**

**Detailed Solution:**

108. (C) 
Let $x$ be the number of bacteria at time $t$. 
$\frac{\mathrm{dx}}{\mathrm{dt}} \propto \mathrm{x} \Rightarrow \frac{\mathrm{dx}}{\mathrm{dt}}=\mathrm{kx} \Rightarrow \int \frac{\mathrm{dx}}{\mathrm{x}}=\int \mathrm{k} \cdot \mathrm{dt}$
$\log \mathrm{x}=\mathrm{kt}+\mathrm{c}$
Initially, i.e. when $t=0$, let $x=x_{0}$
$\begin{array}{l}\log x_{0}=k \times 0+c \\ \log x=k t+\log x_{0}\end{array} \quad \Rightarrow c=\log x_{0}$
$\log x-\log x_{0}=k t \quad \Rightarrow \log \left(\frac{x}{x_{0}}\right)=k t$...(1)
Since the number doubles in $4 \mathrm{hrs}$, i.e.
$\begin{aligned}
t &=4 \text { and } x=2 x_{0} \\
\therefore \log \left(\frac{2 x_{0}}{x_{0}}\right) &=4 k \quad \Rightarrow k \quad=\frac{1}{4} \log 2
\end{aligned}$
$\begin{array}{l}
\text { When } t=12, \log \left(\frac{x}{x_{0}}\right)=\frac{12}{4} \log 2=3 \log 2 \\
\therefore \log \left(\frac{x}{x_{0}}\right)=\log 8 \quad \Rightarrow x=8 x_{0}
\end{array}$
This problem can be alternatively solved as follows :
Original number $=\mathrm{N}$.
After four hours, number $=2 \mathrm{~N}$
After eight hours, number $=4 \mathrm{~N}$
After twelve hours, number $=8 \mathrm{~N}$

</details>

---

### Q57. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The growth of population is proportional to the number present. If the population of a colony doubles is 50 years, then the population will become triple in _____ years

**Options:**

- **(A)** $5\left(\frac{\ell \circ g 2}{\ell \operatorname{og} 3}\right) \mathrm{yrs}$
- **(B)** $50\left(\frac{\log 3}{\ell \mathrm{og} 2}\right) \mathrm{yrs}$
- **(C)** $5\left(\frac{\log 3}{\log 2}\right) \mathrm{yrs}$
- **(D)** $50\left(\frac{\log 2}{\ell \mathrm{og} 3}\right) \mathrm{yrs}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $50\left(\frac{\log 3}{\ell \mathrm{og} 2}\right) \mathrm{yrs}$**

**Detailed Solution:**

Let $\mathrm{P}_{0}=$ Initial population
Given $\frac{\mathrm{dP}}{\mathrm{dt}} \propto \mathrm{P} \Rightarrow \frac{\mathrm{dP}}{\mathrm{dt}}=\lambda \mathrm{P} \Rightarrow \int \frac{\mathrm{dP}}{\mathrm{P}}=\int \lambda \mathrm{dt}$
$\log |\mathrm{P}|=\lambda \mathrm{t}+\mathrm{C}\ldots(1)$
At $t=0, \quad P=P_{0}$ we get $\log P_{0}=0+C \Rightarrow C=\log P_{0}$
$\log P=\lambda t+\log P_{0} \Rightarrow \log \left(\frac{P}{P_{0}}\right)=\lambda t$
When $P=2 P_{0}, t=50 \Rightarrow \log \left(\frac{2 P_{0}}{P_{0}}\right)=50 \lambda$
$\therefore \log 2=50 \lambda \Rightarrow \lambda=\frac{1}{50} \log 2$
$\therefore \log \left(\frac{\mathrm{P}}{\mathrm{P}_{0}}\right)=\frac{\mathrm{t}}{50}(\log 2)$
When $\mathrm{P}=3 \mathrm{P}_{0}$ we get
$\log 3=\frac{t}{50}(\log 2) \Rightarrow t=50\left(\frac{\log 3}{\log 2}\right)$ yrs.

</details>

---

### Q58. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Radium decomposes at a rate proportional to the amount present. If half the orignal amount disappears in 1600 yrs, then the percentage loss in 100 years is $\left(\right.$ Given $\left.\log 2=0.6912 \& \mathrm{e}^{-0 \cdot 04320}=0 \cdot 9576\right)$

**Options:**

- **(A)** $3 \cdot 24 \%$
- **(B)** $5 \cdot 24 \%$
- **(C)** $2 \cdot 24 \%$
- **(D)** $4 \cdot 24 \%$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $4 \cdot 24 \%$**

**Detailed Solution:**

Let $R=$ Amount of radium present at time $t$.
We have $\frac{d R}{d t} \displaystyle\propto R \Rightarrow \frac{d R}{t}=k R \quad \rightarrow \int \frac{d R}{k}=\int {kdt}$
$\therefore \log R=kt+C$...(1)
when $t=0$, let $R=R_{0}$ so we get
$\log R_{0}=0+c \Rightarrow c=\log R$
$\log \frac{R}{R_{0}}=kt$
$(\therefore)$
When $t=1600 \mathrm{yrs}, \mathrm{R}=\frac{1}{2} \mathrm{R_{0}}$
$\therefore \log \frac{1}{2} \frac{R_{0}}{R_{0}}=1000 \Rightarrow \log \frac{1}{2}-1000 k$ $\therefore k=\frac{1}{1000} \log \frac{1}{2}-\frac{1}{1000}\left(0-k g_{2}\right)=\frac{-00012}{1000}$ 
$\therefore k=-0.000432t$
When t $=100$, we get
$\therefore \log \frac{R}{R_{0}}=-0.0432 \Rightarrow \frac{R}{R_{0}}=e^{-4043}$
$\therefore \frac{R}{R_{0}}=0.9576 \Rightarrow R=0.9576 R_{0}$
$\% \operatorname{loss}=\frac{R_{0}-0.9576 R_{0}}{R_{0}} \times 100 \%$
$=0.0424 \times 100 \%=4.24 \%$

</details>

---

### Q59. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The rate of decay of mass of a certain substance at time 't' is proportional to the
mass at that instant. The time during which the original mass of $m_{0}$ gm. will be left to $m_{1} \mathrm{gm}$. is 
(K is constant of proportionality)

**Options:**

- **(A)** $\mathrm{K} \log \left(\frac{m_{1}}{m_{0}}\right)$
- **(B)** $\left(\frac{1}{\mathrm{~K}}\right) \log \left(\frac{m_{1}}{m_{0}}\right)$
- **(C)** $\left(\frac{1}{\mathrm{~K}}\right) \log \left(\frac{m_{0}}{m_{1}}\right)$
- **(D)** $\mathrm{K} \log \left(\frac{m_{0}}{m_{1}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\frac{1}{\mathrm{~K}}\right) \log \left(\frac{m_{0}}{m_{1}}\right)$**

**Detailed Solution:**

Given $\frac{\mathrm{dm}}{\mathrm{dt}} \propto \mathrm{m} \Rightarrow \frac{\mathrm{dm}}{\mathrm{dt}}=-\mathrm{Km} \Rightarrow \int \frac{\mathrm{dm}}{\mathrm{m}}=\int-\mathrm{Kdt}$
$\therefore \log \mathrm{m}=-\mathrm{Kt}+\mathrm{c}$
When $\mathrm{t}=0, \mathrm{~m}=\mathrm{m}_{0}$
$\therefore \log \mathrm{m}_{0}=0+\mathrm{c} \Rightarrow \mathrm{c}=\log \mathrm{m}_{0}$
$$
\log \mathrm{m}=-\mathrm{Kt}+\log \mathrm{m}_{0}
$$
$\therefore \log \left(\frac{\mathrm{m}}{\mathrm{m}_{0}}\right)=-\mathrm{Kt}$
When $\mathrm{m}=\mathrm{m}_{1}$, we get
$$
\log \left(\frac{\mathrm{m}_{1}}{\mathrm{~m}_{0}}\right)=-\mathrm{Kt}
$$
$\quad \mathrm{t}=\frac{-1}{\mathrm{~K}} \log \left(\frac{\mathrm{m}_{1}}{\mathrm{~m}_{0}}\right)=\frac{1}{\mathrm{~K}} \log \left(\frac{\mathrm{m}_{0}}{\mathrm{~m}_{1}}\right)$

</details>

---

### Q60. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation whose solution is $y=c_{1} \operatorname{cosax}+c_{2} \operatorname{sinax}\left(\right.$ Where $c_{1}$
and $c_{2}$ are arbitrary constants) is

**Options:**

- **(A)** $\frac{d^{2} y}{d x^{2}}-a^{2} y=0$
- **(B)** $\frac{d^{2} y}{d x^{2}}+a^{2} y=0$
- **(C)** $\frac{d^{2} y}{d x^{2}}+a y^{2}=0$
- **(D)** $\frac{d^{2} y}{d x^{2}}+y^{2}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{d^{2} y}{d x^{2}}+a^{2} y=0$**

**Detailed Solution:**

Given $y=c_{1} \cos a x+c_{2} \sin a x$
$\therefore \frac{d y}{d x}=-a c_{1} \sin a x+a c_{2} \cos a x$
$\begin{aligned} \therefore y\left(\frac{1}{1-x^{2}}\right) &=\int \frac{x}{\left(1-x^{2}\right)^{\frac{1}{2}}} \times \frac{1}{\left(1-x^{2}\right)} d x \\ &=\frac{-1}{2} \int \frac{-2 x}{\left(1-x^{2}\right)^{3 / 2}} d x=\left(-\frac{1}{2}\right) \frac{\left(1-x^{2}\right)^{\frac{1}{2}}}{\left(-\frac{1}{2}\right)}+c \\ y\left(\frac{1}{1-x^{2}}\right) &=\frac{1}{\sqrt{1-x^{2}}}+c \Rightarrow y=\sqrt{1-x^{2}}+c\left(1-x^{2}\right) \end{aligned}$

</details>

---

### Q61. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The population $\mathrm{P}(\mathrm{t})$ of a certain mouse species at time $\mathrm{t}$ satisfies the differential equation $\frac{d P(t)}{d t}=0 \cdot 5 P(t)-450 \cdot$ If $\mathrm{P}(0)=850$, then the time at which the population becomes zero is

**Options:**

- **(A)** $\left(\frac{1}{2}\right) \log 18$
- **(B)** $\log 18$
- **(C)** $2 \log 18$
- **(D)** $\log 9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \log 18$**

**Detailed Solution:**

$\frac{\mathrm{dp}(\mathrm{t})}{\mathrm{dt}}=0.5 \mathrm{p}(\mathrm{t})-450$
$\frac{\mathrm{dp}(\mathrm{t})}{\mathrm{dt}}=\frac{1}{2} \mathrm{p}(\mathrm{t})-450 \Rightarrow \frac{\mathrm{dp}(\mathrm{t})}{\mathrm{dt}}=\frac{\mathrm{p}(\mathrm{t})-900}{2}$
$\therefore 2 \int \frac{\mathrm{d}[\mathrm{p}(\mathrm{t})]}{\mathrm{p}(\mathrm{t})-900}=\int \mathrm{dt} \Rightarrow 2 \log |\mathrm{p}(\mathrm{t})-900|=\mathrm{t}+\mathrm{c}$
When $\mathrm{t}=0, \mathrm{p}(\mathrm{t})=850$
$\therefore 2 \log |850-900|=0+\mathrm{c} \Rightarrow \mathrm{c}=2 \log 50$
$\therefore 2 \log |\mathrm{p}(\mathrm{t})-900|=\mathrm{t}+2 \log 50$
When $\mathrm{p}(\mathrm{t})=0$, we write
$2 \log |0-900|=\mathrm{t}+2 \log 50$
$\therefore \mathrm{t}=2 \log \left|\frac{900}{50}\right|$
$\mathrm{t} \quad=2 \log 18$

</details>

---

### Q62. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The rate of decay of mass of certain substance at time tis proportional to the
tt that instant. The time during which the original mass of $m_{0}$ gram will be leftht
$m_{\text {, gram is }} \quad(k$ is constant of proportionality

**Options:**

- **(A)** $\frac{1}{k} \log \left(\frac{m_{1}}{m_{0}}\right)$
- **(B)** $k \log \left(\frac{m_{0}}{m_{1}}\right)$
- **(C)** $k \log \left(\frac{m_{1}}{m_{0}}\right)$
- **(D)** $\frac{1}{k} \log \left(\frac{m_{0}}{m_{1}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{k} \log \left(\frac{m_{0}}{m_{1}}\right)$**

**Detailed Solution:**

Let $m$ be the initial mass of substance at time $t$.
$$
\begin{array}{l}
\therefore \frac{\mathrm{dm}}{\mathrm{dt}} \propto \mathrm{km} \Rightarrow \frac{\mathrm{dm}}{\mathrm{dt}}=-\mathrm{km} \quad \Rightarrow \int \frac{\mathrm{dm}}{\mathrm{m}}=\int-\mathrm{k} \mathrm{dt} \\
\therefore \log \mathrm{m}=-\mathrm{kt}+\mathrm{c}....(1) \\
\text { When } \mathrm{t}=0, \mathrm{~m}=\mathrm{m}_{0} \text { we get } \\
\log \mathrm{m}_{0}=0+\mathrm{c} \Rightarrow \mathrm{c}=\log \mathrm{m}_{0} \\
\text { From }(1), \log \left(\frac{\mathrm{m}}{\mathrm{m}_{0}}\right)=-\mathrm{kt} \Rightarrow \mathrm{t}=\frac{-1}{\mathrm{k}} \log \left(\frac{\mathrm{m}}{\mathrm{m}_{0}}\right)
\end{array}
$$
$$
\begin{array}{l}
\text { When } m=m_{1} \text {, we get } \\
\qquad \begin{aligned}
t &=\frac{-1}{k} \log \left(\frac{m_{1}}{m_{0}}\right) \Rightarrow t=\frac{1}{k} \log \left(\frac{m_{0}}{m_{1}}\right)
\end{aligned}
\end{array}
$$

</details>

---

### Q63. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the population grows at the rate $5 \%$ peryear, then the time taken for the population
to become double is $\quad$ (Given $\log 2=0.6912$ )

**Options:**

- **(A)** $13.8275$ years
- **(B)** $13.624$ years
- **(C)** 13.725 years
- **(D)** $13.8240$ years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $13.8240$ years**

**Detailed Solution:**

Let initial population $=P_{0}$ and let $P$ be the population at time $t$ We have $\frac{\mathrm{dP}}{\mathrm{dt}}=\frac{5 \mathrm{P}}{100}$
$\therefore \frac{d P}{d t}=\frac{P}{20} \Rightarrow \int \frac{d P}{P}=\int \frac{1}{20} d t$
$\therefore \log P=\frac{1}{20} t+C$....(1)
When $t=0, P=P_{0}$
$\therefore \log \mathrm{P}_{0}=0+\mathrm{C} \Rightarrow \mathrm{C}=\log \mathrm{P}_{0}$
From (1), $\log \left(\frac{P}{P_{0}}\right)=\frac{t}{20}$....(2)
When $P=2 P_{0}$, we get
$\log 2=\frac{t}{20} \Rightarrow t=20(\log 2)=20 \times 0.6912=13.8240$ years

</details>

---

### Q64. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the radius of a circle increases at the rate of $7 \mathrm{~cm} / \mathrm{sec}$, then the rate of increase of
its area after 10 minutes is

**Options:**

- **(A)** $1,84,800 \mathrm{~cm}^{2} / \mathrm{sec}$
- **(B)** $1,64,800 \mathrm{~cm}^{2} / \mathrm{sec}$
- **(C)** $1,88,400 \mathrm{~cm}^{2} / \mathrm{sec}$
- **(D)** $1,68,400 \mathrm{~cm}^{2} / \mathrm{sec}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1,84,800 \mathrm{~cm}^{2} / \mathrm{sec}$**

**Detailed Solution:**

$\begin{aligned} \frac{d \varepsilon}{d t} &=7 \mathrm{~cm} / \mathrm{sec} . \\ A &=\pi \varepsilon^{2} \\ \frac{d A}{d t} &=2 \pi \varepsilon \frac{d \varepsilon}{d t}-(1) \\ \text { Radius after } 10 \text { minutes } ; & \varepsilon=70 \mathrm{~cm} \times 60 \mathrm{~cm} \\ \frac{d A}{d t} &=2 \times \frac{22}{7} \times 70 \times 7 \times 60[\mathrm{Put} \text { in (1)... }\\ &=1,84,800 \mathrm{~cm}^{2} / \mathrm{sec} . \end{aligned}$

</details>

---

### Q65. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Bacteria increases at the rate proportional to the number of bacteria present. If the
original number N doubles in 4 hours, then the number of bacteria will be $4 \mathrm{~N}$ in

**Options:**

- **(A)** 2 hours
- **(B)** 4 hours
- **(C)** 6 hours
- **(D)** 8 hours

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8 hours**

**Detailed Solution:**

Let $\mathrm{N}$ be the number of bacteria present at time $t_{0}$. Let $\mathrm{N}_{0}$ be the initial number of bacteria. Here $\frac{\mathrm{dN}}{\mathrm{dt}} \alpha \mathrm{N} \Rightarrow \frac{\mathrm{dN}}{\mathrm{dt}}=\mathrm{KN} \Rightarrow \frac{\mathrm{dN}}{\mathrm{N}}=\mathrm{K} \mathrm{dt}$
$\therefore \int \frac{\mathrm{dN}}{\mathrm{N}}=\mathrm{K} \int \mathrm{dt} \Rightarrow \log \mathrm{N}=\mathrm{Kt}+\mathrm{C}$
When $\mathrm{t}=0, \mathrm{~N}=\mathrm{N}_{0}$
$$
\therefore \log N_{0}=C \Rightarrow \log \left(\frac{N}{N_{0}}\right)=K t
$$
When $t=4, N=2 N_{0} \Rightarrow 4 K=\log 2$
$$
\begin{array}{l}
\mathrm{K}=\frac{1}{4} \log 2 \\
\therefore \log \left(\frac{\mathrm{N}}{\mathrm{N}_{0}}\right)=\frac{\mathrm{t}}{4} \log 2
\end{array}
$$
When $\mathrm{N}=4 \mathrm{~N}_{0}$, we get
$$
\log 4=\frac{t}{4} \log 2 \Rightarrow 2(\log 2)=\frac{t}{4}(\log 2) \Rightarrow t=8 \text { hours }
$$
This problem can also be saved as follows :
Number of bacteria doubles in 4 hrs.
$\therefore$ If initial number of bacteria are $N$, then
After 4 hours number of bacteria become $2 \mathrm{~N}$.
After 8 hours, number of bacteria becomes $4 \mathrm{~N}$

</details>

---

### Q66. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the population grows at the rate of $8 \%$ per year, then the time taken for the
population to be doubled is $\quad$ (given $\log 2=0 \cdot 6912$ )

**Options:**

- **(A)** $8.64$ years
- **(B)** 6.8 years
- **(C)** $10.27$ years
- **(D)** $4 \cdot 3$ years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $8.64$ years**

**Detailed Solution:**

Let $P_{0}$ be the initial population and let the population after $t$ years be $2 P_{0}$. then, 
$\begin{aligned} \frac{\mathrm{dP}}{\mathrm{dt}} &=\frac{8 \mathrm{P}}{100} \Rightarrow \frac{\mathrm{dP}}{\mathrm{dt}}=\frac{2 \mathrm{P}}{25} \\ \therefore \frac{\mathrm{dP}}{\mathrm{P}} &=\frac{2}{25} \mathrm{dt} \Rightarrow \int \frac{1}{\mathrm{P}} \mathrm{dP}=\frac{2}{25} \int \mathrm{dt} \\ \log \mathrm{P} &=\frac{2}{25} \mathrm{t}+\mathrm{C}....(1) \end{aligned}$
$$
\begin{array}{l}
\text { At, } t=0, P=P_{0} \\
\log P_{0}=\frac{2 \times 0}{25}+C \Rightarrow C=\log P_{0} \\
\therefore \log P=\frac{2}{25} t+\log P_{0} \Rightarrow \log \frac{P}{P_{0}}=\frac{2}{25} t \\
\therefore t=\frac{25}{2} \cdot \log \left(\frac{P}{P_{0}}\right)
\end{array}
$$
When $\mathrm{P}=2 \mathrm{P}_{0}$
$t=\frac{25}{2} \cdot \log \left(\frac{2 P_{0}}{P_{0}}\right)=\frac{25}{2} \log 2=8.64$

</details>

---

### Q67. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A metal has half life period of 10 days, $A$ sample originally has a mass of $1000 \mathrm{mg}$,
then the mass remaining after 50 days is

**Options:**

- **(A)** $\frac{225}{8} m g$
- **(B)** $\frac{125}{8} \mathrm{mg}$
- **(C)** $\frac{125}{4} \mathrm{mg}$
- **(D)** $\frac{225}{4} m g$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{125}{4} \mathrm{mg}$**

**Detailed Solution:**

A mass has half life period of 10 days. It means every ten days, mass remaining is half of the mass before 10 days.
Initial mass $=1000 \mathrm{mg}$.
$\therefore$ Mass after, 10 days $=\frac{1}{2} \times 1000=500 \mathrm{mg}$
Mass after 20 days $=\frac{1}{2} \times 500=250 \mathrm{mg}$
Mass after 30 days $=\frac{1}{2} \times 250=125 \mathrm{mg}$
Mass after 40 days $=\frac{1}{2} \times 125=\frac{125}{2} \mathrm{mg}$
Mass after 50 days $=\frac{1}{2} \times \frac{125}{2}=\frac{125}{4} \mathrm{mg}$

</details>

---

### Q68. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the population grows at the rate of $5 \%$ per year, then the time taken for the
population to become double is (Given $\log 2=0.6912$ )

**Options:**

- **(A)** $13.624$ years
- **(B)** $13 \cdot 8240$ years
- **(C)** $13.725$ years
- **(D)** $13.8275$ years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $13 \cdot 8240$ years**

**Detailed Solution:**

Let $\mathrm{P}$ be the population at time $\mathrm{t}$ and $\mathrm{P}_{0}$ be the initial population. $\begin{aligned} \text { Given } \frac{\mathrm{dP}}{\mathrm{dt}} &=\frac{5 \mathrm{P}}{100} \Rightarrow \int \frac{\mathrm{dP}}{\mathrm{P}}=\int \frac{1}{20} \mathrm{dt} \\ \log \mathrm{P} &=\frac{1}{20} \mathrm{t}+\mathrm{c} ...(1) \end{aligned}$
We have $t=0, P=P_{0}$
$\therefore \log \mathrm{P}_{0}=\mathrm{c}$
$\therefore \log \mathrm{P} \quad=\frac{\mathrm{t}}{20}+\log \mathrm{P}_{0}$
$\therefore \log \left(\frac{\mathrm{P}}{\mathrm{P}_{0}}\right)=\frac{\mathrm{t}}{20}$ ...(2)
When $P=2 P_{0}$, we write
$\log \left(\frac{2 P_{0}}{P_{0}}\right)=\frac{t}{20} \Rightarrow \log 2=\frac{t}{20}$ $t=20(0.6912)=13.824$ years

</details>

---

### Q69. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Water at $100^{\circ} \mathrm{C}$ cools in 15 minutes to $75^{\circ} \mathrm{C}$ in a room temperature of $25^{\circ} \mathrm{C}$. Then the
temperature of water after 30 minutes is

**Options:**

- **(A)** $\left(\frac{400}{9}\right)^{\circ} \mathrm{C}$
- **(B)** $\left(\frac{526}{9}\right)^{\circ} \mathrm{C}$
- **(C)** $\left(\frac{335}{9}\right)^{\circ} \mathrm{C}$
- **(D)** $\left(\frac{175}{3}\right)^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{175}{3}\right)^{\circ} \mathrm{C}$**

**Detailed Solution:**

Let $\theta^{\circ} \mathrm{C}$ be the temperature of water at time $\mathrm{t}$ min. Room temperature is given $25^{\circ} \mathrm{C}$. then by Newton's law of cooling $\frac{-d \theta}{d t} \propto(\theta-25)$
$\therefore \frac{\mathrm{d} \theta}{\mathrm{dt}}=-\mathrm{K}(\theta-25)$ where $\mathrm{K}>0$
$\therefore \frac{\mathrm{d} \theta}{\theta-25}=-\mathrm{K} \mathrm{dt} \Rightarrow \int \frac{\mathrm{d} \theta}{\theta-25}=-\mathrm{K} \int \mathrm{dt}$
$\log (\theta-25)=-\mathrm{Kt}+\mathrm{c}$ $\ldots(1)$
When $\mathrm{t}=0, \theta=100^{\circ}$
$\therefore \log 75=\mathrm{c}$
$\therefore$ from (1) $\log (\theta-25)=-\mathrm{K} t+\log 75$
$\therefore \log \left(\frac{\theta-25}{75}\right)=-\mathrm{Kt}$ $\ldots(2)$
When $t=15, \theta=75^{\circ}$
$\begin{aligned}
& \log \left(\frac{50}{75}\right)=-15 \mathrm{~K} \Rightarrow \mathrm{K}=\frac{-1}{15} \log \left(\frac{2}{3}\right) \\
\therefore & \log \left(\frac{\theta-25}{75}\right)=\frac{\mathrm{t}}{15} \log \left(\frac{2}{3}\right) ...[from 2] \\
\text { When } \mathrm{t}=30^{\circ} & \log \left(\frac{\theta-25}{75}\right)=\frac{30}{15} \log \left(\frac{2}{3}\right) \\
& \log \left(\frac{\theta-25}{75}\right)=2 \log \left(\frac{2}{3}\right)=\log \left(\frac{2}{3}\right)^{2}=\log \left(\frac{4}{9}\right) \\
\therefore & \frac{\theta-25}{75}=\frac{4}{9} \Rightarrow \theta=\frac{525}{9}=\left(\frac{175}{3}\right)^{\circ} \mathrm{C}
\end{aligned}$

</details>

---

### Q70. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a certain culture of bacteria, the rate of increase is proportional to the number
present. It is found that the number doubles in 4 hours. Then the number of times
the bacteria are increased in 12 hours is

**Options:**

- **(A)** 6
- **(B)** 8
- **(C)** 12
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

Let $x$ be the number of bacteria in certain culture at time $t$. Then rate of increase is $\frac{d x}{d t}$ which is proportional to $x$.
$\begin{array}{l}
\therefore \frac{\mathrm{dx}}{\mathrm{dt}} \propto \mathrm{x} \Rightarrow \frac{\mathrm{dx}}{\mathrm{dt}}=\mathrm{Kx} \Rightarrow \frac{\mathrm{dx}}{\mathrm{x}}=\mathrm{Kdt} \Rightarrow \int \frac{\mathrm{dx}}{\mathrm{x}}=\mathrm{K} \int \mathrm{dt} \\
\therefore \log \mathrm{x}=\mathrm{Kt}+\mathrm{c} ...(1)\\
\text { Initially when } \mathrm{t}=0, \operatorname{let} \mathrm{x}=\mathrm{x}_{0} \\
\therefore \log \mathrm{x}=0+\mathrm{c} \Rightarrow \mathrm{c}=\log \mathrm{x}_{0} \\
\therefore \text { from }(1) \log \mathrm{x}=\mathrm{kt}+\log \mathrm{x}_{0} \\
\therefore \log \left(\frac{\mathrm{x}}{\mathrm{x}_{0}}\right)=\mathrm{Kt}...(2)
\end{array}$
Given number doubles in 4 hrs i.e. when $t=4, x=2 x_{0}$ $\therefore \log \left(\frac{2 \mathrm{x}_{0}}{\mathrm{x}_{0}}\right)=4 \mathrm{~K} \Rightarrow \mathrm{K}=\frac{1}{4} \log 2$
$\therefore$ from (2) $\log \left(\frac{x}{x_{0}}\right)=\frac{t}{4} \log 2$
When $\mathrm{t}=12$
$\log \left(\frac{x}{x_{0}}\right)=\frac{12}{4} \log 2=3 \log 2=\log 2^{3}=\log 8$
$\therefore \frac{x}{x_{0}}=8 \Rightarrow x=8 x_{0}$
This problem can be alternatively solved as follows :
Let the intial number of bacteria be $\mathrm{x}$.
$\therefore$ Number of bacteria after $4 \mathrm{hrs}=2 \mathrm{x}$
Number of bacteria after $8 \mathrm{hrs}=2(2 \mathrm{x})=4 \mathrm{x}$
Number of bacteria after $12 \mathrm{hrs}=2(4 \mathrm{x})=8 \mathrm{x}$

</details>

---

### Q71. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A body cools according to Newton's law from $100^{\circ} \mathrm{C}$ to $60^{\circ} \mathrm{C}$ in 20 minutes. The
temperature of the surrounding being $20^{\circ} \mathrm{C}$ then the temperature of the body after
one hour is

**Options:**

- **(A)** $15^{\circ} \mathrm{C}$
- **(B)** $30^{\circ} \mathrm{C}$
- **(C)** $40^{\circ} \mathrm{C}$
- **(D)** $20^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $30^{\circ} \mathrm{C}$**

**Detailed Solution:**

Let $\theta^{\prime} \mathrm{C}$ be the temperature of the body at time t. The temperature of surrounding is $20^{\circ} \mathrm{C}$.
According to Newton's law of cooling
$\frac{d \theta}{d t} \propto(\theta-20) \Rightarrow \frac{d \theta}{d t}=-K(\theta-20), \quad$ where $K>0$
$\therefore \int \frac{d \theta}{\theta-20}=\int-K d t \Rightarrow \log |\theta-20|=-K t+c$
We have $\theta=100$ and $t=0$
$\therefore \log |100-20|=0+c \Rightarrow c=\log 80$
$\therefore \log |\theta-20|=-\mathrm{Kt}+\log 80$
$\therefore \log \left|\frac{\theta-20}{80}\right|=-\mathrm{Kt}$
When $t=20, \theta=60$
$\therefore K=\frac{-1}{20} \log \left(\frac{1}{2}\right)$
Thus $\log \left(\frac{\theta-20}{80}\right)=\frac{\mathrm{t}}{20} \log \left(\frac{1}{2}\right)$
When $t=60$
$\log \left(\frac{\theta-20}{80}\right)=3 \log \left(\frac{1}{2}\right)=\log \left(\frac{1}{8}\right) \Rightarrow \frac{\theta-20}{80}=\frac{1}{8} \Rightarrow \theta=30^{\circ}$

</details>

---

### Q72. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The rate of growth of bacteria is proportional to the bacteria present. If it is found
that the number doubles in 3 hours, then the number of times the bacteria are
increased in 6 hours is

**Options:**

- **(A)** 6 times the original
- **(B)** 4 times the original
- **(C)** 8 times the original
- **(D)** 5 times the original

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4 times the original**

**Detailed Solution:**

Let $b$ be the number of bacteria.
We have $\frac{\mathrm{db}}{\mathrm{dt}} \propto \mathrm{b} \Rightarrow \int \frac{\mathrm{db}}{\mathrm{b}}=\int \mathrm{Kdt}$
$\therefore \log \mathrm{b}=\mathrm{Kt}+\mathrm{c}$ ...(1)
Let $b_{0}$ be the initial number of bacteria. At $t=0, b=b_{0}$
$\log \mathrm{b}_{0}=\mathrm{K}(0)+\mathrm{c} \Rightarrow \mathrm{c}=\log \mathrm{b}_{0}$
$\therefore \log \left(\frac{b}{b_{0}}\right)=\mathrm{Kt}$ ...(2)
When $t=3, b=2 b_{0}$
$\therefore \log \left(\frac{2 b_{0}}{b_{0}}\right)=3 K \Rightarrow K=\frac{1}{3}(\log 2)$
Thus $\log b=\frac{1}{3}(\log 2) t+\log b_{0}$
When $\mathrm{t}=6$
$\log \left(\frac{b}{b_{0}}\right)=2 \log 2=\log 4 \Rightarrow \frac{b}{b_{0}}=4 \Rightarrow b=4 b_{0}$
This problem can also be solved as follows :
The number of bacteria doubles in 3 hours.
Let initial number of bacteria $=\mathrm{N}$.
$\therefore$ After 3 hours, number of bacteria $=2 \mathrm{~N}$.
After 6 hours, number of bacteria $=4 \mathrm{~N}$.

</details>

---

### Q73. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The rate of growth of bacteria is proportional to number present. If initially there
were 1000 bacteria and the number doubles in 1 hour then the number of bacteria
after $2 \frac{1}{2}$ hours are (Given $\sqrt{2}=1.414$ )

**Options:**

- **(A)** 4646 approximately
- **(B)** 5056 approximately
- **(C)** 5656 approximately
- **(D)** $400 \sqrt{2}$ approximately

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5656 approximately**

**Detailed Solution:**

The rate of growth is proportional to the number present
$\therefore \frac{\mathrm{d} \mathrm{N}}{\mathrm{dt}} \propto \mathrm{N} \Rightarrow \frac{\mathrm{d} \mathrm{N}}{\mathrm{dt}}=\mathrm{kN} \Rightarrow \frac{\mathrm{d} \mathrm{N}}{\mathrm{N}}=\mathrm{k} \mathrm{dt}$
$\therefore$ On integrating we get
$\int \frac{\mathrm{dN}}{\mathrm{N}}=\mathrm{k} \int \mathrm{dt}$
$\therefore \log \mathrm{N}=\mathrm{kt}+\mathrm{C}$
When $\mathrm{t}=0, \mathrm{~N}=1000 \Rightarrow \mathrm{C}=\log 1000$
$\therefore \log \mathrm{N}=\mathrm{kt}+\log 1000$
$\therefore \quad \log \left(\frac{\mathrm{N}}{1000}\right)=\mathrm{kt}$
$\mathrm{N}=1000 \mathrm{e}^{\mathrm{kt}}$ ...(1)
When $\mathrm{t}=1, \mathrm{~N}=2000$
$\therefore \mathrm{e}^{\mathrm{k}}=2 \quad \Rightarrow \mathrm{N}=1000 \times 2^{1} \quad \ldots[$ from (1) $]$
When $t=2 \frac{1}{2}$, we get
$\mathrm{N}=1000 \times 2^{\frac{5}{2}}=1000 \times 4 \sqrt{2}$
$=1000 \times 4 \times 1.414=5656$

</details>

---

### Q74. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>m</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></msup><mi mathvariant="normal"> </mi><mi mathvariant="normal"> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal"> </mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>A</mi><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>,</mo></math> then <math><mi>A</mi><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mi>m</mi></math>
- **(B)** <math><mo>–</mo><mi>m</mi></math>
- **(C)** <math><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mo>-</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

Given,  <math><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>m</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></msup></math> 
 <math><mo>⇒</mo><mi> </mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>m</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></msup><mo>&sdot;</mo><mi>m</mi><mo>&sdot;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mi>A</mi><mo>=</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

</details>

---

