# Perform F-test for Comparison of Variances (Small Samples)
import math
from scipy.stats import f

# User Input
sample1 = list(map(float, input("Enter Sample 1 values (space-separated): ").split()))
sample2 = list(map(float, input("Enter Sample 2 values (space-separated): ").split()))
alpha = float(input("Enter significance level (alpha, e.g., 0.05): "))

n1, n2 = len(sample1), len(sample2)

# Means
mean1 = sum(sample1) / n1
mean2 = sum(sample2) / n2

# Variances
var1 = sum((x - mean1) ** 2 for x in sample1) / (n1 - 1)
var2 = sum((x - mean2) ** 2 for x in sample2) / (n2 - 1)

print("Mean1 =", mean1)
print("Mean2 =", mean2)
print("Variance1 =", var1)
print("Variance2 =", var2)

if var1 > var2:
    f_stat = var1 / var2
    df1 = len(sample1) - 1
    df2 = len(sample2) - 1
else:
    f_stat = var2 / var1
    df1 = len(sample2) - 1
    df2 = len(sample1) - 1

p_value = 2 * f.sf(f_stat, df1, df2)

if p_value < alpha:
    print("Reject Null Hypothesis (H0).")
    print("There is a significant difference between the two variances.")
else:
    print("Accept Null Hypothesis (H0).")
    print("There is no significant difference between the two variances.")


"""

================================================================================
THEORY: F-TEST FOR COMPARISON OF VARIANCES
================================================================================

1. AIM OF THE MATH CONCEPT:
   To test whether two independent populations have equal variances.

2. FORMULA:
   F = larger_variance / smaller_variance
   df1 = n1 - 1,  df2 = n2 - 1

3. TERMS OF FORMULA:
   - var1, var2 : Sample variances of Sample 1 and Sample 2.
   - df1, df2   : Degrees of freedom.
   - p_value    : Two-tailed probability from F survival function.

4. DEFINITION:
   The F-test compares the ratio of two sample variances to determine if their
   underlying population variances are equal.

5. THEORY RELATED:
   H0: sigma1^2 = sigma2^2. If p_value < alpha, reject H0.

6. REAL-LIFE APPLICATIONS:
   - Comparing consistency of two machines in a factory.
   - Comparing volatility (risk) of two financial stocks.

7. EXAMPLES:
   Sample 1 = [12, 9, 13, 10, 18], Sample 2 = [7, 10, 6, 9, 15], alpha = 0.05.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Sample 1 = [12, 9, 13, 10, 18] (n1 = 5), Sample 2 = [7, 10, 6, 9, 15] (n2 = 5).

   Step 1: Means: mean1 = 62/5 = 12.4,  mean2 = 47/5 = 9.4.
   Step 2: Variances:
       var1 = ((12-12.4)^2 + (9-12.4)^2 + (13-12.4)^2 + (10-12.4)^2 + (18-12.4)^2) / 4 = 49.2 / 4 = 12.3.
       var2 = ((7-9.4)^2 + (10-9.4)^2 + (6-9.4)^2 + (9-9.4)^2 + (15-9.4)^2) / 4 = 49.2 / 4 = 12.3.
   Step 3: F-statistic: F = 12.3 / 12.3 = 1.0 (df1 = 4, df2 = 4).
   Step 4: p-value = 2 * f.sf(1.0, 4, 4) = 1.0 > 0.05 => Accept H0.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 10 12 9 11 13
# 8 7 9 10 6
# 0.05
