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
