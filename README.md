Librería CNYT - Calculadora de Números Complejos
Autor: Allan Contreras

Descripción
Esta librería fue creada con la finalidad de realizar diversas operaciones con números complejos, tanto en su forma de números individuales como en vectores y matrices. Está diseñada para facilitar cálculos de álgebra lineal compleja y provee una amplia gama de funcionalidades, desde operaciones básicas hasta verificación de propiedades avanzadas en matrices complejas.

Funcionalidades Principales
Suma de números complejos
Resta de números complejos
Producto de números complejos
División de números complejos
Módulo de un número complejo
Conjugado de un número complejo
Conversión entre coordenadas polares y cartesianas
Fase de un número complejo
Operaciones con vectores y matrices complejas
Adición de vectores/matrices
Inverso aditivo de vectores/matrices
Multiplicación de un escalar por un vector/matriz
Transpuesta, conjugada y adjunta de una matriz/vector
Producto de matrices
Producto interno de vectores
Acción de una matriz sobre un vector
Norma de un vector
Distancia entre dos vectores
Revisión de matrices unitarias y Hermitianas
Producto tensorial de matrices/vectores
¿Cómo se usa?
Para usar esta librería, es necesario contar con los números complejos, vectores o matrices que se desean operar, y seleccionar la función correcta según la operación requerida. Los números complejos se representan de la siguiente forma:

Representación de Números Complejos
Formato: 2+1𝑖
Denotación en la librería: (Número Real, Número Imaginario)
Parámetros Generales
Se ha utilizado la función round para aproximar los resultados con una precisión de 2 decimales, con el fin de mejorar la precisión en los casos de prueba.
round(valor, 2)
Funciones Disponibles
Operaciones Básicas
Resta
La función restcomplex se utiliza para restar dos números complejos: 
def restcomplex(c1, c2):
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    return (real, imag)
Suma
La función sumcomplex se utiliza para sumar dos números complejos:
def sumcomplex(c1, c2):
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    return (real, imag)
División
La función divcomplex se utiliza para dividir dos números complejos:
def divcomplex(c1, c2):
    real = round(((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0]**2) + (c2[1]**2)), 2)
    imag = round(((c2[0] * c1[1]) - (c1[0] * c2[1])) / ((c2[0]**2) + (c2[1]**2)), 2)
    return (real, imag)
Multiplicación
La función multcomplex se utiliza para multiplicar dos números complejos:
def multcomplex(c1, c2):
    real = (c1[0] * c2[0]) - (c1[1] * c2[1])
    imag = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return (real, imag)
Módulo
La función moducomplex se utiliza para obtener el módulo de un número complejo:
def moducomplex(c):
    return round(math.sqrt((c[0] ** 2) + (c[1] ** 2)), 2)
Conjugado
La función conjucomplex se utiliza para obtener el conjugado de un número complejo:
def conjucomplex(c):
    return (c[0], -1 * c[1])
Conversión de Cartesiano a Polar
La función cartesian_to_polar_complex convierte un número complejo en coordenadas cartesianas a coordenadas polares:
def cartesian_to_polar_complex(c):
    r = round(math.sqrt(c[0]**2 + c[1]**2), 2)
    theta = round(math.atan2(c[1], c[0]), 2)
    return (r, theta)
Fase
La función fasecomplex retorna la fase (ángulo) de un número complejo:
def fasecomplex(c):
    return round(math.atan2(c[1], c[0]), 2)
Operaciones Avanzadas con Vectores y Matrices
Adición de Vectores Complejos
def add_complex_vectors(v1, v2):
    return [(v1[i][0] + v2[i][0], v1[i][1] + v2[i][1]) for i in range(len(v1))]
Multiplicación Escalar por un Vector Complejo
def scalar_mult_complex_vector(scalar, v):
    return [(scalar[0] * v[i][0] - scalar[1] * v[i][1], scalar[0] * v[i][1] + scalar[1] * v[i][0]) for i in range(len(v))]
Transpuesta de una Matriz/Vector
def transpose(matrix):
    return list(map(list, zip(*matrix)))
Producto Interno de Dos Vectores
def inner_product(v1, v2):
    result = (0, 0)
    for i in range(len(v1)):
        result = sumcomplex(result, multcomplex(v1[i], conjucomplex(v2[i])))
    return result
Acción de una Matriz sobre un Vector
def action_complex_matrix_on_vector(matrix, vector):
    return [sum([multcomplex(matrix[i][j], vector[j]) for j in range(len(vector))]) for i in range(len(matrix))]
Verificación de Propiedades de Matrices
¿Es Unitaria?
def is_unitary(matrix):
    adj = adjoint(matrix)
    identity = [[(1 if i == j else 0, 0) for j in range(len(matrix))] for i in range(len(matrix))]
    product = mult_complex_matrices(matrix, adj)
    return all(product[i][j] == identity[i][j] for i in range(len(product)) for j in range(len(product[0])))
¿Es Hermitiana?
def is_hermitian(matrix):
    return matrix == adjoint(matrix)
