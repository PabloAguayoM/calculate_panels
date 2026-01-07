# calculate_panels

Este proyecto implementa la función `calculate_panels(a, b, x, y)` cuyo objetivo es determinar la cantidad máxima de paneles rectangulares de dimensiones `a × b` que pueden colocarse dentro del área de un techo de dimensiones `x × y`, permitiendo la rotación de los paneles.

## Problema a resolver

Dado un panel rectangular y un techo rectangular, se debe calcular cuántos paneles caben dentro del techo considerando ambas orientaciones posibles, sin restricciones de posición u orientación, y retornando únicamente un valor entero.

No se requiere graficar ni optimizar más allá de lo solicitado.

## Enfoque de la solución

La solución realiza:

1. Verificación básica para detectar casos donde los paneles no caben.
2. Cálculo del área del techo y del área del panel.
3. Evaluación de ambas orientaciones del panel (`a × b` y `b × a`).
4. División entera para maximizar el número de paneles posibles.
5. Retorno del valor máximo obtenido.

## Archivos del proyecto

- `principal.py`: Contiene la función `calculate_panels`.
- `prueba.py`: Incluye los tests basados en los ejemplos del enunciado.

## Ejemplos de prueba

Resultados esperados según el enunciado:

| Paneles (a×b) | Techo (x×y) | Resultado |
|---|---|---|
| 1×2 | 2×4 | 4 |
| 1×2 | 3×5 | 7 |
| 2×2 | 1×10 | 0 |

## Ejecución

Para ejecutar los tests:

```bash
python prueba.py
