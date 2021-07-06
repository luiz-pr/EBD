from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
Layout = [
    [sg.Text('nome: '), sg.Input(key='nome')],
    [sg.Text('Departamento: '), sg.Input(key='departamento')],
    [sg.Checkbox('Trouxe Bíblia?')],
    [sg.Checkbox('Trouxe Revista?')],
    [sg.Checkbox('Trouxe Visitante?')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', Layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Salvar':
        if valores['nome'] == 'luiz' and valores['departanmento'] == 'jovem':
            print('Hello world!')

pessoa = [valores['nome'], valores['departamento'], ]