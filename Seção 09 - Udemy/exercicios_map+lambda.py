"""
# 1. Dobre todos os números da lista: [2, 4, 6, 8] usando map + lambda

numeros = [2, 4, 6, 8]

dobro = map(lambda x: x * 2, numeros)

print(list(dobro))

# Transforme todos os nomes para MAIÚSCULAS:

nomes = ['ana', 'maria', 'joao']

maiusculas = map(lambda palavras: palavras.upper(), nomes)

print(list(maiusculas))

# Remova os espaços extras dos nomes:

nomes = [' Luan  ', ' Maria ', ' João   ']

corrigido = map(lambda letras: letras.strip(), nomes)

print(list(corrigido))

# Converta todos os preços da lista para float:

precos = ['10.50', '23.99', '5.00']

floatt = map(lambda x: float(x), precos)

print(list(floatt))


# Crie uma lista que mostre se os números são pares ou ímpares:

numeros = [1, 2, 3, 4, 5]

resultado = map(lambda x: 'par' if x % 2 == 0 else 'impar', numeros)

print(list(resultado))


# Pegue uma lista de nomes e retorne apenas as iniciais:

# nomes = ['Ana Beatriz', 'João Silva', 'Maria Clara']
#
# iniciais = map(lambda letra: letra[0], nomes)
#
# print(list(iniciais))


palavras = ['código', 'lógica', 'python']
# Resultado esperado: 'código, lógica, python'

print(', '.join(palavras))

numeros = [1, 2, 3, 4]
str_numeros = map(str, numeros)  # ou list comprehension: [str(n) for n in numeros]
print('-'.join(str_numeros))  # Resultado: '1-2-3-4'

# ❓3. Pegue as iniciais dos nomes e junte numa string só:

# nomes = ['Luan Kayo', 'Maria Eduarda', 'Pedro Lucas']
# # Resultado esperado: ['LK', 'ME', 'PL']
# # Bônus: junta todos em uma única string: 'LKMEPL'

nomes = ['Luan Kayo', 'Maria Eduarda', 'Pedro Lucas']

iniciais = map(lambda letra: ''.join([parte[0] for parte in letra.split()]), nomes)

juntos = ''.join(iniciais)
print(juntos)
"""

numeros = [2, 3, 5, 7, 11]
# Resultado esperado: [4, 9, 25, 49, 121]

quadrado = map(lambda x: x ** 2, numeros)

print(list(quadrado))

# 🔹 2. Converta temperaturas de Celsius para Fahrenheit
# Fórmula: F = (C * 1.8) + 32

celsius = [0, 10, 25, 30, 40]
# Resultado: [32.0, 50.0, 77.0, 86.0, 104.0]

conversao = map(lambda f: (f * 1.8) + 32, celsius)

print(list(conversao))


# 🔹 3. Adicione “R$” no início de todos os valores

# Resultado: ['R$10.50', 'R$25.00', 'R$99.90']
# (Dica: usar f-string dentro do lambda com format)

valores = [10.5, 25, 99.9]
formatado = list(map(lambda v: f'R${v:.2f}', valores))
print(formatado)  # ['R$10.50', 'R$25.00', 'R$99.90']

# 🔹 4. Pegue o comprimento de cada palavra

palavras = ['Python', 'map', 'lambda', 'join']
# Resultado: [6, 3, 6, 4]

resultado = map(lambda letras: len(letras), palavras)
print(list(resultado))

# 🔹 5. Nome + idade formatado

pessoas = [('Luan', 21), ('Maria', 19), ('Carlos', 30)]
# Resultado: ['Luan tem 21 anos', 'Maria tem 19 anos', 'Carlos tem 30 anos']

result = map(lambda x: f'{x[0]} tem {x[1]} anos', pessoas)

print(list(result))
