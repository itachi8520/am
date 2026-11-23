# Fit Normal Distribution Curve to Data
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# User Input marks data
marks = list(map(float, input("Enter marks data (space-separated): ").split()))

# Fit normal distribution to the data
mean = np.mean(marks)
std = np.std(marks)
print("Mean:", mean)
print("Std:", std)

# Create a wide x-axis for the bell curve so the curve becomes visible
x = np.linspace(mean - 4 * std, mean + 4 * std, 500)

# Normal distribution using fitted parameters
y = norm.pdf(x, mean, std)

plt.figure(figsize=(9, 5))
plt.plot(x, y, linewidth=2, label="Normal Curve (Fitted)")
plt.hist(marks, bins=10, density=True, alpha=0.3, label="Data Histogram")

# Lines for min/max of your data
plt.axvline(min(marks), linestyle='--', label=f"Min = {min(marks)}")
plt.axvline(max(marks), linestyle='--', label=f"Max = {max(marks)}")

plt.title("Normal Curve Fitted to Your Data")
plt.xlabel("Marks")
plt.ylabel("Density")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


"""

================================================================================
THEORY: NORMAL CURVE FITTING TO DATA
================================================================================

1. AIM OF THE MATH CONCEPT:
   To fit a Normal distribution curve to an empirical dataset using its mean
   and standard deviation and compare it against a density histogram.

2. FORMULA:
   mean = (1/n) * sum(x_i)
   std  = sqrt((1/n) * sum((x_i - mean)^2))
   f(x) = (1 / (std * sqrt(2*pi))) * exp(-0.5 * ((x - mean) / std)^2)

3. TERMS OF FORMULA:
   - x_i  : Observed data points (marks).
   - mean : Sample mean.
   - std  : Sample standard deviation.

4. DEFINITION:
   Normal curve fitting estimates the Gaussian parameters (mean, std) from raw
   data and overlays the theoretical bell curve onto the empirical histogram.

5. THEORY RELATED:
   Setting density=True normalizes histogram bar areas to 1 so they match the
   scale of the probability density function.

6. REAL-LIFE APPLICATIONS:
   - Academic bell-curve grading, manufacturing quality control, medical reference ranges.

7. EXAMPLES:
   Fitting a normal curve to student marks (mean ≈ 20.72, std ≈ 2.38).

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given marks = [18, 20, 20, 22]:
   Step 1: Mean = (18 + 20 + 20 + 22) / 4 = 80 / 4 = 20.0.
   Step 2: Variance = ((18-20)^2 + (20-20)^2 + (20-20)^2 + (22-20)^2) / 4
                    = (4 + 0 + 0 + 4) / 4 = 2.0.
   Step 3: Std = sqrt(2.0) ≈ 1.4142.
   Step 4: Peak density at x = 20:
       f(20) = 1 / (1.4142 * sqrt(2 * pi)) ≈ 0.2821.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 18 20 20 22 24 21 19 23 20 22
