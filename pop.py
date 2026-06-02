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


class Produto:
    def __init__(self, nome,preco):
        self.nome = nome
        self.preco = preco
    def exibir_dados(self):
        print(f'Produto: {self.nome}')
        print(f'valor R$: {self.preco}')
produto1=Produto('Mouse Gamer', 150)
produto1.exibir_dados()        



              
                  




     