# To find out the code vectors(words) of LBC(n, r) using the generator matrix G.

from numpy import dot

# INPUT->
n = int(input('n: '))  # columns
r = int(input('r: '))  # rows
G = [[int(i) for i in input('>').split()] for row in range(r)]  # matrix

'''for row in G:
    print(row)  # debugging'''

# CALCULATION->
outer = 1
inner = 2 ** r  # binary = [0, 1]; len(binary) = 2
rvs = []  # binary row-vectors
for row in range(r):
    outer = outer * 2
    inner = inner // 2
    num = 0
    for o in range(outer):
        for i in range(inner):
            num += 1
            try:
                globals()['v' + str(num)].append(o % 2)
            except KeyError:
                globals()['v' + str(num)] = []
                globals()['v' + str(num)].append(o % 2)
                rvs.append(globals()['v' + str(num)])

'''for rv in rvs:
    print(rv)  # debugging'''

# OUTPUT->
print('\n')
for rv in rvs:
    ans = list()
    for i in dot(rv, G):  # dot() -> for matrix multiplication
        ans.append(i % 2)
    print(ans)

'''
INPUT: (No. of columns, No. of rows, Linear Block Code)
6
3
1 0 0 1 1 0
0 1 0 1 1 1
0 0 1 0 0 1


INTERNAL CALCULATION:

GENERATOR MATRIX (G)
[[1, 0, 0, 1, 1, 0],
[0, 1, 0, 1, 1, 1],
[0, 0, 1, 0, 0, 1]]

Binary Row Vectors
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]


OUTPUT (CODE VECTORS)
[0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 1]
[0, 1, 0, 1, 1, 1]
[0, 1, 1, 1, 1, 0]
[1, 0, 0, 1, 1, 0]
[1, 0, 1, 1, 1, 1]
[1, 1, 0, 0, 0, 1]
[1, 1, 1, 0, 0, 0]
'''
