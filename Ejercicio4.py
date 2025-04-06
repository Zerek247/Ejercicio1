# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text='Aprendiendo Python'
print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
print("Hola" + " " + "Python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
print("Hola\nmi nomnre es\nArturo")

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name='Arturo'
apellido="Ramirez"
age=28
print(f"Mi nombre es {name}, mi apellido es {apellido}, y mi edad es {age}")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
palabra='Python'
a,b,c,d,e,f= palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
palabra="Programacion"
pal_slice=palabra[3:8]
print(pal_slice)


# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
palabra="Python"
pal_reverse=palabra[::-1]
print(pal_reverse)


# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
cadena="aprendiendo python"
print(cadena.upper())


# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
frase="Programacion en Python"
print(frase.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
numerica="12345"
print(numerica.isnumeric())