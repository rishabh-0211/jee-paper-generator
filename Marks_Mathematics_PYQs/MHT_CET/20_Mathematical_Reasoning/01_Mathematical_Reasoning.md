# MHT CET Mathematics - Mathematical Reasoning

## Topic 1: Mathematical Reasoning

**Total Questions:** 265

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The logical statement $\sim [(p \rightarrow q) \leftrightarrow (p \wedge \sim q)]$ is

**Options:**

- **(A)** a fallacy
- **(B)** equivalent to $p \wedge q$
- **(C)** equivalent to $p \vee q$
- **(D)** a tautology

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a tautology**

**Detailed Solution:**

Let $X \equiv p \rightarrow q$.

The negation of $X$ is $\sim (p \rightarrow q) \equiv p \wedge \sim q$.

The given logical statement can be written as $\sim [X \leftrightarrow \sim X]$.

The biconditional statement $X \leftrightarrow \sim X$ is always false, which means it is a contradiction (fallacy).

The negation of a contradiction is always true.

Therefore, the given statement is a tautology.

Answer: a tautology

</details>

---

### Q2. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $p, q, r$ are statements with truth values F, T, F respectively then the truth values of $(p \wedge q) \leftrightarrow \sim p$ and $q \rightarrow (p \vee \sim r)$ are respectively _____

**Options:**

- **(A)** T, F
- **(B)** T, T
- **(C)** F, F
- **(D)** F, T

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) F, T**

**Detailed Solution:**

Given $p = F$, $q = T$, $r = F$.

For the first statement $(p \wedge q) \leftrightarrow \sim p$:
$p \wedge q \equiv F \wedge T \equiv F$
$\sim p \equiv \sim F \equiv T$
Therefore, $(p \wedge q) \leftrightarrow \sim p \equiv F \leftrightarrow T \equiv F$.

For the second statement $q \rightarrow (p \vee \sim r)$:
$\sim r \equiv \sim F \equiv T$
$p \vee \sim r \equiv F \vee T \equiv T$
Therefore, $q \rightarrow (p \vee \sim r) \equiv T \rightarrow T \equiv T$.

The truth values are F and T respectively.

Answer: F, T

</details>

---

### Q3. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $[p \wedge (q \vee r)] \vee [\sim r \wedge \sim q \wedge p]$ is equivalent to _____

**Options:**

- **(A)** $q \vee r$
- **(B)** $p \vee r$
- **(C)** $r$
- **(D)** $p$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $p$**

**Detailed Solution:**

Given statement pattern: $[p \wedge (q \vee r)] \vee [\sim r \wedge \sim q \wedge p]$

Using commutative law on the second bracket:

$[p \wedge (q \vee r)] \vee [p \wedge (\sim q \wedge \sim r)]$

Using De Morgan's law on $(\sim q \wedge \sim r)$:

$[p \wedge (q \vee r)] \vee [p \wedge \sim (q \vee r)]$

Using distributive law:

$p \wedge [(q \vee r) \vee \sim (q \vee r)]$

Since $x \vee \sim x \equiv T$ (Tautology), we get:

$p \wedge T$

Since $p \wedge T \equiv p$, the statement pattern is equivalent to $p$.

Answer: $p$

</details>

---

### Q4. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider the following statements -
(i) If a person is social, then he is happy.
(ii) If a person is not social, then he is not happy.
(iii) If a person is not happy, then he is not social.
(iv) If a person is happy, then he is social.
Which of the above statements are equivalent?

**Options:**

- **(A)** (i) and (iv), (ii) and (iii)
- **(B)** (i) and (iii), (ii) and (iv)
- **(C)** (i) and (ii), (iii) and (iv)
- **(D)** (i) and (iii), (i) and (iv)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (i) and (iii), (ii) and (iv)**

**Detailed Solution:**

Let $p$ be the statement "A person is social" and $q$ be the statement "A person is happy".

The given statements can be written in symbolic form as:
(i) $p \rightarrow q$
(ii) $\sim p \rightarrow \sim q$
(iii) $\sim q \rightarrow \sim p$
(iv) $q \rightarrow p$

A conditional statement is logically equivalent to its contrapositive.

The contrapositive of $p \rightarrow q$ is $\sim q \rightarrow \sim p$. Thus, statement (i) is equivalent to statement (iii).

The contrapositive of $\sim p \rightarrow \sim q$ is $\sim (\sim q) \rightarrow \sim (\sim p)$, which simplifies to $q \rightarrow p$. Thus, statement (ii) is equivalent to statement (iv).

Therefore, (i) and (iii) are equivalent, and (ii) and (iv) are equivalent.

Answer: (i) and (iii), (ii) and (iv)

</details>

---

### Q5. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement $(p \wedge \sim q) \to (\sim p \vee r)$ is equivalent to:

**Options:**

- **(A)** $(p \wedge \sim q) \wedge (\sim r)$
- **(B)** $(p \vee \sim q) \wedge (p \wedge \sim r)$
- **(C)** $(\sim p \vee q) \vee (p \wedge \sim r)$
- **(D)** $(p \wedge \sim q) \vee (p \wedge \sim r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(p \wedge \sim q) \wedge (\sim r)$**

**Detailed Solution:**

The given statement is $(p \wedge \sim q) \to (\sim p \vee r)$.

The negation of an implication $X \to Y$ is $X \wedge \sim Y$.

Here, $X = p \wedge \sim q$ and $Y = \sim p \vee r$.

The negation of the given statement is $(p \wedge \sim q) \wedge \sim (\sim p \vee r)$.

Using De Morgan's Law, $\sim (\sim p \vee r) \equiv p \wedge \sim r$.

Substituting this back, we get $(p \wedge \sim q) \wedge (p \wedge \sim r)$.

Using the associative law and the idempotent law $p \wedge p \equiv p$, this simplifies to $p \wedge \sim q \wedge \sim r$.

This can be grouped as $(p \wedge \sim q) \wedge (\sim r)$.

Answer: $(p \wedge \sim q) \wedge (\sim r)$

</details>

---

### Q6. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $p \rightarrow (q \rightarrow p) \equiv$

**Options:**

- **(A)** $p \rightarrow (p \rightarrow q)$
- **(B)** $p \rightarrow (p \wedge q)$
- **(C)** $p \rightarrow (p \leftrightarrow q)$
- **(D)** $p \rightarrow (p \vee q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $p \rightarrow (p \vee q)$**

**Detailed Solution:**

The given statement pattern is $p \rightarrow (q \rightarrow p)$.

Using the logical equivalence $A \rightarrow B \equiv \sim A \vee B$, we can simplify the expression:

$p \rightarrow (q \rightarrow p) \equiv \sim p \vee (\sim q \vee p)$

Using the associative and commutative laws:

$\equiv (\sim p \vee p) \vee \sim q$

Since $\sim p \vee p \equiv T$ (a tautology):

$\equiv T \vee \sim q \equiv T$

Thus, the given statement pattern is a tautology.

Now, checking the given options:

For $p \rightarrow (p \rightarrow q)$:
$\equiv \sim p \vee (\sim p \vee q) \equiv \sim p \vee q$ (Not a tautology)

For $p \rightarrow (p \wedge q)$:
$\equiv \sim p \vee (p \wedge q) \equiv (\sim p \vee p) \wedge (\sim p \vee q) \equiv T \wedge (\sim p \vee q) \equiv \sim p \vee q$ (Not a tautology)

For $p \rightarrow (p \leftrightarrow q)$:
If $p$ is True and $q$ is False, $p \leftrightarrow q$ is False. Then $T \rightarrow F$ is False. (Not a tautology)

For $p \rightarrow (p \vee q)$:
$\equiv \sim p \vee (p \vee q) \equiv (\sim p \vee p) \vee q \equiv T \vee q \equiv T$

Since $p \rightarrow (p \vee q)$ is also a tautology, it is logically equivalent to $p \rightarrow (q \rightarrow p)$.

Answer: $p \rightarrow (p \vee q)$

</details>

---

### Q7. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The negation of the inverse of $\sim p \rightarrow q$ is equivalent to:

**Options:**

- **(A)** $\sim q \rightarrow p$
- **(B)** $\sim q \wedge p$
- **(C)** $\sim p \wedge \sim q$
- **(D)** $p \wedge q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $p \wedge q$**

**Detailed Solution:**

The given statement is $\sim p \rightarrow q$.

The inverse of a conditional statement $A \rightarrow B$ is $\sim A \rightarrow \sim B$.

Substituting $A = \sim p$ and $B = q$, the inverse of the given statement is $\sim(\sim p) \rightarrow \sim q$, which simplifies to $p \rightarrow \sim q$.

We need to find the negation of this inverse, which is $\sim(p \rightarrow \sim q)$.

Using the logical equivalence $A \rightarrow B \equiv \sim A \vee B$, we can rewrite the inverse as $p \rightarrow \sim q \equiv \sim p \vee \sim q$.

Now, applying the negation:

$\sim(\sim p \vee \sim q)$

By De Morgan's laws, this is equivalent to $p \wedge q$.

Answer: $p \wedge q$

</details>

---

### Q8. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement $(p \wedge (\sim q)) \vee ((\sim p) \wedge q) \vee ((\sim p) \wedge (\sim q))$ is equivalent to :

**Options:**

- **(A)** $(p \vee q)$
- **(B)** $p \vee (\sim q)$
- **(C)** $\sim p \vee q$
- **(D)** $\sim p \vee \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sim p \vee \sim q$**

**Detailed Solution:**

The given expression is $(p \wedge (\sim q)) \vee ((\sim p) \wedge q) \vee ((\sim p) \wedge (\sim q))$

Taking $(\sim p)$ common from the last two terms using the distributive law, we get:

$(p \wedge (\sim q)) \vee ((\sim p) \wedge (q \vee (\sim q)))$

Since $q \vee (\sim q)$ is a tautology (True), the expression becomes:

$(p \wedge (\sim q)) \vee (\sim p)$

Applying the distributive law again:

$(p \vee (\sim p)) \wedge ((\sim q) \vee (\sim p))$

Since $p \vee (\sim p)$ is a tautology (True), the expression simplifies to:

$(\sim q) \vee (\sim p)$

By commutative law, this is equivalent to:

$\sim p \vee \sim q$

Answer: $\sim p \vee \sim q$

</details>

---

### Q9. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $A = \{1, 2, 3, \ldots, 10\}$. Consider the following statements:
$p: \forall x \in A,\,x^2 - x > 0$
$q: \exists x \in A$, such that $x + 10 = 20$
Then the truth values of $p$ and $q$ are respectively ____

**Options:**

- **(A)** $T,\,T$
- **(B)** $T,\,F$
- **(C)** $F,\,T$
- **(D)** $F,\,F$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $F,\,T$**

**Detailed Solution:**

Given $A = \{1, 2, 3, \ldots, 10\}$.

For statement $p$: $\forall x \in A,\,x^2 - x > 0$.
When $x = 1$, $x^2 - x = 1^2 - 1 = 0$, which is not greater than $0$.
Thus, statement $p$ is False ($F$).

For statement $q$: $\exists x \in A$, such that $x + 10 = 20$.
When $x = 10$, $x + 10 = 10 + 10 = 20$. Since $10 \in A$, the statement is satisfied.
Thus, statement $q$ is True ($T$).

The truth values of $p$ and $q$ are respectively $F,\,T$.

Answer: $F,\,T$

</details>

---

### Q10. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the compound statement $(p \wedge \sim q) \rightarrow (q \vee \sim r)$ is false then which of the following statements is a true ?

**Options:**

- **(A)** $(p \wedge r) \rightarrow q$
- **(B)** $(\sim p \vee q) \rightarrow r$
- **(C)** $(p \rightarrow q) \wedge r$
- **(D)** $p \rightarrow (q \wedge r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\sim p \vee q) \rightarrow r$**

**Detailed Solution:**

The given compound statement is $(p \wedge \sim q) \rightarrow (q \vee \sim r)$.

An implication $A \rightarrow B$ is false if and only if $A$ is true and $B$ is false.

Therefore, $p \wedge \sim q$ is true and $q \vee \sim r$ is false.

For $p \wedge \sim q$ to be true, both $p$ and $\sim q$ must be true. This gives $p$ is True (T) and $q$ is False (F).

For $q \vee \sim r$ to be false, both $q$ and $\sim r$ must be false. Since $q$ is already False, $\sim r$ must be False, which gives $r$ is True (T).

Thus, the truth values are $p = T$, $q = F$, and $r = T$.

Now, evaluating the given options:

Option 1: $(p \wedge r) \rightarrow q \equiv (T \wedge T) \rightarrow F \equiv T \rightarrow F \equiv F$

Option 2: $(\sim p \vee q) \rightarrow r \equiv (F \vee F) \rightarrow T \equiv F \rightarrow T \equiv T$

Option 3: $(p \rightarrow q) \wedge r \equiv (T \rightarrow F) \wedge T \equiv F \wedge T \equiv F$

Option 4: $p \rightarrow (q \wedge r) \equiv T \rightarrow (F \wedge T) \equiv T \rightarrow F \equiv F$

Only the statement in the second option is true.

Answer: $(\sim p \vee q) \rightarrow r$

</details>

---

### Q11. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $p$: switch $S_1$ is closed, $q$: switch $S_2$ is closed.
Then, the equivalent symbolic form for the following circuit is:
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/15_may_shift_1__q113_d1.png" />

**Options:**

- **(A)** $\sim p \wedge \sim q$
- **(B)** $p \wedge q$
- **(C)** $p \vee q$
- **(D)** $\sim p \vee \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sim p \vee \sim q$**

**Detailed Solution:**

Let $p$ represent the switch $S_1$ being closed and $q$ represent the switch $S_2$ being closed.

The switches $S_1'$ and $S_2'$ represent the negations $\sim p$ and $\sim q$ respectively.

The given circuit consists of three parallel branches. The logical expression for the circuit is the disjunction (OR) of the expressions for each branch:

Top branch: $S_1$ and $S_2'$ in series $\rightarrow p \wedge \sim q$

Middle branch: $S_1'$ and $S_2$ in series $\rightarrow \sim p \wedge q$

Bottom branch: $S_1'$ and $S_2'$ in series $\rightarrow \sim p \wedge \sim q$

The equivalent symbolic form for the entire circuit is:

$(p \wedge \sim q) \vee (\sim p \wedge q) \vee (\sim p \wedge \sim q)$

Simplifying the expression by taking $\sim p$ common from the last two terms:

$(p \wedge \sim q) \vee [\sim p \wedge (q \vee \sim q)]$

Since $q \vee \sim q$ is a tautology (True), the expression becomes:

$(p \wedge \sim q) \vee \sim p$

Using the distributive law:

$(p \vee \sim p) \wedge (\sim q \vee \sim p)$

Since $p \vee \sim p$ is True, the expression simplifies to:

$\sim q \vee \sim p$

This is equivalent to $\sim p \vee \sim q$.

Answer: $\sim p \vee \sim q$

</details>

---

### Q12. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $p \to (\sim p \vee q)$ is false, then the truth values of $p, q$ are:

**Options:**

- **(A)** $T, F$
- **(B)** $F, T$
- **(C)** $F, F$
- **(D)** $T, T$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $T, F$**

**Detailed Solution:**

The implication $A \to B$ is false if and only if $A$ is true and $B$ is false.

For the given statement $p \to (\sim p \vee q)$ to be false, $p$ must be true ($T$) and $(\sim p \vee q)$ must be false ($F$).

Since $p$ is true, $\sim p$ is false.

For the disjunction $(\sim p \vee q)$ to be false, both of its components must be false. Since $\sim p$ is already false, $q$ must also be false ($F$).

Therefore, the truth values of $p$ and $q$ are $T$ and $F$ respectively.

Answer: $T, F$

</details>

---

### Q13. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The logical expression $[\sim(p \to q) \wedge (q \to p)] \vee \sim(p \leftrightarrow q)$ is equivalent to:

**Options:**

- **(A)** $p \leftrightarrow q$
- **(B)** $(p \vee q) \wedge \sim(p \wedge q)$
- **(C)** $\sim p \vee \sim q$
- **(D)** $p \wedge q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(p \vee q) \wedge \sim(p \wedge q)$**

**Detailed Solution:**

We first simplify the term $\sim(p \to q) \wedge (q \to p)$.

Since $p \to q \equiv \sim p \vee q$, its negation is $\sim(p \to q) \equiv p \wedge \sim q$.

Also, $q \to p \equiv \sim q \vee p$.

Taking their intersection:

$\sim(p \to q) \wedge (q \to p) \equiv (p \wedge \sim q) \wedge (\sim q \vee p) \equiv p \wedge \sim q$

Next, we expand the second term $\sim(p \leftrightarrow q)$.

The biconditional $p \leftrightarrow q \equiv (p \wedge q) \vee (\sim p \wedge \sim q)$.

Its negation is $\sim(p \leftrightarrow q) \equiv (p \wedge \sim q) \vee (\sim p \wedge q)$.

Now, substituting these into the given logical expression:

$[\sim(p \to q) \wedge (q \to p)] \vee \sim(p \leftrightarrow q) \equiv (p \wedge \sim q) \vee [ (p \wedge \sim q) \vee (\sim p \wedge q) ]$

By the idempotent law, $(p \wedge \sim q) \vee (p \wedge \sim q) \equiv p \wedge \sim q$.

Thus, the expression simplifies to:

$(p \wedge \sim q) \vee (\sim p \wedge q)$

Now we evaluate the given options to find the equivalent expression. Expanding the second option:

$(p \vee q) \wedge \sim(p \wedge q) \equiv (p \vee q) \wedge (\sim p \vee \sim q)$

Using the distributive law:

$\equiv (p \wedge \sim p) \vee (p \wedge \sim q) \vee (q \wedge \sim p) \vee (q \wedge \sim q)$

Since $p \wedge \sim p$ and $q \wedge \sim q$ are both false ($F$), this reduces to:

$\equiv F \vee (p \wedge \sim q) \vee (\sim p \wedge q) \vee F$

$\equiv (p \wedge \sim q) \vee (\sim p \wedge q)$

This perfectly matches our simplified expression.

Answer: $(p \vee q) \wedge \sim(p \wedge q)$

</details>

---

### Q14. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$[(p \wedge q) \vee (\sim r \vee \sim s \vee \sim t)] \wedge [(p \wedge q) \vee (r \wedge s \wedge t)] \equiv$

**Options:**

- **(A)** $\sim p \wedge q$
- **(B)** $p \vee q$
- **(C)** $p \wedge q$
- **(D)** $p \vee \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $p \wedge q$**

**Detailed Solution:**

Let $A = p \wedge q$ and $B = r \wedge s \wedge t$.

By De Morgan's law, $\sim B = \sim(r \wedge s \wedge t) = \sim r \vee \sim s \vee \sim t$.

The given expression can be rewritten as:

$[A \vee \sim B] \wedge [A \vee B]$

Using the distributive law, this is equivalent to:

$A \vee (\sim B \wedge B)$

Since $\sim B \wedge B$ is always false ($F$), the expression simplifies to:

$A \vee F \equiv A$

Substituting back $A = p \wedge q$, the given expression is equivalent to $p \wedge q$.

Answer: $p \wedge q$

</details>

---

### Q15. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let p, q, r be three logical statements. Consider the compound statements
$S_1: [(p \to q) \wedge \sim q] \to r$ and
$S_2: (p \vee q) \vee r$
Then which of the following is not true?

**Options:**

- **(A)** If $S_2$ is True, then $S_1$ is True.
- **(B)** If $S_2$ is False, then $S_1$ is False.
- **(C)** If $S_1$ is False, then $S_2$ is False.
- **(D)** If $S_2$ is False, then $S_1$ is True.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If $S_2$ is False, then $S_1$ is True.**

**Detailed Solution:**

Given $S_1: [(p \to q) \wedge \sim q] \to r$

Using the logical equivalence $p \to q \equiv \sim p \vee q$, we can simplify the premise of $S_1$:

$(p \to q) \wedge \sim q \equiv (\sim p \vee q) \wedge \sim q$

By the distributive law:

$(\sim p \vee q) \wedge \sim q \equiv (\sim p \wedge \sim q) \vee (q \wedge \sim q)$

Since $q \wedge \sim q$ is always False, we get:

$(\sim p \wedge \sim q) \vee \text{False} \equiv \sim p \wedge \sim q$

Now, substitute this back into $S_1$:

$S_1 \equiv (\sim p \wedge \sim q) \to r$

Using the implication equivalence $A \to B \equiv \sim A \vee B$:

$S_1 \equiv \sim(\sim p \wedge \sim q) \vee r$

By De Morgan's law:

$S_1 \equiv (p \vee q) \vee r$

We are given $S_2: (p \vee q) \vee r$.

Thus, $S_1$ and $S_2$ are logically equivalent ($S_1 \equiv S_2$). They will always have the exact same truth values for any combination of $p, q,$ and $r$.

Therefore, if $S_2$ is False, $S_1$ must also be False. The statement "If $S_2$ is False, then $S_1$ is True" is not true.

Answer: If $S_2$ is False, then $S_1$ is True.

</details>

---

### Q16. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of converse of "I can travel by train if I get my ticket reserved" is

**Options:**

- **(A)** I get my ticket reserved and I cannot travel by train.
- **(B)** I get my ticket not reserved and I can travel by train.
- **(C)** I cannot travel by train and I get my ticket reserved.
- **(D)** I can travel by train and I get my ticket not reserved

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) I can travel by train and I get my ticket not reserved**

**Detailed Solution:**

Let $p$ be the statement: "I get my ticket reserved".
Let $q$ be the statement: "I can travel by train".

The given statement is "I can travel by train if I get my ticket reserved", which can be written as "If $p$ then $q$", i.e., $p \rightarrow q$.

The converse of $p \rightarrow q$ is $q \rightarrow p$.

The negation of the converse is $\sim(q \rightarrow p)$.

Using the logical equivalence $A \rightarrow B \equiv \sim A \vee B$, we have:
$q \rightarrow p \equiv \sim q \vee p$

Therefore, the negation is:
$\sim(q \rightarrow p) \equiv \sim(\sim q \vee p) \equiv q \wedge \sim p$

Translating $q \wedge \sim p$ back into words, we get: "I can travel by train and I get my ticket not reserved".

Answer: I can travel by train and I get my ticket not reserved

</details>

---

### Q17. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A statement logically equivalent to the statement pattern $\sim[(p \rightarrow \sim q) \wedge (\sim q \vee p)]$ is

**Options:**

- **(A)** $p \wedge q$
- **(B)** $p \vee q$
- **(C)** $p$
- **(D)** $q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $q$**

**Detailed Solution:**

The given statement pattern is $\sim[(p \rightarrow \sim q) \wedge (\sim q \vee p)]$.

Using the logical equivalence $p \rightarrow \sim q \equiv \sim p \vee \sim q$, the expression inside the square brackets becomes:

$(\sim p \vee \sim q) \wedge (\sim q \vee p)$

By the commutative property, this can be written as:

$(\sim q \vee \sim p) \wedge (\sim q \vee p)$

Using the distributive law, this simplifies to:

$\sim q \vee (\sim p \wedge p)$

Since $\sim p \wedge p \equiv F$ (where $F$ is a contradiction), we get:

$\sim q \vee F \equiv \sim q$

Substituting this back into the original statement pattern, we get:

$\sim[\sim q] \equiv q$

Answer: $q$

</details>

---

### Q18. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The truth values of logical statements $p, q, r$ are T, T and F respectively. If $*$ and $\#$ are symbolic logical connectives such that $(p\,\#\,r) \rightarrow (\sim q\,\#\,r)$ is false and $(\sim p\,*\,q) \leftrightarrow (\sim q\,\#\,r)$ is true, then $*$ and $\#$ are respectively ____

**Options:**

- **(A)** $\wedge, \vee$
- **(B)** $\vee, \wedge$
- **(C)** $\rightarrow, \vee$
- **(D)** $\wedge, \rightarrow$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\wedge, \vee$**

**Detailed Solution:**

Given $p \equiv T$, $q \equiv T$, $r \equiv F$.

The statement $(p\,\#\,r) \rightarrow (\sim q\,\#\,r)$ is false.

An implication $A \rightarrow B$ is false only when $A$ is true and $B$ is false.

Thus, $p\,\#\,r \equiv T$ and $\sim q\,\#\,r \equiv F$.

Substituting the truth values, $T\,\#\,F \equiv T$ and $F\,\#\,F \equiv F$.

From the given options, the disjunction ($\vee$) satisfies these conditions since $T \vee F \equiv T$ and $F \vee F \equiv F$. Therefore, $\#$ is $\vee$.

It is also given that $(\sim p\,*\,q) \leftrightarrow (\sim q\,\#\,r)$ is true.

Since $\sim q\,\#\,r \equiv F$, for the biconditional to be true, $\sim p\,*\,q$ must also be false.

Substituting the truth values, $F\,*\,T \equiv F$.

From the given options, the conjunction ($\wedge$) satisfies this condition since $F \wedge T \equiv F$. If $*$ were $\rightarrow$, $F \rightarrow T \equiv T$, which does not satisfy the condition.

Therefore, $*$ is $\wedge$ and $\#$ is $\vee$.

Answer: $\wedge, \vee$

</details>

---

### Q19. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $p \wedge q$ is F and $p \rightarrow q$ is F, then the truth values of $p$ and $q$ respectively are

**Options:**

- **(A)** both are true
- **(B)** T, F
- **(C)** F, T
- **(D)** both are false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) T, F**

**Detailed Solution:**

Given $p \rightarrow q$ is F.

The conditional statement $p \rightarrow q$ is false if and only if $p$ is T and $q$ is F.

Checking the first condition with these truth values, we get $p \wedge q \equiv \text{T} \wedge \text{F} \equiv \text{F}$, which satisfies the given condition that $p \wedge q$ is F.

Thus, the truth values of $p$ and $q$ are T and F respectively.

Answer: T, F

</details>

---

### Q20. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The compound statement $[\sim (p \rightarrow q) \vee \sim (p \wedge r)] \wedge p$ is logically equivalent to:

**Options:**

- **(A)** $p \wedge q \wedge r$
- **(B)** $\sim p \vee \sim q \vee \sim r$
- **(C)** $p \wedge (\sim q \vee \sim r)$
- **(D)** $p \wedge \sim (q \wedge \sim r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $p \wedge (\sim q \vee \sim r)$**

**Detailed Solution:**

The given statement is $[\sim (p \rightarrow q) \vee \sim (p \wedge r)] \wedge p$.

Using the logical equivalence $p \rightarrow q \equiv \sim p \vee q$, we have:
$\sim (p \rightarrow q) \equiv \sim (\sim p \vee q) \equiv p \wedge \sim q$

Using De Morgan's law, we have:
$\sim (p \wedge r) \equiv \sim p \vee \sim r$

Substituting these into the given statement, we get:
$[(p \wedge \sim q) \vee (\sim p \vee \sim r)] \wedge p$

Applying the distributive law, this is equivalent to:
$((p \wedge \sim q) \wedge p) \vee ((\sim p \vee \sim r) \wedge p)$

Simplifying each term:
$(p \wedge \sim q) \wedge p \equiv p \wedge \sim q$
$(\sim p \vee \sim r) \wedge p \equiv (\sim p \wedge p) \vee (\sim r \wedge p) \equiv F \vee (p \wedge \sim r) \equiv p \wedge \sim r$

The expression simplifies to:
$(p \wedge \sim q) \vee (p \wedge \sim r)$

Taking $p$ common using the distributive law, we get:
$p \wedge (\sim q \vee \sim r)$

Answer: $p \wedge (\sim q \vee \sim r)$

</details>

---

### Q21. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The negation of the contrapositive of the statement $(p \vee q) \rightarrow r$ is logically equivalent to..

**Options:**

- **(A)** $\sim r \rightarrow (\sim p \wedge \sim q)$
- **(B)** $\sim r \wedge (p \vee q)$
- **(C)** $\sim r \rightarrow (p \vee q)$
- **(D)** $r \wedge (\sim p \vee q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sim r \wedge (p \vee q)$**

**Detailed Solution:**

The given statement is $(p \vee q) \rightarrow r$.

The contrapositive of a conditional statement $A \rightarrow B$ is $\sim B \rightarrow \sim A$.

So, the contrapositive of $(p \vee q) \rightarrow r$ is $\sim r \rightarrow \sim (p \vee q)$.

Using the equivalence $X \rightarrow Y \equiv \sim X \vee Y$, the contrapositive can be written as:

$\sim (\sim r) \vee \sim (p \vee q) \equiv r \vee \sim (p \vee q)$

The negation of this contrapositive is:

$\sim (r \vee \sim (p \vee q))$

Using De Morgan's laws, we get:

$\sim r \wedge \sim (\sim (p \vee q)) \equiv \sim r \wedge (p \vee q)$

Answer: $\sim r \wedge (p \vee q)$

</details>

---

### Q22. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The dual of the statement pattern $(p \wedge q) \wedge \sim (p \vee q)$ is a:

**Options:**

- **(A)** tautology
- **(B)** contradiction
- **(C)** logically equivalent to $\sim p \wedge q$
- **(D)** logically equivalent to $q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) tautology**

**Detailed Solution:**

The given statement pattern is $(p \wedge q) \wedge \sim (p \vee q)$.

The dual of a statement pattern is obtained by replacing $\wedge$ with $\vee$ and $\vee$ with $\wedge$.

The dual of the given statement pattern is $(p \vee q) \vee \sim (p \wedge q)$.

Using De Morgan's Law, $\sim (p \wedge q) \equiv \sim p \vee \sim q$.

Substituting this, we get $(p \vee q) \vee (\sim p \vee \sim q)$.

Rearranging the terms, we get $(p \vee \sim p) \vee (q \vee \sim q)$.

Since $p \vee \sim p \equiv t$ and $q \vee \sim q \equiv t$, we get $t \vee t \equiv t$.

Thus, the dual is a tautology.

Answer: tautology

</details>

---

### Q23. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The dual of the statement pattern $\sim p \rightarrow \sim(\sim p \rightarrow q)$ is...

**Options:**

- **(A)** $p \vee (p \rightarrow \sim q)$
- **(B)** $\sim p \vee (p \rightarrow \sim q)$
- **(C)** $p \wedge (p \rightarrow \sim q)$
- **(D)** $p \wedge (\sim p \rightarrow \sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $p \wedge (p \rightarrow \sim q)$**

**Detailed Solution:**

The given statement pattern is $\sim p \rightarrow \sim(\sim p \rightarrow q)$.

Using the logical equivalence $A \rightarrow B \equiv \sim A \vee B$, we can simplify the inner implication:

$\sim p \rightarrow q \equiv \sim(\sim p) \vee q \equiv p \vee q$

Substituting this back, the statement becomes:

$\sim p \rightarrow \sim(p \vee q)$

Using De Morgan's law, $\sim(p \vee q) \equiv \sim p \wedge \sim q$, so the statement is:

$\sim p \rightarrow (\sim p \wedge \sim q)$

Applying the implication equivalence again:

$\sim(\sim p) \vee (\sim p \wedge \sim q) \equiv p \vee (\sim p \wedge \sim q)$

To find the dual of a statement, we replace $\vee$ with $\wedge$ and $\wedge$ with $\vee$. The dual of the above statement is:

$p \wedge (\sim p \vee \sim q)$

Now, checking the given options, we can rewrite $p \wedge (\sim p \vee \sim q)$ by converting the disjunction back to an implication:

$\sim p \vee \sim q \equiv p \rightarrow \sim q$

Therefore, the dual can be written as:

$p \wedge (p \rightarrow \sim q)$

Answer: $p \wedge (p \rightarrow \sim q)$

</details>

---

### Q24. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the statement pattern $(p \vee \sim q) \wedge (\sim p \vee q)$ is true, then which of the following is true?

**Options:**

- **(A)** $p = T, q = F$
- **(B)** both $p$ and $q$ have the same truth value
- **(C)** $p \rightarrow \sim q$ is a contradiction
- **(D)** $p = F, q = T$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) both $p$ and $q$ have the same truth value**

**Detailed Solution:**

The given statement pattern is $(p \vee \sim q) \wedge (\sim p \vee q)$.

We know the logical equivalence $p \rightarrow q \equiv \sim p \vee q$ and $q \rightarrow p \equiv \sim q \vee p \equiv p \vee \sim q$.

Substituting these into the given expression, we get:

$(q \rightarrow p) \wedge (p \rightarrow q)$

This is the definition of the biconditional statement $p \leftrightarrow q$.

The statement $p \leftrightarrow q$ is true if and only if both $p$ and $q$ have the same truth value (i.e., both are true or both are false).

Therefore, both $p$ and $q$ must have the same truth value.

Answer: both $p$ and $q$ have the same truth value

</details>

---

### Q25. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the following statements:
(i) $\sim(p \wedge \sim q)$
(ii) $(p \rightarrow q) \leftrightarrow (\sim q \rightarrow \sim p)$
Result 1 : (i) and (ii) are logically equivalent
Result 2 : (ii) is a contradiction
then which of the following is correct?

**Options:**

- **(A)** Result 1 is true, Result 2 is true
- **(B)** Result 1 is true, Result 2 is false
- **(C)** Result 1 is false, Result 2 is true
- **(D)** Result 1 is false, Result 2 is false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Result 1 is false, Result 2 is false**

**Detailed Solution:**

Statement (i) can be simplified using De Morgan's laws:

$\sim(p \wedge \sim q) \equiv \sim p \vee q \equiv p \rightarrow q$

Statement (ii) is given by:

$(p \rightarrow q) \leftrightarrow (\sim q \rightarrow \sim p)$

We know that $\sim q \rightarrow \sim p$ is the contrapositive of $p \rightarrow q$, which means they are logically equivalent. Therefore, the biconditional statement $(p \rightarrow q) \leftrightarrow (\sim q \rightarrow \sim p)$ is always true, making it a tautology.

Evaluating Result 1:
Statement (i) is $p \rightarrow q$, which is not a tautology (it is false when $p$ is true and $q$ is false). Statement (ii) is a tautology. Since they do not have the same truth values for all assignments, they are not logically equivalent. Thus, Result 1 is false.

Evaluating Result 2:
Statement (ii) is a tautology, which means it is always true. A contradiction is a statement that is always false. Thus, Result 2 is false.

Both Result 1 and Result 2 are false.

Answer: Result 1 is false, Result 2 is false

</details>

---

### Q26. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The switching circuit for the logical expression $(p \wedge q) \vee \sim(p \wedge q)$ is simplified and found to be equivalent to a circuit with:

**Options:**

- **(A)** Two switches in series
- **(B)** Two switches in parallel
- **(C)** A single switch
- **(D)** The lamp always glows

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The lamp always glows**

**Detailed Solution:**

Let $r = p \wedge q$.

The given logical expression becomes $r \vee \sim r$.

By the complement law of Boolean algebra, $r \vee \sim r = \text{True}$ (or $1$).

Since the logical value is always True regardless of the states of the switches $p$ and $q$, the circuit is always closed.

Thus, the current always flows and the lamp always glows.

Answer: The lamp always glows

</details>

---

### Q27. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement "She will earn money if she works" is...

**Options:**

- **(A)** She works and she will earn money
- **(B)** She works and she will not earn money
- **(C)** She will earn money and she works.
- **(D)** She will earn money and she does not work.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) She works and she will not earn money**

**Detailed Solution:**

Let $p$ be the statement "She works".

Let $q$ be the statement "She will earn money".

The given statement "She will earn money if she works" can be rewritten as "If she works, then she will earn money", which is represented as $p \rightarrow q$.

The negation of an implication $p \rightarrow q$ is given by $\sim(p \rightarrow q)$.

Since $p \rightarrow q \equiv \sim p \vee q$, its negation is:

$\sim(\sim p \vee q) \equiv p \wedge \sim q$

The statement $p \wedge \sim q$ translates to "She works and she will not earn money".

Answer: She works and she will not earn money

</details>

---

### Q28. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The inverse of a statement $(p \vee q) \to r$ is

**Options:**

- **(A)** $(p \vee q) \vee \sim r$
- **(B)** $(p \vee q) \vee r$
- **(C)** $(p \vee q) \to \sim r$
- **(D)** $(p \wedge q) \vee \sim r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(p \vee q) \vee \sim r$**

**Detailed Solution:**

The inverse of a conditional statement $A \to B$ is $\sim A \to \sim B$.

For the given statement $(p \vee q) \to r$, we have $A = p \vee q$ and $B = r$.

The inverse is $\sim (p \vee q) \to \sim r$.

Using the logical equivalence $X \to Y \equiv \sim X \vee Y$, we can rewrite the inverse as:

$\sim (\sim (p \vee q)) \vee \sim r$

$(p \vee q) \vee \sim r$

Answer: $(p \vee q) \vee \sim r$

</details>

---

### Q29. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Symbolic form of the circuit
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/12_may_shift_1__q113_d1_v3.png" />
is equivalent to .........

**Options:**

- **(A)** $p\to q$
- **(B)** $p\vee q$
- **(C)** $\sim(p\wedge q)$
- **(D)** $q\to p$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $q\to p$**

**Detailed Solution:**

Let $p$ and $q$ represent the switches $S_1$ and $S_2$ respectively.

The switches $S_1'$ and $S_2'$ are represented by $\sim p$ and $\sim q$.

The given circuit consists of three parallel branches. The symbolic logic expression is:

$p \vee (\sim p \wedge \sim q) \vee (p \wedge q)$

Rearranging the terms, we get:

$\equiv p \vee (p \wedge q) \vee (\sim p \wedge \sim q)$

By the absorption law, $p \vee (p \wedge q) \equiv p$. The expression simplifies to:

$\equiv p \vee (\sim p \wedge \sim q)$

Applying the distributive law:

$\equiv (p \vee \sim p) \wedge (p \vee \sim q)$

Since $p \vee \sim p \equiv T$:

$\equiv T \wedge (p \vee \sim q)$

By the identity law:

$\equiv p \vee \sim q$

$\equiv \sim q \vee p$

This is logically equivalent to the conditional statement $q \rightarrow p$.

</details>

---

### Q30. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The dual statement of "$x=1$ only if $x^2=x$" is

**Options:**

- **(A)** $x=1$ and $x^2=x$
- **(B)** $x\neq 1$ or $x^2=x$
- **(C)** $x\neq 1$ and $x^2=x$
- **(D)** $x=1$ or $x^2\neq x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x\neq 1$ and $x^2=x$**

**Detailed Solution:**

Let $p$ be the statement "$x=1$" and $q$ be the statement "$x^2=x$".

The given statement "$p$ only if $q$" is logically equivalent to $p \rightarrow q$.

We know that the conditional statement $p \rightarrow q$ is logically equivalent to $\sim p \vee q$.

The dual of a compound statement is obtained by replacing the disjunction ($\vee$) with conjunction ($\wedge$) and vice versa.

Therefore, the dual of $\sim p \vee q$ is $\sim p \wedge q$.

Translating this back into words, $\sim p \wedge q$ corresponds to "$x \neq 1$ and $x^2=x$".

Answer: $x\neq 1$ and $x^2=x$

</details>

---

### Q31. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the truth values of $p, q, r, s$ are respectively $T, F, F, T$ then the truth values of the compound statements $\sim(p\to\sim q)$ and $(\sim r\wedge s)\to(p\wedge\sim q)$ are respectively ... and .....

**Options:**

- **(A)** $F, F$
- **(B)** $T, T$
- **(C)** $F, T$
- **(D)** $T, F$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $F, T$**

**Detailed Solution:**

Given $p = T$, $q = F$, $r = F$, $s = T$.

For the first statement $\sim(p \to \sim q)$:
$\sim q = \sim F = T$
$p \to \sim q = T \to T = T$
$\sim(p \to \sim q) = \sim T = F$

For the second statement $(\sim r \wedge s) \to (p \wedge \sim q)$:
$\sim r = \sim F = T$
$\sim r \wedge s = T \wedge T = T$
$p \wedge \sim q = T \wedge T = T$
$(\sim r \wedge s) \to (p \wedge \sim q) = T \to T = T$

The truth values are $F$ and $T$ respectively.

Answer: $F, T$

</details>

---

### Q32. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\sim p \vee q$ is false then which of the following is correct?

**Options:**

- **(A)** $p \leftrightarrow q$ is $T$
- **(B)** $p \rightarrow q$ is $T$
- **(C)** $q \rightarrow p$ is $T$
- **(D)** $q \rightarrow p$ is $F$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $q \rightarrow p$ is $T$**

**Detailed Solution:**

Given $\sim p \vee q$ is false.

A disjunction is false only when both of its components are false.

Therefore, $\sim p$ is false and $q$ is false.

This implies $p$ is true ($T$) and $q$ is false ($F$).

Checking the given options:

$p \leftrightarrow q \equiv T \leftrightarrow F \equiv F$

$p \rightarrow q \equiv T \rightarrow F \equiv F$

$q \rightarrow p \equiv F \rightarrow T \equiv T$

Thus, $q \rightarrow p$ is $T$.

Answer: $q \rightarrow p$ is $T$

</details>

---

### Q33. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The contrapositive of $\sim q \rightarrow p$ is equivalent to

**Options:**

- **(A)** $p \rightarrow q$
- **(B)** $p \wedge q$
- **(C)** $p \vee q$
- **(D)** $\sim p \rightarrow \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $p \vee q$**

**Detailed Solution:**

The contrapositive of a conditional statement $A \rightarrow B$ is $\sim B \rightarrow \sim A$.

For the given statement $\sim q \rightarrow p$, the contrapositive is $\sim p \rightarrow \sim (\sim q)$.

This simplifies to $\sim p \rightarrow q$.

Using the logical equivalence $X \rightarrow Y \equiv \sim X \vee Y$, we get:

$\sim p \rightarrow q \equiv \sim (\sim p) \vee q \equiv p \vee q$.

Answer: $p \vee q$

</details>

---

### Q34. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the following statements.
$p$: If $3^4 > 4^3$, then $3^3 > 4^4$
$q$: The roots of the equation $x^2 - 2x + 2 = 0$ are real if and only if Mumbai is in Maharashtra.
$r$: Statement $p$ is true or statement $q$ is false.
Which of the following has truth value T (true)?

**Options:**

- **(A)** $(p \vee q) \wedge r$
- **(B)** $p \vee (q \wedge r)$
- **(C)** $p \wedge (q \vee r)$
- **(D)** $(p \wedge q) \vee r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(p \wedge q) \vee r$**

**Detailed Solution:**

Evaluate the truth value of statement $p$:
$3^4 = 81$ and $4^3 = 64$, so $3^4 > 4^3$ is True (T).
$3^3 = 27$ and $4^4 = 256$, so $3^3 > 4^4$ is False (F).
Statement $p$ is of the form $T \rightarrow F$, which is False. Thus, $p \equiv F$.

Evaluate the truth value of statement $q$:
The discriminant of $x^2 - 2x + 2 = 0$ is $D = 4 - 8 = -4 < 0$, so the roots are not real. This part is False (F).
"Mumbai is in Maharashtra" is True (T).
Statement $q$ is of the form $F \leftrightarrow T$, which is False. Thus, $q \equiv F$.

Evaluate the truth value of statement $r$:
"Statement $p$ is true" is False (since $p \equiv F$).
"Statement $q$ is false" is True (since $q \equiv F$).
Statement $r$ is of the form $F \vee T$, which is True. Thus, $r \equiv T$.

Now, check the truth values of the given options:
$(p \vee q) \wedge r \equiv (F \vee F) \wedge T \equiv F \wedge T \equiv F$
$p \vee (q \wedge r) \equiv F \vee (F \wedge T) \equiv F \vee F \equiv F$
$p \wedge (q \vee r) \equiv F \wedge (F \vee T) \equiv F \wedge T \equiv F$
$(p \wedge q) \vee r \equiv (F \wedge F) \vee T \equiv F \vee T \equiv T$

Therefore, $(p \wedge q) \vee r$ has the truth value T.

Answer: $(p \wedge q) \vee r$

</details>

---

### Q35. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following is/are not true ?
I) If 1 is not a prime number, then 2 is not a prime number.
II) e is a vowel and $12 \times 3 = 36$
III) It is not true that 14 is a composite number and 3 is even number.
IV) $\sqrt{5}$ is an irrational number, but $3 + \sqrt{5}$ is a complex number.

**Options:**

- **(A)** Only I and IV
- **(B)** Only I
- **(C)** Only II and III
- **(D)** Only I, II and IV

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Only I**

**Detailed Solution:**

Let us evaluate the truth value of each statement:

Statement I: "If $1$ is not a prime number, then $2$ is not a prime number."
This is a conditional statement of the form $p \rightarrow q$.
$p$: $1$ is not a prime number (True).
$q$: $2$ is not a prime number (False, since $2$ is a prime number).
The truth value of $T \rightarrow F$ is False. Thus, Statement I is not true.

Statement II: "e is a vowel and $12 \times 3 = 36$"
This is a conjunction of the form $p \wedge q$.
$p$: e is a vowel (True).
$q$: $12 \times 3 = 36$ (True).
The truth value of $T \wedge T$ is True. Thus, Statement II is true.

Statement III: "It is not true that $14$ is a composite number and $3$ is even number."
This is of the form $\sim(p \wedge q)$.
$p$: $14$ is a composite number (True).
$q$: $3$ is an even number (False).
The truth value of $p \wedge q$ is $T \wedge F \equiv F$.
Therefore, $\sim(F)$ is True. Thus, Statement III is true.

Statement IV: "$\sqrt{5}$ is an irrational number, but $3 + \sqrt{5}$ is a complex number."
The word "but" acts as a logical "and" ($\wedge$).
$p$: $\sqrt{5}$ is an irrational number (True).
$q$: $3 + \sqrt{5}$ is a complex number (True, since every real number is a complex number with an imaginary part of $0$).
The truth value of $T \wedge T$ is True. Thus, Statement IV is true.

Therefore, only Statement I is not true.

Answer: Only I

</details>

---

### Q36. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The negation of the inverse of the statement $\sim p \vee \sim q$ is...

**Options:**

- **(A)** $p \wedge q$
- **(B)** $\sim p \wedge q$
- **(C)** $\sim p \wedge \sim q$
- **(D)** $p \vee q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sim p \wedge \sim q$**

**Detailed Solution:**

The given statement is $\sim p \vee \sim q$.

We know that a disjunction $A \vee B$ can be expressed as a conditional statement $\sim A \rightarrow B$.

Thus, the statement $\sim p \vee \sim q$ can be written as $p \rightarrow \sim q$.

The inverse of a conditional statement $A \rightarrow B$ is $\sim A \rightarrow \sim B$.

Therefore, the inverse of $p \rightarrow \sim q$ is $\sim p \rightarrow \sim(\sim q)$, which simplifies to $\sim p \rightarrow q$.

Converting this inverse back to a logical disjunction, we get $\sim(\sim p) \vee q \equiv p \vee q$.

The negation of this inverse is $\sim(p \vee q)$.

By De Morgan's Law, $\sim(p \vee q) \equiv \sim p \wedge \sim q$.

Answer: $\sim p \wedge \sim q$

</details>

---

### Q37. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the truth value of $[(p \vee q) \wedge (q \to r) \wedge (\sim r)] \to (p \wedge q)$ is false, then which of the following is <strong>NOT</strong> true?

**Options:**

- **(A)** Truth value of $p \to q$ is False
- **(B)** Truth value of $p \to r$ is False.
- **(C)** Truth value of $(\sim q) \to p$ is False.
- **(D)** The truth value of $(\sim p) \wedge r$ is False.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Truth value of $(\sim q) \to p$ is False.**

**Detailed Solution:**

Given that the truth value of $[(p \vee q) \wedge (q \to r) \wedge (\sim r)] \to (p \wedge q)$ is False.

An implication $A \to B$ is False if and only if $A$ is True and $B$ is False. Therefore, the antecedent $(p \vee q) \wedge (q \to r) \wedge (\sim r)$ is True and the consequent $p \wedge q$ is False.

For the antecedent to be True, each of its conjuncts must be True:
1) $\sim r$ is True $\Rightarrow r$ is False.
2) $q \to r$ is True. Since $r$ is False, $q$ must be False (otherwise $T \to F$ would be False).
3) $p \vee q$ is True. Since $q$ is False, $p$ must be True.

Checking the consequent: $p \wedge q \equiv T \wedge F \equiv F$, which is consistent.

Thus, the truth values are: $p$ is True, $q$ is False, and $r$ is False.

Now, evaluating the given options:
1) $p \to q \equiv T \to F \equiv F$. The statement "Truth value of $p \to q$ is False" is True.
2) $p \to r \equiv T \to F \equiv F$. The statement "Truth value of $p \to r$ is False" is True.
3) $(\sim q) \to p \equiv (\sim F) \to T \equiv T \to T \equiv T$. The statement "Truth value of $(\sim q) \to p$ is False" is False.
4) $(\sim p) \wedge r \equiv (\sim T) \wedge F \equiv F \wedge F \equiv F$. The statement "The truth value of $(\sim p) \wedge r$ is False" is True.

Therefore, the statement in the third option is NOT true.

Answer: Truth value of $(\sim q) \to p$ is False.

</details>

---

### Q38. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If p, q, r are simple propositions with truth values T, F, T respectively, then which of the following is not a true statement?

**Options:**

- **(A)** $[q \wedge (p \to q)] \to p$
- **(B)** $(p \wedge q) \to (q \vee \sim p)$
- **(C)** $[(\sim p \vee q) \wedge \sim r] \leftrightarrow p$
- **(D)** $(p \wedge q) \vee (\sim q \vee r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $[(\sim p \vee q) \wedge \sim r] \leftrightarrow p$**

**Detailed Solution:**

Given $p = T$, $q = F$, $r = T$.

Evaluating the first option:
$[q \wedge (p \to q)] \to p \equiv [F \wedge (T \to F)] \to T \equiv [F \wedge F] \to T \equiv F \to T \equiv T$

Evaluating the second option:
$(p \wedge q) \to (q \vee \sim p) \equiv (T \wedge F) \to (F \vee F) \equiv F \to F \equiv T$

Evaluating the third option:
$[(\sim p \vee q) \wedge \sim r] \leftrightarrow p \equiv [(F \vee F) \wedge F] \leftrightarrow T \equiv [F \wedge F] \leftrightarrow T \equiv F \leftrightarrow T \equiv F$

Evaluating the fourth option:
$(p \wedge q) \vee (\sim q \vee r) \equiv (T \wedge F) \vee (T \vee T) \equiv F \vee T \equiv T$

The statement in the third option is not true.

Answer: $[(\sim p \vee q) \wedge \sim r] \leftrightarrow p$

</details>

---

### Q39. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\sim p \to q$ is false and $q \leftrightarrow r$ is false, then the truth value of $(p, q, r)$ is...

**Options:**

- **(A)** $(T, F, T)$
- **(B)** $(F, T, F)$
- **(C)** $(F, F, T)$
- **(D)** $(F, T, T)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(F, F, T)$**

**Detailed Solution:**

The implication $\sim p \to q$ is given as false.

An implication $A \to B$ is false if and only if $A$ is true and $B$ is false.

Therefore, $\sim p$ is true and $q$ is false.

Since $\sim p$ is true, $p$ must be false ($F$). Thus, $p = F$ and $q = F$.

The biconditional $q \leftrightarrow r$ is given as false.

A biconditional $A \leftrightarrow B$ is false if and only if $A$ and $B$ have opposite truth values.

Since $q$ is false, $r$ must be true ($T$).

The truth values of $(p, q, r)$ are $(F, F, T)$.

Answer: $(F, F, T)$

</details>

---

### Q40. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The simplified switching circuit for the following circuit is
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_1__q113_d1.png" />

**Options:**

- **(A)** <img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_1__q113_d2.png" />
- **(B)** <img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_1__q113_d3.png" />
- **(C)** <img style="width: 250px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_1__q113_d4.png" />
- **(D)** <img style="width: 250px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_1__q113_d5.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_1__q113_d2.png" />**

**Detailed Solution:**

Let $p, q, r$ represent the switches $S_1, S_2, S_3$ respectively.

The Boolean expression for the top branch is $p \wedge (q \vee r)$.

The Boolean expression for the bottom branch is $\sim r \wedge \sim q \wedge p$, which can be rewritten as $p \wedge (\sim q \wedge \sim r)$.

The total circuit is the parallel combination of these two branches, so the expression is:

$[p \wedge (q \vee r)] \vee [p \wedge (\sim q \wedge \sim r)]$

Using De Morgan's Law, $\sim q \wedge \sim r \equiv \sim(q \vee r)$.

Substituting this, we get:

$[p \wedge (q \vee r)] \vee [p \wedge \sim(q \vee r)]$

Using the distributive law, we can factor out $p$:

$p \wedge [(q \vee r) \vee \sim(q \vee r)]$

Since $A \vee \sim A \equiv T$ (where $T$ represents a closed circuit or tautology), we have:

$p \wedge T \equiv p$

This means the simplified circuit consists only of the switch $S_1$.

Answer: <img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_1__q113_d2.png" />

</details>

---

### Q41. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The logical statement $(p \vee q) \wedge [(\sim p \wedge q) \vee (p \wedge \sim q)] \wedge \sim q$ is logically equivalent to ...

**Options:**

- **(A)** $p \wedge \sim q$
- **(B)** $\sim p \wedge q$
- **(C)** $p \wedge q$
- **(D)** $\sim p \vee \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $p \wedge \sim q$**

**Detailed Solution:**

Given statement: $(p \vee q) \wedge [(\sim p \wedge q) \vee (p \wedge \sim q)] \wedge \sim q$

Consider the part $[(\sim p \wedge q) \vee (p \wedge \sim q)] \wedge \sim q$

Using distributive law:

$= ((\sim p \wedge q) \wedge \sim q) \vee ((p \wedge \sim q) \wedge \sim q)$

$= (\sim p \wedge (q \wedge \sim q)) \vee (p \wedge (\sim q \wedge \sim q))$

$= (\sim p \wedge F) \vee (p \wedge \sim q)$

$= F \vee (p \wedge \sim q)$

$= p \wedge \sim q$

Now, substitute this back into the original statement:

$= (p \vee q) \wedge (p \wedge \sim q)$

Using distributive law:

$= (p \wedge (p \wedge \sim q)) \vee (q \wedge (p \wedge \sim q))$

$= ((p \wedge p) \wedge \sim q) \vee (p \wedge (q \wedge \sim q))$

$= (p \wedge \sim q) \vee (p \wedge F)$

$= (p \wedge \sim q) \vee F$

$= p \wedge \sim q$

Answer: $p \wedge \sim q$

</details>

---

### Q42. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following logical statements is a tautology?

**Options:**

- **(A)** $[(p \rightarrow q) \wedge \sim q] \rightarrow \sim p$
- **(B)** $(p \rightarrow q) \wedge (p \wedge \sim q)$
- **(C)** $[(p \vee q) \wedge \sim p] \wedge \sim q$
- **(D)** $[(p \vee \sim q) \vee (\sim p \wedge q)] \wedge r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $[(p \rightarrow q) \wedge \sim q] \rightarrow \sim p$**

**Detailed Solution:**

Consider the first option: $[(p \rightarrow q) \wedge \sim q] \rightarrow \sim p$

Using logical equivalences, we know that $p \rightarrow q \equiv \sim p \vee q$.

Substituting this into the premise:
$(p \rightarrow q) \wedge \sim q \equiv (\sim p \vee q) \wedge \sim q$
$\equiv (\sim p \wedge \sim q) \vee (q \wedge \sim q)$
$\equiv (\sim p \wedge \sim q) \vee F$
$\equiv \sim p \wedge \sim q$

Now, substituting this back into the original statement:
$(\sim p \wedge \sim q) \rightarrow \sim p$
$\equiv \sim(\sim p \wedge \sim q) \vee \sim p$
$\equiv (p \vee q) \vee \sim p$
$\equiv (p \vee \sim p) \vee q$
$\equiv T \vee q \equiv T$

Since the final truth value is always True ($T$), this statement is a tautology.

Checking the other options for completeness:
$(p \rightarrow q) \wedge (p \wedge \sim q) \equiv (\sim p \vee q) \wedge \sim(\sim p \vee q) \equiv F$ (Contradiction)

$[(p \vee q) \wedge \sim p] \wedge \sim q \equiv (q \wedge \sim p) \wedge \sim q \equiv \sim p \wedge (q \wedge \sim q) \equiv F$ (Contradiction)

$[(p \vee \sim q) \vee (\sim p \wedge q)] \wedge r \equiv [(p \vee \sim q \vee \sim p) \wedge (p \vee \sim q \vee q)] \wedge r \equiv (T \wedge T) \wedge r \equiv r$ (Not a tautology)

Answer: $[(p \rightarrow q) \wedge \sim q] \rightarrow \sim p$

</details>

---

### Q43. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a switching circuit, if the combination $(S_1 \wedge S_2)$ is connected in parallel to the combination $(S_1' \wedge S_2')$, then the room is lit only when $\ldots$

**Options:**

- **(A)** $S_1$ is ON and $S_2$ is OFF
- **(B)** $S_1$ is OFF and $S_2$ is ON
- **(C)** $S_1$ and $S_2$ both ON or $S_1$ and $S_2$ both OFF
- **(D)** The room is always lit.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $S_1$ and $S_2$ both ON or $S_1$ and $S_2$ both OFF**

**Detailed Solution:**

The boolean expression for the given switching circuit is $(S_1 \wedge S_2) \vee (S_1' \wedge S_2')$.

Let $p$ and $q$ represent the truth values of switches $S_1$ and $S_2$ respectively.

The room is lit when the expression $(p \wedge q) \vee (\sim p \wedge \sim q)$ evaluates to True.

This expression is True if and only if both $p$ and $q$ are True, or both $p$ and $q$ are False.

Thus, the room is lit only when $S_1$ and $S_2$ are both ON, or $S_1$ and $S_2$ are both OFF.

Answer: $S_1$ and $S_2$ both ON or $S_1$ and $S_2$ both OFF

</details>

---

### Q44. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the truth value of the statement pattern $(\sim p \wedge q) \vee (\sim p \wedge \sim q) \vee (p \wedge \sim q)$ is $F$, then the truth values of $(p \vee \sim q)$ and $(p \to q)$ are $\ldots$ respectively.

**Options:**

- **(A)** $F, F$
- **(B)** $F, T$
- **(C)** $T, T$
- **(D)** $T, F$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $T, T$**

**Detailed Solution:**

The given statement pattern is $(\sim p \wedge q) \vee (\sim p \wedge \sim q) \vee (p \wedge \sim q)$.

Simplifying the first two terms using the distributive law:

$(\sim p \wedge q) \vee (\sim p \wedge \sim q) \equiv \sim p \wedge (q \vee \sim q) \equiv \sim p \wedge T \equiv \sim p$

The statement pattern then becomes:

$\sim p \vee (p \wedge \sim q)$

Using the distributive law again:

$(\sim p \vee p) \wedge (\sim p \vee \sim q) \equiv T \wedge (\sim p \vee \sim q) \equiv \sim p \vee \sim q$

It is given that the truth value of this pattern is $F$.

$\sim p \vee \sim q \equiv F$

This is possible only when both $\sim p$ and $\sim q$ are $F$.

Thus, $p \equiv T$ and $q \equiv T$.

Now, substituting the truth values of $p$ and $q$ into the required expressions:

$p \vee \sim q \equiv T \vee F \equiv T$

$p \to q \equiv T \to T \equiv T$

The truth values are $T, T$ respectively.

Answer: $T, T$

</details>

---

### Q45. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The minimum number of switches in the simplified form of the following switching circuit is
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/17_april_shift_2__q111_d1.png" />

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

Let the switches $S_1, S_2, S_3$ be represented by boolean variables $p, q, r$ respectively. Then $S_1', S_2'$ represent their complements $p', q'$.

The given switching circuit consists of three parallel branches. We can write the boolean expression for the circuit as:
$L = (S_1 \cdot S_2) + (S_1' \cdot S_2) + (S_3 \cdot S_2')$

Substituting the variables, we get:
$L = (p \cdot q) + (p' \cdot q) + (r \cdot q')$

Now, we simplify the boolean expression:
Factor out $q$ from the first two terms:
$L = q \cdot (p + p') + r \cdot q'$

Since $p + p' = 1$ (a boolean variable and its complement always sum to 1):
$L = q \cdot 1 + r \cdot q'$
$L = q + q' \cdot r$

Using the distributive law $A + A'B = A + B$, we can further simplify:
$L = (q + q') \cdot (q + r)$
$L = 1 \cdot (q + r)$
$L = q + r$

Converting back to the switch notation, the simplified expression is:
$L = S_2 + S_3$

This simplified expression represents two switches ($S_2$ and $S_3$) connected in parallel. Therefore, the minimum number of switches in the simplified form is $2$.

Answer: $2$

</details>

---

### Q46. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The correct logical equivalence from the following is /are ___
(I) $p \to (q \to r) \equiv (p \wedge q) \to r$
(II) $(p \to q) \to r \equiv p \to (q \vee r)$
(III) $(p \to q) \to r \equiv (p \to r) \wedge (\sim q \to r)$
(IV) $p \to (q \to r) \equiv q \to (p \to r)$

**Options:**

- **(A)** only (I) and (II)
- **(B)** only (III) and (IV)
- **(C)** only (II) and (IV)
- **(D)** only (I) and (IV)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) only (I) and (IV)**

**Detailed Solution:**

Using the property $A \to B \equiv \sim A \vee B$, we evaluate each statement.

For (I):
$p \to (q \to r) \equiv \sim p \vee (\sim q \vee r) \equiv (\sim p \vee \sim q) \vee r \equiv \sim(p \wedge q) \vee r \equiv (p \wedge q) \to r$
Statement (I) is correct.

For (II):
$(p \to q) \to r \equiv (\sim p \vee q) \to r \equiv \sim(\sim p \vee q) \vee r \equiv (p \wedge \sim q) \vee r \equiv (p \vee r) \wedge (\sim q \vee r)$
$p \to (q \vee r) \equiv \sim p \vee q \vee r$
Statement (II) is incorrect.

For (III):
$(p \to q) \to r \equiv (p \vee r) \wedge (\sim q \vee r)$
$(p \to r) \wedge (\sim q \to r) \equiv (\sim p \vee r) \wedge (q \vee r)$
Statement (III) is incorrect.

For (IV):
$p \to (q \to r) \equiv \sim p \vee \sim q \vee r$
$q \to (p \to r) \equiv \sim q \vee (\sim p \vee r) \equiv \sim p \vee \sim q \vee r$
Statement (IV) is correct.

Therefore, only (I) and (IV) are correct.

Answer: only (I) and (IV)

</details>

---

### Q47. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The contrapositive of the statement pattern $[p \vee (p \to q)] \to (p \wedge \sim q)$ is

**Options:**

- **(A)** $(p \wedge \sim q) \to [p \wedge (p \to q)]$
- **(B)** $(\sim p \wedge \sim q) \to [\sim p \wedge (p \to \sim q)]$
- **(C)** $(\sim p \vee q) \wedge [\sim p \vee (p \wedge \sim q)]$
- **(D)** $(\sim p \vee q) \to [\sim p \wedge (p \wedge \sim q)]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim p \vee q) \to [\sim p \wedge (p \wedge \sim q)]$**

**Detailed Solution:**

Let the given statement be $X \to Y$, where $X = p \vee (p \to q)$ and $Y = p \wedge \sim q$.

The contrapositive of $X \to Y$ is $\sim Y \to \sim X$.

First, we find $\sim Y$:
$\sim Y = \sim (p \wedge \sim q) = \sim p \vee q$

Next, we find $\sim X$:
$\sim X = \sim [p \vee (p \to q)]$
Using De Morgan's Law, we get:
$\sim X = \sim p \wedge \sim (p \to q)$

Since $p \to q \equiv \sim p \vee q$, its negation is $\sim (p \to q) \equiv p \wedge \sim q$.
Substituting this back, we get:
$\sim X = \sim p \wedge (p \wedge \sim q)$

Therefore, the contrapositive $\sim Y \to \sim X$ is:
$(\sim p \vee q) \to [\sim p \wedge (p \wedge \sim q)]$

</details>

---

### Q48. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the converse of $p \vee q$ is

**Options:**

- **(A)** $\sim p \vee q$
- **(B)** $p \wedge q$
- **(C)** $p \vee \sim q$
- **(D)** $\sim p \wedge \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $p \wedge q$**

**Detailed Solution:**

The statement $p \vee q$ can be expressed as a conditional statement: $\sim p \rightarrow q$.

The converse of a conditional statement $A \rightarrow B$ is $B \rightarrow A$.

Therefore, the converse of $\sim p \rightarrow q$ is $q \rightarrow \sim p$.

The statement $q \rightarrow \sim p$ is logically equivalent to $\sim q \vee \sim p$.

The negation of this converse is $\sim(q \rightarrow \sim p) \equiv \sim(\sim q \vee \sim p)$.

Using De Morgan's laws, $\sim(\sim q \vee \sim p) \equiv q \wedge p \equiv p \wedge q$.

Answer: $p \wedge q$

</details>

---

### Q49. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following statements is/are False?
$S_1 : \exists\, n \in N$, such that $n^2 + n + 2$ is divisible by 4.
$S_2 : \exists\, x \in N$, such that $x - 17 < 20$.
$S_3 : \forall\, n \in N, \quad x^2 + 3x - 10 = 0$.
$S_4 : \forall\, n \in N, \quad n^2 \geq 1$.

**Options:**

- **(A)** $S_1$ and $S_2$.
- **(B)** $S_1$ and $S_3$.
- **(C)** Only $S_3$.
- **(D)** $S_2$ and $S_4$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Only $S_3$.**

**Detailed Solution:**

For $S_1$: Let $n = 1 \in N$. Then $n^2 + n + 2 = 1^2 + 1 + 2 = 4$, which is divisible by $4$. Thus, there exists at least one natural number satisfying the condition, making $S_1$ true.

For $S_2$: Let $x = 1 \in N$. Then $x - 17 = 1 - 17 = -16$, which is strictly less than $20$. Thus, there exists at least one natural number satisfying the condition, making $S_2$ true.

For $S_3$: The statement asserts that for all natural numbers, the equation $x^2 + 3x - 10 = 0$ holds. However, $x^2 + 3x - 10 = (x + 5)(x - 2) = 0$ is only satisfied for $x = 2$ and $x = -5$. It does not hold for all natural numbers (for example, $x = 1$ gives $-6 \neq 0$). Thus, $S_3$ is false.

For $S_4$: The set of natural numbers is $N = \{1, 2, 3, \dots\}$. For any $n \in N$, we have $n \geq 1$, which implies $n^2 \geq 1$. Thus, $S_4$ is true.

Therefore, only statement $S_3$ is false.

Answer: Only $S_3$.

</details>

---

### Q50. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The negation of $(p \wedge q) \rightarrow ((p \vee r) \rightarrow\, \sim q)$ is equivalent to ...

**Options:**

- **(A)** $p \wedge q$
- **(B)** $p \wedge\, \sim r$
- **(C)** $q \wedge (p \vee r)$
- **(D)** $\sim p \wedge\, \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $p \wedge q$**

**Detailed Solution:**

Let the given statement be $S \equiv (p \wedge q) \rightarrow ((p \vee r) \rightarrow \sim q)$.

The negation of a conditional statement $X \rightarrow Y$ is $X \wedge \sim Y$.

$\sim S \equiv (p \wedge q) \wedge \sim((p \vee r) \rightarrow \sim q)$

Applying the negation rule again to the second part:

$\sim S \equiv (p \wedge q) \wedge ((p \vee r) \wedge \sim(\sim q))$

$\sim S \equiv (p \wedge q) \wedge ((p \vee r) \wedge q)$

Using the associative and idempotent laws ($q \wedge q \equiv q$):

$\sim S \equiv p \wedge q \wedge (p \vee r)$

Using the absorption law, $p \wedge (p \vee r) \equiv p$:

$\sim S \equiv (p \wedge (p \vee r)) \wedge q$

$\sim S \equiv p \wedge q$

Answer: $p \wedge q$

</details>

---

### Q51. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $[(p \wedge q) \rightarrow (\sim p \vee r)] \vee [(\sim p \vee r) \rightarrow (p \wedge q)]$ is

**Options:**

- **(A)** a contradiction
- **(B)** a tautology
- **(C)** equivalent to $(p \wedge q) \vee r$.
- **(D)** equivalent to $(p \vee q)$ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a tautology**

**Detailed Solution:**

Let $A = p \wedge q$ and $B = \sim p \vee r$.

The given statement pattern can be written as $(A \rightarrow B) \vee (B \rightarrow A)$.

Using the logical equivalence $X \rightarrow Y \equiv \sim X \vee Y$, the expression becomes:

$(\sim A \vee B) \vee (\sim B \vee A)$

Using the commutative and associative properties of disjunction, we can rearrange the terms as:

$(\sim A \vee A) \vee (\sim B \vee B)$

We know that for any statement $X$, $\sim X \vee X \equiv T$ (where $T$ represents a tautology).

Substituting this into the expression, we get:

$T \vee T \equiv T$

Therefore, the given statement pattern is a tautology.

Answer: a tautology

</details>

---

### Q52. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the statements
p: If voltage increases then current decreases.
q : If voltage does not increases then current does not decreases.
r : If current decreases then voltage increases.
s : If current does not decreases then voltage does not increases.
then which of the following pairs of statements having same meaning

**Options:**

- **(A)** p, q and r, s
- **(B)** p, r and q, s
- **(C)** p, s and q, r
- **(D)** no pair having same meaning

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) p, s and q, r**

**Detailed Solution:**

Let $V$ be the statement "voltage increases".

Let $C$ be the statement "current decreases".

The given statements can be represented symbolically as:

$p : V \rightarrow C$

$q : \sim V \rightarrow \sim C$

$r : C \rightarrow V$

$s : \sim C \rightarrow \sim V$

A conditional statement is logically equivalent to its contrapositive ($A \rightarrow B \equiv \sim B \rightarrow \sim A$).

The contrapositive of statement $p$ ($V \rightarrow C$) is $\sim C \rightarrow \sim V$, which is exactly statement $s$. Thus, $p$ and $s$ are logically equivalent.

The contrapositive of statement $q$ ($\sim V \rightarrow \sim C$) is $C \rightarrow V$, which is exactly statement $r$. Thus, $q$ and $r$ are logically equivalent.

Therefore, the pairs of statements having the same meaning are $p, s$ and $q, r$.

Answer: p, s and q, r

</details>

---

### Q53. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $p \to (q \vee \sim r)$ is false, then the truth values of $(p \leftrightarrow q) \wedge r$ and $\sim p \to \sim q$ are :

**Options:**

- **(A)** $T, T$
- **(B)** $T, F$
- **(C)** $F, T$
- **(D)** $F, F$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $F, T$**

**Detailed Solution:**

Given $p \to (q \vee \sim r)$ is false.

An implication $A \to B$ is false if and only if $A$ is true and $B$ is false.

Thus, $p$ is $T$ and $q \vee \sim r$ is $F$.

For a disjunction $q \vee \sim r$ to be false, both components must be false. Therefore, $q$ is $F$ and $\sim r$ is $F$, which means $r$ is $T$.

We have the truth values: $p = T$, $q = F$, $r = T$.

Evaluating the first expression $(p \leftrightarrow q) \wedge r$ :
$(T \leftrightarrow F) \wedge T \equiv F \wedge T \equiv F$

Evaluating the second expression $\sim p \to \sim q$ :
$\sim T \to \sim F \equiv F \to T \equiv T$

The truth values are $F$ and $T$.

</details>

---

### Q54. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the truth value of the compound statement $[(p \leftrightarrow q) \wedge (q \to r) \wedge \sim r] \to (p \wedge \sim q)$ is false, then the truth values of the statement patterns $(p \to q) \leftrightarrow (q \to r)$ and $\sim(p \vee r) \to (q \wedge p)$ are, respectively ...

**Options:**

- **(A)** $(T, T)$
- **(B)** $(T, F)$
- **(C)** $(F, T)$
- **(D)** $(F, F)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(T, F)$**

**Detailed Solution:**

The given compound statement is $[(p \leftrightarrow q) \wedge (q \to r) \wedge \sim r] \to (p \wedge \sim q)$.

An implication $X \to Y$ is false if and only if $X$ is true and $Y$ is false.

Thus, $(p \leftrightarrow q) \wedge (q \to r) \wedge \sim r$ is true and $p \wedge \sim q$ is false.

For the conjunction $(p \leftrightarrow q) \wedge (q \to r) \wedge \sim r$ to be true, each of its components must be true:
$\sim r$ is true $\Rightarrow r = F$
$q \to r$ is true $\Rightarrow q \to F$ is true $\Rightarrow q = F$
$p \leftrightarrow q$ is true $\Rightarrow p \leftrightarrow F$ is true $\Rightarrow p = F$

Checking the second part with these values: $p \wedge \sim q = F \wedge T = F$, which satisfies the condition that $Y$ is false.

So, the truth values are $p = F$, $q = F$, $r = F$.

Now, evaluating the first statement pattern:
$(p \to q) \leftrightarrow (q \to r)$
$= (F \to F) \leftrightarrow (F \to F)$
$= T \leftrightarrow T = T$

Evaluating the second statement pattern:
$\sim(p \vee r) \to (q \wedge p)$
$= \sim(F \vee F) \to (F \wedge F)$
$= \sim F \to F$
$= T \to F = F$

The truth values are $T$ and $F$, respectively.

Answer: $(T, F)$

</details>

---

### Q55. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The negation of the contrapositive of the statement $(p \vee \sim q) \to (p \wedge \sim q)$ is

**Options:**

- **(A)** $(p \wedge \sim q) \vee (\sim p \wedge \sim q)$
- **(B)** $(\sim p \wedge q) \vee (p \wedge \sim q)$
- **(C)** $(\sim p \vee \sim q) \wedge (p \vee q)$
- **(D)** $(\sim p \vee q) \wedge (p \vee \sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim p \vee q) \wedge (p \vee \sim q)$**

**Detailed Solution:**

The contrapositive of a conditional statement $X \to Y$ is logically equivalent to the statement itself.

Therefore, the negation of the contrapositive of $X \to Y$ is logically equivalent to the negation of $X \to Y$.

The negation of $X \to Y$ is $X \wedge \sim Y$.

Given the statement $(p \vee \sim q) \to (p \wedge \sim q)$, we have $X = p \vee \sim q$ and $Y = p \wedge \sim q$.

The negation of the statement is:

$X \wedge \sim Y = (p \vee \sim q) \wedge \sim (p \wedge \sim q)$

By De Morgan's laws, $\sim (p \wedge \sim q) \equiv \sim p \vee q$.

Substituting this back, we get:

$(p \vee \sim q) \wedge (\sim p \vee q)$

Rearranging the terms, this is identical to $(\sim p \vee q) \wedge (p \vee \sim q)$.

</details>

---

### Q56. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Simplest form of the following switching circuit is
<img style="width: 350px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_1__q132_d1.png" />

**Options:**

- **(A)** <img style="width: 250px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_1__q132_d2.png" />
- **(B)** <img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_1__q132_d3.png" />
- **(C)** <img style="width: 250px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_1__q132_d4.png" />
- **(D)** <img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_1__q132_d5.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_1__q132_d3.png" />**

**Detailed Solution:**

Let $p$ represent the switch $S_1$ and $q$ represent the switch $S_2$.

The given switching circuit consists of three parallel branches. The logical expression for the entire circuit is:

$E = (p \land q) \lor (p \land \sim q) \lor (\sim p \land q)$

We can simplify this boolean expression by grouping the first two terms:

$E = [p \land (q \lor \sim q)] \lor (\sim p \land q)$

Since $q \lor \sim q$ is always true (a tautology, denoted as $T$), we have:

$E = (p \land T) \lor (\sim p \land q)$

$E = p \lor (\sim p \land q)$

Applying the distributive law:

$E = (p \lor \sim p) \land (p \lor q)$

Again, since $p \lor \sim p$ is a tautology ($T$):

$E = T \land (p \lor q)$

$E = p \lor q$

This simplified logical expression represents a circuit where switches $S_1$ and $S_2$ are connected in parallel.

Answer: <img style="width: 200px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_1__q132_d3.png" />

</details>

---

### Q57. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The dual of the statement pattern $(p \wedge \sim q) \longrightarrow (q \wedge \sim p)$ is equivalent to

**Options:**

- **(A)** $\sim(p \rightarrow q) \wedge (q \rightarrow p)$
- **(B)** $(p \rightarrow q) \wedge \sim(q \rightarrow p)$
- **(C)** $(\sim p \rightarrow q) \wedge (q \rightarrow p)$
- **(D)** $(q \rightarrow p) \vee (\sim p \rightarrow \sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(p \rightarrow q) \wedge \sim(q \rightarrow p)$**

**Detailed Solution:**

First, convert the given statement pattern into logical connectives $\vee$, $\wedge$, and $\sim$.

$(p \wedge \sim q) \longrightarrow (q \wedge \sim p) \equiv \sim(p \wedge \sim q) \vee (q \wedge \sim p)$

Applying De Morgan's Law, we get:

$\equiv (\sim p \vee q) \vee (q \wedge \sim p)$

To find the dual of the statement, replace $\vee$ with $\wedge$ and $\wedge$ with $\vee$:

Dual $\equiv (\sim p \wedge q) \wedge (q \vee \sim p)$

Since $(\sim p \wedge q)$ implies $(q \vee \sim p)$, their conjunction simplifies to:

Dual $\equiv \sim p \wedge q$

Now, evaluating the given options to find the equivalent expression:

For the second option:

$(p \rightarrow q) \wedge \sim(q \rightarrow p)$

$\equiv (\sim p \vee q) \wedge \sim(\sim q \vee p)$

$\equiv (\sim p \vee q) \wedge (q \wedge \sim p)$

Since $(q \wedge \sim p)$ implies $(\sim p \vee q)$, their conjunction simplifies to:

$\equiv q \wedge \sim p$

$\equiv \sim p \wedge q$

This matches the simplified dual statement.

Answer: $(p \rightarrow q) \wedge \sim(q \rightarrow p)$

</details>

---

### Q58. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Negation of the statement "If an integer is greater than 4 and less than 5, then it is a multiple of 3", is

**Options:**

- **(A)** An integer is not greater than 4 but less than 5 and it is a multiple of 3.
- **(B)** If an integer is not greater than 4 and less than 5 then it is not a multiple of 3.
- **(C)** An integer is greater than 4 and less than 5 but it is not a multiple of 3.
- **(D)** An integer is not greater than 4 and not less than 5 but it is not a multiple of 3.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) An integer is greater than 4 and less than 5 but it is not a multiple of 3.**

**Detailed Solution:**

Let $p$ be the statement "An integer is greater than 4 and less than 5".

Let $q$ be the statement "it is a multiple of 3".

The given statement is of the form $p \rightarrow q$.

The negation of an implication $p \rightarrow q$ is given by $\sim(p \rightarrow q) \equiv p \wedge \sim q$.

Therefore, the negation of the given statement is "An integer is greater than 4 and less than 5 but it is not a multiple of 3".

Answer: An integer is greater than 4 and less than 5 but it is not a multiple of 3.

</details>

---

### Q59. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The dual of the converse of the inverse of the logical statement $p \to (q \to r)$ is equivalent to...

**Options:**

- **(A)** $\sim [p \vee (r \to q)]$
- **(B)** $p \vee (r \to q)$
- **(C)** $\sim [p \vee (q \to r)]$
- **(D)** $p \vee (q \to r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sim [p \vee (r \to q)]$**

**Detailed Solution:**

The given statement is $p \to (q \to r)$.

The inverse of a conditional statement $A \to B$ is $\sim A \to \sim B$.

The converse of $C \to D$ is $D \to C$.

Thus, the converse of the inverse of $A \to B$ is $\sim B \to \sim A$, which is the contrapositive of the original statement.

For $p \to (q \to r)$, the converse of the inverse is:

$\sim (q \to r) \to \sim p$

We can simplify this using the equivalence $X \to Y \equiv \sim X \vee Y$:

$\sim (q \to r) \to \sim p \equiv (q \to r) \vee \sim p$

$\equiv (\sim q \vee r) \vee \sim p$

$\equiv \sim p \vee \sim q \vee r$

To find the dual of a logical expression, we replace $\vee$ with $\wedge$ and $\wedge$ with $\vee$ (while keeping the literals unchanged).

The dual of $(\sim p \vee \sim q \vee r)$ is $(\sim p \wedge \sim q \wedge r)$.

Now, we check the given options to find which one is equivalent to $\sim p \wedge \sim q \wedge r$.

Evaluating the first option:

$\sim [p \vee (r \to q)] \equiv \sim [p \vee (\sim r \vee q)]$

Using De Morgan's laws:

$\equiv \sim p \wedge \sim (\sim r \vee q)$

$\equiv \sim p \wedge (r \wedge \sim q)$

$\equiv \sim p \wedge \sim q \wedge r$

This matches the dual of the converse of the inverse.

Answer: $\sim [p \vee (r \to q)]$

</details>

---

### Q60. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The statements p, q and r have truth values True, False and False respectively. The truth values of a logical statement $[\sim(p \wedge \sim q) \vee (q \vee \sim r)]$ and its dual are, respectively.....

**Options:**

- **(A)** True, True
- **(B)** True, False
- **(C)** False, True
- **(D)** False, False

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) True, False**

**Detailed Solution:**

Given $p = T$, $q = F$, $r = F$.

The logical statement is $S = [\sim(p \wedge \sim q) \vee (q \vee \sim r)]$.

Substituting the truth values:
$p \wedge \sim q = T \wedge \sim F = T \wedge T = T$
$\sim(p \wedge \sim q) = \sim T = F$
$q \vee \sim r = F \vee \sim F = F \vee T = T$

Therefore, $S = F \vee T = T$.

The dual of the statement $S$ is obtained by replacing $\wedge$ with $\vee$ and $\vee$ with $\wedge$.

The dual statement is $S^* = [\sim(p \vee \sim q) \wedge (q \wedge \sim r)]$.

Substituting the truth values:
$p \vee \sim q = T \vee \sim F = T \vee T = T$
$\sim(p \vee \sim q) = \sim T = F$
$q \wedge \sim r = F \wedge \sim F = F \wedge T = F$

Therefore, $S^* = F \wedge F = F$.

The truth values of the statement and its dual are True and False respectively.

Answer: True, False

</details>

---

### Q61. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the truth value of the compound statement
$[(p \vee q) \wedge (q \rightarrow r) \wedge (\sim r)] \rightarrow (p \wedge q)$ is false, then the truth values of $p \rightarrow q$ and $q \rightarrow p$ are respectively...

**Options:**

- **(A)** $(F, T)$
- **(B)** $(T, F)$
- **(C)** $(T, T)$
- **(D)** $(F, F)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(F, T)$**

**Detailed Solution:**

Let $X = (p \vee q) \wedge (q \rightarrow r) \wedge (\sim r)$ and $Y = p \wedge q$.

The truth value of $X \rightarrow Y$ is given as False.

An implication $X \rightarrow Y$ is False if and only if $X$ is True and $Y$ is False.

For $X$ to be True, all its conjuncts must be True:
1) $\sim r$ is True $\Rightarrow r$ is False ($F$).
2) $q \rightarrow r$ is True. Since $r$ is False, $q$ must be False ($F$).
3) $p \vee q$ is True. Since $q$ is False, $p$ must be True ($T$).

Checking $Y$: $p \wedge q = T \wedge F = F$, which satisfies the condition that $Y$ is False.

Thus, the truth values are $p = T$, $q = F$, and $r = F$.

Now, evaluating the required statements:
$p \rightarrow q \equiv T \rightarrow F \equiv F$
$q \rightarrow p \equiv F \rightarrow T \equiv T$

The truth values of $p \rightarrow q$ and $q \rightarrow p$ are respectively $F$ and $T$.

Answer: $(F, T)$

</details>

---

### Q62. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statements is logically equivalent to $\sim(p \leftrightarrow q)$ ?

**Options:**

- **(A)** $\sim p \rightarrow q$
- **(B)** $\sim p \leftrightarrow \sim q$
- **(C)** $\sim(q \rightarrow \sim p)$
- **(D)** $p \leftrightarrow \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $p \leftrightarrow \sim q$**

**Detailed Solution:**

The logical equivalence of the biconditional statement is given by:

$p \leftrightarrow q \equiv (p \rightarrow q) \wedge (q \rightarrow p)$

Taking the negation of both sides:

$\sim(p \leftrightarrow q) \equiv \sim((p \rightarrow q) \wedge (q \rightarrow p))$

Using De Morgan's laws:

$\equiv \sim(p \rightarrow q) \vee \sim(q \rightarrow p)$

Since $p \rightarrow q \equiv \sim p \vee q$, we get:

$\equiv \sim(\sim p \vee q) \vee \sim(\sim q \vee p)$

Applying De Morgan's laws again:

$\equiv (p \wedge \sim q) \vee (q \wedge \sim p)$

Now, evaluating the expression $p \leftrightarrow \sim q$:

$p \leftrightarrow \sim q \equiv (p \rightarrow \sim q) \wedge (\sim q \rightarrow p)$

$\equiv (\sim p \vee \sim q) \wedge (q \vee p)$

Using the distributive law:

$\equiv (\sim p \wedge q) \vee (\sim p \wedge p) \vee (\sim q \wedge q) \vee (\sim q \wedge p)$

Since $\sim p \wedge p \equiv F$ and $\sim q \wedge q \equiv F$:

$\equiv (\sim p \wedge q) \vee (p \wedge \sim q)$

Comparing the two results, we conclude that $\sim(p \leftrightarrow q) \equiv p \leftrightarrow \sim q$.

Answer: $p \leftrightarrow \sim q$

</details>

---

### Q63. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the statement patterns
A. $(q \rightarrow p) \vee (p \rightarrow q)$
B. $(\sim p \vee \sim q) \leftrightarrow \sim (p \wedge q)$
C. $[(p \vee q) \wedge \sim p] \wedge \sim q$
D. $(p \wedge q) \wedge (\sim p \vee \sim q)$
then statement patterns

**Options:**

- **(A)** A and B are contradictions, C and D are tautologies.
- **(B)** A and B are tautologies, C and D are contradictions.
- **(C)** A, B, C, D all are tautologies.
- **(D)** A, B, C, D all are contradictions.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A and B are tautologies, C and D are contradictions.**

**Detailed Solution:**

For statement pattern A:
$(q \rightarrow p) \vee (p \rightarrow q) \equiv (\sim q \vee p) \vee (\sim p \vee q) \equiv (\sim q \vee q) \vee (\sim p \vee p) \equiv T \vee T \equiv T$
Thus, A is a tautology.

For statement pattern B:
By De Morgan's Law, $\sim (p \wedge q) \equiv \sim p \vee \sim q$.
The statement becomes $(\sim p \vee \sim q) \leftrightarrow (\sim p \vee \sim q)$, which is of the form $X \leftrightarrow X \equiv T$.
Thus, B is a tautology.

For statement pattern C:
$[(p \vee q) \wedge \sim p] \wedge \sim q \equiv [(p \wedge \sim p) \vee (q \wedge \sim p)] \wedge \sim q \equiv [F \vee (q \wedge \sim p)] \wedge \sim q \equiv (q \wedge \sim p) \wedge \sim q \equiv \sim p \wedge (q \wedge \sim q) \equiv \sim p \wedge F \equiv F$
Thus, C is a contradiction.

For statement pattern D:
$(p \wedge q) \wedge (\sim p \vee \sim q) \equiv (p \wedge q) \wedge \sim (p \wedge q)$, which is of the form $X \wedge \sim X \equiv F$.
Thus, D is a contradiction.

Therefore, A and B are tautologies, while C and D are contradictions.

Answer: A and B are tautologies, C and D are contradictions.

</details>

---

### Q64. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $(p \wedge q) \rightarrow (r \vee \sim s)$ is false. Then the truth values of $p, q, r$ and $s$ are respectively

**Options:**

- **(A)** T, F, T, T
- **(B)** T, T, F, T
- **(C)** T, T, T, F
- **(D)** T, T, F, F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) T, T, F, T**

**Detailed Solution:**

The given statement pattern is $(p \wedge q) \rightarrow (r \vee \sim s)$.

An implication $A \rightarrow B$ is false if and only if $A$ is true and $B$ is false.

Therefore, $(p \wedge q)$ is true and $(r \vee \sim s)$ is false.

For $(p \wedge q)$ to be true, both $p$ and $q$ must be true. Thus, $p = \text{T}$ and $q = \text{T}$.

For $(r \vee \sim s)$ to be false, both $r$ and $\sim s$ must be false. Thus, $r = \text{F}$ and $\sim s = \text{F}$.

Since $\sim s = \text{F}$, $s$ must be true, so $s = \text{T}$.

The truth values of $p, q, r$ and $s$ are T, T, F, T respectively.

Answer: T, T, F, T

</details>

---

### Q65. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A = \{1, 2, 3, 4, 5, 6\}$ then which of the following is not true?

**Options:**

- **(A)** $\exists x \in A$ such that $x + 3 = 9$.
- **(B)** $\exists x \in A$ such that $x + 2 < 9$.
- **(C)** $\forall x \in A, x + 6 \geq 10$.
- **(D)** $\exists x \in A$ such that $x + 6 < 10$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\forall x \in A, x + 6 \geq 10$.**

**Detailed Solution:**

Given $A = \{1, 2, 3, 4, 5, 6\}$.

Checking the first option: $\exists x \in A$ such that $x + 3 = 9 \Rightarrow x = 6$. Since $6 \in A$, this statement is true.

Checking the second option: $\exists x \in A$ such that $x + 2 < 9 \Rightarrow x < 7$. Since $1 \in A$ satisfies this, the statement is true.

Checking the third option: $\forall x \in A, x + 6 \geq 10 \Rightarrow x \geq 4$. This statement is false because for $x = 1, 2, 3 \in A$, the condition $x \geq 4$ is not satisfied.

Checking the fourth option: $\exists x \in A$ such that $x + 6 < 10 \Rightarrow x < 4$. Since $1, 2, 3 \in A$ satisfy this, the statement is true.

The statement which is not true is $\forall x \in A, x + 6 \geq 10$.

Answer: $\forall x \in A, x + 6 \geq 10$.

</details>

---

### Q66. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the following statements
$r$: If $p \rightarrow q$ is false then $p \vee q$ is false.
$s$: If $p \leftrightarrow q$ is false then $p \vee q$ is false.
The truth values of $r \rightarrow s$ and $s \rightarrow r$ are respectively ____

**Options:**

- **(A)** T, T
- **(B)** T, F
- **(C)** F, T
- **(D)** F, F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) T, T**

**Detailed Solution:**

Let us evaluate the truth value of statement $r$.
The premise is "$p \rightarrow q$ is false". The implication $p \rightarrow q$ is false only when $p$ is True (T) and $q$ is False (F).
For $p = \text{T}$ and $q = \text{F}$, the value of $p \vee q$ is $\text{T} \vee \text{F} = \text{T}$ (True).
However, statement $r$ claims that $p \vee q$ is false. Since the conclusion is false when the premise is true, statement $r$ is False (F).

Now, let us evaluate the truth value of statement $s$.
The premise is "$p \leftrightarrow q$ is false". The biconditional $p \leftrightarrow q$ is false when $p$ and $q$ have opposite truth values. This gives two cases:
Case 1: $p = \text{T}$ and $q = \text{F}$. Here, $p \vee q = \text{T} \vee \text{F} = \text{T}$.
Case 2: $p = \text{F}$ and $q = \text{T}$. Here, $p \vee q = \text{F} \vee \text{T} = \text{T}$.
In both cases, $p \vee q$ is True. Statement $s$ claims that $p \vee q$ is false, which is incorrect. Thus, statement $s$ is also False (F).

Since both statements $r$ and $s$ are False:
The truth value of $r \rightarrow s$ is $\text{F} \rightarrow \text{F}$, which is True (T).
The truth value of $s \rightarrow r$ is $\text{F} \rightarrow \text{F}$, which is True (T).

Therefore, the truth values of $r \rightarrow s$ and $s \rightarrow r$ are T and T respectively.

Answer: T, T

</details>

---

### Q67. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the truth value of the compound statement $[(p \vee q) \wedge (q \rightarrow r) \wedge (\sim r)] \rightarrow (p \wedge q)$ is False then the truth values of $p \rightarrow q$ and $q \rightarrow p$ are respectively......

**Options:**

- **(A)** $(T, T)$
- **(B)** $(T, F)$
- **(C)** $(F, T)$
- **(D)** $(F, F)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(F, T)$**

**Detailed Solution:**

The compound statement $X \rightarrow Y$ is False if and only if $X$ is True and $Y$ is False.

Here, $X = (p \vee q) \wedge (q \rightarrow r) \wedge (\sim r)$ and $Y = p \wedge q$.

Since $X$ is True, each of its components must be True:
1) $\sim r$ is True $\Rightarrow r$ is False.
2) $q \rightarrow r$ is True. Since $r$ is False, $q$ must be False.
3) $p \vee q$ is True. Since $q$ is False, $p$ must be True.

Checking $Y$: $p \wedge q = T \wedge F = F$, which satisfies the condition that $Y$ is False.

Thus, $p = T$ and $q = F$.

Now, we evaluate $p \rightarrow q$ and $q \rightarrow p$:
$p \rightarrow q = T \rightarrow F = F$
$q \rightarrow p = F \rightarrow T = T$

The truth values are $(F, T)$.

Answer: $(F, T)$

</details>

---

### Q68. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $(p \vee q) \rightarrow \sim r$ is logically equivalent to

**Options:**

- **(A)** $(\sim p \vee \sim q) \vee \sim r$
- **(B)** $(\sim p \wedge \sim q) \wedge \sim r$
- **(C)** $(\sim p \wedge \sim q) \vee \sim r$
- **(D)** $(\sim p \vee \sim q) \wedge \sim r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\sim p \wedge \sim q) \vee \sim r$**

**Detailed Solution:**

The given statement pattern is $(p \vee q) \rightarrow \sim r$.

Using the logical equivalence $A \rightarrow B \equiv \sim A \vee B$, the expression can be rewritten by taking $A = p \vee q$ and $B = \sim r$.

$(p \vee q) \rightarrow \sim r \equiv \sim(p \vee q) \vee \sim r$

Applying De Morgan's law, $\sim(p \vee q) \equiv \sim p \wedge \sim q$.

Substituting this into the expression yields:

$(\sim p \wedge \sim q) \vee \sim r$

Answer: $(\sim p \wedge \sim q) \vee \sim r$

</details>

---

### Q69. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If p : switch $\mathrm{s}_1$ is closed, q : switch $\mathrm{s}_2$ is closed then correct interpretation from the following circuit is

<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/em7kPaHh5PMfFc29E30_DKmk9NS4AH1tmOJlg94-J_s.original.fullsize.png">

**Options:**

- **(A)** The lamp is always on
- **(B)** The lamp is always off
- **(C)** Symbolic form is $\mathrm{p} \vee(\sim \mathrm{p} \wedge \sim \mathrm{q}) \vee \mathrm{q}$
- **(D)** is equivalent to $\mathrm{p} \vee \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The lamp is always off**

**Detailed Solution:**

Let $p$ be the statement "switch $\mathrm{S}_1$ is closed" and $q$ be the statement "switch $\mathrm{S}_2$ is closed".
Then, $\sim p$ represents "switch $\mathrm{S}_1'$ is closed" and $\sim q$ represents "switch $\mathrm{S}_2'$ is closed".

From the given circuit diagram, we can observe that:
1. Switch $\mathrm{S}_1$ is in series with the rest of the circuit.
2. Switches $\mathrm{S}_1'$ and $\mathrm{S}_2'$ are in parallel with each other.
3. Switch $\mathrm{S}_2$ is in series with the preceding combination.

The symbolic form of the given switching circuit is:
$p \wedge (\sim p \vee \sim q) \wedge q$

Now, let's simplify this logical expression:
$p \wedge (\sim p \vee \sim q) \wedge q$
By commutative and associative laws, we can rearrange the terms:
$\equiv (p \wedge q) \wedge (\sim p \vee \sim q)$

Using De Morgan's Law, we know that $(\sim p \vee \sim q) \equiv \sim(p \wedge q)$. Substituting this into the expression:
$\equiv (p \wedge q) \wedge \sim(p \wedge q)$

This is of the form $r \wedge \sim r$, which is a contradiction and is always False ($\mathrm{F}$).
$\equiv \mathrm{F}$

Since the logical expression is always False, the circuit is always open regardless of the states of the switches. Therefore, current will never flow through the circuit, and the lamp is always off.

Answer: The lamp is always off

</details>

---

### Q70. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The negation of statement pattern $(p \wedge \sim q) \rightarrow(p \vee \sim q)$ is

**Options:**

- **(A)** a tautology
- **(B)** a contingency
- **(C)** a contradiction
- **(D)** equivalent to $\mathrm{p} \vee \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) a contradiction**

**Detailed Solution:**

Let the given statement pattern be $S \equiv (p \wedge \sim q) \rightarrow (p \vee \sim q)$.

The negation of an implication $A \rightarrow B$ is $A \wedge \sim B$.

$\sim S \equiv (p \wedge \sim q) \wedge \sim(p \vee \sim q)$

Using De Morgan's law, $\sim(p \vee \sim q) \equiv \sim p \wedge q$.

$\sim S \equiv (p \wedge \sim q) \wedge (\sim p \wedge q)$

Using commutative and associative laws:

$\sim S \equiv (p \wedge \sim p) \wedge (q \wedge \sim q)$

Since $p \wedge \sim p \equiv F$ and $q \wedge \sim q \equiv F$:

$\sim S \equiv F \wedge F \equiv F$

Thus, the negation of the given statement pattern is a contradiction.

Answer: a contradiction

</details>

---

### Q71. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An alternative equivalent circuit for the circuit <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/PC8MIZozvEmHEsUhESX-7WB0XEBD1PvXIms9SQuK2jU.original.fullsize.png">
 is

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/W9xERPITNm5qidk5s6gToYIgBEBdc0w0oaEJfzyc9TU.original.fullsize.png">
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/z4c75GbmHXaon_NWToda8O4xTS8Gg954UjfDGou0Y7A.original.fullsize.png">
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/1PJ0qDnvp2ncdWpL2WmbYfc1Mvd-RYKM7z386jU-scM.original.fullsize.png">
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/5JaEmD3E_nb3jgMTEJ0RdcQom_0yMl7AdCO2dpamXJw.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/W9xERPITNm5qidk5s6gToYIgBEBdc0w0oaEJfzyc9TU.original.fullsize.png">**

**Detailed Solution:**

Let $p, q, r$ represent the switches $S_1, S_2, S_3$ respectively.

The given circuit consists of two parallel branches:
The upper branch has switches $S_1$ and $S_2$ in series, which is represented by $p \land q$.
The lower branch has switches $S_1$ and $S_3$ in series, which is represented by $p \land r$.

Since these two branches are connected in parallel, the symbolic form of the given circuit is:
$(p \land q) \lor (p \land r)$

By using the distributive law of logic, we can simplify this expression:
$(p \land q) \lor (p \land r) \equiv p \land (q \lor r)$

This simplified logical expression represents a circuit where switch $S_1$ (corresponding to $p$) is connected in series with a parallel combination of switches $S_2$ and $S_3$ (corresponding to $q \lor r$).

Looking at the given options, this arrangement exactly matches the circuit shown in the second option.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/W9xERPITNm5qidk5s6gToYIgBEBdc0w0oaEJfzyc9TU.original.fullsize.png">

</details>

---

### Q72. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the following statements
$p: 2$ is an even prime number
q : If $\mathrm{z}_1=2-i, \mathrm{z}_2=-2+i \quad$ where $i=\sqrt{-1}$, then $\operatorname{Im}\left[\frac{1}{z_1 \stackrel{}{\bar{z}_2}}\right]=-\frac{1}{5}$
$r: \tan \left(-945^{\circ}\right)=-1$
then which of the following has truth value True.

**Options:**

- **(A)** $(p \rightarrow q) \leftrightarrow(q \wedge r)$
- **(B)** $\mathrm{q} \leftrightarrow \mathrm{r}$
- **(C)** $p \rightarrow q$
- **(D)** $(\mathrm{p} \rightarrow \mathrm{r}) \leftrightarrow \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(p \rightarrow q) \leftrightarrow(q \wedge r)$**

**Detailed Solution:**

Statement $p$: $2$ is an even prime number. This is True, so $p \equiv T$.

Statement $q$: Given $z_1 = 2 - i$ and $z_2 = -2 + i$, we have $\bar{z}_2 = -2 - i$.
$z_1 \bar{z}_2 = (2 - i)(-2 - i) = -(2 - i)(2 + i) = -(4 - i^2) = -5$.
$\dfrac{1}{z_1 \bar{z}_2} = -\dfrac{1}{5} + 0i$.
$\operatorname{Im}\left[\dfrac{1}{z_1 \bar{z}_2}\right] = 0 \neq -\dfrac{1}{5}$. This is False, so $q \equiv F$.

Statement $r$: $\tan(-945^{\circ}) = -\tan(945^{\circ}) = -\tan(2 \times 360^{\circ} + 225^{\circ}) = -\tan(225^{\circ}) = -\tan(180^{\circ} + 45^{\circ}) = -\tan(45^{\circ}) = -1$. This is True, so $r \equiv T$.

Evaluating the given options:
For $(p \rightarrow q) \leftrightarrow (q \wedge r)$:
$p \rightarrow q \equiv T \rightarrow F \equiv F$
$q \wedge r \equiv F \wedge T \equiv F$
$F \leftrightarrow F \equiv T$.

For $q \leftrightarrow r$:
$F \leftrightarrow T \equiv F$.

For $p \rightarrow q$:
$T \rightarrow F \equiv F$.

For $(p \rightarrow r) \leftrightarrow q$:
$p \rightarrow r \equiv T \rightarrow T \equiv T$
$T \leftrightarrow F \equiv F$.

The only expression with a truth value of True is $(p \rightarrow q) \leftrightarrow (q \wedge r)$.

Answer: $(p \rightarrow q) \leftrightarrow(q \wedge r)$

</details>

---

### Q73. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If p, q, r, s are statements, where, $p: A^2-B^2=(A-B)(A+B) ; A, B$ are matrices, $A B \neq B A$
q: $5 \leqslant 5$
r: ${ }^8 \mathrm{C}_1+{ }^8 \mathrm{C}_2+{ }^8 \mathrm{C}_3+\ldots \ldots \ldots . .+{ }^8 \mathrm{C}_8=256$
s: Maximum value of ${ }^8 \mathrm{C}_{\mathrm{r}}$ is 70 then the statement from the following having truth value true is ....

**Options:**

- **(A)** $(\mathrm{p} \wedge \sim \mathrm{r}) \vee(\sim \mathrm{q} \wedge \sim \mathrm{s})$
- **(B)** $(\mathrm{p} \vee \sim q) \leftrightarrow(\sim \mathrm{r} \rightarrow \mathrm{s})$
- **(C)** $(\mathrm{p} \leftrightarrow \mathrm{q}) \wedge(\sim \mathrm{p} \vee \sim \mathrm{q})$
- **(D)** $(\mathrm{s} \vee \sim \mathrm{p}) \leftrightarrow(\sim \mathrm{p} \wedge \sim \mathrm{r})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\mathrm{s} \vee \sim \mathrm{p}) \leftrightarrow(\sim \mathrm{p} \wedge \sim \mathrm{r})$**

**Detailed Solution:**

Statement p: For matrices $A$ and $B$, $(A-B)(A+B) = A^2 + AB - BA - B^2$. Since $AB \neq BA$, $A^2 + AB - BA - B^2 \neq A^2 - B^2$. Thus, the truth value of p is F.

Statement q: $5 \leqslant 5$ is a true statement. Thus, the truth value of q is T.

Statement r: We know that $\sum_{i=0}^{n} {}^{n}C_{i} = 2^n$. Therefore, ${}^{8}C_{1} + {}^{8}C_{2} + \dots + {}^{8}C_{8} = 2^8 - {}^{8}C_{0} = 256 - 1 = 255$. The statement claims it is $256$, so the truth value of r is F.

Statement s: The maximum value of ${}^{n}C_{r}$ for an even $n$ occurs at $r = \dfrac{n}{2}$. For $n=8$, the maximum is ${}^{8}C_{4} = \dfrac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2 \times 1} = 70$. Thus, the truth value of s is T.

Now, substituting the truth values (p = F, q = T, r = F, s = T) into the given options:

First option: $(\mathrm{p} \wedge \sim \mathrm{r}) \vee (\sim \mathrm{q} \wedge \sim \mathrm{s}) \equiv (\text{F} \wedge \text{T}) \vee (\text{F} \wedge \text{F}) \equiv \text{F} \vee \text{F} \equiv \text{F}$

Second option: $(\mathrm{p} \vee \sim \mathrm{q}) \leftrightarrow (\sim \mathrm{r} \rightarrow \mathrm{s}) \equiv (\text{F} \vee \text{F}) \leftrightarrow (\text{T} \rightarrow \text{T}) \equiv \text{F} \leftrightarrow \text{T} \equiv \text{F}$

Third option: $(\mathrm{p} \leftrightarrow \mathrm{q}) \wedge (\sim \mathrm{p} \vee \sim \mathrm{q}) \equiv (\text{F} \leftrightarrow \text{T}) \wedge (\text{T} \vee \text{F}) \equiv \text{F} \wedge \text{T} \equiv \text{F}$

Fourth option: $(\mathrm{s} \vee \sim \mathrm{p}) \leftrightarrow (\sim \mathrm{p} \wedge \sim \mathrm{r}) \equiv (\text{T} \vee \text{T}) \leftrightarrow (\text{T} \wedge \text{T}) \equiv \text{T} \leftrightarrow \text{T} \equiv \text{T}$

Only the fourth statement has a truth value of True.

Answer: $(\mathrm{s} \vee \sim \mathrm{p}) \leftrightarrow(\sim \mathrm{p} \wedge \sim \mathrm{r})$

</details>

---

### Q74. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statement is a tautology?

**Options:**

- **(A)** $(\sim q \wedge p) \wedge(p \wedge \sim p)$
- **(B)** $(\mathrm{p} \wedge \mathrm{q}) \wedge(\sim \mathrm{p} \wedge \mathrm{q})$
- **(C)** $[(\sim q) \wedge p] \wedge q$
- **(D)** $(\sim q \wedge p) \vee(p \vee \sim p)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim q \wedge p) \vee(p \vee \sim p)$**

**Detailed Solution:**

Let us evaluate each option by using the laws of logic.

For the first option:
$(\sim q \wedge p) \wedge (p \wedge \sim p)$
Since $p \wedge \sim p \equiv F$ (contradiction), we have:
$(\sim q \wedge p) \wedge F \equiv F$

For the second option:
$(p \wedge q) \wedge (\sim p \wedge q)$
Using associative and commutative laws:
$(p \wedge \sim p) \wedge (q \wedge q) \equiv F \wedge q \equiv F$

For the third option:
$[(\sim q) \wedge p] \wedge q$
Using associative and commutative laws:
$(\sim q \wedge q) \wedge p \equiv F \wedge p \equiv F$

For the fourth option:
$(\sim q \wedge p) \vee (p \vee \sim p)$
Since $p \vee \sim p \equiv T$ (tautology), we have:
$(\sim q \wedge p) \vee T \equiv T$

Since the truth value of the fourth statement is always True, it is a tautology.

Answer: $(\sim q \wedge p) \vee(p \vee \sim p)$

</details>

---

### Q75. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider statements $\mathrm{p}: \mathrm{S}_1$ is closed; $\mathrm{q}: \mathrm{S}_2$ is closed; $\mathrm{r}: \mathrm{S}_3$ is closed. The simplified equivalent circuit diagram and its logical statement for the switching circuit is respectively.

<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/yhGUtCjbl_d3kCeHoZUCScJ2UN4ohh2nVKUf2l57Qfw.original.fullsize.png">

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/KYrlNGIgSZ7k3d_qKbok1Z-8ANuzazZXzRpC9kQ9Feo.original.fullsize.png">
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/H_K6PzzS7Uynn8yybX_mlaDN8kV7wTE2rvBIKcEsb5w.original.fullsize.png">
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/PjU634ZMeqC2fZZzMA67-Z0EcYqJ7Q2ixupA2CWcNoQ.original.fullsize.png">
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/OpVZENWMrJO52rHoGr_10TLsJODEraSdg08Xeoj4KGE.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/PjU634ZMeqC2fZZzMA67-Z0EcYqJ7Q2ixupA2CWcNoQ.original.fullsize.png">**

**Detailed Solution:**

Let $p$, $q$, and $r$ represent the statements that switches $S_1$, $S_2$, and $S_3$ are closed, respectively. Then $\sim p$ and $\sim q$ represent that switches $S_1'$ and $S_2'$ are closed.

The given circuit consists of three parts connected in series. We can write the logical expression for each part:

Part 1: Three parallel branches containing $(S_1' \text{ and } S_2')$, $S_1$, and $S_2$.
Logical expression: $(\sim p \wedge \sim q) \vee p \vee q$
Using De Morgan's law, this becomes $\sim(p \vee q) \vee (p \vee q)$, which is of the form $\sim X \vee X \equiv T$ (a tautology, meaning it is always closed).

Part 2: Switch $S_3$ in series.
Logical expression: $r$

Part 3: Two parallel branches containing $(S_1 \text{ and } S_2)$ and $(S_1' \text{ and } S_2)$.
Logical expression: $(p \wedge q) \vee (\sim p \wedge q)$
Using the distributive law, this becomes $(p \vee \sim p) \wedge q \equiv T \wedge q \equiv q$.

The complete logical expression for the circuit is the series combination (conjunction) of these three parts:
$T \wedge r \wedge q \equiv q \wedge r$

The simplified logical statement is $q \wedge r$, which corresponds to a circuit with switches $S_2$ and $S_3$ connected in series.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/PjU634ZMeqC2fZZzMA67-Z0EcYqJ7Q2ixupA2CWcNoQ.original.fullsize.png">

</details>

---

### Q76. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the truth value of the expression $[(p \vee q) \wedge(q \rightarrow r) \wedge(\sim r)] \rightarrow(p \wedge q)$ is False then truth values of $p, q, r$ are respectively.

**Options:**

- **(A)** T, T, T
- **(B)** T, F, F
- **(C)** F, F, F
- **(D)** F, T, T

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) T, F, F**

**Detailed Solution:**

Let the given statement be $A \rightarrow B$, where $A = (p \vee q) \wedge (q \rightarrow r) \wedge (\sim r)$ and $B = p \wedge q$.

For an implication $A \rightarrow B$ to be False, the antecedent $A$ must be True and the consequent $B$ must be False.

Therefore, $(p \vee q) \wedge (q \rightarrow r) \wedge (\sim r)$ is True and $p \wedge q$ is False.

For the conjunction $(p \vee q) \wedge (q \rightarrow r) \wedge (\sim r)$ to be True, each of its components must be True.

$\sim r$ is True $\Rightarrow r$ is False (F).

$q \rightarrow r$ is True. Since $r$ is False, $q$ must be False (F) because True $\rightarrow$ False is False.

$p \vee q$ is True. Since $q$ is False, $p$ must be True (T).

Checking the consequent $B$: $p \wedge q = \text{T} \wedge \text{F} = \text{F}$, which satisfies the condition that $B$ is False.

Thus, the truth values of $p, q, r$ are T, F, F respectively.

Answer: T, F, F

</details>

---

### Q77. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{p} \equiv$ The switch $\mathrm{S}_1$ is closed, $\mathrm{q} \equiv$ The switch $\mathrm{S}_2$ is closed, $\mathrm{r} \equiv$ switch $S_3$ is closed, then symbolic form of following switching circuit is equivalent to
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/EYH48F9ZS4dPeT789Ai9UNAa7HkINcMDX7WkGXp2iA0.original.fullsize.png">

**Options:**

- **(A)** p
- **(B)** q
- **(C)** $\mathrm{p} \wedge \mathrm{q}$
- **(D)** $\mathrm{p} \vee \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) p**

**Detailed Solution:**

Let $p$, $q$, and $r$ represent the switches $S_1$, $S_2$, and $S_3$ respectively.

The switches $S_2'$ and $S_3'$ represent $\sim q$ and $\sim r$ respectively.

In the given circuit, the top branch consists of switch $S_1$ in series with a parallel combination of $S_2$ and $S_3$. Its symbolic form is $p \wedge (q \vee r)$.

The bottom branch consists of switches $S_3'$, $S_2'$, and $S_1$ in series. Its symbolic form is $\sim r \wedge \sim q \wedge p$.

Since the top and bottom branches are connected in parallel, the symbolic form of the entire circuit is given by the disjunction of the two branches:

$[p \wedge (q \vee r)] \vee [\sim r \wedge \sim q \wedge p]$

Using the commutative law, we can rewrite the second term:

$[p \wedge (q \vee r)] \vee [p \wedge (\sim q \wedge \sim r)]$

Applying De Morgan's law to the second term ($\sim q \wedge \sim r \equiv \sim(q \vee r)$):

$[p \wedge (q \vee r)] \vee [p \wedge \sim(q \vee r)]$

Using the distributive law, we can factor out $p$:

$p \wedge [(q \vee r) \vee \sim(q \vee r)]$

By the complement law, any statement disjoined with its negation is a tautology (True, denoted as $T$), so $(q \vee r) \vee \sim(q \vee r) \equiv T$:

$p \wedge T$

By the identity law, $p \wedge T \equiv p$.

Thus, the given switching circuit is equivalent to $p$.

Answer: p

</details>

---

### Q78. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the following three statements
(A) If $3+2=7$ then $4+3=8$.
(B) If $5+2=7$ then earth is flat.
(C) If both (A) and (B) are true then $5+6=11$.
Which of the following statements is correct?

**Options:**

- **(A)** (A) and (C) are true while (B) is false.
- **(B)** (A) is true while (B) and (C) are false.
- **(C)** (A) is false but (B) and (C) are true.
- **(D)** (A) is false while (C) is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (A) and (C) are true while (B) is false.**

**Detailed Solution:**

Statement (A) is of the form $p \rightarrow q$, where $p$ is "$3+2=7$" (False) and $q$ is "$4+3=8$" (False). Since $F \rightarrow F$ is True, statement (A) is True.

Statement (B) is of the form $p \rightarrow q$, where $p$ is "$5+2=7$" (True) and $q$ is "earth is flat" (False). Since $T \rightarrow F$ is False, statement (B) is False.

Statement (C) is of the form $p \rightarrow q$, where $p$ is "both (A) and (B) are true". Since (A) is True and (B) is False, $p$ is False. The statement $q$ is "$5+6=11$" (True). Since $F \rightarrow T$ is True, statement (C) is True.

Thus, (A) and (C) are true while (B) is false.

Answer: (A) and (C) are true while (B) is false.

</details>

---

### Q79. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The negation of the statement "The triangle is an equilateral or isosceles triangle and the triangle is not isosceles and it is right angled" is

**Options:**

- **(A)** The triangle is not an equilateral or not an isosceles triangle or it is not an isosceles or it is not right angled
- **(B)** The triangle is not an equilateral triangle or not isosceles triangle and it is isosceles or it is not right angled
- **(C)** If the triangle is an equilateral triangle or an isosceles triangle then it is an isosceles triangle or not right angled
- **(D)** If the triangle is an equilateral triangle or an isosceles triangle then it is not isosceles triangle and it is not right angled

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) If the triangle is an equilateral triangle or an isosceles triangle then it is an isosceles triangle or not right angled**

**Detailed Solution:**

Let the simple statements be:
$p$: The triangle is an equilateral triangle.
$q$: The triangle is an isosceles triangle.
$r$: The triangle is right angled.

The given statement in symbolic form is:
$(p \lor q) \land (\sim q \land r)$

The negation of the statement is:
$\sim [ (p \lor q) \land (\sim q \land r) ]$

Using De Morgan's law $\sim (A \land B) \equiv \sim A \lor \sim B$, we get:
$\sim (p \lor q) \lor \sim (\sim q \land r)$

Using De Morgan's law again on the second bracket, $\sim (\sim q \land r) \equiv q \lor \sim r$, we get:
$\sim (p \lor q) \lor (q \lor \sim r)$

Using the conditional equivalence $\sim A \lor B \equiv A \rightarrow B$, this can be rewritten as:
$(p \lor q) \rightarrow (q \lor \sim r)$

Translating this back into words, we get:
"If the triangle is an equilateral triangle or an isosceles triangle then it is an isosceles triangle or not right angled."

Answer: If the triangle is an equilateral triangle or an isosceles triangle then it is an isosceles triangle or not right angled

</details>

---

### Q80. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the statements $\mathrm{p}, \mathrm{q}$ and r are true, false and true statements respectively, then the truth value of the statement pattern $[\sim q \wedge(p \vee \sim q) \wedge \sim r] \vee p$ and the truth value of its dual statement respectively are

**Options:**

- **(A)** T, T
- **(B)** F, T
- **(C)** T, F
- **(D)** F, F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) T, T**

**Detailed Solution:**

Given the truth values: $p \equiv T$, $q \equiv F$, and $r \equiv T$.

The given statement pattern is:
$[\sim q \wedge (p \vee \sim q) \wedge \sim r] \vee p$

Substituting the truth values into the pattern:
$\sim q \equiv \sim F \equiv T$
$p \vee \sim q \equiv T \vee T \equiv T$
$\sim r \equiv \sim T \equiv F$

The expression inside the square bracket evaluates to:
$T \wedge T \wedge F \equiv F$

The entire statement pattern evaluates to:
$F \vee p \equiv F \vee T \equiv T$

The dual of a statement pattern is obtained by replacing $\wedge$ with $\vee$ and $\vee$ with $\wedge$. The dual of the given statement pattern is:
$[\sim q \vee (p \wedge \sim q) \vee \sim r] \wedge p$

Substituting the truth values into the dual pattern:
$\sim q \equiv T$
$p \wedge \sim q \equiv T \wedge T \equiv T$
$\sim r \equiv F$

The expression inside the square bracket evaluates to:
$T \vee T \vee F \equiv T$

The entire dual statement pattern evaluates to:
$T \wedge p \equiv T \wedge T \equiv T$

Therefore, the truth values of the statement pattern and its dual are T and T respectively.

Answer: T, T

</details>

---

### Q81. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Number of switches in alternative equivalent simple circuit for the circuit is (are)
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/zAUZ80cUPe-1e38PVDjmzdalaFif6_aLGo79wrFl6OY.original.fullsize.png">

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Let $p, q, r$ represent the statements that switches $S_1, S_2, S_3$ are closed, respectively. Then $S_1 \equiv p$, $S_2 \equiv q$, $S_3 \equiv r$, $S_2' \equiv \sim q$, and $S_3' \equiv \sim r$.

From the given circuit diagram:
The top branch has switch $S_1$ in series with a parallel combination of $S_2'$ and $S_3'$. Its logical expression is $p \land (\sim q \lor \sim r)$.
The bottom branch has switches $S_2, S_3$, and $S_1$ in series. Its logical expression is $q \land r \land p$.

Since the top and bottom branches are connected in parallel, the logical expression for the entire circuit is:
$L = [p \land (\sim q \lor \sim r)] \lor (q \land r \land p)$

Now, we simplify this logical expression:
$L = [p \land (\sim q \lor \sim r)] \lor [p \land (q \land r)]$ (Commutative law)
$L = p \land [(\sim q \lor \sim r) \lor (q \land r)]$ (Distributive law)

Using De Morgan's Law, $\sim q \lor \sim r = \sim(q \land r)$:
$L = p \land [\sim(q \land r) \lor (q \land r)]$

Using the Complement Law, $\sim A \lor A = T$ (where $T$ is a tautology or a closed circuit):
$L = p \land T$

Using the Identity Law, $p \land T = p$:
$L = p$

The simplified expression is $p$, which represents a single switch $S_1$.
Therefore, the alternative equivalent simple circuit contains only $1$ switch.

Answer: 1

</details>

---

### Q82. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the statements given by following
(A) If $4+3=8$, then $5+3=9$
(B) If $6+4=10$, then moon is flat
(C) If both (A) and (B) are true, then $5+6=17$
Then which of the following statement is correct?

**Options:**

- **(A)** (A) is true while (B) and (C) are false
- **(B)** (A) and (B) are false, while (c) is true
- **(C)** (A) and (C) are true, while (B) is false
- **(D)** (A) is false, but (B) and (C) are true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (A) and (C) are true, while (B) is false**

**Detailed Solution:**

Let us evaluate the truth value of each statement.

Statement (A): If $4+3=8$, then $5+3=9$.
The hypothesis $4+3=8$ is False (F) and the conclusion $5+3=9$ is False (F).
For a conditional statement $p \rightarrow q$, if $p$ is F and $q$ is F, the statement is True (T).
Thus, (A) is True.

Statement (B): If $6+4=10$, then moon is flat.
The hypothesis $6+4=10$ is True (T) and the conclusion "moon is flat" is False (F).
For a conditional statement $p \rightarrow q$, if $p$ is T and $q$ is F, the statement is False (F).
Thus, (B) is False.

Statement (C): If both (A) and (B) are true, then $5+6=17$.
The hypothesis "both (A) and (B) are true" is False (F) because (B) is False.
The conclusion $5+6=17$ is False (F).
Since the hypothesis is F and the conclusion is F, the conditional statement is True (T).
Thus, (C) is True.

Therefore, (A) and (C) are true, while (B) is false.

Answer: (A) and (C) are true, while (B) is false

</details>

---

### Q83. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The contrapositive of the statement $\sim p \vee(q \wedge \sim r)$ is

**Options:**

- **(A)** $\mathrm{p} \rightarrow \mathrm{q} \wedge \mathrm{r}$
- **(B)** $(q \wedge r) \rightarrow p$
- **(C)** $\sim \mathrm{q} \vee \sim \mathrm{r} \rightarrow \mathrm{p}$
- **(D)** $(\mathrm{r} \vee \sim \mathrm{q}) \rightarrow \sim \mathrm{p}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\mathrm{r} \vee \sim \mathrm{q}) \rightarrow \sim \mathrm{p}$**

**Detailed Solution:**

The given statement is $\sim p \vee (q \wedge \sim r)$.

Using the logical equivalence $A \rightarrow B \equiv \sim A \vee B$, the statement can be written as an implication:

$p \rightarrow (q \wedge \sim r)$

The contrapositive of an implication $A \rightarrow B$ is $\sim B \rightarrow \sim A$.

Therefore, the contrapositive of $p \rightarrow (q \wedge \sim r)$ is:

$\sim (q \wedge \sim r) \rightarrow \sim p$

Using De Morgan's law, $\sim (q \wedge \sim r) \equiv \sim q \vee \sim(\sim r) \equiv \sim q \vee r \equiv r \vee \sim q$.

Thus, the contrapositive is $(r \vee \sim q) \rightarrow \sim p$.

Answer: $(\mathrm{r} \vee \sim \mathrm{q}) \rightarrow \sim \mathrm{p}$

</details>

---

### Q84. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following is the negation of the statement " For all $\mathrm{M}>0$, there exist $x \in s$ such that $x \geqslant \mathrm{M}$ "

**Options:**

- **(A)** $\exists \mathrm{M}>0$ such that $x \geqslant \mathrm{M}$ for all $x \in \mathrm{~s}$
- **(B)** $\exists \mathrm{M}>0, \exists x \in \mathrm{~s}$ such that $x \geqslant \mathrm{M}$
- **(C)** $\exists \mathrm{M}>0$ such that $x < \mathrm{M}$ for all $x \in \mathrm{~s}$
- **(D)** $\exists \mathrm{M}>0$, there exist $x \in \mathrm{~s}$ such that $x < \mathrm{M}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\exists \mathrm{M}>0$ such that $x < \mathrm{M}$ for all $x \in \mathrm{~s}$**

**Detailed Solution:**

The given statement can be written in logical notation as:

$\forall \mathrm{M} > 0, \exists x \in s$ such that $x \geqslant \mathrm{M}$

To find the negation of a quantified statement, we change the universal quantifier "for all" ($\forall$) to the existential quantifier "there exists" ($\exists$), and vice versa. We also negate the condition.

The negation of $\forall \mathrm{M} > 0$ is $\exists \mathrm{M} > 0$.

The negation of $\exists x \in s$ is $\forall x \in s$ (or "for all $x \in s$").

The negation of the condition $x \geqslant \mathrm{M}$ is $x < \mathrm{M}$.

Combining these, the negation of the entire statement is:

$\exists \mathrm{M} > 0$ such that $x < \mathrm{M}$ for all $x \in s$

Answer: $\exists \mathrm{M}>0$ such that $x < \mathrm{M}$ for all $x \in \mathrm{~s}$

</details>

---

### Q85. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If p : switch $\mathrm{S}_1$ is closed, q : switch $\mathrm{S}_2$ is closed, r : switch $\mathrm{S}_3$ closed, then the symbolic form of the following switching circuit is equivalent to Switching Circuit :
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/NLIh2ycMp07N-An8G2BXAT-0LRqRhqBxigJ0uXWDroM.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{p} \wedge(\mathrm{q} \vee \mathrm{r})$
- **(B)** $q \vee r$
- **(C)** p
- **(D)** $(\sim \mathrm{q} \wedge \sim \mathrm{r})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{p} \wedge(\mathrm{q} \vee \mathrm{r})$**

**Detailed Solution:**

Let $p, q, r$ represent the switches $S_1, S_2, S_3$ respectively.

The given circuit consists of two main branches connected in parallel.

The upper branch has switch $S_1$ in series with a parallel combination of $S_2$ and $S_3$. Its symbolic form is $p \wedge (q \vee r)$.

The lower branch has switches $S_3, S_2$, and $S_1$ connected in series. Its symbolic form is $r \wedge q \wedge p$, which can be written as $p \wedge (q \wedge r)$.

Since the two branches are in parallel, the total symbolic form of the circuit is the disjunction of the two branches:

$[p \wedge (q \vee r)] \vee [p \wedge (q \wedge r)]$

Using the distributive law, we can factor out $p$:

$= p \wedge [(q \vee r) \vee (q \wedge r)]$

Since $(q \wedge r)$ implies $(q \vee r)$, their disjunction is simply $(q \vee r)$. Thus, $(q \vee r) \vee (q \wedge r) = q \vee r$.

Therefore, the simplified symbolic form is:

$= p \wedge (q \vee r)$

Answer: $\mathrm{p} \wedge(\mathrm{q} \vee \mathrm{r})$

</details>

---

### Q86. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

p : If 7 is an odd number then 7 is divisible by 2
q : If 7 is prime number then 7 is an odd number
If $V_1$ and $V_2$ are respective truth values of contrapositive of $p$ and $q$ then $\left(V_1, V_2\right) \equiv$

**Options:**

- **(A)** $(\mathrm{T}, \mathrm{T})$
- **(B)** $(\mathrm{T}, \mathrm{F})$
- **(C)** $(\mathrm{F}, \mathrm{T})$
- **(D)** $(F, F)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\mathrm{F}, \mathrm{T})$**

**Detailed Solution:**

Let $r$ be the statement "7 is an odd number" and $s$ be the statement "7 is divisible by 2".
The truth value of $r$ is T and the truth value of $s$ is F.
Statement $p$ is $r \rightarrow s$, which is $T \rightarrow F \equiv F$.
Since the contrapositive of a conditional statement is logically equivalent to the original statement, the truth value of the contrapositive of $p$ is $V_1 = F$.

Let $u$ be the statement "7 is a prime number" and $v$ be the statement "7 is an odd number".
The truth value of $u$ is T and the truth value of $v$ is T.
Statement $q$ is $u \rightarrow v$, which is $T \rightarrow T \equiv T$.
Similarly, the truth value of the contrapositive of $q$ is $V_2 = T$.

Therefore, $(V_1, V_2) \equiv (F, T)$.

Answer: $(\mathrm{F}, \mathrm{T})$

</details>

---

### Q87. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following statements has the truth value T ?
A: cube roots of unity are in Geometric progression and their sum is 1
B: $4+7>10$ iff $2+8 < 10$
C: $\exists x \in \mathbb{N}$ such that $x^2-3 x+2=0$ and $\exists \mathrm{n} \in \mathbb{N}$ such that n is an odd number
D : $3+\mathrm{i}$ is a complex number or $\sqrt{2}+\sqrt{3}=\sqrt{5}$

**Options:**

- **(A)** only A
- **(B)** B, C & D
- **(C)** both A and C
- **(D)** both C and D

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) both C and D**

**Detailed Solution:**

Let us evaluate the truth value of each statement:

Statement A: The cube roots of unity are $1, \omega, \omega^2$. Their sum is $1 + \omega + \omega^2 = 0$. Since the statement claims their sum is $1$, it is False (F).

Statement B: $4+7 > 10$ is True (T) and $2+8 < 10$ is False (F). The biconditional statement (iff) between a True and a False statement is False. Hence, statement B is False (F).

Statement C: The equation $x^2-3x+2=0$ gives $x=1$ and $x=2$, both of which are natural numbers. Thus, $\exists x \in \mathbb{N}$ such that $x^2-3x+2=0$ is True (T). Also, there exist odd natural numbers (e.g., $n=1$), so $\exists n \in \mathbb{N}$ such that $n$ is an odd number is True (T). The conjunction (and) of two True statements is True. Hence, statement C is True (T).

Statement D: $3+\mathrm{i}$ is a complex number, which is True (T). $\sqrt{2}+\sqrt{3}=\sqrt{5}$ is False (F). The disjunction (or) of a True and a False statement is True. Hence, statement D is True (T).

Therefore, both statements C and D have the truth value T.

Answer: both C and D

</details>

---

### Q88. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the truth value of the statement pattern $[\mathrm{p} \wedge \sim \mathrm{r}] \rightarrow \sim \mathrm{r} \wedge \mathrm{q}$ is False, then which of the following has truth value False?

**Options:**

- **(A)** $(p \vee r) \rightarrow \sim r$
- **(B)** $(r \vee q) \rightarrow \sim p$
- **(C)** $\sim(p \vee q) \rightarrow \sim r$
- **(D)** $\sim(r \vee q) \rightarrow \sim p$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sim(r \vee q) \rightarrow \sim p$**

**Detailed Solution:**

The statement pattern $[p \wedge \sim r] \rightarrow (\sim r \wedge q)$ is False.

An implication $A \rightarrow B$ is False if and only if $A$ is True and $B$ is False.

Therefore, $p \wedge \sim r$ is True and $\sim r \wedge q$ is False.

For $p \wedge \sim r$ to be True, both $p$ and $\sim r$ must be True. This gives $p \equiv \text{T}$ and $r \equiv \text{F}$.

Since $\sim r$ is True, for $\sim r \wedge q$ to be False, $q$ must be False. This gives $q \equiv \text{F}$.

Thus, the truth values are $p \equiv \text{T}$, $q \equiv \text{F}$, and $r \equiv \text{F}$.

Now, checking the given options:

For $(p \vee r) \rightarrow \sim r$: $(\text{T} \vee \text{F}) \rightarrow \text{T} \equiv \text{T} \rightarrow \text{T} \equiv \text{T}$

For $(r \vee q) \rightarrow \sim p$: $(\text{F} \vee \text{F}) \rightarrow \text{F} \equiv \text{F} \rightarrow \text{F} \equiv \text{T}$

For $\sim(p \vee q) \rightarrow \sim r$: $\sim(\text{T} \vee \text{F}) \rightarrow \text{T} \equiv \text{F} \rightarrow \text{T} \equiv \text{T}$

For $\sim(r \vee q) \rightarrow \sim p$: $\sim(\text{F} \vee \text{F}) \rightarrow \text{F} \equiv \text{T} \rightarrow \text{F} \equiv \text{F}$

The statement pattern $\sim(r \vee q) \rightarrow \sim p$ has truth value False.

Answer: $\sim(r \vee q) \rightarrow \sim p$

</details>

---

### Q89. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The correct simplified circuit diagram for the logical statement $[\{\mathrm{q} \wedge(\sim \mathrm{q} \vee \mathrm{r})\} \wedge\{\sim \mathrm{p} \vee(\mathrm{p} \wedge \sim \mathrm{r})\}] \vee(\mathrm{p} \wedge \mathrm{r})$ where $\mathrm{p}, \mathrm{q}, \mathrm{r}$ represent switches $\mathrm{s}_1, \mathrm{~s}_2, \mathrm{~s}_3$ respectively.

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/OfjrV4j8wHJscLMacnhOAoS3U7NYTt1nWY-N_H-C6Po.original.fullsize.png">
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/Ij-ieO0lfEr0yxzHqTiS0GtrK3C0sIaQjRqC6ZcpFqQ.original.fullsize.png">
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/CS1WyGoSLbb0FoB02NMmiotdVXQ8ycYYsrluk9wkE_U.original.fullsize.png">
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/Ar6X_auE82BGh1UhGupRdoJZcgmT6o_vpfqAxWob7Tw.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/Ij-ieO0lfEr0yxzHqTiS0GtrK3C0sIaQjRqC6ZcpFqQ.original.fullsize.png">**

**Detailed Solution:**

The given logical statement is:
$[\{q \wedge (\sim q \vee r)\} \wedge \{\sim p \vee (p \wedge \sim r)\}] \vee (p \wedge r)$

Let us simplify the expression step by step.

First, simplify the term $q \wedge (\sim q \vee r)$ using the distributive law:
$q \wedge (\sim q \vee r) \equiv (q \wedge \sim q) \vee (q \wedge r)$
Since $q \wedge \sim q \equiv F$ (False), we get:
$F \vee (q \wedge r) \equiv q \wedge r$

Next, simplify the term $\sim p \vee (p \wedge \sim r)$ using the distributive law:
$\sim p \vee (p \wedge \sim r) \equiv (\sim p \vee p) \wedge (\sim p \vee \sim r)$
Since $\sim p \vee p \equiv T$ (True), we get:
$T \wedge (\sim p \vee \sim r) \equiv \sim p \vee \sim r$

Now, substitute these simplified terms back into the first square bracket:
$[\{q \wedge (\sim q \vee r)\} \wedge \{\sim p \vee (p \wedge \sim r)\}]$
$\equiv (q \wedge r) \wedge (\sim p \vee \sim r)$
$\equiv (q \wedge r \wedge \sim p) \vee (q \wedge r \wedge \sim r)$
Since $r \wedge \sim r \equiv F$, the second term becomes $F$:
$\equiv (q \wedge r \wedge \sim p) \vee F \equiv \sim p \wedge q \wedge r$

Now, substitute this into the complete expression:
$(\sim p \wedge q \wedge r) \vee (p \wedge r)$

Factor out $r$ using the distributive law:
$\equiv r \wedge ((\sim p \wedge q) \vee p)$
$\equiv r \wedge ((\sim p \vee p) \wedge (q \vee p))$
$\equiv r \wedge (T \wedge (p \vee q))$
$\equiv r \wedge (p \vee q)$

In terms of switching circuits, $p, q, r$ represent switches $S_1, S_2, S_3$ respectively. 
The logical connective $\vee$ represents a parallel combination, and $\wedge$ represents a series combination.
Thus, $r \wedge (p \vee q)$ corresponds to switch $S_3$ in series with the parallel combination of switches $S_1$ and $S_2$.

This arrangement is correctly shown in the second circuit diagram.

Answer: 
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/Ij-ieO0lfEr0yxzHqTiS0GtrK3C0sIaQjRqC6ZcpFqQ.original.fullsize.png">

</details>

---

### Q90. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\{(p \wedge \sim q) \wedge(p \wedge r)\} \rightarrow \sim p \vee q$ has truth value false then truth values of the statements p, q, r are respectively

**Options:**

- **(A)** $\mathrm{T}, \mathrm{T}, \mathrm{T}$
- **(B)** $\mathrm{F}, \mathrm{F}, \mathrm{F}$
- **(C)** $\mathrm{F}, \mathrm{F}, \mathrm{T}$
- **(D)** $\mathrm{T}, \mathrm{F}, \mathrm{T}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{T}, \mathrm{F}, \mathrm{T}$**

**Detailed Solution:**

The given statement is $\{(p \wedge \sim q) \wedge(p \wedge r)\} \rightarrow \sim p \vee q$.

An implication $X \rightarrow Y$ is false if and only if $X$ is true and $Y$ is false.

Therefore, we have:
$(p \wedge \sim q) \wedge (p \wedge r) \equiv \text{T}$
$\sim p \vee q \equiv \text{F}$

From $\sim p \vee q \equiv \text{F}$, both $\sim p$ and $q$ must be false. 
This gives $p \equiv \text{T}$ and $q \equiv \text{F}$.

From $(p \wedge \sim q) \wedge (p \wedge r) \equiv \text{T}$, all components connected by $\wedge$ must be true.
This implies $p \wedge r \equiv \text{T}$.

Since $p \equiv \text{T}$, we must have $r \equiv \text{T}$.

Thus, the truth values of $p, q, r$ are T, F, T respectively.

Answer: $\mathrm{T}, \mathrm{F}, \mathrm{T}$

</details>

---

### Q91. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the statement pattern $(p \wedge q) \rightarrow(r \vee \sim s)$ is false, then the truth values of p, q, r and s are respectively.

**Options:**

- **(A)** $\mathrm{T}, \mathrm{F}, \mathrm{T}, \mathrm{F}$
- **(B)** $\mathrm{T}, \mathrm{T}, \mathrm{T}, \mathrm{F}$
- **(C)** $\mathrm{T}, \mathrm{T}, \mathrm{F}, \mathrm{F}$
- **(D)** $\mathrm{T}, \mathrm{T}, \mathrm{F}, \mathrm{T}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{T}, \mathrm{T}, \mathrm{F}, \mathrm{T}$**

**Detailed Solution:**

The given statement pattern is $(p \wedge q) \rightarrow (r \vee \sim s)$.

It is given that the statement pattern is false.

A conditional statement $A \rightarrow B$ is false if and only if $A$ is true and $B$ is false.

Therefore, $(p \wedge q)$ is true and $(r \vee \sim s)$ is false.

For $(p \wedge q)$ to be true, both $p$ and $q$ must be true. Thus, $p \equiv \mathrm{T}$ and $q \equiv \mathrm{T}$.

For $(r \vee \sim s)$ to be false, both $r$ and $\sim s$ must be false. Thus, $r \equiv \mathrm{F}$ and $\sim s \equiv \mathrm{F}$.

Since $\sim s \equiv \mathrm{F}$, we get $s \equiv \mathrm{T}$.

The truth values of $p, q, r, s$ are respectively $\mathrm{T}, \mathrm{T}, \mathrm{F}, \mathrm{T}$.

Answer: $\mathrm{T}, \mathrm{T}, \mathrm{F}, \mathrm{T}$

</details>

---

### Q92. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The logical statement $[\sim(\sim \mathrm{p} \vee \mathrm{q}) \vee(\mathrm{p} \wedge \mathrm{r})] \wedge(\sim \mathrm{q} \wedge \mathrm{r})$ is equivalent to

**Options:**

- **(A)** $(p \wedge r) \wedge \sim q$
- **(B)** $(\sim \mathrm{p} \wedge \sim \mathrm{q}) \wedge \mathrm{r}$
- **(C)** $\sim \mathrm{p} \vee \mathrm{r}$
- **(D)** $(p \wedge \sim q) \vee r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(p \wedge r) \wedge \sim q$**

**Detailed Solution:**

The given statement is $[\sim(\sim p \vee q) \vee (p \wedge r)] \wedge (\sim q \wedge r)$.

Using De Morgan's law, $\sim(\sim p \vee q) \equiv p \wedge \sim q$.

The statement becomes $[(p \wedge \sim q) \vee (p \wedge r)] \wedge (\sim q \wedge r)$.

Using the distributive law, $(p \wedge \sim q) \vee (p \wedge r) \equiv p \wedge (\sim q \vee r)$.

Substituting this back, we get $p \wedge (\sim q \vee r) \wedge (\sim q \wedge r)$.

Using the associative law, this is $p \wedge [(\sim q \vee r) \wedge (\sim q \wedge r)]$.

Using the distributive law on the second part:

$(\sim q \vee r) \wedge (\sim q \wedge r) \equiv (\sim q \wedge (\sim q \wedge r)) \vee (r \wedge (\sim q \wedge r))$

$\equiv (\sim q \wedge r) \vee (\sim q \wedge r) \equiv \sim q \wedge r$.

Therefore, the entire statement simplifies to $p \wedge (\sim q \wedge r)$, which can be rearranged as $(p \wedge r) \wedge \sim q$.

Answer: $(p \wedge r) \wedge \sim q$

</details>

---

### Q93. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The equivalent statement of " If three vertices of a triangle are represented by cube roots of unity, then the triangle is an equilateral triangle " is

**Options:**

- **(A)** Three vertices of a triangle are represented by cube roots of unity and the triangle is not an equilaterals triangle.
- **(B)** If a triangle is an equilateral triangle then the three vertices of a triangle are represented by cube roots of unity.
- **(C)** If three vertices of triangle are not represented by cube roots of unity then the triangle is not an equilateral triangle.
- **(D)** If a triangle is not an equilateral triangle then the three vertices of the triangle can not be represented by cube roots of unity.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If a triangle is not an equilateral triangle then the three vertices of the triangle can not be represented by cube roots of unity.**

**Detailed Solution:**

Let $p$ be the statement "Three vertices of a triangle are represented by cube roots of unity".

Let $q$ be the statement "The triangle is an equilateral triangle".

The given statement is a conditional statement of the form $p \rightarrow q$.

The logically equivalent statement of an implication $p \rightarrow q$ is its contrapositive, which is $\sim q \rightarrow \sim p$.

Here, $\sim q$ is "A triangle is not an equilateral triangle".

And $\sim p$ is "The three vertices of the triangle can not be represented by cube roots of unity".

Therefore, the equivalent statement is "If a triangle is not an equilateral triangle then the three vertices of the triangle can not be represented by cube roots of unity".

Answer: If a triangle is not an equilateral triangle then the three vertices of the triangle can not be represented by cube roots of unity.

</details>

---

### Q94. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The negation of $(p \wedge \sim q) \rightarrow(p \vee \sim q)$ is

**Options:**

- **(A)** a tautology
- **(B)** a contingency
- **(C)** a contradiction
- **(D)** equivalent to $\mathrm{p} \wedge \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) a contradiction**

**Detailed Solution:**

Let the given statement be $S \equiv (p \wedge \sim q) \rightarrow (p \vee \sim q)$.

The negation of $S$ is $\sim S \equiv \sim ((p \wedge \sim q) \rightarrow (p \vee \sim q))$.

Using the logical equivalence $\sim (X \rightarrow Y) \equiv X \wedge \sim Y$, we get:

$\sim S \equiv (p \wedge \sim q) \wedge \sim (p \vee \sim q)$

Using De Morgan's Law, $\sim (p \vee \sim q) \equiv \sim p \wedge q$.

Substituting this into the expression:

$\sim S \equiv (p \wedge \sim q) \wedge (\sim p \wedge q)$

Using the commutative and associative laws of conjunction:

$\sim S \equiv (p \wedge \sim p) \wedge (q \wedge \sim q)$

Since $p \wedge \sim p \equiv F$ and $q \wedge \sim q \equiv F$, where $F$ denotes a contradiction:

$\sim S \equiv F \wedge F \equiv F$

Thus, the negation of the given statement is a contradiction.

Answer: a contradiction

</details>

---

### Q95. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The logically equivalent statement of $(\sim p \wedge q) \vee(\sim p \wedge \sim q) \vee(p \wedge \sim q)$ is

**Options:**

- **(A)** $(\sim \mathrm{p}) \wedge \mathrm{q}$
- **(B)** $(\sim p) \vee(\sim q)$
- **(C)** $(\sim p) \wedge(\sim q)$
- **(D)** $\mathrm{p} \vee \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\sim p) \vee(\sim q)$**

**Detailed Solution:**

The given logical expression is $(\sim p \wedge q) \vee (\sim p \wedge \sim q) \vee (p \wedge \sim q)$.

Consider the first two terms: $(\sim p \wedge q) \vee (\sim p \wedge \sim q)$.

By the distributive law, this is equivalent to $\sim p \wedge (q \vee \sim q)$.

Since $q \vee \sim q \equiv T$ (tautology), this becomes $\sim p \wedge T \equiv \sim p$.

Substituting this back into the original expression, we get:

$\sim p \vee (p \wedge \sim q)$

Applying the distributive law again, this is equivalent to:

$(\sim p \vee p) \wedge (\sim p \vee \sim q)$

Since $\sim p \vee p \equiv T$, this becomes:

$T \wedge (\sim p \vee \sim q) \equiv \sim p \vee \sim q$

Thus, the logically equivalent statement is $(\sim p) \vee (\sim q)$.

Answer: $(\sim p) \vee(\sim q)$

</details>

---

### Q96. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If a statement $q$ has truth value False and $(p \wedge q) \leftrightarrow r$ has truth value True then which of the following has truth value true?

**Options:**

- **(A)** $\mathrm{p} \wedge \mathrm{q}$
- **(B)** $\mathrm{p} \vee \mathrm{r}$
- **(C)** $\mathrm{p} \wedge \mathrm{r}$
- **(D)** $(p \wedge r) \rightarrow(p \vee r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(p \wedge r) \rightarrow(p \vee r)$**

**Detailed Solution:**

Given $q \equiv F$.

The truth value of $p \wedge q$ is $F$ for any truth value of $p$.

Given $(p \wedge q) \leftrightarrow r \equiv T$.

Substituting $p \wedge q \equiv F$, we get $F \leftrightarrow r \equiv T$.

For a biconditional statement to be true, both components must have the same truth value. This implies $r \equiv F$.

Now evaluating the given options:

For $p \wedge q$, since $q \equiv F$, $p \wedge q \equiv F$.

For $p \vee r$, since $r \equiv F$, $p \vee r \equiv p \vee F \equiv p$ (not always true).

For $p \wedge r$, since $r \equiv F$, $p \wedge r \equiv p \wedge F \equiv F$.

For $(p \wedge r) \rightarrow (p \vee r)$, since $r \equiv F$, $p \wedge r \equiv F$. The implication becomes $F \rightarrow (p \vee F) \equiv F \rightarrow p$. An implication with a false antecedent is always true, so $F \rightarrow p \equiv T$.

Therefore, $(p \wedge r) \rightarrow (p \vee r)$ has the truth value True.

Answer: $(p \wedge r) \rightarrow(p \vee r)$

</details>

---

### Q97. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following are pairs of equivalent circuits
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/Ie_zY2sCT9VD7IvAX9kmo0oRBFi73_gZlconqJYsx64.original.fullsize.png">

**Options:**

- **(A)** (A) and (B)
- **(B)** (B) and (D)
- **(C)** (C) and (E)
- **(D)** (A) and (C)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (A) and (C)**

**Detailed Solution:**

Let the switches $S_1, S_2, S_3$ be represented by logical statements $p, q, r$ respectively. A series connection corresponds to the logical AND ($\wedge$) operation, and a parallel connection corresponds to the logical OR ($\vee$) operation.

For circuit (A), the upper branch has $S_1$ and $S_2$ in series ($p \wedge q$) and the lower branch has $S_1$ and $S_3$ in series ($p \wedge r$). These two branches are connected in parallel, so the logical expression is $(p \wedge q) \vee (p \wedge r)$.

For circuit (B), the upper branch has $S_1$ ($p$) and the lower branch has $S_2$ and $S_3$ in series ($q \wedge r$). These are in parallel, so the expression is $p \vee (q \wedge r)$.

For circuit (C), switch $S_1$ ($p$) is in series with the parallel combination of $S_2$ and $S_3$ ($q \vee r$). The logical expression is $p \wedge (q \vee r)$.

For circuit (D), all three switches are in series, so the expression is $p \wedge q \wedge r$.

For circuit (E), the upper branch has $S_1$ and $S_2$ in series ($p \wedge q$) and the lower branch has $S_3$ ($r$). These are in parallel, so the expression is $(p \wedge q) \vee r$.

By the distributive law of logic, we know that:
$(p \wedge q) \vee (p \wedge r) \equiv p \wedge (q \vee r)$

This shows that the logical expression for circuit (A) is equivalent to the logical expression for circuit (C). Therefore, circuits (A) and (C) are equivalent.

Answer: (A) and (C)

</details>

---

### Q98. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The last column in the truth table of the statement pattern $[p \rightarrow(q \wedge \sim p)] \vee[(p \vee \sim q) \wedge p]$ is

**Options:**

- **(A)** TTTF
- **(B)** TFFF
- **(C)** TTTT
- **(D)** FFTT

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) TTTT**

**Detailed Solution:**

The given statement pattern is $[p \rightarrow(q \wedge \sim p)] \vee[(p \vee \sim q) \wedge p]$.

Consider the first part of the statement pattern: $p \rightarrow (q \wedge \sim p)$.
Using the conditional law $A \rightarrow B \equiv \sim A \vee B$, we get:
$p \rightarrow (q \wedge \sim p) \equiv \sim p \vee (q \wedge \sim p)$
By the distributive law, this becomes:
$\equiv (\sim p \vee q) \wedge (\sim p \vee \sim p)$
$\equiv (\sim p \vee q) \wedge \sim p$
By the absorption law, this simplifies to $\sim p$.

Now consider the second part of the statement pattern: $(p \vee \sim q) \wedge p$.
By the absorption law, $(p \vee \sim q) \wedge p \equiv p$.

Substituting these simplified forms back into the original statement pattern, we get:
$[p \rightarrow(q \wedge \sim p)] \vee[(p \vee \sim q) \wedge p] \equiv \sim p \vee p$

By the complement law, $\sim p \vee p \equiv T$.
Thus, the given statement pattern is a tautology. Since there are two statement letters ($p$ and $q$), the truth table has 4 rows, and every entry in the last column will be $T$.

Therefore, the last column is TTTT.

Answer: TTTT

</details>

---

### Q99. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the three statements -
$\mathrm{p}: \forall \mathrm{n} \in \mathbb{N}, 10 \mathrm{n}-3$ is a prime number, when n is not divisible by 3 .
$\mathrm{q}: \frac{2}{\sqrt{3}}, \frac{-2}{\sqrt{3}}, \frac{-1}{\sqrt{3}}$ are the direction cosines of a directed line.
$\mathrm{r}: \sin x$ is an increasing function in the interval $\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]$.
Then which of the following statement pattern has truth value true?

**Options:**

- **(A)** $(p \wedge q) \leftrightarrow r$
- **(B)** $(p \rightarrow q) \rightarrow \sim r$
- **(C)** $(\sim p \vee q) \wedge r$
- **(D)** $(\sim \mathrm{p} \wedge \sim \mathrm{q}) \leftrightarrow \sim \mathrm{r}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\sim p \vee q) \wedge r$**

**Detailed Solution:**

For statement $p$: Let $n = 8$. Here, $n$ is not divisible by $3$. However, $10(8) - 3 = 77$, which is not a prime number. Thus, the truth value of $p$ is $F$.

For statement $q$: The sum of squares of direction cosines $l, m, n$ of a line must be $1$. Here, $l^2 + m^2 + n^2 = \left(\dfrac{2}{\sqrt{3}}\right)^2 + \left(\dfrac{-2}{\sqrt{3}}\right)^2 + \left(\dfrac{-1}{\sqrt{3}}\right)^2 = \dfrac{4}{3} + \dfrac{4}{3} + \dfrac{1}{3} = 3 \neq 1$. Thus, the truth value of $q$ is $F$.

For statement $r$: Let $f(x) = \sin x$. Then $f'(x) = \cos x$. For $x \in \left[\dfrac{-\pi}{2}, \dfrac{\pi}{2}\right]$, $\cos x \ge 0$, which means $f(x)$ is an increasing function. Thus, the truth value of $r$ is $T$.

Evaluating the given statement patterns:

$(p \wedge q) \leftrightarrow r \equiv (F \wedge F) \leftrightarrow T \equiv F \leftrightarrow T \equiv F$

$(p \rightarrow q) \rightarrow \sim r \equiv (F \rightarrow F) \rightarrow \sim T \equiv T \rightarrow F \equiv F$

$(\sim p \vee q) \wedge r \equiv (\sim F \vee F) \wedge T \equiv (T \vee F) \wedge T \equiv T \wedge T \equiv T$

$(\sim p \wedge \sim q) \leftrightarrow \sim r \equiv (\sim F \wedge \sim F) \leftrightarrow \sim T \equiv (T \wedge T) \leftrightarrow F \equiv T \leftrightarrow F \equiv F$

The statement pattern $(\sim p \vee q) \wedge r$ has the truth value $T$.

Answer: $(\sim p \vee q) \wedge r$

</details>

---

### Q100. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The statement pattern $[(p \rightarrow q) \wedge \sim q] \rightarrow r$ is a tautology when $r$ is equivalent to

**Options:**

- **(A)** $\mathrm{p} \wedge \sim \mathrm{q}$
- **(B)** $q \vee p$
- **(C)** $\mathrm{p} \wedge \mathrm{q}$
- **(D)** $\sim \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sim \mathrm{q}$**

**Detailed Solution:**

The given statement pattern is $[(p \rightarrow q) \wedge \sim q] \rightarrow r$.

Consider the antecedent: $(p \rightarrow q) \wedge \sim q$.

Using the logical equivalence $p \rightarrow q \equiv \sim p \vee q$, we get:

$(p \rightarrow q) \wedge \sim q \equiv (\sim p \vee q) \wedge \sim q$

By distributive law:

$(\sim p \vee q) \wedge \sim q \equiv (\sim p \wedge \sim q) \vee (q \wedge \sim q)$

Since $q \wedge \sim q \equiv F$, we have:

$(\sim p \wedge \sim q) \vee F \equiv \sim p \wedge \sim q$

Thus, the given statement pattern simplifies to $(\sim p \wedge \sim q) \rightarrow r$.

For this conditional statement to be a tautology, the consequent $r$ must be true whenever the antecedent $\sim p \wedge \sim q$ is true. If $\sim p \wedge \sim q$ is true, then both $\sim p$ and $\sim q$ are true.

Checking the given options, if $r \equiv \sim q$, the statement pattern becomes $(\sim p \wedge \sim q) \rightarrow \sim q$.

Using the conditional equivalence $A \rightarrow B \equiv \sim A \vee B$:

$(\sim p \wedge \sim q) \rightarrow \sim q \equiv \sim(\sim p \wedge \sim q) \vee \sim q$

By De Morgan's law:

$\equiv (p \vee q) \vee \sim q$

By associative law:

$\equiv p \vee (q \vee \sim q)$

Since $q \vee \sim q \equiv T$ (tautology):

$\equiv p \vee T \equiv T$

Hence, the statement pattern is a tautology when $r$ is equivalent to $\sim q$.

Answer: $\sim \mathrm{q}$

</details>

---

### Q101. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement $\sim(p \leftrightarrow \sim q)$ is

**Options:**

- **(A)** equivalent to $\mathrm{p} \leftrightarrow \mathrm{q}$
- **(B)** a fallacy
- **(C)** a tautology
- **(D)** equivalent to $\sim \mathrm{p} \leftrightarrow \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) equivalent to $\mathrm{p} \leftrightarrow \mathrm{q}$**

**Detailed Solution:**

Constructing the truth table for the given logical statements:

<table><tr><td>$p$</td><td>$q$</td><td>$\sim q$</td><td>$p \leftrightarrow \sim q$</td><td>$\sim(p \leftrightarrow \sim q)$</td><td>$p \leftrightarrow q$</td></tr><tr><td>T</td><td>T</td><td>F</td><td>F</td><td>T</td><td>T</td></tr><tr><td>T</td><td>F</td><td>T</td><td>T</td><td>F</td><td>F</td></tr><tr><td>F</td><td>T</td><td>F</td><td>T</td><td>F</td><td>F</td></tr><tr><td>F</td><td>F</td><td>T</td><td>F</td><td>T</td><td>T</td></tr></table>

From the truth table, the entries in the columns for $\sim(p \leftrightarrow \sim q)$ and $p \leftrightarrow q$ are identical.

Therefore, $\sim(p \leftrightarrow \sim q) \equiv p \leftrightarrow q$.

Answer: equivalent to $\mathrm{p} \leftrightarrow \mathrm{q}$

</details>

---

### Q102. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Truth values of $p \rightarrow r$ is $F$ and $p \leftrightarrow q$ is $F$. Then the truth values of $(\sim p \vee q) \rightarrow(p \vee \sim q)$ and $(p \wedge \sim q) \rightarrow(\sim p \wedge q)$ are respectively

**Options:**

- **(A)** $\mathrm{T}, \mathrm{F}$
- **(B)** $\mathrm{F}, \mathrm{T}$
- **(C)** $\mathrm{T}, \mathrm{T}$
- **(D)** $\mathrm{F}, \mathrm{F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{T}, \mathrm{F}$**

**Detailed Solution:**

Given $p \rightarrow r$ is $F$, which implies $p$ is $T$ and $r$ is $F$.

Given $p \leftrightarrow q$ is $F$. Since $p$ is $T$, $q$ must be $F$.

Thus, $p = T$, $q = F$, $r = F$.

For the first expression: $(\sim p \vee q) \rightarrow (p \vee \sim q)$

Substituting the truth values:

$(\sim T \vee F) \rightarrow (T \vee \sim F)$

$(F \vee F) \rightarrow (T \vee T)$

$F \rightarrow T \equiv T$

For the second expression: $(p \wedge \sim q) \rightarrow (\sim p \wedge q)$

Substituting the truth values:

$(T \wedge \sim F) \rightarrow (\sim T \wedge F)$

$(T \wedge T) \rightarrow (F \wedge F)$

$T \rightarrow F \equiv F$

The truth values are $T$ and $F$ respectively.

Answer: $\mathrm{T}, \mathrm{F}$

</details>

---

### Q103. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The proposition $(\sim p) \vee(p \wedge \sim q)$ is equivalent to

**Options:**

- **(A)** $\mathrm{p} \wedge(\sim \mathrm{q})$
- **(B)** $\mathrm{p} \rightarrow(\sim \mathrm{q})$
- **(C)** $\mathrm{p} \vee(\mathrm{q})$
- **(D)** $\mathrm{q} \rightarrow \mathrm{p}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{p} \rightarrow(\sim \mathrm{q})$**

**Detailed Solution:**

The given proposition is $(\sim p) \vee (p \wedge \sim q)$.

Using the distributive law:

$\equiv (\sim p \vee p) \wedge (\sim p \vee \sim q)$

Since $\sim p \vee p \equiv T$ (Tautology):

$\equiv T \wedge (\sim p \vee \sim q)$

Using the identity law:

$\equiv \sim p \vee \sim q$

Using the conditional equivalence $A \rightarrow B \equiv \sim A \vee B$:

$\equiv p \rightarrow (\sim q)$

Answer: $\mathrm{p} \rightarrow(\sim \mathrm{q})$

</details>

---

### Q104. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If p : The total prime numbers between 2 to 100 are 26 .
q : Zero is a complex number.
r : Least common multiple (L.C.M.) of 6 and 7 is 6 .
Then which of the following is correct?

**Options:**

- **(A)** $(p \wedge q) \rightarrow r$ has truth value False.
- **(B)** $(\mathrm{p} \rightarrow \mathrm{q}) \rightarrow \mathrm{r}$ has truth value True.
- **(C)** $(p \vee q) \leftrightarrow r$ has truth value False.
- **(D)** $(\mathrm{p} \rightarrow \mathrm{q}) \rightarrow(\mathrm{q} \rightarrow \mathrm{p})$ has truth value True.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(p \vee q) \leftrightarrow r$ has truth value False.**

**Detailed Solution:**

The truth values of the given statements are evaluated as follows:

Statement p: The total prime numbers between 2 to 100 are 26.
There are exactly 25 prime numbers up to 100. Thus, the truth value of p is False (F).

Statement q: Zero is a complex number.
Zero can be written in the form $0 + 0i$, which makes it a complex number. Thus, the truth value of q is True (T).

Statement r: Least common multiple (L.C.M.) of 6 and 7 is 6.
The L.C.M. of 6 and 7 is 42. Thus, the truth value of r is False (F).

Now, we substitute the truth values $p \equiv F$, $q \equiv T$, and $r \equiv F$ into the given options:

For $(p \wedge q) \rightarrow r$:
$(F \wedge T) \rightarrow F \equiv F \rightarrow F \equiv T$

For $(p \rightarrow q) \rightarrow r$:
$(F \rightarrow T) \rightarrow F \equiv T \rightarrow F \equiv F$

For $(p \vee q) \leftrightarrow r$:
$(F \vee T) \leftrightarrow F \equiv T \leftrightarrow F \equiv F$

For $(p \rightarrow q) \rightarrow (q \rightarrow p)$:
$(F \rightarrow T) \rightarrow (T \rightarrow F) \equiv T \rightarrow F \equiv F$

The only option that correctly matches the evaluated truth value is $(p \vee q) \leftrightarrow r$, which has a truth value of False.

Answer: $(p \vee q) \leftrightarrow r$ has truth value False.

</details>

---

### Q105. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The contrapositive of the inverse of $\mathrm{p} \rightarrow(\mathrm{p} \rightarrow \mathrm{q})$ is

**Options:**

- **(A)** $(\sim \mathrm{p} \wedge \mathrm{q}) \rightarrow \mathrm{p}$
- **(B)** $(\sim \mathrm{p} \vee \mathrm{q}) \rightarrow \mathrm{p}$
- **(C)** $\mathrm{p} \rightarrow(\sim \mathrm{p} \vee \mathrm{q})$
- **(D)** $(p \vee q) \rightarrow p$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\sim \mathrm{p} \vee \mathrm{q}) \rightarrow \mathrm{p}$**

**Detailed Solution:**

Let the given statement be $A \rightarrow B$, where $A \equiv \mathrm{p}$ and $B \equiv \mathrm{p} \rightarrow \mathrm{q}$.

The inverse of $A \rightarrow B$ is $\sim A \rightarrow \sim B$.

The contrapositive of the inverse $\sim A \rightarrow \sim B$ is $\sim(\sim B) \rightarrow \sim(\sim A)$, which simplifies to $B \rightarrow A$.

Substituting $A$ and $B$ back, we get $(\mathrm{p} \rightarrow \mathrm{q}) \rightarrow \mathrm{p}$.

Using the logical equivalence $\mathrm{p} \rightarrow \mathrm{q} \equiv \sim \mathrm{p} \vee \mathrm{q}$, the expression becomes $(\sim \mathrm{p} \vee \mathrm{q}) \rightarrow \mathrm{p}$.

Answer: $(\sim \mathrm{p} \vee \mathrm{q}) \rightarrow \mathrm{p}$

</details>

---

### Q106. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $p \rightarrow(q \vee r)$ is false, then the truth values of $\mathrm{p}, \mathrm{q}, \mathrm{r}$ are respectively

**Options:**

- **(A)** F,F,F
- **(B)** T, T, F
- **(C)** T, F, F
- **(D)** $\mathrm{F}, \mathrm{T}, \mathrm{T}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) T, F, F**

**Detailed Solution:**

The given statement is $p \rightarrow (q \vee r)$.

It is given that $p \rightarrow (q \vee r)$ is false.

A conditional statement $X \rightarrow Y$ is false only when $X$ is true and $Y$ is false.

Therefore, $p$ is true (T) and $q \vee r$ is false (F).

The disjunction $q \vee r$ is false only when both $q$ and $r$ are false.

Therefore, $q$ is false (F) and $r$ is false (F).

The truth values of $p, q, r$ are T, F, F respectively.

Answer: T, F, F

</details>

---

### Q107. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Contrapositive of the statement.
'If two numbers are equal, then their squares are equal' is

**Options:**

- **(A)** If the squares of two numbers are equal, then the numbers are not equal.
- **(B)** If the squares of two numbers are not equal, then the numbers are equal.
- **(C)** If the squares of two numbers are not equal, then the numbers are not equal.
- **(D)** If the squares of two numbers are equal, then the numbers are equal.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) If the squares of two numbers are not equal, then the numbers are not equal.**

**Detailed Solution:**

Let $p$ be the statement 'Two numbers are equal'.

Let $q$ be the statement 'Their squares are equal'.

The given statement is in the form $p \rightarrow q$.

The contrapositive of the conditional statement $p \rightarrow q$ is $\sim q \rightarrow \sim p$.

Here, $\sim q$ is 'The squares of two numbers are not equal' and $\sim p$ is 'The numbers are not equal'.

Therefore, the contrapositive statement is 'If the squares of two numbers are not equal, then the numbers are not equal'.

Answer: If the squares of two numbers are not equal, then the numbers are not equal.

</details>

---

### Q108. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The following statement $(\mathrm{p} \rightarrow \mathrm{q}) \rightarrow((\sim \mathrm{p} \rightarrow \mathrm{q}) \rightarrow \mathrm{q})$ is

**Options:**

- **(A)** a fallacy.
- **(B)** equivalent to $(\sim \mathrm{p}) \rightarrow \mathrm{q}$.
- **(C)** equivalent to $\mathrm{p} \rightarrow(\sim \mathrm{q})$.
- **(D)** a tautology.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a tautology.**

**Detailed Solution:**

The given statement is $(p \rightarrow q) \rightarrow ((\sim p \rightarrow q) \rightarrow q)$.

Consider the second part of the statement: $(\sim p \rightarrow q) \rightarrow q$.

Using the logical equivalence $A \rightarrow B \equiv \sim A \vee B$, we get:

$\sim p \rightarrow q \equiv p \vee q$

Substituting this back, we have:

$(p \vee q) \rightarrow q \equiv \sim(p \vee q) \vee q$

Using De Morgan's law, we get:

$\sim(p \vee q) \vee q \equiv (\sim p \wedge \sim q) \vee q$

Using the distributive law, we get:

$(\sim p \vee q) \wedge (\sim q \vee q)$

Since $\sim q \vee q \equiv T$ (a tautology), the expression simplifies to:

$(\sim p \vee q) \wedge T \equiv \sim p \vee q$

We know that $\sim p \vee q \equiv p \rightarrow q$.

Therefore, the original statement becomes:

$(p \rightarrow q) \rightarrow (p \rightarrow q)$

Any statement of the form $X \rightarrow X$ is always true.

Thus, the given statement is a tautology.

Answer: a tautology.

</details>

---

### Q109. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Contrapositive of the statement
'If two numbers are not equal, then their squares are not equal', is

**Options:**

- **(A)** If the squares of two numbers are not equal, then the numbers are equal.
- **(B)** If the squares of two numbers are equal, then the numbers are not equal.
- **(C)** If the squares of two numbers are equal, then the numbers are equal.
- **(D)** If the squares of two numbers are not equal, then the numbers are not equal.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) If the squares of two numbers are equal, then the numbers are equal.**

**Detailed Solution:**

Let $p$ be the statement 'Two numbers are not equal'.

Let $q$ be the statement 'Their squares are not equal'.

The given statement is in the form $p \rightarrow q$.

The contrapositive of the conditional statement $p \rightarrow q$ is $\sim q \rightarrow \sim p$.

Here, $\sim q$ is 'The squares of two numbers are equal' and $\sim p$ is 'The numbers are equal'.

Therefore, the contrapositive is 'If the squares of two numbers are equal, then the numbers are equal'.

Answer: If the squares of two numbers are equal, then the numbers are equal.

</details>

---

### Q110. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let p : A man is judge.
$\mathrm{q}: \mathrm{He}$ is honest.
The inverse of $p \rightarrow q$ is

**Options:**

- **(A)** If a man is judge, then he is honest.
- **(B)** If a man is not judge, then he is not honest.
- **(C)** If a man is honest, then he is judge.
- **(D)** If a man is not honest then, he is not judge.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) If a man is not judge, then he is not honest.**

**Detailed Solution:**

Given:
$p$: A man is judge.
$q$: He is honest.

The given statement is $p \rightarrow q$.
The inverse of the conditional statement $p \rightarrow q$ is $\sim p \rightarrow \sim q$.

$\sim p$: A man is not judge.
$\sim q$: He is not honest.

Therefore, the inverse statement $\sim p \rightarrow \sim q$ is "If a man is not judge, then he is not honest."

Answer: If a man is not judge, then he is not honest.

</details>

---

### Q111. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{p}, \mathrm{q}$ and r be the statements
p : X is an equilateral triangle
$\mathrm{q}: \mathrm{X}$ is isosceles triangle
$r: q \vee \sim p$,
then the equivalent statement of $r$ is

**Options:**

- **(A)** If X is not an equilateral triangle, then X is not an isosceles triangle
- **(B)** X is neither isosceles nor equilateral triangle
- **(C)** X is isosceles but not an equilateral triangle
- **(D)** If X is not an isosceles triangle, then X is not an equilateral triangle.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If X is not an isosceles triangle, then X is not an equilateral triangle.**

**Detailed Solution:**

Given statements:
$p$: X is an equilateral triangle
$q$: X is an isosceles triangle
$r$: $q \vee \sim p$

We know that the logical expression $q \vee \sim p$ can be rewritten using the commutative law as $\sim p \vee q$.

Using the conditional equivalence $\sim A \vee B \equiv A \rightarrow B$, we get:
$\sim p \vee q \equiv p \rightarrow q$

The contrapositive of $p \rightarrow q$ is $\sim q \rightarrow \sim p$, which is logically equivalent to it.

Translating $\sim q \rightarrow \sim p$ into words, we get:
"If X is not an isosceles triangle, then X is not an equilateral triangle."

This matches the given option.

Answer: If X is not an isosceles triangle, then X is not an equilateral triangle.

</details>

---

### Q112. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $(p \wedge \sim r) \rightarrow(\sim p \vee q)$ has truth value False, then truth values of $p, q, r$ are respectively.

**Options:**

- **(A)** F, F, T
- **(B)** F, T, F
- **(C)** T, F, F
- **(D)** $\quad \mathrm{T}, \mathrm{T}, \mathrm{F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) T, F, F**

**Detailed Solution:**

The given statement is $(p \wedge \sim r) \rightarrow (\sim p \vee q)$.

An implication $A \rightarrow B$ is False if and only if $A$ is True and $B$ is False.

Therefore, $p \wedge \sim r$ must be True, and $\sim p \vee q$ must be False.

For $p \wedge \sim r$ to be True, both $p$ and $\sim r$ must be True. This gives $p = \text{T}$ and $r = \text{F}$.

For $\sim p \vee q$ to be False, both $\sim p$ and $q$ must be False. Since $p = \text{T}$, $\sim p$ is already False. This gives $q = \text{F}$.

Thus, the truth values of $p, q, r$ are T, F, F respectively.

Answer: T, F, F

</details>

---

### Q113. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The converse of "If 3 is a prime number, then 3 is odd." is

**Options:**

- **(A)** If 3 is odd then it is a prime number.
- **(B)** If 3 is not a prime number then 3 is even.
- **(C)** If 3 is a prime number then 3 is even.
- **(D)** If 3 is not a prime number then 3 is not odd.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) If 3 is odd then it is a prime number.**

**Detailed Solution:**

Let $p$ be the statement "$3$ is a prime number" and $q$ be the statement "$3$ is odd".

The given statement is of the form $p \rightarrow q$.

The converse of the conditional statement $p \rightarrow q$ is $q \rightarrow p$.

Therefore, the converse of the given statement is "If $3$ is odd, then it is a prime number".

Answer: If 3 is odd then it is a prime number.

</details>

---

### Q114. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The expression $((p \wedge q) \vee(p \vee \sim q)) \wedge(\sim p \wedge \sim q)$ is equivalent to

**Options:**

- **(A)** $\mathrm{p} \wedge \mathrm{q}$
- **(B)** $\mathrm{p} \vee \sim \mathrm{q}$
- **(C)** $\mathrm{p} \wedge \sim \mathrm{q}$
- **(D)** $(\sim p) \wedge(\sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim p) \wedge(\sim q)$**

**Detailed Solution:**

Given expression: $((p \wedge q) \vee (p \vee \sim q)) \wedge (\sim p \wedge \sim q)$

Using the associative property, the first part can be written as:
$((p \wedge q) \vee p) \vee \sim q$

Using the absorption law, $(p \wedge q) \vee p = p$.
So, the first part simplifies to $p \vee \sim q$.

Now, substitute this back into the original expression:
$(p \vee \sim q) \wedge (\sim p \wedge \sim q)$

Using the distributive law:
$(p \wedge (\sim p \wedge \sim q)) \vee (\sim q \wedge (\sim p \wedge \sim q))$

Using the associative and commutative properties:
$(p \wedge \sim p \wedge \sim q) \vee (\sim p \wedge (\sim q \wedge \sim q))$

Since $p \wedge \sim p = F$ (False) and $\sim q \wedge \sim q = \sim q$:
$(F \wedge \sim q) \vee (\sim p \wedge \sim q)$

$F \vee (\sim p \wedge \sim q) = \sim p \wedge \sim q$

Answer: $(\sim p) \wedge(\sim q)$

</details>

---

### Q115. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The inverse of $p \rightarrow(q \rightarrow r)$ is logically equivalent to

**Options:**

- **(A)** $\mathrm{p} \rightarrow(\mathrm{q} \rightarrow \mathrm{r})$
- **(B)** $(\mathrm{q} \rightarrow \mathrm{r}) \rightarrow \sim \mathrm{p}$
- **(C)** $(p \vee q) \rightarrow r$
- **(D)** $(\mathrm{q} \rightarrow \mathrm{r}) \rightarrow \mathrm{p}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\mathrm{q} \rightarrow \mathrm{r}) \rightarrow \mathrm{p}$**

**Detailed Solution:**

The given statement is $p \rightarrow (q \rightarrow r)$.

The inverse of a conditional statement $A \rightarrow B$ is $\sim A \rightarrow \sim B$.

Therefore, the inverse of $p \rightarrow (q \rightarrow r)$ is $\sim p \rightarrow \sim(q \rightarrow r)$.

Using the property that a conditional statement is logically equivalent to its contrapositive ($X \rightarrow Y \equiv \sim Y \rightarrow \sim X$), we get:

$\sim p \rightarrow \sim(q \rightarrow r) \equiv \sim(\sim(q \rightarrow r)) \rightarrow \sim(\sim p)$

$\equiv (q \rightarrow r) \rightarrow p$

Answer: $(\mathrm{q} \rightarrow \mathrm{r}) \rightarrow \mathrm{p}$

</details>

---

### Q116. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Negation of the statement "The payment will be made if and only if the work is finished in time." is

**Options:**

- **(A)** The work is finished in time and the payment is not made.
- **(B)** The payment is made and the work is not finished in time.
- **(C)** The work is finished in time and the payment is not made, or the payment is made and the work is finished in time.
- **(D)** Either the work is finished in time and the payment is not made, or the payment is made and the work is not finished in time.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Either the work is finished in time and the payment is not made, or the payment is made and the work is not finished in time.**

**Detailed Solution:**

Let $p$ be the statement "The payment will be made".

Let $q$ be the statement "The work is finished in time".

The given statement is of the form $p \leftrightarrow q$.

The negation of $p \leftrightarrow q$ is $\sim(p \leftrightarrow q)$.

Using the logical equivalence $p \leftrightarrow q \equiv (p \rightarrow q) \wedge (q \rightarrow p)$, we get:

$\sim(p \leftrightarrow q) \equiv \sim((p \rightarrow q) \wedge (q \rightarrow p))$

$\equiv \sim(p \rightarrow q) \vee \sim(q \rightarrow p)$

$\equiv (p \wedge \sim q) \vee (q \wedge \sim p)$

Translating this back to English:

$p \wedge \sim q$: The payment is made and the work is not finished in time.

$q \wedge \sim p$: The work is finished in time and the payment is not made.

Therefore, the negation is "Either the work is finished in time and the payment is not made, or the payment is made and the work is not finished in time."

Answer: Either the work is finished in time and the payment is not made, or the payment is made and the work is not finished in time.

</details>

---

### Q117. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Negation of the statement ' Horses have wings if and only if crows have tails. ' is

**Options:**

- **(A)** Horses have wings but crows do not have tails.
or crows have tails but horses do not have wings.
- **(B)** Horses do not have wings if and only if crows do not have tails.
- **(C)** Horses do not have wings and crows have tails.
or Horses have wings and crows have tails.
- **(D)** Horses do not have wings and crows do not have tails.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Horses have wings but crows do not have tails.
or crows have tails but horses do not have wings.**

**Detailed Solution:**

Let $p$ be the statement 'Horses have wings'.

Let $q$ be the statement 'Crows have tails'.

The given statement is of the form $p \leftrightarrow q$.

The negation of $p \leftrightarrow q$ is $\sim(p \leftrightarrow q)$.

We know that $p \leftrightarrow q \equiv (p \rightarrow q) \wedge (q \rightarrow p)$.

Therefore, $\sim(p \leftrightarrow q) \equiv \sim((p \rightarrow q) \wedge (q \rightarrow p))$

$\equiv \sim(p \rightarrow q) \vee \sim(q \rightarrow p)$

$\equiv (p \wedge \sim q) \vee (q \wedge \sim p)$

This translates to: 'Horses have wings and crows do not have tails, or crows have tails and horses do not have wings'.

Since the word 'but' is logically equivalent to 'and', the statement can be written as: 'Horses have wings but crows do not have tails, or crows have tails but horses do not have wings'.

Answer: Horses have wings but crows do not have tails.
or crows have tails but horses do not have wings.

</details>

---

### Q118. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{p} \rightarrow(\sim \mathrm{p} \vee \sim \mathrm{q})$ is false, then the truth values of $p$ and $q$ are respectively

**Options:**

- **(A)** F, F
- **(B)** $\mathrm{F}, \mathrm{T}$
- **(C)** $\mathrm{T}, \mathrm{T}$
- **(D)** $\mathrm{T}, \mathrm{F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{T}, \mathrm{T}$**

**Detailed Solution:**

The given statement is $p \rightarrow (\sim p \vee \sim q)$.

We know that an implication $X \rightarrow Y$ is false if and only if $X$ is true and $Y$ is false.

Therefore, $p$ must be true (T) and the expression $(\sim p \vee \sim q)$ must be false (F).

Since $p$ is true, $\sim p$ is false (F).

For the disjunction $(\sim p \vee \sim q)$ to be false, both of its components must be false. This means $\sim q$ must also be false (F).

Since $\sim q$ is false, $q$ must be true (T).

Hence, the truth values of $p$ and $q$ are T and T respectively.

Answer: $\mathrm{T}, \mathrm{T}$

</details>

---

### Q119. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $p, q, r$ be three statements such that the truth value of $(p \wedge q) \rightarrow(\sim q \vee r)$ is $F$. Then the truth values of $p, q, r$ are respectively

**Options:**

- **(A)** T, F, T.
- **(B)** $\mathrm{T}, \mathrm{T}, \mathrm{T}$.
- **(C)** F, T, F.
- **(D)** $T, T, F$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $T, T, F$.**

**Detailed Solution:**

The given statement is $(p \wedge q) \rightarrow (\sim q \vee r)$.

We are given that the truth value of this statement is F.

An implication $X \rightarrow Y$ is F if and only if $X$ is T and $Y$ is F.

Therefore, $p \wedge q$ is T and $\sim q \vee r$ is F.

For $p \wedge q$ to be T, both $p$ and $q$ must be T. Thus, $p$ is T and $q$ is T.

For $\sim q \vee r$ to be F, both $\sim q$ and $r$ must be F.

Since $q$ is T, $\sim q$ is F, which is consistent. Thus, $r$ must be F.

The truth values of $p, q, r$ are T, T, F respectively.

Answer: $T, T, F$.

</details>

---

### Q120. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the statements given by following :
(A) If $3+3=7$, then $4+3=8$.
(B) If $5+3=8$, then earth is flat.
(C) If both $(\mathrm{A})$ and $(\mathrm{B})$ are true, then $5+6=17$.
Then which of the following statements is correct?

**Options:**

- **(A)** (A) is true while (B) and (C) are false.
- **(B)** (A) and (C) are true while (B) is false.
- **(C)** (A) and (B) are false, while (C) is true.
- **(D)** (A) is false but (B) and (C) are true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (A) and (C) are true while (B) is false.**

**Detailed Solution:**

A conditional statement $p \rightarrow q$ is false if and only if $p$ is true and $q$ is false. In all other cases, it is true.

Statement (A): The premise $3+3=7$ is false and the conclusion $4+3=8$ is false. Since a false premise implies anything, $F \rightarrow F$ is True. Thus, (A) is True.

Statement (B): The premise $5+3=8$ is true and the conclusion "earth is flat" is false. Since $T \rightarrow F$ is False, statement (B) is False.

Statement (C): The premise is "both (A) and (B) are true". Since (B) is false, this premise is false. The conclusion $5+6=17$ is also false. Since $F \rightarrow F$ is True, statement (C) is True.

Therefore, (A) and (C) are true while (B) is false.

Answer: (A) and (C) are true while (B) is false.

</details>

---

### Q121. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the statements $p, q$ and $r$ have the truth values $F, T, F$ respectively, then the truth values of the statement patterns $(p \wedge \sim q) \rightarrow r$ and $(p \vee q) \rightarrow r$ are respectively

**Options:**

- **(A)** $\mathrm{T}, \mathrm{T}$
- **(B)** $\mathrm{T}, \mathrm{F}$
- **(C)** $\mathrm{F}, \mathrm{T}$
- **(D)** F, F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{T}, \mathrm{F}$**

**Detailed Solution:**

Given the truth values $p = F$, $q = T$, and $r = F$.

For the first statement pattern $(p \wedge \sim q) \rightarrow r$:
Substituting the truth values, we get $(F \wedge \sim T) \rightarrow F$.
Since $\sim T = F$, this becomes $(F \wedge F) \rightarrow F$.
As $F \wedge F = F$, the expression simplifies to $F \rightarrow F$, which evaluates to $T$.

For the second statement pattern $(p \vee q) \rightarrow r$:
Substituting the truth values, we get $(F \vee T) \rightarrow F$.
As $F \vee T = T$, the expression simplifies to $T \rightarrow F$, which evaluates to $F$.

The truth values of the given statement patterns are $T$ and $F$ respectively.

Answer: $\mathrm{T}, \mathrm{F}$

</details>

---

### Q122. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The inverse of $[p \wedge(\sim q)] \rightarrow r$ is

**Options:**

- **(A)** $\sim \mathrm{r} \rightarrow(\sim \mathrm{p} \vee \mathrm{q})$
- **(B)** $\mathrm{r} \rightarrow(\sim \mathrm{p} \wedge \sim \mathrm{q})$
- **(C)** $(\sim p \vee q) \rightarrow \sim r$
- **(D)** $\mathrm{r} \rightarrow(\mathrm{p} \wedge \mathrm{q})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\sim p \vee q) \rightarrow \sim r$**

**Detailed Solution:**

The given statement is $[p \wedge (\sim q)] \rightarrow r$.

The inverse of a conditional statement $X \rightarrow Y$ is $\sim X \rightarrow \sim Y$.

Here, $X = p \wedge (\sim q)$ and $Y = r$.

The inverse is $\sim [p \wedge (\sim q)] \rightarrow \sim r$.

By De Morgan's law, $\sim [p \wedge (\sim q)] \equiv \sim p \vee \sim (\sim q) \equiv \sim p \vee q$.

Thus, the inverse is $(\sim p \vee q) \rightarrow \sim r$.

Answer: $(\sim p \vee q) \rightarrow \sim r$

</details>

---

### Q123. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $(p \wedge \sim q) \wedge(p \wedge r) \rightarrow \sim p \vee q$ is false, then the truth values of $p, q$ and $r$ are respectively

**Options:**

- **(A)** $\mathrm{T}, \mathrm{T}, \mathrm{T}$
- **(B)** F, F, F
- **(C)** T, F, T
- **(D)** $F, T, F$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) T, F, T**

**Detailed Solution:**

The given statement is $(p \wedge \sim q) \wedge (p \wedge r) \rightarrow \sim p \vee q$.

A conditional statement $X \rightarrow Y$ is false if and only if $X$ is true and $Y$ is false.

Therefore, $(p \wedge \sim q) \wedge (p \wedge r)$ must be true and $\sim p \vee q$ must be false.

For $\sim p \vee q$ to be false, both $\sim p$ and $q$ must be false. This implies that $p$ is true (T) and $q$ is false (F).

For $(p \wedge \sim q) \wedge (p \wedge r)$ to be true, both $p \wedge \sim q$ and $p \wedge r$ must be true.

Since $p$ is true, for $p \wedge r$ to be true, $r$ must be true (T).

Thus, the truth values of $p, q$, and $r$ are T, F, and T respectively.

Answer: T, F, T

</details>

---

### Q124. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The statement pattern $[p \wedge(q \vee r)] \vee[\sim r \wedge \sim q \wedge p]$ is equivalent to

**Options:**

- **(A)** $q \vee r$
- **(B)** $\mathrm{p} \vee \mathrm{r}$.
- **(C)** q
- **(D)** p

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) p**

**Detailed Solution:**

The given statement pattern is $[p \wedge (q \vee r)] \vee [\sim r \wedge \sim q \wedge p]$.

Using the commutative law, we can rewrite the second term:

$[p \wedge (q \vee r)] \vee [p \wedge (\sim q \wedge \sim r)]$

Applying De Morgan's law to $(\sim q \wedge \sim r)$, we get $\sim (q \vee r)$:

$[p \wedge (q \vee r)] \vee [p \wedge \sim (q \vee r)]$

Using the distributive law, we can factor out $p$:

$p \wedge [(q \vee r) \vee \sim (q \vee r)]$

By the complement law, $(q \vee r) \vee \sim (q \vee r)$ is a tautology $T$.

Substituting this back, we get:

$p \wedge T$

By the identity law, $p \wedge T$ is equivalent to $p$.

Answer: p

</details>

---

### Q125. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\sim[(p \vee \sim q) \rightarrow(p \wedge \sim q)] \equiv$

**Options:**

- **(A)** $(p \wedge \sim q) \wedge(\sim p \vee q)$
- **(B)** $(p \wedge \sim q) \wedge(\sim p \wedge q)$
- **(C)** $(p \vee \sim q) \wedge(\sim p \vee q)$
- **(D)** $(p \vee \sim q) \vee(\sim p \vee q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(p \vee \sim q) \wedge(\sim p \vee q)$**

**Detailed Solution:**

Using the property of implication, $A \rightarrow B \equiv \sim A \vee B$.

The negation of implication is $\sim(A \rightarrow B) \equiv A \wedge \sim B$.

Let $A = p \vee \sim q$ and $B = p \wedge \sim q$.

The given expression is $\sim(A \rightarrow B)$, which is equivalent to $A \wedge \sim B$.

Substituting $A$ and $B$, we get $(p \vee \sim q) \wedge \sim(p \wedge \sim q)$.

Using De Morgan's law, $\sim(p \wedge \sim q) \equiv \sim p \vee q$.

Therefore, the expression is equivalent to $(p \vee \sim q) \wedge (\sim p \vee q)$.

Answer: $(p \vee \sim q) \wedge(\sim p \vee q)$

</details>

---

### Q126. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Consider the following statements p : the switch $\mathrm{S}_1$ is closed. q : the switch $\mathrm{S}_2$ is closed.
$r$ : the switch $\mathrm{S}_3$ is closed.
Then the switching circuit represented by the statement $(\mathrm{p} \wedge \mathrm{q}) \vee(\sim \mathrm{p} \wedge(\sim \mathrm{q} \vee \mathrm{p} \vee \mathrm{r}))$ is

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/9Q9z1uPAYCBliDjbiOA0fzLkQgdtW3OIffS0rLTQHac.original.fullsize_2.png"/>
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/8bJYK6j_IG2H2zBsqvdNHKvAs52Cy8GO0QGpqQf01jw.original.fullsize_2.png"/>
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/ib-8v9whkr-ZM3QMufcAHA7tbma19rBE-IUlMSUTiKk.original.fullsize_2.png"/>
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/i09kq0PcbmNsV1dX4Hrh-zA2hQ6zea1gUQNhhcyTsoY.original.fullsize_2.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/ib-8v9whkr-ZM3QMufcAHA7tbma19rBE-IUlMSUTiKk.original.fullsize_2.png"/>**

**Detailed Solution:**

The given logical statement is $(p \wedge q) \vee (\sim p \wedge (\sim q \vee p \vee r))$.

The $\vee$ operator between $(p \wedge q)$ and $\sim p \wedge (\sim q \vee p \vee r)$ indicates two main branches connected in parallel.

The first branch $(p \wedge q)$ represents switches $S_1$ and $S_2$ connected in series.

The second branch $\sim p \wedge (\sim q \vee p \vee r)$ represents switch $S_1'$ connected in series with a parallel combination of three switches.

The expression $(\sim q \vee p \vee r)$ represents switches $S_2'$, $S_1$, and $S_3$ connected in parallel.

Comparing this with the given options, the third circuit diagram matches this arrangement perfectly. The upper branch contains $S_1$ and $S_2$ in series, and the lower branch contains $S_1'$ in series with a parallel group of $S_2'$, $S_1$, and $S_3$.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/ib-8v9whkr-ZM3QMufcAHA7tbma19rBE-IUlMSUTiKk.original.fullsize_2.png"/>

</details>

---

### Q127. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If p and q are statements, then $\qquad$ is a contingency.

**Options:**

- **(A)** $\mathrm{p} \wedge \sim \mathrm{p}$
- **(B)** $\mathrm{p} \vee \sim \mathrm{p}$
- **(C)** $\mathrm{p} \vee \mathrm{q}$
- **(D)** $(\mathrm{p} \wedge(\mathrm{p} \rightarrow \mathrm{q})) \rightarrow \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{p} \vee \mathrm{q}$**

**Detailed Solution:**

A contingency is a proposition that is neither a tautology nor a contradiction.

Evaluating the given options:

$p \wedge \sim p$ is always false, hence it is a contradiction.

$p \vee \sim p$ is always true, hence it is a tautology.

$p \vee q$ can be true or false depending on the truth values of $p$ and $q$. For example, if $p$ is true and $q$ is true, $p \vee q$ is true. If $p$ is false and $q$ is false, $p \vee q$ is false. Thus, it is a contingency.

$(p \wedge (p \rightarrow q)) \rightarrow q \equiv (p \wedge (\sim p \vee q)) \rightarrow q \equiv (p \wedge q) \rightarrow q \equiv \sim(p \wedge q) \vee q \equiv \sim p \vee \sim q \vee q \equiv \sim p \vee T \equiv T$. This is a tautology.

Therefore, $p \vee q$ is a contingency.

Answer: $\mathrm{p} \vee \mathrm{q}$

</details>

---

### Q128. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which one of the following is the pair of equivalent circuits?
i. <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/MbmTgGFjmWsfKLDcsiHMsmYHh1I6Vt4Jv5WKfiI_8HA.original.fullsize.png"/>
ii.<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/QKLtKR_WcrnT8j5gANUWGJcCh-kWrMEUSLVe5eNOkhU.original.fullsize.png"/>
iii.<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/ocg70W1Uen--kUHaf4-hiSSfEvfqI97s-04W6lZkHDs.original.fullsize.png"/>
iv.<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/5CV2EHOcxHlzu8y9JiRzT4n3SKwCh7V34Tb8hyRSiTo.original.fullsize.png"/>
v.<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/JeEiaBIX03tkrvYDl9W7waSmKcpuQBHcARQUVrpjv8Q.original.fullsize.png"/>

**Options:**

- **(A)** (i) and (ii)
- **(B)** (ii) and (iv)
- **(C)** (iii) and (v)
- **(D)** (i) and (iii)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (i) and (iii)**

**Detailed Solution:**

Let us determine the Boolean expression for each circuit by representing series connections with AND ($	ext{$\land$}$) and parallel connections with OR ($	ext{$\lor$}$).

For circuit (i):
The upper branch has switches $S_1$ and $S_2$ in series, which gives $S_1 \land S_2$.
The lower branch has switches $S_1$ and $S_3$ in series, which gives $S_1 \land S_3$.
These two branches are in parallel, so the equivalent expression is:
$Y_1 = (S_1 \land S_2) \lor (S_1 \land S_3)$
Using the distributive law, this simplifies to:
$Y_1 = S_1 \land (S_2 \lor S_3)$

For circuit (ii):
The upper branch has switch $S_1$.
The lower branch has switches $S_2$ and $S_3$ in series, giving $S_2 \land S_3$.
These branches are in parallel, so the expression is:
$Y_2 = S_1 \lor (S_2 \land S_3)$

For circuit (iii):
Switches $S_2$ and $S_3$ are in parallel, giving $(S_2 \lor S_3)$.
This combination is in series with switch $S_1$, so the expression is:
$Y_3 = S_1 \land (S_2 \lor S_3)$

For circuit (iv):
All three switches are in series, so the expression is:
$Y_4 = S_1 \land S_2 \land S_3$

For circuit (v):
The upper branch has $S_1$ and $S_2$ in series, giving $S_1 \land S_2$.
The lower branch has switch $S_3$.
These branches are in parallel, so the expression is:
$Y_5 = (S_1 \land S_2) \lor S_3$

Comparing the Boolean expressions, we get $Y_1 = Y_3$. Therefore, circuits (i) and (iii) are equivalent.

Answer: (i) and (iii)

</details>

---

### Q129. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of contrapositive of the statement $\mathrm{p} \rightarrow(\sim \mathrm{q} \wedge \mathrm{r})$ is

**Options:**

- **(A)** $(\sim q \vee \sim r) \wedge \sim p$
- **(B)** $(q \vee \sim r) \wedge p$
- **(C)** $(q \wedge \sim r) \vee p$
- **(D)** $\quad(\sim q \wedge \sim r) \vee \sim p$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(q \vee \sim r) \wedge p$**

**Detailed Solution:**

Let the given statement be $A \rightarrow B$, where $A = p$ and $B = \sim q \wedge r$.

The contrapositive of $A \rightarrow B$ is $\sim B \rightarrow \sim A$.

The negation of the contrapositive is $\sim(\sim B \rightarrow \sim A)$.

Using the logical equivalence $\sim(X \rightarrow Y) \equiv X \wedge \sim Y$, we get:

$\sim(\sim B \rightarrow \sim A) \equiv \sim B \wedge \sim(\sim A) \equiv \sim B \wedge A$

Substituting $A = p$ and $B = \sim q \wedge r$, we obtain:

$\sim(\sim q \wedge r) \wedge p$

Using De Morgan's law, $\sim(\sim q \wedge r) \equiv q \vee \sim r$.

Therefore, the required statement is $(q \vee \sim r) \wedge p$.

Answer: $(q \vee \sim r) \wedge p$

</details>

---

### Q130. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If statement I : If the work is not finished on time, the contractor is in trouble.
statement II : Either the work is finished on time or the contractor is in trouble. then

**Options:**

- **(A)** statement II is negation of statement I.
- **(B)** statement II is converse of statement I.
- **(C)** statement II and statement I are equivalent.
- **(D)** statement II is an inverse of statement I.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) statement II and statement I are equivalent.**

**Detailed Solution:**

Let $p$ be the statement "The work is finished on time".
Let $q$ be the statement "The contractor is in trouble".

Statement I can be written as: $\sim p \rightarrow q$
Statement II can be written as: $p \vee q$

Using the logical equivalence $A \rightarrow B \equiv \sim A \vee B$, we can rewrite Statement I as:
$\sim p \rightarrow q \equiv \sim(\sim p) \vee q \equiv p \vee q$

Since both statements reduce to $p \vee q$, Statement I and Statement II are logically equivalent.

Answer: statement II and statement I are equivalent.

</details>

---

### Q131. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the statement $p \vee \sim(q \wedge r)$ is false; then the truth values of $p, q$ and $r$ are respectively

**Options:**

- **(A)** $\mathrm{F}, \mathrm{T}, \mathrm{F}$
- **(B)** $\mathrm{F}, \mathrm{T}, \mathrm{T}$
- **(C)** $T, F, F$
- **(D)** $F, F, T$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{F}, \mathrm{T}, \mathrm{T}$**

**Detailed Solution:**

The given statement is $p \vee \sim(q \wedge r)$.

It is given that this statement is false.

A disjunction $A \vee B$ is false if and only if both $A$ and $B$ are false.

Therefore, $p$ is false and $\sim(q \wedge r)$ is false.

Since $\sim(q \wedge r)$ is false, $q \wedge r$ must be true.

A conjunction $A \wedge B$ is true if and only if both $A$ and $B$ are true.

Therefore, $q$ is true and $r$ is true.

The truth values of $p, q$, and $r$ are F, T, and T respectively.

Answer: $\mathrm{F}, \mathrm{T}, \mathrm{T}$

</details>

---

### Q132. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement $[\mathrm{p} \wedge(\mathrm{q} \vee \mathrm{r})] \vee[\sim \mathrm{r} \wedge \sim \mathrm{q} \wedge \mathrm{p}]$ is equivalent to

**Options:**

- **(A)** $\sim r$
- **(B)** $p$
- **(C)** $\sim q$
- **(D)** $q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $p$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/QFG4GJQRANkyIVA8J0Z5XOMeM6_dSkMRJtlNJ55V_g4.original.fullsize.png">

</details>

---

### Q133. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the statement $\mathrm{p} \leftrightarrow(\mathrm{q} \rightarrow \mathrm{p})$ is false, then true statement/statement pattern is

**Options:**

- **(A)** $\mathrm{p}$
- **(B)** $\mathrm{p} \rightarrow(\mathrm{p} \vee \sim \mathrm{q})$
- **(C)** $\mathrm{p} \wedge(\sim \mathrm{p} \wedge \mathrm{q})$
- **(D)** $(p \vee \sim q) \rightarrow p$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{p} \rightarrow(\mathrm{p} \vee \sim \mathrm{q})$**

**Detailed Solution:**

$\mathrm{p} \leftrightarrow(\mathrm{q} \rightarrow \mathrm{p})$ is false $\Rightarrow \mathrm{p} \equiv \mathrm{F}$ and $\mathrm{q} \equiv \mathrm{F}$ Consider option (B),
$\begin{aligned}
\mathrm{p} \rightarrow(\mathrm{p} \vee \sim \mathrm{q}) & \equiv \mathrm{F} \rightarrow(\mathrm{F} \vee \sim \mathrm{F}) \\
& \equiv \mathrm{F} \rightarrow(\mathrm{F} \vee \mathrm{T}) \\
& \equiv \mathrm{F} \rightarrow \mathrm{T} \\
& \equiv \mathrm{T}
\end{aligned}$

</details>

---

### Q134. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The statement $[(\mathrm{p} \rightarrow \mathrm{q}) \wedge \sim \mathrm{q}] \rightarrow \mathrm{r}$ is a tautology, when $\mathrm{r}$ is equivalent to

**Options:**

- **(A)** $\mathrm{p} \wedge \sim \mathrm{q}$
- **(B)** $q \vee p$
- **(C)** $\mathrm{p} \wedge \mathrm{q}$
- **(D)** $\sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sim q$**

**Detailed Solution:**

\begin{array}{|c|c|c|c|c|c|c|}
\hline \mathrm{p} & \mathrm{q} & \mathrm{r} & \mathrm{p} \rightarrow \mathrm{q} & \sim \mathrm{q} & (\mathrm{p} \rightarrow \mathrm{q}) \wedge \sim \mathrm{q} & {[(\mathrm{p} \rightarrow \mathrm{q}) \wedge \sim \mathrm{q}] \rightarrow \mathrm{r}} \\
\hline \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\hline \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\hline
\end{array}
$\therefore \quad[(p \rightarrow q) \wedge \sim q] \rightarrow r$ is a tautology when all the entries in the last column are $T$, which is only possible when $r \equiv \sim q$

</details>

---

### Q135. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement "The number is an odd number if and only if it is divisible by $3$ . "

**Options:**

- **(A)** (A) The number is an odd number but not divisible by 3 or the number is divisible by 3 but not odd.
- **(B)** The number is not an odd number iff it is not divisible by 3 .
- **(C)** The number is not an odd number but it is divisible by 3 .
- **(D)** The number is not an odd number or is not divisible by 3 but the number is divisible by $3$ or odd.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (A) The number is an odd number but not divisible by 3 or the number is divisible by 3 but not odd.**

**Detailed Solution:**

Let $\mathrm{p}$ : The number is an odd number,
$\mathrm{q}:$ The number is divisible by 3
$$
\sim(p \leftrightarrow q) \equiv(p \wedge \sim q) \vee(q \wedge \sim p)
$$
$\therefore \quad$ The negation of the given statement is "The number is an odd number but not divisible by 3 or the number is divisible by 3 but not odd'.

</details>

---

### Q136. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{q}$ is false and $\mathrm{p} \wedge \mathrm{q} \leftrightarrow \mathrm{r}$ is true, then is a tautology.

**Options:**

- **(A)** $\mathrm{p} \vee \mathrm{r}$
- **(B)** $(\mathrm{p} \wedge \mathrm{r}) \rightarrow \mathrm{p} \vee \mathrm{r}$
- **(C)** $(\mathrm{p} \vee \mathrm{r}) \rightarrow \mathrm{p} \wedge \mathrm{r}$
- **(D)** $\mathrm{p} \wedge \mathrm{r}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\mathrm{p} \wedge \mathrm{r}) \rightarrow \mathrm{p} \vee \mathrm{r}$**

**Detailed Solution:**

$\mathrm{q}$ is false and $\mathrm{p} \wedge \mathrm{q} \leftrightarrow \mathrm{r}$ is true
$\Rightarrow p \wedge q \equiv F$ and $r \equiv F$
$\Rightarrow \mathrm{p} \equiv \mathrm{T}$ or $\mathrm{F}, \mathrm{q} \equiv \mathrm{F}$ and $\mathrm{r} \equiv \mathrm{F}$
(1) $\mathrm{p} \vee \mathrm{r} \equiv \mathrm{T}$ or $\mathrm{F}$
(2) $(\mathrm{p} \wedge \mathrm{r}) \rightarrow(\mathrm{p} \vee \mathrm{r}) \equiv \mathrm{F} \rightarrow(\mathrm{T}$ or $\mathrm{F}) \equiv \mathrm{T}$
(3) $(\mathrm{p} \vee \mathrm{r}) \rightarrow(\mathrm{p} \wedge \mathrm{r}) \equiv(\mathrm{T}$ or $\mathrm{F}) \rightarrow \mathrm{F} \equiv \mathrm{T}$ or $\mathrm{F}$
(4) $\mathrm{p} \wedge \mathrm{r} \equiv \mathrm{F}$

</details>

---

### Q137. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Negation of contrapositive of statement pattern $(p \vee \sim q) \rightarrow(p \wedge \sim q)$ is

**Options:**

- **(A)** $(\sim p \wedge q) \vee(p \wedge \sim q)$
- **(B)** $(\sim \mathrm{p} \vee \mathrm{q}) \wedge(\mathrm{p} \vee \sim \mathrm{q})$
- **(C)** $(p \wedge \sim q) \vee(\sim p \wedge \sim q)$
- **(D)** $(\sim \mathrm{p} \vee \sim \mathrm{q}) \wedge(\mathrm{p} \vee \mathrm{q})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\sim \mathrm{p} \vee \mathrm{q}) \wedge(\mathrm{p} \vee \sim \mathrm{q})$**

**Detailed Solution:**

Contrapositive of $(p \vee \sim q) \rightarrow(p \wedge \sim q)$ is
$\sim(p \wedge \sim q) \rightarrow \sim(p \vee \sim q)$
$\begin{aligned} & \equiv \sim[\sim(p \wedge \sim q)] \vee \sim(p \vee \sim q) \ldots[p \rightarrow q \equiv \sim p \vee q] \\ & \equiv(p \wedge \sim q) \vee(\sim p \wedge q) \quad \ldots[\text { De Morgan's law] }\end{aligned}$
Negation of contrapositive of
$(p \vee \sim q) \rightarrow(p \wedge \sim q)$ is
$\sim[(p \wedge \sim q) \vee(\sim p \wedge q)]$
$\begin{array}{ll}\equiv \sim(p \wedge \sim q) \wedge \sim(\sim p \wedge q) & \ldots[\text { [De Morgan's law] } \\ \equiv(\sim p \vee q) \wedge(p \vee \sim q) & \ldots[\text { De Morgan's law] }\end{array}$

</details>

---

### Q138. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Negation of inverse of the following statement pattern $(p \wedge q) \rightarrow(p \vee \sim q)$ is

**Options:**

- **(A)** $\mathrm{p}$
- **(B)** $\sim q$
- **(C)** $\sim p$
- **(D)** $\mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sim q$**

**Detailed Solution:**

Inverse of $(p \wedge q) \rightarrow(p \vee \sim q)$ is
$$
\begin{aligned}
& \sim(p \wedge q) \rightarrow \sim(p \vee \sim q) \\
& \equiv \sim[\sim(p \wedge q)] \vee \sim(p \vee \sim q) \ldots[p \rightarrow q \equiv \sim p \vee q]
\end{aligned}
$$
$$
\begin{aligned}
& \equiv(p \wedge q) \vee(\sim p \wedge q)...[De Morgan's law]\\
& \equiv(q \wedge p) \vee(q \wedge \sim p)...[Commutative law] \\
& \equiv q \wedge(p \vee \sim p)...[Distributive law] \\
& \equiv q \wedge T...[Complement law] \\
& \equiv q...[Identity law]
\end{aligned}
$$
$\therefore \quad$ Negation of inverse of $(p \wedge q) \rightarrow(p \vee \sim q)$ is $\sim q$

</details>

---

### Q139. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The expression $(p \wedge \sim q) \vee q \vee(\sim p \wedge q)$ is equivalent to

**Options:**

- **(A)** $\sim p \vee q$
- **(B)** $p \wedge q$
- **(C)** $\mathrm{p} \vee \mathrm{q}$
- **(D)** $\mathrm{p} \vee \sim \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{p} \vee \mathrm{q}$**

**Detailed Solution:**

$$
\begin{aligned}
& (p \wedge \sim q) \vee q \vee(\sim p \wedge q) \\
& \equiv[(p \vee q) \wedge(\sim q \vee q)] \vee(\sim p \wedge q)
\end{aligned}
$$
...[Distributive law]
$$
\begin{aligned}
& \equiv[(p \vee q) \wedge T] \vee(\sim p \wedge q) \ldots[\text { Complement law] } \\
& \equiv(p \vee q) \vee(\sim p \wedge q) \\
& \equiv(p \vee q \vee \sim p) \wedge(p \vee q \vee q)
\end{aligned}
$$
...[Distributive law]
$$
\equiv(T \vee q) \wedge(p \vee q)
$$
...[Complement law and Idempotent law]
$$
\begin{aligned}
& \equiv T \wedge(p \vee q) \\
& \equiv p \vee q
\end{aligned}
$$
$\therefore$ [Identity law]
...[Identity law]

</details>

---

### Q140. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let
Statement 1 : If a quadrilateral is a square, then all of its sides are equal.

Statement 2: All the sides of a quadrilateral are equal, then it is a square.

**Options:**

- **(A)** Statement 2 is contrapositive of statement 1.
- **(B)** Statement 2 is negation of statement 1 .
- **(C)** Statement 2 is inverse of statement 1.
- **(D)** Statement 2 is the converse of statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 2 is the converse of statement 1.**

**Detailed Solution:**

Let p: A quadrilateral is a square
$q$ : All sides of quadrilateral are equal.
$\therefore \quad$ Statement 1 is $\mathrm{p} \rightarrow \mathrm{q}$,
Statement 2 is $\mathrm{q} \rightarrow \mathrm{p}$
$\therefore \quad$ Statement 2 is the converse of statement 1.

</details>

---

### Q141. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The contrapositive of "If $x$ and $y$ are integers such that $x y$ is odd, then both $x$ and $y$ are odd" is

**Options:**

- **(A)** If both $x$ and $y$ are odd integers, then $x y$ is odd.
- **(B)** If both $x$ and $y$ are even integers, then $x y$ is even.
- **(C)** If $x$ or $y$ is an odd integer, then $x y$ is odd.
- **(D)** If both $x$ and $y$ are not odd integers, then the product $x y$ is not odd.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If both $x$ and $y$ are not odd integers, then the product $x y$ is not odd.**

**Detailed Solution:**

Let $\mathrm{p}: x$ and $y$ are integers such that $x y$ is odd. $\mathrm{q}:$ both $x$ and $y$ are odd.
$\therefore \quad$ Given statement is $\mathrm{p} \rightarrow \mathrm{q}$
$\therefore \quad$ Its contrapositive is $\sim q \rightarrow p$
$\therefore \quad$ Option (D) is correct.

</details>

---

### Q142. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The inverse of the statement
"If the surface area increase, then the pressure decreases.", is

**Options:**

- **(A)** If the surface area does not increase, then the pressure does not decrease.
- **(B)** If the pressure decreases, then the surface area increases.
- **(C)** If the pressure does not decreases, then the surface area does not increase.
- **(D)** If the surface area does not increase, then the pressure decreases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) If the surface area does not increase, then the pressure does not decrease.**

**Detailed Solution:**

Let $\mathrm{p}$ : The surface area increases
$q$ : The pressure decreases
Given statement is $\mathrm{p} \rightarrow \mathrm{q}$
$\therefore \quad$ It's inverse is $\sim \mathrm{p} \rightarrow \sim \mathrm{q}$
$\therefore \quad$ Option (A) is correct.

</details>

---

### Q143. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If truth value of logical statement $(p \leftrightarrow \sim q) \rightarrow(\sim p \wedge q)$ is false, then the truth values of $\mathrm{p}$ and $\mathrm{q}$ are respectively

**Options:**

- **(A)** $\mathrm{F}, \mathrm{T}$
- **(B)** $\mathrm{T}, \mathrm{T}$
- **(C)** $\mathrm{T}, \mathrm{F}$
- **(D)** $\mathrm{F}, \mathrm{F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{T}, \mathrm{F}$**

**Detailed Solution:**

As $(p \leftrightarrow \sim q) \rightarrow(\sim p \wedge q)$ is false, we get $p \leftrightarrow \sim q \equiv T$ and $\sim p \wedge q \equiv F$
$\sim p \wedge q=F$
$\Rightarrow \sim \mathrm{p} \equiv \mathrm{F}$ and $\mathrm{q} \equiv \mathrm{F}$
$\Rightarrow \mathrm{p} \equiv \mathrm{T}$ and $\mathrm{q} \equiv \mathrm{F}$

</details>

---

### Q144. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The logical statement $(\sim(\sim \mathrm{p} \vee \mathrm{q}) \vee(\mathrm{p} \wedge \mathrm{r})) \wedge(\sim \mathrm{q} \wedge \mathrm{r})$ is equivalent to

**Options:**

- **(A)** $\sim \mathrm{p} \vee \mathrm{r}$
- **(B)** $(p \wedge \sim q) \vee r$
- **(C)** $(\mathrm{p} \wedge \mathrm{r}) \wedge \sim \mathrm{q}$
- **(D)** $(\sim p \wedge \sim q) \wedge r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\mathrm{p} \wedge \mathrm{r}) \wedge \sim \mathrm{q}$**

**Detailed Solution:**

$\begin{aligned}
& {[\sim(\sim p \vee q) \vee(p \wedge r)] \wedge(\sim q \wedge r)} \\
& \equiv[(p \wedge \sim q) \vee(p \wedge r)] \wedge(\sim q \wedge r) & \Rightarrow \ldots[\text { De Morgan's law }]
\end{aligned}$
$\equiv \mathrm{p} \wedge(\sim \mathrm{q} \vee \mathrm{r}) \wedge(\sim \mathrm{q} \wedge \mathrm{r}) \quad \ldots[$ Distributive law $]$
$\equiv p \wedge[(\sim q \vee r) \wedge \sim q] \wedge r^{\prime} .. [\text { Associative law] }$
$\equiv \mathrm{p} \wedge(\sim \mathrm{q}) \wedge\mathrm{r} \quad \ldots[$ Absórption law]
$\equiv(p \wedge r) \wedge \sim q$
.. [Commutative and Associative law]

</details>

---

### Q145. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $\mathrm{p} \rightarrow \sim(\mathrm{p} \wedge \sim \mathrm{q})$ is equivalent to

**Options:**

- **(A)** $\mathrm{q}$
- **(B)** $(\sim p) \vee q$
- **(C)** $(\sim p) \wedge q$
- **(D)** $(\sim p) \vee(\sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\sim p) \vee q$**

**Detailed Solution:**

$$
\begin{aligned}
& p \rightarrow \sim(p \wedge \sim q) \\
& \equiv \sim p \vee \sim(p \wedge \sim q) \\
& \equiv \sim p \vee(\sim p \vee q) \\
& \equiv(\sim p \vee \sim p) \vee q \\
& \equiv \sim p \vee q
\end{aligned}
$$
$\ldots[\because \mathrm{p} \rightarrow \mathrm{q} \equiv \sim \mathrm{p} \vee \mathrm{q}]$
...[De Morgan's law]
...[Associative law]
...[Idempotent law]

</details>

---

### Q146. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement pattern $\sim \mathrm{S} \vee(\sim \mathrm{r} \wedge \mathrm{s})$ is equivalent to

**Options:**

- **(A)** $\mathrm{s} \wedge \mathrm{r}$
- **(B)** $\mathrm{s} \wedge(\mathrm{r} \wedge \sim \mathrm{s})$
- **(C)** $\mathrm{s} \wedge \sim \mathrm{r}$
- **(D)** $\mathrm{S} \vee(\mathrm{r} \vee \sim \mathrm{s})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{s} \wedge \mathrm{r}$**

**Detailed Solution:**

$\begin{aligned}
& \sim(\sim s \vee(\sim r \wedge s)) \\
& \equiv s \wedge \sim(\sim r \wedge s)...[De Morgan's law] \\
& \equiv s \wedge(r \vee \sim s)......[De Morgan's law] \\
& \equiv(s \wedge r) \vee(s \wedge \sim s)...[Distributive law] \\
& \equiv(s \wedge r) \vee F...[Complement law] \\
& \equiv s \wedge r...[Identity law]
\end{aligned}$

</details>

---

### Q147. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{p}$ and $\mathrm{q}$ are true statements and $\mathrm{r}$ and $s$ are false statements, then the truth values of the statement patterns $(p \wedge q) \vee r$ and $(\mathrm{p} \vee \mathrm{s}) \leftrightarrow(\mathrm{q} \wedge \mathrm{r})$ are respectively

**Options:**

- **(A)** $\mathrm{F}, \mathrm{T}$
- **(B)** $\mathrm{T}, \mathrm{T}$
- **(C)** $\mathrm{F}, \mathrm{F}$
- **(D)** $\mathrm{T}, \mathrm{F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{T}, \mathrm{F}$**

**Detailed Solution:**

$\begin{array}{ll}(\mathrm{p} \wedge \mathrm{q}) \vee \mathrm{r} & (\mathrm{p} \vee \mathrm{s}) \leftrightarrow(\mathrm{q} \wedge \mathrm{r}) \\ \equiv(T \wedge \mathrm{T}) \vee \mathrm{F} & \equiv(\mathrm{T} \vee \mathrm{F}) \leftrightarrow(\mathrm{T} \wedge \mathrm{F}) \\ \equiv \mathrm{T} \vee \mathrm{F} & \equiv \mathrm{T} \leftrightarrow \mathrm{F} \\ \equiv \mathrm{T} & \equiv \mathrm{F}\end{array}$

</details>

---

### Q148. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The logical statement $[\sim(\sim \mathrm{p} \vee \mathrm{q}) \vee(\mathrm{p} \wedge \mathrm{r})] \wedge(\sim \mathrm{q} \wedge \mathrm{r})$ is equivalent to

**Options:**

- **(A)** $(p \wedge r) \wedge \sim q$
- **(B)** $(p \wedge \sim q) \vee r$
- **(C)** $\sim \mathrm{p} \vee \mathrm{r}$
- **(D)** $\sim \mathrm{p} \wedge \mathrm{r}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(p \wedge r) \wedge \sim q$**

**Detailed Solution:**

$\begin{aligned} & {[\sim(\sim p \vee q) \vee(p \wedge r)] \wedge(\sim q \wedge r)} \\ & \equiv[(p \wedge \sim q) \vee(p \wedge r)] \wedge(\sim q \wedge r) \\ & \text {...[De Morgan's law] } \\ & \equiv \mathrm{p} \wedge(\sim q \vee r) \wedge(\sim q \wedge r) \ldots \text {. [Distributive law] } \\ & \equiv \mathrm{p} \wedge[(\sim \mathrm{q} \vee \mathrm{r}) \wedge \sim \mathrm{q}] \wedge \mathrm{r} \ldots \text {... Associative law] } \\ & \equiv p \wedge(\sim q) \wedge r \quad \text {... [Absorption law] } \\ & \equiv(p \wedge r) \wedge \sim q \quad \ldots[\text { Commutative law }] \\ & \end{aligned}$

</details>

---

### Q149. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{p}, \mathrm{q}, \mathrm{r}$ be three statements, then $[\mathrm{p} \rightarrow(\mathrm{q} \rightarrow \mathrm{r})] \leftrightarrow[(\mathrm{p} \wedge \mathrm{q}) \rightarrow \mathrm{r}]$ is

**Options:**

- **(A)** equivalent to $\mathrm{p} \leftrightarrow \mathrm{q}$.
- **(B)** contingency.
- **(C)** tautology.
- **(D)** contradiction.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) tautology.**

**Detailed Solution:**

Given statement,
$\begin{aligned}
{[p \rightarrow(q \rightarrow r)] } & \leftrightarrow[(p \wedge q) \rightarrow r] \\
p \rightarrow(q \rightarrow r) & \equiv \sim p \vee(q \rightarrow r) \\
& \equiv \sim p \vee(\sim q \vee r) \\
& \equiv[(\sim p) \vee(-q)] \vee r ... [\text { Associative law}]\\
& \equiv \sim(p \wedge q) \vee r \quad \ldots[\text { De'morgans law }] \\
& \equiv p \wedge q \rightarrow r
\end{aligned}$
$\therefore$Given statement is tautology.

</details>

---

### Q150. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Negation of the statement
"The payment will be made if and only if the work is finished in time." Is

**Options:**

- **(A)** The work is finished in time and the payment is not made.
- **(B)** The payment is made and the work is not finished in time.
- **(C)** The work is finished in time and the payment is not made, or the payment is made and the work is finished in time.
- **(D)** Either the work is finished in time and the payment is not made, or the payment is made and the work is not finished in time.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Either the work is finished in time and the payment is not made, or the payment is made and the work is not finished in time.**

**Detailed Solution:**

Let $\mathrm{p}$ : Payment will be made
$q$ : Work is finished in time. Given statement is
$(p \rightarrow q) \wedge(q \rightarrow p)$
Negation of above statement is $(p \wedge \sim q) \vee(q \wedge \sim p)$
$\therefore$Option (D) is correct.

</details>

---

### Q151. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement $(p \wedge q) \rightarrow(\sim p \vee r)$ is

**Options:**

- **(A)** $\mathrm{p} \vee \mathrm{q} \vee \sim \mathrm{r}$
- **(B)** $\mathrm{p} \wedge \mathrm{q} \wedge \approx \mathrm{r}$
- **(C)** $\sim p \vee q \wedge r$
- **(D)** $\sim \mathrm{p} \vee \sim \mathrm{q} \vee \sim \mathrm{r}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{p} \wedge \mathrm{q} \wedge \approx \mathrm{r}$**

**Detailed Solution:**

$\begin{aligned} & \sim[(p \wedge q) \rightarrow(\sim p \vee r)] \\ & \equiv(p \wedge q) \wedge \sim(\sim p \vee r) \ldots[\because \sim(p \rightarrow q) \equiv p \wedge \sim q] \\ & \equiv p \wedge q \wedge p \wedge \sim r \quad \ldots[\text { Associative Law }] \\ & \equiv p \wedge q \wedge \sim r \quad \ldots[\text { Idempotent Law }]\end{aligned}$

</details>

---

### Q152. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If truth values of statements $p, q$ are true, and $r$, $s$ are false, then the truth values of the following statement patterns are respectively
$\mathrm{a}: \sim(\mathrm{p} \wedge \sim \mathrm{r}) \vee(\sim \mathrm{q} \vee \mathrm{s})$
$\mathrm{b}:(\sim \mathrm{q} \wedge \sim \mathrm{r}) \leftrightarrow(\mathrm{p} \vee \mathrm{s})$
$c:(\sim p \vee q) \rightarrow(r \wedge \sim s)$

**Options:**

- **(A)** $T,F,F$
- **(B)** $F,F,F$
- **(C)** $F,T,T$
- **(D)** $T,F,T$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $F,F,F$**

**Detailed Solution:**

a.
$\begin{aligned}
& \sim(\mathrm{p} \wedge \sim \mathrm{r}) \vee(\sim \mathrm{q} \vee \mathrm{s}) \\
& \equiv \sim(\mathrm{T} \wedge \sim \mathrm{F}) \vee(\sim \mathrm{T} \vee \mathrm{F}) \\
& \equiv(\mathrm{F} \vee \mathrm{F}) \vee(\mathrm{F} \vee \mathrm{F}) \\
& \equiv \mathrm{F} \vee \mathrm{F} \\
& \equiv \mathrm{F}
\end{aligned}$
b.
$\begin{aligned}
& (\sim \mathrm{q} \wedge \sim \mathrm{r}) \leftrightarrow(\mathrm{p} \vee \mathrm{s}) \\
& \equiv(\sim \mathrm{T} \wedge \sim \mathrm{F}) \leftrightarrow(\mathrm{T} \vee \mathrm{F}) \\
& \equiv \mathrm{F} \leftrightarrow \mathrm{T} \\
& \equiv \mathrm{F}
\end{aligned}$
c.
$\begin{aligned}
& (\sim p \vee q) \rightarrow(r \wedge \sim s) \\
& \equiv(\sim T \vee T) \rightarrow(F \wedge \sim F) \\
& \equiv(F \vee T) \rightarrow(F \wedge T) \\
& \equiv T \rightarrow F \\
& \equiv F
\end{aligned}$

</details>

---

### Q153. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The inverse of statement pattern $(p \vee q) \rightarrow(p \wedge q)$ is

**Options:**

- **(A)** $(\sim p \vee \sim q) \rightarrow(\sim p \wedge \sim q)$
- **(B)** $(p \wedge q) \rightarrow(p \vee q)$
- **(C)** $(p \wedge q) \rightarrow(p \vee q)$
- **(D)** $\sim(p \vee q) \rightarrow(p \wedge q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(p \wedge q) \rightarrow(p \vee q)$**

**Detailed Solution:**

$\begin{aligned} & \because \text { inverse of } p \rightarrow q \text { is } \sim p \rightarrow \sim q \\ & \Rightarrow \text { inverse of } p \vee q \rightarrow p \wedge q \\ & \equiv \sim(p \vee q) \rightarrow \sim(p \wedge q) \\ & \equiv(\sim p \wedge \sim q) \rightarrow(\sim p \vee \sim q)\end{aligned}$

</details>

---

### Q154. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $[p \rightarrow(q \rightarrow p)] \rightarrow[p \rightarrow(p \vee q)]$ is

**Options:**

- **(A)** A tautology
- **(B)** A contradiction
- **(C)** A contingency
- **(D)** Equivalent to $p \leftrightarrow q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A tautology**

**Detailed Solution:**

$p \rightarrow(q \rightarrow p)$ is a tautology
$p \rightarrow(p \vee q)$ is a tautology
Hence, $[p \rightarrow(q \rightarrow p)] \rightarrow[p \rightarrow(p \vee q)]$ is a tautology

</details>

---

### Q155. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For statement; If a quadrilateral $A B C D$ is a rhombus then its opposite sides are parallel", its contrapositive and converse are respectively given by

**Options:**

- **(A)** i. If opposite sides of a quadrilateral $A B C D$ are not parallel, then quadrilateral $A B C D$ is a rhombus.
ii. If opposite sides of a quadrilateral $A B C D$ are not parallel, then the quadrilateral $A B C D$ is a rhombus.
- **(B)** i. If opposite sides of a quadrilateral $A B C D$ are not parallel then quadrilateral $A B C D$ is not rhombus.
ii. If opposite sides of a quadrilateral $A B C D$ are parallel, then quadrilateral $A B C D$ is not rhombus.
- **(C)** i. If opposite sides of a quadrilateral $A B C D$ are parallel, then quadrilateral $A B C D$ is not a rhombus.
ii. If opposite sides of a quadrilateral $A B C D$ are parallel, then quadrilateral $A B C D$ is a rhombus.
- **(D)** i. If opposite sides of a quadrilateral $A B C D$ are parallel, then quadrilateral $A B C D$ is not a rhombus.
ii. If opposite sides of a quadrilateral $A B C D$ are not parallel, then quadrilateral $A B C D$ is a rhombus.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) i. If opposite sides of a quadrilateral $A B C D$ are parallel, then quadrilateral $A B C D$ is not a rhombus.
ii. If opposite sides of a quadrilateral $A B C D$ are parallel, then quadrilateral $A B C D$ is a rhombus.**

**Detailed Solution:**

Contrapositive of $p \rightarrow q$ is $\sim q \rightarrow \sim p$ and converse of $p \rightarrow q$ is $q \rightarrow p$ Hence, option (C) is correct

</details>

---

### Q156. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $p$ and $q$ each have truth value $F$, then the truth values of the statement patterns $(\sim p \vee q) \leftrightarrow \sim(p \wedge q)$ and $\quad \sim p \leftrightarrow(p \rightarrow \sim q)$ respectively are

**Options:**

- **(A)** $\mathrm{T}, \mathrm{F}$
- **(B)** $\mathrm{T}, \mathrm{T}$
- **(C)** $\mathrm{F}, \mathrm{T}$
- **(D)** $\mathrm{F}, \mathrm{F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{T}, \mathrm{T}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/xAnu9W20GKjgIeS71wlgqbMytBZOEgMlMG3PdNklURA.original.fullsize.png">

</details>

---

### Q157. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If statement I: If a quadrilateral $A B C D$ is a square, then all of its sides are equal.
Statement II: All the sides of a quadrilateral $A B C D$ are equal, then $A B C D$ is a square.
Then

**Options:**

- **(A)** statement II is an inverse of statement I.
- **(B)** statement II is a negation of statement I.
- **(C)** statement II is a converse of statement I.
- **(D)** statement II is a contrapositive of statement I.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) statement II is a converse of statement I.**

**Detailed Solution:**

Converse of $p \rightarrow q$ is $q \rightarrow p$
Hence, statement-II is converse of statement-I

</details>

---

### Q158. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $p: 25$ is an odd prime number.
$q: 14$ is a composite number and
$r: 64$ is a perfect square number.
Then which of the following statement pattern is true?

**Options:**

- **(A)** $\sim(q \wedge r) \vee p$
- **(B)** $(p \wedge q) \vee r$
- **(C)** $(p \vee q) \wedge(\sim r)$
- **(D)** $\sim p \vee(q \wedge r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sim p \vee(q \wedge r)$**

**Detailed Solution:**

Here, $P \equiv \mathrm{F}, q \equiv \mathrm{T}, r \equiv \mathrm{T}$
$\Rightarrow \sim p \vee(q \wedge r)$ is true

</details>

---

### Q159. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of statement ' I study or I fail' is

**Options:**

- **(A)** I study and I fail.
- **(B)** I do not study and I fail.
- **(C)** I study and I do not fail.
- **(D)** I do not study and I do not fail.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) I do not study and I do not fail.**

**Detailed Solution:**

$\because(p \vee q) \equiv \sim p \wedge \sim q$
$\Rightarrow$ Negation of I study or I fail
ミ I do not study and I do not fail

</details>

---

### Q160. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following is correct statement?
(a) $S_1:(p \wedge q) \equiv \sim(p \rightarrow \sim q)$.
(b) $S_2:(p \wedge q) \wedge(\sim p v \sim q)$ is tautology.
(c) $\left.S_3:[p \wedge(p \rightarrow \sim q)] \rightarrow q\right)$ is contradiction.
(d) $S_4: p \rightarrow(q \rightarrow p)$ is contingency.

**Options:**

- **(A)** Statement $S_3$ is correct,
- **(B)** Statement $S_1$ is correct,
- **(C)** Statement $S_1$ and $S_2$ are correct,
- **(D)** Statement $S_4$ is correct,

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement $S_1$ is correct,**

**Detailed Solution:**

$$
\begin{aligned}
& \because \sim(p \rightarrow q) \equiv p \wedge \sim q \\
& \Rightarrow \sim(p \rightarrow \sim q) \equiv p \wedge \sim(\sim q) \equiv p \wedge q
\end{aligned}
$$
Hence, $S_1$ is correct

</details>

---

### Q161. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$p$ and $q$ are two logical statements.
If $r: p \rightarrow(\sim p \vee q)$ has truth value false, then truth values of $p$ and $q$ are respectively

**Options:**

- **(A)** $\mathrm{T}, \mathrm{T}$
- **(B)** $\mathrm{T}, \mathrm{F}$
- **(C)** $\mathrm{F}, \mathrm{T}$
- **(D)** F, F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{T}, \mathrm{F}$**

**Detailed Solution:**

$p \rightarrow(\sim p \vee q)$ is false
$\Rightarrow(p$ is true $)$ and $(\sim p \vee q)$ is false
$\Rightarrow p$ is true and $q$ is false

</details>

---

### Q162. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of $\sim s \vee(\sim r \vee s)$ is equivalent to

**Options:**

- **(A)** $s \wedge r$
- **(B)** $\sim r \wedge s$
- **(C)** $s \wedge(r \wedge \sim s)$
- **(D)** $s \wedge(r \vee \sim s)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $s \wedge r$**

**Detailed Solution:**

$\begin{aligned} & \sim\{\sim s \vee(\sim r \wedge s)\} \equiv \sim(\sim s) \wedge\{\sim(\sim r \wedge s)\} \\ & \equiv s \wedge\{\sim(\sim r) \vee \sim s\} \\ & \equiv s \wedge\{r \vee \sim s\} \\ & \equiv(s \wedge r) \vee(s \wedge \sim s) \\ & \equiv(s \wedge r) \vee c \\ & \equiv(s \wedge r)\end{aligned}$

</details>

---

### Q163. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $\sim(p \leftrightarrow \sim q)$ is

**Options:**

- **(A)** equivalent to $(\sim p) \leftrightarrow q$
- **(B)** a tautology
- **(C)** a fallacy
- **(D)** equivalent to $(p \leftrightarrow q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) equivalent to $(p \leftrightarrow q)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/9bbEP9GJye1V8fC-CrlPeLm3FitNIjNJpEK_FIShoHM.original.fullsize.png">

Hence $\sim(p \leftrightarrow \sim q) \equiv p \leftrightarrow q$

</details>

---

### Q164. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider the following three statements
$P: 11$ is a prime number.
Q: 7 is a factor of 176 .
$R$ : LCM of 3 and 7 is 21 .
Then, the truth value of which one of the following statement is true?

**Options:**

- **(A)** $P \vee(\sim Q \wedge R)$
- **(B)** $(\sim P) \wedge(\sim Q \wedge R)$
- **(C)** $(P \wedge Q) \vee(\sim R)$
- **(D)** $(\sim P) \vee(Q \wedge R)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $P \vee(\sim Q \wedge R)$**

**Detailed Solution:**

$P: 11$ is a prime number $(\mathrm{T})$
$Q: 7$ is a factor of $176(\mathrm{~F})$
$R$ : L.C.M of 3 and 7 is 21 (T)
Now, $P \vee(\sim Q \wedge R) \equiv \mathrm{T} \vee(\mathrm{T} \wedge \mathrm{T}) \equiv \mathrm{T}$

</details>

---

### Q165. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $(p \wedge \sim r) \rightarrow(\sim p \vee q)$ has truth value ' $F$ ', then truth values of $p, q$ and $r$ are respectively

**Options:**

- **(A)** F,F,T
- **(B)** T,T,T
- **(C)** T,F,F
- **(D)** F,F,F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) T,F,F**

**Detailed Solution:**

$\because(p \wedge \sim r) \rightarrow(\sim p \vee q)$ has truth value $F$
$\Rightarrow(p \wedge \sim r)$ is $T$ and $(\sim p \vee q)$ is $F$
$\Rightarrow(P$ is $T$ and $\sim r$ is $T)$ and $(\sim p$ is $F$ and $q$ is $F)$
$\Rightarrow P$ is $T, r$ is $F$ and $q$ is $F$

</details>

---

### Q166. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $p: A$ man is happy, $q: A$ man is rich, then the symbolic form of ' $A$ man is neither happy nor rich' is

**Options:**

- **(A)** $\sim p \wedge q$
- **(B)** $\sim p \vee \sim q$
- **(C)** $p \vee q$
- **(D)** $\sim(p \vee q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sim(p \vee q)$**

**Detailed Solution:**

A man is neither happy nor rich
$\equiv$ (Man is not happy) and (Man is not rich)
$\equiv \sim P \wedge \sim q$ 
$\equiv \sim(P \vee q)$

</details>

---

### Q167. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $(p \wedge q) \vee(\sim p \wedge q) \vee(r \wedge \sim q)$ is logical equivalent to

**Options:**

- **(A)** $p \wedge r$
- **(B)** $q \wedge r$
- **(C)** $q \vee r$
- **(D)** $p \vee r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $q \vee r$**

**Detailed Solution:**

$\begin{aligned} & (p \wedge q) \vee(\sim p \wedge q) \vee(r \wedge \sim q) \\ & \equiv\{(p \vee \sim p) \wedge q\} \vee(r \wedge \sim q) \\ & \equiv(t \wedge q) \vee(r \wedge \sim q) \\ & \equiv q \vee(r \wedge \sim q) \\ & \equiv(q \vee r) \wedge(q \vee \sim q) \\ & \equiv(q \vee r) \wedge t \\ & \equiv q \vee r\end{aligned}$

</details>

---

### Q168. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let A, B, C and D be four nonempty sets. The contrapositive of 'if $A \subseteq B$ and $B \subseteq D$ then $A \subseteq C$ ' is

**Options:**

- **(A)** If $A \subseteq C$, then $A \subseteq B$ or $B \nsubseteq D$
- **(B)** If $A \subset C$, then $A \subseteq B$ and $B \subseteq D$
- **(C)** If $A \subseteq C$, then $A \subseteq B$ and $B \subseteq D$
- **(D)** If $\mathrm{A} \subseteq C$, then $\mathrm{B} \subset \mathrm{A}$ or $\mathrm{D} \subset \mathrm{B}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) If $A \subseteq C$, then $A \subseteq B$ or $B \nsubseteq D$**

**Detailed Solution:**

The contrapositive of $p \rightarrow q$ is $\sim q \rightarrow \sim p$
so, the required contrapositive is
If $A \nsubseteq C$, then $A \nsubseteq B$ or $B \nsubseteq D$

</details>

---

### Q169. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statement pattern is contradiction?

**Options:**

- **(A)** $S_3 \equiv(\sim p \wedge q) \wedge(\sim q)$
- **(B)** $S_2 \equiv(p \rightarrow q) \vee(p \wedge \sim q)$
- **(C)** $S_1 \equiv(\sim p \vee \sim q) \vee(p \vee \sim q)$
- **(D)** $S_4 \equiv(\sim p \wedge q) \vee(\sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $S_3 \equiv(\sim p \wedge q) \wedge(\sim q)$**

**Detailed Solution:**

$\begin{aligned} & S_3 \equiv(\sim p \wedge q) \wedge(\sim q) \\ & \equiv \sim p \wedge(q \wedge \sim q) \\ & \text { [Associative law] } \\ & \equiv \sim p \wedge c \\ & {[\because q \wedge \sim q \equiv c]} \\ & \equiv c \\ & {[\because p \wedge c \equiv c]} \\ & \end{aligned}$

</details>

---

### Q170. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the simple statements $p, q$, and $r, p \rightarrow(q \vee r)$ is logically equivalent to

**Options:**

- **(A)** $(p \vee q) \rightarrow r$
- **(B)** $(p \rightarrow q) \vee(p \rightarrow r)$
- **(C)** $(p \rightarrow \sim q) \wedge(p \rightarrow r)$
- **(D)** $(p \rightarrow q) \wedge(p \rightarrow \sim r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(p \rightarrow q) \vee(p \rightarrow r)$**

**Detailed Solution:**

$\begin{aligned} & P \rightarrow(q \vee r) \\ & \equiv \sim p \vee(q \vee r) \quad[\because p \rightarrow q \equiv \sim p \vee q] \\ & \equiv(\sim p \vee q) \vee(\sim p \vee r) \\ & \equiv(p \rightarrow q) \vee(p \rightarrow r)\end{aligned}$

</details>

---

### Q171. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement pattern $p v(q \rightarrow \sim r)$ is

**Options:**

- **(A)** $\sim p \wedge(\sim q \wedge r)$
- **(B)** $\sim p \wedge(\sim q \wedge \sim r)$
- **(C)** $\sim p \wedge(q \wedge \sim r)$
- **(D)** $\sim p \wedge(q \wedge r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sim p \wedge(q \wedge r)$**

**Detailed Solution:**

$\begin{aligned} & \sim\{p \vee(q \rightarrow \sim r)\} \equiv \sim p \wedge \sim(q \rightarrow \sim r)[\because \sim(p \rightarrow q) \equiv p \wedge \sim q] \\ & \equiv \sim p \wedge(q \wedge \sim(\sim r)) \\ & \equiv \sim p \wedge(q \wedge r)\end{aligned}$

</details>

---

### Q172. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $p: \forall \in N, n^2+n$ is an even number
$q: \forall n \in N, n^2-n$ is an odd number,
then the truth values of $p \wedge q, p \wedge q$ and $p \rightarrow q$ are respectively

**Options:**

- **(A)** $\mathrm{F}, \mathrm{T}, \mathrm{T}$
- **(B)** $\mathrm{F}, \mathrm{F}, \mathrm{T}$
- **(C)** F, T, F
- **(D)** $\mathrm{T}, \mathrm{T}, \mathrm{F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) F, T, F**

**Detailed Solution:**

$\because$ product of two natural numbers is an even natural number
Hence, $n^2+n=n(n+1)$ and $n^2-n=n(n-1)$ are even numbers
So, $p$ is true and $q$ is false
$\Rightarrow p \wedge q$ is false
and $p \vee q$ is true
and $p \rightarrow q$ is false

</details>

---

### Q173. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement "The payment will be made if and only if the work is finished in time" is

**Options:**

- **(A)** The work is finished in time and the payment is not made
- **(B)** Either the work finished in time and the payment is not made or the payment is made and the work is not finished in time
- **(C)** The payment is made and the work is not finished in time
- **(D)** The work is finished in time and the payment is not made or the payment is made and the work is finished in time

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Either the work finished in time and the payment is not made or the payment is made and the work is not finished in time**

**Detailed Solution:**

We know
$\sim(p \leftrightarrow q) \equiv(p \wedge \sim q) \vee(\sim p \wedge q)$
Hence option (B) is correct

</details>

---

### Q174. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The contrapositive of $(\sim \mathrm{p} \wedge \mathrm{q}) \rightarrow(\mathrm{q} \wedge \sim \mathrm{r})$ is

**Options:**

- **(A)** $(\mathrm{p} \vee \sim \mathrm{q}) \rightarrow(\sim \mathrm{q} \vee \mathrm{r})$
- **(B)** $(\sim q \vee r) \rightarrow(\sim p \vee q)$
- **(C)** $(\sim \mathrm{q} \wedge \mathrm{r}) \rightarrow(\sim \mathrm{q} \wedge \mathrm{p})$
- **(D)** $(\sim \mathrm{q} \vee \mathrm{r}) \rightarrow(\mathrm{p} \vee \sim \mathrm{q})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim \mathrm{q} \vee \mathrm{r}) \rightarrow(\mathrm{p} \vee \sim \mathrm{q})$**

**Detailed Solution:**

Contrapositive of $\mathrm{p} \rightarrow \mathrm{q}$ is $\sim \mathrm{q} \rightarrow \sim \mathrm{p}$
Hence, contrapositive of $(\sim p \wedge q) \rightarrow(q \wedge \sim r)$ is
$\begin{aligned} & \sim(\mathrm{q} \wedge \sim \mathrm{r}) \rightarrow \sim(\sim \mathrm{p} \wedge \mathrm{q}) \\ & \Rightarrow(\sim \mathrm{q} \vee \mathrm{r}) \rightarrow(\mathrm{p} \vee \sim \mathrm{q})\end{aligned}$

</details>

---

### Q175. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The statement $(\mathrm{p} \rightarrow \mathrm{q}) \rightarrow[(\sim \mathrm{p} \rightarrow \mathrm{q}) \rightarrow \mathrm{q}]$ is

**Options:**

- **(A)** equivalent to $\sim \mathrm{p} \rightarrow \mathrm{q}$
- **(B)** a tautology
- **(C)** a fallacy
- **(D)** equivalent to $\mathrm{p} \rightarrow \sim \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a tautology**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/BkzOKeCRxpYLeAs4RE7k9dvepDduJ9l_Td3dnw0MPMY.original.fullsize.png">

</details>

---

### Q176. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The stament pattern $\mathrm{p} \rightarrow(\mathrm{q} \rightarrow \mathrm{p})$ is equivalent to

**Options:**

- **(A)** $p \rightarrow(p \rightarrow q)$
- **(B)** $\mathrm{p} \rightarrow(\mathrm{p} \vee \mathrm{q})$
- **(C)** $\mathrm{p} \rightarrow(\mathrm{p} \wedge \mathrm{q})$
- **(D)** $\mathrm{p} \rightarrow(\mathrm{p} \leftrightarrow \mathrm{q})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{p} \rightarrow(\mathrm{p} \vee \mathrm{q})$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/1a3epLq__HbswhdKD-Ldv2LgD1AY5S_Ydu8i8VsyhGg.original.fullsize.png">

</details>

---

### Q177. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Negation of a statement 'If $\forall x, x$ is a complex number then $x^2<0$ ' is

**Options:**

- **(A)** $\exists x, x$ is not a complex number and $x^2 \geq 0$
- **(B)** $\exists x, x$ is not a complex number and $x^2<0$
- **(C)** $\forall x, x$ is not a complex number and $x^2 \geq 0$
- **(D)** $\forall \mathrm{x}, \mathrm{x}$ is not a complex number and $\mathrm{x}^2<0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\forall x, x$ is not a complex number and $x^2 \geq 0$**

**Detailed Solution:**

$\because$ Negation of 'if $p$ then $q$ ' is ' $p$ and not q'.
Hence the required negation is
$\forall x, x$ is a complex number and $x^2 \geq 0$

</details>

---

### Q178. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $p \rightarrow(p \wedge \sim q)$ is false, then the truth values of $p$ and $q$ are respectively

**Options:**

- **(A)** F, F
- **(B)** $\mathrm{T}, \mathrm{F}$
- **(C)** $\mathrm{F}, \mathrm{T}$
- **(D)** $\mathrm{T}, \mathrm{T}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{T}, \mathrm{T}$**

**Detailed Solution:**

$\mathrm{p} \rightarrow(\mathrm{p} \wedge \sim \mathrm{q})$ will be false if
$\mathrm{P}$ is true and $\mathrm{p} \wedge \sim \mathrm{q}$ is false
$\Rightarrow \mathrm{P}$ is true and $\mathrm{q}$ is true

</details>

---

### Q179. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Consider the statement " $\mathrm{P}(n): n^2-n+37$ is prime." then, which one of the following is true?

**Options:**

- **(A)** $\mathrm{P}(3)$ is false, but $\mathrm{P}(5)$ is true.
- **(B)** $P(5)$ is false, but $P(3)$ is true.
- **(C)** Both $\mathrm{P}(3)$ and $\mathrm{P}(5)$ are true.
- **(D)** Both $\mathrm{P}(3)$ and $\mathrm{P}(5)$ are false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $P(5)$ is false, but $P(3)$ is true.**

**Detailed Solution:**

"p $(n): n^2-n+37$ is prime"
Now, $\mathrm{p}(3)=3^2-3+37=43$ (which is prime)
and $p(5)=5^2-5+37=57$ (which is not prime)
Hence, $\mathrm{p}(3)$ is true but $\mathrm{p}(5)$ is false
In the question write ' $n$ ' ' in place of ' $n_2$ '

</details>

---

### Q180. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The logical statement $(p \wedge \sim q) \vee q \vee(\sim p \wedge q)$ is equivalent to

**Options:**

- **(A)** $p \vee \sim q$
- **(B)** $\sim p \wedge q$
- **(C)** $p \wedge q$
- **(D)** $p \vee q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $p \vee q$**

**Detailed Solution:**

$\begin{aligned} & (p \wedge \sim q) \vee q \vee(\sim p \wedge q) \\ & \equiv\{(p \wedge \sim q) \vee(\sim p \wedge q)\} \vee q \\ & \equiv \sim(p \Leftrightarrow q) \vee q \equiv p \vee q\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/QjtvYLfeiLGLWM32XV4vzeNR59TQd_CDjaU4kP0HefA.original.fullsize.png">

</details>

---

### Q181. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The logical statement $\sim(p \vee q) \vee(\sim p \wedge q)$ is equivalent to

**Options:**

- **(A)** $\mathrm{q}$
- **(B)** $\sim q$
- **(C)** $\sim p$
- **(D)** p

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sim p$**

**Detailed Solution:**

$\begin{aligned} & \sim(\mathrm{p} \vee \mathrm{q}) \vee(\sim \mathrm{p} \wedge \mathrm{q}) \equiv(\sim \mathrm{p} \wedge \sim \mathrm{q}) \vee(\sim \mathrm{p} \wedge \mathrm{q}) \text { [De Morgana’s law] } \\ & \equiv \sim p \wedge(\sim q \vee q) \quad \text { [Distributive law] } \\ & \equiv \sim p \wedge t \quad[\because \sim q \vee q \equiv t] \\ & \equiv \sim \mathrm{p} \\ & \end{aligned}$

</details>

---

### Q182. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of $\forall \mathrm{x} \in \mathrm{N}, \mathrm{x}^2+\mathrm{x}$ is even number' is

**Options:**

- **(A)** $\forall \mathrm{x} \in \mathrm{N}, \mathrm{x}^2+\mathrm{x}$ is not an even number
- **(B)** $\forall \mathrm{x} \in \mathrm{N}, \mathrm{x}^2+\mathrm{x}$ is not an odd number
- **(C)** $\exists x \in N$ such that $x^2+x$ an even number
- **(D)** $\exists \mathrm{x} \in \mathrm{N}$ such that $\mathrm{x}^2+\mathrm{x}$ is not an even number

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\exists \mathrm{x} \in \mathrm{N}$ such that $\mathrm{x}^2+\mathrm{x}$ is not an even number**

**Detailed Solution:**

Let $\mathrm{p}: \forall \mathrm{x} \in \mathrm{N}$ and $\mathrm{q}: \mathrm{x}^2+\mathrm{x}$ is even number.
The logical form of given statement is $\mathrm{p} \wedge \mathrm{q}$.
$\sim(\mathrm{p} \wedge \mathrm{q}) \equiv \sim \mathrm{p} \vee \sim$ q i.e. $\exists \mathrm{x} \in \mathrm{N}$ such that $\mathrm{x}+\mathrm{x}$ is not an even number.

</details>

---

### Q183. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{p}$ : It is raining.
q: Weather is pleasant.
then simplified form of the statement "It is not ture, if it is raining then weather is not pleasant" is

**Options:**

- **(A)** It is not raining or weather is pleasant
- **(B)** It is raining or weather is not pleasant
- **(C)** It is raining or weather is pleasant
- **(D)** It is raining and the weather is pleasant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) It is raining and the weather is pleasant**

**Detailed Solution:**

$\mathrm{p}$ : it is raining and $\mathrm{q}$ : Weather is pleasant
The symbolic form, of given statement is $\sim(p \rightarrow \sim q)$ $\equiv \sim(\sim \mathrm{p} \vee \sim \mathrm{q})$
$\equiv \mathrm{p} \wedge \mathrm{q}$ i.e. It is raining and the weather is pleasant.

</details>

---

### Q184. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

"If two triangle are congruent, then their areas are equal." Is the given statement, then the contrapositive of the inverse of the given statement is
(Where p: Two triangles are congruent, $\mathrm{q}$ : Their areas are equal)

**Options:**

- **(A)** It two triangles are not congruent. then their areas are equal
- **(B)** If two triangles are not congruent, then their areas are not equal
- **(C)** If areas of two triangles are equal, then they are congruent
- **(D)** If areas of two triangles are not equal, then they arc congruent

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) If areas of two triangles are equal, then they are congruent**

**Detailed Solution:**

Let $p$ : Two triangles are congruent.
q: Their areas are equal.
Logical form of given statement is $\mathrm{p} \rightarrow \mathrm{q}$
Inverse of given statement is $\sim p \rightarrow \sim q$.
Contrapositive of inverse of given statement is $\sim(\sim q) \rightarrow \sim(\sim p)$ i.e. $\mathrm{q} \rightarrow \mathrm{p}$ i.e.
If areas of two triangles are equal, then they are congruent.

</details>

---

### Q185. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of inverse of $\sim p \rightarrow q$ is

**Options:**

- **(A)** $\sim \mathrm{p} \wedge \mathrm{q}$
- **(B)** $\sim \mathrm{q} \rightarrow \mathrm{p}$
- **(C)** $p \wedge(\sim q)$
- **(D)** $\mathrm{p} \wedge \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{p} \wedge \mathrm{q}$**

**Detailed Solution:**

We have $\sim \mathrm{p} \rightarrow \mathrm{q}$
Inverse of given statement is
$$
\sim(\sim \mathrm{p}) \rightarrow \sim \text { q i.e. } \mathrm{p} \rightarrow \sim \mathrm{q}
$$
Negation of inverse of given statement is $\sim(p \rightarrow \sim q)$
$$
\equiv \sim(\sim p \vee \sim q) \equiv p \wedge q
$$

</details>

---

### Q186. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\mathrm{S}_1:$ If -7 is an integer, the $\sqrt{-7}$ is a complex number
$\mathrm{S}_2:-7$ is not an integer or $\sqrt{-7}$ is a complex number

**Options:**

- **(A)** $\mathrm{S}_1$ and $\mathrm{S}_2$ are converse statements of each other
- **(B)** $S_1$ and $S_2$ are negations of each other
- **(C)** $\mathrm{S}_1$ and $\mathrm{S}_2$ are equivalent statements
- **(D)** $S_1$ and $S_2$ are contrapositive of each other

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{S}_1$ and $\mathrm{S}_2$ are equivalent statements**

**Detailed Solution:**

Let $p:-7$ is an integer.
$\mathrm{q}: \sqrt{-7}$ is a complex number.
Logical form of $\mathrm{S}_1 \equiv \mathrm{p} \rightarrow \mathrm{q}$
Logical form of $\mathrm{S}_2 \equiv \sim \mathrm{p} \vee \mathrm{q}$
We know that $\mathrm{p} \rightarrow \mathrm{q} \equiv \sim \mathrm{p} \vee \mathrm{q}$
$\therefore \mathrm{S}_1$ and $\mathrm{S}_2$ are equivalent statements.

</details>

---

### Q187. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Negation of the statement : $3+6>8$ and $2+3 < 6$ is

**Options:**

- **(A)** $3+6 \leq 8 \text { or } 2+3 < 6$
- **(B)** $3+6 < 8 \text { or } 2+3 < 6$
- **(C)** $3+6 \leq 8 \text { or } 2+3 \geq 6$
- **(D)** $3+6>8 \text { or } 2+3 \geq 6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3+6 \leq 8 \text { or } 2+3 \geq 6$**

**Detailed Solution:**

Let $\mathrm{p}: 3+6>89$ and $\mathrm{q}: 2+3 < 6$
The logical form of given statement is $\mathrm{p} \wedge \mathrm{q}$.
$$
\therefore-(\mathrm{p} \wedge \mathrm{q}) \equiv \sim \mathrm{p} \vee \sim \text { q i.e. } 3+6 \leq 8 \text { or } 2+3 \geq 6
$$

</details>

---

### Q188. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{p}$ : It is raining and $\mathrm{q}$ It is pleasant, then the symbolic from of "It is neither raining nor pleasant" is

**Options:**

- **(A)** $\sim \mathrm{p} \wedge \mathrm{q}$
- **(B)** $\sim \mathrm{p} \vee \mathrm{q}$
- **(C)** $(\sim \mathrm{p}) \wedge(\sim \mathrm{q})$
- **(D)** $(\sim \mathrm{p}) \vee(\sim \mathrm{q})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim \mathrm{p}) \vee(\sim \mathrm{q})$**

**Detailed Solution:**

$\mathrm{p}$ : It is raining and q: It is pleasant
So symbolic form of 'It is neither raining nor pleasant' is $\sim \mathrm{p} \vee \sim \mathrm{q}$

</details>

---

### Q189. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of $\mathrm{p} \wedge(\mathrm{q} \rightarrow \mathrm{r})$ is

**Options:**

- **(A)** $\sim \mathrm{p} \wedge(\sim \mathrm{q} \rightarrow \sim \mathrm{r})$
- **(B)** $\sim \mathrm{p} \vee(\mathrm{q} \wedge \sim \mathrm{r})$
- **(C)** $\sim \mathrm{p} \vee(\sim \mathrm{q} \rightarrow \sim \mathrm{r})$
- **(D)** $\mathrm{p} \vee(\sim \vee \mathrm{r})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sim \mathrm{p} \vee(\mathrm{q} \wedge \sim \mathrm{r})$**

**Detailed Solution:**

$\begin{aligned} & \sim[\mathrm{p} \wedge(\mathrm{q} \rightarrow \mathrm{r})] \\ & \equiv \sim[\mathrm{p} \wedge(\sim \mathrm{q} \vee \mathrm{r})] \\ & \equiv(\sim \mathrm{p}) \vee \sim(\sim \mathrm{q} \vee \mathrm{r}) \\ & \equiv \sim \mathrm{p} \vee(\mathrm{q} \wedge \sim \mathrm{r})\end{aligned}$

</details>

---

### Q190. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{a}: \sim(\mathrm{p} \wedge \sim \mathrm{r}) \vee(\sim \mathrm{q} \vee \mathrm{s})$ and $\mathrm{b}:(\mathrm{p} \vee \mathrm{s}) \leftrightarrow(\mathrm{q} \wedge \mathrm{r})$.
If the truth values of a $p$ and $q$ are true and that of $r$ and $s$ are false, then the truth values of a and b are respectively

**Options:**

- **(A)** T,F
- **(B)** T,T
- **(C)** F,F
- **(D)** F,T

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) F,F**

**Detailed Solution:**

We have $\mathrm{p}, \mathrm{q} \equiv \mathrm{T}$ and $\mathrm{r}, \mathrm{s} \equiv \mathrm{F}$
$$
\begin{aligned}
& \mathrm{a}: \sim(\mathrm{p} \wedge \sim \mathrm{r}) \vee(\sim \mathrm{q} \vee \mathrm{s}) \equiv \sim(\mathrm{T} \wedge \sim \mathrm{F}) \vee(\sim \mathrm{T} \vee \mathrm{F}) \\
& \equiv \sim(\mathrm{T} \wedge \mathrm{T}) \vee(\mathrm{F} \vee \mathrm{F}) \\
& \equiv \sim \mathrm{T} \vee \mathrm{F} \equiv \mathrm{F} \vee \mathrm{F} \equiv \mathrm{F} \\
& \mathrm{b}:(\mathrm{p} \vee \mathrm{s}) \leftrightarrow(\mathrm{q} \wedge \mathrm{r}) \equiv(\mathrm{T} \vee \mathrm{F}) \leftrightarrow(\mathrm{T} \wedge \mathrm{F}) \equiv \mathrm{T} \leftrightarrow \mathrm{F} \equiv \mathrm{F}
\end{aligned}
$$

</details>

---

### Q191. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $(p \wedge q) \wedge[(p \wedge q) \vee(\sim p \wedge q)]$ is equivalent to

**Options:**

- **(A)** $q$
- **(B)** $\mathrm{p} \wedge \mathrm{q}$
- **(C)** $p$
- **(D)** $\mathrm{p} \vee \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{p} \wedge \mathrm{q}$**

**Detailed Solution:**

$\begin{aligned} & (p \wedge q) \wedge[(p \wedge q) \vee(\sim p \wedge q)] \\ & \equiv(p \wedge q) \wedge[q \wedge(p \vee \sim p)] \\ & \equiv(p \wedge q) \wedge[q \wedge T] \equiv(p \wedge q) \wedge q \equiv p \wedge q\end{aligned}$

</details>

---

### Q192. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Given p: A man is a judge, q: A man is honest If $\mathrm{S} 1$ : If a man is a judge, then he is honest S2: If a man is a judge, then he is not honest S3: A man is not a judge or he is honest S4: A man is a judge and he is honest Then

**Options:**

- **(A)** $\mathrm{S}_2 \equiv \mathrm{S}_3$
- **(B)** $\mathrm{S}_1 \equiv \mathrm{S}_2$
- **(C)** $\mathrm{S}_2 \equiv \mathrm{S}_4$
- **(D)** $\mathrm{S}_1 \equiv \mathrm{S}_3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{S}_1 \equiv \mathrm{S}_3$**

**Detailed Solution:**

We will write logical form of given statements
$$
\begin{array}{ll}
\mathrm{S}_1=\mathrm{p} \rightarrow \mathrm{q} & \mathrm{S}_2=\mathrm{p} \rightarrow-\mathrm{q} \\
\mathrm{S}_3=\sim \mathrm{p} \vee \mathrm{q} & \mathrm{S}_4=\mathrm{p} \wedge \mathrm{q}
\end{array}
$$
We know that $\mathrm{p} \rightarrow \mathrm{q} \equiv \sim \mathrm{q} \rightarrow \sim \mathrm{p} \equiv \sim(\sim \mathrm{q}) \vee \sim \mathrm{p} \equiv \mathrm{q} \vee \sim \mathrm{p}$

</details>

---

### Q193. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The expression $[(p \wedge \sim q) \vee q] \vee(\sim p \wedge q)$ is equivalent to

**Options:**

- **(A)** $\mathrm{p} \vee \mathrm{q}$
- **(B)** $\mathrm{p} \wedge \mathrm{q}$
- **(C)** $\mathrm{p} \rightarrow \mathrm{q}$
- **(D)** $\mathrm{p} \leftrightarrow \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{p} \vee \mathrm{q}$**

**Detailed Solution:**

\begin{array}{|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline \mathrm{p} & \mathrm{Q} & \sim \mathrm{p} & \sim \mathrm{q} & \mathrm{p} \vee \mathrm{q} & \mathrm{p} \wedge \mathrm{q} & \mathrm{p} \rightarrow \mathrm{q} & \mathrm{p} \leftrightarrow \mathrm{q} & 1 \wedge 4 & 2 \vee 9 & 2 \wedge 3 & 10 \vee 11 \\
\hline 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\
\hline \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\hline \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\hline
\end{array}
Entries in columns 5 and 12 are identical.

</details>

---

### Q194. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If statement $\mathrm{p}$ and $\mathrm{q}$ are true and $\mathrm{r}$ and $\mathrm{s}$ are false, then truth values of $\sim(\mathrm{p} \rightarrow \mathrm{q}) \leftrightarrow(\mathrm{p} \wedge \mathrm{s})$ and $(\sim \mathrm{p} \rightarrow \mathrm{q}) \wedge(\mathrm{r} \leftrightarrow \mathrm{s})$ are respectively.

**Options:**

- **(A)** F, F
- **(B)** T, T
- **(C)** T, F
- **(D)** F, T

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) T, T**

**Detailed Solution:**

$\begin{aligned} & \sim(\mathrm{p} \rightarrow \mathrm{q}) \leftrightarrow(\mathrm{r} \wedge \mathrm{s}) \\ & \equiv \sim(\mathrm{T} \rightarrow \mathrm{T}) \leftrightarrow(\mathrm{F} \wedge \mathrm{F}) \\ & =\sim(\mathrm{T}) \leftrightarrow \mathrm{F} \equiv \mathrm{F} \leftrightarrow \mathrm{F} \equiv \mathrm{T} \\ & \text { Also }(\sim \mathrm{P} \rightarrow \mathrm{q}) \wedge(\mathrm{r} \leftrightarrow \mathrm{s}) \\ & \equiv(\sim \mathrm{T} \rightarrow \mathrm{T}) \wedge(\mathrm{F} \leftrightarrow \mathrm{F}) \\ & \equiv(\mathrm{F} \rightarrow \mathrm{T}) \wedge(\mathrm{T}) \equiv \mathrm{T} \wedge \mathrm{T} \equiv \mathrm{T}\end{aligned}$

</details>

---

### Q195. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $p \rightarrow(\sim p \vee q)$ is false, then the truth values of $p$ and $q$ are, respectively

**Options:**

- **(A)** T, F
- **(B)** F, F
- **(C)** F, T
- **(D)** T, T

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) T, F**

**Detailed Solution:**

$$
\mathrm{p} \rightarrow(\sim \mathrm{p} \vee \mathrm{q}) \equiv \mathrm{F}
$$
We know that $\mathrm{T} \rightarrow \mathrm{F} \equiv \mathrm{F}$
$$
\therefore \mathrm{p} \equiv \mathrm{T} \text { and }(\sim \mathrm{p} \vee 1) \equiv \mathrm{F}
$$
We know that $\mathrm{F} \vee \mathrm{F} \equiv \mathrm{F}$
$$
\therefore \sim \mathrm{p} \equiv \mathrm{F} \text { and } \mathrm{q} \equiv \mathrm{F}
$$
Thus p, q are T, F respectively.

</details>

---

### Q196. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The logical statement $(\mathrm{p} \rightarrow \mathrm{q}) \wedge(\mathrm{p} \rightarrow \sim \mathrm{p})$ is equivalent to

**Options:**

- **(A)** $\sim \mathrm{p}$
- **(B)** $\mathrm{p}$
- **(C)** $q$
- **(D)** $\sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sim \mathrm{p}$**

**Detailed Solution:**

$\begin{aligned} & (\mathrm{p} \rightarrow \mathrm{q}) \wedge(\mathrm{q} \rightarrow \sim \mathrm{p}) \\ & \equiv(\sim \mathrm{p} \vee \mathrm{q}) \wedge(\sim \mathrm{q} \vee \sim \mathrm{p}) \\ & =(\sim \mathrm{p}) \vee(\mathrm{q} \wedge-\mathrm{q}) \\ & \equiv(\sim \mathrm{p}) \vee \mathrm{F} \equiv \sim \mathrm{p}\end{aligned}$

</details>

---

### Q197. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{p}, \mathrm{q}$ are true statements and $\mathrm{r}$ is false statement, then which of the following is correct.

**Options:**

- **(A)** $(p \vee q) \vee r$ has truth value $F$.
- **(B)** $(p \wedge q) \rightarrow r$ has truth value $T$.
- **(C)** $(\mathrm{p} \rightarrow \mathrm{r}) \rightarrow \mathrm{q}$ has truth value $\mathrm{F}$.
- **(D)** $(\mathrm{p} \leftrightarrow \mathrm{q}) \rightarrow \mathrm{r}$ has truth value $F$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\mathrm{p} \leftrightarrow \mathrm{q}) \rightarrow \mathrm{r}$ has truth value $F$.**

**Detailed Solution:**

We will go by option
(1) $(\mathrm{p} \vee \mathrm{q}) \vee \mathrm{r} \equiv(\mathrm{T} \vee \mathrm{T}) \vee \mathrm{F} \equiv \mathrm{T} \vee \mathrm{F} \equiv \mathrm{T}$
(2) $(\mathrm{p} \wedge \mathrm{q}) \rightarrow \mathrm{r} \equiv(\mathrm{T} \wedge \mathrm{T}) \rightarrow \mathrm{F} \equiv \mathrm{T} \rightarrow \mathrm{F} \equiv \mathrm{F}$
(3) $(\mathrm{p} \rightarrow \mathrm{r}) \rightarrow \mathrm{q} \equiv(\mathrm{T} \rightarrow \mathrm{F}) \rightarrow \mathrm{T} \equiv \mathrm{F} \rightarrow \mathrm{T} \equiv \mathrm{T}$
(4) $(\mathrm{p} \leftrightarrow \mathrm{q}) \rightarrow \mathrm{r} \equiv(\mathrm{T} \leftrightarrow \mathrm{T}) \rightarrow \mathrm{F} \equiv \mathrm{T} \rightarrow \mathrm{F} \equiv \mathrm{F}$

</details>

---

### Q198. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Negation of the statement $\forall \mathrm{x} \in \mathrm{R}, \mathrm{x}^2+1=0$ is

**Options:**

- **(A)** $\exists x \in R$ such that $x^2+1 < 0$
- **(B)** $\exists x \in R$ such that $x^2+1 \leq 0$
- **(C)** $\exists x \in R$ such that $x^2+1 \neq 0$
- **(D)** $\exists \mathrm{x} \in \mathrm{R}$ such that $\mathrm{x}^2+1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\exists x \in R$ such that $x^2+1 \neq 0$**

**Detailed Solution:**

$$
\text { Negation of }\left(\forall x \in R, x^2+1=0\right) \text { is } \exists x \in R \text {, such that } x^2+1 \neq 0
$$

</details>

---

### Q199. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Then symbolic from of the statement "If it does not rain today or I won't go to school, then I will meet my friend and I will go to watch a movie" is
p: It rains today
q: I am going to school
r: I will meet my friend
s: I will go to watch a movie

**Options:**

- **(A)** $\sim(\mathrm{p} \vee \mathrm{q}) \rightarrow(\mathrm{r} \vee \mathrm{s})$
- **(B)** $(p \wedge q) \rightarrow(r \vee s)$
- **(C)** $\sim(\mathrm{p} \wedge \mathrm{q}) \rightarrow(\mathrm{r} \wedge \mathrm{s})$
- **(D)** $(\sim \mathrm{p} \wedge \mathrm{q}) \rightarrow(\mathrm{r} \wedge \mathrm{s})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sim(\mathrm{p} \wedge \mathrm{q}) \rightarrow(\mathrm{r} \wedge \mathrm{s})$**

**Detailed Solution:**

From the data given, symbolic form of the given statement is
$$
\begin{aligned}
& (\sim \mathrm{p} \vee \sim \mathrm{q}) \rightarrow(\mathrm{r} \wedge \mathrm{s}) \\
& \equiv \sim(\mathrm{p} \wedge \mathrm{q}) \rightarrow(\mathrm{r} \wedge \mathrm{s})
\end{aligned}
$$

</details>

---

### Q200. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Negation of $(p \wedge q) \rightarrow(\sim p \vee r)$ is

**Options:**

- **(A)** $\mathrm{p} \vee \mathrm{q} \vee(\sim \mathrm{r})$
- **(B)** $\mathrm{p} \wedge \mathrm{q} \wedge \mathrm{r}$
- **(C)** $\sim \mathrm{p} \wedge \mathrm{q} \wedge \mathrm{r}$
- **(D)** $\mathrm{p} \wedge \mathrm{q} \wedge(\sim \rho)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{p} \wedge \mathrm{q} \wedge(\sim \rho)$**

**Detailed Solution:**

$$
\begin{aligned}
& \sim[(\mathrm{p} \wedge \mathrm{q}) \rightarrow(\sim \mathrm{p} \vee \mathrm{r})] \\
& \equiv \sim[\sim(\mathrm{p} \wedge \mathrm{q}) \vee(\sim \mathrm{p} \vee \mathrm{r})] \\
& \equiv(\mathrm{p} \wedge \mathrm{q}) \wedge \sim(\sim \mathrm{p} \vee \mathrm{r}) \\
& \equiv(\mathrm{p} \wedge \mathrm{q}) \wedge(\mathrm{p} \wedge \sim \mathrm{r}) \equiv \mathrm{p} \wedge \mathrm{q} \wedge(\sim \mathrm{r})
\end{aligned}
$$

</details>

---

### Q201. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The logical expression $p(\sim p \vee \sim q)=$

**Options:**

- **(A)** $p \vee q$
- **(B)** $p \wedge q$
- **(C)** F
- **(D)** T

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $p \wedge q$**

**Detailed Solution:**

Solve the given expression by the help of truth table. So, the truth table will be:
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/BoQ_zRfiPAYZhw5g8Ba8mV4EgCtlXqXHYBNdjY0i8Nc.original.fullsize.png">

As we know that the truth table for $p \wedge(\sim p \vee \sim q)$ is same as the truth table of $p \wedge q$.
Therefore, the correct answer is option (B).

</details>

---

### Q202. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of a statement ' $\mathrm{x} \in \mathrm{A} \cap \mathrm{B}$ $\rightarrow(\mathrm{x} \in \mathrm{A} \text { and } \mathrm{x} \in \mathrm{B})^{\prime}$ is

**Options:**

- **(A)** $\mathrm{x} \in \mathrm{A} \cap \mathrm{B} \rightarrow(\mathrm{x} \in \mathrm{A}$ or $\mathrm{x} \in \mathrm{B})$
- **(B)** $\mathrm{x} \in \mathrm{A} \cap \mathrm{B}$ and $(\mathrm{x} \notin \mathrm{A}$ or $\mathrm{x} \notin \mathrm{B})$
- **(C)** $\mathrm{x} \in \mathrm{A} \cap \mathrm{B}$ or $(\mathrm{x} \in \mathrm{A}$ and $\mathrm{x} \in \mathrm{B})$
- **(D)** $\mathrm{x} \notin \mathrm{A} \cap \mathrm{B}$ and $(\mathrm{x} \in \mathrm{A}$ and $\mathrm{x} \in \mathrm{B})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{x} \in \mathrm{A} \cap \mathrm{B}$ and $(\mathrm{x} \notin \mathrm{A}$ or $\mathrm{x} \notin \mathrm{B})$**

**Detailed Solution:**

Let $\mathrm{p}: \mathrm{x} \in \mathrm{A} \cap \mathrm{B}$ and $\mathrm{q}: \mathrm{x} \in \mathrm{A}$ and $\mathrm{x} \in \mathrm{B}$. $\therefore$ Logical form of given statement is $\mathrm{p} \rightarrow \mathrm{q}$. Now $\mathrm{p} \rightarrow \mathrm{q} \equiv \sim \mathrm{p} \wedge \sim \mathrm{q}$, which is stated as $\mathrm{x} \in \mathrm{A} \cap \mathrm{B}$ and $(\mathrm{x} \notin \mathrm{A}$ or $\mathrm{x} \notin \mathrm{B})$.

</details>

---

### Q203. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\{2,3,4,5,6\}$, then which of the following statement has truth value 'false"

**Options:**

- **(A)** $\exists x \in A$, such that $(x-2) \in N$
- **(B)** $\forall x \in A, x+6$ is divisible by 2
- **(C)** $\exists x \in A$, such that $x+2$ is a prime number.
- **(D)** $\exists x \in A$, such that $x^{2}+1$ is an even number.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\forall x \in A, x+6$ is divisible by 2**

**Detailed Solution:**

$x+6$ is divisible by 2 only when $x$ is even. Hence given statement is false.

</details>

---

### Q204. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The logical expression 
$[\mathrm{p} \wedge(\mathrm{q} \vee \mathrm{r})] \vee[(\sim \mathrm{p} \wedge \mathrm{q}) \vee(\sim \mathrm{p} \wedge \mathrm{r})]$ is equivalent to

**Options:**

- **(A)** $\mathrm{p}$
- **(B)** $\mathrm{q}$
- **(C)** $\mathrm{p} \wedge \mathrm{r}$
- **(D)** $\mathrm{q} \vee \mathrm{r}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{q} \vee \mathrm{r}$**

**Detailed Solution:**

$[p \wedge(q \vee r)] \vee[(\sim p \wedge q) \vee(\sim p \wedge r)]$
$\equiv[p \wedge(q \vee r)] \vee[\sim p \wedge(q \vee r)]$
$\equiv(q \vee r) \wedge(p \vee \sim p)$
$\equiv(q \vee r) \wedge T$
$\equiv q \vee r$

</details>

---

### Q205. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the logical statement $(\mathrm{p} \vee \sim \mathrm{q}) \rightarrow(\mathrm{p} \wedge \sim \mathrm{q})$ is

**Options:**

- **(A)** $(p \wedge \sim q) \wedge(p \vee \sim q)$
- **(B)** $(p \vee \sim q) \wedge(\sim p \vee q)$
- **(C)** $(p \vee \sim q) \wedge(p \wedge q)$
- **(D)** $(p \vee \sim q) \vee(\sim p \wedge q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(p \vee \sim q) \wedge(\sim p \vee q)$**

**Detailed Solution:**

$\sim[p \vee \sim q \rightarrow(p \wedge \sim q)]$
$\equiv \sim \sim(p \vee \sim q) \vee(p \wedge \sim q)]$
$\equiv(p \vee \sim q) \wedge \sim(p \wedge \sim q)$
$\equiv(p \vee \sim q) \wedge(\sim p \vee q)$

</details>

---

### Q206. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{p}:$ Seema is fat. $\mathrm{q}:$ She is happy, then the logical equivalent statement of 'If Seema is fat, then she is happy' is

**Options:**

- **(A)** Seema is not fat or she is unhappy.
- **(B)** Seema is not fat or she is happy.
- **(C)** Seema is fat and she is happy.
- **(D)** Seema is fat or she is happy.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Seema is not fat or she is happy.**

**Detailed Solution:**

Logical equivalence of given statement is $\mathrm{p} \rightarrow \mathrm{q}$
We know that $p \rightarrow q \equiv \sim p \vee q$
$\therefore$ Required equivalent statement is "Seema is not fat or she is happy"

</details>

---

### Q207. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $\mathrm{p} \wedge(\mathrm{q} \vee \sim \mathrm{p})$ is equivalent to

**Options:**

- **(A)** $\mathrm{p} \wedge \mathrm{q}$
- **(B)** $\mathrm{p} \rightarrow \mathrm{q}$
- **(C)** $\mathrm{q} \wedge \sim \mathrm{p}$
- **(D)** $\mathrm{p} \vee \mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{p} \wedge \mathrm{q}$**

**Detailed Solution:**

(C)
$\begin{array}{ll}\mathrm{p} \wedge(\mathrm{q} \vee \sim \mathrm{p}) & \\ \equiv(\mathrm{p} \wedge \mathrm{q}) \vee(\mathrm{p} \wedge \sim \mathrm{p}) & {[\text { Distributive law }]} \\ \equiv(\mathrm{p} \wedge \mathrm{q}) \vee \mathrm{F} & {[\text { complement law }]} \\ \equiv \mathrm{p} \wedge \mathrm{q} & {[\text { Identity law }]}\end{array}$

</details>

---

### Q208. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement pattern $\sim \mathrm{p} \vee(\mathrm{q} \rightarrow \sim \mathrm{r})$ is

**Options:**

- **(A)** $\mathrm{p} \rightarrow(\mathrm{q} \wedge \sim \mathrm{r})$
- **(B)** $\mathrm{p} \vee(\mathrm{q} \wedge \mathrm{r})$
- **(C)** $\mathrm{p} \wedge(\mathrm{q} \wedge \mathrm{r})$
- **(D)** $\sim \mathrm{p} \wedge(\mathrm{q} \wedge \mathrm{r})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{p} \wedge(\mathrm{q} \wedge \mathrm{r})$**

**Detailed Solution:**

(A)
$\begin{array}{l}
\sim[\sim p \vee(q \rightarrow \sim r)] \\
\equiv p \wedge \sim(q \rightarrow \sim r) \\
\equiv p \wedge \sim(\sim q \vee \sim r) \\
\equiv p \wedge \sim[\sim(q \wedge r)] \\
\equiv p \wedge(q \wedge r)
\end{array}$

</details>

---

### Q209. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement "If $5 < 7$ and $7>2$, then $5>2 "$ is

**Options:**

- **(A)** $5 < 7$ and $7>2$ and $5 \leq 2$
- **(B)** $5 < 7$ and $7>2$ or $5 < 2$
- **(C)** $5 < 7$ and $7>2$ and $5>2$
- **(D)** $5 < 7$ and $7>2$ or $5 \leq 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5 < 7$ and $7>2$ and $5 \leq 2$**

**Detailed Solution:**

(D)
Let $\mathrm{p}: 5 < 7$ and $\mathrm{q}: 7>2$ and $\mathrm{r}: 5>2 .$ The logical form of given statement is $(\mathrm{p} \wedge \mathrm{q}) \rightarrow \mathrm{r}$ $\therefore \quad[(\mathrm{p} \wedge \mathrm{q}) \rightarrow \mathrm{r}] \equiv \sim[\sim(\mathrm{p} \wedge \mathrm{q}) \vee \mathrm{r}]$ $\quad \equiv(\mathrm{p} \wedge \mathrm{q}) \vee \sim \mathrm{r}$ $[(5 < 7)$ and $(7>2)]$ and $(5 \leq 2)$

</details>

---

### Q210. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The dual of a statement 'Mangoes are delicious but expensive' is

**Options:**

- **(A)** Mangoes are delicious or Mangoes are not expensive.
- **(B)** Mangoes are not delicious and Mangoes are not expensive.
- **(C)** Mangoes are delicious or Mangoes are expensive.
- **(D)** Mangoes are delicious and Mangoes are expensive.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Mangoes are delicious or Mangoes are expensive.**

**Detailed Solution:**

(A)
Mangoes are delicious or mangoes are expensive.

</details>

---

### Q211. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement 'He is poor but happy' is

**Options:**

- **(A)** He is poor but not happy.
- **(B)** He is not poor or not happy.
- **(C)** He is not poor and not happy.
- **(D)** He is neither poor nor happy.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) He is not poor or not happy.**

**Detailed Solution:**

(D)
Let $\mathrm{p}$ : He is poor and $\mathrm{q}$ : He is happy.
The logical form of given statement is $\mathrm{p} \wedge \mathrm{q}$.
$\therefore \sim(p \wedge q) \equiv \sim p \vee \sim q$ i.e. He not poor or he is not happy.

</details>

---

### Q212. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If p, $q$ are true statement and $\mathrm{r}$ is false statement, then which of the following atements is a true statement.

**Options:**

- **(A)** $(p \wedge q) \rightarrow r$ is true
- **(B)** $(p \rightarrow r) \rightarrow q$ is false
- **(C)** $(p \vee q) \vee r$ is false
- **(D)** $(p \leftrightarrow q) \leftrightarrow r$ is false.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(p \leftrightarrow q) \leftrightarrow r$ is false.**

**Detailed Solution:**

$(\mathrm{A})$
We have $\mathrm{p} \equiv \mathrm{T}, \mathrm{q} \equiv \mathrm{T}$ and $\mathrm{r} \equiv \mathrm{F}$
We will check truth value of each option.
(A) $(\mathrm{p} \leftrightarrow \mathrm{q}) \leftrightarrow \mathrm{r}$
$\equiv(T \leftrightarrow T) \leftrightarrow F \equiv T \leftrightarrow F \equiv F$
(B) $(p \vee q) \vee r$
$\equiv(T \vee T) \vee F \equiv T \vee F=T$
(C) $(p \wedge q) \rightarrow r$
$\equiv(\mathrm{T} \wedge \mathrm{T}) \rightarrow \mathrm{F} \equiv \mathrm{T} \rightarrow \mathrm{F} \equiv \mathrm{F}$
(D) $(\mathrm{p} \rightarrow \mathrm{r}) \rightarrow \mathrm{q}$
$\equiv(T \rightarrow F) \rightarrow T \equiv F \rightarrow T \equiv T$

</details>

---

### Q213. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{p} \rightarrow(\sim \mathrm{p} \vee \mathrm{q})$ is false, then the truth values of $\mathrm{p}$ and $\mathrm{q}$ are respectively

**Options:**

- **(A)** F, T
- **(B)** F, F
- **(C)** T, T
- **(D)** T, F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) T, F**

**Detailed Solution:**

(D)
We know that $\mathrm{T} \rightarrow \mathrm{F}$ is false.
$\therefore \mathrm{p}$ must be true and $(\sim \mathrm{p} \vee \mathrm{q})$ must be false. $\Rightarrow \mathrm{p}$ is true.
We know that $\mathrm{F} \vee \mathrm{F}$ is false.
So $\mathrm{q}$ must be false.

</details>

---

### Q214. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The symbolic form of the following circuit is (where
and $s_{2}$ closed respectively)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/63cvddwdIHOl1qAs_u7-5V7UkdYOFdbgmwgOiHz4nNU.original.fullsize.png">

**Options:**

- **(A)** $(p \wedge q) \wedge(\sim p \wedge \sim q) \equiv \ell$
- **(B)** $p \vee[q \wedge(\sim p \wedge \sim q) \equiv \ell$
- **(C)** $\mathrm{p} \wedge[\mathrm{q} \wedge(\sim \mathrm{p} \wedge \sim \mathrm{q}) \equiv \ell$
- **(D)** $(p \vee q) \vee(\sim p \wedge \sim q) \equiv \ell$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(p \vee q) \vee(\sim p \wedge \sim q) \equiv \ell$**

**Detailed Solution:**

(B)
Let $\mathrm{p}$ : the switch $\mathrm{S}_{1}$ is closed
$\mathrm{q}$ : The switch $\mathrm{S}_{2}$ is closed
$l:$ The lamp
Given circuit can be expressed as $(p \vee q) \vee(\sim p \wedge \sim q)$

</details>

---

### Q215. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The entries in the last column of the truth table for $\sim(\mathrm{p} \wedge \mathrm{q})$ are

**Options:**

- **(A)** $\mathrm{F} \quad \mathrm{F} \quad \mathrm{T} \quad \mathrm{T}$
- **(B)** $\mathrm{T} \quad \mathrm{F} \quad \mathrm{F} \quad \mathrm{F}$
- **(C)** $\mathrm{F} \quad \mathrm{T} \quad \mathrm{T} \quad \mathrm{T}$
- **(D)** $\mathrm{T} \quad \mathrm{T} \quad \mathrm{F} \quad \mathrm{F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{F} \quad \mathrm{T} \quad \mathrm{T} \quad \mathrm{T}$**

**Detailed Solution:**

$\begin{array}{|c|c|c|c|} \hline p & q & p \wedge q & \sim(p \wedge q) \\ \hline T & T & T & F \\ \hline T & F & F & T \\ \hline F & T & F & T \\ \hline F & F & F & T \\ \hline \end{array}$

</details>

---

### Q216. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Amongs the given statements below
___________ is a tautology

**Options:**

- **(A)** $\sim p \vee(\sim p \vee \sim q)$
- **(B)** $\sim q \wedge(\sim p \vee \sim q)$
- **(C)** $(\sim p \vee \sim q) \wedge(p \vee \sim q)$
- **(D)** $(\sim p \vee \sim q) \vee(p \vee \sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim p \vee \sim q) \vee(p \vee \sim q)$**

**Detailed Solution:**

\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
\hline \mathrm{p} & \mathrm{q} & \sim \mathrm{p} & \sim \mathrm{q} & \sim \mathrm{p} \vee \sim \mathrm{q} & (3) \vee(5) & (4) \wedge(5) & \mathrm{p} \vee \sim \mathrm{q} & (5) \wedge(8) & (5) \vee(8) \\
\hline 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
\hline \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\hline \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\hline \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\hline & & & & (\mathrm{a}) & (\mathrm{b}) & & (\mathrm{c}) & (\mathrm{d}) \\
\hline
\end{array}
All entries in column 10 are T. Hence statement(d) is a tautology.

</details>

---

### Q217. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Write the statement in symbolic form 'Sandeep neither likes tea nor coffee but enjoys a soft drink'. Where 
$\mathrm{p}$ : Sandeep likes tea
$\mathrm{q}:$ Sandeep likes coffee
$\mathrm{r}:$ Sandeep enjoys a soft drink

**Options:**

- **(A)** $(\sim p \wedge q) \vee r$
- **(B)** $(\sim p \wedge \sim q) \wedge r$
- **(C)** $(\sim p \vee \sim q) \vee r$
- **(D)** $(\sim p \vee \sim q) \wedge r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(\sim p \wedge \sim q) \wedge r$**

**Detailed Solution:**

Symbolic form is $(\sim p \wedge \sim q) \wedge r$

</details>

---

### Q218. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The verbal statement of the same meaning, of the statement 'If the grass is green then it rains in July' is

**Options:**

- **(A)** The grass is not green and it does not rains in July.
- **(B)** The grass is not green or it rains in July.
- **(C)** If the grass is not green, then it does not rain in July.
- **(D)** The grass is not green if and only if it rains in July.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The grass is not green or it rains in July.**

**Detailed Solution:**

Let $p:$ The grass is green
$\mathrm{q}$ : If rains in July.
The logical form of given statement is $\mathrm{p} \rightarrow \mathrm{q}$
We know that $\mathrm{p} \rightarrow \mathrm{q} \equiv \sim \mathrm{p} \vee \mathrm{q}$
The grass is not green or it rains in July.

</details>

---

### Q219. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the symbolic form of the switching circuit is $[\sim \mathrm{pv}(\mathrm{p} \wedge \sim \mathrm{q})] \mathrm{v} \mathrm{q}$, then the current flows through the circuit onlyif

**Options:**

- **(A)** irrespective of status of the switches
- **(B)** one switch should be open and other should be closed
- **(C)** both switches should be closed
- **(D)** both switches should be open

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) irrespective of status of the switches**

**Detailed Solution:**

$[\sim p \vee(p \wedge \sim q)] \vee q$
$=[(\sim p \vee p) \wedge(\sim p \vee \sim q)] \vee q$
$E[T \wedge(\sim p \vee \sim q)] \vee q$
$\equiv(\sim p \vee \sim q) \vee q$
$\equiv \sim p \vee(\sim q \vee q) \equiv \sim p \vee T \equiv T$
This shows that current flows irrespective of status of the switches.

</details>

---

### Q220. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $(\sim \mathrm{p} \wedge \mathrm{q}) \rightarrow \mathrm{r}$ is false then the truth values of $\mathrm{p}, \mathrm{q}, \mathrm{r}$ are respectively

**Options:**

- **(A)** $\mathbf{F}, \mathbf{T}, \mathbf{F}$
- **(B)** $\mathrm{F}, \mathrm{T}, \mathrm{T}$
- **(C)** $\mathrm{T}, \mathrm{T}, \mathrm{F}$
- **(D)** $\mathrm{F}, \mathrm{F}, \mathrm{T}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathbf{F}, \mathbf{T}, \mathbf{F}$**

**Detailed Solution:**

Given $(\sim p \wedge q) \rightarrow r$ is false $T \rightarrow F \equiv F$ 
We know that $T \rightarrow F=F$ 
$\therefore \sim p \wedge q=T \quad$ and $r \equiv F$ 
Also we know that $\mathrm{T} \wedge \mathrm{T}=\mathrm{T}$ 
$\therefore \mathrm{q} \equiv \mathrm{T}$ and $\sim \mathrm{p}=\mathrm{T} \Rightarrow \mathrm{p}=\mathrm{F}$

</details>

---

### Q221. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The contrapositive of the statement 'If Raju is courageous, then he will join Indian
Army', is

**Options:**

- **(A)** If Raju does not join Indian Army, then he is courageous.
- **(B)** If Raju does not join Indian Army, then he is not courageous.
- **(C)** If Raju join Indian Army, then he is not courageous
- **(D)** If Raju join Indian Army, then he is courageous.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) If Raju does not join Indian Army, then he is not courageous.**

**Detailed Solution:**

Let $\mathrm{p}$ : Raju is courageous, and $\mathrm{q}$ : Raju will join Indian army.
The contrapositive of $\mathrm{p} \rightarrow \mathrm{q}$ is $\sim \mathrm{q} \rightarrow \sim \mathrm{p}$ i.e.
If Raju does not join Indian army, then he is not courageous.

</details>

---

### Q222. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The logical expression $[p \wedge(q \vee r)] \vee[\sim r \wedge \sim q \wedge p]$ is equivalent to

**Options:**

- **(A)** $\mathrm{q}$
- **(B)** $\sim q$
- **(C)** $\sim \mathrm{p}$
- **(D)** $\mathrm{p}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{p}$**

**Detailed Solution:**

$[p \wedge(q \vee r)] \vee[\sim r \wedge \sim \wedge \wedge p]$
$\equiv[p \wedge(q \vee r)] \vee[p \wedge(\sim q \wedge \sim r)]$
$\underline{\underline{\underline{\alpha}}}[p \wedge(q \vee r)] \vee[p \wedge(\sim(q \vee r))]$
$=p \wedge[(q \vee r) \vee(\sim(q \vee r))]$
$=p \wedge T=p$

</details>

---

### Q223. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern $\sim(\mathrm{p} \vee \mathrm{q}) \vee(\sim \mathrm{p} \wedge \mathrm{q})$ is equivalent to

**Options:**

- **(A)** $\sim \mathrm{p}$
- **(B)** $\mathrm{p}$
- **(C)** $\sim q$
- **(D)** $\mathrm{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sim \mathrm{p}$**

**Detailed Solution:**

$\sim(p \vee q) \vee(\sim p \wedge q)$
$=(\sim p \wedge \sim q) \vee(\sim p \wedge q)$
$\equiv \sim p \wedge(\sim q \vee q)$
$\equiv \sim p \wedge T \cong \sim p$

</details>

---

### Q224. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The symbolic form of the following circuit is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ee57WyxZ8qG7xz2qLMzQ1eqytM_qNnqTBbiTYG7f79Q.original.fullsize.png">

(where $\mathrm{p}, \mathrm{q}$ and $\mathrm{r}$ represents switches $\mathrm{s}_{1}, \mathrm{~s}_{2}$ and $\mathrm{s}_{3}$ which are closed respectively)

**Options:**

- **(A)** $(p \vee q) \wedge[\sim p \vee(\sim q \wedge p \wedge r)] \equiv \ell$
- **(B)** $[(p \vee q) \wedge \sim p] \vee[\sim p \vee q \vee r)] \equiv \ell$
- **(C)** $(p \wedge q) \vee[\sim p \wedge(\sim q \vee p \vee r)] \equiv \ell$
- **(D)** $(p \wedge q) \vee \sim p \vee[\sim p \vee p \vee r] \equiv \ell$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(p \wedge q) \vee[\sim p \wedge(\sim q \vee p \vee r)] \equiv \ell$**

**Detailed Solution:**

The symbolic form of given circuit is
$(\mathrm{p} \wedge \mathrm{q}) \vee[\sim \mathrm{p} \wedge(\sim \mathrm{q} \vee \mathrm{p} \vee \mathrm{r})]=\ell$

</details>

---

### Q225. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statement pattern is a tautology?
$$
\begin{array}{l}
\mathrm{S}_{1} \equiv(\sim \mathrm{q} \wedge \mathrm{p}) \wedge \mathrm{q} \\
\mathrm{S}_{2} \equiv[\mathrm{p} \wedge(\mathrm{p} \rightarrow \mathrm{q})] \rightarrow \mathrm{q} \\
\mathrm{S}_{3} \equiv(\mathrm{p} \wedge \mathrm{q}) \wedge(\sim \mathrm{p} \vee \sim \mathrm{q}) \\
\mathrm{S}_{4} \equiv(\mathrm{p} \wedge \mathrm{q}) \rightarrow \mathrm{r}
\end{array}
$$

**Options:**

- **(A)** $\mathrm{S}_{4}$
- **(B)** $\mathrm{S}_{3}$
- **(C)** $\mathrm{S}_{1}$
- **(D)** $\mathrm{S}_{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{S}_{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/8OEM50QnbtMTNKN0FRi0_Q6UXr3ShVBpMZLUCo9vmmo.original.fullsize.png">

All the entries in column 10 are $\mathrm{T} \Rightarrow \mathrm{S}_{2}$ is a tautology

</details>

---

### Q226. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The dual of the statement pattern $\sim \mathrm{p} \wedge(\mathrm{q} \vee \mathrm{t})$ is
(where $t$ is a tautology and $c$ is a contradiction)

**Options:**

- **(A)** $p \vee(q \wedge c)$
- **(B)** $\sim \mathrm{p} \vee(\mathrm{q} \wedge \mathrm{t})$
- **(C)** $\sim \mathrm{p} \vee(\mathrm{q} \wedge \mathrm{c})$
- **(D)** $p \vee(q \wedge t)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sim \mathrm{p} \vee(\mathrm{q} \wedge \mathrm{c})$**

**Detailed Solution:**

dual of $\sim p \wedge(q \vee t)$ is $\sim p \vee(q \wedge c)$

</details>

---

### Q227. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following statement pattern is a contradiction?
$$
\begin{array}{l}
\mathrm{S}_{1} \equiv(\mathrm{p} \rightarrow \mathrm{q}) \wedge(\mathrm{p} \wedge \sim \mathrm{q}) \\
\mathrm{S}_{2} \equiv[\mathrm{p} \wedge(\mathrm{p} \rightarrow \mathrm{q})] \rightarrow \mathrm{q} \\
\mathrm{S}_{3} \equiv(\mathrm{p} \vee \mathrm{q}) \rightarrow \sim \mathrm{p} \\
\mathrm{S}_{4} \equiv[\mathrm{p} \wedge(\mathrm{p} \rightarrow \mathrm{q})] \leftrightarrow \mathrm{q}
\end{array}
$$

**Options:**

- **(A)** $\mathrm{S}_{4}$
- **(B)** $\mathrm{~S}_{1}$
- **(C)** $\mathrm{~S}_{2}$
- **(D)** $\mathrm{~S}_{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{~S}_{1}$**

**Detailed Solution:**

\begin{array}{|l|l|l|l|l|l|}
\hline 1 & 2 & 3 & 4 & 5 & 6 \\
\hline \mathrm{p} & \mathrm{q} & \mathrm{p} \rightarrow \mathrm{q} & \sim \mathrm{q} & \mathrm{P} \wedge \sim \mathrm{q} & (\mathrm{p} \rightarrow \mathrm{g}) \wedge(\mathrm{p} \wedge \sim \mathrm{q}) \\
\hline \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\hline \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\hline \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\hline \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\hline
\end{array}
All entries in last column are $\mathrm{F}$. So $\mathrm{S}_{1}$ is a contradiction.
This problem can be alternatively solved as follows :
$\begin{aligned}
S_{1} & \equiv(p \rightarrow q) \wedge(p \wedge \sim q) \\
& \equiv[(\sim p \vee q)] \wedge[\sim(\sim p \vee q)] \\
& \equiv F
\end{aligned}$

</details>

---

### Q228. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement, $\exists x \in A$ such that $x+5>8$ is

**Options:**

- **(A)** $\forall x \in A, \quad x+5 \geq 8$
- **(B)** $\forall x \in A, \quad x+5 \leq 8$
- **(C)** $\forall x \in A, \quad x+5>8$
- **(D)** $\exists x \in A$ such that $x+5 < 8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\forall x \in A, \quad x+5 \leq 8$**

**Detailed Solution:**

While doing negation we replace $\exists$ by $\forall$ and $>$ by $\leq$.
So required statement is $\forall \mathrm{x} \in \mathrm{A}$ such that $\mathrm{x}+5 \leq 8$

</details>

---

### Q229. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following statement pattern is a tautology?
$\mathrm{S}_{1} \equiv \sim \mathrm{p} \rightarrow(\mathrm{q} \leftrightarrow \mathrm{p})$
$\mathrm{S}_{2} \equiv \sim \mathrm{p} \mathrm{V} \sim \mathrm{q}$
$\mathrm{S}_{3} \equiv(\mathrm{p} \rightarrow \mathrm{q}) \wedge(\mathrm{q} \rightarrow \mathrm{p})$
$\mathrm{S}_{4} \equiv(\mathrm{q} \rightarrow \mathrm{p}) \vee(\sim \mathrm{p} \leftrightarrow \mathrm{q})$

**Options:**

- **(A)** $\mathrm{S}_{2}$
- **(B)** $\mathrm{~S}_{4}$
- **(C)** $\mathrm{~S}_{1}$
- **(D)** $\mathrm{~S}_{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{~S}_{4}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/itEk2yJG4gk0DWDOaCwnVuVyc10Yk729qMVFxXFhwHQ.original.fullsize.png">

We find that all entries in column (12) are T 
$\therefore \mathrm{S}_{4}$ is a tautology

</details>

---

### Q230. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The statement pattern $[(p \vee q) \wedge \sim p] \wedge(\sim q)$ is

**Options:**

- **(A)** a contradiction
- **(B)** equivalent to $p \wedge q$
- **(C)** a contingency
- **(D)** a tautology

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a contradiction**

**Detailed Solution:**

\begin{array}{|c|c|c|c|c|c|c|}
\hline 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline \mathrm{p} & \mathrm{q} & \sim \mathrm{p} & \sim \mathrm{q} & \mathrm{p} \vee \mathrm{q} & (\mathrm{p} \vee \mathrm{q}) \wedge \sim \mathrm{p} & {[(\mathrm{p} \vee \mathrm{q}) \wedge \sim \mathrm{p}] \wedge \sim \mathrm{q}} \\
\hline \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\hline \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\hline \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\hline \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\hline
\end{array}
All entries in last column are F.
$\therefore$ It is contradiction.

</details>

---

### Q231. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The equivalent form of the statement <math><mo>~</mo><mfenced separators="|"><mrow><mi>p</mi><mo>→</mo><mo>~</mo><mi>q</mi></mrow></mfenced></math> is ________

**Options:**

- **(A)** <math><mi>p</mi><mo>∧</mo><mi>q</mi></math>
- **(B)** <math><mi>p</mi><mo>∧</mo><mo>~</mo><mi>q</mi></math>
- **(C)** <math><mi>p</mi><mo>∨</mo><mo>~</mo><mi>q</mi></math>
- **(D)** <math><mo>~</mo><mi>p</mi><mo>∨</mo><mi>q</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>p</mi><mo>∧</mo><mi>q</mi></math>**

**Detailed Solution:**

Since, <math><mo>∼</mo><mfenced separators="|"><mrow><mi>p</mi><mo>→</mo><mi>q</mi></mrow></mfenced><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>q</mi></mrow></mfenced></math>  
Then, <math><mo>∼</mo><mfenced separators="|"><mrow><mi>p</mi><mo>→</mo><mo>∼</mo><mi>q</mi></mrow></mfenced><mo>&#8658;</mo><mi>p</mi><mo>∧</mo><mfenced separators="|"><mrow><mo>∼</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>q</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>=</mo><mi>p</mi><mo>∧</mo><mi>q</mi></math>

</details>

---

### Q232. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following is NOT equivalent to <math><mi>p</mi><mo>→</mo><mi>q</mi><mo>?</mo></math>

**Options:**

- **(A)** <math><mi>p</mi></math> only if <math><mi>q</mi></math>
- **(B)** <math><mi>q</mi></math> is necessary for <math><mi>p</mi></math>
- **(C)** <math><mi>q</mi></math> only if <math><mi>p</mi></math>
- **(D)** <math><mi>p</mi></math> is sufficient for <math><mi>q</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>q</mi></math> only if <math><mi>p</mi></math>**

**Detailed Solution:**

<math><mi>p</mi><mo>→</mo><mi>q</mi></math> is equivalent to 
<math><mn>1</mn><mo>.</mo><mi></mi></math> If <math><mi>p</mi></math> then <math><mi>q</mi></math>  
<math><mn>2</mn><mo>.</mo><mi></mi><mi>q</mi></math> is necessary for <math><mi>p</mi></math>  
<math><mn>3</mn><mo>.</mo><mi></mi><mi>p</mi></math> is sufficient for <math><mi>q</mi></math>  
<math><mn>4</mn><mo>.</mo><mi></mi><mi>p</mi></math> only if <math><mi>q</mi></math>

</details>

---

### Q233. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern <math><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mfenced close="]" open="[" separators="|"><mrow><mo>~</mo><mi>r</mi><mo>∨</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mi>q</mi></mrow></mfenced></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mo>~</mo><mi>p</mi><mo>∧</mo><mi>q</mi></mrow></mfenced></math> is equivalent to ________

**Options:**

- **(A)** <math><mi>r</mi></math>
- **(B)** <math><mi>q</mi></math>
- **(C)** <math><mi>p</mi><mo>∧</mo><mi>q</mi></math>
- **(D)** <math><mi>p</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>q</mi></math>**

**Detailed Solution:**

<table border='1px solid'> <thead> <tr> <th> <math><mi mathvariant="normal">p</mi></math> </th> <th> <math><mi mathvariant="normal">q</mi></math> </th> <th> <math><mi mathvariant="normal">r</mi></math> </th> <th> <math><mi mathvariant="normal">p</mi><mo>∧</mo><mi mathvariant="normal">q</mi><mi mathvariant="normal"></mi><mo>=</mo><mi mathvariant="normal"></mi><mi mathvariant="normal">A</mi></math> </th> <th> <math><mo>~</mo><mi mathvariant="normal">r</mi></math> </th> <th> <math><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mo>~</mo><mi>r</mi><mi></mi><mo>=</mo><mi></mi><mi>B</mi></math> </th> <th> <math><mi>A</mi><mo>∧</mo><mi>B</mi></math> </th> <th> <math><mo>~</mo><mi>p</mi></math> </th> <th> <math><mo>~</mo><mi>p</mi><mo>∧</mo><mi>q</mi><mo>=</mo><mi>C</mi></math> </th> <th> <math><mfenced separators="|"><mrow><mi>A</mi><mo>∧</mo><mi>B</mi></mrow></mfenced><mo>∨</mo><mi>C</mi></math> </th> </tr> </thead> <tbody> <tr> <td>T</td> <td>T</td> <td>T</td> <td>T</td> <td>F</td> <td>T</td> <td>T</td> <td>F</td> <td>F</td> <td>T</td> </tr> <tr> <td>T</td> <td>T</td> <td>F</td> <td>T</td> <td>T</td> <td>T</td> <td>T</td> <td>F</td> <td>F</td> <td>T</td> </tr> <tr> <td>T</td> <td>F</td> <td>T</td> <td>F</td> <td>F</td> <td>F</td> <td>F</td> <td>F</td> <td>F</td> <td>F</td> </tr> <tr> <td>T</td> <td>F</td> <td>F</td> <td>F</td> <td>T</td> <td>T</td> <td>F</td> <td>F</td> <td>F</td> <td>F</td> </tr> <tr> <td>F</td> <td>T</td> <td>T</td> <td>F</td> <td>F</td> <td>F</td> <td>F</td> <td>T</td> <td>T</td> <td>T</td> </tr> <tr> <td>F</td> <td>T</td> <td>F</td> <td>F</td> <td>T</td> <td>T</td> <td>F</td> <td>T</td> <td>T</td> <td>T</td> </tr> <tr> <td>F</td> <td>F</td> <td>T</td> <td>F</td> <td>F</td> <td>F</td> <td>F</td> <td>T</td> <td>F</td> <td>F</td> </tr> <tr> <td>F</td> <td>F</td> <td>F</td> <td>F</td> <td>T</td> <td>T</td> <td>F</td> <td>T</td> <td>F</td> <td>F</td> </tr> </tbody> </table>

</details>

---

### Q234. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statement is contingency?

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mo>∼</mo><mi>q</mi></math>
- **(B)** <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mo>∼</mo><mi>p</mi></math>
- **(C)** <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mo>∼</mo><mi>q</mi></math>
- **(D)** <math><mi>p</mi><mo>→</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mo>∼</mo><mi>q</mi></math>**

**Detailed Solution:**

Key Idea : A statement which is neither a tautology nor a contradiction is a contingency. 
Option (1) <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mo>∼</mo><mi>q</mi></math>  
<math><mo>≡</mo><mi>p</mi><mo>∨</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∨</mo><mo>∼</mo><mi>q</mi></mrow></mfenced><mo>≡</mo><mi>p</mi><mo>∨</mo><mi>T</mi></math>  
<math><mo>≡</mo></math> T which is a tautology. 
Option (2) <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mo>∼</mo></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mo>∼</mo></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mo>∼</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mi>q</mi><mo>≡</mo><mi>T</mi><mo>∨</mo><mi>q</mi></math>  
<math><mo>≡</mo></math> T which is tautology 
Option (3) <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mo>∼</mo><mi>q</mi></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∧</mo><mo>∼</mo><mi>q</mi></mrow></mfenced><mo>≡</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mi>F</mi></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>q</mi></mrow></mfenced></math>  
If <math><mi>p</mi><mo>→</mo><mi>T</mi><mo>,</mo><mi>q</mi><mo>→</mo><mi>T</mi></math>  
Then <math><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>q</mi><mo>→</mo><mi>F</mi></math>  
If <math><mi>p</mi><mo>→</mo><mi>T</mi><mo>,</mo><mi>q</mi><mo>→</mo><mi>F</mi></math>  
Then <math><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>q</mi><mo>→</mo><mi>T</mi></math>  
So, <math><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>q</mi></mrow></mfenced></math> is a contingency. 
Therefore statement <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mo>∼</mo><mi>q</mi></math> is contingency.

</details>

---

### Q235. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The negation of <math><mi>“</mi><mo>∀</mo><mo>,</mo><mi>n</mi><mo>∈</mo><mi>N</mi><mo>,</mo><mi>n</mi><mo>+</mo><mn>7</mn><mo>&gt;</mo><mn>6</mn><mi>”</mi></math> is ….

**Options:**

- **(A)** <math><mo>∃</mo><mi>n</mi><mo>∈</mo><mi>N</mi></math> , such that <math><mi>n</mi><mo>+</mo><mn>7</mn><mo>≤</mo><mn>6</mn></math>
- **(B)** <math><mo>∃</mo><mi>n</mi><mo>∈</mo><mi>N</mi></math> , such that <math><mi>n</mi><mo>+</mo><mn>7</mn><mo>≥</mo><mn>6</mn></math>
- **(C)** <math><mo>∀</mo><mi>n</mi><mo>∈</mo><mi>N</mi><mo>,</mo><mi>n</mi><mo>+</mo><mn>7</mn><mo>≤</mo><mn>6</mn></math>
- **(D)** <math><mo>∃</mo><mi>n</mi><mo>∈</mo><mi>N</mi><mo>,</mo></math> such that <math><mi>n</mi><mo>+</mo><mn>7</mn><mo>&lt;</mo><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>∃</mo><mi>n</mi><mo>∈</mo><mi>N</mi></math> , such that <math><mi>n</mi><mo>+</mo><mn>7</mn><mo>≤</mo><mn>6</mn></math>**

**Detailed Solution:**

Key Idea – The negation of the quantifier For every is there exists. 
Given statements <math><mo>∀</mo><mi>”</mi><mi>n</mi><mo>∈</mo><mi>N</mi><mi>”</mi></math> such than <math><mi>n</mi><mo>+</mo><mn>7</mn><mo>&gt;</mo><mn>6</mn><mi>”</mi></math>  
<math><mo>∴</mo></math> The negation of the given statement is 
<math><mo>∃</mo><mi>n</mi><mo>∈</mo><mi>N</mi><mo>,</mo></math> such that <math><mi>n</mi><mo>+</mo><mn>7</mn><mo>≤</mo><mn>6</mn></math>

</details>

---

### Q236. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If p and q true and r and s are false statements, then which of the following is true?

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mi>q</mi><mo>∧</mo><mi>r</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∧</mo><mi>s</mi></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>→</mo><mi>q</mi></mrow></mfenced><mo>→</mo><mfenced separators="|"><mrow><mi>r</mi><mo>∧</mo><mi>s</mi></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mi>p</mi><mo>→</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>r</mi><mo>↔</mo><mi>s</mi></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>r</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>q</mi><mo>-</mo><mo>∨</mo><mi>s</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced separators="|"><mrow><mi>p</mi><mo>→</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>r</mi><mo>↔</mo><mi>s</mi></mrow></mfenced></math>**

**Detailed Solution:**

We have statements <math><mi>p</mi><mo>,</mo><mi>q</mi><mo>→</mo><mi>T</mi><mi></mi></math> and <math><mi>r</mi><mo>,</mo><mi>s</mi><mo>→</mo><mi>F</mi></math>  
Option (a) <math><mfenced separators="|"><mrow><mi>q</mi><mo>∧</mo><mi>r</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∧</mo><mi>s</mi></mrow></mfenced><mo>≡</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∧</mo><mi>F</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>F</mi><mo>∧</mo><mi>F</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mi>F</mi><mo>∨</mo><mi>F</mi><mo>≡</mo><mi>F</mi></math>  
Option (b) <math><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>→</mo><mi>q</mi></mrow></mfenced><mo>↔</mo><mfenced separators="|"><mrow><mi>r</mi><mo>∧</mo><mi>s</mi></mrow></mfenced><mo>≡</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>→</mo><mfenced separators="|"><mrow><mi>r</mi><mo>∨</mo><mi>s</mi></mrow></mfenced></math>  
<math><mfenced separators="|"><mrow><mo>∵</mo><mi>p</mi><mo>→</mo><mi>q</mi><mo>≡</mo><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mi>v</mi><mi>q</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>r</mi><mo>∧</mo><mi>s</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>r</mi><mo>∧</mo><mi>s</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mfenced separators="|"><mrow><mo>∵</mo><mi>p</mi><mo>↔</mo><mi>q</mi><mo>≡</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mi>p</mi><mi>v</mi><mo>-</mo><mi>q</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mo>∼</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∨</mo><mi>T</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>F</mi><mo>∧</mo><mi>F</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi>T</mi><mo>∨</mo><mi>F</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>F</mi><mo>∧</mo><mi>F</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mi>F</mi><mo>∨</mo><mi>F</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∨</mo><mi>T</mi></mrow></mfenced><mo>≡</mo><mi>F</mi><mo>∧</mo><mi>T</mi><mo>≡</mo><mi>F</mi></math>  
Option (c) <math><mfenced separators="|"><mrow><mi>p</mi><mo>→</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>r</mi><mo>↔</mo><mi>s</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mo>∼</mo><mi>r</mi><mo>∨</mo><mi>s</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mi>r</mi><mo>∨</mo><mo>∼</mo><mi>s</mi></mrow></mfenced></mrow></mfenced><mfenced separators="|"><mrow><mo>∵</mo><mi>p</mi><mo>→</mo><mi>q</mi><mo>≡</mo><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mi>F</mi><mo>∨</mo><mi>T</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi>T</mi><mo>∨</mo><mi>F</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mi>F</mi><mo>∨</mo><mi>T</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>≡</mo><mi>T</mi><mo>∨</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∧</mo><mi>T</mi></mrow></mfenced><mo>≡</mo><mi>T</mi><mo>∨</mo><mi>T</mi><mo>≡</mo><mi>T</mi></math>  
Option (d) do similar as option (a).

</details>

---

### Q237. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statement pattern is a tautology?

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mi>p</mi><mo>→</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mi>q</mi></math>
- **(B)** <math><mi>p</mi><mo>→</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∨</mo><mi>p</mi></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>→</mo><mi>q</mi></math>
- **(D)** <math><mi>p</mi><mo>∨</mo><mfenced separators="|"><mrow><mi>q</mi><mo>→</mo><mi>p</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>p</mi><mo>→</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∨</mo><mi>p</mi></mrow></mfenced></math>**

**Detailed Solution:**

Option <math><mfenced separators="|"><mrow><mi>a</mi></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mi>p</mi><mo>→</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mi>q</mi></math>  
<math><mo>=</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∨</mo><mi>q</mi></math>  
<math><mo>=</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced></math>  
It is not a tautology since if p is true and q is false then <math><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced></math> is false. 
Option <math><mfenced separators="|"><mrow><mi>b</mi></mrow></mfenced><mo>,</mo><mi>p</mi><mo>→</mo><mo>=</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∨</mo><mi>p</mi></mrow></mfenced></math>  
<math><mo>=</mo><mo>∼</mo><mi>p</mi><mo>∨</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∨</mo><mi>p</mi></mrow></mfenced></math>  
<math><mo>=</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>p</mi></mrow></mfenced><mo>∨</mo><mi>q</mi></math>  
<math><mi>T</mi><mo>∨</mo><mi>q</mi><mfenced separators="|"><mrow><mo>∵</mo><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>p</mi><mo>≡</mo><mi>T</mi></mrow></mfenced></math>  
It is a tautology since if q is true or false then <math><mi>T</mi><mo>∨</mo><mi>q</mi></math> must be true. 
Similarly, check other options.

</details>

---

### Q238. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

“If two triangles are congruent, then their areas are equal” is the given statement then the contrapositive of, the inverse of the given statement is

**Options:**

- **(A)** If areas of two triangles are not equal then they are congruent
- **(B)** If two triangles are not congruent then their areas are equal
- **(C)** If two triangles are not congruent then their areas are not equal
- **(D)** If areas of two triangles are equal then they are congruent

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If areas of two triangles are equal then they are congruent**

**Detailed Solution:**

Key Idea Use <math><mi>p</mi><mo>→</mo><mi>q</mi></math> then inverse of it is 
<math><mo>∼</mo><mi>p</mi><mo>→</mo><mo>∼</mo><mi>q</mi></math> and contrapositive is <math><mo>∼</mo><mi>q</mi><mo>→</mo><mo>∼</mo><mi>p</mi></math>  
The inverse of the given statement: “If two triangles are not congruent, then their areas are not equal.” 
<math><mo>∴</mo></math> The contrapositive of the inverse of the given statement : If areas of two triangles are equal, then are congruent.

</details>

---

### Q239. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let a: <math><mi></mi><mo>∼</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>r</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>q</mi><mo>∨</mo><mi>s</mi></mrow></mfenced></math> and <math><mi>b</mi><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>s</mi></mrow></mfenced><mo>↔</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∧</mo><mi>r</mi></mrow></mfenced></math> . If the truth values of p and q are true and that of r and s are false, then the truth values of a and b are respectively…

**Options:**

- **(A)** F, F
- **(B)** T, T
- **(C)** T, F
- **(D)** F, T

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) F, F**

**Detailed Solution:**

Key Idea Use <math><mi>p</mi><mo>→</mo><mi>q</mi><mo>≡</mo><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></math> and <math><mi>p</mi><mo>↔</mo><mi>q</mi><mo>≡</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mo>∼</mo><mi>q</mi></mrow></mfenced></math>  
Given, <math><mi>p</mi><mo>,</mo><mi>q</mi><mo>→</mo><mi>T</mi></math> and <math><mi>r</mi><mo>,</mo><mi>s</mi><mo>→</mo><mi>F</mi></math>  
<math><mo>∴</mo><mi>a</mi><mo>:</mo><mo>∼</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∧</mo><mo>∼</mo><mi>r</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>q</mi><mo>∨</mo><mi>s</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mo>∼</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∧</mo><mi>T</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>F</mi><mo>∨</mo><mi>F</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mo>∼</mo><mfenced separators="|"><mrow><mi>T</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>F</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mi>F</mi><mo>∨</mo><mi>F</mi><mo>≡</mo><mi>F</mi></math>  
and <math><mi>b</mi><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>s</mi></mrow></mfenced><mo>→</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∧</mo><mi>r</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mo>∼</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>s</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∧</mo><mi>r</mi></mrow></mfenced></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mi>s</mi></mrow></mfenced><mo>∨</mo><mo>∼</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∧</mo><mi>r</mi></mrow></mfenced></mrow></mfenced></math>  
<math><mo>∵</mo><mi>p</mi><mo>↔</mo><mi>q</mi><mo>≡</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mi>p</mi><mo>∨</mo><mo>∼</mo><mi>q</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mo>∼</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∨</mo><mi>F</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∧</mo><mi>F</mi></mrow></mfenced></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∨</mo><mi>F</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∧</mo><mi>F</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mfenced separators="|"><mrow><mi>F</mi><mo>∨</mo><mi>F</mi></mrow></mfenced><mo>∧</mo><mfenced separators="|"><mrow><mi>T</mi><mo>∨</mo><mi>T</mi></mrow></mfenced></math>  
<math><mo>≡</mo><mi>F</mi><mo>∧</mo><mi>T</mi><mo>≡</mo><mi>F</mi></math>

</details>

---

### Q240. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

The negation of the statement : "Getting above <math><mn>95</mn><mi>%</mi></math> marks is necessary condition for Hema to get the admission in good college".

**Options:**

- **(A)** Hema gets above <math><mn>95</mn><mi>%</mi></math> marks but she does not get the admission condition for Hema to get the admission in good college."
- **(B)** Hema does not get above <math><mn>95</mn><mi>%</mi></math> marks and she gets admission in good college
- **(C)** If Hema does not get above <math><mn>95</mn><mi>%</mi></math>  marks then she will not get the admission in good college.
- **(D)** Hema does not get above <math><mn>95</mn><mi>%</mi></math>  marks or she gets the admission in good college.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Hema does not get above <math><mn>95</mn><mi>%</mi></math> marks and she gets admission in good college**

**Detailed Solution:**

Getting 95% is a necessary condition and not a sufficient condition.
It Means, If Hema gets admission then she got more than 95% marks.
Hence negation of this statement is;
Hema does not get above 95% and she gets admission in good college

</details>

---

### Q241. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

The compound statement <math> <mrow> <mi>p</mi><mo>∧</mo><mrow><mo>(</mo> <mrow> <mo>~</mo><mi>p</mi><mo>∧</mo><mi>q</mi> </mrow> <mo>)</mo></mrow> </mrow> </math> is

**Options:**

- **(A)** A tautology
- **(B)** A contradiction
- **(C)** Equivalent to <math> <mrow> <mi>p</mi><mo>∧</mo><mi>q</mi> </mrow> </math>
- **(D)** Equivalent to <math><mi>p</mi><mo>∨</mo><mi>q</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A contradiction**

**Detailed Solution:**

Given compound statement is
<math> <mrow> <mrow><mo>(</mo> <mrow> <mi>p</mi><mo>∧</mo><mo>~</mo><mi>p</mi></mrow> <mo>)</mo></mrow><mo>∧</mo><mi>q</mi></mrow> </math>
<math> <mo>=</mo><mrow> <mi>F</mi><mo>∧</mo><mi>q</mi></mrow> </math>
<math> <mrow> <mo>=</mo><mi>F</mi> </mrow></math>(contradiction)

</details>

---

### Q242. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

The contrapositive of the statement: "If the weather is fine then my friends will come and we go for a picnic." is

**Options:**

- **(A)** The weather is fine but my friends will not come or we do not go for a picnic.
- **(B)** If my friends do not come or we do not go for picnic then weather will not be fine.
- **(C)** If the weather is not fine then my friends will not come or we do not go for a picnic.
- **(D)** The weather is not fine but my friends will come and we go for a picnic.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) If my friends do not come or we do not go for picnic then weather will not be fine.**

**Detailed Solution:**

<math> <mrow> <mi>p</mi><mo>→</mo><mrow><mo>(</mo> <mrow> <mi>q</mi><mo>∧</mo><mi>r</mi></mrow> <mo>)</mo></mrow></mrow> </math>
Contrapositive <math> <mrow> <mrow><mo>(</mo> <mrow> <mo>∽</mo><mrow><mo>(</mo> <mrow> <mi>q</mi><mo>∧</mo><mi>r</mi></mrow> <mo>)</mo></mrow></mrow> <mo>)</mo></mrow><mo>→</mo><mo>∽</mo><mi>p</mi></mrow> </math>
<math> <mrow> <mo>∴</mo><mrow><mo>(</mo> <mrow> <mo>∽</mo><mi>q</mi><mo>∨</mo><mo>∽</mo><mi>r</mi></mrow> <mo>)</mo></mrow><mo>→</mo><mo>∽</mo><mi>p</mi></mrow> </math>
If my friends do not come or we do not go for picnic then weather will not be fine.

</details>

---

### Q243. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>c</mi></math> denotes the contradiction then dual of the compounds statement <math><mo>∽</mo><mi>p</mi><mo>∧</mo><mo>(</mo><mi>q</mi><mo>∨</mo><mi>c</mi><mo>)</mo></math> is

**Options:**

- **(A)** <math><mo>∽</mo><mi>p</mi><mo>∨</mo><mo>(</mo><mi>q</mi><mo>∧</mo><mi>t</mi><mo>)</mo></math>
- **(B)** <math><mo>∽</mo><mi>p</mi><mo>∧</mo><mo>(</mo><mi>q</mi><mo>∨</mo><mi>t</mi><mo>)</mo></math>
- **(C)** <math><mi>p</mi><mo>∨</mo><mo>(</mo><mo>∽</mo><mi>q</mi><mo>∨</mo><mi>t</mi><mo>)</mo></math>
- **(D)** <math><mi> </mi><mo>∽</mo><mi>p</mi><mo>∨</mo><mo>(</mo><mi>q</mi><mo>∧</mo><mi>c</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mo>∽</mo><mi>p</mi><mo>∨</mo><mo>(</mo><mi>q</mi><mo>∧</mo><mi>t</mi><mo>)</mo></math>**

**Detailed Solution:**

Dual of  <math><mo>∽</mo><mi>p</mi><mo>∧</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∨</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mo>∽</mo><mi>p</mi><mo>∨</mo><mo>(</mo><mi>q</mi><mo>∧</mo><mi>t</mi><mo>)</mo></math>

</details>

---

### Q244. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statement pattern is a tautology?

**Options:**

- **(A)** <math><mi>p</mi><mi> </mi><mo>∨</mo><mo>(</mo><mi>q</mi><mo>→</mo><mi>p</mi><mo>)</mo></math>
- **(B)** <math><mo>∽</mo><mi>q</mi><mo>→</mo><mo>∽</mo><mi>p</mi></math>
- **(C)** <math><mfenced separators="|"><mrow><mi>q</mi><mo>→</mo><mi>p</mi></mrow></mfenced><mi> </mi><mo>∨</mo><mi> </mi><mfenced separators="|"><mrow><mo>∽</mo><mi>p</mi><mo>↔</mo><mi>q</mi></mrow></mfenced></math>
- **(D)** <math><mi>p</mi><mi> </mi><mo>∧</mo><mo>∽</mo><mi>p</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced separators="|"><mrow><mi>q</mi><mo>→</mo><mi>p</mi></mrow></mfenced><mi> </mi><mo>∨</mo><mi> </mi><mfenced separators="|"><mrow><mo>∽</mo><mi>p</mi><mo>↔</mo><mi>q</mi></mrow></mfenced></math>**

**Detailed Solution:**

It can be done using truth or using rules of logic.
(i) <math><mi>p</mi><mi> </mi><mo>∨</mo><mfenced separators="|"><mrow><mi>q</mi><mo>→</mo><mi>p</mi></mrow></mfenced><mi> </mi><mo>≡</mo><mi>p</mi><mo>∨</mo><mfenced separators="|"><mrow><mo>∽</mo><mi>q</mi><mo>∨</mo><mi>p</mi></mrow></mfenced><mo>≡</mo><mi>p</mi><mo>∨</mo><mi>p</mi><mo>∨</mo><mo>∽</mo><mi>q</mi></math>
<math><mo>≡</mo><mi>p</mi><mo>∨</mo><mi> </mi><mo>∽</mo><mi>q</mi></math>
(ii) <math><mo>∽</mo><mi>q</mi><mo>→</mo><mi> </mi><mo>∽</mo><mi>p</mi><mo>≡</mo><mi>q</mi><mo>∨</mo><mi> </mi><mo>∽</mo><mi>p</mi></math>
(iv) <math><mi>p</mi><mo>∧</mo><mi> </mi><mo>∽</mo><mi>p</mi><mo>≡</mo><mi>F</mi></math>
So left is (iii)
 <table border="1">	<tbody>		<tr>			<td>p</td>			<td>q</td>			<td><math><mi>q</mi><mi> </mi><mo>→</mo><mi>p</mi></math></td>			<td><math><mo>∽</mo><mi>p</mi></math></td>			<td><math><mo>∽</mo><mi>p</mi><mo>↔</mo><mi>q</mi></math></td>			<td><math><mfenced separators="|"><mrow><mi>q</mi><mo>→</mo><mi>p</mi></mrow></mfenced><mo>∨</mo><mfenced separators="|"><mrow><mo>∽</mo><mi>p</mi><mo>↔</mo><mi>q</mi></mrow></mfenced></math></td>		</tr>		<tr>			<td>T</td>			<td>T</td>			<td>T</td>			<td>F</td>			<td>F</td>			<td>T</td>		</tr>		<tr>			<td>T</td>			<td>F</td>			<td>T</td>			<td>F</td>			<td>T</td>			<td>T</td>		</tr>		<tr>			<td>F</td>			<td>T</td>			<td>F</td>			<td>T</td>			<td>T</td>			<td>T</td>		</tr>		<tr>			<td>F</td>			<td>F</td>			<td>T</td>			<td>T</td>			<td>F</td>			<td>T</td>		</tr>	</tbody></table>

</details>

---

### Q245. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

The statement pattern <math> <mrow> <mo stretchy="false">(</mo><mo>∽</mo><mi>p</mi><mo>∧</mo><mi>q</mi><mo stretchy="false">)</mo> </mrow> </math> is a logically equivalent to

**Options:**

- **(A)** <math> <mrow><mo>(</mo> <mrow> <mi>p</mi><mo>∨</mo><mi>q</mi> </mrow> <mo>)</mo></mrow><mo>∨</mo><mo>∽</mo><mi>q</mi> </math>
- **(B)** <math><mo>(</mo><mi>p</mi><mo>∨</mo><mi>q</mi><mo>)</mo><mo>∧</mo><mo>∽</mo><mi>p</mi></math>
- **(C)** <math > <mrow><mo>(</mo>  <mrow>   <mi>p</mi><mo>&#x2227;</mo><mi>q</mi>  </mrow> <mo>)</mo></mrow><mo>&#x2192;</mo><mi>p</mi></math>
- **(D)** <math><mi> </mi><mo>(</mo><mi>p</mi><mo>∨</mo><mi>q</mi><mo>)</mo><mo>→</mo><mi>p</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>(</mo><mi>p</mi><mo>∨</mo><mi>q</mi><mo>)</mo><mo>∧</mo><mo>∽</mo><mi>p</mi></math>**

**Detailed Solution:**

Hence <math><mfenced separators="|"><mrow><mi>p</mi><mi> </mi><mo>∨</mo><mi>q</mi></mrow></mfenced><mo>∧</mo><mi> </mi><mo>∽</mo><mi>p</mi><mo>=</mo><mfenced separators="|"><mrow><mi>p</mi><mi> </mi><mo>∧</mo><mi> </mi><mo>∽</mo><mi>p</mi></mrow></mfenced><mo>∨</mo><mo>(</mo><mi>q</mi><mo>∧</mo><mi> </mi><mo>∽</mo><mi>p</mi><mo>)</mo></math> .......... Distributive law
<math><mo>=</mo><mi>F</mi><mo>∨</mo><mfenced separators="|"><mrow><mi>q</mi><mo>∧</mo><mi> </mi><mo>∽</mo><mi>p</mi></mrow></mfenced></math> Complementary law
<math><mo>=</mo><mi>q</mi><mo>∧</mo><mi> </mi><mo>∽</mo><mi>p</mi></math> Identify law
<math><mo>=</mo><mo>∽</mo><mi>p</mi><mo>∧</mo><mi>q</mi></math> Commutative law

</details>

---

### Q246. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

Symbolic form of the given switching circuit is equivalent to ________



<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/kljkksgsjhkshfhshdgfsj.JPG" style="width: 350px; height: 136px;" />

**Options:**

- **(A)** <math><mi>p</mi><mi> </mi><mo>∨</mo><mo>∼</mo><mi>q</mi></math>
- **(B)** <math><mi>p</mi><mi> </mi><mo>&#x2227;</mo><mo>∼</mo><mi>q</mi></math>
- **(C)** <math><mi>p</mi><mo>↔</mo><mi>q</mi></math>
- **(D)** <math><mo>∼</mo><mfenced separators="|"><mrow><mi>p</mi><mo>↔</mo><mi>q</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>∼</mo><mfenced separators="|"><mrow><mi>p</mi><mo>↔</mo><mi>q</mi></mrow></mfenced></math>**

**Detailed Solution:**

Let <math><msub><mrow><mi>s</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>≡</mo><mi>p</mi></math>
<math><msub><mrow><mi>s</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>≡</mo><mi>q</mi></math>
<math><mo>⇒</mo></math> Given circuit represents the expression
<math><mi> </mi><mi> </mi><mfenced separators="|"><mrow><mi>p</mi><mi> </mi><mo>∧</mo><mo>∼</mo><mi>q</mi></mrow></mfenced><mi> </mi><mo>∨</mo><mfenced separators="|"><mrow><mo>∼</mo><mi>p</mi><mo>∧</mo><mi>q</mi></mrow></mfenced></math>
<math><mo>⇔</mo><mi> </mi><mi> </mi><mi> </mi><mo>∼</mo><mfenced separators="|"><mrow><mi>p</mi><mo>↔</mo><mi>q</mi></mrow></mfenced></math>

</details>

---

### Q247. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

Which of the following quantified statement is true?

**Options:**

- **(A)** The square of every real number is positive
- **(B)** There exists a real number whose square is negative
- **(C)** There exists a real number whose square is not positive
- **(D)** Every real number is rational

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) There exists a real number whose square is not positive**

**Detailed Solution:**

<math> <mrow> <msup> <mtext>x</mtext> <mn>2</mn> </msup> <mo>≥</mo> <mn>0</mn> </mrow> </math> for all real numbers x
For <math> <mrow> <mtext>x</mtext> <mo>=</mo> <mn>0</mn> <mtext>,</mtext> <mspace width="0.5em"></mspace> <msup> <mtext>x</mtext> <mn>2</mn> </msup> <mo>=</mo> <mn>0</mn> </mrow> </math> (not positive)

</details>

---

### Q248. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>p</mi></math>: Every square is a rectangle



<math><mi>q</mi></math>: Every rhombus is a kite then truth values of <math><mi>p</mi><mo>→</mo><mi>q</mi></math> and <math><mi>p</mi><mo>↔</mo><mi>q</mi></math> are ____ and _____ respectively.

**Options:**

- **(A)** <math > <mrow>  <mi>F</mi><mo>,</mo><mi>F</mi> </mrow></math>
- **(B)** <math > <mrow>  <mi>T</mi><mo>,</mo><mi>F</mi> </mrow></math>
- **(C)** <math > <mrow>  <mi>F</mi><mo>,</mo><mi>T</mi> </mrow></math>
- **(D)** <math > <mrow>  <mi>T</mi><mo>,</mo><mi>T</mi> </mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math > <mrow>  <mi>T</mi><mo>,</mo><mi>T</mi> </mrow></math>**

**Detailed Solution:**

P : Every square is a rectangle <math><mo>→</mo><mi>T</mi></math>
q : Every rhombus is a kite <math><mo>→</mo><mi>T</mi></math>
<math><mo>∴</mo><mi>p</mi><mo>→</mo><mi>q</mi><mo>≡</mo><mi>T</mi></math>
<math><mi>p</mi><mo>↔</mo><mi>q</mi><mo>≡</mo><mi>T</mi></math>

</details>

---

### Q249. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

The value of $(1+\Delta)(1-\nabla)$ is

**Options:**

- **(A)** 0
- **(B)** $-1$
- **(C)** 1
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

We have, $(1+\Delta)(1-\nabla) f(x)$
$$
\begin{array}{l}
=(1+\Delta)\{(1-\nabla) f(x)\} \\
=(1+\Delta)\{f(x)-\nabla f(x)\} \\
=(1+\Delta)[f(x)-\{f(x)-f(x-h)\}] \\
=(1+\Delta) f(x-h)=E f(x-h) \\
\quad[\because(E=1+\Delta)] \\
=f(x)=1 \cdot f(x)
\end{array}
$$
Thus, $(1+\Delta)(1-\nabla) f(x)=1 \cdot f(x)$, for any function $f(x)$.
$$
\therefore \quad(1+\Delta)(1+\nabla)=1
$$

</details>

---

### Q250. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `3`

For the circuit show below, the Boolean polynomial is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/D0fkh4WOwwH80pDH7EHgeKoOSrlZCC8QJP6MQlIIdBU.original.fullsize.png">

**Options:**

- **(A)** $(\sim p \vee q) \vee(p \vee \sim q)$
- **(B)** $(\sim p \wedge q) \wedge(p \wedge q)$
- **(C)** $(\sim p \wedge \sim q) \wedge(q \wedge p)$
- **(D)** $(\sim p \wedge q) \vee(p \wedge \sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim p \wedge q) \vee(p \wedge \sim q)$**

**Detailed Solution:**

Since, $\sim p$ and $q$ both switch also are in series
$$
\Rightarrow \quad(\sim p \wedge q)
$$
and $p$ and $\sim q$ both switch also are in series
$$
\Rightarrow \quad(p \wedge \sim q)
$$
Both Eqs. (i) and (ii) are parallel switch
$$
\Rightarrow \quad(\sim p \wedge q) \vee(p \wedge \sim q)
$$

</details>

---

### Q251. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

In a Boolean Algebra $B$, for all $x$, $y$ in $B$, $x \wedge(x \vee y)$ is equal to

**Options:**

- **(A)** $y$
- **(B)** $x$
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x$**

**Detailed Solution:**

$x \wedge(x \vee y)$
$=(x \wedge x) \vee(x \wedge y)$ by distribution law'
$=x \vee(x \wedge y)$ 'by idempotent law'
$=(x \vee f)$ 'by contradiction law'
$=x$

</details>

---

### Q252. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

The inverse of the proposition $(p \wedge-q) \Rightarrow r$ is

**Options:**

- **(A)** $\sim r \Rightarrow \sim p \vee q$
- **(B)** $\sim p \vee q \Rightarrow \sim r$
- **(C)** $r \Rightarrow p \wedge \sim q$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sim p \vee q \Rightarrow \sim r$**

**Detailed Solution:**

Inverse of $p \Rightarrow q$ is $\sim p \Rightarrow \sim q$
$\therefore$ Inverse of $(p \wedge \sim q) \Rightarrow \mathrm{r}$ is
$$
\sim(p \wedge \sim q) \Rightarrow \sim r
$$
i.e., $\quad(\sim p \vee q) \Rightarrow \wedge \sim r$

</details>

---

### Q253. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

The propositions $(p \Rightarrow \sim p) \wedge(\sim p \Rightarrow p)$ is a

**Options:**

- **(A)** tautology and contradiction
- **(B)** neither tautology nor contradiction
- **(C)** contradiction
- **(D)** tautology

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) contradiction**

**Detailed Solution:**

\begin{array}{c|c|c|c|c}
\hlinep & \sim p & p \Rightarrow \sim p & \sim p \Rightarrow p & (p \Rightarrow \sim p) \wedge(\sim p \Rightarrow p) \\
\hline \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\hline
\end{array}
Clearly,$(p \Rightarrow \sim p) \wedge(\sim p \Rightarrow p)$ is a
contradiction.

</details>

---

### Q254. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

$(p \wedge q) \vee \sim p$ is equivalent to

**Options:**

- **(A)** $\sim p \wedge q$
- **(B)** $\sim p \vee q$
- **(C)** $p \wedge q$
- **(D)** $p \vee q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sim p \vee q$**

**Detailed Solution:**

$(p \wedge q) \vee \sim p=\sim p \vee(p \wedge q)$
[By commutative law] $\begin{array}{lr}=(\sim p \vee p) \wedge(\sim p \vee q) & \text { [By distributive law] } \\ =(p \vee \sim p) \wedge(\sim p \vee q) & \text { [By commutative law] }\end{array}$
$=t \wedge(\sim p \vee q)$
[By complement law]
$=\sim p \vee q$
[By identity law]

</details>

---

### Q255. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

If $p, q, r$ are single propositions with truth values $T, F, F, \quad$ then the truth value of $(p \wedge \sim q) \rightarrow(\sim p \vee r)$ is

**Options:**

- **(A)** $T$
- **(B)** $\bar{F}$
- **(C)** Cannot find
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\bar{F}$**

**Detailed Solution:**

\begin{array}{c|c|c|c|c|c|c|c}
\hlinep & q & r & \sim q & \sim p & p \wedge \sim q & \sim p \vee r & (p \wedge \sim q) \rightarrow \\
& & & & & & & (\sim p \vee r) \\
\hlineT & F & F & T & F & T & F & F \\
\hline
\end{array}

</details>

---

### Q256. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `3`

The output of the following circuit is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/buWL4OT4ZMQwnzzkewfspoaEG0mfW4Dnsyj6bBgYaWc.original.fullsize.png">

**Options:**

- **(A)** $p$
- **(B)** $q$
- **(C)** $\sim p$
- **(D)** $p+q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $q$**

**Detailed Solution:**

Output $=(p+-p) \cdot q=1 \cdot q=q$

</details>

---

### Q257. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

Simplify $(p \vee q) \wedge(p \vee \sim q)$

**Options:**

- **(A)** $p$
- **(B)** $T$
- **(C)** $\bar{F}$
- **(D)** $q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $p$**

**Detailed Solution:**

$(p \vee q) \wedge(p \vee \sim q)$
$=p \vee(q \wedge \sim q) \quad$ (distributive law) $=p \vee 0$
(complement law)
$=p$
(0 is indentity for $\vee$ )

</details>

---

### Q258. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `3`

Simplify the following circuit and find the boolean polynomial.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/dr5jrQkDObPEoHpfcyBIXkbsTQ6MhS0iHYnAuX5R454.original.fullsize.png">

**Options:**

- **(A)** $p \vee(q \wedge r)$
- **(B)** $p \wedge(q \vee r)$
- **(C)** $p \vee(q \vee r)$
- **(D)** $p \wedge(q \wedge r)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $p \vee(q \wedge r)$**

**Detailed Solution:**

$(p \vee q) \wedge(p \vee r)=p \vee(q \wedge r)$

</details>

---

### Q259. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

$\sim(\sim p \rightarrow q) \equiv$

**Options:**

- **(A)** $p \wedge \sim q$
- **(B)** $\sim p \wedge q$
- **(C)** $\sim p \wedge \sim q$
- **(D)** $\sim p \vee \sim q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sim p \wedge \sim q$**

**Detailed Solution:**

$\sim(\sim p \rightarrow q)=\sim p \wedge \sim q$

</details>

---

### Q260. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

Negation of the conditional, "If it rains, I shall go to school" is

**Options:**

- **(A)** It rains and I shall go to school
- **(B)** It rains and I shall not go to school
- **(C)** It does not rains and I shall go to school
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) It rains and I shall not go to school**

**Detailed Solution:**

Let $p:$ It rains, $q:$ I shall go to school Thus, we have $p \Rightarrow q$ Its negation is $\sim(p \Rightarrow q)$ ie, $p \wedge \sim q$ ie, it rains and I shall not go to school.

</details>

---

### Q261. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

Dual of $\left(x^{\prime} \vee y^{\prime}\right)=x \wedge y$ is

**Options:**

- **(A)** $\left(x^{\prime} \vee y^{\prime}\right)=x \vee y_{1}$
- **(B)** $\left(x^{\prime} \wedge y^{\prime}\right)^{\prime}=x \vee y$
- **(C)** $\left(x^{\prime} \wedge y^{\prime}\right)^{\prime}=x \wedge y$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(x^{\prime} \wedge y^{\prime}\right)^{\prime}=x \vee y$**

**Detailed Solution:**

Dual of $\left(x^{\prime} \vee y^{\prime}\right)^{\prime}=x \wedge y$ is $\left(x^{\prime} \wedge y^{\prime}\right)^{\gamma}=x \vee y$

</details>

---

### Q262. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `3`

For the circuits shown below, the Boolean polynomial is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/uIMNuiEEvTXaiEBQObzkSU-3I0FjDvhf7VV7dwKcMqs.original.fullsize.png">

**Options:**

- **(A)** $(\sim p \vee q) \vee(p \vee \sim q)$
- **(B)** $(\sim p \wedge q) \wedge(p \wedge q)$
- **(C)** $(\sim p \wedge \sim q) \wedge(q \wedge p)$
- **(D)** $(\sim p \wedge q) \vee(p \wedge \sim q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\sim p \wedge q) \vee(p \wedge \sim q)$**

**Detailed Solution:**

For the given circuit, Boolean polynomial is $(\sim p \wedge q) \vee(p \wedge \sim q)$

</details>

---

### Q263. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

The dual of the statement $[p \vee(\sim q)] \wedge(\sim p)$ is

**Options:**

- **(A)** $p \vee(\sim q) \vee \sim p$
- **(B)** $(p \wedge \sim q) \vee \sim p$
- **(C)** $p \wedge \sim(q \vee \sim p)$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(p \wedge \sim q) \vee \sim p$**

**Detailed Solution:**

The dual of the given statement is $(p \wedge \sim q) \vee \sim p$

</details>

---

### Q264. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

In the usual notation the value of $\Delta \nabla$ is equal to

**Options:**

- **(A)** $\Delta-\nabla$
- **(B)** $\Delta+\nabla$
- **(C)** $\nabla-\Delta$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\Delta-\nabla$**

**Detailed Solution:**

Now, $\Delta \nabla f(x)=\Delta[f(x)-f(x-h)]$
$\therefore$
$$
\begin{aligned}
&=\Delta f(x)-\Delta f(x-h) \\
&=\Delta f(x)-[f(x)-f(x-h)] \\
&=\Delta f(x)-\nabla f(x) \\
\Delta \nabla &=\Delta-\nabla
\end{aligned}
$$

</details>

---

### Q265. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statement has the truth value ' $F^{\prime}$ ?

**Options:**

- **(A)** A quadratic equation has always a real root
- **(B)** The number of ways of seating 2 persons in two chairs out of $n$ persons in $P(n, 2)$.
- **(C)** The cube roots of unity are in GP
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A quadratic equation has always a real root**

**Detailed Solution:**

The roots of a quadratic equation can be imaginary.

</details>

---

