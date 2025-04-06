# 1. Crea una lista con los números del 1 al 5 e imprímela.
lista_num=[1,2,3,4,5]
print(lista_num)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
lista2=[10,20,30,40,50]
print(lista2[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
lista3=[1,2,3,4,5]
lista3.append(6)
print(lista3)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
lista4=[10,20,30,40,50]
lista4.insert(2,15)
print(lista4)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
lista5=[10,20,30,30,40,50]
del lista5[2]
print(lista5)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
lista6=[1,2,3,4,5]
varpop=lista6.pop(-1)
print(varpop,"\n",lista6)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
lista_r = [100, 200, 300, 400, 500]
lista_r.reverse()
print(lista_r)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
list_asc=[3, 1, 4, 2, 5]
list_asc.sort()
print(list_asc)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
conc1=[1, 2, 3]
conc2=[4, 5, 6]
final=conc1 + conc2
print(final)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
sub=[10, 20, 30, 40, 50]
print(sub[1:3 ])