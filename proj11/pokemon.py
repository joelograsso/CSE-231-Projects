# =============================================================================
# Pokemon Class file
# 
# Contains the Pokemon and Move class for proj11
# =============================================================================

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
        Returns the name of the move
        '''
        return self.name

    def __repr__(self):
        '''
        Returns the name of the move
        '''
        return self.name
    
    def get_name(self):
        '''
        Returns the name attribute
        '''
        return self.name
    
    def get_element(self):
        '''
        Returns the element attribute of a move
        '''
        return self.element
    
    def get_power(self):
        '''
        Returns the power of a move
        '''
        return self.power
    
    def get_accuracy(self):
        '''
        Returns the accuracy of the move
        '''
        return self.accuracy
    
    def get_attack_type(self):
        '''
        Returns the attack type of the move
        '''
        return self.attack_type

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
        Returns a string containing the name, hp, patt, sdef, element1/2, and 
        the moves of the pokemon
        '''
        moves_list = []
        line1 = '{:<15s}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n'.format(self.name, \
                 self.hp, self.patt, self.pdef, self.satt, self.sdef )
        line2 = '{:<15s}{:<15s}\n'.format(self.element1, self.element2)
        if self.moves != list():
            for move in self.moves:
                name = move.get_name()
                moves_list.append(name)
            line3 = '{:<15s}{:<15s}{:<15s}{:<15s}'.format(*moves_list)
        else:
            line3 = ''
        return line1 + line2+ line3

    def __repr__(self):
        '''
        Returns same as __str__ value
        '''
        return self.__str__()


    def get_name(self):
        '''
        Returns name of pokemon
        '''
        return self.name
    
    def get_element1(self):
        '''
        Returns element 1 of pokemom
        '''
        return self.element1
    
    def get_element2(self):
        '''
        Returns element 2 of pokemon
        '''
        return self.element2
    
    def get_hp(self):
        '''
        Returns hp of Pokemon 
        '''
        return self.hp
    
    def get_patt(self):
        '''
        Returns patt of pokemon
        '''
        return self.patt

    def get_pdef(self):
        '''
        Returns pdef of pokemon
        '''
        return self.pdef

    def get_satt(self):
        '''
        Returns satt of pokemon
        '''
        return self.satt

    def get_sdef(self):
        '''
        Returns sdef of pokemon
        '''
        return self.sdef
    
    def get_moves(self):
        '''
        Returns the moves of pokemon
        '''
        return self.moves

    def get_number_moves(self):
        '''
        Returns the number of moves
        '''
        return len(self.moves)

    def choose(self,index):
        '''
        Takes and index and returns the corresponding move of pokemon
        '''
        try:
            return self.moves[int(index)]
        except IndexError:
            return None

        
    def show_move_elements(self):
        '''
        Displays the elements of the pokemon's move
        '''
        element_list=[]
        for move in self.moves:
            element = str(move.get_element())
            element_list.append(element)
        print('{:<15s}{:<15s}{:<15s}{:<15s}'.format(*element_list))


    def show_move_power(self):
        '''
         Displays the power of the pokemon's move
        '''
        power_list=[]
        for move in self.moves:
            power = move.get_power()
            power_list.append(power)
        print('{:<15d}{:<15d}{:<15d}{:<15d}'.format(*power_list))

    def show_move_accuracy(self):
        '''
         Displays the accuracy of the pokemon's move
        '''
        acc_list=[]
        for move in self.moves:
            acc = move.get_accuracy()
            acc_list.append(acc)
        print('{:<15d}{:<15d}{:<15d}{:<15d}'.format(*acc_list))
        
    def add_move(self, move):
        '''
        Adds a move to the list of moves if there are less than 4 moves
        '''
        if self.get_number_moves() < 3:
            self.moves.append(move)
            
            
        
    def attack(self, move, opponent):
        '''
        Calculates the attack damage on an opponent.
        '''
    
        accuracy = move.get_accuracy()
        MP = move.get_power()
        attack_type = move.get_attack_type()
        if attack_type == 2:
            A = self.get_patt()
            D = opponent.get_pdef()
        elif attack_type == 3:
            A = self.get_satt()
            D = opponent.get_sdef()
        else:
            print("Invalid attack_type, turn skipped.")
            return
        
        if randint(1, 101) <= accuracy:
            Mod = 1.0
            move_element = move.get_element()
            if opponent.get_element1() in is_effective_dictionary[move_element]:
                Mod = Mod * 2
            if opponent.get_element1() in not_effective_dictionary[move_element]:
                Mod = Mod * 0.5
            if opponent.get_element1() in no_effect_dictionary[move_element]:
                Mod = Mod * 0
            if opponent.get_element2() in is_effective_dictionary[move_element]:
                Mod = Mod * 2
            if opponent.get_element2() in not_effective_dictionary[move_element]:
                Mod = Mod * 0.5
            if opponent.get_element2() in no_effect_dictionary[move_element]:
                Mod = Mod * 0
                
            if Mod > 1:
                print("It's super effective!!!!")
            elif Mod == 0:
                print("No effect!")
            elif Mod < 1:
                print("Not very effective...")
                
            if self.get_element1() == move_element:
                Mod = Mod *1.5
            if self.get_element2() == move_element:
                Mod = Mod * 1.5
                
#            if Mod > 1:
#                print("It's super effective!!!!")
#            elif Mod < 1:
#                print("Not very effective...")
                
            damage = int(((MP * (A/D)*20)/50 + 2)*Mod)    #calculates the formula
            opponent.subtract_hp(damage)    #removes HP from opponent
            
            
        else:
            print('Move missed!')
            return
    
            
            
        
            
        
    def subtract_hp(self,damage):
        '''
        Subtracts the damage away from the pokemon's HP
        '''
        if self.hp > 0:
            self.hp = self.hp - damage
            if self.hp < 0:
                self.hp = 0
        
    

        