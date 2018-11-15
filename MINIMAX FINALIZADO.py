#!/usr/bin/env python3
from math import inf as infinity
import platform
import time
from os import system

"""
Esse programa e o jogo da velha com minimax, utilizando Python.

"""
contador = 0
pessoa = -1
maquina = +1
tabuleiro = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(estado):
    """
    Funcao heuristica para avaliar o estado.
    :parametro estado: estado atual do tabuleiro
    :return: volta 1 se a maquina vence e -1 se o jogador vence; 0 em caso de empate
    
    """
    if vence(estado, maquina):
        pontuacao = +1
    elif vence(estado, pessoa):
        pontuacao = -1
    else:
        pontuacao = 0
       
    return pontuacao


def vence(estado, jogador):
    """
    Essa funcao testa se um jogador especifico ganhou. Possibilidades:
    * Tres linhas    [X X X] ou [O O O]
    * Tres colunas   [X X X] ou [O O O]
    * Duas diagonais [X X X] ou [O O O]
    :param estado: estado atual do tabuleiro
    :param jogador: pessoa ou maquinautador
    :return: verdadeiro se jogador ganha
    
   
    """
    vence_estado = [
        [estado[0][0], estado[0][1], estado[0][2]],
        [estado[1][0], estado[1][1], estado[1][2]],
        [estado[2][0], estado[2][1], estado[2][2]],
        [estado[0][0], estado[1][0], estado[2][0]],
        [estado[0][1], estado[1][1], estado[2][1]],
        [estado[0][2], estado[1][2], estado[2][2]],
        [estado[0][0], estado[1][1], estado[2][2]],
        [estado[2][0], estado[1][1], estado[0][2]],
    ]
    if [jogador, jogador, jogador] in vence_estado:
        return True
    else:
        return False


def game_over(estado):
    """
     Essa funcao testa se a pessoa ou maquina ganharam
    :param estado: estado do tabuleiro
    :return: verdadeiro se pessoa ou maquinha ganham

   
    """
    return vence(estado, pessoa) or vence(estado, maquina)


def espacos_vazios(estado):
    """
    Cada espaco vazio vai ser adicionado na lista de espacos
    :param estado: estado atual do tabuleiro
    :return: lista de espacos vazios
         """
    espacos = []

    for x, row in enumerate(estado):
        for y, espaco in enumerate(row):
            if espaco == 0: espacos.append([x, y])
    return espacos


def movimento_valido(x, y):
    """
     Um movimento e valido se o espaco escolhido estiver vazio
    :param x: coordenada x
    :param y: coordenada y
    :return:verdadeiro se o espaco[x][y] estiver vazio
    
  
    """
    if [x, y] in espacos_vazios(tabuleiro):
        return True
    else:
        return False


def faz_jogada(x, y, jogador):
    """
    Faz a jogada, se as coordenadas forem validas
    :param x: coordenada x
    :param y: coordenada y
    :param jogador: jogador atual

    
    """
    if movimento_valido(x, y):
        tabuleiro[x][y] = jogador
        return True
    else:
        return False


def minimax(estado, profundidade, jogador):
    """
     Funcao da IA que escolhe melhor movimento
    :param estado: estado atual do tabuleiro
    :param profundidade: indice de nos na arvore (0 <= profundidade <= 9),
    nunca 9 nesse caso (ver funcao iaturn())
    :param jogador: a pessoa ou maquina
    :return: lista com [melhor linha, melhor coluna, melhor pontuacao]
    
    
    """
    global contador
    if jogador == maquina:
        melhor = [-1, -1, -infinity]
    else:
        melhor = [-1, -1, +infinity]

    if profundidade == 0 or game_over(estado):
        pontuacao = evaluate(estado)
        
        return [-1, -1, pontuacao]
    for espaco in espacos_vazios(estado):
        contador = contador + 1
        x, y = espaco[0], espaco[1]
        estado[x][y] = jogador
        pontuacao = minimax(estado, profundidade - 1, -jogador)
        estado[x][y] = 0
        pontuacao[0], pontuacao[1] = x, y

        if jogador == maquina:
            if pontuacao[2] > melhor[2]:
                melhor = pontuacao  # malor de maximo
        else:
            if pontuacao[2] < melhor[2]:
                melhor = pontuacao  # valor me minimo   
    return melhor


