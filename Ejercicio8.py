# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
dict1={
    "name": 'Arthur',
    "age": 28,
    "country": "CDMX"
}
print(dict1)

# 2. Accede al valor de la clave name en el diccionario.
print(dict1["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
dict1["Job"] = "Programador"
print(dict1)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
dict1["age"] = 38
print(dict1)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del dict1[("country")]
print(dict1)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
cuad={
    1:1**2,
    2:2**2,
    3:3**2,
    4:4**2,
    5:5**2
}
print(cuad)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
dict2={"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in dict2)

# 8. Imprime solo las claves del diccionario.
print(dict2.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
list_dict=list(dict2.keys())
print(list_dict)


# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
lista=["name", "age", "job"]
listatodict=dict.fromkeys(lista)
print(listatodict)
print(type(listatodict))