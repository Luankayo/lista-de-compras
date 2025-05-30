# 1. Gere um número aleatório entre 1 e 10 e peça pro usuário tentar adivinhar

from random import randint

for i in range(1):
    print(randint(1, 10))

# 2. Faça um programa que recebe uma lista de nomes e sorteia um deles.

from random import choice
nomes = []

while True:
    try:
        nome = input('Digite seu nome (ou (sair) para sair: ')
        if nome.lower() == 'sair':
            break
        nomes.append(nome)
    except ValueError:
        print('ERRO! Digite um nome válido.')

print(choice(nomes))

# 3. Peça 4 nomes e mostre uma ordem aleatória para apresentação dos trabalhos.

from random import shuffle

lista = []
while True:
    alunos = input('Digite o nome dos alunos para apresentar o trabalho(ou (sair) para sair): ')
    if alunos.lower() == 'sair':
        break
    lista.append(alunos)

shuffle(lista)
print(lista)

# 4. Crie um dado de 6 lados que pode ser "rolado" infinitamente até o usuário digitar "sair".

from random import randint

dado = [1, 2, 3, 4, 5, 6]

while True:
    resposta = input('Deseja rolar o dado? Digite SIM para rolar e NAO para sair: ')
    if resposta.lower() == 'sair':
        break
    elif resposta.lower() == 'sim':
        print(randint(1, 6))

print('programa finalizado!')

# 5. Sorteie 6 números únicos entre 1 e 60 (simulador de Mega-Sena).

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')
