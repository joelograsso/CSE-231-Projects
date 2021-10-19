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
        makes each line (except first) into list and 
        creates objects using the name of the move, the element id, the power,
        accuracy, and attack type
        if generation isnt 1 or attack type is 1 or power/accuracy have no value, 
        then move isn't entered into list
        returns list of move objects
    '''
    move_list = []
    #file = open(fp, "r", encoding = "utf-8 ")
    next(fp, None)
    for i in fp.readlines():
        move_info = i.split(",")
        #print (move_info)
        if move_info[2] != '1' or move_info[9] == '1' or \
        move_info[4] == '' or move_info[6] == '':
            continue
        else:
            name = move_info[1]
            type_id = int(move_info[3])
            element = element_id_list[type_id]
            power = int(move_info[4])
            accuracy = int(move_info[6])
            attack_type = int(move_info[9])
            #print(name, element, power, accuracy, attack_type)
            move = Move(name, element, power, accuracy, attack_type)
            move_list.append(move)
        
    return move_list

def read_file_pokemon(fp):
    '''
        splits each line into list, 
        finds id of ecah pokemon
        if id number is new, adds to id list
        if generation 1 or id has already been used, 
        then moves to next line
        creates pokemon object with info from list and adds objects 
        to pokemon list
        returns list of pokemon objects
    '''
    pokemon_list = []
    id_list = []
    #file = open(fp, "r", encoding = "utf-8 ")
    next(fp, None)
    for i in fp.readlines():
        pokemon_info = i.split(",")
        id_num = pokemon_info[0]
        
        if pokemon_info[-2] != '1' or id_num in id_list :
            continue
        else:
            id_list.append(id_num)
            
            name = pokemon_info[1].lower()
            element1 = pokemon_info[2].lower()
            element2 = pokemon_info[3].lower()
            moves = None
            hp = int(pokemon_info[5])
            patt = int(pokemon_info[6])
            pdef = int(pokemon_info[7])
            satt = int(pokemon_info[8])
            sdef = int(pokemon_info[9])
            
            pokemon = Pokemon(name, element1, element2, moves, hp, patt, pdef, satt, sdef)
            pokemon_list.append(pokemon)
            
    return pokemon_list

def choose_pokemon(choice,pokemon_list):
    '''
        first tests to see if choice is integer or string
        if integer, finds pokemon at the index of the integr-1
        if string, finds pokemon with that name
        returns deep copy of that pokemon object
    '''
    
    try:
        choice = int(choice)
    except ValueError:
        choice = str(choice)
        
    if type(choice) == int:
        pokemon = deepcopy(pokemon_list[choice-1])
        return pokemon
    else:
        for i in pokemon_list:
            if choice.lower() == i.get_name().lower() :
                return deepcopy(i)

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