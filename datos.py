def obtener_datos_usuario():
    nombre = input("Ingrese su nombre: ")
    correo_electronico = input("Ingrese su correo electrónico: ")
    numero_telefonico = input("Ingrese su número telefónico: ")
    return nombre, correo_electronico, numero_telefonico

nombre_usuario, correo_electronico_usuario, numero_telefonico_usuario = obtener_datos_usuario()

print("Nombre: ", nombre_usuario)
print("Correo electrónico: ", correo_electronico_usuario)
print("Número telefónico: ", numero_telefonico_usuario)  

