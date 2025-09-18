from functions import *

lista = [
    'abono', 'acetaldehido', 'acidofenol', 'acidomixto', 'aceitemotor',
    'bicarbonato', 'combcarreras', 'combustiblecarreras', 'desatascador',
    'dinitro', 'fenol', 'formaldehido', 'glicerol', 'glycerol', 'grasa',
    'hexamina', 'hielo', 'llimpiallantas', 'limpiacristales', 'metilbenzeno',
    'monedas', 'pastaaldehida', 'peniques', 'pintura', 'quitaesmaltes',
    'repelente', 'solucionnitrada', 'detergente', 'vinagre', 'vodka'
    ]

dicc = {
    "vodka": obtVodka(),
    "peniques": obtPeniques(),
    "acetaldehido": obtAcetaldehido(),
    "combustiblecarreras": obtCarreras(),
    "monedas": obtMonedas(),
    "formaldehido": obtFormaldehido(),
    "detergente": obtDetergente(),
    "pastaaldehida": obtPasta(),
    "quitaesmaltes": obtQuitaesmaltes(),
    "aceite_motor": obtAceiteMotor(),
    "repelente": obtRepelente(),
    "limpiallantas": obtLimpiaLlantas(),
    "fenol": obtFenol(),
    "desatascador": obtDesatascador(),
    "acidofenol": obtAcidoFenol(),
    "pintura": obtPintura(),
    "metilbenzeno": obtMetilbenzeno(),
    "bicarbonato": obtBicarbonato(),
    "vinagre": obtVinagre(),
    "dinitro": obtDinitro(),
    "limpiacristales": obtLimpiacristales(),
    "hexamina": obtHexamina(),
    "abono": obtAbono(),
}