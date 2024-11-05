
# import time
# import math

# # Function to find factors between 1 and floor(sqrt(n))
# def find_factors(n):
#     factors = []
#     sqrt_n = math.isqrt(n)  # Efficient integer square root
#     for i in range(1, sqrt_n + 1):
#         if n % i == 0:
#             factors.append(i)  # Add i as a factor
#             if i != n // i:    # Add n // i as a factor if it's different
#                 factors.append(n // i)
#     factors.sort()  # Sort the factors
#     return factors

# # Function to measure the execution time of finding factors
# def measure_execution_time(n):
#     start_time = time.time()  # Record the start time
#     factors = find_factors(n)  # Find factors
#     end_time = time.time()  # Record the end time
#     execution_time = end_time - start_time  # Calculate execution time
#     return factors, execution_time

# # Main function to run the algorithm for different values of n
# def run_factor_tests():
#     numbers_to_test = [10**i for i in range(1, 10)]  # Powers of 10 from 10 to 1 billion

#     # Print results in tabular format
#     print(f"{'Number':<15}{'Execution Time (seconds)':<25}{'Factors'}")
#     print('-' * 60)
#     for n in numbers_to_test:
#         factors, exec_time = measure_execution_time(n)
#         print(f"{n:<15}{exec_time:<25.10f}{factors}")

# # Run the tests
# if __name__ == "__main__":
#     run_factor_tests()

#------------------------------------------------------------------

from math import sqrt
from datetime import datetime

# Start the timer
start_time = datetime.now()

# Get input from the user and convert it to an integer
n = int(input("What positive integer would you like to test? "))

# Function to calculate the square root of n
def Square_Root(n):
    positive_integer = n
    root = sqrt(positive_integer)
    return int(root)  # Return the integer part of the square root

# Function to find factors between 1 and sqrt(n)
def Find_Factors(sqrt_n, n):
    factors = []  # List to store the factors
    for i in range(1, sqrt_n + 1):
        if n % i == 0:  # If i divides n evenly
            factors.append(i)
            if i != n // i and n // i <= sqrt_n:  # Add the complementary factor
                factors.append(n // i)
    factors.sort()  # Sort the factors for neat output
    return factors

# Calculate the integer square root of n
sqrt_n = Square_Root(n)

# Find the factors
factors = Find_Factors(sqrt_n, n)

# Stop the timer
end_time = datetime.now()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the results
print(f"Factors of {n}: {factors}")
print(f"Time taken: {elapsed_time.total_seconds()} seconds")
