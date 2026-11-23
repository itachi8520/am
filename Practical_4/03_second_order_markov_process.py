# Perform Second-Order Markov Process Simulation
import numpy as np
import random

# User Input
num_states = int(input("Enter number of states (e.g., 3): "))
states = list(range(num_states))

# Define transition probabilities for each pair (previous two states)
P = {}
print(f"Enter transition probabilities for each pair (s1, s2) ({num_states} space-separated values):")
for s1 in states:
    for s2 in states:
        P[(s1, s2)] = list(map(float, input(f"Pair ({s1}, {s2}): ").split()))

# Initialize with two starting states
current_state = [random.choice(states), random.choice(states)]
sequence = current_state.copy()
n = int(input("Enter number of steps (n): "))

# Simulation Loop
for i in range(n):
    prev_pair = (sequence[-2], sequence[-1])
    probs = P[prev_pair]
    next_state = int(np.random.choice(states, p=probs))
    sequence.append(next_state)

print("Second-Order Markov Process Simulation:")
print("Sequence of States:", sequence)


"""

================================================================================
THEORY: SECOND-ORDER MARKOV PROCESS SIMULATION
================================================================================

1. AIM OF THE MATH CONCEPT:
   To simulate a stochastic process where the next state depends on the previous
   two states.

2. FORMULA:
   P(X_{t+1} = k | X_t = j, X_{t-1} = i, ..., X_0) = P(X_{t+1} = k | X_t = j, X_{t-1} = i)

3. TERMS OF FORMULA:
   - (X_{t-1}, X_t) : Pair of previous two states.
   - P[(i, j)]      : Transition probability vector for pair (i, j).
   - n              : Number of simulation steps.

4. DEFINITION:
   A Second-Order Markov Chain is a discrete-time stochastic process with memory
   of length 2.

5. THEORY RELATED:
   With m states, there are m^2 possible pairs of previous states.

6. REAL-LIFE APPLICATIONS:
   - NLP trigram models, DNA sequence analysis, music generation.

7. EXAMPLES:
   3 states [0, 1, 2] with 9 transition rows, simulated for n = 5 steps.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Suppose states = [0, 1], P[(0, 1)] = [0.3, 0.7], P[(1, 1)] = [0.6, 0.4],
   and starting pair is [0, 1].
   Step 1: Previous pair is (0, 1). Sample next state using [0.3, 0.7] -> say 1.
           Sequence = [0, 1, 1].
   Step 2: Previous pair is (1, 1). Sample next state using [0.6, 0.4] -> say 0.
           Sequence = [0, 1, 1, 0].
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 2
# 0.8 0.2
# 0.5 0.5
# 0.3 0.7
# 0.1 0.9
# 10
