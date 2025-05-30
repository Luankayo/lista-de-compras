# Exercício 1 – Divisão segura
# Crie uma função chamada dividir(a, b) que retorna a divisão de a por b.
# Se b for zero, capture a exceção e mostre a mensagem: "Erro: divisão por zero", retornando None.

def dividir(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Erro: divisão por zero')


print(dividir(10, 2))

# Exercício 2 – Conversão de string para inteiro
# Peça para o usuário digitar um número.
# Tente converter esse valor para inteiro usando int().
# Se der erro, exiba: "Entrada inválida, digite um número inteiro".


while True:
    try:
        num = int(input('Digite um número: '))
        print(f'Você digitou o número {num}')
        break  # sai do loop se der certo
    except ValueError:
        print('Entrada inválida! Digite um número inteiro.')

# Exercício 3 – Soma de lista com validação
# Crie uma função chamada soma_lista(lista) que soma apenas os valores numéricos da lista.
# Se algum valor da lista não for número, ignore ele e exiba: "Valor inválido ignorado: X".

def soma_lista(lista):
    soma = 0
    for item in lista:
        try:
            soma += item
        except TypeError:
            print(f'Valor inválido ignorado: {item}')
    return soma

# Exemplo de uso
print(soma_lista([6, 3, 4]))                   # Deve somar tudo: 13
print(soma_lista([6, 'a', 2, None, 5]))        # Deve ignorar 'a' e None, somando: 13



# Exercício 4 – Cadastro com validação
# Crie uma função chamada cadastrar_usuario() que pede nome e idade com input().
# A idade deve ser convertida para inteiro.
# Se a conversão falhar, exiba uma mensagem de erro e continue pedindo até o usuário digitar corretamente.

def cadastrar():
    while True:
        nome = input('Digite seu nome: ')
        try:
            idade = int(input('Digite sua idade: '))
            break
        except ValueError:
            print('Erro! Digite um número inteiro para sua idade.')
    print(f'Usuário {nome} tem {idade} anos de idade.')

cadastrar()

# Exercício 5 – Calculadora com tratamento de exceções
# Crie uma função chamada calc(a, b, operador) que realiza operações matemáticas (+, -, *, /).
# Trate os seguintes erros:
# - Divisão por zero -> mostrar "Erro: divisão por zero"
# - Operador inválido -> mostrar "Erro: operador inválido"
# - Tipos inválidos -> mostrar "Erro: valores informados não são números"
