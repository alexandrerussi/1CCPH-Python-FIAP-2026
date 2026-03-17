print("Ola mundo")

print(7 + 4)
print("7 + 4")
print("7" + "4") # CONCATENANDO STRINGS

# Comentários em python (1 linha)
'''
    Comentários de
    múltiplas
    linhas
'''

# VARIÁVEIS
nome = "Alexandre" # str
idade = 26 # int
peso = 70.2 # float

print(nome, idade, peso)

# INPUT - SIMULA FORMS NO CMD
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(nome, idade, peso)
print(f"Oiii, {nome}!!!")

ano_nascimento = 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(idade)