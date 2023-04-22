import random

def mainMenu():
    print("Bienvenido a la academia de manejo")
    print("Seleccione una opción:")
    print("1. Crear una cuenta")
    print("2. Curso teórico")
    print("3. Clases de manejo")
    print("4. Dictamen médico")
    print("5. Solicitar factura electrónica")
    print("6. Ver reporte administrativo")
    print("0. Salir")

    opcion = input("Ingrese el número de la opción que desea: ")

    if opcion == "1":
        crearCuenta()
    elif opcion == "2":
        reservarCursoTeorico()
    elif opcion == "3":
        reservarClasesManejo()
    elif opcion == "4":
        dictamenMedico()
    elif opcion == "5":
        generarFactura()
    elif opcion == "6":
        reporteAdministrativo()
    elif opcion == "0":
        print("Gracias por utilizar nuestros servicios")
    else:
        print("Opción no válida, por favor ingrese una opción correcta.")
    mainMenu()

def crearCuenta():
    nombre_completo = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su número telefónico: ")
    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese una contraseña para su cuenta: ")

    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre_completo},{telefono},{correo},{contraseña}\n")

    print("¡Cuenta creada exitosamente!")

def reservarClasesManejo():
    print("Este servicio se da de martes a domingo, de 8am a 5pm, y su costo va a depender de si aporta su carro o no")

    # Horas disponibles
    print("Horas disponibles: de 8am a 5pm")
    print("Días disponibles: martes a domingo")

    horas = int(input("Ingrese la cantidad de horas a contratar (mínimo 1 hora): "))

    while horas < 1:
        horas = int(input("Cantidad de horas no válida. Ingrese la cantidad de horas a contratar (mínimo 1 hora): "))

    opcion = input(
        "¿Qué tipo de vehículo va a utilizar?\n1. Vehículo personal\n2. Vehículo de la empresa\nIngrese el número de la opción que desea: ")

    while opcion not in ["1", "2"]:
        opcion = input(
            "Opción no válida. ¿Qué tipo de vehículo va a utilizar?\n1. Vehículo personal\n2. Vehículo de la empresa\nIngrese el número de la opción que desea: ")

    if opcion == "1":
        print("Ha elegido utilizar su vehículo personal")
        costo_hora = 3000  # costo por hora con vehículo propio: 3000 colones
    else:
        print("Ha elegido utilizar el vehículo de la empresa")
        costo_hora = 4000  # costo por hora con vehículo de la empresa: 4000 colones

    # Hora de inicio
    hora_inicio = input("Ingrese la hora de inicio (formato de 24 horas, por ejemplo 13:30): ")

    # Hora de fin
    hora_fin = input("Ingrese la hora de fin (formato de 24 horas, por ejemplo 15:30): ")
    dias = input("Ingrese los días en los que distribuirá las horas contratadas (separados por comas, sin espacios): ")

    # Resumen de la reserva
    print("\nResumen de la reserva:")
    print(f"Cantidad de horas: {horas}")
    print(f"Vehículo utilizado: {'Propio' if opcion == '1' else 'De la empresa'}")
    print(f"Hora de inicio: {hora_inicio}")
    print(f"Hora de fin: {hora_fin}")
    print(f"Días: {dias}")

    # Aquí se pueden guardar los datos de la reserva en un archivo de texto, por ejemplo:
    with open("reservas.txt", "a") as file:
        file.write(
            f"Reserva de clases de manejo: {horas} horas, vehículo {opcion}, hora inicio {hora_inicio}, hora fin {hora_fin}, días {dias}\n")

    # Aquí se puede retornar el costo total de la reserva
    costo_total = horas * costo_hora
    print(f"\n¡Reserva agregada con éxito! Costo total: {costo_total} colones")
    return costo_total

import random

def generarReserva():
# Se genera un número aleatorio de 6 dígitos como identificador de reserva
    return random.randint(100000, 999999)

