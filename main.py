import functions as fn
import gui
import math
from PySimpleGUI import Window, Popup, WIN_CLOSED

window = Window('RSA', gui.layout)

private_key = []
public_key = []

while True:
    event, values = window.read()
    if event == WIN_CLOSED or event == 'Cancelar':
        break
    if values['primo1'] != '' and values['primo2'] != '':
        if event == 'Calcular':
            p = int(values['primo1'])
            q = int(values['primo2'])
            n = p * q
            z = (p - 1)*(q - 1)
            e = 0

            for temp in range(3, z):
                a = math.gcd(temp, z)
                if (a == 1):
                    e = temp
                    break

            d = fn.inverso_do_modulo(e, z)

            private_key = (d, n)
            public_key = (e, n)

            window['privada'].update(','.join(map(str, private_key)))
            window['publica'].update(','.join(map(str, public_key)))
    if event == 'Ok':
        if window['publica'] == '' or window['privada'] == '':
            Popup('Insira as chaves!')
        elif bool(values['texto_padrao'] == '') == bool(values['texto_encriptado'] == ''):
            Popup('Insira uma entrada para processar apenas!')
        else:
            if bool(values['texto_padrao'] != ''):
                window['texto_encriptado'].update(
                    ','.join(map(str, fn.codificar(
                        public_key, values['texto_padrao'])))
                )
                values['texto_padrao'] = ''
            else:
                window['texto_padrao'].update(
                    fn.decodificar(private_key, [int(numeric_string) for numeric_string in str(values['texto_encriptado']).split(',')]))
                values['texto_encriptado'] = ''

window.close()
