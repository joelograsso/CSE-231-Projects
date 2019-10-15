########################################
#  Computer Project 3
#   Strings
#   Tuition Calculator
#   asks user if they are a resident and if not if they are international
#   asks user for their class and college that they are in
#   returns the tuition back to the user 
#   asks if user wants to do anothew calculation
#########################################
print('2019 MSU Undergraduate Tuition Calculator.')
ANS = ' '
while ANS != 'no':
    RESIDENT = input('Resident (yes/no): ')    #asks user if they are resident
    RESIDENT_LOWER = RESIDENT.lower()
    if RESIDENT_LOWER == 'no': 
        INT = input('International (yes/no): ')    #asks user if they are international if not a resident
        INT_LOWER = INT.lower()
        LEVEL = input('Level—freshman, sophomore, junior, senior: ' )    #asks what class user is
        LEVEL_LOWER = LEVEL.lower()
        while LEVEL_LOWER != 'freshman' and LEVEL_LOWER != 'sophomore' and LEVEL_LOWER != 'junior' and LEVEL_LOWER != 'senior':    #if a class is not identified, says input is invalid and asks again
            print('Invalid input. Try again.')
            LEVEL = input('Level—freshman, sophomore, junior, senior: ' )
            LEVEL_LOWER = LEVEL.lower()
        if LEVEL_LOWER == 'junior' or LEVEL_LOWER == 'senior':    #if class was a junior or senior
            COLLEGE = input('Enter college as business, engineering, health, sciences, or none: ')    #asks for college in
            COLLEGE_LOWER = COLLEGE.lower()
            CMSE = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ')   #asks if their major is CMSE 
            CMSE_LOWER = CMSE.lower()
            if COLLEGE_LOWER == 'business':    # if in business school 
                CREDITS = input('Credits: ')    #inital input of credits
                while CREDITS.isdigit() == False or CREDITS == '0':    #verifies that credits are intigers above but not including 0
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)    #turns credits into a intiger for math
                if CREDITS > 18:    
                    TUITION = 20786 + 1385.75*(CREDITS - 18) + 21 + 3 + 5 + 226     #tuition for a nonresidental business student with 18+ credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670    #adds cost of being a CMSE major
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750    #adds cost of being an international student
                elif 12<= CREDITS <= 18:
                    TUITION = 20786 + 21 + 3 + 5 + 226    #tuition for a nonresidential business student with 12-18 credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670    #adds cost of being a CMSE major
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750    #adds cost of being an international student
                elif 0< CREDITS < 12:
                    TUITION = 1385.75*CREDITS + 21 + 3    #tuition for nonresidential business students with less than 12 credits
                    if CREDITS <= 4:
                        TUITION = TUITION + 113    #adds part time special fee for business school if credits <= 4
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402    #adds part time special fee for CMSE majors 
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 375    #adds part time special fee for internaional students
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 + 226    #adds state news tax and full time fee for nonresidential business students if credits >6
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670    #adds full time CMSE major fee for nonresidential business students 
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750    #adds full time international fee for nonresidential business students  
                    if CREDITS == 5:    
                        TUITION = TUITION + 670    #adds full time business fee if credits = 5
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750    #adds full time international fee to nonresidential business students  
            elif COLLEGE_LOWER == 'engineering':    #if in the engineering school 
                CREDITS = input('Credits: ') 
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 20786 + 1385.75*(CREDITS - 18) + 21 + 3 + 5 + 670    #tuition for nonresidential engineering students with over 18 credits 
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750
                elif 12<= CREDITS <= 18:
                    TUITION = 20786 + 21 + 3 + 5 + 226    #tuition for nonresidential engineering students with 12-18 credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750
                elif 0< CREDITS < 12:
                    TUITION = 1385.75*CREDITS + 21 + 3    #tuition for nonresidential engineering students with less than 12 credits 
                    if CREDITS <= 4:
                        TUITION = TUITION + 402
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 375
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 + 226
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                    if CREDITS == 5:
                        TUITION = TUITION + 402  
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
            elif COLLEGE_LOWER == 'health':    # if in health school
                CREDITS = input('Credits: ')
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 20501 + 1366.75*(CREDITS - 18) + 21 + 3 + 5 + 100    #tuition for nonresidential health students with 18+ credits 
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750
                elif 12<= CREDITS <= 18:
                    TUITION = 20501 + 21 + 3 + 5 + 100    #tuition for nonresidential health students with 12-18 credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750
                elif 0< CREDITS < 12:
                    TUITION = 1336.75*CREDITS + 21 + 3    #tuition for nonresidential health students with less than 12 credits
                    if CREDITS <= 4:
                        TUITION = TUITION + 50
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 375
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 + 100
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                    if CREDITS == 5:
                        TUITION = TUITION + 100  
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
            elif COLLEGE_LOWER == 'sciences':    #if in sciences school
                CREDITS = input('Credits: ')
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 20501 + 1366.75*(CREDITS - 18) + 21 + 3 + 5 + 100    #tuition for nonresidential science students with 18+ credits 
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750
                elif 12<= CREDITS <= 18:
                    TUITION = 20501 + 21 + 3 + 5 + 100    #tuition for nonresidential science students with 12-18 credits 
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750
                elif 0< CREDITS < 12:
                    TUITION = 1366.75*CREDITS + 21 + 3    #tuition for nonresidential science students with less than 12 credits 
                    if CREDITS <= 4:
                        TUITION = TUITION + 50
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 375
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 + 100
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                    if CREDITS == 5:
                        TUITION = TUITION + 100 
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
            else:     #if no college is inputed
                JM = input('Are you in the James Madison College (yes/no): ')    #asks if in james madison 
                JM_LOWER = JM.lower()
                CREDITS = input('Credits: ')
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 20501 + 1366.75*(CREDITS - 18) + 21 + 3 + 5 + 7.5     #tuition for nonresidential James Madison students with 18+ credits 
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750
                elif 12<= CREDITS <= 18:
                    TUITION = 20501 + 21 + 3 + 5     #tuition for nonresidential James Madison students with 12-18 credits 
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                    if INT_LOWER == 'yes':
                        TUITION = TUITION + 750
                elif 0< CREDITS < 12:
                    TUITION = 1325.5*CREDITS + 21 + 3 + 7.5    #tuition for nonresidential James Madison students with lerss than 12 credits 
                    if CREDITS <= 4:
                        TUITION = TUITION + 50    
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
        elif  LEVEL_LOWER == 'freshman' or LEVEL_LOWER == 'sophomore':    #if class was fershman of sophomore
            COE = input('Are you admitted to the College of Engineering (yes/no): ')    #asks if admitted into college of engineering
            COE_LOWER = COE.lower()
            if COE_LOWER == 'yes':    #if accepted into CoE
                if LEVEL_LOWER == 'freshman':    #if class was freshman
                    CREDITS = input('Credits: ')
                    while CREDITS.isdigit() == False or CREDITS == '0':
                        if '.' in CREDITS:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS.isdigit() == False:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS <= '0':
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                    CREDITS = int(CREDITS)
                    if CREDITS > 18:
                        TUITION = 19883 + 1325.5*(CREDITS - 18) + 21 + 3 + 5 + 670    #tuition for nonresidential engineering freshman students with 18+ credits 
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                    elif 12<= CREDITS <= 18:
                        TUITION = 19883 + 21 + 3 + 5 + 670    #tuition for nonresidential engineering freshman students with 12-18 credits 
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                    elif 0< CREDITS < 12:
                        TUITION = 1382.5*CREDITS + 21 + 3    #tuition for nonresidential engineering freshman students with less than 12 credits 
                        if CREDITS <= 4:
                            TUITION = TUITION + 402
                            if CMSE_LOWER == 'yes':
                                TUITION = TUITION + 402
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 375
                        if CREDITS >= 6:
                            TUITION = TUITION + 5 + 670
                            if CMSE_LOWER == 'yes':
                                TUITION = TUITION + 670
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 750
                        if CREDITS == 5:
                            TUITION = TUITION + 670  
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 750
                elif LEVEL_LOWER == 'sophomore':    #if class was a sophomore
                   CREDITS = input('Credits: ')
                   while CREDITS.isdigit() == False or CREDITS == '0':
                        if '.' in CREDITS:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS.isdigit() == False:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS <= '0':
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                   CREDITS = int(CREDITS)
                   if CREDITS > 18:
                        TUITION = 19883 + 1325.5*(CREDITS - 18) + 21 + 3 + 5 + 670    #tuition for nonresidential engineering sophomore students with 18+ credits 
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                   elif 12<= CREDITS <= 18:
                        TUITION = 19883 + 21 + 3 + 5 + 670    #tuition for nonresidential engineering sophomore students with 12-18 credits 
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                   elif 0< CREDITS < 12:
                        TUITION = 1382.5*CREDITS + 21 + 3    #tuition for nonresidential engineering sophomore students with less than 12 credits 
                        if CREDITS <= 4:
                            TUITION = TUITION + 402
                            if CMSE_LOWER == 'yes':
                                TUITION = TUITION + 402
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 375
                        if CREDITS >= 6:
                            TUITION = TUITION + 5 + 670
                            if CMSE_LOWER == 'yes':
                                TUITION = TUITION + 670
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 750
                        if CREDITS == 5:
                            TUITION = TUITION + 670  
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 750
            elif COE_LOWER == 'no':    #if not accepted into CoE
                JM = input('Are you in the James Madison College (yes/no): ')    #asks if in James Madison
                JM_LOWER = JM.lower()
                if JM_LOWER == 'yes':    #if in James Madison
                    CREDITS = input('Credits: ')
                    while CREDITS.isdigit() == False or CREDITS == '0':
                        if '.' in CREDITS:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS.isdigit() == False:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS <= '0':
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                    CREDITS = int(CREDITS)
                    if CREDITS > 18:
                        TUITION = 19883 + 1325.5*(CREDITS - 18) + 21 + 3 + 5 + 7.5    #tuition for nonresidential James Madison students with 18+ credits 
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                    elif 12<= CREDITS <= 18:
                        TUITION = 19883 + 21 + 3 + 5 + 7.5    #tuition for nonresidential James Madison students with 12-18 credits
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                    elif 0< CREDITS < 12:
                        TUITION = 494*CREDITS + 21 +3 + 7.5    #tuition for nonresidential James Madison students with less than 12 credits
                        if CREDITS >=6:
                            TUITION = TUITION + 5
                        if INT_LOWER == 'yes':
                            TUITION = TUITION + 750
                else:    #if not in James Madison
                        CREDITS = input('Credits: ')
                        while CREDITS.isdigit() == False or CREDITS == '0':
                            if '.' in CREDITS:
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                            if CREDITS.isdigit() == False:
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                            if CREDITS <= '0':
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                        CREDITS = int(CREDITS)
                        if CREDITS > 18:
                            TUITION = 19883 + 1325.5*(CREDITS - 18) + 21 + 3 + 5    #tuition for nonresidential students with 18+ credits
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 750
                        elif 12<= CREDITS <= 18:
                            TUITION = 19883 + 21 + 3 + 5    #tuition for nonresidential students with 12-18 credits
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 750
                        elif 0< CREDITS < 12:
                            TUITION = 494*CREDITS + 21 +3    #tuition for nonresidential students with less than 12 credits
                            if CREDITS >=6:
                                TUITION = TUITION + 5
                            if INT_LOWER == 'yes':
                                TUITION = TUITION + 750
    elif RESIDENT_LOWER == 'yes':    #if resident
        LEVEL = input('Level—freshman, sophomore, junior, senior: ' ) #aks for college   
        LEVEL_LOWER = LEVEL.lower()
        while LEVEL_LOWER != 'freshman' and LEVEL_LOWER != 'sophomore' and LEVEL_LOWER != 'junior' and LEVEL_LOWER != 'senior':     #if a class is not identified, says input is invalid and asks again
            print('Invalid input. Try again.')
            LEVEL = input('Level—freshman, sophomore, junior, senior: ' )
            LEVEL_LOWER = LEVEL.lower()
        if LEVEL_LOWER == 'junior' or LEVEL_LOWER == 'senior':    #if junior or senior
            COLLEGE = input('Enter college as business, engineering, health, sciences, or none: ')    #enters college
            COLLEGE_LOWER = COLLEGE.lower()
            CMSE = input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ')    #asks if major is CMSE
            CMSE_LOWER = CMSE.lower()
            if COLLEGE_LOWER == 'business': #if in business school
                CREDITS = input('Credits: ')
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 8595 + 573*(CREDITS - 18) + 21 + 3 + 5 + 226    #tuition for a residental business student with 18+ credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                elif 12<= CREDITS <= 18:
                    TUITION = 8595 + 21 + 3 + 5 + 226    #tuition for a residental business student with 12-18 credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                elif 0< CREDITS < 12:
                    TUITION = 573*CREDITS + 21 + 3    #tuition for a residental business student with less than 12 credits
                    if CREDITS <= 4:
                        TUITION = TUITION + 113
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 + 226
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                    if CREDITS == 5:
                        TUITION = TUITION + 402            
            elif COLLEGE_LOWER == 'engineering':    #if in engineering college 
                CREDITS = input('Credits: ')
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 8595 + 573*(CREDITS - 18) + 21 + 3 + 5 + 670    #tuition for a residental engineering student with 18+ credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                elif 12<= CREDITS <= 18:
                    TUITION = 8595 + 21 + 3 + 5 + 670    #tuition for a residental engineering student with 12-18 credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                elif 0< CREDITS < 12:
                    TUITION = 573*CREDITS + 21 + 3    #tuition for a residental engineering student with less than 12 credits
                    if CREDITS <= 4:
                        TUITION = TUITION + 402
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 + 670
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                    if CREDITS == 5:
                        TUITION = TUITION + 670  
            elif COLLEGE_LOWER == 'health':    #if in health school
                CREDITS = input('Credits: ')
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 8325 + 555*(CREDITS - 18) + 21 + 3 + 5 + 100    #tuition for a residental health student with 18+ credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                elif 12<= CREDITS <= 18:
                    TUITION = 8325 + 21 + 3 + 5 + 100    #tuition for a residental health student with 12-18 credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670 
                elif 0< CREDITS < 12:
                    TUITION = 573*CREDITS +21 +3    #tuition for a residental health student with less than 12 credits
                    if CREDITS <= 4:
                        TUITION = TUITION + 50
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 + 100
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                    if CREDITS == 5:
                        TUITION = TUITION + 100          
            elif COLLEGE_LOWER == 'sciences':    #if in science college
                CREDITS = input('Credits: ')
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 8325 + 555*(CREDITS - 18) + 21 + 3 + 5 + 100    #tuition for a residental science student with 18+ credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670 
                elif 12<= CREDITS <= 18:
                    TUITION = 8325 + 21 + 3 + 5 + 100    #tuition for a residental science student with 12-18 credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                elif 0< CREDITS < 12:
                    TUITION = 573*CREDITS  +21 +3    #tuition for a residental science student with less than 12 credits
                    if CREDITS <= 4:
                        TUITION = TUITION + 50
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 + 100
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                    if CREDITS == 5:
                        TUITION = TUITION + 100  
            else:    #if no college specified 
                JM = input('Are you in the James Madison College (yes/no): ')    #asks if in James Madison
                JM_LOWER = JM.lower()
                CREDITS = input('Credits: ')
                while CREDITS.isdigit() == False or CREDITS == '0':
                    if '.' in CREDITS:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS.isdigit() == False:
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                    if CREDITS <= '0':
                        print('Invalid input. Try again.' )
                        CREDITS = input('Credits: ')
                CREDITS = int(CREDITS)
                if CREDITS > 18:
                    TUITION = 8325 + 555*(CREDITS - 18) + 21 + 3 + 5 + 100    #tuition for a residental James Madison student with 18+ credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                elif 12<= CREDITS <= 18:
                    TUITION = 8325 + 21 + 3 + 5 + 100    #tuition for a residental James Madison student with 12-18 credits
                    if CMSE_LOWER == 'yes':
                        TUITION = TUITION + 670
                elif 0< CREDITS < 12:
                    TUITION = 555*CREDITS + 21 + 3    #tuition for a residental James Madison student with less than 12 credits
                    if CREDITS <= 4:
                        TUITION = TUITION + 50
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 402
                    if CREDITS >= 6:
                        TUITION = TUITION + 5 
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
        elif  LEVEL_LOWER == 'freshman' or LEVEL_LOWER == 'sophomore':    #if class is freshman or sophomore  
            COE = input('Are you admitted to the College of Engineering (yes/no): ')    #asks if in college of engineering
            COE_LOWER = COE.lower()
            if COE_LOWER == 'yes':    #if in CoE
                if LEVEL_LOWER == 'freshman':    #if a freshman
                    CREDITS = input('Credits: ')    #input credits
                    while CREDITS.isdigit() == False or CREDITS == '0':
                        if '.' in CREDITS:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS.isdigit() == False:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS <= '0':
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                    CREDITS = int(CREDITS)
                    if CREDITS > 18:
                        TUITION = 7230 + 482*(CREDITS - 18) + 21 + 3 + 5 + 670    #tuition for a freshman residental engineering student with 18+ credits
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670 
                    elif 12<= CREDITS <= 18:
                        TUITION = 7230 + 21 + 3 + 5 + 670    #tuition for a freshman residental engineering student with 12-18 credits
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                    elif 0< CREDITS < 12:
                        TUITION = 482*CREDITS + 21 + 3    #tuition for a freshman residental engineering student with less than 12 credits
                        if CREDITS <= 4:
                            TUITION = TUITION + 402
                            if CMSE_LOWER == 'yes':
                                TUITION = TUITION + 402
                        if CREDITS >= 6:
                            TUITION = TUITION + 5 + 402
                            if CMSE_LOWER == 'yes':
                                TUITION = TUITION + 670
                elif LEVEL_LOWER == 'sophomore':   #if sophomore 
                   CREDITS = input('Credits: ')
                   while CREDITS.isdigit() == False or CREDITS == '0':
                        if '.' in CREDITS:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS.isdigit() == False:
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                        if CREDITS <= '0':
                            print('Invalid input. Try again.' )
                            CREDITS = input('Credits: ')
                   CREDITS = int(CREDITS)
                   if CREDITS > 18:
                        TUITION = 7410 + 494*(CREDITS - 18) + 21 + 3 + 5 + 670    #tuition for a sophomore residental engineering student with 18+ credits
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670 
                   elif 12<= CREDITS <= 18:
                        TUITION = 7410 + 21 + 3 + 5 + 670    #tuition for a sophomore residental engineering student with 12-18 credits
                        if CMSE_LOWER == 'yes':
                            TUITION = TUITION + 670
                   elif 0< CREDITS < 12:
                        TUITION = 494*CREDITS +21 +3    #tuition for a sophomore residental engineering student with less than 12 credits
                        if CREDITS <= 4:
                            TUITION = TUITION + 402
                            if CMSE_LOWER == 'yes':
                                TUITION = TUITION + 402
                        if CREDITS >= 6:
                            TUITION = TUITION + 5 + 402
                            if CMSE_LOWER == 'yes':
                                TUITION = TUITION + 670
            elif COE_LOWER == 'no':    #if not in CoE
                JM = input('Are you in the James Madison College (yes/no): ')    #asks if in James Madison 
                JM_LOWER = JM.lower()
                if JM_LOWER == 'yes':    #if in James Madison 
                    if LEVEL_LOWER == 'sophomore':    #if sophomore
                        CREDITS = input('Credits: ')
                        while CREDITS.isdigit() == False or CREDITS == '0':
                            if '.' in CREDITS:
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                            if CREDITS.isdigit() == False:
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                            if CREDITS <= '0':
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                        CREDITS = int(CREDITS)
                        if CREDITS > 18:
                            TUITION = 7410 + 494*(CREDITS - 18) + 21 + 3 + 5 + 7.5    #tuition for a sophomore residental James Madison student with 18+ credits
                        elif 12<= CREDITS <= 18:
                            TUITION = 7410 + 21 + 3 + 5 + 7.5    #tuition for a sophomore residental James Madison student with 12-18 credits
                        elif 0< CREDITS < 12:
                            TUITION = 494*CREDITS + 21 +3 + 7.5    #tuition for a sophomore residental James Madison student with less than 12 credits
                            if CREDITS >=6:
                                TUITION = TUITION + 5
                    if LEVEL_LOWER == 'freshman':    #if freshman
                        CREDITS = int(input('Credits: '))
                        if CREDITS > 18:
                            TUITION = 7230 + 482*(CREDITS - 18) + 21 + 3 + 5 + 7.5    #tuition for a freshman residental James Madison student with 18+ credits
                        elif 12<= CREDITS <= 18:
                            TUITION = 7230 + 21 + 3 + 5 + 7.5    #tuition for a freshman residental James Madison student with 12-18 credits
                        elif 0< CREDITS < 12:
                            TUITION = 482*CREDITS + 21 +3 + 7.5    #tuition for a freshman residental James Madison student with less than 12 credits
                            if CREDITS >=6:
                                TUITION = TUITION + 5
                else:     # if not in James Madison
                    if LEVEL_LOWER == 'freshman':    #if freshman
                        CREDITS = input('Credits: ')
                        while CREDITS.isdigit() == False or CREDITS == '0':
                            if '.' in CREDITS:
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                            if CREDITS.isdigit() == False:
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                            if CREDITS <= '0':
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                        CREDITS = int(CREDITS)
                        if CREDITS > 18:
                            TUITION = 7230 + 482*(CREDITS - 18) + 21 + 3 + 5 #tuition for a freshman residental student with 18+ credits
                        elif 12<= CREDITS <= 18:
                            TUITION = 7230 + 21 + 3 + 5    #tuition for a freshman residental student with 12-18 credits
                        elif 0< CREDITS < 12:
                            TUITION = 482*CREDITS + 21 +3     #tuition for a freshman residental student with less than 12 credits
                            if CREDITS >=6:
                                TUITION = TUITION + 5
                    elif LEVEL_LOWER == 'sophomore':    #if sophomore
                        CREDITS = input('Credits: ')
                        while CREDITS.isdigit() == False or CREDITS == '0':
                            if '.' in CREDITS:
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                            if CREDITS.isdigit() == False:
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                            if CREDITS <= '0':
                                print('Invalid input. Try again.' )
                                CREDITS = input('Credits: ')
                        CREDITS = int(CREDITS)
                        if CREDITS > 18:
                            TUITION = 7410 + 494*(CREDITS - 18) + 21 + 3 + 5     #tuition for a sophomore residental student with 18+ credits
                        elif 12<= CREDITS <= 18:
                            TUITION = 7410 + 21 + 3 + 5     #tuition for a sophomore residental student with 12-18 credits
                        elif 0< CREDITS < 12:
                            TUITION = 494*CREDITS + 21 +3     #tuition for a sophomore residental student with less than 12 credits
                            if CREDITS >=6:
                                TUITION = TUITION + 5   
    TUITION = float(TUITION)    #turns tuition into a float
    print('Tuition is ${:,.2f}'.format(TUITION)+'.')    #prints tuition 
    ANS = input('Do you want to do another calculation (yes/no): ')    #asks if user would like to do a calculation again
    

