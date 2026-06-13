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
