"""
Reversed

nao é o mesmo que a função reverse(). (so funciona pra listas)
"""

palavra = "academia"
invertida = ''.join(reversed(palavra))
print(invertida)  # saida: aimedaca
    
pagamentos = [120, 135, 150, 200, 100, 90]

# Mostra os pagamentos do mais recente pro mais antigo
print(list(reversed(pagamentos)))

# Palíndromo: mesma palavra de frente pra trás e de trás pra frente
palavras = ['arara', 'radar', 'banana', 'python']

