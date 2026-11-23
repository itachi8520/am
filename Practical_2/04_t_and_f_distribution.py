# T & F Distribution
import random
import math
import matplotlib.pyplot as plt

# Standard Normal using CLT
def normal_random():
    return random.gauss(0, 1)

# t-distribution random variable
def t_random(df):
    z = normal_random()
    v = sum(normal_random() ** 2 for _ in range(df))  # sum of squared normals
    return z / math.sqrt(v / df)

# F-distribution random variable
def f_random(d1, d2):
    u = sum(normal_random() ** 2 for _ in range(d1)) / d1
    v = sum(normal_random() ** 2 for _ in range(d2)) / d2
    return u / v

# Generate many samples
def generate_samples(func, n, *args):
    return [func(*args) for _ in range(n)]

# User Input
n_samples = int(input("Enter number of samples to generate (e.g., 5000): "))
df_t = int(input("Enter degrees of freedom for t-distribution (df, e.g., 10): "))
d1 = int(input("Enter d1 for F-distribution (e.g., 5): "))
d2 = int(input("Enter d2 for F-distribution (e.g., 10): "))

t_samples = generate_samples(t_random, n_samples, df_t)
f_samples = generate_samples(f_random, n_samples, d1, d2)

# Plot
plt.figure(figsize=(12, 5))

# t-distribution
plt.subplot(1, 2, 1)
plt.hist(t_samples, bins=50, density=True, color="skyblue", edgecolor="black")
plt.title(f"t-distribution (df={df_t})")

# F-distribution
plt.subplot(1, 2, 2)
plt.hist(f_samples, bins=50, density=True, color="salmon", edgecolor="black")
plt.title(f"F-distribution (d1={d1}, d2={d2})")

plt.show()


"""

================================================================================
THEORY: STUDENT'S t-DISTRIBUTION AND F-DISTRIBUTION
================================================================================

1. AIM OF THE MATH CONCEPT:
   To simulate and plot Student's t-distribution and Snedecor's F-distribution
   using standard normal random variables.

2. FORMULA:
   - t-Distribution: T = Z / sqrt(V / df),  where V = sum(Z_i^2 for i = 1..df)
   - F-Distribution: F = (U / d1) / (V / d2)

3. TERMS OF FORMULA:
   - Z      : Standard Normal variable N(0, 1).
   - U, V   : Independent Chi-Square variables.
   - df     : Degrees of freedom for t-distribution.
   - d1, d2 : Numerator and denominator degrees of freedom for F-distribution.

4. DEFINITION:
   - t-distribution: A symmetric bell-shaped distribution with heavier tails
     than the Normal distribution, used for small-sample mean inference.
   - F-distribution: A right-skewed non-negative distribution representing the
     ratio of two scaled Chi-Square variables.

5. THEORY RELATED:
   As df increases, the t-distribution approaches N(0, 1). The F-distribution is
   always >= 0 and is central to variance comparison and ANOVA.

6. REAL-LIFE APPLICATIONS:
   - t-distribution: Comparing small-sample means in clinical or academic tests.
   - F-distribution: ANOVA across multiple groups, comparing manufacturing variances.

7. EXAMPLES:
   Simulating 5,000 samples of t(df=10) and F(d1=5, d2=10).

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Suppose Z = 1.5 and Chi-Square V = 9 with df = 4. Compute T.
   Step 1: Compute V / df = 9 / 4 = 2.25.
   Step 2: Take square root: sqrt(2.25) = 1.5.
   Step 3: Divide Z by sqrt(V / df): T = 1.5 / 1.5 = 1.0.
   Final Answer: T = 1.0.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 5000
# 10
# 5
# 10
