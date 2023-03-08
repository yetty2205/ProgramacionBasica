# Inicializamos variables
tipo_sangre = ''
peso = 0
estatura = 0
es_donador = False

# Solicitamos la información del cliente
tipo_sangre = input('Ingrese su tipo de sangre: ')
peso = float(input('Ingrese su peso en kilogramos: '))
estatura = float(input('Ingrese su estatura en metros: '))
es_donador = input('¿Desea ser donador de sangre? (S/N)').upper() == 'S'

# Imprimimos el dictamen médico
print('--- DICTAMEN MÉDICO ---')
print('Tipo de sangre:', tipo_sangre)
print('Peso:', peso, 'kg')
print('Estatura:', estatura, 'm')
print('¿Es donador?:', 'Sí' if es_donador else 'No')

# Solicitamos información adicional para factura electrónica
quiere_factura = input('¿Desea factura electrónica? (S/N)').upper() == 'S'
if quiere_factura:
    rfc = input('Ingrese su RFC: ')
    nombre = input('Ingrese su nombre completo: ')
    direccion = input('Ingrese su dirección completa: ')
    correo = input('Ingrese su correo electrónico: ')

# Generamos un identificador aleatorio para el servicio
import random
identificador = random.randint(10000, 99999)

# Almacenamos la información en un archivo de texto
archivo = open('servicios.txt', 'a')
archivo.write(f'{identificador};{tipo_sangre};{peso};{estatura};{es_donador};{quiere_factura};{rfc};{nombre};{direccion};{correo}\n')
archivo.close()

# Función administrativa para ver la cantidad de dinero recolectado
# y el número de reservas
clave_admin = input('Ingrese la clave de administrador: ')
if clave_admin == 'admin123':
    archivo = open('servicios.txt', 'r')
    reservas = 0
    dinero = 0
    for linea in archivo:
        datos = linea.split(';')
        if datos[5] == 'True':
            dinero += 1000
        reservas += 1
    archivo.close()
    print(f'Cantidad de dinero recolectado: ${dinero}')
    print(f'Número de reservas: {reservas}')
else:
    print('Clave de administrador incorrecta')
