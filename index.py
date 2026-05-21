import flet as ft   # as significa renomear para ft

def main(page: ft.Page): # essa função vai criar uma página
    def clicar(e):
        texto.value = 'App Flet'
       
        page.update()
    

    texto = ft.Text('Usando o Flet')
    botao = ft.ElevatedButton('Clique aqui', on_click=clicar)

    
    
    page.add(texto,botao)

ft.app(target=main)
