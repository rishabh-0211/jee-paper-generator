# JEE Advanced Mathematics - Probability

## Topic 5: Baye's Theorem

**Total Questions:** 8

---

### Q1. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `3`

A factory has a total of three manufacturing units, $M_1, M_2$, and $M_3$, which produce bulbs independent of each other. The units $M_1, M_2$, and $M_3$ produce bulbs in the proportions of 2:2:1, respectively. It is known that $20 \%$ of the bulbs produced in the factory are defective. It is also known that, of all the bulbs produced by $M_1, 15 \%$ are defective. Suppose that, if a randomly chosen bulb produced in the factory is found to be defective, the probability that it was produced by $M_2$ is $\frac{2}{5}$.
If a bulb is chosen randomly from the bulbs produced by $M_3$, then the probability that it is defective is ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.3**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/97BQBuYdwZ1cFsl6KOxQicZCxZeXrOpwtVO_jqqu2jk.original.fullsize.png">
Now given probability
$\begin{aligned}
& P\left(\frac{\text { Produced by } \mathrm{M}_2}{\text { defective }}\right)=\frac{\frac{40}{100} \times \frac{14-\mathrm{x}}{40}}{\frac{20}{100}}=\frac{2}{5} \\
& \Rightarrow \frac{14-\mathrm{x}}{40}=\frac{1}{5} \\
& \Rightarrow 14-\mathrm{x}=8 \\
& \Rightarrow \mathrm{x}=6
\end{aligned}$
So, the required probability
$=\frac{6}{20}=0.3$

</details>

---

### Q2. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

A student appears for a quiz consisting of only true-false type questions and answers all the questions. The student knows the answers of some questions and guesses the answers for the remaining questions. Whenever the student knows the answer of a question, he gives the correct answer. Assume that the probability of the student giving the correct answer for a question, given that he has guessed it, is $\frac{1}{2}$. Also assume that the probability of the answer for a question being guessed, given that the student's answer is correct, is $\frac{1}{6}$. Then the probability that the student knows the answer of a randomly chosen question is

**Options:**

- **(A)** $\frac{1}{12}$
- **(B)** $\frac{1}{7}$
- **(C)** $\frac{5}{7}$
- **(D)** $\frac{5}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{5}{7}$**

**Detailed Solution:**

$\mathrm{C} \rightarrow$ Correct
$\mathrm{G} \rightarrow$ Guess
$\mathrm{K} \rightarrow$ Knows
$\begin{array}{ll}\mathrm{P}\left(\frac{\mathrm{C}}{\mathrm{G}}\right)=\frac{1}{2} \quad, \quad \mathrm{P}\left(\frac{\mathrm{C}}{\mathrm{K}}\right)=1 \\\mathrm{P}\left(\frac{\mathrm{G}}{\mathrm{C}}\right)=\frac{1}{6}\end{array}$
$\begin{aligned} & \text { Let required probability }=\mathrm{x} \\ & \therefore \mathrm{P}\left(\frac{\mathrm{G}}{\mathrm{C}}\right)=\frac{(1-\mathrm{x}) \mathrm{P}\left(\frac{\mathrm{C}}{\mathrm{G}}\right)}{(1-\mathrm{x}) \mathrm{P}\left(\frac{\mathrm{C}}{\mathrm{G}}\right)+\mathrm{x} \cdot \mathrm{P}\left(\frac{\mathrm{C}}{\mathrm{K}}\right)} \\ & \frac{1}{6}=\frac{(1-\mathrm{x})\left(\frac{1}{2}\right)}{(1-\mathrm{x})\left(\frac{1}{2}\right)+(\mathrm{x})(1)} \\ & \Rightarrow \mathrm{x}=\frac{5}{7} \Rightarrow \text { Option (3) is correct. }\end{aligned}$

</details>

---

