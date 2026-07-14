#Classwork 07 - Git/Github Repo
#INPUT
rol = input("Ingresa tu rol UTFSM (sin guión ni dígito verificador): ")

#PROCESS
rol_invertido = rol[::-1]
secuencia = [2, 3, 4, 5, 6, 7]
suma = 0

for i in range(len(rol_invertido)):
    digito = int(rol_invertido[i])        # convertimos el carácter a número
    multiplicador = secuencia[i % 6]      # i % 6 hace que se repita la secuencia
    suma += digito * multiplicador

modulo = suma % 11
digito_verificador = 11 - modulo

# OUTPUT
print(f"El dígito verificador es: {digito_verificador}")
print(f"Tu rol completo es: {rol}-{digito_verificador}")



#⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹


                                       #Classwork 07 - ERROR HANDLING


#INPUT
rol_completo = input("Ingresa tu rol UTFSM con guión y dígito verificador (formato XXXXXXXXX-X): ")

#PROCESS Y ERROR HANDLING
partes = rol_completo.split("-")

if len(partes) != 2:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")

else:
    rol = partes[0]
    digito_ingresado = partes[1]

    if rol.isdigit() == False:
        print("Los digitos del rol deben ser numéricos")

    elif digito_ingresado.isdigit() == False:
        print("El digito verificador debe ser numérico")

    else:
        rol_invertido = rol[::-1]
        secuencia = [2, 3, 4, 5, 6, 7]
        suma = 0

        for i in range(len(rol_invertido)):
            digito = int(rol_invertido[i])        # convertimos el carácter a número
            multiplicador = secuencia[i % 6]      # i % 6 = repetri ciclo
            suma += digito * multiplicador

        modulo = suma % 11
        digito_verificador = 11 - modulo
        digito_ingresado = int(digito_ingresado)

        if digito_verificador != digito_ingresado:
            print(f"Error: El dígito verificador no conicide, se esperaba {digito_verificador}")

        else:
            # OUTPUT
            print(f"{rol}-{digito_verificador}")