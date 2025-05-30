"""
Reduce

a partir do python 3+ a funcao reduce nao é mais uma funcao integrada
(built-in)

Temos que importar e utilizar essa funcao a partir do modulo 'functools'

Guido van Rossum: utilize a função reduce() se vc realmente precisa dela
em todo caso, 99% das vezes um loop for é mais legivel.

"""

from functools import reduce

dados = [2, 3, 4, 6, 9, 5, 4, 6, 3, 2, 7, 8, 9, 4, 3, 5]


multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)