def clean():
    """
    Limpa o console
    """
    system('clear')


def render(estado, m_escolha, p_escolha):
    """
     Imprime o tabuleiro no console
    :param estado: estado atual do tabuleiro
    
       """
    print('----------------')
    for row in estado:
        print('\n----------------')
        for espaco in row:
            if espaco == +1:
                print('|', m_escolha, '|', end='')
            elif espaco == -1:
                print('|', p_escolha, '|', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n----------------')


def rodada_maquina(m_escolha, p_escolha):
    """
     Chama a funcao minimax se profundidade <9, caso contrario escolhe uma coordenada aleatoria
    :param m_escolha: escolha da maquina X ou O
    :param p_escolha: escolha da pessoa X ou O
    :return:
    """
    profundidade = len(espacos_vazios(tabuleiro))
    if profundidade == 0 or game_over(tabuleiro):
        return

#    clean()
    print('Rodada da maquina')
    render(tabuleiro, m_escolha, p_escolha)
    movimento = minimax(tabuleiro, profundidade, maquina)
    x, y = movimento[0], movimento[1]
    faz_jogada(x, y, maquina)
    print('NÓS ESPANDIDOS', contador)
    time.sleep(1)


def rodada_pessoa(m_escolha, p_escolha):
    """
    A pessoa faz um movimento valido
    :param m_escolha: escolha da maquina X ou O
    :param p_escolha: escolha da pessoa X ou O
    
    """
    global contador
    contador =0
    profundidade = len(espacos_vazios(tabuleiro))
    if profundidade == 0 or game_over(tabuleiro):
        return

    # dicionario de movimentos validos
    movimento = -1
    movimentos = {
        1: [2, 0], 2: [2, 1], 3: [2, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [0, 0], 8: [0, 1], 9: [0, 2],
    }

#    clean()
    print('Rodada da pessoa')
    render(tabuleiro, m_escolha, p_escolha)

    while (movimento < 1 or movimento > 9):
        try:
            movimento = int(input('Use o numpad (1..9): '))
            coord = movimentos[movimento]
            try_movimento = faz_jogada(coord[0], coord[1], pessoa)

            if try_movimento == False:
                print('Ja preenchido')
                movimento = -1
        except KeyboardInterrupt:
            print('FALOU')
            exit()
        except:
            print('Invalido')


def main():
    """
  Main que chama todas as funcoes   
    """

    p_escolha = '' # X ou O
    m_escolha = '' # X ou O
    first = ''  # se a pessoa vai primeiro

    # pessoa escolhe X ou O 
    while p_escolha != 'O' and p_escolha != 'X':
        try:
            print('')
            p_escolha = input('Escolha X ou O\nEscolhido: ').upper()
        except KeyboardInterrupt:
            print('FALOU')
            exit()
        except:
            print('Invalido')

    # Definindo escolha da maquina
    if p_escolha == 'X':
        m_escolha = 'O'
    else:
        m_escolha = 'X'

    # Define jogador que comeca

    while first != 'Y' and first != 'N':
        try:
            first = input('Primeiro a comecar?[y/n]: ').upper()
        except KeyboardInterrupt:
            print('FALOU')
            exit()
        except:
            print('Invalido')

    # Loop principal
    while len(espacos_vazios(tabuleiro)) > 0 and not game_over(tabuleiro):
        if first == 'N':
            rodada_maquina(m_escolha, p_escolha)
            first = ''

        rodada_pessoa(m_escolha, p_escolha)
        rodada_maquina(m_escolha, p_escolha)
       
    # Mensagem de fim de jogo
    if vence(tabuleiro, pessoa):

        print('Rodada da pessoa')
        render(tabuleiro, m_escolha, p_escolha)
        print('GANHOU!')
    elif vence(tabuleiro, maquina):

        print('Rodada da maquina')
        render(tabuleiro, m_escolha, p_escolha)
        print('PERDEU!')
    else:

        render(tabuleiro, m_escolha, p_escolha)
        print('EMPATE!')

#    exit()
    
main()