#Austin Lucas
#11/12/24
#MATH 311 - 001
#Fall 24
#A4

import csv
import numpy as np

def read_csv(file_name):
    """Reads the given CSV file and converts it into a matrix."""
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        matrix = [list(map(int, row)) for row in reader]
    return np.array(matrix)

def matrix_computation(matrix):
    """Computes the Path Matrix."""
    n = len(matrix)
    P = np.copy(matrix)  # Start with Matrix B
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                P[i][j] = P[i][j] or (P[i][k] and P[k][j])
    
    return P

def display_matrix(matrix, title):
    """Prints the matrix in a nicely formatted table."""
    n = len(matrix)
    print(f"\n{title}:\n")
    
    # Print header row with vertex numbers. Online help was used for formatting the table.
    header = "Vertex".ljust(8) + "".join(f"{i + 1}".rjust(5) for i in range(n))
    print(header)
    print("-" * len(header))
    
    # Print each row with vertex labels and formatted entries
    for i, row in enumerate(matrix):
        row_str = "".join(f"{'1' if cell == 1 else '0'}".rjust(5) for cell in row)
        print(f"{i + 1}".ljust(8) + row_str)

# Main program
file_name = 'airline.csv'  # Ensure your CSV file is in the correct location
B = read_csv(file_name)

# Display the Edge Matrix
display_matrix(B, "EDGE MATRIX")

# Compute Matrix P 
P = matrix_computation(B)

# Display the Path Matrix
display_matrix(P, "PATH MATRIX")


""" - Output

Vertex      1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30
--------------------------------------------------------------------------------------------------------------------------------------------------------------
1           0    0    0    1    1    1    1    0    1    1    1    0    0    0    1    1    1    1    0    0    0    0    1    0    1    0    0    1    0    0
2           0    0    1    1    0    0    0    1    0    0    1    0    1    0    1    1    0    1    1    0    0    0    0    0    1    1    0    0    0    0
3           0    0    0    0    0    0    0    1    0    0    1    1    0    1    0    1    0    1    0    0    0    1    1    0    1    0    0    1    1    1
4           0    1    0    1    1    0    0    0    0    0    1    1    0    1    0    1    0    1    0    0    0    0    0    0    1    0    0    1    1    0
5           1    0    0    1    1    1    0    0    1    1    0    1    0    1    1    0    1    0    1    1    0    0    0    0    1    1    1    1    0    1
6           0    1    0    0    0    1    0    1    1    0    0    0    0    1    0    0    0    1    1    0    0    0    1    1    0    0    0    1    1    1
7           1    0    0    0    0    0    1    0    0    0    1    0    1    1    0    0    0    1    0    1    1    1    0    1    0    0    0    0    0    0
8           0    1    0    0    1    1    1    0    1    1    0    0    0    0    0    0    0    1    0    1    0    1    0    0    1    0    0    0    1    0
9           0    1    0    0    1    1    0    0    1    1    0    1    0    0    1    0    1    0    0    0    0    1    1    0    1    1    0    1    0    1
10          0    0    1    0    0    0    1    0    1    0    1    0    0    0    0    0    1    1    1    1    1    1    0    0    0    0    0    0    0    0
11          0    1    0    1    0    1    0    1    0    0    0    0    0    0    0    0    1    1    1    1    0    0    0    0    0    0    0    1    1    1
12          0    1    0    0    1    0    1    0    0    0    1    1    1    0    0    1    0    0    0    1    0    1    0    0    0    0    1    1    1    1
13          1    0    1    0    1    0    0    0    0    1    0    1    0    0    0    1    0    0    0    0    0    1    1    0    1    0    0    1    1    0
14          0    0    0    0    0    0    1    0    1    1    0    1    0    0    1    1    1    0    1    1    0    1    1    0    1    0    0    0    1    1
15          1    1    1    1    1    0    0    0    0    1    1    0    0    0    1    1    0    0    0    0    1    1    1    1    0    1    1    0    1    1
16          1    1    0    0    0    0    1    1    1    0    0    0    1    1    1    1    1    0    0    0    0    0    1    0    0    1    1    0    0    0
17          1    0    0    0    0    0    0    0    1    0    1    0    0    0    0    1    1    0    1    1    0    1    1    0    0    1    1    1    1    1
18          1    0    1    1    0    0    0    0    0    1    0    0    0    0    1    0    0    0    0    0    1    0    0    0    0    1    1    1    1    0
19          0    0    1    1    0    0    1    0    0    1    0    0    0    0    0    1    0    0    0    0    0    1    0    0    1    0    1    0    1    1
20          1    0    1    0    0    1    0    0    0    0    1    0    0    0    0    0    1    0    0    0    0    0    1    1    1    0    0    0    1    1
21          0    1    0    0    0    1    1    0    0    0    0    1    1    0    0    1    0    0    1    1    0    0    1    0    0    1    1    0    1    1
22          1    0    1    0    0    0    0    0    1    1    0    1    1    1    1    0    0    0    0    0    0    0    0    1    1    0    0    0    0    0
23          0    0    1    0    0    0    0    1    1    1    0    0    1    0    1    1    0    0    0    0    0    1    0    0    1    0    0    0    0    0
24          0    1    1    0    0    0    1    1    0    0    0    0    0    0    1    1    0    0    0    0    1    1    0    1    0    0    1    0    0    1
25          0    0    1    0    0    0    0    0    1    0    1    0    1    0    1    1    1    0    0    0    0    1    0    1    0    0    0    0    1    0
26          0    0    0    0    1    0    0    0    0    0    1    0    0    1    0    1    0    1    1    1    0    0    0    0    1    0    1    1    0    1
27          0    0    0    0    0    0    0    1    0    0    0    0    0    0    0    0    1    0    1    1    0    0    0    1    0    0    1    0    0    1
28          1    0    0    0    1    0    1    0    0    0    1    1    0    1    0    0    1    0    1    1    0    0    0    0    1    0    0    0    1    0
29          0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
30          1    0    1    0    0    1    0    1    0    0    0    0    0    0    0    1    1    1    0    0    0    0    1    0    0    0    1    1    0    0

PATH MATRIX:

Vertex      1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30
--------------------------------------------------------------------------------------------------------------------------------------------------------------
1           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
2           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
3           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
4           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
5           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
6           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
7           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
8           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
9           1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
10          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
11          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
12          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
13          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
14          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
15          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
16          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
17          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
18          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
19          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
20          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
21          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
22          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
23          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
24          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
25          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
26          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
27          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
28          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
29          0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0    0
30          1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1    1
"""