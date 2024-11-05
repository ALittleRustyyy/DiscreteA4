import csv 
import pandas 
import numpy as np

def read_csv(file_name):        #takes in the given CSV file and reads it, then converts it to a matrix
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        matrix = [list(map(int, row)) for row in reader]
    return np.array(matrix)

def matrix_computation(matrix):
    n = len(matrix)
    # Start with Matrix B
    P = np.copy(matrix)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                P[i][j] = P[i][j] or (P[i][k] and P[k][j])      #checks if there is a path between vertexes I and J
    
    return P

def display_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Read the matrix from the CSV file
file_name = 'TestCSV.csv'  # Replace with file you want to test
B = read_csv(file_name)

# Compute the transitive closure matrix (P)
P = matrix_computation(B)

# Display the result
print("Matrix P")
display_matrix(P)
