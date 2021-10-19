# =============================================================================
#  Computer project 11
#     Pokemon
#  Prompts user to battle
#    select pokemon for user 1
#    select pokemon for user 2
#        Battle until someone is defeated or someone quits
# =============================================================================
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''
    This function takes in a file pointer for a moves csv file and returns a list
    of all the valid moves.
    '''
    Move_list = []
    reader = csv.reader(fp)
    next(reader)
    for line in reader:
        generation_id = int(line[2])    #generation ID
        name = line[1]    #name of move
        type_id = int(line[3])    #used to get element
        power = line[4]    #power of move
        accuracy = line[6]    #accuracy of move
        attack_type = line[9]     #attack type of a move
        if generation_id == 1:
            if 0<= type_id <= len(element_id_list):
                element = element_id_list[type_id]
                if attack_type != '1':
                    if power != '':
                        if accuracy != '':
                            move = Move(name, element, int(power), int(accuracy), int(attack_type))
                            Move_list.append(move)
        else:
            continue
    return Move_list




def read_file_pokemon(fp):
    '''
    This function takes in a file pointer for a pokemon csv file and returns a 
    list of all the pokemon.
    '''
    pokemon_list = []
    ID_count = {}
    reader = csv.reader(fp)
    next(reader)
    for line in reader:
        ID = line[0]
        name = line[1].lower()     #gathering all the required info for the Move class
        element1 = line[2].lower()
        element2 = line[3].lower()
        HP = int(line[5])
        patt = int(line[6])
        pdef = int(line[7])
        satt = int(line[8])
        sdef = int(line[9])
        generation = line[11]
        if generation == '1':
            if ID not in ID_count:    #makes sure ID has not been seen already 
                ID_count[ID] = 1
                pokemon = Pokemon(name, element1, element2, None, HP, patt, pdef, satt, sdef)
                pokemon_list.append(pokemon)
    return pokemon_list

def choose_pokemon(choice,pokemon_lists):
    '''
    This function selects the pokemon that the user chooses or returns None if 
    they enter an index out of the range or an invalid name.
    '''

    if choice.isdigit() == True:
        if 1 <= int(choice) <= len(pokemon_lists):    #valid index
            Pokemon = deepcopy(pokemon_lists[int(choice) - 1])
            return Pokemon
        else:
            return None
    else:
        for pokemon in pokemon_lists:
            if choice.lower() == pokemon.get_name():          
                Pokemon = deepcopy(pokemon)
                return Pokemon
        return None
                
def add_moves(pokemon,moves_list):
    '''
    This function adds random moves to a pokemon from the move list if they match
    the pokemon's elements.
    '''
    
    index = randint(0, len(moves_list)-1)    #randomly assign index
    move = moves_list[index]
    pokemon.add_move(move)    #assigns random move
    move_count =  1
    i = 0
    while i < 200:    #trys the first 200 options
        index = randint(0, len(moves_list)-1)
        move = moves_list[index]
        if move.get_element() == pokemon.get_element1() or move.get_element() == pokemon.get_element2():
            if move not in pokemon.get_moves():
                if move_count != 4:
                    move_count += 1
                    pokemon.add_move(move)
                    i += 1
                else:
                    return True    #if 4 moves are available
                    break
        i +=1
    return False    #cant get 4 moves
        


def turn (player_num, player_pokemon, opponent_pokemon):
    '''
    This functions does the turns for each player. 
    '''
    print("Player {}'s turn".format(player_num))    #prints players turn
    print(player_pokemon)
    print("Show options: 'show ele', 'show pow', 'show acc'")    #shows options
    choice = input("Select an attack between 1 and {} or show option or 'q': ".format(opponent_pokemon.get_number_moves())).lower()
    while choice != 'q':
        if choice == 'show ele':
            player_pokemon.show_move_elements()    #displays elements of moves
            print("Show options: 'show ele', 'show pow', 'show acc'")
            choice = input("Select an attack between 1 and {} or show option or 'q': ".format(opponent_pokemon.get_number_moves())).lower()
        elif choice == 'show pow':
            player_pokemon.show_move_power()    #displays power of moves
            print("Show options: 'show ele', 'show pow', 'show acc'")
            choice = input("Select an attack between 1 and {} or show option or 'q': ".format(opponent_pokemon.get_number_moves())).lower()
        elif choice == 'show acc':
            player_pokemon.show_move_accuracy()    #displays accuracy of moves
            print("Show options: 'show ele', 'show pow', 'show acc'")
            choice = input("Select an attack between 1 and {} or show option or 'q': ".format(opponent_pokemon.get_number_moves())).lower()
        elif choice.isdigit() == True:
            if 1 <= int(choice) <= 4:
                moves = player_pokemon.get_moves()
                move = moves[int(choice)-1]
                print("selected move: {}".format(move))
                print("\n{} hp before:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
                player_pokemon.attack(move, opponent_pokemon)
                print("{} hp after:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
                if opponent_pokemon.get_hp() <= 0:
                    if player_num == '1':
                        print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format('2','1'))
                        return False
                    else:
                        print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format('1','2'))
                        return False
                else:
                    return True
    if choice == 'q':
        if player_num == '1':
            print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, '2'))
            return False
        else:
            print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, '1'))
            return False
    
    
    
    
    
    
def main():
    p1 = '1'
    p2= '2'
    moves_fp = open("moves.csv", 'r')
    pokemon_fp = open('pokemon.csv', 'r')
    pokemon_list = read_file_pokemon(pokemon_fp)
    moves_list = read_file_moves(moves_fp)
#    print(pokemon_list)
    usr_inp = input("Would you like to have a pokemon battle?").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input(" Invalid option! Please enter a valid choice: Y/y, N/n or Q/q:").lower()
#        
    if usr_inp != 'y':
        print(" Well that's a shame, goodbye")
        return
    else:
        while usr_inp != 'q' and usr_inp != 'n':
            valid1 = False
            valid2 = False
            while valid1 == False:    #makes sure user inputs a valid 
                choice1= input(" Player {}, choose a pokemon by name or index: ".format(p1))
                if choice1 != None:
                    pokemon1 = choose_pokemon(choice1, pokemon_list)
                    if add_moves(pokemon1, moves_list) == True:
                        print("pokemon{}:\n".format(p1))
                        print('{:<15s}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n'.format(pokemon1.get_name(), \
                     pokemon1.get_hp(), pokemon1.get_patt(), pokemon1.get_pdef(), pokemon1.get_satt(), pokemon1.get_sdef()))
                        print('{:<15s}{:<15s}\n'.format(pokemon1.get_element1(), pokemon1.get_element2()))
                        valid1 = True
                    else:
                        print("Insufficient moves; choose a different pokemon.")
                        valid1 = False
                else:
                    choice1 = input("Invalid option, choose a pokemon by name or index: ")
                    valid1 = False
    
            while valid2 == False:
                choice2= input("Player {}, choose a pokemon by name or index: ".format(p2))
                if choice2 != None:
                    pokemon2 = choose_pokemon(choice2, pokemon_list)
                    if add_moves(pokemon2, moves_list) == True:
                        print("pokemon{}:\n".format(p2))
                        print('{:<15s}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n'.format(pokemon2.get_name(), \
                     pokemon2.get_hp(), pokemon2.get_patt(), pokemon2.get_pdef(), pokemon2.get_satt(), pokemon2.get_sdef()))
                        print('{:<15s}{:<15s}\n'.format(pokemon2.get_element1(), pokemon2.get_element2()))
                        valid2 = True
                    else:
                        print("Insufficient moves; choose a different pokemon.")
                        valid2 = False
                else:
                    choice2 = input("Invalid option, choose a pokemon by name or index: ")
                    valid2 = False
                    
            player1 = True
            player2 = False   
            no_win = True
            while no_win == True:
                if player1 == True:    #player 1 turn
                    player2 = True
                    player1 = False
                    no_win = turn(p1,pokemon1,pokemon2)
                elif player2 == True:    #player 2 turn
                    player1 = True
                    player2 = False
                    no_win = turn(p2, pokemon2, pokemon1)
            usr_inp = input("Battle over, would you like to have another? ").lower()
            if usr_inp != 'y':
                print(" Well that's a shame, goodbye")
                return
    
if __name__ == "__main__":
    main()
