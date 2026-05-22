import flet as ft

def main(page:ft.Page):
 
    page.title = 'Calculadora'
    numero1 = ft.TextField(label='Primeiro número')
    numero2 = ft.TextField(label='Segundo número')

    resultado = ft.TextField(label='Resultado:')

    
    def calcular(e):
        n1=float(numero1.value) 
        n2=float(numero2.value)
        
       
       
        operacao = operacoes.value # value tras as informaçoes que estão dentro de operaões

        if operacao == '+':
            conta=n1+n2
        elif operacao == '-':
            conta=n1-n2    
        elif operacao == '*':
            conta=n1*n2        
        elif operacao == '/':
            conta=n1/n2    

        resultado.value = f'Resultado: {conta}'
        page.update()

    operacoes = ft.Dropdown(     # Dropdown cria uma lista de informações///variavel operações vai ter uma lista com o comando ft.Dropdown
            label="Escolha a operação",
            options=[
               ft.dropdown.Option('+'),
               ft.dropdown.Option('-'),
               ft.dropdown.Option('*'),
               ft.dropdown.Option('/'),
            ]

        ) 

    botao = ft.ElevatedButton(
        "calcular",
        on_click=calcular
    )


    page.add(numero1,numero2,operacoes,resultado,botao)

ft.app(target=main)



