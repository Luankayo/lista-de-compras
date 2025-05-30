# Ordene os planos do mais barato pro mais caro e imprima a lista.

planos = [
    {"nome": "Mensal", "preco": 79.90},
    {"nome": "Trimestral", "preco": 199.90},
    {"nome": "Anual", "preco": 699.90}
]

ordenados = sorted(planos, key=lambda plano: plano['preco'])
print(ordenados)

planos2 = [
    {"nome": "Mensal", "alunos_ativos": 15},
    {"nome": "Trimestral", "alunos_ativos": 35},
    {"nome": "Anual", "alunos_ativos": 60}
]

filtro = filter(lambda plano: plano['alunos_ativos'] > 30, planos2)

print(list(filtro))

planos = [
    {"nome": "Mensal", "preco": 79.90},
    {"nome": "Trimestral", "preco": 199.90},
    {"nome": "Anual", "preco": 699.90}
]

print(any([valor['preco'] < 100 for valor in planos]))
print(all([valor['preco'] < 1000 for valor in planos]))

planos = [
    {"nome": "Mensal", "preco": 79.90, "alunos_ativos": 10},
    {"nome": "Trimestral", "preco": 199.90, "alunos_ativos": 5},
    {"nome": "Anual", "preco": 699.90, "alunos_ativos": 2}
]


faturamento_total = sum(plano['preco'] * plano['alunos_ativos'] for plano in planos)
print(f"Faturamento total: R$ {faturamento_total:.2f}")
