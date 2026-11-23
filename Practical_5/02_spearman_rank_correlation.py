# Spearman's Rank Correlation
import numpy as np
from scipy.stats import rankdata

# User Input
x = np.array(list(map(float, input("Enter X values (space-separated): ").split())))
y = np.array(list(map(float, input("Enter Y values (space-separated): ").split())))

# Rank the data
rank_x = rankdata(x)
rank_y = rankdata(y)

# Calculate differences and Spearman's rho
d = rank_x - rank_y
n = len(x)
rho = 1 - (6 * np.sum(d ** 2)) / (n * (n ** 2 - 1))

print("Spearman's Rank Correlation (rho):", round(rho, 4))


"""

================================================================================
THEORY: SPEARMAN'S RANK CORRELATION
================================================================================

1. AIM OF THE MATH CONCEPT:
   To measure the monotonic relationship between two variables using their ranks.

2. FORMULA:
   rho = 1 - (6 * sum(d_i^2)) / (n * (n^2 - 1))

3. TERMS OF FORMULA:
   - rho : Spearman's rank correlation coefficient (-1 <= rho <= 1).
   - d_i : Difference between ranks of each pair (rank_x - rank_y).
   - n   : Number of observations.

4. DEFINITION:
   Spearman's rank correlation is a non-parametric measure of rank correlation
   assessing monotonic association between two variables.

5. THEORY RELATED:
   Does not assume linearity or normality and is robust to outliers.

6. REAL-LIFE APPLICATIONS:
   - Comparing judge rankings, ordinal survey analysis, search ranking evaluation.

7. EXAMPLES:
   x = [10, 20, 30, 40, 50], y = [10, 25, 30, 45, 55] -> rho = 1.0000.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given X = [10, 20, 30, 40], Y = [15, 25, 20, 40] (n = 4):
   Step 1: Ranks: rank_x = [1, 2, 3, 4], rank_y = [1, 3, 2, 4].
   Step 2: Differences d = [0, -1, 1, 0], d^2 = [0, 1, 1, 0], sum(d^2) = 2.
   Step 3: Apply formula:
       rho = 1 - (6 * 2) / (4 * (16 - 1)) = 1 - 12 / 60 = 1 - 0.2 = 0.8.
   Final Answer: rho = 0.8.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 10 20 30 40
# 15 25 20 40
