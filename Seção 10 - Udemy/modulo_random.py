"""
Modulo random

from random import random

for i in range(3):
    print(random())


#uniform() - gerar um número real pseudo-aleatório
#  entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) #o 7 não é incluído

# randint() - valores inteiros pseudo-aleatorios
# entre os valores estabelecidos

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')

# choice - mostra um valor aleatorio
# entre um iterável

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

# shuflle() - funcao de embaralhar dados
from random import shuffle

cartas = ['k', 'q', 'j', 'a', '2', '3', '4']

print(cartas)

shuffle(cartas)

print(cartas)
"""

