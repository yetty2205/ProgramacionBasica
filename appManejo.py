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
        """ solicitarFactura() """
    elif opcion == "5":
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
    mainMenu()

import random

def generarReserva():
# Se genera un número aleatorio de 6 dígitos como identificador de reserva
    return random.randint(100000, 999999)

def reservarCursoTeorico():
    print("Este servicio se da de lunes a sábado, de 8am a 9pm, y su costo es de 2000 colones por hora.")
    horas = int(input("Ingrese la cantidad de horas a contratar (mínimo 1 hora): "))

    while horas < 1:
        horas = int(input("Ingrese la cantidad de horas a contratar (mínimo 1 hora): "))

    dias = input("Ingrese los días en los que distribuirá las horas contratadas: ")
    id_reserva = generarReserva()

    with open("reservas.txt", "a") as archivo:
        archivo.write(f"{id_reserva},curso_teorico,{horas},{dias}\n")

    costo_total = horas * 2000

    print(f"¡Reserva creada exitosamente! El costo total es de {costo_total} colones.")
    mainMenu()

def reservarClasesManejo():
    print("Este servicio se da de martes a domingo, de 8am a 5pm, y su costo va a depender de si aporta su carro o no")

    horas = int(input("Ingrese la cantidad de horas a contratar (mínimo 1 hora): "))

    while horas < 1:
        horas = int(input("Cantidad de horas no válida. Ingrese la cantidad de horas a contratar (mínimo 1 hora): "))

    opcion = input("¿Qué tipo de vehículo va a utilizar?\n1. Vehículo personal\n2. Vehículo de la empresa\nIngrese el número de la opción que desea: ")

    while opcion not in ["1", "2"]:
        opcion = input("Opción no válida. ¿Qué tipo de vehículo va a utilizar?\n1. Vehículo personal\n2. Vehículo de la empresa\nIngrese el número de la opción que desea: ")

    if opcion == "1":
        print("Ha elegido utilizar su vehículo personal")
        costo_hora = 3000  # costo por hora con vehículo propio: 3000 colones
    else:
        print("Ha elegido utilizar el vehículo de la empresa")
        costo_hora = 4000  # costo por hora con vehículo de la empresa: 4000 colones

    dias = input("Ingrese los días en los que distribuirá las horas contratadas (separados por comas, sin espacios): ")

    # aquí se pueden guardar los datos de la reserva en un archivo de texto, por ejemplo:
    with open("reservas.txt", "a") as file:
        file.write(f"Reserva de clases de manejo: {horas} horas, vehículo {opcion}, días {dias}\n")

    # aquí se puede retornar el costo total de la reserva
    return horas * costo_hora
mainMenu()

def dictamenMedico():
    nombre = input("Ingrese su nombre completo: ")
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
    mainMenu()


def reporteAdministrativo(clave):
    if clave != "admin123": # Verifica que la clave de administrador sea correcta
        print("Clave incorrecta. Acceso denegado.")
        return
    
    
    num_reservas = 0
    dinero_total = 0
    
    
    with open("reservas.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.split(",") 
            tipo_servicio = datos[0]
            costo = int(datos[1])
            num_horas = int(datos[2])
            
            num_reservas += num_horas
            dinero_total += costo * num_horas
            
    # Imprime el reporte administrativo con la cantidad de reservas y el dinero recolectado
    print(f"Cantidad de reservas: {num_reservas}")
    print(f"Dinero recolectado: {dinero_total} colones")
    mainMenu()



