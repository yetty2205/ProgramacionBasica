#curso  de manejo practico

print("Este servicio se da de martes a domingo, de 8am a 5pm, y su costo va a depender de si aporta su carro o no")

horas = float(input("Ingrese la cantidad de horas a contratar: "))

print("¿Que tipo de vehiculo va a utilizar: ?")
print("1. Vehiculo personal")
print("2. Vehiculo de la empresa")

opcion = input("Ingrese el numero de la opcion que desea: ")

if opcion == "1":
    print("Ha elegido utilizar su vehiculo personal")
elif opcion == "2":
    print("Ha elegido utilizar el vehiculo de la empresa")
else:
    print("Opcion no valida, ingrese la opcion nuevamente") 

dias = input("Ingrese los dias en los que distribuira las horas contratadas: ")


    
    
