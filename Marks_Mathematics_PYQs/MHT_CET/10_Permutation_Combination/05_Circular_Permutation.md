# MHT CET Mathematics - Permutation Combination

## Topic 5: Circular Permutation

**Total Questions:** 9

---

### Q1. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Four men and three women are to be arranged at a round table. The number of arrangements in which no two women are together is ....

**Options:**

- **(A)** $7!$
- **(B)** $3! \times 4!$
- **(C)** $3! \times 3!$
- **(D)** $6!$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3! \times 4!$**

**Detailed Solution:**

First, arrange the $4$ men around the circular table. The number of ways to do this is $(4 - 1)! = 3!$.

When the $4$ men are seated, they create $4$ gaps between them.

To ensure that no two women sit together, the $3$ women must be placed in these $4$ gaps.

The number of ways to choose $3$ gaps out of $4$ and arrange the $3$ women in them is $^{4}P_{3} = 4 \times 3 \times 2 = 4!$.

Therefore, the total number of arrangements is $3! \times 4!$.

Answer: $3! \times 4!$

</details>

---

### Q2. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

11 players of the Indian cricket team are sitting at a circular table. The number of ways they can sit so that two players, the wicket keeper and the captain never sit together is ___

**Options:**

- **(A)** $10!$
- **(B)** $2 \times 9!$
- **(C)** $8 \times 9!$
- **(D)** $9 \times 9!$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8 \times 9!$**

**Detailed Solution:**

Total number of players is $11$.

Total number of ways to arrange $11$ players around a circular table is $(11 - 1)! = 10!$.

To find the number of ways where the wicket keeper and the captain sit together, consider them as a single unit.

The number of units to arrange is $9$ remaining players plus $1$ unit, which equals $10$ units.

The number of ways to arrange these $10$ units around a circular table is $(10 - 1)! = 9!$.

The wicket keeper and the captain can interchange their positions within the unit in $2! = 2$ ways.

The number of ways they sit together is $2 \times 9!$.

The number of ways they never sit together is the total number of ways minus the number of ways they sit together.

Required number of ways is $10! - 2 \times 9! = 10 \times 9! - 2 \times 9! = 8 \times 9!$.

Answer: $8 \times 9!$

</details>

---

### Q3. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of ways that 8 beads of different colours can be strung to form a necklace is

**Options:**

- **(A)** $5040$
- **(B)** $2520$
- **(C)** $2840$
- **(D)** $5080$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2520$**

**Detailed Solution:**

The number of ways to arrange $n$ distinct objects in a circle is $(n-1)!$.

For a necklace, clockwise and counter-clockwise arrangements are considered identical because it can be flipped over.

Therefore, the number of ways to string $n$ different beads into a necklace is $\dfrac{(n-1)!}{2}$.

Given $n = 8$, the number of ways is $\dfrac{(8-1)!}{2} = \dfrac{7!}{2}$.

Since $7! = 5040$, the number of ways is $\dfrac{5040}{2} = 2520$.

Answer: $2520$

</details>

---

### Q4. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A family consisting of a mother, father and their 8 children ( 4 boys and 4 girls) are to be seated at a round table in a party. How many ways can this be done if the mother and father sit together and the males and females alternate?

**Options:**

- **(A)** 567
- **(B)** 765
- **(C)** 657
- **(D)** 576

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 576**

**Detailed Solution:**

Total number of people = 10 (5 males including the father, and 5 females including the mother).

Since males and females must alternate, the seating pattern around the circular table must be M, F, M, F, M, F, M, F, M, F.

The mother and father must sit together, so they occupy an adjacent (Male, Female) pair of seats. We can treat the (Father, Mother) pair as a single unit.

Fixing this (Father, Mother) unit at the round table can be done in $1$ way.

Now, there are $4$ remaining male seats and $4$ remaining female seats.

The $4$ boys can be arranged in the $4$ male seats in $4!$ ways.

The $4$ girls can be arranged in the $4$ female seats in $4!$ ways.

Total number of ways = $4! \times 4! = 24 \times 24 = 576$.

Answer: 576

</details>

---

### Q5. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

21 friends were invited for a party. Two round tables can accommodate 12 and 9 friends each. The number of ways of the seating arrangements of friends is .....

**Options:**

- **(A)** $11!\times 8!$
- **(B)** $12!\times 9!$
- **(C)** $\frac{35}{9} \times 19!$
- **(D)** $\frac{20!}{12!8!} \times 11!\times 9!$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{35}{9} \times 19!$**

