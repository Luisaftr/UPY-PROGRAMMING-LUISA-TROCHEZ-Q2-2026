import math
# Numerical Integration Program CLASSWORK 08 - Luisa Trochez

# INPUT
a = input("Left end point of the interval: ")
b = input("Right end point of the interval: ")

# Procesar 'pi' en a y b
if "pi" in a:
    a = float(eval(a.replace("pi", str(math.pi))))
else:
    a = float(a)

if "pi" in b:
    b = float(eval(b.replace("pi", str(math.pi))))
else:
    b = float(b)

# PROCESS
if a >= b:
    print("Error: el punto izquierdo debe ser menor que el punto derecho.")
else:
    f_x = input("Write the function in variable x (use 'math.sin(x)', 'math.cos(x)', 'x**2', etc.): ")
    method = input("Select integration method (LRM / RRM / MPM / TM): ")

    # PROCESS
    n = 1000
    h = (b - a) / n
    area = 0.0

    # Función auxiliar para evaluar f en un punto
    def evaluate(xi):
        expr = f_x.replace('x', f'({xi})')
        return eval(expr, {"__builtins__": None, "math": math}, {}) #Eval para pi y funciones matemáticas como sin,cos, etc.

    if method == 'RRM':
        xs = [a + (i + 1) * h for i in range(n)]
        for xi in xs:
            area += evaluate(xi) * h

    elif method == 'MPM':
        xs = [a + (i + 0.5) * h for i in range(n)]
        for xi in xs:
            area += evaluate(xi) * h

    elif method == 'TM':
        # Método trapezoide:
        # área = (h/2) * [f(x0) + 2*f(x1) + 2*f(x2) + ... + 2*]
        area = evaluate(a) + evaluate(b)          # primer y último valor (sin multiplicar)
        for i in range(1, n):                     
            xi = a + i * h
            area += 2 * evaluate(xi)
        area *= h / 2                             # multiplicar todo por h/2 al final por eso * antes de igual

    else:  # LRM por defecto
        xs = [a + i * h for i in range(n)]
        for xi in xs:
            area += evaluate(xi) * h

    # OUTPUT
    print(f"The integral of {f_x} on [{a}, {b}] is {area:.6f}")
    
    
    
    #⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹

                               # Numerical Integration Program CLASSWORK 08 - ERROR HANDLING
                               

def parse_limite(texto):
    texto = texto.strip()
    if "pi" in texto:
        texto = texto.replace("pi", str(math.pi))
    return float(eval(texto, {"__builtins__": None, "math": math}, {}))

# INPUT
a_texto = input("Left end point of the interval: ")
b_texto = input("Right end point of the interval: ")

try:
    a = parse_limite(a_texto)
except:
    print("El límite inferior debe ser numérico")
    exit()

try:
    b = parse_limite(b_texto)
except:
    print("El límite superior debe ser numérico")
    exit()

if a >= b:
    print("El límite inferior debe ser menor que el límite superior")
    exit()

f_x = input("Write the function in variable x (use 'math.sin(x)', 'math.cos(x)', 'x**2', etc.): ")
method = input("Select integration method (LRM / RRM / MPM / TM): ")

if f_x.strip() == "":
    print("La función ingresada no es válida")
    exit()

if "^" in f_x:
    print("La función ingresada no es válida")
    exit()

if "x" not in f_x:
    print("La función debe estar escrita en términos de x")
    exit()

if method not in ["LRM", "RRM", "MPM", "TM"]:
    print("El método de integración no es válido. Usa LRM, RRM, MPM o TM")
    exit()

def evaluate(xi):
    expr = f_x.replace('x', f'({xi})')
    return eval(expr, {"__builtins__": None, "math": math}, {})

n = 1000
h = (b - a) / n
area = 0.0

try:
    if method == 'RRM':
        for i in range(n):
            xi = a + (i + 1) * h
            area += evaluate(xi) * h

    elif method == 'MPM':
        for i in range(n):
            xi = a + (i + 0.5) * h
            area += evaluate(xi) * h

    elif method == 'TM':
        area = evaluate(a) + evaluate(b)
        for i in range(1, n):
            xi = a + i * h
            area += 2 * evaluate(xi)
        area = area * (h / 2)

    else:  # LRM
        for i in range(n):
            xi = a + i * h
            area += evaluate(xi) * h

except ZeroDivisionError:
    print("La función no está definida en algún punto del intervalo")
    exit()

# OUTPUT
print(f"The integration of {f_x} is {area:.3f}")



