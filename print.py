# sintaxe:
# print(objetos, argumentos)

mensagem = 'funcao print()'
print(mensagem)
print('aula de python')

nome = 'Lucas Estanislau'
teste = 'Teste'
print(teste, '-', nome)


print('Outro texto')

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha.', end='')
print(' continuo na mesma linha')

nome = 'Jose'
idade = 35
msg_formatada = 'o nome dele(a) é {0} e ele(a) tem {1} anos'.format(nome, idade)
print(msg_formatada)

# f string
nome = 'Joao'
peso = 77.5
msg = f'Olá, meu nome é {nome} e meu peso é {peso} kg'
print(msg)

a = 10
b = 5
res = f'A soma de {a} com {b} é igual a {a+b}'
print(res)

valor = 125.573621
print(f'o valor é {valor:.2f}')

nome = 'Maria'
idade = 43
print(f'Nome:\t{nome}\tidade:\t{idade}')