### Q3. JEE Advanced 2022 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Suppose that
Box-I contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> red, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> blue and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> green balls,
Box-ll contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math> red, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> blue and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> green balls,
Box-III contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> blue, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> green and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> yellow balls,
Box-IV contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> green, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math> orange and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> white balls.
A ball is chosen randomly from Box-l; call this ball <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is red then a ball is chosen randomly from Box-ll, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is blue then a ball is chosen randomly from Box-III, and if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is green then a ball is chosen randomly from Box-IV. The conditional probability of the event &#39;one of the chosen balls is white&#39; given that the event &#39;at least one of the chosen balls is green&#39; has happened, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>256</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>16</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>52</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>52</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mtext>Red&#160;from&#160;Box</mtext><mo>&#160;</mo><mi mathvariant="normal">I</mi></mrow></mfenced><mo>=</mo><mfrac><mn>8</mn><mn>16</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mtext>Blue&#160;from&#160;Box</mtext><mo>&#160;</mo><mi mathvariant="normal">I</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mtext>Green&#160;from&#160;Box</mtext><mo>&#160;</mo><mi mathvariant="normal">I</mi></mrow></mfenced><mo>=</mo><mfrac><mn>10</mn><mn>32</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>16</mn></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mtext>Green&#160;from&#160;Box</mtext><mo>&#160;</mo><mi>II</mi></mrow></mfenced><mo>=</mo><mfrac><mn>15</mn><mn>48</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mtext>Green&#160;from&#160;Box</mtext><mo>&#160;</mo><mi>III</mi></mrow></mfenced><mo>=</mo><mfrac><mn>12</mn><mn>16</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mtext>White&#160;from&#160;Box</mtext><mo>&#160;</mo><mi>IV</mi></mrow></mfenced><mo>=</mo><mfrac><mn>6</mn><mn>32</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>16</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/1ba88ef8-879e-4be5-846a-70dd18320a33-image.png" style="width: 416px; height: 250px;" /></p><p>Event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> : One of the chosen ball is white
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>:</mo></math> At least one of the chosen ball is green</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>A</mi><mi>B</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>B</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mn>5</mn><mn>16</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>16</mn></mfrac></mrow><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>15</mn><mn>48</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>16</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>16</mn></mfrac><mo>&#215;</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mn>52</mn></mfrac></math></p></blockquote>

</details>

---

### Q4. JEE Advanced 2016 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A computer producing factory has only two plants <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math>. Plant <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math> produces <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>%</mo></math> and plant <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math> produces <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>%</mo></math> of the total computers produced. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>%</mo></math> of computers produced in the factory turn out to be defective. It is known that, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(computer turns out to be defective given that it is produced in plant <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn><mi>P</mi></math>(computer turns out to be defective given that it is produced in plant <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math>).</p><p>Where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>E</mi></mfenced></math> denotes the probability of an event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>.</mo></math> A computer produced in the factory is randomly selected and it does not turn out to be defective. Then the probability that it is produced in plant <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math> is</p>

**Options:**

