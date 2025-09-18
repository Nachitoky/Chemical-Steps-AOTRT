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
    ("aceite_motor", obtAceiteMotor),
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