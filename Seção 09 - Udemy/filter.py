valores = [5, 12, 3, 18, 7, 21]
# Resultado esperado: [12, 18, 21]

print(list(filter(lambda x: x > 10, valores)))

palavras = ['python', 'map', 'lambda', 'join', 'openai']
# Resultado: ['python', 'lambda', 'openai']

print(list(filter(lambda letra: len(letra) > 5, palavras)))

numeros = [1, 2, 3, 4, 5, 6]
# Resultado: [2, 4, 6]
print(list(filter(lambda x: x % 2 == 0, numeros)))

nomes = ['Luan', 'Maria', 'Matheus', 'João', 'Marcos']
# Resultado: ['Maria', 'Matheus', 'Marcos']

print(list(filter(lambda letra: letra[0] == 'M', nomes)))

valores = [True, False, True, False, True]
# Resultado: [True, True, True]

print(list(filter(lambda x: x == True, valores)))

alunos = [
    {'nome': 'Luan', 'nota': 8.5},
    {'nome': 'Maria', 'nota': 6.2},
    {'nome': 'Carlos', 'nota': 9.1},
    {'nome': 'João', 'nota': 5.0}
]

f = filter(lambda x: x['nota'] > 7, alunos)
print(list(f))
# Resultado esperado: [{'nome': 'Luan', 'nota': 8.5}, {'nome': 'Carlos', 'nota': 9.1}]


produtos = [
    {'nome': 'Smartwatch', 'preco': 200, 'promocao': True},
    {'nome': 'Cabo USB', 'preco': 25, 'promocao': False},
    {'nome': 'Fone Bluetooth', 'preco': 150, 'promocao': True},
]

promo = filter(lambda p: p['promocao'] == True, produtos)

print(list(promo))

# Resultado esperado: [{'nome': 'Smartwatch'...}, {'nome': 'Fone Bluetooth'...}]

nomes = ['Luan', 'Maria Eduarda', 'Pedro', 'Carlos Alberto', 'João']
compostos = filter(lambda nome: len(nome.split()) > 1, nomes)
print(list(compostos))

# Resultado esperado: ['Maria Eduarda', 'Carlos Alberto']


clientes = ['Amanda', 'Bruno', 'Carla', 'Beatriz', 'Luan', 'aline']

# Resultado esperado: ['Amanda', 'Bruno', 'Beatriz', 'aline']
# (Obs: a letra inicial pode estar minúscula também)

print(list(filter(lambda nome: nome[0].upper() in ['A', 'B'], clientes)))

funcionarios = [
    {'nome': 'João', 'cargo': 'Gerente', 'ativo': True},
    {'nome': 'Luan', 'cargo': 'Recepcionista', 'ativo': True},
    {'nome': 'Cláudia', 'cargo': 'Gerente', 'ativo': False},
    {'nome': 'Pedro', 'cargo': 'Gerente', 'ativo': True},
]

# Resultado esperado: [{'nome': 'João'...}, {'nome': 'Pedro'...}]
ativos = filter(lambda x: x['cargo'] == 'Gerente'and x['ativo'] == True, funcionarios)
print(list(ativos))
