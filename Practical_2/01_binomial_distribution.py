# Demonstrate Discrete Random Variable (Binomial Distribution)
import numpy as np
import matplotlib.pyplot as plt
import math

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def binomial_pmf(n, p):
    probs = []
    for k in range(n + 1):
        prob = nCr(n, k) * (p ** k) * ((1 - p) ** (n - k))
        probs.append(prob)
    return probs

n = int(input("Enter number of trials (n): "))
p = float(input("Enter probability of success (p): "))

x = np.arange(0, n + 1)
pmf = binomial_pmf(n, p)

print(f"\nBinomial Distribution: n={n}, p={p}")
print("k\tP(X=k)")
for k, prob in zip(x, pmf):
    print(f"{k}\t{prob:.5f}")

# Binomial Plot
plt.bar(x, pmf, color='skyblue', edgecolor='black')
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.xlabel("k (Number of Successes)")
plt.ylabel("P(X=k)")
plt.show()


"""

================================================================================
THEORY: BINOMIAL DISTRIBUTION (DISCRETE RANDOM VARIABLE)
================================================================================

1. AIM OF THE MATH CONCEPT:
   To compute and plot the probability mass function (PMF) of getting exactly k
   successes in n independent Bernoulli trials.

2. FORMULA:
   P(X = k) = nCr(n, k) * p^k * (1 - p)^(n - k)
   where nCr(n, k) = n! / (k! * (n - k)!)

3. TERMS OF FORMULA:
   - n : Total number of independent trials.
   - k : Number of successes (0, 1, 2, ..., n).
   - p : Probability of success in a single trial.
   - (1 - p) : Probability of failure in a single trial.

4. DEFINITION:
   The Binomial distribution is a discrete probability distribution modeling the
   number of successes in a fixed number of independent yes/no trials with
   constant success probability.

5. THEORY RELATED:
   Conditions: fixed n, two outcomes per trial, constant p, independent trials.
   Mean = n * p, Variance = n * p * (1 - p).

6. REAL-LIFE APPLICATIONS:
   - Quality control (defective items in a batch).
   - Clinical trials (patients responding to a drug).
   - Marketing (email click-through counts).

7. EXAMPLES:
   Tossing a fair coin 10 times (n = 10, p = 0.5) and finding the probability
   of getting 0 to 10 heads.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   A fair coin is tossed n = 4 times (p = 0.5). Find the probability of getting
   exactly k = 2 heads.

   Step 1: Identify parameters: n = 4, k = 2, p = 0.5, (1 - p) = 0.5.
   Step 2: Compute combination: C(4, 2) = 4! / (2! * 2!) = 24 / 4 = 6.
   Step 3: Apply formula:
       P(X = 2) = 6 * (0.5)^2 * (0.5)^(4 - 2)
                = 6 * 0.25 * 0.25
                = 6 * 0.0625 = 0.375.
   Final Answer: P(X = 2) = 0.375 (37.5%).
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 4
# 0.5
