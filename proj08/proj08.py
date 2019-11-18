# =============================================================================
# Computer Project 08
# 
# This project is designed to generate all possible approved words from a given
# string and optional list of strings for a game of scrabble.   
# Calls for a a file, the rack and the letters on the board.
# displays top 5 words based on score and length in descending alphabetical order.
# then asks for another example.
#
# =============================================================================

import itertools
from operator import itemgetter
SCORE_DICT = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def open_file():
    """
    This function takes in no parameters and returns a valid file
    """
    valid = False
    while valid == False:
        file = input("Input word file: ")
        try:
            fp = open(file, 'r')
            valid = True
        except FileNotFoundError:
            print("File not found. Try again.")
            valid = False
    return fp

def read_file(fp):
    """
    This function takes in a file and gathers all the words in the file and puts 
    them into a dictionary and returns the dictionary. Will not add words smaller
    than 3 characters or if they have a hyphen of an apostrophe.
    """
    word_dict = {}
    for word in fp:
       word = word.strip()
       if len(word) < 3:
            pass
       elif '-' in word:
            pass
       elif "'" in word:
            pass
       else:
            word.lower()
            word_dict[word] = 1
    return word_dict

def calculate_score(rack, word):
    """
    This function takes in a rack of characters and a word. It then generates the
    score of the word string and returns the score.
    """
    score = 0
    for letter in word:
        score += SCORE_DICT[letter]    #Looks up letter in dict and adds value to score
    if len(rack) == 7:    #if the rack is a length of 7
        if len(word) >= 7:    #if the word is as long as or longer than the rack
            score += 50    #add 50 points if every letter in rack is used
    return score

def generate_combinations(rack, placed_tile):
    """
    This function takes in the rack and a tile that is placed and generates a
    list of all possible words using that set of characters. Returns 
    """
    all_letters = rack + placed_tile
    set_of_combos = set()    #creates set of the combos
    if placed_tile == '':    #if there is no tile placed
        for i in range(3, 9):    #changes the length of the word
            for combo in itertools.combinations(rack, i):    #finds combos for rack
                set_of_combos.add(combo)
    else:
        for i in range(3, 9):
            for combo in itertools.combinations(all_letters, i):
                if placed_tile in combo:    #only add the combo to the set if it includes the placed tile
                    set_of_combos.add(combo)
    return set_of_combos

def generate_words(combo, scrabble_words_dict):    
    """
    This function takes in a combo and the word dictionary. It then generates 
    words from each combibnation and adds each to a set if it is a valid word.
    """
    set_of_words = set()
    for word in itertools.permutations(combo):
        word = ''.join(word)    #joins the characters in the combo
        if word in scrabble_words_dict:
            set_of_words.add(word)    #adds if it is valid word
    return set_of_words

def generate_words_with_scores(rack, placed_tile, scrabble_words_dict):
    """
    This function takes in a rack, a placed tile, and the word dictionary. It 
    generates a set of combinations and then looks through each combo and generates
    a set of words based off the combo. Then takes each word and finds the score
    of the word. Then adds the word:score to a dictionary and returns a dictionary.
    """
    score = 0
    word_dict = {}
    set_of_combos = generate_combinations(rack, placed_tile)
    for combo in set_of_combos:
        set_of_words = generate_words(combo, scrabble_words_dict)    #generates words
        for word in set_of_words:
            score = calculate_score(rack, word)    #calculates the score for every word
            word_dict[word] = score    #adds word:value to dictionary
    return word_dict
            
def sort_words(word_dic):
    """
    This function takes in the word dictionary holding the scores and their values
    and returns a tuple containing two lists. The first list is sorted by score,
    length, and alphabetical. The second will be sorted by length, score, and alphabetical.
    Ths lists are sorted in descending alphabetical order.
    """
    sorted_by_score = []
    sorted_by_length = []
    for word, score in word_dic.items():
        tup = (word, score, len(word))
        sorted_by_score.append(tup)    #adds tup to each list.
        sorted_by_length.append(tup)
        
    sorted_by_score.sort(key=itemgetter(0))    #sort in alphabetical order
    sorted_by_length.sort(key=itemgetter(0))
    
    sorted_by_score.sort(key=itemgetter(1,2), reverse = True)    #sort by score then length of word
    sorted_by_length.sort(key=itemgetter(2,1), reverse = True)    #sort by length of word then score
    
    tup = (sorted_by_score, sorted_by_length)
    return tup
        

def display_words(word_list, specifier):
    """
    This function takes in a word list and a specifier and displays the top 5 
    elements of the list. the specifier is either score or length and will display 
    correct list.
    """
    top_5 = word_list[:5]    #top 5 elements in the word list
    if specifier.lower() == 'score':
        print('Word choices sorted by Score')
        print(("{:>6s} - {:s}".format('Score','Word')))
        for tup in top_5:
            word = tup[0]
            score = tup[1]
            print("{:>6d} - {:s}".format(score, word))
            
    elif specifier.lower() == 'length':
        print('\nWord choices sorted by Length')
        print(("{:>6s} - {:s}".format('Length','Word')))
        for tup in top_5:
            word = tup[0]
            length = tup[2]
            print("{:>6d} - {:s}".format(length, word))

def main():
    """
    This function is the starting point of the program. It prompts the user for
    a an example, file, rack, and placed tiles. Then displays the top 5 words for
    scoring and then by length. 
    """
    print("Scrabble Tool")
    choice = input("Would you like to enter an example (y/n): ").lower()
    while choice != 'n':
        fp = open_file()               #opens and read master word file
        file_word_dict = read_file(fp)
        
        rack_valid = False
        while rack_valid == False:
            rack = input("Input the rack (2-7chars): ")
            if 2 <= len(rack) <= 7:    #checks if rack is between 2-7 characters
                rack_valid = True
            else:
                print("Error: only characters and 2-7 of them. Try again.")
                rack_valid = False
                
        tiles_valid = False
        while tiles_valid == False:
            tiles = input("Input tiles on board (enter for none): ") 
            if tiles == '':    #if there is no tile placed
                tiles_valid = True
            elif tiles.isalpha() == True:    #if the tile is a character
                tiles_valid = True
            else:
                print("Error: tiles must be characters or empty")
                tiles_valid = False
                
        master_dict ={}
        if len(tiles) > 0:    #if there are tiles placed
            for tile in tiles:    #adds each combo of tiles placed into the dictionary
                master_dict.update(generate_words_with_scores(rack, tile, file_word_dict))    
            sorted_by_score, sorted_by_length = sort_words(master_dict)
            display_words(sorted_by_score, 'score')
            display_words(sorted_by_length, 'length')
        else:    #if no tiles are placed
            master_dict.update(generate_words_with_scores(rack, tiles, file_word_dict))
            sorted_by_score, sorted_by_length = sort_words(master_dict)
            display_words(sorted_by_score, 'score')
            display_words(sorted_by_length, 'length')
        choice = input("Do you want to enter another example (y/n): ").lower()    #reprompts user
        
    print('Thank you for playing the game')    #displays closing message


if __name__ == "__main__":
    main()
    