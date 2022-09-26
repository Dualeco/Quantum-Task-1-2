import time

N = int(input())

t1 = time.perf_counter()

s = sum(range(1, N + 1))

t2 = time.perf_counter()

print(s)
print('Time: ', t2 - t1, ' seconds')

import numpy as np

M = 5
N = 5

matrix = [
    [0, 1, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1]
]

visited = np.full((M, N), 0)

global island_num
island_num = 0

def in_range(i, j):
    return i >= 0 and i < M and j >= 0 and j < N 

def should_traverse(i, j):
    return matrix[i][j] == 1 and visited[i][j] == 0

def visit(i, j):
    visited[i][j] = island_num

def traverse(i, j):
    queue = [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1),
            (i - 1, j), (i + 1, j),
            (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]
    
    for elem in queue:
        i_e, j_e = elem
        
        if in_range(i_e, j_e) and should_traverse(i_e, j_e):  
            visit(i_e, j_e)
            traverse(i_e, j_e)
        

for i in range(M):
    for j in range(N):
        if should_traverse(i, j):
            island_num = island_num + 1
            
            visit(i, j)
            traverse(i, j)
            

print('Number of islands: ', island_num)
print(visited)
