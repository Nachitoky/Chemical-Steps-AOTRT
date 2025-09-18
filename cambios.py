# ==========================
# FUNCIONES BASE
# ==========================
def funcion_hallar_color(phi, m):
    print(f"El número de la TV es {phi * m}")


def obtCarreras():
    n1 = input("Combustible carreras arriba: ")
    n2 = input("Combustible carreras izquierda: ")
    return int(n1) + int(n2)


def obtVodka():
    n1 = input("Vodka arriba: ")
    n2 = input("Vodka izquierda: ")
    return int(n1) + int(n2)


def obtDetergente():
    n1 = input("Detergente arriba: ")
    n2 = input("Detergente izquierda: ")
    return int(n1) + int(n2)


def obtMonedas():
    n1 = input("Monedas arriba: ")
    n2 = input("Monedas izquierda: ")
    return int(n1) + int(n2)


def obtQuitaesmaltes():
    n1 = input("Quitaesmaltes arriba: ")
    n2 = input("Quitaesmaltes izquierda: ")
    return int(n1) + int(n2)


def obtPeniques():
    n1 = input("Peniques arriba: ")
    n2 = input("Peniques izquierda: ")
    return int(n1) + int(n2)


def obtPasta():
    n1 = input("Pasta aldehída arriba: ")
    n2 = input("Pasta aldehída izquierda: ")
    return int(n1) + int(n2)


def obtFormaldehido():
    n1 = input("Formaldehído arriba: ")
    n2 = input("Formaldehído izquierda: ")
    return int(n1) + int(n2)


def obtAcetaldehido():
    n1 = input("Acetaldehído arriba: ")
    n2 = input("Acetaldehído izquierda: ")
    return int(n1) + int(n2)


def obtAceiteMotor():
    n1 = input("Aceite de motor arriba: ")
    n2 = input("Aceite de motor izquierda: ")
    return int(n1) + int(n2)


def obtRepelente():
    n1 = input("Repelente arriba: ")
    n2 = input("Repelente izquierda: ")
    return int(n1) + int(n2)


def obtLimpiaLlantas():
    n1 = input("Limpia llantas arriba: ")
    n2 = input("Limpia llantas izquierda: ")
    return int(n1) + int(n2)


def obtFenol():
    n1 = input("Fenol arriba: ")
    n2 = input("Fenol izquierda: ")
    return int(n1) + int(n2)


def obtDesatascador():
    n1 = input("Desatascador arriba: ")
    n2 = input("Desatascador izquierda: ")
    return int(n1) + int(n2)


def obtAcidoFenol():
    n1 = input("Ácido fenol arriba: ")
    n2 = input("Ácido fenol izquierda: ")
    return int(n1) + int(n2)


def obtPintura():
    n1 = input("Pintura arriba: ")
    n2 = input("Pintura izquierda: ")
    return int(n1) + int(n2)


def obtMetilbenzeno():
    n1 = input("Metilbenceno arriba: ")
    n2 = input("Metilbenceno izquierda: ")
    return int(n1) + int(n2)


def obtBicarbonato():
    n1 = input("Bicarbonato arriba: ")
    n2 = input("Bicarbonato izquierda: ")
    return int(n1) + int(n2)


def obtVinagre():
    n1 = input("Vinagre arriba: ")
    n2 = input("Vinagre izquierda: ")
    return int(n1) + int(n2)


def obtDinitro():
    n1 = input("Dinitro arriba: ")
    n2 = input("Dinitro izquierda: ")
    return int(n1) + int(n2)


def obtLimpiacristales():
    n1 = input("Limpiacristales arriba: ")
    n2 = input("Limpiacristales izquierda: ")
    return int(n1) + int(n2)


def obtHexamina():
    n1 = input("Hexamina arriba: ")
    n2 = input("Hexamina izquierda: ")
    return int(n1) + int(n2)


def obtAbono():
    n1 = input("Abono arriba: ")
    n2 = input("Abono izquierda: ")
    return int(n1) + int(n2)


# ==========================
# TABLA DE FUNCIONES DISPONIBLES
# ==========================
tuple_list = [
    ("vodka", obtVodka),
    ("peniques", obtPeniques),
    ("acetaldehido", obtAcetaldehido),
    ("combustiblecarreras", obtCarreras),
    ("monedas", obtMonedas),
    ("formaldehido", obtFormaldehido),
    ("detergente", obtDetergente),
    ("pastaaldehida", obtPasta),
    ("quitaesmaltes", obtQuitaesmaltes),
    ("aceitemotor", obtAceiteMotor),
    ("repelente", obtRepelente),
    ("limpiallantas", obtLimpiaLlantas),
    ("fenol", obtFenol),
    ("desatascador", obtDesatascador),
    ("acidofenol", obtAcidoFenol),
    ("pintura", obtPintura),
    ("metilbenzeno", obtMetilbenzeno),
    ("bicarbonato", obtBicarbonato),
    ("vinagre", obtVinagre),
    ("dinitro", obtDinitro),
    ("limpiacristales", obtLimpiacristales),
    ("hexamina", obtHexamina),
    ("abono", obtAbono)
]

# Diccionario global que guarda los valores de cada compuesto
valores_compuestos = {nombre: None for nombre, _ in tuple_list}


# ==========================
# FUNCIONES DE COMPUESTOS FINALES
# ==========================
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


# ==========================
# SOLUCIONES
# ==========================
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


# ==========================
# MENÚ PARA EDITAR
# ==========================
def menu_editar(callback, phi):
    intValue2 = int(input("\n¿Quiere hacer algo más?"
                          "\n 0. Editar un valor"
                          "\n 1. Volver al menú"
                          "\n --> "))
    if intValue2 == 0:
        editarValores(callback=callback, callback_args=(phi,))
    return


# ==========================
# EDITAR VALORES
# ==========================
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


def main():
    phi = int(input("Introduzca Phi: "))
    m = int(input("Introduzca M: "))

    while True:
        intValue1 = int(input(
            "\n¿Qué quiere hacer?"
            "\n0. Número TV"
            "\n1. 3,4-dinitroximetilpropano"
            "\n2. 1,3,5-teranitrofenol"
            "\n3. 3-metil-2,4-dinitrobenceno"
            "\n4. Octa-hidro-2,5-nitro-3,4,7-para-zokina"
            "\n5. Salir"
            "\n --> "
        ))

        if intValue1 == 0:
            funcion_hallar_color(phi, m)
        elif intValue1 == 1:
            nitroximetilpropano(phi)
        elif intValue1 == 2:
            teranitrofenol(phi)
        elif intValue1 == 3:
            dinitrobenceno(phi)
        elif intValue1 == 4:
            hidroparazoquina(phi)
        elif intValue1 == 5:
            print("Saliendo...")
            break
        else:
            print("Debe elegir un número válido")


if __name__ == '__main__':
    main()