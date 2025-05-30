

produtos = [
    {"nome": "Creatina", "preco": 120, "estoque": 8},
    {"nome": "Whey", "preco": 99, "estoque": 0},
    {"nome": "Pré-Treino", "preco": 150, "estoque": 5},
]
# Ordena os produtos pelo preço **somente se o estoque for maior que 0**
# Mostra nome e preço dos produtos disponíveis


ordenados = sorted(produtos, key=lambda x: x['preco'])
print(ordenados)

