import numpy as np
vektor1 = np.array([1,2,3])
vektor2 = np.array([1,1,1])

operasi_perkalian_skalar = np.dot(vektor1,vektor2)
print(operasi_perkalian_skalar)

matriks1 = np.array([[1,2],[3,4]])
matriks2 = np.array([[5,6],[7,8]])

matriks3 = np.matmul(matriks1,matriks2)
print(matriks3)

determinan = np.linalg.det(matriks3)
print(determinan)
