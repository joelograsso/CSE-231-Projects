###########################################################
    #  Computer Project #2
    #
    # This program takes in inputs for identifing the customer code,\
    # how many days the car was rented, and the odometer before and after using the car.
    # It then takes those inputs and applies them to applicable areas within the code \
    # in order to find the total cost of using the car during the time rented.
    #    
    #    
    ###########################################################





print('\nWelcome to car rentals. ')
print('\nAt the prompts, please enter the following: ')
print("\tCustomer's classification code (a character: BDW) ")
print('\tNumber of days the vehicle was rented (int)')
print('\tOdometer reading at the start of the rental period (int)')
print('\tOdometer reading at the end of the rental period (int)')
YN = input('Would you like to continue (Y/N)? ' ) #asks user if want to continue


while YN == 'Y':    #runs loop 
    CLASS_CODE = input('\nCustomer code (BDW): ')    #asks user for class code
    while CLASS_CODE != 'B' and CLASS_CODE != 'D' and CLASS_CODE != 'W':    #loop to search if class code does not equal B,W,or D
       print("\n\t*** Invalid customer code. Try again. ***")
       CLASS_CODE = input('\nCustomer code (BDW): ')       
    if CLASS_CODE == 'B':
        RENTED_DAYS = int(input('\nNumber of days: ' ))    #asks for days rented
        OD_START = int(input('Odometer reading at the start: '))    #odometer readings, beginning and end
        OD_END = int(input('Odometer reading at the end:'))
        OD_OVER = 1000000 - OD_START    #checks to see if odometer resets
        if  OD_OVER <= 10:    #if OD_OVER <= 10 this means that the starting odometer reading had reset and needs to be added on to the end instead of subtracting. 
            MILES_DRIVEN = float((OD_END + OD_OVER)/10)    #adjusts miles driven for a odometer that reset during trip
            TOTAL = 0.25*(MILES_DRIVEN) + 40.0*(float(RENTED_DAYS))    #total price with class code B, with reset
            print("\nCustomer summary: ")
            print("\tclassification code: " + CLASS_CODE)
            print('\trental period (days): ' + str(RENTED_DAYS))
            print('\todometer reading at start: ' + str(OD_START))
            print('\todometer reading at end: ' + str(OD_END))
            print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
            print('\tamount due: $ ' + str(TOTAL))
            YN = input('\nWould you like to continue (Y/N)?' )
        else:    #if the odometer does not reset, runs code below
            MILES_DRIVEN = float((OD_END - OD_START)/10)    #miles driven
            TOTAL = float(0.25*(MILES_DRIVEN) + 40.0*(float(RENTED_DAYS)))    #total price with class code B, no reset
            print("\nCustomer summary: ")
            print("\tclassification code: " + CLASS_CODE)
            print('\trental period (days): ' + str(RENTED_DAYS))
            print('\todometer reading at start: ' + str(OD_START))
            print('\todometer reading at end: ' + str(OD_END))
            print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
            print('\tamount due: $ ' + str(TOTAL))
            YN = input('\nWould you like to continue (Y/N)?' )
    if CLASS_CODE == 'D':
        RENTED_DAYS = int(input('\nNumber of days: ' ))    #asks for days rented
        OD_START = int(input('Odometer reading at the start: '))    #odometer readings, beginning and end
        OD_END = int(input('Odometer reading at the end:'))
        OD_OVER = 1000000 - OD_START    #checks to see if odometer resets
        MILES_DRIVEN = float((OD_END - OD_START)/10)
        AVG_MILES = float(((OD_END - OD_START)/RENTED_DAYS)/10)    #finds average amount of miles
        if AVG_MILES <= 100:    #calculates total price if the average miles are below 100
            TOTAL = 60.0 * (RENTED_DAYS)    #total for class code D under 100 average miles a day
            print("\nCustomer summary: ")
            print("\tclassification code: " + CLASS_CODE)
            print('\trental period (days): ' + str(RENTED_DAYS))
            print('\todometer reading at start: ' + str(OD_START))
            print('\todometer reading at end: ' + str(OD_END))
            print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
            print('\tamount due: $ ' + str(TOTAL))
            YN = input('\nWould you like to continue (Y/N)?' )
        else:    #calculates total price if average miles  > 100
            MILES_OVER = MILES_DRIVEN - (100 * RENTED_DAYS)    #finds how many miles over the 100 miles/day limit you are
            TOTAL = (0.25 * MILES_OVER) + 60 * RENTED_DAYS     #total for class code D over 100 average miles a day
            print("\nCustomer summary: ")
            print("\tclassification code: " + CLASS_CODE)
            print('\trental period (days): ' + str(RENTED_DAYS))
            print('\todometer reading at start: ' + str(OD_START))
            print('\todometer reading at end: ' + str(OD_END))
            print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
            print('\tamount due: $ ' + str(TOTAL))
            YN = input('\nWould you like to continue (Y/N)?' )
    if CLASS_CODE == 'W':
        RENTED_DAYS = int(input('\nNumber of days: ' ))    #asks for days rented
        OD_START = int(input('Odometer reading at the start: '))    #odometer readings, beginning and end
        OD_END = int(input('Odometer reading at the end: '))
        OD_OVER = 1000000 - OD_START    #checks to see if odometer resets
        if RENTED_DAYS >= 7:    #checks to see if rented days  is at minimum 1 week
            if RENTED_DAYS%7 == 0:    #see if the number of weeks is a whole number
                WEEKS =  round(RENTED_DAYS/7) 
                WEEKS = float(WEEKS)
                MILES_DRIVEN = float((OD_END - OD_START)/10)
                AVG_MILES_WEEK = float(((OD_END - OD_START)/WEEKS)/10)
                if AVG_MILES_WEEK <= 900:   
                    TOTAL = 190.0*(WEEKS)    #calculates total if average number of miles per weeks <= 900 miles 
                    print("\nCustomer summary: ")
                    print("\tclassification code: " + CLASS_CODE)
                    print('\trental period (days): ' + str(RENTED_DAYS))
                    print('\todometer reading at start: ' + str(OD_START))
                    print('\todometer reading at end: ' + str(OD_END))
                    print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                    print('\tamount due: $ ' + str(TOTAL))
                    YN = input('\nWould you like to continue (Y/N)?' )
                elif 900 < AVG_MILES_WEEK <= 1500: 
                    TOTAL = 100.0*(WEEKS) + 190*(WEEKS)    #calculates total if average number of miles per week is greater tha 900 but less than/equal to 1500
                    print("\nCustomer summary: ")
                    print("\tclassification code: " + CLASS_CODE)
                    print('\trental period (days): ' + str(RENTED_DAYS))
                    print('\todometer reading at start: ' + str(OD_START))
                    print('\todometer reading at end: ' + str(OD_END))
                    print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                    print('\tamount due: $ ' + str(TOTAL))
                    YN = input('\nWould you like to continue (Y/N)?' )
                else: 
                    TOTAL = (200*(WEEKS) + 190*(WEEKS) + 0.25*(MILES_DRIVEN - (1500 * WEEKS)))    #calculates total if average number of miles per week is greater than 1500
                    print("\nCustomer summary: ")
                    print("\tclassification code: " + CLASS_CODE)
                    print('\trental period (days): ' + str(RENTED_DAYS))
                    print('\todometer reading at start: ' + str(OD_START))
                    print('\todometer reading at end: ' + str(OD_END))
                    print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                    print('\tamount due: $ ' + str(TOTAL))
                    YN = input('\nWould you like to continue (Y/N)?' )
            if RENTED_DAYS%7 != 0:    #checks to see if weeks is a fraction > 1
                WEEKS = round(RENTED_DAYS/7) +1    #rounds week up if fraction of week
                WEEKS = float(WEEKS)    #rounds week to nearest whole number
                MILES_DRIVEN = float((OD_END - OD_START)/10)    #Finds miles driven 
                AVG_MILES_WEEK = float(((OD_END - OD_START)/WEEKS)/10)    #finds average amount of miles traveled per week
                if AVG_MILES_WEEK <= 900:   
                    TOTAL = 190.0 *(WEEKS)    #calculates total if average number of miles per weeks <= 900 miles
                    print("\nCustomer summary: ")
                    print("\tclassification code: " + CLASS_CODE)
                    print('\trental period (days): ' + str(RENTED_DAYS))
                    print('\todometer reading at start: ' + str(OD_START))
                    print('\todometer reading at end: ' + str(OD_END))
                    print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                    print('\tamount due: $ ' + str(TOTAL))
                    YN = input('\nWould you like to continue (Y/N)?' )
                elif 900 < AVG_MILES_WEEK <= 1500:
                    TOTAL = 100.0*(WEEKS) + 190*(WEEKS)    #calculates total if average number of miles per week is greater tha 900 but less than/equal to 1500
                    print("\nCustomer summary: ")
                    print("\tclassification code: " + CLASS_CODE)
                    print('\trental period (days): ' + str(RENTED_DAYS))
                    print('\todometer reading at start: ' + str(OD_START))
                    print('\todometer reading at end: ' + str(OD_END))
                    print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                    print('\tamount due: $ ' + str(TOTAL))
                    YN = input('\nWould you like to continue (Y/N)?' )
                else: 
                    TOTAL = (200*(WEEKS) + 190*(WEEKS) + 0.25*(MILES_DRIVEN - (1500 * WEEKS)))    #calculates total if average number of miles per week is greater than 1500
                    print("\nCustomer summary: ")
                    print("\tclassification code: " + CLASS_CODE)
                    print('\trental period (days): ' + str(RENTED_DAYS))
                    print('\todometer reading at start: ' + str(OD_START))
                    print('\todometer reading at end: ' + str(OD_END))
                    print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                    print('\tamount due: $ ' + str(TOTAL))
                    YN = input('\nWould you like to continue (Y/N)?' )    
        else:
            WEEKS =  round(RENTED_DAYS/7)    # rounds weeks to nearest intiger 
            WEEKS = float(WEEKS)    #turns week into float
            MILES_DRIVEN = float((OD_END - OD_START)/10)
            AVG_MILES_WEEK = float(((OD_END - OD_START)/WEEKS)/10)
            if AVG_MILES_WEEK <= 900:
                TOTAL = 190.0*(WEEKS)    #calculates total if average number of miles per weeks <= 900 miles
                print("\nCustomer summary: ")
                print("\tclassification code: " + CLASS_CODE)
                print('\trental period (days): ' + str(RENTED_DAYS))
                print('\todometer reading at start: ' + str(OD_START))
                print('\todometer reading at end: ' + str(OD_END))
                print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                print('\tamount due: $ ' + str(TOTAL))
                YN = input('\nWould you like to continue (Y/N)?' )
            elif 900 < AVG_MILES_WEEK <= 1500:  
                TOTAL = 100.0*(WEEKS) + 190*(WEEKS)    #calculates total if average number of miles per week is greater tha 900 but less than/equal to 1500
                print("\nCustomer summary: ")
                print("\tclassification code: " + CLASS_CODE)
                print('\trental period (days): ' + str(RENTED_DAYS))
                print('\todometer reading at start: ' + str(OD_START))
                print('\todometer reading at end: ' + str(OD_END))
                print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                print('\tamount due: $ ' + str(TOTAL))
                YN = input('\nWould you like to continue (Y/N)?' )
            else: 
                TOTAL = (200*(WEEKS) + 190*(WEEKS) + 0.25*(MILES_DRIVEN - (1500 * WEEKS)))    #calculates total if average number of miles per week is greater than 1500
                print("\nCustomer summary: ")
                print("\tclassification code: " + CLASS_CODE)
                print('\trental period (days): ' + str(RENTED_DAYS))
                print('\todometer reading at start: ' + str(OD_START))
                print('\todometer reading at end: ' + str(OD_END))
                print('\tnumber of miles driven: ' + str(MILES_DRIVEN))
                print('\tamount due: $ ' + str(TOTAL))
                YN = input('\nWould you like to continue (Y/N)?' )
else:
    print(' Thank you for your loyalty.')