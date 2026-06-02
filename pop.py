### sem POO -Programação Odrientada a Objeto
# cor = 'Preto'
# modelo = 'Civic'

# def acelerar():
#     print('O carro acelerou ')
# print(cor)
# print(modelo)
# acelerar()

# # Programação orientada a objeto.
# class Carro:
#     def __init__(self, cor, modelo, combustivel, motor):
#         self.cor = cor
#         self.modelo = modelo
#         self.combustivel= combustivel
#         self.motor = motor

#     def acelerar(self):
#         print('O carro acelerou')    

# carro1 = Carro('Preto', 'Civic', 'Gasolina','Turbo')
# carro2 = Carro('Vermelho', 'Gol ','Gasolina','Turbo')

# print(carro1.cor)
# print(carro1.modelo)
# print(carro1.combustivel)
# print(carro1.motor)

# print(carro2.cor)
# print(carro2.modelo)
# print(carro2.combustivel)
# print(carro2.motor)

# carro1.acelerar()


# class Conta:
#     def __init__(self,titular,saldo):
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self, valor):
#         self.saldo += valor
#         print('Depósito Realizado')        
#     def mostrar_saldo(self):
#         print(f'Saldo Atual : {self.saldo}')    

#     def sacar(self, valor):
#         self.saldo -= valor
#         print('Saque Realizado')

# conta1 = Conta('Fulano', 1000)
# print(conta1.titular)
# conta1.depositar(500)
# conta1.depositar(500)
# conta1.sacar(300)
# conta1.mostrar_saldo()


# class Produto:
#     def __init__(self, nome,preco):
#         self.nome = nome
#         self.preco = preco
#     def exibir_dados(self):
#         print(f'Produto: {self.nome}')
#         print(f'valor R$: {self.preco}')
# produto1=Produto('Mouse Gamer', 150)
# produto1.exibir_dados()        

# class Aluno:
#     def __init__(self,nome,nota1,nota2):
#         self.nome=nome
#         self.nota1=nota1
#         self.nota2=nota2

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

# --- Testando o Sistema ---

# Criando o objeto com os dados fornecidos
aluno1 = Aluno(nome="Carlos", nota1=8, nota2=6)

# Calculando a média e verificando a situação
media_final = aluno1.calcular_media()
situacao_final = aluno1.verificar_situacao()

# Exibindo os resultados
print(f"Aluno: {aluno1.nome}")
print(f"Média: {media_final:.1f}")
print(f"Situação: {situacao_final}")





              
                  




     