###############################################################################################################################################
#Name: Austin Lucas
#Date: Oct. 1 2024
#Section: Math 311 001
#Quarter: Fall 24
#Assignment: A2
###############################################################################################################################################

import time
import math

# Function to find factors between 1 and floor(sqrt(n)), then appends them to a list
def find_factors(n):
    factors = []
    sqrt_n = math.isqrt(n)  # Efficient integer square root (a function from the math library in python)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            factors.append(i)  # Add i as a factor
            if i != n // i and n // i <= sqrt_n:    # Add n // i as a factor if it's different, thus making sure no repeat factors are added
                factors.append(n // i)
    factors.sort()  # Sort the factors so they are readable
    return factors

# Function to measure execution time
def measure_execution_time(n):
    start_time = time.time()  # Records and saves the start time
    factors = find_factors(n)  # Find factors of n
    end_time = time.time()  # Records and saves the end time
    execution_time = end_time - start_time  
    return factors, execution_time

# Main function to run the algorithm for different values of n
def run_factor_tests():
    numbers_to_test = [10**i for i in range(1, 10)]  # Powers of 10 from 10 to 1 billion
      #You may play with these numbers if you would like. I didnt want to make my laptop scream at me.
      
    # Print results in tabular format, (I will admit that i had to look up a guide to do this) ((im not great at python))
    print(f"{'Number':<15}{'Execution Time (seconds)':<25}{'Factors'}")
    print('-' * 60)
    for n in numbers_to_test:
        factors, exec_time = measure_execution_time(n)
        print(f"{n:<15}{exec_time:<25.10f}{factors}")

run_factor_tests()

#After a certain number, the table loses its legibility because the list of factors begins to bleed
#into the next line. I opted to not cap the table though, so that the values can be seen.
#Also, i got python to time the runtime, but its not reading any significant time until 
#it finds the factors of 1000000000