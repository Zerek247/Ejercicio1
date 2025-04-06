# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
tupla=(10, 20, 30, 40, 50)
print(tupla)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
tupla2=(100, 200, 300, 400, 500)
print(tupla2[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
tupla3=(1,2,3)
tupla3= list(tupla3)
tupla3[0] = 10
tupla3 = tuple(tupla3)
print(tupla3)
print(type(tupla3))

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
cont=(1, 2, 3, 3, 4, 5, 3)
print(cont.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
ind=("Java", "Python", "JavaScript", "Python")
print(ind.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
con1=(1,2,3)
con2=(4,5,6)
suma=con1+con2
print(suma)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
sub=(10, 20, 30, 40, 50)
print(sub[2:4])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
color=("rojo", "verde", "azul")
print(color)
color=list(color)
color[1]= "Amarillo"
color=tuple(color)
print(color)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
# my_tuple=(1,2,3,4,5)
# del my_tuple()
# print(my_tuple)

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
unico=(100,)
print(unico)
print(type(unico))