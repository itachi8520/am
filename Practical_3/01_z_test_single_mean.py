# Perform Large Sample Test for Single Mean (Z-test)
import numpy as np
from scipy.stats import norm

def z_test_single_mean(sample, mu0, sigma, alpha=0.05, alternative='two-sided'):
    sample = np.array(sample)
    n = len(sample)
    x_bar = np.mean(sample)

    # Z-statistic
    z_stat = (x_bar - mu0) / (sigma / np.sqrt(n))

    # p-value based on alternative hypothesis
    if alternative == 'two-sided':
        p_value = 2 * (1 - norm.cdf(abs(z_stat)))
    elif alternative == 'greater':
        p_value = 1 - norm.cdf(z_stat)
    elif alternative == 'less':
        p_value = norm.cdf(z_stat)
    else:
        raise ValueError("alternative must be 'two-sided', 'less', or 'greater'")

    # Decision
    reject = p_value <= alpha
    return {
        "Sample Mean": x_bar,
        "Hypothesized Mean": mu0,
        "Z-statistic": z_stat,
        "p-value": p_value,
        "Conclusion": "Reject H0" if reject else "Fail to Reject H0"
    }

# User Input
data = list(map(float, input("Enter sample data (space-separated): ").split()))
mu0 = float(input("Enter hypothesized population mean (mu0): "))
sigma = float(input("Enter population standard deviation (sigma): "))
alpha = float(input("Enter significance level (alpha, e.g., 0.05): "))
alternative = input("Enter alternative hypothesis (two-sided / greater / less): ").strip().lower()

result = z_test_single_mean(data, mu0, sigma=sigma, alpha=alpha, alternative=alternative)
print(result)


"""

================================================================================
THEORY: LARGE SAMPLE TEST FOR SINGLE MEAN (Z-TEST)
================================================================================

1. AIM OF THE MATH CONCEPT:
   To test whether a sample mean significantly differs from a hypothesized
   population mean (mu0) when population standard deviation (sigma) is known.

2. FORMULA:
   Z = (x_bar - mu0) / (sigma / sqrt(n))

3. TERMS OF FORMULA:
   - x_bar : Sample mean.
   - mu0   : Hypothesized population mean under H0.
   - sigma : Known population standard deviation.
   - n     : Sample size.
   - alpha : Significance level (e.g., 0.05).

4. DEFINITION:
   A one-sample Z-test is a parametric hypothesis test used to check if a sample
   comes from a population with a specified mean when sigma is known.

5. THEORY RELATED:
   H0: mu = mu0. If p-value <= alpha, reject H0; otherwise fail to reject H0.

6. REAL-LIFE APPLICATIONS:
   - Quality control (checking product weight against labeled weight).
   - Healthcare (testing if a treatment shifts mean blood pressure).

7. EXAMPLES:
   Sample = [52, 50, 53, 49, 48, 51, 54, 50, 52, 49], mu0 = 50, sigma = 2, alpha = 0.05.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given sample = [52, 50, 53, 49, 48, 51, 54, 50, 52, 49], n = 10, mu0 = 50,
   sigma = 2, alpha = 0.05 (two-sided).

   Step 1: Calculate sample mean:
       x_bar = (52+50+53+49+48+51+54+50+52+49) / 10 = 508 / 10 = 50.8.
   Step 2: Calculate Z-statistic:
       Z = (50.8 - 50) / (2 / sqrt(10)) = 0.8 / 0.6325 = 1.2649.
   Step 3: Find p-value:
       p-value = 2 * (1 - norm.cdf(1.2649)) = 0.2059.
   Step 4: Decision:
       Since p-value (0.2059) > alpha (0.05), Fail to Reject H0.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 102 98 101 99 100
# 100
# 10
# 0.05
# two-sided
