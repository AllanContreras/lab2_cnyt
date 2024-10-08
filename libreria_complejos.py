import math
import numpy as np  



# Adición de vectores complejos
def add_complex_vectors(v1, v2):
    return [(v1[i][0] + v2[i][0], v1[i][1] + v2[i][1]) for i in range(len(v1))]

# Inverso aditivo de un vector complejo
def inverse_complex_vector(v):
    return [(-v[i][0], -v[i][1]) for i in range(len(v))]

# Multiplicación de un escalar por un vector complejo
def scalar_mult_complex_vector(scalar, v):
    return [(scalar[0] * v[i][0] - scalar[1] * v[i][1], scalar[0] * v[i][1] + scalar[1] * v[i][0]) for i in range(len(v))]

# Adición de matrices complejas
def add_complex_matrices(m1, m2):
    return [[(m1[i][j][0] + m2[i][j][0], m1[i][j][1] + m2[i][j][1]) for j in range(len(m1[0]))] for i in range(len(m1))]

# Inversa aditiva de una matriz compleja
def inverse_complex_matrix(m):
    return [[(-m[i][j][0], -m[i][j][1]) for j in range(len(m[0]))] for i in range(len(m))]

# Multiplicación de un escalar por una matriz compleja
def scalar_mult_complex_matrix(scalar, m):
    return [[(scalar[0] * m[i][j][0] - scalar[1] * m[i][j][1], scalar[0] * m[i][j][1] + scalar[1] * m[i][j][0]) for j in range(len(m[0]))] for i in range(len(m))]

# Transpuesta de una matriz/vector
def transpose(matrix):
    return list(map(list, zip(*matrix)))

# Conjugada de una matriz/vector
def conjugate(matrix):
    return [[(matrix[i][j][0], -matrix[i][j][1]) for j in range(len(matrix[0]))] for i in range(len(matrix))]

# Adjunta (daga) de una matriz/vector
def adjoint(matrix):
    return conjugate(transpose(matrix))

# Producto de dos matrices (de tamaños compatibles)
def mult_complex_matrices(m1, m2):
    result = [[(0, 0) for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] = sumcomplex(result[i][j], multcomplex(m1[i][k], m2[k][j]))
    return result

# "Acción" de una matriz sobre un vector (producto matriz-vector)
def action_complex_matrix_on_vector(matrix, vector):
    return [sum([multcomplex(matrix[i][j], vector[j]) for j in range(len(vector))]) for i in range(len(matrix))]

# Producto interno de dos vectores
def inner_product(v1, v2):
    result = (0, 0)
    for i in range(len(v1)):
        result = sumcomplex(result, multcomplex(v1[i], conjucomplex(v2[i])))
    return result

# Norma de un vector complejo
def norm_complex_vector(v):
    return round(math.sqrt(inner_product(v, v)[0]), 2)

# Distancia entre dos vectores complejos
def distance_complex_vectors(v1, v2):
    diff = [(v1[i][0] - v2[i][0], v1[i][1] - v2[i][1]) for i in range(len(v1))]
    return norm_complex_vector(diff)
# Valores  y vectores propios de una matriz
def eigenvalues_eigenvectors(m):
    matrix = np.array(m, dtype=complex)
    values, vectors = np.linalg.eig(matrix)
    return values, vectors
# Revisión si una matriz es unitaria
def is_unitary(matrix):
    adj = adjoint(matrix)
    identity = [[(1 if i == j else 0, 0) for j in range(len(matrix))] for i in range(len(matrix))]
    product = mult_complex_matrices(matrix, adj)
    return all(product[i][j] == identity[i][j] for i in range(len(product)) for j in range(len(product[0])))

# Revisión si una matriz es Hermitiana
def is_hermitian(matrix):
    return matrix == adjoint(matrix)

# Producto tensor de dos matrices/vectores
def tensor_product(m1, m2):
    return [[multcomplex(m1[i//len(m2)][j//len(m2[0])], m2[i % len(m2)][j % len(m2[0])]) for j in range(len(m1[0]) * len(m2[0]))] for i in range(len(m1) * len(m2))]
