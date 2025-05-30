"""
Generators

Em aulas anteriores nós estudamos:
- list comprehension;
- dict comprehension;
- set comprehension
"""

# 🧠 1. Números pares
# Cria uma generator expression que gere os números pares de 0 até 20.

pares = (x for x in range(0,21) if x % 2 == 0)

print(list(pares))

# 🧠 2. Comprimento das palavras
# Dada a lista palavras = ["banana", "uva", "abacaxi", "kiwi"], cria uma generator expression que gere o comprimento de cada palavra.

palavras = ["banana", "uva", "abacaxi", "kiwi"]

comprimento = (f'O nome {fruta} tem {len(fruta)} letras' for fruta in palavras)

print(list(comprimento))

# 3. Apenas os nomes com mais de 4 letras
# Com a lista nomes = ["Ana", "Carlos", "Be", "Lucas", "Jo"], cria uma generator expression que só retorne os nomes com mais de 4 letras.

nomes = ["Ana", "Carlos", "Be", "Lucas", "Jo"]

letras = (letra for letra in nomes if len(letra) > 4)

print(list(letras))

# 🧠 4. Potências de 2
# Cria uma generator expression que gere as potências de 2 de 0 até 10 (tipo 2⁰, 2¹, 2²...).

potencias = (2 ** x for x in range(11))
print(list(potencias))

# 🧠 5. Soma total de uma generator expression
# Cria uma generator expression que gere os números de 1 a 100, e depois soma tudo com sum().
numeros = sum(x for x in range(101))

print(numeros)


