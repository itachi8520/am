# Joint Probability Mass Function
import numpy as np
import matplotlib.pyplot as plt

# User Input
sides = int(input("Enter number of sides on each die (e.g., 6): "))
die_outcomes = list(range(1, sides + 1))

# Total possible outcomes = sides * sides
total_outcomes = sides * sides
sample_space = [(x, y) for x in die_outcomes for y in die_outcomes]
print(sample_space)

joint_pmf = {}
for (x, y) in sample_space:
    joint_pmf[(x, y)] = 1 / total_outcomes
print(joint_pmf)

pmf_matrix = np.zeros((sides, sides))
for x in die_outcomes:
    for y in die_outcomes:
        pmf_matrix[x - 1, y - 1] = joint_pmf[(x, y)]
print(pmf_matrix)

plt.figure(figsize=(10, 6))
plt.imshow(pmf_matrix, cmap="Blues", interpolation="nearest")

# Add values on each cell
for i in range(sides):
    for j in range(sides):
        plt.text(j, i, f"{pmf_matrix[i, j]:.3f}", ha='center', va='center', color='black')

plt.title("Joint Probability Mass Function (2 Dice)")
plt.ylabel("Y (Die 2)")
plt.xlabel("X (Die 1)")
plt.colorbar(label="Probability")
plt.xticks(np.arange(sides), die_outcomes)
plt.yticks(np.arange(sides), die_outcomes)
plt.show()


"""

================================================================================
THEORY: JOINT PROBABILITY MASS FUNCTION (JOINT PMF)
================================================================================

1. AIM OF THE MATH CONCEPT:
   To compute and visualize the joint probability distribution of two discrete
   random variables (rolling two fair dice).

2. FORMULA:
   p(x, y) = P(X = x, Y = y) = P(X = x) * P(Y = y)   (for independent X, Y)
   sum_x sum_y p(x, y) = 1

3. TERMS OF FORMULA:
   - X, Y    : Discrete random variables (outcomes of Die 1 and Die 2).
   - p(x, y) : Joint probability of pair (x, y).

4. DEFINITION:
   A Joint PMF gives the probability that two discrete random variables X and Y
   simultaneously take specific values x and y.

5. THEORY RELATED:
   Every entry satisfies 0 <= p(x, y) <= 1, and the sum across the entire grid
   equals 1. Summing a row or column gives the Marginal PMF of one variable.

6. REAL-LIFE APPLICATIONS:
   - Risk analysis (joint failure of two components).
   - Weather forecasting (joint probability of rain and high wind).
   - Gaming and board game probability analysis.

7. EXAMPLES:
   Rolling two 6-sided dice produces 36 pairs, each with probability 1/36 ≈ 0.028.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Two fair 6-sided dice are rolled. Find P(X = 3, Y = 5) and P(X + Y = 4).

   Step 1: Total outcomes = 6 * 6 = 36.
   Step 2: Since dice are independent:
       P(X = 3, Y = 5) = (1/6) * (1/6) = 1/36 ≈ 0.0278.
   Step 3: Pairs with X + Y = 4 are (1, 3), (2, 2), (3, 1) -> 3 pairs.
       P(X + Y = 4) = 3 / 36 = 1 / 12 ≈ 0.0833.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 6
