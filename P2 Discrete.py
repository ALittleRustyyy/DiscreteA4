from math import *
from datetime import *

start_time = datetime.now() #Start the clock

n = int(input("What positive integer would you like to test?"))

def Square_Root(n):    #Function that determines the square root of n
    positive_integer = n
    root = sqrt(positive_integer)
    return int(root)   #Return the calculated square root


def Find_Factors(sqrt_n, n):
    factors = []    #Empty list that will store the factors, once they are appended
    for i in range(1, sqrt_n):
        if n % i == 0: #checks to make sure there is no remainder when divided
            factors.append(i)
            if i != n // i and n // i <= sqrt_n: #makes sure that factors are not repeated in the list.
                factors.append(n // i)          #also caps the factors at the square root of n.
    factors.sort() #Sorted list so that list is easily readable
    return factors



end_time = datetime.now()
elapsed_time = end_time - start_time

print(elapsed_time)