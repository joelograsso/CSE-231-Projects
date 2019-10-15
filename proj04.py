#######
#Computer Project #4
#this program prompts the user on a list of mathmatical functions they can select.
#can select to find the natural sum of a number, approximate the value of euler's number,
#and calculate the approximate value of cosh(x) and sinh(x) while comparing it to the math module value.
#will continue to prompt user for inputs unless given the command to quit the program
#######

import math
EPSILON = 1.0e-7

def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the value of the sum of the first N natural numbers. 
             B. Display the approximate value of e.
             C. Display the approximate value of the hyperbolic sine of X.
             D. Display the approximate value of the hyperbolic cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)    
def sum_natural(N):
    '''
    This function takes in a string and tries to turn the string into an int,
    then takes the natural sum of that number and returns it. 
    if the string cannot be turned into an int, it returns nothing
    '''
    try:    #going to try to run this code
        n_int = int(N)    # turns string N into an int
        if N.isdigit() == False or n_int <= 0:    # if N is not a digit or if N is less than or equal to 0, returns nothing 
            return None
        else:    #if N is a digit > 0
            total = 0    #total sum
            n_int = int(N)
            for number in range (0,(n_int + 1)):    #for every number starting from 0 to N
                total = total + number    #total is reassigned to origional total + the number 
            return total    #returns total
    except ValueError:    #if N is not able to be converted into an int
        return None    #returns none
def approximate_euler():
    '''
    This function takes in no inputs and returns the approximate value of euler's number to the 10th decimal
    '''
    n = 0    #counter
    term = 1    #first term at n=0
    e = 0    #value of e
    while True: 
        term = 1/(math.factorial(n))    #term is reassigned to 1/factorial(n)
        n += 1    # adds 1 to the counter
        e += term    # adds term to e
        if abs(term) < EPSILON:    # if the next term is smaller than EPSILON
            e = e - term    #subrtract the last term added
            e = round(e,10)    #round e 10 decimal places
            break    #ends loop 
    return e    #returns e
def approximate_sinh(x):
    '''
    This function approximates the hyperbolic sin of x(in radians) by taking in an input, x
    and returning the value of sinh(x) rounded to the 10th decimal.
    if x is not a valid float, will return None
    '''
    try:    #try to execture 
        n = 0    #counter
        x_float = float(x)    #turns x into a float
        total = 0.0    #total value
        term = 0.0    #value of term
        while True:
            power = float(2*n+1)    #turns power/denominator into float
            term = ((x_float**power)/(math.factorial(power)))    #term is assigned to (x^(2n+1))/(2n+1)!
            total += term    #adds term to the total
            n += 1    #increases counter 
            if abs(term) < EPSILON:    #if the term is smaller than EPSILON
                total = total - term    #take away that last term from the total 
                total = round(total,10)    #round total 10 decimal places
                break    
        return total     #return total
    except ValueError:    #if x cannot be turned into a float
        return None    #return none
def approximate_cosh(x):
    '''
    This function approximates the hyperbolic cso of x(in radians) by taking in an input, x
    and returning the value of cosh(x) rounded to the 10th decimal.
    if x is not a valid float, will return None
    '''
    try:
        n = 0    #counter
        x_float = float(x)    #tuyrns x into a float
        total = 0.0    #total sum
        term = 0.0    #value of term
        while True:
            power = float(2*n)    #truns power/denominator into float
            term = ((x_float**power)/(math.factorial(power)))    #term is assigned to (x^(2n))/(2n)!
            total += term    #add term to total
            n += 1    #add to counter
            if abs(term) < EPSILON:    #if term is smaller than EPSILON
                total = total - term    #take away term from total
                total = round(total,10)    #round total 10 decimal places
                break
        return total    #return total
    except ValueError:    #if x cannot be turned into a float
        return None    #return none
def main():
    display_options()
    option = input("\n\tEnter option: ")    #asks for an option
    option_lower = option.lower()    #turns option to lower case
    while option_lower != 'x':    #while the option isn't x
        option_upper = option.upper()    #turns option to uppercase
        if option_lower == 'a':    #if option_lower == a
            n = input("\nEnter N: ")    #input a value n
            if sum_natural(n) == None:    #if the function returns none
                print("\n\tError: N was not a valid natural number. [{}]".format(n))    #print that it was an invalid number
                option = input("\n\t\tEnter option: ")    #asks for user's option
                option_lower = option.lower()
            else:
                print("\n\tThe sum: " + str(sum_natural(n)))    #prints natural sum of n
                option = input("\n\t\tEnter option: ")    #asks for option
                option_lower = option.lower()
        elif option_lower == 'b':    #if option = b
            MATH_MOD = math.e    #math module value of e
            diff = abs(MATH_MOD - approximate_euler())     #takes the difference of the two numbers
            print("\n\tApproximation: {:.10f}".format(approximate_euler()))    #prints approximate value of euler number
            print("\tMath module:   {:.10f}".format(MATH_MOD))    #print math module value of e
            print("\tdifference:    {:.10f}".format(diff))     #prints the difference between the two numbers
            option = input("\n\tEnter option: ")
            option_lower = option.lower()
        elif option_lower == 'c':     #if option = c
            x = input("\n\tEnter X: ")    #input a value x
            if approximate_sinh(x) == None:    #if the function returns None
                print("\n\tError: X was not a valid float. [{}]".format(x))    #print X was invalid float
                option = input("\n\tEnter option: ")
                option_lower = option.lower()
            else:    #function != None
                x_float = float(x)    #x is float
                MATH_MOD = math.sinh(x_float)    #math module for sinh(x)
                diff = abs(MATH_MOD - approximate_sinh(x))    #difference between the two numbers
                print("\n\tApproximation: {:.10f}".format(approximate_sinh(x)))    #print approximate value of sinh(x)
                print("\tMath module:   {:.10f}".format(MATH_MOD))    #print math module of sinh(x)
                print("\tdifference:    {:.10f}".format(diff))    #prints difference of two numbers
                option = input("\n\tEnter option: ")
                option_lower = option.lower()
        elif option_lower == 'd':    #if option = d
             x = input("\n\tEnter X: ")    #input number x
             if approximate_cosh(x) == None:    #if the function returns None
                print("\n\tError: X was not a valid float. [{}]".format(x))    #print x was an invalid float
                option = input("\n\tEnter option: ")
                option_lower = option.lower()
             else:    #function != None
                x_float = float(x)    #turns x to float
                MATH_MOD = math.cosh(x_float)    #math module of cosh(x)
                diff = abs(MATH_MOD - approximate_cosh(x))    #difference between two numbers
                print("\n\tApproximation: {:.10f}".format(approximate_cosh(x)))    #prints approximate value of cosh(x)
                print("\tMath module:   {:.10f}".format(MATH_MOD))    #prints math module of cosh(x)
                print("\tdifference:    {:.10f}".format(diff))    #prints the difference of the two numbers
                option = input("\n\tEnter option: ")
                option_lower = option.lower()
        elif option_lower == 'm':    #if option = m
            display_options()    #display all options available 
            option = input("\n\tEnter option: ")    #asks for option
            option_lower = option.lower()
        else:    #if option != a,b,c,d,m, or x
            print("\nError:  unrecognized option [{}]".format(option_upper))    #print that option was invalid
            display_options()    #display options
            option = input("\n\tEnter option: ")    #asks for option
            option_lower = option.lower()
    else:    #if option = x
        print('Hope to see you again.')    #print statement and end the program
if __name__ == "__main__": 
    main()