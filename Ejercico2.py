# 1. Declara y asigna valores a las siguientes variables:
# • name: una cadena que contenga tu nombre.
# • age: un número entero que represente tu edad.
# • height: un número flotante que represente tu altura.
# • Imprime cada variable en una línea separada.

name='Arturo'
age=28
height=1.68
print("Mi nombre es:", name, "\nMi edad es:",age,"\nMi estatura es:",height,"m")


# 2. Convierte la variable edad de entero a cadena y concaténala con un texto que diga cuántos años tienes.
print("Mi edad es:",(str(age)))

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student= True
print("Soy estudiante:", is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
nombre_completo='Arturo Ramirez Tejeda'
print("Mi nombre completo tiene una longitud de",len(nombre_completo),"Letras")

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
nombre, apellido, ciudad  = 'Arturo', 'Ramirez', 'Mexico'
print("Mi nombre es", nombre, "Mi apellido es:", apellido, "Soy de:",ciudad)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
color=input("Indica tu color favorito: ")
print("Tu color favorito es: ", color)

# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit= "Pera"
print("La fruta es: ",fruit)
fruit= "Manzana"
print("La fruta es: ",fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price= 10.45
print("El pecio es:" , int(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address= 'Mexico'
address_len= len(address)
print(len(address))


# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone: int = 5515038970
phone = 56.56
print("El numero es:", phone, "Y el tipo de dato es: ", type(phone))