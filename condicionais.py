n1 = n2 = 0.0

media = 0.0

n1 = float(input('digite a 1a nota: '))
n2 = float(input('digite a 2a nota: '))

media = (n1 + n2) / 2

if(media >= 7):
    print("Aprovado!")
    print("Parabéns")
elif(media >= 5):
    print("Recuperação")
else:
    print("Reprovado")
print("Sua média é {}".format(media))