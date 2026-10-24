# MHT CET Mathematics - Basic of Mathematics

## Topic 1: Ratio and Proportion

**Total Questions:** 5

---

### Q1. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The assets of a person are reduced in his business such that the rate of reduction is proportional to the square root of the existing assets. If the assets were initially ₹ $10,00,000$ and due to loss they reduce to ₹ 10,000 after 3 years, then the number of years required for the person to go bankrupt will be

**Options:**

- **(A)** $\frac{10}{3}$
- **(B)** $\frac{10}{9}$
- **(C)** $\frac{20}{9}$
- **(D)** $\frac{20}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{10}{3}$**

**Detailed Solution:**

Let $A$ be the assets of the person at time $t$ (in years).

Given that the rate of reduction of assets is proportional to the square root of the existing assets, we can write the differential equation as:

$\dfrac{dA}{dt} = -k\sqrt{A}$

Separating the variables and integrating both sides:

$\int \dfrac{dA}{\sqrt{A}} = \int -k dt$

$2\sqrt{A} = -kt + C$

Initially, at $t = 0$, the assets are $A = 10,00,000 = 10^6$. Substituting these values:

$2\sqrt{10^6} = -k(0) + C$

$2(1000) = C \Rightarrow C = 2000$

The equation becomes:

$2\sqrt{A} = -kt + 2000$

After $3$ years, at $t = 3$, the assets reduce to $A = 10,000 = 10^4$. Substituting these values:

$2\sqrt{10^4} = -k(3) + 2000$

$2(100) = -3k + 2000$

$200 = -3k + 2000$

$3k = 1800 \Rightarrow k = 600$

The equation for the assets at any time $t$ is:

$2\sqrt{A} = -600t + 2000$

For the person to go bankrupt, the assets must become zero, so $A = 0$. Substituting $A = 0$ into the equation:

$2\sqrt{0} = -600t + 2000$

$0 = -600t + 2000$

$600t = 2000$

$t = \dfrac{2000}{600} = \dfrac{10}{3}$ years

Answer: $\frac{10}{3}$

</details>

---

### Q2. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=\frac{x^{\frac{2}{3}}-x^{\frac{-1}{3}}}{x^{\frac{2}{3}}+x^{\frac{-1}{3}}}, x \neq 0$, then $(x+1)^2 y_1=$

**Options:**

- **(A)** 2
- **(B)** -2
- **(C)** $\frac{-1}{3}$
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

Given $y = \dfrac{x^{2/3} - x^{-1/3}}{x^{2/3} + x^{-1/3}}$

Multiplying the numerator and denominator by $x^{1/3}$:

$y = \dfrac{x^{2/3} \cdot x^{1/3} - x^{-1/3} \cdot x^{1/3}}{x^{2/3} \cdot x^{1/3} + x^{-1/3} \cdot x^{1/3}}$

$y = \dfrac{x - 1}{x + 1}$

Differentiating with respect to $x$ using the quotient rule:

$y_1 = \dfrac{d}{dx} \left( \dfrac{x - 1}{x + 1} \right)$

$y_1 = \dfrac{(x + 1)(1) - (x - 1)(1)}{(x + 1)^2}$

$y_1 = \dfrac{2}{(x + 1)^2}$

$(x + 1)^2 y_1 = 2$

Answer: 2

</details>

---

### Q3. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a body cools from $80^{\circ} \mathrm{C}$ to $50^{\circ} \mathrm{C}$ in the room temperature of $25^{\circ} \mathrm{C}$ in 30 minutes, then the temperature of the body after 1 hour is

**Options:**

- **(A)** $31.36^{\circ} \mathrm{C}$
- **(B)** $32.25^{\circ} \mathrm{C}$
- **(C)** $36.36^{\circ} \mathrm{C}$
- **(D)** $33.25^{\circ} \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $36.36^{\circ} \mathrm{C}$**

**Detailed Solution:**

