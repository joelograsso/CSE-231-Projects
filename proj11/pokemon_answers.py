"""
    SOURCE HEADER GOES HERE!
"""

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
#Attributes:
#• name: the name of the move (string)
#• element: the move’s type (string)
#• power: the base damage that the move inflicts (int)
#• accuracy: how likely the move is to hit an opponent (int)
#• attack_Type: classification if this is a physical attack, special attack or status move (int)
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
            Returns just the name of the move (used for printing).
            for printing. Takes 1 arg: self. Returns a string.
        '''        
        return(str(self.name))

    def __repr__(self):
        '''
            Returns just the name of the move (can utilize the __str__() method here).
            for displaying in the shell. Takes 1 arg: self. Returns a string.
        '''
        return(self.__str__())
    
    def get_name(self):
        '''
            Returns the name attribute.
        '''
        return(self.name)
    
    def get_element(self):
        '''
            Returns the element attribute.
        '''
        return(self.element)
    
    def get_power(self):
        '''
            Returns the power attribute.
        '''
        return(self.power)
    
    def get_accuracy(self):
        '''
            Returns the accuracy attribute.
        '''
        return(self.accuracy)
    
    def get_attack_type(self):
        '''
            Returns the attack_type attribute.
        '''
        return(self.attack_type)

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
#Attributes:
#• name: the name of the pokemon (string)
#• element1: the first element of the pokemon (string)
#• element2: the second element of the pokemon (string) (None if the pokemon has one
#element)
#• hp: the health points of the pokemon, when this reaches 0 the pokemon faints (int)
#• patt: the physical strength of the pokemon (int)
#• pdef: the physical defense of the pokemon (int)
#• satt: the special strength of the pokemon (int)
#• sdef: the special defense of the pokemon (int)
#• moves: the list of moves that this pokemon has access to (list of Moves)
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
            Returns a string containing the parts of the pokemon object divided into three lines. The
            first line will display in this order: name, hp, patt, pdef, satt and sdef, followed by a
            newline character directly after sdef with no space inbetween sdef and the newline
            character. The second line will display the element1 and element2 with a newline
            character after element2. The third line will display all the moves of that pokemon.
            Each attribute will take up exactly 15 spaces and be left adjusted no matter the type.
        '''
        string = "{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n{:<15}{:<15}\n".format(self.name,\
                  self.hp, self.patt, self.pdef, self.satt, self.sdef, self.element1, \
                  self.element2,)
        
        for i in range(len(self.moves)): #{:<15}
            moves1 = self.moves
            #print(moves1[i])
            move = "{:<15}".format(str(moves1[i]))
            string += move
        
        return string
            
    def __repr__(self):
        '''
            Returns the same value as the __str__() method to.
            for displaying in the shell. Takes 1 arg: self. Returns a string
        '''
        return(self.__str__())


    def get_name(self):
        '''
            Returns the name attribute
        '''
        return(self.name)
    
    def get_element1(self):
        '''
            Returns the element1 attribute
        '''
        return(self.element1)
    
    def get_element2(self):
        '''
            Returns the element2 attribute (can be None)
        '''
        return(self.element2)
    
    def get_hp(self):
        '''
            Returns the hp attribute.
        '''
        return(self.hp)
    
    def get_patt(self):
        '''
            Returns the patt attribute.
        '''
        return(self.patt)

    def get_pdef(self):
        '''
            Returns the pdef attribute.
        '''
        return(self.pdef)

    def get_satt(self):
        '''
            Returns the satt attribute.
        '''
        return(self.satt)

    def get_sdef(self):
        '''
            Returns the sdef attribute.
        '''
        return(self.sdef)
    
    def get_moves(self):
        '''
            Returns the moves attribute (list)
        '''
        return(self.moves)

    def get_number_moves(self):
        '''
            Returns the number of moves.
        '''
        return(len(self.moves))

    def choose(self,index):
        '''
            Takes an index and returns the corresponding move from the moves list. 
            If there is an IndexError returns None.
        '''
        try:
            return(self.moves[index])
        except IndexError:
            return None

        
    def show_move_elements(self):
        '''
            Displays the elements of the pokemon’s moves (each in a 15-space field, left justified).
            This function does not return anything.
        '''
        string = ''
        for i in range(len(self.moves)):
            power = "{:<15} ".format((self.moves[i]).get_element())
            string += power
        
        print(string)


    def show_move_power(self):
        '''
            Displays the power of the pokemon’s moves (each in a 15-space field, left justified). This
            function does not return anything.
        '''
        string = ''
        for i in range(len(self.moves)):
            power = "{:<15} ".format((self.moves[i]).get_power())
            string += power
        
        print(string)

    def show_move_accuracy(self):
        '''
            Displays the accuracy of the pokemon’s moves (each in a 15-space field, left justified).
            This function does not return anything.
        '''
        string = ''
        for i in range(len(self.moves)):
            power = "{:<15} ".format((self.moves[i]).get_accuracy())
            string += power
        
        print(string)
        
        
    def add_move(self, move):
        '''
            Adds the move parameter to the list of moves for this pokemon if this pokemon has
            three or less moves. This function does not return anything.
        '''
        if len(self.moves)<4:
            self.moves.append(move)
            
        
    def attack(self, move, opponent):
        '''
            This method takes the move used by the attacker (self) and deals damage to the
            opponent (who should also be an instance of class Pokemon). It does not return
            anything
        '''
        mp = move.get_power()
