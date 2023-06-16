import os
import time
import random
import pandas as pd

#index_col="ATTACK" -> O Index da planilha vai ser a coluna ATTACK, possibilitando a comparacao por STRING e nao por um index INT
type_chart = pd.read_excel(os.path.join(os.path.dirname(__file__), "../Pokemon-Game/EffetivenessDataBase.xlsx"), index_col="ATTACK")

player = None
computer = None
isdead = False
menu = None
option = None

#Criando classe pai para futuramente criar os pokemons em si
class Pokemon:
    def __init__(self, name, type, level, hp, attacks):
        self.name = name
        self.type = type
        self.level = level
        self.hp = hp
        self.attacks = attacks

    def attack(self):
        pass

    def level_up(self):
        pass

#Criando func para calcular o dano a partir da planilha de dados de acordo com o tipo do ataque X tipo do pokemon, definindo a efetividade. Verificando se o Poke morreu
def calcdamage(movetype, poketype, dmg, poketarget):

    time.sleep(0.5)
    mod = type_chart.loc[movetype, poketype.type]

    if mod == 0:
        print("It doesn't affect...")
        dmg = dmg * mod
        print(f'Damage inflicted: {dmg}')
        poketarget.hp = poketarget.hp - dmg
        if poketarget.hp < 0:
            print(f'{poketarget.name} fainted!')
            isdead = True

    elif mod == 0.5:
        print("It's not very effective...")
        dmg = dmg * mod
        print(f'Damage inflicted: {dmg}')
        poketarget.hp = poketarget.hp - dmg
        if poketarget.hp < 0:
            print(f'{poketarget.name} fainted!')
            isdead = True

    elif mod == 1:
        print("It's normal damage.")
        dmg = dmg * mod
        print(f'Damage inflicted: {dmg}')
        poketarget.hp = poketarget.hp - dmg
        if poketarget.hp < 0:
            print(f'{poketarget.name} fainted!')
            isdead = True

    elif mod == 2:
        print("It's super effective!")
        dmg = dmg * mod
        print(f'Damage inflicted: {dmg}')
        poketarget.hp = poketarget.hp - dmg
        if poketarget.hp < 0:
            print(f'{poketarget.name} fainted!')
            isdead = True

    else:
        print("It's not very effective")
        print(f'Damage inflicted: {dmg}')
        poketarget.hp = poketarget.hp - dmg
        if poketarget.hp < 0:
            print(f'{poketarget.name} fainted!')
            isdead = True

#Setando os ataques de cada Pokemon, Nome/Tipo/Dano
charmander_attacks = [['Scratch', 'Normal', 10], ['Burn', 'Fire', 15], ['Fire Fang', 'Fire', 20],
                      ['Flamethrower', 'Fire', 30]]
squirtle_attacks = [['Scratch', 'Normal', 10], ['Water Gun', 'Water', 15], ['Water Pulse', 'Water', 20],
                    ['Hydro Pump', 'Water', 30]]
bulbasaur_attacks = [['Scratch', 'Normal', 10], ['Vine Whip', 'Grass', 15], ['Razor Leaf', 'Grass', 20],
                     ['Solar Beam', 'Grass', 30]]
mew_attacks = [['Scratch', 'Normal', 10], ['Ancient Power', 'Rock', 70], ['Aura Sphere', 'Fighting', 80],
                     ['Psychic', 'Psychic', 90]]

