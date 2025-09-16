def main():
    phi = int(input("Introduzca Phi: "))
    m = int(input("Introduzca M: "))
    while True:
        n = int(input(
            "\n¿Qué quiere hacer?"
            "\n0. Número TV"
            "\n1. 3,4-dinitroximetilpropano"
            "\n2. 1,3,5-teranitrofenol"
            "\n3. 3-metil-2,4-dinitrobenceno"
            "\n4. Octa-hidro-2,5-nitro-3,4,7-para-zokina"
            "\n5. Salir"
            "\n --> "
        ))

        if n == 0:
            funcion_hallar_color(phi, m)
        elif n == 1:
            nitroximetilpropano(phi)
        elif n == 2:
            teranitrofenol()
        elif n == 3:
            dinitrobenceno()
        elif n == 4:
            hidroparazoquina()
        elif n == 5:
            print("Saliendo...")
            break
        else:
            print("Debe elegir un número entre 0 y 5")


def funcion_hallar_color(phi, m):
    print(f"El número de la TV es {phi * m}")


# ===============================
# Funciones input de elementos
# ===============================
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


# ===============================
# Funciones de compuestos finales
# ===============================
def nitroximetilpropano(phi):
    print("--- SPAWN ---")
    comb_carreras = obtCarreras()
    vodka = obtVodka()
    detergente = obtDetergente()

    print("--- TIENDA ---")
    monedas = obtMonedas()
    quitaesmaltes = obtQuitaesmaltes()
    peniques = obtPeniques()

    print("--- GASOLINERA ---")
    pasta_aldehida = obtPasta()
    formaldehido = obtFormaldehido()

    print("--- ESTACIÓN TV ---")
    acetaldehido = obtAcetaldehido()
    
    # Pasos quimicos
    print(f"Vodka [TIENDA] + Peniques [TIENDA] --> {vodka + peniques - phi}")
    print(f"Combustible de carreras [GASOLINERA] + Monedas [TELEFONOS] --> {comb_carreras + monedas - phi}")
    print(f"Formaldehído [GARAJE] + Acetaldehído [GARAJE] + Detergente [TIENDA] --> {formaldehido + acetaldehido + detergente - phi}")
    print(f"Pasta aldehída [GARAJE] + Quitaesmalte [HOTEL (cerca de la casetilla)] --> {pasta_aldehida + quitaesmaltes - phi}")
    return None


def teranitrofenol():
    print("--- SPAWN ---")
    repelente = obtRepelente()
    detergente = obtDetergente()


    print("--- TIENDA ---")
    desatascador = obtDesatascador()
    
    print("--- GASOLINERA ---")
    acido_fenol = obtAcidoFenol()
    fenol = obtFenol()

    print("--- PLAYA ---")
    aceite_motor = obtAceiteMotor()
    limpia_llantas = obtLimpiaLlantas()

    # Pasos quimicos
    print(f"Aceite motor [GARAJE] + Repelente [] + Limpia llantas [GARAJE] --> {aceite_motor + repelente + limpia_llantas}")
    print(f"Fenol [GARAJE] + Desatascador [TIENDA] --> {fenol + desatascador}")
    print(f"Ácido fenolsulfónico [GARAJE] + Detergente [TIENDA] --> {acido_fenol + detergente}")
    return None


def dinitrobenceno():
    print("--- SPAWN ---")
    comb_carreras = obtCarreras()
    bicarbonato = obtBicarbonato()
    detergente = obtDetergente()

    print("--- TIENDA ---")
    desatascador = obtDesatascador()

    print("--- GASOLINERA ---")
    dinitro = obtDinitro()

    print("--- PARKING CARAVANAS ---")
    pintura = obtPintura()
    vinagre = obtVinagre()

    print("--- ESTACION TV ---")
    metilbenzeno = obtMetilbenzeno()

    # Pasos quimicos
    print(f"Desatascador [GASOLINERA] + Pintura [GASOLINERA] + Detergente [TIENDA] --> {desatascador + pintura + detergente}")
    print(f"Metilbenceno [SPAWN] + Bicarbonato [SPAWN] + Vinagre [TIENDA] + Detergente [TIENDA] --> {metilbenzeno + bicarbonato + vinagre + detergente}")
    print(f"Dinitro [SPAWN] + Combustible de carreras [GASOLINERA] --> {dinitro + comb_carreras}")
    return None


def hidroparazoquina():
    print("--- SPAWN ---")
    comb_carreras = obtCarreras()
    detergente = obtDetergente()

    print("--- TIENDA ---")
    monedas = obtMonedas()
    limpiacristales = obtLimpiacristales()

    print("--- GASOLINERA ---")
    hexamina = obtHexamina()
    formaldehido = obtFormaldehido()

    print("--- PARKING CARAVANAS ---")
    abono = obtAbono()
    vinagre = obtVinagre()

    # Pasos quimicos
    print(f"Combustible de carreras [GASOLINERA] + Monedas [TIENDA] --> {comb_carreras + monedas}")
    print(f"Formaldehído [GASOLINERA] + Limpiacristales [SPAWN] --> {formaldehido + limpiacristales}")
    print(f"Hexamina [SPAWN] + Vinagre [TIENDA] + Abono [SPAWN] + Detergente [GASOLINERA] --> {hexamina + vinagre + abono + detergente}")
    return None


if __name__ == '__main__':
    main()