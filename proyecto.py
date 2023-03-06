#curso teorico

print("El horario de la escuela es de lunes a sábado de 8am a 9pm para el servicio de curso teórico y el costo por hora es de 2000 colones.")

horas= float(input("Cuantas horas desea contratar: "))

dias= input("Ingrese los dias en los que distribuira las horas contratadas: ")


if horas >= 1:    # Procesamiento de datos si la cantidad de horas es mayor o igual a uno
    print("Usted ha contratado: ", horas, "horas del curso teorico")
else:    # Acción si la cantidad de horas es menor a uno
    print("La cantidad de horas debe ser mayor o igual a uno. Ingrese la cantidad nuevamente.")
