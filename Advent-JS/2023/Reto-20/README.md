# Reto # 20 🏋️‍♂️ Distribuye el peso

¡Tenemos problemas con la carga de los juguetes en el trineo 🛷 de Santa 🎅! Parece que la distribución de los juguetes no es la adecuada y el trineo no puede despegar. ¿Podrías ayudarnos a resolver este problema?

Para solucionarlo hemos decidido utilizar un método similar al de un filtro de imágenes. En cada posición, vamos a distribuir la carga de los juguetes en función del número de juguetes de las posiciones vecinas.

Una posición vecina es aquella que está encima, abajo, a la izquierda o a la derecha de la posición actual. Por lo tanto, no se consideran vecinas las posiciones en diagonal.

Escribe una función distributeGifts que reciba una matriz de números representando los juguetes en el trineo y devuelva otra matriz con el mismo tamaño y número de elementos pero donde cada elemento es el promedio de su valor original y los valores de sus vecinos.

Ten en cuenta que hay posiciones que son null y que no contarán para el promedio como vecino pero sí se sustituirá por el valor promedio de sus vecinos.

Ten en cuenta:

- Las matrices no siempre son cuadradas, pueden tener más filas que columnas o viceversa.
- Para redondear los valores, debes utilizar la función Math.round() de JavaScript.
- Los valores null no se tienen en cuenta para el cálculo del promedio pero sí se sustituyen por el valor promedio de sus vecinos.
- Los bordes de la matriz tienen menos vecinos posibles que el resto de posiciones.
- Siempre son números enteros positivos.
