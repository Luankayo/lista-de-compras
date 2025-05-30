# 1️⃣ Ordena os planos do mais barato pro mais caro.
# 2️⃣ Cria uma lista formatada assim com map():
# ["Plano: Mensal Básico - R$ 59.90", "Plano: Mensal Premium - R$ 89.90", ...]
# 3️⃣ Filtra só os planos com mais de 20 clientes ativos.
# 4️⃣ Usa any() pra saber se algum plano custa mais de R$ 800.
# 5️⃣ Usa all() pra saber se todos os planos têm mais de 10 clientes ativos.
# 6️⃣ Cria um generator expression que gera apenas os nomes dos planos com mais de 30 clientes, e exibe com list()
# 7️⃣ Soma o faturamento total da academia (preço × ativos de cada plano).

planos = [
    {"nome": "Mensal Básico", "preco": 59.90, "ativos": 32},
    {"nome": "Mensal Premium", "preco": 89.90, "ativos": 45},
    {"nome": "Anual Básico", "preco": 599.90, "ativos": 12},
    {"nome": "Anual Premium", "preco": 899.90, "ativos": 28},
    {"nome": "Trimestral", "preco": 199.90, "ativos": 15},
]

ordenados = sorted(planos, key=lambda x: x['preco'])

print(f'Lista de Planos do mais barato ao mais caro:')

# Agora, imprimindo cada plano em uma linha separada
for plano in ordenados:
    print(f"Plano: {plano['nome']} | Preço: R${plano['preco']:.2f} | Quant. de Planos ativos: {plano['ativos']}")
    print('-' * 40)  # Separador entre os planos

filtrados = filter(lambda plano: plano['ativos'] > 20, planos)

print('Planos com mais de 20 alunos:')
for plano in filtrados:
    print(f'📌 {plano["nome"]} - {plano['ativos']} alunos ativos')


print(any(plano['preco'] > 800 for plano in planos))
print(all(plano['ativos'] > 10 for plano in planos))

gerador = (plano for plano in planos if plano['ativos'] > 30)
print(list(gerador))


calculo = (plano['preco'] * plano['ativos'] for plano in planos)

faturamento_total = sum(calculo)

print('=' * 40)
print(f'O faturamento total da academia é de R$ {faturamento_total}')


