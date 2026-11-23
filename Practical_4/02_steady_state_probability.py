# Steady State Probability
import numpy as np

# User Input
num_states = int(input("Enter number of states (e.g., 2): "))
print(f"Enter the {num_states}x{num_states} Transition Matrix P row by row:")
P_rows = []
for i in range(num_states):
    P_rows.append(list(map(float, input(f"Row {i}: ").split())))
P = np.array(P_rows, dtype=float)

# vP = v, v(P - I) = 0
A = (P - np.eye(num_states)).T
b = np.zeros(num_states)

# Add the normalization condition: pi1 + pi2 + ... = 1
A = np.vstack((A, np.ones(num_states)))
b = np.append(b, 1)

print(A)
print(b)

# Solve
steady_state = np.linalg.lstsq(A, b, rcond=None)[0]
print("Steady-state distribution:", steady_state)


"""

================================================================================
THEORY: STEADY-STATE PROBABILITY OF A MARKOV CHAIN
================================================================================

1. AIM OF THE MATH CONCEPT:
   To compute the long-run equilibrium probability distribution of a Markov chain.

2. FORMULA:
   pi * P = pi   =>   (P - I)^T * pi^T = 0
   with sum(pi_i) = 1

3. TERMS OF FORMULA:
   - pi : Steady-state probability vector.
   - P  : Transition probability matrix.
   - I  : Identity matrix.

4. DEFINITION:
   The steady-state distribution is a probability vector pi that remains
   unchanged after multiplying by the transition matrix P.

5. THEORY RELATED:
   Ergodic Markov chains converge to a unique steady-state distribution
   independent of the starting state.

6. REAL-LIFE APPLICATIONS:
   - Long-term market share prediction, PageRank, server load balancing.

7. EXAMPLES:
   P = [[0.7, 0.3], [0.4, 0.6]] yields steady-state [0.5714, 0.4286].

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Find steady-state distribution for P = [[0.7, 0.3], [0.4, 0.6]].

   Step 1: Set up pi * P = pi:
       0.7*pi1 + 0.4*pi2 = pi1  =>  -0.3*pi1 + 0.4*pi2 = 0  =>  pi1 = (4/3)*pi2.
   Step 2: Use normalization pi1 + pi2 = 1:
       (4/3)*pi2 + pi2 = 1  =>  (7/3)*pi2 = 1  =>  pi2 = 3/7 ≈ 0.4286.
   Step 3: Find pi1:
       pi1 = 1 - 3/7 = 4/7 ≈ 0.5714.
   Final Answer: pi = [0.5714, 0.4286].
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 2
# 0.7 0.3
# 0.4 0.6
