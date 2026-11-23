# Central Limit Theorem
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# User Input
pop_size = int(input("Enter population size (e.g., 100000): "))
sample_size = int(input("Enter sample size (e.g., 50): "))
num_samples = int(input("Enter number of samples (e.g., 1000): "))

# Population
population = np.random.uniform(0, 1, pop_size)

sample_means = []
for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=True)
    sample_means.append(np.mean(sample))

plt.figure(figsize=(12, 6))

# Plot original population
plt.subplot(1, 2, 1)
plt.hist(population, bins=100, color='skyblue', edgecolor='black', density=True)
plt.title("Original Population (Uniform)")
plt.xlabel("Value")
plt.ylabel("Probability Density")

# Plot sampling distribution of means
plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=100, color='salmon', edgecolor='black', density=True)
mean = np.mean(sample_means)
std = np.std(sample_means)

# Generate normal distribution curve
x = np.linspace(min(sample_means), max(sample_means), 1000)
pdf = norm.pdf(x, mean, std)

# Plot the normal curve
plt.plot(x, pdf, 'r', linewidth=2, label="Normal Distribution (CLT Prediction)")
plt.title("Sampling Distribution of Means (CLT)")
plt.xlabel("Sample Mean")
plt.ylabel("Probability Density")
plt.legend()
plt.show()


"""

================================================================================
THEORY: CENTRAL LIMIT THEOREM (CLT)
================================================================================

1. AIM OF THE MATH CONCEPT:
   To verify that the distribution of sample means approaches a Normal
   distribution as sample size increases, even when the original population is
   not normally distributed.

2. FORMULA:
   X_bar ~ N(mu, sigma^2 / n)
   Standard Error (SE) = sigma / sqrt(n)

3. TERMS OF FORMULA:
   - X_bar : Sample mean.
   - mu    : Population mean.
   - sigma : Population standard deviation.
   - n     : Size of each sample.

4. DEFINITION:
   The Central Limit Theorem states that the sampling distribution of the mean
   of sufficiently large independent random samples from any population with
   finite variance is approximately Normal.

5. THEORY RELATED:
   Even if the population is Uniform (flat) or Exponential (skewed), the
   averages of samples of size n >= 30 form a bell-shaped Normal curve centered
   at the population mean mu.

6. REAL-LIFE APPLICATIONS:
   - Election polling and survey estimation.
   - Quality control in manufacturing.
   - A/B testing in web analytics.

7. EXAMPLES:
   Drawing 1,000 samples of size n = 50 from a Uniform(0, 1) population.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   A Uniform(0, 1) population has mean mu = 0.5 and standard deviation
   sigma = 1 / sqrt(12) ≈ 0.2887. Find the mean and standard error of the
   sampling distribution for sample size n = 50.

   Step 1: Mean of sample means = mu = 0.5.
   Step 2: Standard Error (SE) = sigma / sqrt(n)
                               = 0.2887 / sqrt(50)
                               = 0.2887 / 7.0711 ≈ 0.0408.
   Final Answer: Sample means follow N(0.5, 0.0408^2).
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 100000
# 50
# 1000
