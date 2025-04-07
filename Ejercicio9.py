# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
# num = 5
# if num > 0:
#     print("Tu numero es positivo")
# elif num < 0:
#     print("Tu numero es negativo")
# else:
#     print("Tu numero es igual a 0")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad (18 años o más) o menor de edad.
# ing = int(input("Ingresa tu edad: "))
# if ing >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")


# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
# stri=""
# if stri:
#     print("No esta vacia")
# else:
#     print("La cadena esta vacia")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
# a=int(input("Ingresa el primer numero "))
# b=int(input("Ingresa el segundo numero "))
# if a > b:
#     print(f"{a} es mayor a {b}")
# elif a < b:
#     print(f"{a} es menor a {b}")
# else:
#     print(f"{a} es igual a {b}")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
# div=int(input("Ingresa un numero: "))
# if div % 3 == 0 and div % 5 == 0:
#     print("El numero cumple las condiciones")
# else:
#     print("el numero no cumple")


# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
# par=int(input("Ingresa un numero: "))
# if par % 2 == 0:
#     print("Tu numero es par")
# else:
#     print("Tu numero es impar")


# 7. Escribe un programa que determine si una persona puede votar en función de su edad (mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
# voto=int(input("Ingresa tu edad: "))
# if voto >= 18:
#     print("Puedes votar")
# elif voto == 16 or voto == 17:
#     print("Puedes votar pero necesitas un permiso especial")
# else:
#     print("No puedes votar")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
# contra="hola123"
# sol=input("Ingresa la contrase;a: ")
# if sol == contra:
#     print("Acceso autorizado")
# else:
#     print("Error, no coincide")

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
# entre=int(input("Ingresa un numero del 10 al 20: "))
# if entre >= 10 and entre <= 20:
#     print("El numero esta entre 10 y 20")
# else:
#     print("ERROR!! no esta entre 10 y 20")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color (rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
# semaforo=(input("En que color esta el semaforo? "))
# if semaforo.lower() == "verde":
#     print("Avance")
# elif semaforo.lower() == "amarillo":
#     print("Alerta!")
# elif semaforo.lower() == "rojo":
#     print("DETENGASEEE!!")
# else:
#     print("Ese color no existe")