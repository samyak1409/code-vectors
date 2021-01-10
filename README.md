# code-vectors
Program to find out the code vectors(words) of a Linear Block Code using Generator matrix.


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
