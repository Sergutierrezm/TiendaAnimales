from typing import no_type_check
from datetime import datetime

#Inventario realizado mendiante un Diccionario
inventario = {
    "perro": 10,
    "gato": 8,
    "pajaros": 10
}
cantidad_animal = 0
for val in inventario.values():
    cantidad_animal += val

compras = []

#Saludos al usuario despues de registrar el nombre y apellidos
print("Bienvenido a la tienda de mascotas")
print("Indica tu nombre")
nombre = input()
print("indica tu apellido")
apellido = input()
nombre_completo = nombre + " " + apellido
print("Encatando", nombre_completo)


#Menu con opciones
def MenuDelPrograma():
    print("Selecciona la opcion que deseas")
    print("1: Conocer cuantos animales tenemos")
    print("2: comprar un animal")
    print("3: Mostrar compras")
    print("4: Salir del programa")

#Inventario
def mostrar_inventario():
    print("Actualmente tenemos:")
    for llave, valor in inventario.items():
        print(f"{llave}: {valor}")
    
#Funcion para que el usuario pueda comprar un animal
def comprar_animal ():
    carrito = []
    while True:
        print("¿Que animal quieres comprar?")
        print("Escribe F si desea salir de la lista o V si deseas ver los animales que estas comprando")
        animal = input()
        if animal == "F":
            break
        if animal == "V":
            print(f"Estos son los animales que llevas en el carro {carrito}") 
            continue
        if animal not in inventario:
            print(f"Lo sentimos, ese {animal} no lo tenemos")
        elif inventario[animal] == 0:
            print(f"Ese {animal} esta agotado")    
        elif animal not in carrito:
            carrito.append(animal)
        else:
            print("Ese animal ya se encuentra en el carro")

    print("El contenido de tu carro es:")
    for animal in carrito:
        print(" ", animal)
        inventario[animal] -= 1
    fecha = datetime.now()
    compras.append((nombre, carrito,fecha))

#Funcion para revisar el historial de compras de animales con fecha y nombre del usuario
def mostrar_compras():
    print("")
    print("Compras realizadas")
    for compra in compras:
        print(f"   {compra[0]} compró {compra[1]} en  {compra[2]}")


#Logica del programa asociada con las funciones
while True:
    MenuDelPrograma()
    respuesta = int(input())
    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:   
        comprar_animal()
    elif respuesta == 3:
        mostrar_compras()
    elif respuesta == 4:
        print("Saliendo del programa")
        break    
    

