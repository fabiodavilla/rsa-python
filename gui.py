import PySimpleGUI as sg

sg.theme('Default1')

layout = [
    [
        sg.Text('Primeiro primo:', size=12),
        sg.InputText(key='primo1', size=16),
        sg.Text('Segundo primo:', size=12),
        sg.InputText(key='primo2', size=16),
        sg.Button('Calcular')
    ],
    [
        sg.Text('Chave pública:', size=12),
        sg.InputText(key='publica', size=16),
        sg.Text('Chave privada:', size=12),
        sg.InputText(key='privada', size=16)
    ],
    [
        sg.Text('Texto normal:', size=12),
        sg.InputText(key='texto_padrao', do_not_clear=False, size=50)
    ],
    [
        sg.Text('Texto encriptado:', size=12),
        sg.InputText(key='texto_encriptado', do_not_clear=False, size=50)
    ],
    [
        sg.Push(),
        sg.Button('Ok'),
        sg.Button('Cancelar')
    ]
]
