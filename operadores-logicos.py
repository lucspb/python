idade = 15
altura = 1.80

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar do evento? ' + str(resultado)
print(msg)

# disparar alarme | or
porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg2 = 'alarme disparado? ' + str(alarme)
print(msg2)


# negacao
pode_sair = True
pode_sair = not pode_sair
msg3 = 'Posso sair?' + str(pode_sair)
print(msg3)