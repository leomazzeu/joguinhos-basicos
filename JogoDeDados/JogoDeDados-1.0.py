from random import randint
from time import sleep

pJogador = 0
pComputador = 0

print('SEJA BEM VINDO AO JOGO DE DADOS')
nomeJogador = str(input('Digite seu apelido: '))
sleep(1)
decisao = str(input('Você deseja jogar o dado? (Sim/Não): ')).upper()
while (decisao != 'SIM' and decisao != 'NÃO' and decisao != 'NAO'):
    print('Digite um valor válido.')
    decisao = str(input('Você deseja jogar o dado? (Sim/Não): ')).upper()
while (decisao == 'SIM'):
    jogadaJogador = randint(1, 6)
    jogadaComputador = randint(1, 6)
    if (jogadaJogador > jogadaComputador):
        print(f'Seu dado caiu no número {jogadaJogador}')
        sleep(2)
        print(f'O dado do seu oponente deu o número {jogadaComputador}')
        sleep(2)
        print('Parabéns! Você venceu essa rodada.')
        sleep(2)
        pJogador = pJogador + 1
        decisao = str(input('Você deseja jogar o dado novamente? (Sim/Não): ')).upper()
    elif (jogadaJogador < jogadaComputador):
        print(f'Seu dado caiu no número {jogadaJogador}')
        sleep(2)
        print(f'O dado do seu oponente deu o número {jogadaComputador}')
        sleep(2)
        print(f'Que pena! Você perdeu essa rodada.')
        sleep(2)
        pComputador = pComputador + 1
        decisao = str(input('Você deseja jogar o dado novamente? (Sim/Não): ')).upper()
    else:
        print(f'A jogada de ambos deram o número {jogadaJogador}')
        sleep(2)
        print('Portanto, essa rodada foi considerada um empate.')
        sleep(2)
        decisao = str(input('Você deseja jogar o dado novamente? (Sim/Não): ')).upper()
    while (decisao != 'SIM' and decisao != 'NÃO' and decisao != 'NAO'):
            print('Digite um valor válido.')
            decisao = str(input('Você deseja jogar o dado? (Sim/Não): ')).upper()
print(f'PONTUAÇÃO: {nomeJogador}: {pJogador} | Computador: {pComputador}')
print('JOGO FINALIZADO!')