# Pedir al usuario que ingrese su nombre completo
nombre_completo = input("Ingrese su nombre completo: ")

# Pedir al usuario que ingrese su número telefónico
telefono = input("Ingrese su número telefónico: ")

# Pedir al usuario que ingrese su correo electrónico
correo = input("Ingrese su correo electrónico: ")

# Pedir al usuario que ingrese su contraseña
contraseña = input("Ingrese una contraseña para su cuenta: ")

# Abrir el archivo de texto en modo de escritura y agregar los datos del usuario
with open("usuarios.txt", "a") as archivo:
    archivo.write(f"{nombre_completo},{telefono},{correo},{contraseña}\n")

# Confirmar al usuario que se ha creado su cuenta exitosamente
print("¡Cuenta creada exitosamente!")


