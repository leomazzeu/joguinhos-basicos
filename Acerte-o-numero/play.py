from random import randint

pontos = 0
tentativas = 0

print('SEJA BEM VINDO AO JOGO')
print('Objetivo: Escolha um número de 1 a 10.')
print('Se o número escolhido for o mesmo que o do computador, você vence.')
decisao = int(input('Deseja jogar? 1 - SIM | 2 - NÃO: '))

while (decisao != 1 and decisao != 2):
    print('Por favor, digite um valor válido.')
    decisao = int(input('Deseja jogar? 1 - SIM | 2 - NÃO: '))
while (decisao == 1):
    jogadaComputador = randint(1, 10)
    jogadaUsuario = int(input('Escolha um número de 1 a 10: '))
    while (jogadaUsuario < 1 or jogadaUsuario > 10):
        jogadaUsuario = int(input('Escolha um número de 1 a 10: '))
    if (jogadaUsuario == jogadaComputador):
        print('Parabéns! Você acertou.')
        print('Você somou +1 ponto.')
        tentativas = tentativas + 1
        pontos = pontos + 1
        decisao = int(input('Deseja jogar novamente? 1 - SIM | 2 - NÃO: '))
    else:
        tentativas = tentativas + 1
        print('Que pena! Você não acertou dessa vez.')
        decisao = int(input('Deseja jogar novamente? 1 - SIM | 2 - NÃO: '))
    while (decisao != 1 and decisao != 2):
            print('Por favor, digite um valor válido.')
            decisao = int(input('Deseja jogar? 1 - SIM | 2 - NÃO: '))
    
if (decisao == 2):
    print('!FIM DO JOGO!')
    print(f'Sua pontuação: {pontos}')
    print(f'Número de tentativas: {tentativas}')
