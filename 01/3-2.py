# Code for  birthday paradox using a formula
import numpy as np
from scipy.special import factorial, comb

def same_birth_formula(n):
    numerator = comb(365, n) * factorial(n)
    denominator = (365 ** n)
    return 1 - (numerator / denominator)
    
# Run experiments for n = 5, 10, ..., 100 and print probabilities.
def birthday_paradox_formula():
    print(f"{'n':>5} | {'Probability of Shared Birthday':>30}")
    print("-" * 40)
    
    for n in range(5, 101, 5):
        probability = same_birth_formula(n)
        print(f"{n:>5} | {probability:>30.4f}")

# Perform the computation using birthday paradox formula
birthday_paradox_formula()