- **(A)** <math><mfrac><mrow><mn>36</mn></mrow><mrow><mn>73</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>47</mn></mrow><mrow><mn>79</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>78</mn></mrow><mrow><mn>93</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>75</mn></mrow><mrow><mn>83</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>78</mn></mrow><mrow><mn>93</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><msub><mi>T</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mn>20</mn><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><msub><mi>T</mi><mn>2</mn></msub></mfenced><mo>=</mo><mfrac><mn>80</mn><mn>100</mn></mfrac></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mfrac><mi>D</mi><msub><mi>T</mi><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mi>x</mi></math> (where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> represents defective units)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mfrac><mi>D</mi><msub><mi>T</mi><mn>1</mn></msub></mfrac></mfenced><mo>=</mo><mn>10</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mi>D</mi></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>100</mn></mfrac></math> (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><msub><mi>T</mi><mn>1</mn></msub></mfenced><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mfrac><mi>D</mi><msub><mi>T</mi><mn>1</mn></msub></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><msub><mi>T</mi><mn>2</mn></msub></mfenced><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mfrac><mi>D</mi><msub><mi>T</mi><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mn>100</mn></mfrac><mo>&#215;</mo><mn>10</mn><mi>x</mi><mo>+</mo><mfrac><mn>80</mn><mn>100</mn></mfrac><mo>&#215;</mo><mi>x</mi><mo>=</mo><mfrac><mn>7</mn><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>40</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mfrac><mi>D</mi><msub><mi>T</mi><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>40</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mfrac><mover><mi>D</mi><mo>-</mo></mover><msub><mi>T</mi><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mn>39</mn><mn>40</mn></mfrac><mo>=</mo></math>Probability of not defective, given that it is produced in plant <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mfrac><mi>D</mi><msub><mi>T</mi><mn>1</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mn>10</mn><mn>40</mn></mfrac><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mfrac><mover><mi>D</mi><mo>-</mo></mover><msub><mi>T</mi><mn>1</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mn>30</mn><mn>40</mn></mfrac></math></p><p>Now using Bayes&#39; theorem</p><p>Probability of computer from <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math> given that it is not defective :</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mfrac><msub><mi>T</mi><mn>2</mn></msub><mover><mi>D</mi><mo>-</mo></mover></mfrac></mfenced><mo>=</mo><mfrac><mrow><mfrac><mn>80</mn><mn>100</mn></mfrac><mo>&#215;</mo><mfrac><mn>39</mn><mn>40</mn></mfrac></mrow><mrow><mfrac><mn>20</mn><mn>100</mn></mfrac><mo>&#215;</mo><mfrac><mn>30</mn><mn>40</mn></mfrac><mo>+</mo><mfrac><mn>80</mn><mn>100</mn></mfrac><mo>&#215;</mo><mfrac><mn>39</mn><mn>40</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>78</mn><mn>93</mn></mfrac></math></p>

</details>

---

### Q5. JEE Advanced 2015 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></math> be the number of red and black balls, respectively, in box I. Let <math><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub></math> be the number of red and black balls, respectively, in box II.
One of the two boxes, box I and box II, was selected at random and a ball was drawn randomly out of this box. The balls was found to be red. If the probability that this red ball was drawn from box II is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> , then the correct option(s) with the possible values of <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub></math> is(are)

**Options:**

- **(A)** <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>3</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>3</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>5</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>15</mn></math>
- **(B)** <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>3</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>6</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>10</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>50</mn></math>
- **(C)** <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>8</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>6</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>5</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>20</mn></math>
- **(D)** <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>6</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>12</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>5</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>20</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>3</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>6</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>10</mn><mo>,</mo><mi> </mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>50</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image5-0e47e896-9b1e-46bf-b7e9-41b93902f118.jpg"/> 
 <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>+</mo><mi> </mi><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow></mfrac></math> 
 <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>+</mo><mi> </mi><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow></mfrac></math> 
(i)  <math><mi> </mi><mi>R</mi><mi>H</mi><mi>S</mi><mi> </mi><mfrac><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>20</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> 
(ii)  <math><mi>R</mi><mi>H</mi><mi>S</mi><mi> </mi><mfrac><mrow><mfrac><mrow><mn>10</mn></mrow><mrow><mn>60</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>10</mn></mrow><mrow><mn>60</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>9</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> 
(iii)  <math><mfrac><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>8</mn></mrow><mrow><mn>14</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>20</mn><mo>+</mo><mn>7</mn></mrow><mrow><mn>35</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>27</mn></mrow></mfrac></math> 
(iv)  <math><mfrac><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>6</mn></mrow><mrow><mn>18</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>5</mn><mo>+</mo><mn>3</mn></mrow><mrow><mn>15</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mi> </mi><mfrac><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow><mrow><mfrac><mrow><mn>8</mn></mrow><mrow><mn>15</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math> .

</details>

---

### Q6. JEE Advanced 2013 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong> Paragraph: </strong>

A box $B_{1}$ contains $1$ white ball, $3$ red balls and $2$ black balls. Another box $B_{2}$ contains $2$ white balls, $3$ red balls and $4$ black balls. A third box $B_{3}$ contains $3$ white balls, $4$ red balls and $5$ black balls.


 <strong> Question: </strong>

If $2$ balls are drawn (without replacement) from a randomly selected box and one of the balls is white and the other ball is red, the probability that these $2$ balls are drawn from box $B_{2}$ is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>1</mn> <mn>6</mn> </mrow> <mrow> <mn>1</mn> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>2</mn> <mn>6</mn> </mrow> <mrow> <mn>1</mn> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>6</mn> <mn>5</mn> </mrow> <mrow> <mn>1</mn> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>5</mn> <mn>5</mn> </mrow> <mrow> <mn>1</mn> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mfrac> <mrow> <mn>5</mn> <mn>5</mn> </mrow> <mrow> <mn>1</mn> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>&#160;</mo><mo>:</mo></math> one ball is white and other is red
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mn>1</mn></msub><mo>&#160;</mo><mo>:</mo></math> both balls are from box <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">B</mi><mn>1</mn></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mn>2</mn></msub><mo>&#160;</mo><mo>:</mo></math> both ball are from box <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">B</mi><mn>2</mn></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mn>3</mn></msub><mo>&#160;</mo><mo>:</mo></math> both ball are from box <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">B</mi><mn>3</mn></msub></math>
Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>P</mtext><mfenced><mtext>required</mtext></mfenced><mo>=</mo><mtext>P</mtext><mfenced><mfrac><msub><mtext>E</mtext><mn>2</mn></msub><mtext>A</mtext></mfrac></mfenced></math>
<math> <mrow> <mo>=</mo> <mfrac> <mrow> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>A</mtext> </mrow> <mrow> <msub> <mtext>E</mtext> <mn>2</mn> </msub> </mrow> </mfrac> </mrow> </mfenced> <mo>&#183;</mo> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mtext>E</mtext> <mn>2</mn> </msub> </mrow> </mfenced> </mrow> <mrow> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>A</mtext> </mrow> <mrow> <msub> <mtext>E</mtext> <mn>1</mn> </msub> </mrow> </mfrac> </mrow> </mfenced> <mo>&#183;</mo> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mtext>E</mtext> <mn>1</mn> </msub> </mrow> </mfenced> <mo>+</mo> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>A</mtext> </mrow> <mrow> <msub> <mtext>E</mtext> <mn>2</mn> </msub> </mrow> </mfrac> </mrow> </mfenced> <mo>&#183;</mo> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mtext>E</mtext> <mn>2</mn> </msub> </mrow> </mfenced> <mo>+</mo> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mtext>A</mtext> </mrow> <mrow> <msub> <mtext>E</mtext> <mn>3</mn> </msub> </mrow> </mfrac> </mrow> </mfenced> <mo>&#183;</mo> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <msub> <mtext>E</mtext> <mn>3</mn> </msub> </mrow> </mfenced> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>=</mo> <mfrac> <mrow> <mfrac> <mrow> <msup> <mspace></mspace> <mn>2</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> <mo>&#215;</mo> <msup> <mspace></mspace> <mn>3</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> </mrow> <mrow> <msup> <mspace></mspace> <mn>9</mn> </msup> <msub> <mtext>C</mtext> <mn>2</mn> </msub> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> <mrow> <mfrac> <mrow> <msup> <mspace></mspace> <mn>1</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> <mo>&#215;</mo> <msup> <mspace></mspace> <mn>3</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> </mrow> <mrow> <msup> <mspace></mspace> <mn>6</mn> </msup> <msub> <mtext>C</mtext> <mn>2</mn> </msub> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <msup> <mspace></mspace> <mn>2</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> <mo>&#215;</mo> <msup> <mspace></mspace> <mn>3</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> </mrow> <mrow> <msup> <mspace></mspace> <mn>9</mn> </msup> <msub> <mtext>C</mtext> <mn>2</mn> </msub> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <msup> <mspace></mspace> <mn>3</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> <mo>&#215;</mo> <msup> <mspace></mspace> <mn>4</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> </mrow> <mrow> <msup> <mspace></mspace> <mrow> <mn>1</mn> <mn>2</mn> </mrow> </msup> <msub> <mtext>C</mtext> <mn>2</mn> </msub> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>=</mo> <mfrac> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> </mrow> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>5</mn> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <mn>2</mn> </mrow> <mrow> <mn>1</mn> <mn>1</mn> </mrow> </mfrac> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>=</mo> <mfrac> <mrow> <mn>5</mn> <mn>5</mn> </mrow> <mrow> <mn>1</mn> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> </mrow> </math>

</details>

---

### Q7. JEE Advanced 2013 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong> Paragraph: </strong>

A box $B_{1}$ contains $1$ white ball, $3$ red balls and $2$ black balls. Another box $B_{2}$ contains $2$ white balls, $3$ red balls and $4$ black balls. A third box $B_{3}$ contains $3$ white balls, $4$ red balls and $5$ black balls.


 <strong> Question: </strong>

If $1$ ball is drawn from each of the boxes $B_{1}, B_{2}$ and $B_{3}$, the probability that all $3$ drawn balls are of the same colour is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>8</mn> <mn>2</mn> </mrow> <mrow> <mn>6</mn> <mn>4</mn> <mn>8</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>9</mn> <mn>0</mn> </mrow> <mrow> <mn>6</mn> <mn>4</mn> <mn>8</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>5</mn> <mn>5</mn> <mn>8</mn> </mrow> <mrow> <mn>6</mn> <mn>4</mn> <mn>8</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>5</mn> <mn>6</mn> <mn>6</mn> </mrow> <mrow> <mn>6</mn> <mn>4</mn> <mn>8</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mfrac> <mrow> <mn>8</mn> <mn>2</mn> </mrow> <mrow> <mn>6</mn> <mn>4</mn> <mn>8</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM00012628_AnsExp_1.jpg" style="width: 301px; height: 99px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>)</mo><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi mathvariant="normal">P</mi><mo>&#160;</mo><mo>(</mo><mi mathvariant="normal">R</mi><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>)</mo><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">B</mi><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>)</mo></math>
<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>2</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>1</mn> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>4</mn> </mrow> <mrow> <mn>1</mn> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> <mo>+</mo> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>2</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>4</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mo>&#215;</mo> <mfrac> <mrow> <mn>5</mn> </mrow> <mrow> <mn>1</mn> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>     <math> <mrow> <mo>&#8658;&#160;&#160;&#160;&#160;&#160;</mo> <mfrac> <mrow> <mn>6</mn> <mo>+</mo> <mn>3</mn> <mn>6</mn> <mo>+</mo> <mn>4</mn> <mn>0</mn> </mrow> <mrow> <mn>6</mn> <mo>&#215;</mo> <mn>9</mn> <mo>&#215;</mo> <mn>1</mn> <mn>2</mn> </mrow> </mfrac> <mo>&#160;&#160;&#160;&#160;&#160;&#8658;&#160;&#160;&#160;&#160;</mo> <mfrac> <mrow> <mn>8</mn> <mn>2</mn> </mrow> <mrow> <mn>6</mn> <mn>4</mn> <mn>8</mn> </mrow> </mfrac> </mrow> </math>

