# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
# def personalized_greeting(saludo = "Desconocido"):
#     print(f"Hola, {saludo}")

# personalized_greeting()


# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(5,5))

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
# def is_even (num = 44):
#     return num

# if is_even() % 2 == 0:
#     print(True)
# else:
#     print(False)

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
# def convert_to_uppercase(texto):
#     return texto.upper()

# print(convert_to_uppercase("hsdfsdfdytruyola"))


# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
# def arbitrary_sum(*num):
#      return sum(num)

# print(arbitrary_sum(4,4,5,7,34,465,57))


# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
# def generate_full_greeting(nombre, apellido):
#      return print(f"Hola, {nombre} {apellido}")

# generate_full_greeting("Arturo", "Ramirez")


# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
# def power(num, exp):
#      return num ** exp

# print(power(2,5))


# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
# def calaculate_average(num1,num2,num3):
#     return (num1 + num2 + num3) / 3

# print(calaculate_average(5,5,5))


# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
# def count_characters(cad):
#     return len(cad)

# print(count_characters("Hola"))


# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*cad):
    for i in cad:
        print(i.upper())

display_messages("hola","como","estas","hehehe")
        


