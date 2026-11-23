# Perform Test for Single Proportion (Large Sample)
import math

# Step 1: Input data
n = int(input("Enter sample size (n): "))
x = int(input("Enter number of successes (x): "))
p0 = float(input("Enter assumed population proportion (p0): "))
alpha = float(input("Enter level of significance (e.g., 0.05): "))
tail = input("Enter test type (two/left/right): ").strip().lower()

# Step 2: Compute sample proportion
phat = x / n

# Step 3: Compute standard error
se = math.sqrt((p0 * (1 - p0)) / n)

# Step 4: Compute z statistic
z_cal = (phat - p0) / se

# Step 5: Determine critical (tabulated) z-value
if tail == "two":
    z_tab = 1.96 if alpha == 0.05 else 2.58 if alpha == 0.01 else 1.64
elif tail == "right":
    z_tab = 1.645 if alpha == 0.05 else 2.33
elif tail == "left":
    z_tab = -1.645 if alpha == 0.05 else -2.33
else:
    print("Invalid tail type! Please enter 'two', 'left', or 'right'.")
    exit()

# Step 6: Display results
print("\n--- RESULTS ---")
print(f"Sample proportion (p_hat) = {phat:.3f}")
print(f"Population proportion (p0) = {p0}")
print(f"Calculated z = {z_cal:.3f}")
print(f"Tabulated z = {z_tab}")
print(f"Significance Level (alpha) = {alpha}")

# Step 7: Decision
if tail == "two":
    if abs(z_cal) > z_tab:
        print("\nReject Null Hypothesis (H0).")
    else:
        print("\nAccept Null Hypothesis (H0).")
elif tail == "right":
    if z_cal > z_tab:
        print("\nReject Null Hypothesis (H0).")
    else:
        print("\nAccept Null Hypothesis (H0).")
elif tail == "left":
    if z_cal < z_tab:
        print("\nReject Null Hypothesis (H0).")
    else:
        print("\nAccept Null Hypothesis (H0).")


"""

================================================================================
THEORY: LARGE SAMPLE TEST FOR SINGLE PROPORTION (Z-TEST)
================================================================================

1. AIM OF THE MATH CONCEPT:
   To test whether an observed sample proportion significantly differs from a
   hypothesized population proportion (p0).

2. FORMULA:
   p_hat = x / n
   z = (p_hat - p0) / sqrt((p0 * (1 - p0)) / n)

3. TERMS OF FORMULA:
   - n     : Sample size.
   - x     : Number of successes.
   - p_hat : Sample proportion.
   - p0    : Hypothesized population proportion.

4. DEFINITION:
   A one-proportion Z-test evaluates whether the proportion of successes in a
   large sample matches a claimed population proportion.

5. THEORY RELATED:
   For large n, p_hat is approximately Normal by the CLT. Comparing z_cal with
   z_tab determines whether to reject H0: p = p0.

6. REAL-LIFE APPLICATIONS:
   - Election polling (testing if support exceeds 50%).
   - Manufacturing (testing if defect rate differs from 3%).

7. EXAMPLES:
   n = 600, x = 157, p0 = 0.3, alpha = 0.05, two-tailed.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given n = 600, x = 157, p0 = 0.3, alpha = 0.05 (two-tailed).

   Step 1: Sample proportion: p_hat = 157 / 600 = 0.2617.
   Step 2: Standard error: SE = sqrt((0.3 * 0.7) / 600) = sqrt(0.00035) = 0.01871.
   Step 3: Z-statistic: z_cal = (0.2617 - 0.3) / 0.01871 = -2.049.
   Step 4: Decision: |z_cal| = 2.049 > z_tab (1.96) => Reject H0.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 100
# 60
# 0.5
# 0.05
# two
