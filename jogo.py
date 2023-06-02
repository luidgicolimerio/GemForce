# Jogadores 2 - 4
# Dicionário de Deck do jogador
# Carta - dicionário
import cards
import os
player_1 = False
player_2 = False
player_3 = False
player_4 = False
i = 0

def jogar_carta(deck):
    global i
    for carta in deck:
        print('Cartas do Deck:')
        print()
        print(f'Carta {i}: ')
        print(carta.get('tipo'))
        if list(carta.keys())[1] == "gera":
            print("2x")

        if carta.get('geraGY') != None:
                    print("Gemas Amarelas: ",carta.get('geraGY'))
        if carta.get('geraGG') != None:
                    print("Gemas Verdes: ",carta.get('geraGG'))
        if carta.get('geraGB') != None:
                    print("Gemas Azuis: ",carta.get('geraGB'))
        if carta.get('geraGP') != None:
                    print("Gemas Rosas: ",carta.get('geraGP'))
        i += 1
def comprar_carta(pontos, caravana):
    while True:
        escolha = input('Você deseja comprar um golem[1]\n ou comprar um mineiro[2]: ')
        try:
            escolha = int(escolha)
        except ValueError:
             print('Você não digitou um número')
             continue
        if escolha != 1 and 2:
            print('Selecione uma opção válida!')
        else:
             break
    if escolha == 1:
        print('Golems disponíveis para compra: ')
        for i in range(5):
            print(cards.cartas_de_golem[i].get('nome'),"|", end=" ")
            for nome, custo in cards.cartas_de_golem[i].items():
                if nome != 'nome':
                    print(nome," :", custo, end=" ")
                print()
            print()
        while True:    
            jogada = input('Escolha um golem para comprar: ')
            try:
                jogada = int(jogada)
                carta = cards.cartas_de_golem[jogada]
                if caravana.get('GY') >= carta.get('custoGY'):
                    novo_valor_gemas =  caravana.get('GY') - carta.get('custoGY')
                    caravana.update({'GY' : novo_valor_gemas,})
                else:
                    print('Você não pode comprar esse golem')
                    return False

                if caravana.get('GG') >= carta.get('custoGG'):
                    novo_valor_gemas =  caravana.get('GG') - carta.get('custoGG')
                    caravana.update({'GG' : novo_valor_gemas,})
                else:
                    print('Você não pode comprar esse golem')
                    return False

                if caravana.get('GB') >= carta.get('custoGB'):
                    novo_valor_gemas =  caravana.get('GB') - carta.get('custoGB')
                    caravana.update({'GG' : novo_valor_gemas,})
                else:
                    print('Você não pode comprar esse golem')
                    return False

                if caravana.get('GP') >= carta.get('custoGP'):
                    novo_valor_gemas =  caravana.get('GP') - carta.get('custoGP')
                    caravana.update({'GP' : novo_valor_gemas,})
                else:
                    print('Você não pode comprar esse golem')
                    return False
                cards.cartas_de_golem.pop(jogada)
                pontos += carta.get('pontos')
                print()
                print(f'Você está com {pontos} pontos!') 
                return "golem"
            
            except ValueError:
                 print('Digite um número')
                 continue
            except IndexError:
                print('Você não escolheu uma carta válida')
                continue
        
    elif escolha == 2:
        print('Mineiros disponíveis para compra: ')
        for i in range(5):
            print(cards.cartas_de_golem[i].get('nome'),"|", end=" ") # Trocar lista de golems por lista de mineiros
            for nome, custo in cards.cartas_de_golem[i].items():     # Criar carta de mineradores
                if nome != 'nome':
                    print(nome," :", custo, end=" ")
            print()
             
         
quantidade_de_players = input('Quantos jogadores irão jogar: ')
try: 
    quantidade_de_players = int(quantidade_de_players)
    if quantidade_de_players == 2:
        player_1 = True
        player_2 = True
    elif quantidade_de_players == 3:
        player_1 = True
        player_2 = True
        player_3 = True
    elif quantidade_de_players == 4:
        player_1 = True
        player_2 = True
        player_3 = True
        player_4 = True
    else:
        print('Digite [2], [3] ou [4]')
except:
    print('Digite apenas números')

if player_1 and player_2:
    deck_player_1 =[cards.carta_inicial_0, cards.carta_inicial_1]
    deck_player_2 = [cards.carta_inicial_0, cards.carta_inicial_1]
    pontos_player_1 = 0
    pontos_player_2 = 0
    deck_buildado_player_1 = deck_player_1.copy()
    deck_buildado_player_2 = deck_player_2.copy()
    caravana_player_1 = cards.caravana.copy()
    caravana_player_2 = cards.caravana.copy()

if  player_3:
    deck_player_3 = [cards.carta_inicial_0, cards.carta_inicial_1]
    deck_buildado_player_3 = deck_player_3.copy()
    pontos_player_3 = 0
    caravana_player_3 = cards.caravana.copy()



if  player_4:
    deck_player_4 = [cards.carta_inicial_0, cards.carta_inicial_1]
    deck_buildado_player_4 = deck_player_4.copy()
    pontos_player_4 = 0
    caravana_player_4 = cards.caravana.copy()

while True:
    print("Turno do Player 1: ")

    while True:
        print('Escolha uma opção de jogada: ')
        print("Jogar uma carta [1]")
        print("Comprar carta ou golem [2]")
        print("Descansar [3]")
        acao = input("Digite a sua jogada: ")
        os.system('cls')
        i = 0
        try:
            acao = int(acao)
        except ValueError:
            print('Você não digitou um número')
            continue
        if acao == 1:
            if deck_player_1 == []:
                print('Você não tem cartas na sua mão, descanse ou compre uma carta')
                continue
            jogar_carta(deck_player_1)
            jogada = input('Escolha a carta que deseja jogar:')
            try:
                jogada = int(jogada)
                carta = deck_player_1[jogada]

                if carta.get('tipo') == 'Mineiro':
                    if carta.get('geraGY') != None:
                        caravana_player_1['GY'] += carta.get('geraGY')
                    if carta.get('geraGG') != None:
                        caravana_player_1['GG'] += carta.get('geraGG')
                    if carta.get('geraGB') != None:
                        caravana_player_1['GB'] += carta.get('geraGB')
                    if carta.get('geraGP') != None:
                        caravana_player_1['GP'] += carta.get('geraGP')

                deck_player_1.pop(jogada)
            except IndexError:
                print('Você não escolheu uma carta válida')
                continue
            except ValueError:
                print('Você não digitou um número')
                continue
        if acao == 2:
            comprou = comprar_carta(pontos_player_1, caravana_player_1)
            if comprou == "golem":
                break