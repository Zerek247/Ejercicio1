# 1. Usa un bucle while para imprimir los números del 1 al 10.
# conteo = 0
# while conteo <= 10:
#     print(f"Num : {conteo}")
#     conteo += 1

# 2. Usa un bucle for para recorrer la lista [10, 20, 30, 40, 50] e imprime cada número.
# lista=[10, 20, 30, 40, 50]
# for elemento in lista:
#     print(f"elemento: {elemento}, y su indice en la lista es: ", lista.index(elemento))

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
# suma = 1
# while suma <= 100:
#     print(suma)
#     suma += 1

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
# a,b,c,d,e,f = "Python"
# for letra in a,b,c,d,e,f:
#     print(letra)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
# numero = 1
# while numero <= 50:
#     print(f"Numero: {numero}")
#     numero += 1
#     if numero % 7 == 0:
#         print(f"El primer numero divisible es: {numero}")
#         break

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
# dicc={"name": "Brais", 
#       "age": 37, 
#       "country": "Galicia"
#       }
# for recorrer in dicc.keys():
#     print(recorrer)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
# pares= 1
# lista = []
# while pares <= 20:
#     pares += 1
#     if pares % 2==0:
#         lista.append(str(pares))

# print("Los numero pares encontrados son: ", ", ".join(lista))

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
# for i in range(10, 0, -1):
#     print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista [30, 10, 30, 20, 30, 40].
# lista=[30, 10, 30, 20, 30, 40]
# for i in range(1):
#     conteo = lista.count(30)
#     print(conteo)

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
# lista = ["Arthur", "Brais", "XDDDd","asdgfdsgd"]
# for i in lista:
#     print(i)
#     if i == "Brais":
#         break