# ------------------------------------ MEGA REVISÃO ---------------------------------------

# Exercício 1 – For e listas
# Escreva um programa que receba uma lista de nomes e imprima cada nome em maiúsculas usando for.
lista_nomes = []

while True:
    nome = input("Digite um nome (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break  # Sai do loop

    lista_nomes.append(nome)  # Adiciona o nome à lista

# Depois que saiu do loop, imprime os nomes em maiúsculo
print("\nNOMES DIGITADOS:")
for nome in lista_nomes:
    print(nome.upper())


# Exercício 2 – While e validação
# Crie um loop while que peça para o usuário digitar uma senha. Só saia do loop quando a senha for igual a "python123".

usuario = input('Digite seu nome: ')

while True:
    senha = input(f'Digite sua senha, {usuario}: ')
    if senha == 'python123':
        print(f'Login efetuado com sucesso, {usuario}!')
        break
    else:
        print('Senha incorreta!')

# Exercício 3 – Função que calcula média
# Faça uma função que receba uma lista de números e retorne a média deles.

def media(lista):
    return sum(lista)/len(lista)

while True:
    lista = []
    sair = input("Digite 'sair' para sair ou 'continuar' para continuar: ")
    if sair.lower() == 'continuar':
        numeros = input(int('Digite os números para calcular a media: '))
        lista.append(numeros)
    elif sair.lower() == 'sair':
        break

print(media(lista))

# Exercício 4 – Combinação: função com loop for
# Crie uma função que receba uma lista de números e retorne a soma dos números pares dessa lista, usando um for.

# Exercício 5 – Combinação: função com while
# Faça uma função que peça para o usuário digitar números até que ele digite zero. A função deve retornar a soma de todos os números digitados (excluindo o zero).
#
