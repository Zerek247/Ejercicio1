# 1. Crea un set con los números del 1 al 5 e imprímelo.
set1={1,2,3,4,5}
print(set1)

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
set1.add(6)
print(set1)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
set1.add(5)
print(set1)

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in set1)

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
set1.remove(4)
print(set1)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
set1.clear()
print(set1)

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
setf={"manzana", "naranja", "plátano"}
setf = list(sorted(setf))
print(setf[0])
print(type(setf))

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
seta={1,2,3}
setb={4,5,6}
print(seta.union(setb))

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
setdif1={1,2,3,4}
setdif2={3,4,5,6}
print(setdif1.difference(setdif2))

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
dele={1,2,3}
del dele
#print(dele)