Let $\theta$ be the temperature of the body at any time $t$.
$\begin{aligned}
\therefore \quad & \frac{\mathrm{d} \theta}{\mathrm{dt}} \propto(\theta-25) \\
& \Rightarrow \frac{\mathrm{d} \theta}{\mathrm{dt}}=-\mathrm{k}(\theta-25), \mathrm{k}>0
\end{aligned}$
Integrating on both sides, we get
$\begin{aligned}
& \log |\theta-25|=-\mathrm{kt}+\mathrm{c} \\
& \text { When } \mathrm{t}=0, \theta=80^{\circ} \\
\therefore \quad & \log 55=0+\mathrm{c} \\
\Rightarrow \quad \mathrm{c}=\log 55 & \log |\theta-25|=-\mathrm{kt}+\log 55 \\
\therefore \quad & \text { When } \mathrm{t}=30, \theta=50^{\circ} \\
\therefore \quad & \log 25=-30 \mathrm{k}+\log 55 \\
\Rightarrow & \mathrm{k}=-\frac{1}{30} \log \frac{5}{11} \\
\therefore \quad & \log |\theta-25|=\frac{\mathrm{t}}{30} \log \frac{5}{11}+\log 55
\end{aligned}$
When $\mathrm{t}=1$ hour $=60$ minutes, ... [From (i)]
$\begin{aligned}
& \log |\theta-25|=\frac{60}{30} \log \frac{5}{11}+\log 55 \\
& \Rightarrow \log \left(\frac{\theta-25}{55}\right)=2 \log \left(\frac{5}{11}\right) \\
& \Rightarrow \frac{\theta-25}{55}=\left(\frac{5}{11}\right)^2 \\
& \Rightarrow \frac{\theta-25}{55}=\frac{25}{121} \\
& \Rightarrow \theta=25+\frac{125}{11}=25+11.36=36.36^{\circ} \mathrm{C}
\end{aligned}$

</details>

---

### Q4. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The money invested in a company is compounded continuously. If $₹ 200$ invested today becomes $₹ 400$ in 6 years, then at the end of 33 years it will become ₹

**Options:**

- **(A)** $1600 \sqrt{2}$
- **(B)** $3200 \sqrt{2}$
- **(C)** $12800 \sqrt{2}$
- **(D)** $6400 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $6400 \sqrt{2}$**

**Detailed Solution:**

Here, Amount $(A)=₹ 400$
Principal $(P)=₹ 200, N=6$ years
$$
\begin{aligned}
& A-P\left(1+\frac{R}{100}\right)^N \\
& \Rightarrow 400=200\left(1+\frac{R}{100}\right)^6 \\
& \Rightarrow\left(1+\frac{R}{100}\right)^6=2 \\
& \Rightarrow 1+\frac{R}{100}=2^{\frac{1}{6}} \\
& \begin{aligned}
A & =P\left(1+\frac{R}{100}\right)^N \\
& =200\left(1+\frac{R}{100}\right)^{33} \\
& =200\left(2^{\frac{1}{6}}\right)^{33} \\
& =200\left(2^5 \cdot 2^{\frac{1}{2}}\right) \\
& =200(32 \sqrt{2}) \\
& =6400 \sqrt{2}
\end{aligned}
\end{aligned}
$$

</details>

---

### Q5. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The decay rate of radio active material at any time $t$ is proportional to its mass at that time. The mass is 27 grams when $t=0$. After three hours it was found that 8 grams are left. Then the substance left after one more hour is

**Options:**

- **(A)** $\frac{27}{8}$ grams
- **(B)** $\frac{81}{4}$ grams
- **(C)** $\frac{16}{3}$ grams
- **(D)** $\frac{16}{9}$ grams

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{16}{3}$ grams**

**Detailed Solution:**

Let ' $x$ ' be the mass of the material at time ' $t$ '.
$\therefore \quad \frac{\mathrm{d} x}{\mathrm{dt}}=-\mathrm{k} x,(-\mathrm{ve}$ sign indicates decay. $)$
$$
\therefore \quad \int \frac{\mathrm{d} x}{x}=-\mathrm{k} \int \mathrm{dt}
$$
$\therefore \quad \log |x|=-\mathrm{kt}+\mathrm{c}$
When $\mathrm{t}=0, x=27$
$\therefore \quad \mathrm{c}=\log 27$
$\therefore \quad \log |x|=-\mathrm{kt}+\log 27$
When $\mathrm{t}=3, x=8$
$$
\therefore \quad \mathrm{k}=\log \left(\frac{3}{2}\right)
$$
When $\mathrm{t}=4$, we get
$$
\begin{array}{ll} 
& \log |x|=-4 \log \left(\frac{3}{2}\right)+\log 27 \\
\therefore \quad & \log |x|=\log \left(\frac{16}{3}\right) \\
\therefore \quad & x=\frac{16}{3} \text { grams }
\end{array}
$$

</details>

---

