from random import randint
computador = randint (0, 5)#faz o computador pensar
#print ('Pensei no número {}'.format(computador))
print ('-=-' * 20)
print ('Vou pensar em um número de 0 e 5.Tente advinhar...')
print ('-=-' * 20)
jogador = int (input('Em que número eu pensei? ')) #jogador tenta advinhar
if jogador == computador:
    print ('Parabéns, você acertou')
else:
    print('Ganhei! eu pensei no número {} e não no {}!'.format(computador, jogador))
