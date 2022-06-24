#Part 1

#a)
print(2**11)
print((2**4)**4)
print(4**4)
print(8**5)
print(842%100)
print(837%20)
print(22%111)
print(111%22)

#b
print()
import numpy as np
V1 = np.array([[1,1,3]])
V2 = np.array([[1,2,2]])
M = np.array([[2, 1, 3], [1, 2, 1], [1, 0, 1]])

print(V2-V1)
print(V1+V1)
print(np.linalg.norm(V1))
print(np.linalg.norm(V2))
print(np.matmul(M,V2.transpose()))
print(np.linalg.matrix_power(M,2))
print(np.linalg.matrix_power(M,3))