#Principal func que sera o jogo propriamente dito
def fight(player_pk, comp_pk, death=False):
    i = None
    move_chosen = None

    print(f'Player: {player_pk.name} go!')
    time.sleep(0.5)
    print(f'Computer: {comp_pk.name} go!\n')
    time.sleep(0.5)
    while (player_pk.hp > 0 and comp_pk.hp > 0) and isdead == False:
        time.sleep(2.5)
        print('----------YOUR TURN----------') #Vez do jogador
        while move_chosen != '1' or move_chosen != '2' or move_chosen != '3' or move_chosen != '4':
            print('\nChoose your movement:')
            length = len(player_pk.attacks)
            for i in range(length):
                print(f'{i + 1} - {player_pk.attacks[i][0]} | Damage: {player_pk.attacks[i][2]}')

            move_chosen = input()

            if move_chosen == '1':
                move_chosen = int(move_chosen) - 1
                print(f'You chose {player_pk.attacks[move_chosen][0]}!')
                calcdamage(player_pk.attacks[move_chosen][1], comp_pk, player_pk.attacks[move_chosen][2], comp_pk)
                print(f'PLAYER {player_pk.name} HP: {player_pk.hp}')
                print(f'COMPUTER {comp_pk.name} HP: {comp_pk.hp}')
                i = None
                move_chosen = None
                break

            elif move_chosen == '2':
                move_chosen = int(move_chosen) - 1
                print(f'You chose {player_pk.attacks[move_chosen][0]}!')
                calcdamage(player_pk.attacks[move_chosen][1], comp_pk, player_pk.attacks[move_chosen][2], comp_pk)
                print(f'PLAYER {player_pk.name} HP: {player_pk.hp}')
                print(f'COMPUTER {comp_pk.name} HP: {comp_pk.hp}')
                i = None
                move_chosen = None
                break

            elif move_chosen == '3':
                move_chosen = int(move_chosen) - 1
                print(f'You chose {player_pk.attacks[move_chosen][0]}!')
                calcdamage(player_pk.attacks[move_chosen][1], comp_pk, player_pk.attacks[move_chosen][2], comp_pk)
                print(f'PLAYER {player_pk.name} HP: {player_pk.hp}')
                print(f'COMPUTER {comp_pk.name} HP: {comp_pk.hp}')
                i = None
                move_chosen = None
                break

            elif move_chosen == '4':
                move_chosen = int(move_chosen) - 1
                print(f'You chose {player_pk.attacks[move_chosen][0]}!')
                calcdamage(player_pk.attacks[move_chosen][1], comp_pk, player_pk.attacks[move_chosen][2], comp_pk)
                print(f'PLAYER {player_pk.name} HP: {player_pk.hp}')
                print(f'COMPUTER {comp_pk.name} HP: {comp_pk.hp}')
                i = None
                move_chosen = None
                break

            else:
                print("Invalid Movement...")
                i = None
                move_chosen = None
                time.sleep(0.5)

        if (player_pk.hp > 0 and comp_pk.hp > 0) and isdead == False:
            time.sleep(2.5)
            print('\n----------ENEMY TURN----------\n') #Vez do computador
            computer_attack = random.choice([0, 1, 2, 3])

            if computer_attack == 0:
                print(f'Computer chose {comp_pk.attacks[computer_attack][0]}!')
                calcdamage(comp_pk.attacks[computer_attack][1], player_pk, comp_pk.attacks[computer_attack][2],
                           player_pk)
                print(f'PLAYER {player_pk.name} HP: {player_pk.hp}')
                print(f'COMPUTER {comp_pk.name} HP: {comp_pk.hp}\n')

            elif computer_attack == 1:
                print(f'Computer chose {comp_pk.attacks[computer_attack][0]}!')
                calcdamage(comp_pk.attacks[computer_attack][1], player_pk, comp_pk.attacks[computer_attack][2],
                           player_pk)
                print(f'PLAYER {player_pk.name} HP: {player_pk.hp}')
                print(f'COMPUTER {comp_pk.name} HP: {comp_pk.hp}\n')

            elif computer_attack == 2:
                print(f'Computer chose {comp_pk.attacks[computer_attack][0]}!')
                calcdamage(comp_pk.attacks[computer_attack][1], player_pk, comp_pk.attacks[computer_attack][2],
                           player_pk)
                print(f'PLAYER {player_pk.name} HP: {player_pk.hp}')
                print(f'COMPUTER {comp_pk.name} HP: {comp_pk.hp}\n')

            elif computer_attack == 3:
                print(f'Computer chose {comp_pk.attacks[computer_attack][0]}!')
                calcdamage(comp_pk.attacks[computer_attack][1], player_pk, comp_pk.attacks[computer_attack][2],
                           player_pk)
                print(f'PLAYER {player_pk.name} HP: {player_pk.hp}')
                print(f'COMPUTER {comp_pk.name} HP: {comp_pk.hp}\n')

        else:
            print('\n- - - END GAME - - -')
            time.sleep(0.5)
            break


while menu != '0':
    print('- - - - - MENU- - - - -'
          '\n1 - Choose a Pokemon'
          '\n0 - EXIT GAME\n')
    menu = input()
    if menu == '1':
        time.sleep(0.5)
        while player != '1' or player != '2' or player != '3':
            player = input(f"Choose your Pokemon:\n 1 - Charmander\n 2 - Squirtle\n 3 - Bulbasaur\n")
             #Criando Pokemon a partir da classe pai para o jogador
            if player == '1':
                player = Pokemon('Charmander', 'Fire', 1, 100, charmander_attacks)
                break
            elif player == '2':
                player = Pokemon('Squirtle', 'Water', 1, 100, squirtle_attacks)
                break
            elif player == '3':
                player = Pokemon('Bulbasaur', 'Grass', 1, 100, bulbasaur_attacks)
                break
            elif player == '151':
                print('Oh! You found something diferent!!')
                player = Pokemon('Mew', 'Psychic', 99, 300, mew_attacks)
                break
            else:
                print("Choose again...")
                time.sleep(0.5)

        computer = random.choice([1, 2, 3])
         #Criando Pokemon a partir da classe pai para o jogador
        if computer == 1:
            computer = Pokemon('Charmander', 'Fire', 1, 100, charmander_attacks)
        elif computer == 2:
            computer = Pokemon('Squirtle', 'Water', 1, 100, squirtle_attacks)
        elif computer == 3:
            computer = Pokemon('Bulbasaur', 'Grass', 1, 100, bulbasaur_attacks)
        menu = None

        while option != '0':
            print('- - - - - BATTLE OPTIONS - - - - -'
                '\n1 - Start Battle!'
                '\n0 - QUIT\n')
            option = input()
            if option == '1':
                if player.hp <= 0 or computer.hp <= 0:
                    break
                else:
                    print('Starting Battle!')
                    time.sleep(0.5)
                    fight(player, computer)
                    option = None
            elif option == '0':
                option = None
                break
            else:
                print('Invalid option...\n')
    elif menu == '0':
        menu = None
        break
    else:
        print('Invalid option...\n')
