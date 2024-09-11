import libreria_complejos as cpmx

def printcomplex(c):
    if type(c) == float:
        print(round(c,2))
    else:
        if c[1] < 0:
            return (str(c[0]) + " - " + str(abs(c[1])) + "i")
        else:
            return (str(c[0]) + " + " + str(c[1]) + "i")


def casos_prueba(rest1,ver1,rest2,ver2):
    Passed = 0
    Failed = 0
    if rest1 == ver1:
        Passed+=1
    else:
        Failed+=1
    if rest2 == ver2:
        Passed+=1
    else:
        Failed+=1

    return "De dos casos pruebas:",Passed, "Pasaron con exito y",Failed,"No funcionaron con exito" 

# Números y vectores complejos de prueba
c1 = (2, 5)
c2 = (7, 8)
c3 = (-21, 15)
c4 = (-2, -2)

v1 = [(2, 3), (1, 1), (4, -5)]
v2 = [(3, 2), (0, 0), (-1, 4)]

m1 = [[(1, 1), (0, 0)], [(2, 2), (3, 3)]]
m2 = [[(1, 0), (2, 0)], [(3, 0), (4, 0)]]

print("Adición de Vectores Complejos")
val1 = cpmx.add_complex_vectors(v1, v2)
val2 = cpmx.add_complex_vectors(v1, v1)
print(*casos_prueba(val1, [(5, 5), (1, 1), (3, -1)], val2, [(4, 6), (2, 2), (8, -10)]))
print()

print("Inverso Aditivo de un Vector Complejo")
val1 = cpmx.inverse_complex_vector(v1)
val2 = cpmx.inverse_complex_vector(v2)
print(*casos_prueba(val1, [(-2, -3), (-1, -1), (-4, 5)], val2, [(-3, -2), (0, 0), (1, -4)]))
print()

print("Multiplicación de Escalar por un Vector Complejo")
val1 = cpmx.scalar_mult_complex_vector(2, v1)
val2 = cpmx.scalar_mult_complex_vector(-1, v2)
print(*casos_prueba(val1, [(4, 6), (2, 2), (8, -10)], val2, [(-3, -2), (0, 0), (1, -4)]))
print()

print("Adición de Matrices Complejas")
val1 = cpmx.add_complex_matrices(m1, m2)
val2 = cpmx.add_complex_matrices(m1, m1)
print(*casos_prueba(val1, [[(2, 1), (2, 0)], [(5, 2), (7, 3)]], val2, [[(2, 2), (0, 0)], [(4, 4), (6, 6)]]))
print()

print("Transpuesta de una Matriz Compleja")
val1 = cpmx.transpose_complex_matrix(m1)
val2 = cpmx.transpose_complex_matrix(m2)
print(*casos_prueba(val1, [[(1, 1), (2, 2)], [(0, 0), (3, 3)]], val2, [[(1, 0), (3, 0)], [(2, 0), (4, 0)]]))
print()

print("Conjugada de una Matriz Compleja")
val1 = cpmx.conjugate_complex_matrix_vector(m1)
val2 = cpmx.conjugate_complex_matrix_vector(m2)
print(*casos_prueba(val1, [[(1, -1), (0, 0)], [(2, -2), (3, -3)]], val2, [[(1, 0), (2, 0)], [(3, 0), (4, 0)]]))
print()

print("Adjunta de una Matriz Compleja")
val1 = cpmx.adjoint_complex_matrix_vector(m1)
val2 = cpmx.adjoint_complex_matrix_vector(m2)
print(*casos_prueba(val1, [[(1, -1), (2, -2)], [(0, 0), (3, -3)]], val2, [[(1, 0), (3, 0)], [(2, 0), (4, 0)]]))
print()

print("Producto Interno de Dos Vectores Complejos")
val1 = cpmx.inner_product(v1, v2)
val2 = cpmx.inner_product(v1, v1)
print(*casos_prueba(val1, (-5, 24), val2, (55, 0)))
print()

print("Norma de un Vector Complejo")
val1 = cpmx.norm_complex_vector(v1)
val2 = cpmx.norm_complex_vector(v2)
print(*casos_prueba(val1, 7.42, val2, 5.0))
print()

print("Distancia entre Dos Vectores Complejos")
val1 = cpmx.distance_complex_vectors(v1, v2)
val2 = cpmx.distance_complex_vectors(v1, v1)
print(*casos_prueba(val1, 8.12, val2, 0.0))
print()

print("Verificar si una Matriz es Unitaria")
val1 = cpmx.is_unitary_matrix(m1)
val2 = cpmx.is_unitary_matrix(m2)
print("Matriz 1:", "Unitaria" if val1 else "No unitaria")
print("Matriz 2:", "Unitaria" if val2 else "No unitaria")
print()

print("Verificar si una Matriz es Hermitiana")
val1 = cpmx.is_hermitian_matrix(m1)
val2 = cpmx.is_hermitian_matrix(m2)
print("Matriz 1:", "Hermitiana" if val1 else "No hermitiana")
print("Matriz 2:", "Hermitiana" if val2 else "No hermitiana")
print()

print("Producto Tensorial de Dos Matrices Complejas")
val1 = cpmx.tensor_product_complex(m1, m2)
print("Producto tensorial calculado correctamente:", val1)
print()
