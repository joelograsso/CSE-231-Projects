"""
    SOURCE HEADER GOES HERE!
"""
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
        first takes random integer and adds move at that index of
        move list to pokemon's move list
        next, while loop that ends when four moves are added is run, 
        takes new random move from list like above and compares the 
        move type to the pokemon type, if they are the same then added to
        pokemon's move list
        if move is already in list, then not added to list
        each run through while loop, one count added to tries, 
        if tries reaches 200, then returns false
        if four moves are successsfully added, returns true
        
    '''

    rand_num = randint(0,len(moves_list)-1)
    pokemon.add_move(moves_list[rand_num])
    
    move_count = 1
    tries = 0
    type1 = pokemon.get_element1()
    type2 = pokemon.get_element2()
    while move_count<4:
        if tries == 200:
            return False
        
        tries += 1
        new_rand_num = randint(0,len(moves_list)-1)
        move = moves_list[new_rand_num]
        if move in pokemon.get_moves():
            continue
        elif move.get_element() == type1 or move.get_element() == type2:
            pokemon.add_move(move)
            move_count += 1
        else:
            continue
            
    return True

def turn (player_num, player_pokemon, opponent_pokemon):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    print("Player {}'s turn".format(player_num))
    print(player_pokemon)
    print("Show options: 'show ele', 'show pow', 'show acc'")
    choice = input("Select an attack between 1 and 4 or show option or 'q': ")
    choice = choice.lower().strip()
    opp_num = 0
    if player_num == 1:
        opp_num = 2
    else:
        opp_num = 1
    while True:
        if choice == 'q':
            print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, opp_num))
            return False
            
        elif choice == 'show ele':
            player_pokemon.show_move_elements()
        elif choice == 'show pow':
            player_pokemon.show_move_power()
        elif choice == 'show acc':
            player_pokemon.show_move_accuracy()
        else:
            break
        print("Show options: 'show ele', 'show pow', 'show acc'")
        choice = input("Select an attack between 1 and 4 or show option or 'q': ")
        choice = choice.lower().strip()
    
    index = int(choice)-1
    move = player_pokemon.get_moves()[index]
    print("selected move: {}".format(move.get_name()))
    print("{} hp before:{}".format(opponent_pokemon.get_name(),opponent_pokemon.get_hp()))
    player_pokemon.attack(move,opponent_pokemon)
    print("{} hp after:{}".format(opponent_pokemon.get_name(),opponent_pokemon.get_hp()))
    
    if opponent_pokemon.get_hp() == 0:
         print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(opp_num, player_num))
         return False
    else:
         return True
         
def main():
    #move and pokemon csv files read and sorted into useable lists
    move_file = open("moves.csv")
    moves_list = read_file_moves(move_file)
    pokemon_file = open("pokemon.csv")
    pokemon_list = read_file_pokemon(pokemon_file)
    
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower() 
    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return

    else:
        while True:
            user1 = input("Player {}, choose a pokemon by name or index: ".format("1"))
            pokemon1 = choose_pokemon(user1,pokemon_list)
            print("pokemon{}:\n".format("1"))
            print(pokemon1)
            
            user1 = input("Player {}, choose a pokemon by name or index: ".format("2"))
            pokemon2 = choose_pokemon(user1,pokemon_list)
            print("pokemon{}:\n".format("2"))
            print(pokemon2)
            
            add_moves(pokemon1,moves_list)
            add_moves(pokemon2,moves_list)
            
            while True:
                turn1 = turn(1, pokemon1, pokemon2)
                if turn1 == False:
                    break
                else:
                    turn1 = turn(2, pokemon2, pokemon1)
                    
                    if turn1 == False:
                        break
                    else:
                        print("{} hp after: {}".format("Player 1",pokemon1.get_hp()))
                        print("{} hp after: {}".format("Player 2",pokemon2.get_hp()))
                        continue
            another_str = 'ynq'
            another = input("Battle over, would you like to have another? ").lower().strip()
            while True:
                if another not in another_str:
                    another = input( "Invalid option! Please enter a valid choice: ").lower().strip()
                else:
                    break
            
            if another != 'y':
                print("Well that's a shame, goodbye")
                break
            else:
                continue
    
if __name__ == "__main__":
    main()
    
"Would you like to have a pokemon battle? "
"Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: "
"Player {}, choose a pokemon by name or index: "
"pokemon{}:\n"
"Insufficient moves; choose a different pokemon."
"Invalid option, choose a pokemon by name or index: "
"Select an attack between {} and {}: "
"Invalid input"
"Battle over, would you like to have another? "
"Invalid option! Please enter a valid choice: "
"{} {} {} {} {} {}\n"
"Number out of index range"
"selected move:"
"{} hp before:{}"
"{} hp after:{}"
"Player {}'s pokemon fainted, Player {} has won the pokemon battle!"
"Player {}'s turn"
"Player {} quits, Player {} has won the pokemon battle!"
"P{} hp after:"
"Show options: 'show ele', 'show pow', 'show acc'"
"Select an attack between 1 and {} or show option or 'q': "
"Well that's a shame, goodbye"