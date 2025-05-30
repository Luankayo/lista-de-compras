# Estou querendo automatizar tarefa de quando vamos no supermercado fazer compras e ficamos fazendo a soma
# na calculadora ate que nos perdemos e temos que fazer tudo de novo. e com essa automação fica claro quanto ta dando
# e os produtos que eu ja adicionei

compras = {}

print('----------AUTOMAÇÃO DE TAREFAS----------')

while True:
    try:
        resposta = int(input("Digite '1' para continuar e '2' para sair do programa: "))
        if resposta == 2:
            break
        elif resposta == 1:
            produto = input('Digite o nome do produto: ').title().strip()
            valor = float(input('Digite o valor do produto: R$ '))
            compras[produto] = valor
        else:
            print("Digite apenas 1 ou 2.")
    except ValueError:
        print("ERRO! Digite um número válido.")

print('\n---------- lista_de_compras ----------')
total = 0
for produto, valor in compras.items():
    print(f'{produto}: R$ {valor:.2f}')
    total += valor

print(f'\nValor total da compra: R$ {total:.2f}')
