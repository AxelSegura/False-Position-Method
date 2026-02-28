import math


def regla_falsa(f, xi, xd, epsilon=0.001, iteraciones=100): #tabla y epsilon
    print("=" * 80)
    print("MÉTODO DE LA REGLA FALSA")
    print("=" * 80)
    print(f"Función: {f.__doc__}")
    print(f"Intervalo inicial: [{xi}, {xd}]")
    print(f"Tolerancia: {epsilon}")
    print("-" * 80)
    print("| n |     xi     |     xd     |    f(xi)   |    f(xd)   |     xm     |     ε     |   f(xm)    |")
    print("-" * 80)
    
    tabla = []
    iteracion = 1
    
    if f(xi) * f(xd) > 0:
        print("Error: La función no cambia de signo en el intervalo dado")
        return None, None
    
    while iteracion <= iteraciones:
        f_xi = f(xi)
        f_xd = f(xd)
        
        xm = xd - (f_xd * (xd - xi)) / (f_xd - f_xi)
        f_xm = f(xm)
        
        
        if iteracion == 1:
            error = 1.0  
        else:
            error = abs((xm - xm_anterior) / xm) if xm != 0 else abs(xm - xm_anterior)
        
      
        fila = {
            'n': iteracion,
            'xi': xi,
            'xd': xd,
            'f_xi': f_xi,
            'f_xd': f_xd,
            'xm': xm,
            'error': error,
            'f_xm': f_xm
        }
        tabla.append(fila)
        print(f"| {iteracion:2d} | {xi:.6f} | {xd:.6f} | {f_xi:9.6f} | {f_xd:9.6f} | {xm:.6f} | {error:8.6f} | {f_xm:9.6f} |")
        if error <= epsilon:
            print("-" * 80)
            print(f"¡Tolerancia alcanzada en la iteración {iteracion}!")
            print(f"Raíz aproximada: {xm:.8f}")
            print(f"f(xm) = {f_xm:.8f}")
            print(f"Error: {error:.8f}")
            print("=" * 80)
            return tabla, xm
        
        if f_xi * f_xm < 0:  
            xd = xm
        else:  
            xi = xm
        
        xm_anterior = xm
        iteracion += 1
    print("-" * 80)
    print(f"Número máximo de iteraciones ({max_iter}) alcanzado")
    print("=" * 80)
    return tabla, xm

# Funciones
def f1(x):
    return x**3 + 2*x**2 + 7*x -20
if __name__ == "__main__":

    print("REGLAS FALSA - EJERCICIOS")
    print("=" * 80)
    
    print("\nEjercicio 1:")
    tabla1, raiz1 = regla_falsa(f1, 1.0, 2.0) #intervalos
    
    if raiz1 is not None:
        print(f"\nResultado final Ejercicio 1:")
        print(f"Raíz: {raiz1:.8f}")
        print(f"Verificación: f({raiz1:.8f}) = {f1(raiz1):.8f}")
        
    
    print("\n" + "=" * 80)
