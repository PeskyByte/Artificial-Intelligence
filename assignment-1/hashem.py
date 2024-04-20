"""
Start with 5 random 3x3 matrices. DONE 
Then for each matrix generate a child by swapping two random numbers in the parent. Done
Then choose the best five matrices from the 10 matrices available. Done
keep going until you reach a magic matrix (sum of each row col and diagonal = 15).
"""

import time
import random as rnd

nodes = list()

def heuristic(matrix):
    h_t = 0

    for row in matrix:
        sum = 0
        for value in row:
            sum += value
        if sum != 15:
            h_t += 1

    for i in range(3):
        sum = 0
        for j in range(3):
            sum += matrix[j][i]
        if sum != 15:
            h_t += 1

    first_diagonal = 0
    for i in range(3):
        first_diagonal += matrix[i][i]
    if first_diagonal != 15:
        h_t += 1

    second_diagonal = 0
    for i in range(2, -1, -1):
        second_diagonal += matrix[2 - i][i]
    if second_diagonal != 15:
        h_t += 1

    return h_t


def generateChild(matrix):
    row1 = rnd.randint(0, 2)
    row2 = rnd.randint(0, 2)
    col1 = rnd.randint(0, 2)
    col2 = rnd.randint(0, 2)
    r = matrix[:]
    r[row1][col1], r[row2][col2] = r[row2][col2], r[row1][col1]
    nodes.append(r)


if __name__ == "__main__":

    # rnd.seed()
    start_time = time.time()
    generation = 0
    matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for _ in range(5):
        rnd.shuffle(matrix)
        r = [[], [], []]
        r[0] = matrix[0:3]  # first 3 elements
        r[1] = matrix[3:6]  # second 3 elements
        r[2] = matrix[6:9]  # third 3 elements
        nodes.append(r[:])

    while 1:
        for i in range(5):
            generateChild(nodes[i])
        
        nodes.sort(key=heuristic)
        for _ in range(5):
            nodes.pop()

        generation += 1
        if heuristic(nodes[0]) == 0:
            print(nodes[0])
            break

    print("Number of generations = ", generation)
    end_time = time.time()
    print("Execution time = ", end_time - start_time)
