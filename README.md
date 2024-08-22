# Proyecto de Operaciones con Números Complejos

## Descripción

Este proyecto implementa una libería con una serie de funciones para realizar operaciones matemáticas con números complejos, como la suma, resta, multiplicación, división, cálculo del módulo, conjugado, fase, y conversiones entre las formas cartesiana y polar. También se incluye un menú interactivo que permite al usuario seleccionar la operación deseada y proporcionar los valores de entrada.

Además, se ha desarrollado un conjunto de pruebas unitarias utilizando el módulo `unittest` de Python para garantizar la correcta funcionalidad de cada operación.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos principales:

- `Libcplx.py`: Librería la cual contiene las funciones que realizan las operaciones con números complejos.
- `test.py`: Contiene un conjunto de pruebas unitarias para validar la correcta implementación de las funciones en `Libcplx.py`.

## Funcionalidades

Las funciones implementadas en `Libcplx.py` incluyen:

- `cplx_sum(a, b)`: Suma dos números complejos.
- `cplx_sub(a, b)`: Resta dos números complejos.
- `cplx_product(a, b)`: Multiplica dos números complejos.
- `cplx_modulo(num)`: Calcula el módulo de un número complejo.
- `cplx_div(a, b)`: Divide dos números complejos.
- `cplx_conjugate(num)`: Calcula el conjugado de un número complejo.
- `cplx_phase(num)`: Calcula la fase de un número complejo en radianes.
- `cplx_convert(num, option)`: Convierte entre las formas cartesiana y polar de un número complejo.

El menú interactivo en `Libcplx.py` permite al usuario seleccionar la operación que desea realizar y proporcionar los valores de entrada necesarios. Las opciones disponibles son:

1. Sumar dos números complejos.
2. Restar dos números complejos.
3. Multiplicar dos números complejos.
4. Dividir dos números complejos.
5. Calcular el módulo de un número complejo.
6. Obtener el conjugado de un número complejo.
7. Calcular la fase de un número complejo.
8. Convertir de cartesiano a polar.
9. Convertir de polar a cartesiano.
10. Salir del programa.

## Requisitos

- Python
- Módulo `unittest`

