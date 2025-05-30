"""
Try, except, else, finally

DICA DE QUANDO TRATAR CODIGO:

TODA ENTRADA DEVE SER TRATADA!

a função do usuario é destruir seu sistema

# Else é executado somente se nao ocorrer o erro.
try:
    num = int(input('informe um numero: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou {num}')
# Finally

while True:
    try:
        num = int(input('Informe um número: '))
    except ValueError:
        print('❌ Você não digitou um número válido.')
    else:
        print(f'✅ Você digitou o número {num}')
        break
    finally:
        print('--- Tentativa encerrada ---')

def dividir(n1, n2):
    try:
        return int(n1) / int(n2)
    except ValueError:
        return 'Erro! Digite números inteiros'
    except ZeroDivisionError:
        return 'Não é possível fazer divisão por zero!'

num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
print(dividir(num1, num2))

"""

def dividir(n1, n2):
    try:
        return int(n1) / int(n2)
    except ValueError:
        return 'Erro! Digite números inteiros'
    except ZeroDivisionError:
        return 'Não é possível fazer divisão por zero!'

num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
print(dividir(num1, num2))
