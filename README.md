# Libreria CNYT Calculadora de vectores y matrices complejas.

## Autor ***Allan Contreras***

Libreria creada con la finalidad de realizar operaciones de vectores y matrices complejas.

Cuenta con las funciones

- Adición de vectores complejos
- Inverso aditivo de un vector complejo
- Multiplicación de un escalar por un vector complejo
- Adición de matrices complejas
- Inverso aditivo de una matriz compleja
- Multiplicación de un escalar por una matriz compleja
- Transpuesta de una matriz o vector
- Conjugada de una matriz o vector
- Adjunta (daga) de una matriz o vector
- Producto de dos matrices (de tamaños compatibles)
- Acción de una matriz sobre un vector
- Producto interno de dos vectores complejos
- Norma de un vector complejo
- Distancia entre dos vectores complejos
- Cálculo de valores y vectores propios de una matriz compleja
- Revisión de si una matriz es unitaria
- Revisión de si una matriz es Hermitiana
- Producto tensorial de dos matrices o vectores


## ¿Como se usa?

Se neceitan conocer vectores o matrices que se desean operar y escoger correctamente las funciones

## Datos

Manera en que se representan los numeros complejos

``` txt
2 + 1i
```

Denotación

``` txt
(Numero Real, Numero Complejo)
```

## Parametos Generales

>Se uso la Funcion Round para aproximar los valores con una presicion de 2, en este caso, los casos pruebas tuvieron que ser aproximados

```Python
round(Parametro,2)
```

## Contenido


### Adición de Vectores Complejos
La función add_complex_vectors se utiliza para sumar dos vectores complejos elemento a elemento
``` Python
def add_complex_vectors(v1, v2):
    return [(v1[i][0] + v2[i][0], v1[i][1] + v2[i][1]) for i in range(len(v1))]

```

### Inverso Aditivo de un Vector Complejo
La función inverse_complex_vector se utiliza para obtener el inverso aditivo de un vector complejo
``` Python
def inverse_complex_vector(v):
    return [(-x[0], -x[1]) for x in v]

```

### Multiplicación de un Escalar por un Vector Complejo
La función scalar_mult_complex_vector se utiliza para multiplicar un escalar por un vector complejo
``` Python
def scalar_mult_complex_vector(scalar, v):
    return [(scalar * x[0], scalar * x[1]) for x in v]

```

### Adición de Matrices Complejas
La función add_complex_matrices se utiliza para sumar dos matrices complejas elemento a elemento
``` Python
def add_complex_matrices(m1, m2):
    return [[(m1[i][j][0] + m2[i][j][0], m1[i][j][1] + m2[i][j][1]) for j in range(len(m1[i]))] for i in range(len(m1))]

```
### Inverso Aditivo de una Matriz Compleja
La función inverse_complex_matrix se utiliza para obtener el inverso aditivo de una matriz compleja
``` Python
def inverse_complex_matrix(m):
    return [[(-x[0], -x[1]) for x in row] for row in m]

```
### Multiplicación de un Escalar por una Matriz Compleja
La función scalar_mult_complex_matrix se utiliza para multiplicar un escalar por una matriz compleja
``` Python
def scalar_mult_complex_matrix(scalar, m):
    return [[(scalar * x[0], scalar * x[1]) for x in row] for row in m]

```
### Transpuesta de una Matriz o Vector
La función transpose_matrix_or_vector se utiliza para obtener la transpuesta de una matriz o vector
``` Python
def transpose_complex_matrix_vector(m):
    return list(map(list, zip(*m)))

```

### Conjugada de una Matriz o Vector
La función conjugate_matrix_or_vector se utiliza para obtener la conjugada de una matriz o vector complejo
``` Python
def conjugate_complex_matrix_vector(m):
    return [[conjucomplex(x) for x in row] for row in m]

```
### Adjunta (Daga) de una Matriz o Vector
La función adjoint_matrix_or_vector se utiliza para obtener la adjunta (daga) de una matriz o vector
``` Python
def adjoint_complex_matrix_vector(m):
    return conjugate_complex_matrix_vector(transpose_complex_matrix_vector(m))

```

### Producto de Dos Matrices
La función matrix_product se utiliza para multiplicar dos matrices complejas (de tamaños compatibles)
``` Python
def matrix_mult_complex(m1, m2):
    result = [[(0, 0)] * len(m2[0]) for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] = sumcomplex(result[i][j], multcomplex(m1[i][k], m2[k][j]))
    return result

```
### Acción de una Matriz sobre un Vector
La función action_complex_matrix_on_vector calcula la acción de una matriz compleja sobre un vector complejo
``` Python
def action_complex_matrix_on_vector(matrix, vector):
    return [sum([multcomplex(matrix[i][j], vector[j]) for j in range(len(vector))]) for i in range(len(matrix))]

```

### Producto Interno de Dos Vectores
La función inner_product calcula el producto interno entre dos vectores complejos
``` Python
def inner_product(v1, v2):
    result = (0, 0)
    for i in range(len(v1)):
        result = sumcomplex(result, multcomplex(v1[i], v2[i]))
    return result

```

### Norma de un Vector Complejo
La función norm_complex_vector calcula la norma de un vector complejo
``` Python
def norm_complex_vector(v):
    return round(math.sqrt(inner_product(v, v)[0]), 2)

```
### Distancia entre Dos Vectores Complejos
La función distance_complex_vectors calcula la distancia entre dos vectores complejos
``` Python
def distance_complex_vectors(v1, v2):
    diff = [(v1[i][0] - v2[i][0], v1[i][1] - v2[i][1]) for i in range(len(v1))]
    return norm_complex_vector(diff)

```

### Revisión de si una Matriz es Unitaria
La función is_unitary_matrix verifica si una matriz compleja es unitaria. Una matriz es unitaria si su producto con su adjunta da como resultado la matriz identidad
``` Python
def is_unitary_matrix(m):
    adjoint_m = adjoint_complex_matrix_vector(m)
    identity = matrix_mult_complex(m, adjoint_m)
    size = len(identity)
    for i in range(size):
        for j in range(size):
            if i == j:
                if round(identity[i][j][0], 2) != 1 or round(identity[i][j][1], 2) != 0:
                    return False
            else:
                if round(identity[i][j][0], 2) != 0 or round(identity[i][j][1], 2) != 0:
                    return False
    return True

```
### Revisión de si una Matriz es Hermitiana
La función is_hermitian_matrix verifica si una matriz compleja es Hermitiana. Una matriz es Hermitiana si es igual a su adjunta
``` Python
def is_hermitian_matrix(m):
    return m == adjoint_complex_matrix_vector(m)

```
### Producto Tensorial de Dos Matrices o Vectores
La función tensor_product_complex calcula el producto tensorial de dos matrices o vectores complejos
``` Python
def tensor_product_complex(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            for k in range(len(b)):
                row.extend([multcomplex(a[i][j], b[k][l]) for l in range(len(b[0]))])
        result.append(row)
    return result

```
