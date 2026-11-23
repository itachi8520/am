# Small Sample t-test for Difference of Means
import math
from scipy.stats import t

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

# Pooled standard deviation
sp = math.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))

# t-statistic
t_value = (mean1 - mean2) / (sp * math.sqrt((1 / n1) + (1 / n2)))

# Degrees of freedom
df = n1 + n2 - 2
t_tab = t.ppf(1 - alpha / 2, df)  # two-tailed test

print("Mean1 =", mean1)
print("Mean2 =", mean2)
print("Variance1 =", var1)
print("Variance2 =", var2)
print("Pooled SD =", sp)
print("t =", t_value)
print("Degrees of Freedom =", df)

if abs(t_value) > t_tab:
    print("\nReject Null Hypothesis (H0).")
    print("There is a significant difference between the two means.")
else:
    print("\nAccept Null Hypothesis (H0).")
    print("There is no significant difference between the two means.")


"""

================================================================================
THEORY: SMALL SAMPLE t-TEST FOR DIFFERENCE OF MEANS
================================================================================

1. AIM OF THE MATH CONCEPT:
   To test whether there is a significant difference between the means of two
   independent small samples (n1, n2 < 30).

2. FORMULA:
   Sp^2 = ((n1 - 1)*S1^2 + (n2 - 1)*S2^2) / (n1 + n2 - 2)
   t = (mean1 - mean2) / (Sp * sqrt(1/n1 + 1/n2))
   df = n1 + n2 - 2

3. TERMS OF FORMULA:
   - mean1, mean2 : Sample means of Sample 1 and Sample 2.
   - S1^2, S2^2   : Sample variances.
   - Sp           : Pooled standard deviation.
   - df           : Degrees of freedom.

4. DEFINITION:
   The independent two-sample t-test compares the means of two small unrelated
   groups assuming equal population variances.

5. THEORY RELATED:
   H0: mu1 = mu2. Compare |t_calculated| against t_tabulated at df = n1 + n2 - 2.
   If |t| > t_tab, reject H0.

6. REAL-LIFE APPLICATIONS:
   - Comparing test scores of two small student groups.
   - Clinical trials comparing recovery time between treatment and control.

7. EXAMPLES:
   Sample 1 = [12, 9, 13, 10, 8], Sample 2 = [7, 10, 6, 9, 5], alpha = 0.05.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Sample 1 = [12, 9, 13, 10, 8] (n1 = 5), Sample 2 = [7, 10, 6, 9, 5] (n2 = 5),
   alpha = 0.05.

   Step 1: Means: mean1 = 52/5 = 10.4,  mean2 = 37/5 = 7.4.
   Step 2: Variances: var1 = 17.2 / 4 = 4.3,  var2 = 17.2 / 4 = 4.3.
   Step 3: Pooled SD: Sp = sqrt((4*4.3 + 4*4.3) / 8) = sqrt(4.3) = 2.0736.
   Step 4: t-statistic: t = (10.4 - 7.4) / (2.0736 * sqrt(1/5 + 1/5))
                          = 3.0 / (2.0736 * 0.6325) = 2.2875.
   Step 5: Decision: df = 8, t_tab(0.05, 8) = 2.306.
       Since 2.2875 < 2.306, Accept H0 (no significant difference).
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 10 12 11 13 9
# 8 7 9 10 6
# 0.05