**Detailed Solution:**

Total number of friends to be seated = $21$

Number of friends to be seated at the first round table = $12$

Number of friends to be seated at the second round table = $9$

The number of ways to select $12$ friends out of $21$ for the first table is $^{21}C_{12}$. The remaining $9$ friends will automatically go to the second table.

The number of ways to arrange $12$ friends around a round table is $(12 - 1)! = 11!$.

The number of ways to arrange the remaining $9$ friends around the second round table is $(9 - 1)! = 8!$.

Total number of seating arrangements is given by:

$^{21}C_{12} \times 11! \times 8!$

$= \dfrac{21!}{12! \times 9!} \times 11! \times 8!$

$= \dfrac{21 \times 20 \times 19!}{12 \times 11! \times 9 \times 8!} \times 11! \times 8!$

$= \dfrac{21 \times 20}{12 \times 9} \times 19!$

$= \dfrac{420}{108} \times 19!$

$= \dfrac{35}{9} \times 19!$

Answer: $\frac{35}{9} \times 19!$

</details>

---

### Q6. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Five persons $A, B, C, D$ and $E$ are seated in a circular arangement, if each of them is given a hat of one of the three colours red, blue and green, then the number of ways, of distributing the hats such that the person seated in adjacent seats get different coloured hats, is

**Options:**

- **(A)** 30
- **(B)** 15
- **(C)** 60
- **(D)** 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 30**

**Detailed Solution:**

Let the five persons be seated in order around the circle.

Since no two adjacent persons can have the same colored hat, the maximum number of times any color can be used is $2$.

With $5$ persons and $3$ available colors, the only possible distribution of the number of hats of each color is $2, 2, 1$.

The number of ways to choose the color that is used exactly once is $3$.

The person who receives this uniquely colored hat can be chosen in $5$ ways.

Once this person is fixed, the remaining $4$ persons form a linear sequence. To ensure no adjacent persons have the same color, the remaining two colors must alternate.

There are exactly $2$ ways to alternate the remaining two colors among these $4$ persons.

Total number of ways $= 3 \times 5 \times 2 = 30$.

Answer: 30

</details>

---

### Q7. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Five persons $\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}$ and $\mathrm{E}$ are seated in a circular arrangement. If each of them is given a cap of one of the three colours red, blue and green, then the number of ways of distributing the caps such that the persons seated in adjacent seats get different coloured caps, is

**Options:**

- **(A)** 30
- **(B)** 15
- **(C)** 60
- **(D)** 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 30**

**Detailed Solution:**

There are 5 caps and 3 colours.
$\therefore \quad$ At least one colour will get repeated. As adjacent caps should be of different colours, no colour can repeat thrice.
$\therefore \quad$ Exactly two colours will repeat twice.
$\therefore \quad$ Colour of the caps are selected in 3 ways as follows:
Red-Red-Green-Green-Blue, Red-Red-Green-Blue-Blue, Red-Green-Green-Blue-Blue.
Now, while distributing the caps from above combinations, we choose any one of the 5 persons and give single colour cap. And remaining four caps can be distributed in alternate colour sequence, clock-wise or anticlock-wise.
This can be done in $5 \times 2$ ways.
$\therefore \quad$ Required number of ways $=3 \times 5 \times 2=30$.

</details>

---

### Q8. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Number of ways, in which 6 men and 5 women can sit at a round table, if no two women sit together, are

**Options:**

- **(A)** $5 ! \times 4 !$
- **(B)** $6 ! \times 5 !$
- **(C)** $30$
- **(D)** $7 ! \times 5 !$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6 ! \times 5 !$**

**Detailed Solution:**

6 men can be seated around a round table in 5! ways
Now, 5 women can be seated in 6 places in 6 ! ways
Hence total number of ways is $6 ! \times 5$ !

</details>

---

### Q9. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A round table conference is to be held amongst 20 countries. If two particular delegates wish to sit together, then such arrangements can be done in ways.

**Options:**

- **(A)** $2 \times(18) !$
- **(B)** $\frac{19 !}{2 !}$
- **(C)** $18 !$
- **(D)** $19 ! \times 2 !$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 \times(18) !$**

**Detailed Solution:**

We consider two particular delegates as single unit now 19 units can be arranged around a round table in 18! ways and the two delegates can be arranged mutually in 2 ! ways
Hence the required number of ways is $2 \times(18$ !)

</details>

---

