from functions import *

# Función con el menú principal
def main():

    phi = int(input("Introduzca Phi: "))
    m = int(input("Introduzca M: "))
    while True:
        valor1 = int(input(
            "\n¿Qué quiere hacer?"
            "\n0. Número TV"
            "\n1. 3,4-dinitroximetilpropano"
            "\n2. 1,3,5-teranitrofenol"
            "\n3. 3-metil-2,4-dinitrobenceno"
            "\n4. Octa-hidro-2,5-nitro-3,4,7-para-zokina"
            "\n5. Salir"
            "\n --> "
        ))

        if valor1 == 0:
            funcion_hallar_color(phi, m)
        elif valor1 == 1:
            nitroximetilpropano(phi)
        elif valor1 == 2:
            teranitrofenol(phi)
        elif valor1 == 3:
            dinitrobenceno(phi)
        elif valor1 == 4:
            hidroparazoquina(phi)
        elif valor1 == 5:
            print("Saliendo...")
            break
        else:
            print("Debe elegir un número entre 0 y 5")

# Diccionario global que guarda los valores de cada compuesto
valores_compuestos = {nombre: None for nombre, _ in tuple_list}

# Funciones para obtener los compuestos finales. Recibe los datos de "arriba" e "izquierda" y los suma para guardarlos en un diccionario
def nitroximetilpropano(phi):
    v = valores_compuestos
    if v["combustiblecarreras"] is None:
        v["combustiblecarreras"] = obtCarreras()
        v["vodka"] = obtVodka()
        v["detergente"] = obtDetergente()
        v["monedas"] = obtMonedas()
        v["quitaesmaltes"] = obtQuitaesmaltes()
        v["peniques"] = obtPeniques()
        v["pastaaldehida"] = obtPasta()
        v["formaldehido"] = obtFormaldehido()
        v["acetaldehido"] = obtAcetaldehido()

    nitroximetilpropano_sol(phi)
    menu_editar(nitroximetilpropano, phi)


def teranitrofenol(phi):
    v = valores_compuestos
    if v["repelente"] is None:
        v["repelente"] = obtRepelente()
        v["detergente"] = obtDetergente()
        v["desatascador"] = obtDesatascador()
        v["acidoofenol"] = obtAcidoFenol()
        v["fenol"] = obtFenol()
        v["aceitemotor"] = obtAceiteMotor()
        v["limpiallantas"] = obtLimpiaLlantas()

    teranitrofenol_sol(phi)
    menu_editar(teranitrofenol, phi)


def dinitrobenceno(phi):
    v = valores_compuestos
    if v["combustiblecarreras"] is None:
        v["combustiblecarreras"] = obtCarreras()
        v["dinitro"] = obtDinitro()
        v["detergente"] = obtDetergente()
        v["desatascador"] = obtDesatascador()
        v["pintura"] = obtPintura()
        v["vinagre"] = obtVinagre()
        v["metilbenzeno"] = obtMetilbenzeno()
        v["bicarbonato"] = obtBicarbonato()

    dinitrobenceno_sol(phi)
    menu_editar(dinitrobenceno, phi)


def hidroparazoquina(phi):
    v = valores_compuestos
    if v["combustiblecarreras"] is None:
        v["combustiblecarreras"] = obtCarreras()
        v["detergente"] = obtDetergente()
        v["monedas"] = obtMonedas()
        v["limpiacristales"] = obtLimpiacristales()
        v["hexamina"] = obtHexamina()
        v["formaldehido"] = obtFormaldehido()
        v["abono"] = obtAbono()
        v["vinagre"] = obtVinagre()

    hidroparazoquina_sol(phi)
    menu_editar(hidroparazoquina, phi)

# Funciones solución. Mediante los datos del diccionario, calcula el número a poner en la máquina de reacciones.
def nitroximetilpropano_sol(phi):
    v = valores_compuestos
    print(f"\nVodka + Peniques --> {v['vodka'] + v['peniques'] - phi}")
    print(f"Combustible de carreras + Monedas --> {v['combustiblecarreras'] + v['monedas'] - phi}")
    print(f"Formaldehído + Acetaldehído + Detergente --> {v['formaldehido'] + v['acetaldehido'] + v['detergente'] - phi}")
    print(f"Pasta aldehída + Quitaesmaltes --> {v['pastaaldehida'] + v['quitaesmaltes'] - phi}")


def teranitrofenol_sol(phi):
    v = valores_compuestos
    print(f"\nAceite motor + Repelente + Limpia llantas --> {v['aceitemotor'] + v['repelente'] + v['limpiallantas'] - phi}")
    print(f"Fenol + Desatascador --> {v['fenol'] + v['desatascador'] - phi}")
    print(f"Ácido fenol + Detergente --> {v['acidoofenol'] + v['detergente'] - phi}")


def dinitrobenceno_sol(phi):
    v = valores_compuestos
    print(f"\nDesatascador + Pintura + Detergente --> {v['desatascador'] + v['pintura'] + v['detergente'] - phi}")
    print(f"Metilbenceno + Bicarbonato + Vinagre + Detergente --> {v['metilbenzeno'] + v['bicarbonato'] + v['vinagre'] + v['detergente'] - phi}")
    print(f"Dinitro + Combustible de carreras --> {v['dinitro'] + v['combustiblecarreras'] - phi}")


def hidroparazoquina_sol(phi):
    v = valores_compuestos
    print(f"\nCombustible de carreras + Monedas --> {v['combustiblecarreras'] + v['monedas'] - phi}")
    print(f"Formaldehído + Limpiacristales --> {v['formaldehido'] + v['limpiacristales'] - phi}")
    print(f"Hexamina + Vinagre + Abono + Detergente --> {v['hexamina'] + v['vinagre'] + v['abono'] + v['detergente'] - phi}")


# Funciones para editar valores. Esta función recibe un nombre de compuesto y lo busca en el diccionario para editar su valor.
def editarValores(callback=None, callback_args=()):
    strValue1 = input("Introduzca el nombre del compuesto que quiere cambiar:\n--> ")
    strValue1 = strValue1.lower().strip().replace("_", "")

    for nombre, funcion_elemento in tuple_list:
        if strValue1 == nombre:
            nuevo_valor = funcion_elemento()
            valores_compuestos[nombre] = nuevo_valor
            print(f"Nuevo valor para {nombre}: {nuevo_valor}")
            break
    else:
        print("Ese compuesto no existe en la lista.")
        return

    if callback:
        callback(*callback_args)
    return

# Función menú. Le indica al usuario si quiere cambiar algún valor o si desea volver al menú.
def menu_editar(callback, phi):
    intValue2 = int(input("\n¿Quiere hacer algo más?"
                          "\n 0. Editar un valor"
                          "\n 1. Volver al menú"
                          "\n --> "))
    if intValue2 == 0:
        editarValores(callback=callback, callback_args=(phi,))
    return

if __name__ == '__main__':
    main()