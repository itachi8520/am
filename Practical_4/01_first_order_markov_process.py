# Perform First-Order Markov Process Simulation
import numpy as np

# User Input
num_states = int(input("Enter number of states (e.g., 2): "))
states = list(range(num_states))

print(f"Enter the {num_states}x{num_states} Transition Probability Matrix P row by row:")
P = []
for i in range(num_states):
    P.append(list(map(float, input(f"Row {i} (from state {i}): ").split())))

current_state = int(input(f"Enter initial state (0 to {num_states - 1}): "))
n = int(input("Enter number of steps (n): "))

print("Markov Process Simulation:")
sequence = [current_state]
for i in range(n):
    current_state = np.random.choice(states, p=P[current_state])
    sequence.append(int(current_state))

print("Sequence of States:", sequence)


"""

================================================================================
THEORY: FIRST-ORDER MARKOV PROCESS SIMULATION
================================================================================

1. AIM OF THE MATH CONCEPT:
   To simulate a stochastic process where the next state depends only on the
   current state.

2. FORMULA:
   P(X_{t+1} = j | X_t = i, X_{t-1}, ..., X_0) = P(X_{t+1} = j | X_t = i) = P_ij

3. TERMS OF FORMULA:
   - X_t  : State at step t.
   - P_ij : Transition probability from state i to state j.
   - P    : Transition Probability Matrix.

4. DEFINITION:
   A First-Order Markov Chain is a memoryless stochastic process transitioning
   between states based solely on the present state.

5. THEORY RELATED:
   Every row of P sums to 1 (stochastic matrix).

6. REAL-LIFE APPLICATIONS:
   - Weather forecasting, Google PageRank, stock regime modeling.

7. EXAMPLES:
   2 states [0, 1], P = [[0.1, 0.9], [0.8, 0.2]], start = 0, n = 10 steps.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given P = [[0.1, 0.9], [0.8, 0.2]] and initial state X_0 = 0:
   Step 1: From state 0, P(next=0) = 0.1 and P(next=1) = 0.9.
           Suppose random draw selects state 1 -> sequence = [0, 1].
   Step 2: From state 1, P(next=0) = 0.8 and P(next=1) = 0.2.
           Suppose random draw selects state 0 -> sequence = [0, 1, 0].
   Repeating for n steps produces the simulated state sequence.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 2
# 0.7 0.3
# 0.4 0.6
# 0
# 10
