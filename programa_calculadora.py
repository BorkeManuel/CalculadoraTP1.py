from funciones_calculadora import *
#-----------------------------------------------------------------
flag_primero = False
flag_segundo = False

flag_suma = False
flag_resta = False
flag_divis = False
div_cero = False
flag_multip = False
flag_fact = False


seguir = "s"
while seguir == "s":
    match menu_calculadora():
        case "1":
            entrada_1 = pedir_numero()
            flag_primero = True
        case "2":
            if flag_primero == True:
                entrada_2 = pedir_numero()
                flag_segundo = True
            else:
                print("Debe ingresar un primer operando primero")
                pausar()
        case "3":
            if flag_primero == False and flag_segundo == False:
                print("Es necesario ingresar operandos")
                pausar()
            else:
                match menu_operaciones():
                    case "1":
                        resultado_sumar = sumar(entrada_1, entrada_2)
                        flag_suma = True
                    case "2":
                        resultado_restar = restar(entrada_1, entrada_2)
                        flag_resta = True
                    case "3":
                        if entrada_2 == 0:
                            resultado_dividir = print("No es posible dividir por cero.")
                            div_cero = True
                        else:
                            resultado_dividir = dividir(entrada_1, entrada_2)
                            flag_divis = True
                    case "4":
                        resultado_multiplicar = multiplicar(entrada_1, entrada_2)
                        flag_multip = True
                    case "5":
                        resultado_fact_a = factorial(entrada_1)
                        resultado_fact_b = factorial(entrada_2)
                        flag_fact = True
        case "4":
            if flag_suma == True:
                print(f"El resultado de {entrada_1}+{entrada_2} es: {resultado_sumar}")
            if flag_resta == True:
                print(f"El resultado de {entrada_1}-{entrada_2} es: {resultado_restar}")
            if flag_divis == True:
                print(f"El resultado de {entrada_1}/{entrada_2} es: {resultado_dividir:.2f}")
            if div_cero == True:
                print(f"No es posible dividir por cero")
            if flag_multip == True:
                print(f"El resultado de {entrada_1}*{entrada_2} es: {resultado_multiplicar}")
            if flag_fact == True:
                print(f"El factorial de {entrada_1} es: {resultado_fact_a} y El factorial de {entrada_2} es: {resultado_fact_b}")
            if flag_primero == False and flag_segundo == False:
                print("Es necesario ingresar operandos")
            elif flag_suma == False and flag_resta == False and flag_divis == False and \
                div_cero == False and flag_multip == False and flag_fact == False:
                    print("Aún no se realizó ninguna operación.")
            pausar()
        case "5":
            if pedir_confirmacion("Confirma salida? s/n: "):
                seguir = "n"
                continue


print("\nFin del programa")