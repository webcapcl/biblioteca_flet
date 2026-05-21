import flet as ft   

def main(page: ft.Page): 
    def clicar(e):
        # Se o texto atual for a frase inicial, muda para a nova
        if texto.value == 'Usando o Flet':
            texto.value = 'App Flet'
        else:
            # Se já estiver como 'App Flet', volta para a frase do início!
            texto.value = 'Usando o Flet'
        
        page.update() # Atualiza a página para mostrar a mudança
    

    texto = ft.Text('Usando o Flet')
    botao = ft.ElevatedButton('Clique aqui', on_click=clicar)

    page.add(texto, botao)

ft.app(target=main)