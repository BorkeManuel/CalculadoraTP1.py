
def menu_calculadora():
    limpiar_pantalla()
    print(f"{'Menu de Opciones':^50s}")
    print("1- Ingresar 1er Operando (A = x)")
    print("2- Ingresar 2do Operando (B = y)")
    print("3- Operaciones")
    print("4- Mostrar resultados")
    print("5- Salir")
    return input("\nIngrese opcion: ")

def menu_operaciones():
    print(f"\n{'Menu de Operaciones':^50s}")
    print("1- Sumar (A + B)")
    print("2- Restar (A - B)")
    print("3- Dividir (A / B)")
    print("4- Multiplicar (A * B)")
    print("5- Factorial (A!)")
    return input("\nIngrese opcion: ")



def pedir_numero()->int:
    entrada = input("Ingrese un numero: ")
    while not entrada.isdigit():
        entrada = input("Ingrese un numero: ")
    return int(entrada)


def sumar(a:int, b:int)->int:
    r_suma = a + b 
    return r_suma

def restar(a:int, b:int)->int:
    r_resta = a - b
    return r_resta

def dividir(a:int, b:int)->int:
    r_division = a / b
    return r_division

def multiplicar(a:int, b:int)->int:
    r_multiplicacion = a * b
    return r_multiplicacion

def factorial(entrada:int)->int:
    """Calcula el factorial de un numero entero

    Args:
        entrada (int): Numero entero para calcular el factorial

    Raises:
        ValueError: Lanza exception si entrada no es un numero natural

    Returns:
        int: El factorial de entrada
    """
    if entrada < 0:
        raise ValueError("El factorial es solo para numeros naturales.")
    fact = 1
    for i in range(2, entrada + 1):
        fact *= i
    return fact




def pausar():
    import os
    os.system("pause")

def limpiar_pantalla():
    import os
    os.system("cls")

def pedir_confirmacion(mensaje:str)->bool:
    rta = input(mensaje).lower()
    return rta == "s"