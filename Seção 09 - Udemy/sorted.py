"""
Sorted

o sort() so funciona com listas.

sorted() para ordernar elementos.

"""

# 🧠 1. Ordenar números em ordem crescente
# Dada a lista numeros = [15, 2, 34, 10, 55], cria um código que ordene os números de forma crescente. Exiba a lista ordenada.

numeros = [15, 2, 34, 10, 55]

ordenados = sorted(numeros)

print(ordenados)

# 🧠 2. Ordenar palavras por tamanho
# Com a lista palavras = ["morango", "kiwi", "maçã", "abacaxi", "pera"], ordene as palavras por tamanho. Exiba a lista ordenada.

palavras = ["morango", "kiwi", "maçã", "abacaxi", "pera"]

ordenados = sorted(palavras, key=lambda letra: len(letra))
print(ordenados)

# 🧠 3. Ordenar strings em ordem alfabética inversa
# Dada a lista nomes = ["João", "Ana", "Lucas", "Carlos"], cria um código que ordene os nomes em ordem alfabética decrescente.


nomes = ["João", "Ana", "Lucas", "Carlos"]

ordenados = sorted(nomes, key=lambda letra: letra[0], reverse=True)

print(ordenados)
