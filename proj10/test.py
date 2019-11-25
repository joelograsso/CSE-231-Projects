"""
    SOURCE HEADER GOES HERE!
"""


import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    
    '''
         It creates and initializes the stock, tableau, and foundation, and
         then returns them as a tuple, in that order
    '''
    stock = cards.Deck()
    stock.shuffle()
    tableau = [[stock.deal()],[stock.deal()],[stock.deal()],[stock.deal()]]
    foundation = []
    return (stock, tableau, foundation) 
                               
    
def deal_to_tableau( stock, tableau ):
        
    '''
        WRITE DOCSTRING HERE!!!
    '''
    if len(stock) > 0:
        tableau[0].append(stock.deal())
        tableau[1].append(stock.deal())
        tableau[2].append(stock.deal())
        tableau[3].append(stock.deal())
    


def display( stock, tableau, foundation ):
    '''Display the stock, tableau, and foundation.'''
    
    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    
    # determine the number of rows to be printed -- determined by the most
    #           cards in any tableau column
    max_rows = 0
    for col in tableau:
        if len(col) > max_rows:
            max_rows = len(col)

    for i in range(max_rows):
        # display stock (only in first row)
        if i == 0:
            display_char = "" if stock.is_empty() else "XX"
            print("{:<8s}".format(display_char),end='')
        else:
            print("{:<8s}".format(""),end='')

        # display tableau
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print("{:4s}".format( str(col[i]) ), end='' )

        # display foundation (only in first row)
        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')

        print()

def get_option():
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    choice = input("\nInput an option (DFTRHQ): ").upper()
    choice_list = list(choice.replace(' ',''))
    options = 'DFTRHQ'
    columns = '1234'
    while True:
        if choice_list[0] in options:
            if len(choice_list) == 1:
                if choice_list[0] == 'D':
                    return ['D']
                elif choice_list[0] == 'R':
                    return ['R']
                elif choice_list[0] == 'Q':
                    return ['Q']
                elif choice_list[0] == 'H':
                    return ['H']
                else:
                    return None
                
            elif len(choice_list) ==  2:
                if choice_list[0] == 'F':
                    if choice_list[1] in columns:
                        return ['F', int(choice_list[1])]
                else:
                    return None

            elif len(choice_list) == 3:
                if choice_list[0] == 'T':
                    if choice_list[1] in columns:
                        if choice_list[2] in columns:
                            return ['T', int(choice_list[1]),int(choice_list[2])]
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None

                
            
def validate_move_to_foundation( tableau, from_col ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    if 1<= int(from_col) <= 4:
        if len(tableau[int(from_col)-1]) != 0:
            card = tableau[int(from_col)-1][-1]
            if card.rank() == 1:
                return False
            for column in tableau:
                for final_card in column:
                    if len(column) != 0:
                        final_card = column[-1]
                        if final_card.suit() == card.suit():
                            if final_card.rank() == 1:
                                return True
                            elif final_card.rank() > card.rank():
                                    return True
                    else:
                        continue
            else:
                return False
        else:
            return False
    else:
        return False
                
                

    
def move_to_foundation( tableau, foundation, from_col ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    valid = validate_move_to_foundation(tableau, from_col)
    if valid == True:
        card = tableau[int(from_col) - 1].pop()
        foundation.append(card)
        

def validate_move_within_tableau( tableau, from_col, to_col ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    if 1 <= int(from_col) <= 4:
        if 1 <= int(to_col) <=4:
            if len(tableau[int(to_col) - 1]) == 0 and len(tableau[int(from_col) - 1]) != 0:
                return True
    return False



def move_within_tableau( tableau, from_col, to_col ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    valid = validate_move_within_tableau(tableau, from_col, to_col)
    if valid == True:
        card = tableau[int(from_col)-1].pop()
        tableau[int(to_col) - 1].append(card)

        
def check_for_win( stock, tableau ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    ace_count = 0
    if stock.is_empty() == True:
        for i in range(4):
            ace = tableau[i][0]
            if len(tableau[i]) == 1:
                if ace.rank() == 1:
                    ace_count += 1
    if ace_count == 4:
        return True
    else:
        return False
        
def main():
        
    '''
        WRITE DOCSTRING HERE!!!
    '''
 
    stock, tableau, foundation = init_game()
    print( MENU )
    display( stock, tableau, foundation )
    option = get_option()
    while option[0] != 'Q':
        if option[0] == None:
            display( stock, tableau, foundation )
            option = get_option()   
        elif option[0] == 'D':
            deal_to_tableau(stock, tableau)
            display( stock, tableau, foundation )
            option = get_option()
        elif option[0] == 'F':
            from_col = option[1]
            if validate_move_to_foundation(tableau, from_col) == True:
                move_to_foundation(tableau, foundation, from_col)
                if check_for_win(stock, tableau) == True:
                    print("You won!")
                    break
                else:
                    display( stock, tableau, foundation )
                    option = get_option()
            else:
                card = tableau[int(from_col)-1][-1]
                print("Error, cannot move {}.".format(card))
                display( stock, tableau, foundation )
                option = get_option()
                
        elif option[0] == 'T':
            from_col, to_col = option[1],option[2]
            if validate_move_within_tableau(tableau, from_col, to_col) == True:
                move_within_tableau(tableau, from_col, to_col)
                if check_for_win(stock, tableau) == True:
                    print("You won!")
                    break
                else:
                    display( stock, tableau, foundation )
                    option = get_option()
            else:
                display( stock, tableau, foundation )
                option = get_option()
        
        elif option[0] == 'R':
            print("=========== Restarting: new game ============")
            print(RULES)
            stock, tableau, foundation = init_game()
            print( MENU )
            display( stock, tableau, foundation )
            option = get_option()
            
        elif option[0] == 'H':
            print( MENU )
            display( stock, tableau, foundation )
            option = get_option()
        else:
            display( stock, tableau, foundation )
            option = get_option()
    if option[0] == 'Q':
        print("You have chosen to quit.")
            
        

if __name__ == "__main__":
    main()