#        If the attack_type is equal to 2 then A is the attacker’s
#        patt attribute and D is the defender’s pdef attribute. If the attack_type is equal to 3 then
#        A is the attacker’s satt attribute and D is the defender’s sdef. If the attack_type has
#        some other value, print the message "Invalid attack_type, turn
#        skipped." and return
        if move.get_attack_type()==2:
            A = self.get_patt()
            D = opponent.get_pdef()
        elif move.get_attack_type()==3:
            A = self.get_satt()
            D = opponent.get_sdef()
        else: 
            print("Invalid attack_type, turn skipped.")
            return
            
        accuracy_value = randint(1,100)
        if accuracy_value > move.get_accuracy():
            print("Move missed!")
            return
            
        modifier = 1.0
        att_type = move.get_element()
        
        opp_type = opponent.get_element1()
        if opp_type in is_effective_dictionary[att_type]:
            modifier = modifier*2
        elif opp_type in not_effective_dictionary[att_type]:
            modifier = modifier*0.5
        elif opp_type in no_effect_dictionary[att_type]:
            modifier = modifier*0
            
        opp_type = opponent.get_element2()
        if opp_type in is_effective_dictionary[att_type]:
            modifier = modifier*2
        elif opp_type in not_effective_dictionary[att_type]:
            modifier = modifier*0.5
        elif opp_type in no_effect_dictionary[att_type]:
            modifier = modifier*0
        
        if modifier > 1:
            print("It's super effective!!!!")
        elif modifier < 1 and modifier > 0:
            print("Not very effective...")
        elif modifier == 0:
            print("No effect!")
            
        attacker_type1 = self.get_element1()
        attacker_type2 = self.get_element2()
        
        if att_type == attacker_type1 or att_type == attacker_type2:
            modifier = modifier*1.5
        
        damage = int((((mp*(A/D)*20)/50)+2)*modifier)
        #print(modifier)
        
        opponent.subtract_hp(damage)
        
    def subtract_hp(self,damage):
        '''
            This method takes the damage variable and subtracts it from the hp of the Pokemon
            object. The hp of the Pokemon object becomes the maximum of the (hp – damage) or 0.
            This function does not return anything.
        '''
        self.hp = self.hp - damage
        self.hp = 0 if self.hp < 0 else self.hp   