</details>

---

### Q8. JEE Advanced 2011 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Let $U_1$ and $U_2$ be two urns such that $U_1$ contains 3 white and 2 red balls and $U_2$ contains only 1 white ball. A fair coin is tossed. If head appears then 1 ball is drawn at random from $U_1$ and put into $U_2$. However, if tail appears then 2 balls are drawn at random from $U_1$ and put into $U_2$. Now, 1 ball is drawn at random from $U_2$.<strong>Question:</strong>
Given that the drawn ball from $U_2$ is white, the probability that head appeared on the coin is

**Options:**

- **(A)** $\frac{17}{23}$
- **(B)** $\frac{11}{23}$
- **(C)** $\frac{15}{23}$
- **(D)** $\frac{12}{23}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{12}{23}$**

**Detailed Solution:**

$P$ (head appeared/white from $V_2$ )
$$
\begin{aligned}
& =P(H) \cdot \frac{\left\{\frac{{ }^3 C_1}{{ }^5 C_1} \times \frac{{ }^2 C_1}{{ }^2 C_1}+\frac{{ }^2 C_1}{{ }^5 C_1} \times \frac{{ }^1 C_1}{{ }^2 C_1}\right\}}{\frac{23}{30}} \\
& =\frac{1}{2} \frac{\left\{\frac{3}{5} \times 1+\frac{2}{5} \times \frac{1}{2}\right\}}{\frac{23}{30}}=\frac{12}{23} \\
&
\end{aligned}
$$

</details>

---

