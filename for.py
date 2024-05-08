lista = ['maçã', 10, 'pano de prato', 9.40]
palavra = 'teste'
for item in lista:
    print(item)

for letra in palavra:
    print(letra)

for numero in range(10):
    print(numero)

nome = 'Lucas'
for x in range(10):
    print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)

for x in range(2, 20, 3):
    print(x)

jogadores = ['PH', 'Rossi', 'Praxedes', 'Hugo Moura', 'Payet']

for jogador_horrivel in jogadores:
    if jogador_horrivel == 'Payet':
        continue
    print(jogador_horrivel)