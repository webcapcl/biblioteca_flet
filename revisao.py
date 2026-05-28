








#ATIVIDADE 3

# numeros = [] # lista
# soma = 0
# for i in range(5):   # esse comando ele gera 5 vezes i// de index in/// de 
#     numero = int(input('Digite um número: '))          # representa a variavel de cada número que ira receber dentro da lista
#     numeros.append(numero)

# for numero in numeros:
#     soma = soma + numero
# print('Soma Total: ',soma)


 # 1. Cria uma lista vazia para armazenar os números
# # numeros = []

# # 2. Usa um laço para pedir 5 números ao usuário
# for i in range(5):
#     num = int(input(f"Digite o {i+1}º número: "))
#     numeros.append(num)

# # 3. Inicializa a variável que vai acumular a soma
# soma_total = 0

# # 4. Usa o 'for' para somar todos os números da lista
# for numero in numeros:
#     soma_total += numero

# # 5. Mostra o resultado final
# print(f"\nA soma de todos os números digitados é: {soma_total}")


#ATIVIDADE 5

# 1. Cria uma lista com 4 notas
notas = []
soma = 0
for i in range(4):
    nota = float(input('Digite sua nota: '))
    notas.append(nota)

for nota in notas: 
    soma = soma + nota 
media = soma / len(notas)

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')


