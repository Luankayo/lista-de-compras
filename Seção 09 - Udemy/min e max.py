"""
Min e Max

max() -> retorna o maior valor de um iteravel ou maior de dois ou mais elementos

"""
nomes  = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']

print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))


musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock in roll', 'tocou': 3}

]

msc1 = max(musicas, key=lambda x: x['tocou'])
msc2 = min(musicas, key=lambda x: x['tocou'])

for musica in msc1:
    print(f'A musica que tocou mais: {msc1['titulo']}')
    break

for musica in msc2:
    print(f'A musica que tocou menos: {msc2['titulo']}')
    break
