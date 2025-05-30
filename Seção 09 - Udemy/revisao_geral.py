# 🧠 1. lambda + sorted
# Você tem uma lista de dicionários com pessoas e idades:

# pessoas = [
#     {"nome": "Lucas", "idade": 25},
#     {"nome": "Joana", "idade": 19},
#     {"nome": "Carlos", "idade": 32},
# ]
# Ordena essa lista pela idade usando sorted() com lambda.

pessoas = [
    {"nome": "Lucas", "idade": 25},
    {"nome": "Joana", "idade": 19},
    {"nome": "Carlos", "idade": 32},
]

ordem = sorted(pessoas, key=lambda c: c['idade'])

print(ordem)

#
# 🧠 2. map() + formatação
# Dada a lista nomes = ["ana", "joão", "MARIA", "CARLOS"], usa map() com lambda pra formatar os nomes assim: primeira letra maiúscula e o resto minúsculo.

# Resultado esperado: ["Ana", "João", "Maria", "Carlos"]

nomes = ["ana", "joão", "MARIA", "CARLOS"]

formatado = map(lambda nome: nome.title(), nomes)

print(list(formatado))

# 🧠 3. filter() + lambda
# Com a lista salarios = [1200, 2500, 4000, 800, 3500], filtra os salários acima de 2000 usando filter().

salarios = [1200, 2500, 4000, 800, 3500]

filtrado = filter(lambda sal: sal > 2000, salarios)

print(list(filtrado))

# 🧠 5. any() + all() misturado
# Você tem uma lista de senhas digitadas por usuários:

# senhas = ["123", "abc123", "senhaSegura!", "admin", "senha123"]
# Usa any() pra saber se alguma senha tem mais de 10 caracteres.

# Usa all() pra saber se todas têm pelo menos 5 caracteres.

senhas = ["123", "abc123", "senhaSegura!", "admin", "senha123"]

print(any(len(x) > 10 for x in senhas))

print(all(len(x) >= 5 for x in senhas))

# 🧠 6. generator expression + soma condicional
# Gera os quadrados dos números de 1 a 20 apenas se forem múltiplos de 3, e soma tudo com sum().

print(sum(x ** 2 for x in range(21) if x % 3 == 0))

# 🧠 7. sorted() em string complexa
# Dada essa lista:

# produtos = ["TV 32", "Geladeira", "Microondas", "TV 50", "Fogão"]
# Ordena primeiro por tipo do produto (ignora o número da TV), usando key= com lambda.

produtos = ["TV 32", "Geladeira", "Microondas", "TV 50", "Fogão"]

ordenados = sorted(produtos, key=lambda x: x.split()[0])

print(ordenados)
