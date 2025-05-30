"""
Any e All


"""
# 1. Verifica se tem pelo menos um número positivo:
numeros = [-2, -3, 0, -1, 4]

print(any([num > 0 for num in numeros]))

# 2. Verifica se todos os nomes têm mais de 3 letras:
nomes = ['Ana', 'João', 'Lucas', 'Be']

print(all(len(letras) > 3 for letras in nomes))
