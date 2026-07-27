
# Classwork 16 - Recursive Functions
 
# Cuenta regresiva
def recursiva(n):
    try:
        if not isinstance(n, int):
            raise TypeError("n debe ser un numero entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")
 
        if n == 0:
            return "Done!"
        else:
            print(n)
            return recursiva(n - 1)
 
    except (TypeError, ValueError) as error:
        print(f"Error en recursiva: {error}")
        return None
 
 
# 2. Fibonacci
def fibonacci(n):
    try:
        if not isinstance(n, int):
            raise TypeError("n debe ser un numero entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")
 
        if n == 0 or n == 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
 
    except (TypeError, ValueError) as error:
        print(f"Error en fibonacci: {error}")
        return None
 
 
# 3. Factorial
def factorial(n):
    try:
        if not isinstance(n, int):
            raise TypeError("n debe ser un numero entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")
 
        if n == 0 or n == 1:
            return 1
        else:
            return factorial(n - 1) * n
 
    except (TypeError, ValueError) as error:
        print(f"Error en factorial: {error}")
        return None
 
 
# 4. Multiplicacion recursiva
def multiplicacion_recursiva(n, m):
    try:
        if not isinstance(n, int) or not isinstance(m, int):
            raise TypeError("n y m deben ser numeros enteros")
        if m < 0:
            raise ValueError("m no puede ser negativo")
 
        
        if m == 0:
            return 0
        else:
            return multiplicacion_recursiva(n, m - 1) + n
 
    except (TypeError, ValueError) as error:
        print(f"Error en multiplicacion_recursiva: {error}")
        return None
 
 
# 5. Division entera recursiva
def division_entera_recursiva(dividendo, divisor):
    try:
        if not isinstance(dividendo, int) or not isinstance(divisor, int):
            raise TypeError("dividendo y divisor deben ser numeros enteros")
        if divisor == 0:
            raise ZeroDivisionError("el divisor no puede ser 0")
        if dividendo < 0:
            raise ValueError("el dividendo no puede ser negativo")
 
        if dividendo - divisor < 0:
            return 0
        else:
            return division_entera_recursiva(dividendo - divisor, divisor) + 1
 
    except (TypeError, ValueError, ZeroDivisionError) as error:
        print(f"Error en division_entera_recursiva: {error}")
        return None
 
 
# 6. Potencia recursiva
def potencia_recursiva(base, exponente):
    try:
        if not isinstance(base, (int, float)) or not isinstance(exponente, int):
            raise TypeError("base debe ser numero y exponente debe ser entero")
        if exponente < 0:
            raise ValueError("el exponente no puede ser negativo")
 
        if exponente == 0:
            return 1
        else:
            return potencia_recursiva(base, exponente - 1) * base
 
    except (TypeError, ValueError) as error:
        print(f"Error en potencia_recursiva: {error}")
        return None
 
 
# 7. Serie de Collatz
def serie_collatz(n):
    try:
        if not isinstance(n, int):
            raise TypeError("n debe ser un numero entero")
        if n <= 0:
            raise ValueError("n debe ser mayor a 0")
 
        if n == 1:
            print("END!")
            return 0
        else:
            if n % 2 == 0:
                print(n // 2)
                return serie_collatz(n // 2)
            else:
                print(3 * n + 1)
                return serie_collatz(3 * n + 1)
 
    except (TypeError, ValueError) as error:
        print(f"Error en serie_collatz: {error}")
        return None
 
 
# 8. Aplanar un JSON (diccionario anidado)
def aplanar_json(diccionario, clave_padre='', separador='.'):
    try:
        if not isinstance(diccionario, dict):
            raise TypeError("diccionario debe ser un dict")
 
        elementos = []
        for key, value in diccionario.items():
            nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key
 
            if isinstance(value, dict):
                elementos.extend(aplanar_json(value, nueva_llave, separador).items())
            else:
                elementos.append((nueva_llave, value))
 
        return dict(elementos)
 
    except TypeError as error:
        print(f"Error en aplanar_json: {error}")
        return {}
 
 
# Pruebas
if __name__ == "__main__":
    print("--- recursiva ---")
    print(recursiva(5))
    print(recursiva(-3))       
    print(recursiva("5"))     
 
    print("\n--- fibonacci ---")
    print(fibonacci(7))
    print(fibonacci(-1))       
 
    print("\n--- factorial ---")
    print(factorial(5))
    print(factorial(1.5))      
 
    print("\n--- multiplicacion_recursiva ---")
    print(multiplicacion_recursiva(4, 3))
    print(multiplicacion_recursiva(4, -3))   
 
    print("\n--- division_entera_recursiva ---")
    print(division_entera_recursiva(17, 5))
    print(division_entera_recursiva(10, 0))   
 
    print("\n--- potencia_recursiva ---")
    print(potencia_recursiva(2, 5))
    print(potencia_recursiva(2, -2))         
 
    print("\n--- serie_collatz ---")
    print(serie_collatz(6))
    print(serie_collatz(0))                  
 
    print("\n--- aplanar_json ---")
    print(aplanar_json({"a": 1, "b": {"c": 2}}))
    print(aplanar_json(["a", "b", "c"]))     
 