def reservarCursoTeorico():
    print("Este servicio se da de lunes a sábado, de 8am a 9pm, y su costo es de 2000 colones por hora.")
    print("\n")
    horas = int(input("Ingrese la cantidad de horas a contratar (mínimo 1 hora): "))

    while horas < 1:
        horas = int(input("Ingrese la cantidad de horas a contratar (mínimo 1 hora): "))

    dias = input("Ingrese los días en los que distribuirá las horas contratadas: ")
    id_reserva = generarReserva()

    with open("reservas.txt", "a") as archivo:
        archivo.write(f"{id_reserva},curso_teorico,{horas},{dias}\n")

    costo_total = horas * 2000

    print(f"¡Reserva creada exitosamente! El costo total es de {costo_total} colones.")
def dictamenMedico():
    nombre = input("\nIngrese su nombre completo: ")
    telefono = input("Ingrese su número telefónico: ")
    correo = input("Ingrese su correo electrónico: ")
    
    print("Servicio de dictamen médico:")
    tipo_sangre = input("Ingrese su tipo de sangre: ")
    peso = float(input("Ingrese su peso en kilogramos: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    
    donador = input("¿Desea ser donador de órganos? (si / no): ")
    if donador == "si":
        donador = True
    else:
        donador = False
    
    # aquí se puede generar el identificador para el dictamen médico, por ejemplo:
    identificador = f"DM-{nombre}-{telefono}"
    
    # aquí se pueden guardar los datos del dictamen médico en un archivo de texto, por ejemplo:
    with open("dictamenes.txt", "a") as file:
        file.write(f"Identificador: {identificador}\n")
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Teléfono: {telefono}\n")
        file.write(f"Correo electrónico: {correo}\n")
        file.write(f"Tipo de sangre: {tipo_sangre}\n")
        file.write(f"Peso: {peso} kg\n")
        file.write(f"Estatura: {estatura} m\n")
        file.write(f"Donador de órganos: {donador}\n")
        file.write("\n")
    
    # aquí se puede imprimir el dictamen médico con los datos ingresados
    print(f"Dictamen médico:\nIdentificador: {identificador}\nNombre: {nombre}\nTeléfono: {telefono}\nCorreo electrónico: {correo}\nTipo de sangre: {tipo_sangre}\nPeso: {peso} kg\nEstatura: {estatura} m\nDonador de órganos: {donador}")


def generarFactura():
    curso_teorico = 2000
    curso_practico_Cpropio = 3000
    curso_practico_Cprestado = 4000
    dictamen_medico = 5000

    total = 0

    with open("reservas.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if "curso_teorico" in linea:
                horas = int(linea.split(",")[2])
                total += horas * curso_teorico
            elif "curso_practico" in linea:
                opcion = linea.split(",")[3].strip()
                horas = int(linea.split(",")[2])
                if opcion == "vehiculo_propio":
                    total += horas * curso_practico_Cpropio
                elif opcion == "vehiculo_prestado":
                    total += horas * curso_practico_Cprestado

    with open("dictamenes.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            total += dictamen_medico

    print(f"El total del dictamen médico, reserva del curso teórico y clases de manejo es de {total} colones.")



def reporteAdministrativo():
    print("Reporte administrativo\n")
    total_usuarios = 0
    total_ingresos = 0

    # Contar usuarios
    with open("usuarios.txt", "r") as file:
        for line in file:
            total_usuarios += 1

    # Calcular ingresos
    with open("reservas.txt", "r") as file:
        for line in file:
            if "clases de manejo" in line:
                horas = int(line.split(": ")[1].split(" ")[0])
                vehiculo = line.split(",")[1].split(" ")[2]
                costo_hora = 3000 if vehiculo == "personal" else 4000
                total_ingresos += horas * costo_hora
            elif "curso teorico" in line:
                horas = int(line.split(": ")[1].split(" ")[0])
                total_ingresos += horas * 2000

    # Mostrar resultados
    print(f"Total de usuarios registrados: {total_usuarios}")
    print(f"Total de ingresos generados: {total_ingresos} colones")

mainMenu()