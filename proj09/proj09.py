# =============================================================================
# Computer Project 09
# 
# This program analyzes data relevant to the biggest cybersecurity breaches in 
# the past.
#
# Prompts the user for a choice to select from the menu and completes the task 
# described in the menu. 
# =============================================================================

import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

def open_file(message):
    '''
    This function takes in a prompt message and displayes the correct message and 
    returns a file pointer. Will repeatedly ask until a successful one is opened.
    '''
    valid = False
    while valid == False:
        file = input(message)
        if file == '':
            fp = open('breachdata.csv','r', encoding = 'utf-8')
            valid = True
        else:
            try:
                fp = open(file, 'r', encoding = "utf-8")
                valid = True
            except FileNotFoundError:
                print('[ - ] File not found. Try again.')
                valid = False
    return fp
    
    
def build_dict(reader):
    '''
    This function takes in a CSV reader and extracts the entity, records lost(int),
    year(int), story, sector, method, and the news sources(list) from each line.
    Makes sure that all pieces of data are valid and then makes two dictionaries.
    The first dictionary has a key(entity) and a tuple as a value (records lost, 
    year, story, news sources). The second dictionary has a key(year) and a tuple
    as its value (sector, method). This function returns a master dictionary with
    a key(entity) and a list of tuples of the two dictionaries made.
    '''
    master_dict = {}
    next(reader)
    for line in reader:
        D1 ={}
        D2 = {}
        entity = str(line[0].strip())
        try:
            records_lost = int(line[2].replace(',',''))
        except ValueError:    #if cannot turn value into int, gives it value 0
            records_lost = 0
        try:
            year = int(line[3])
        except ValueError:    #if cannot turn value into int, passes line
            continue
        story = line[4]
        sector = line[5]
        method = line[6]
        if ',' in line[11]:
            news_sources = line[11].split(',')    #splits if multiple news sources
        elif len(line[11]) == 0:
            continue    #if no news sources, skip line
        else:
            news_sources = [line[11]]
        D1[entity] = (records_lost, year, story, news_sources)
        D2[year] = (sector, method)
        if entity in master_dict:
            master_dict[entity].append((D1,D2))    #adds to list if in dictionary
        else:
            master_dict[entity] = [(D1, D2)]    #starts list if not in the dictionary 
    return master_dict

def top_rec_lost_by_entity(dictionary):
    '''
    This function takes in the breach dictionary and returns a list of the top 10
    entities that lost the most records.
    '''
    L = []
    for key, value in dictionary.items():
        total = 0
        i = 0
        while i < len(value):    #if there are multiple values in the list
            records_lost = value[i][0][key][0]
            total += records_lost    #adds all records lost in entity
            i += 1
        L.append((key, total))
    L.sort(key=itemgetter(1, 0), reverse = True)    #sorts in descending order by records lost
    return L[:10]    #returns the top 10 


def records_lost_by_year(dictionary):
    '''
    This function takes in the breach dictionary and returns a list of total records
    lost within each year. 
    '''
    L = []
    D = {}
    for key, value in dictionary.items():
        total = 0
        i = 0
        while i < len(value):
            records_lost = value[i][0][key][0]
            year = value[i][0][key][1]
            i += 1
            if year in D:    #if the year is a key in dictionary
                D[year] += records_lost    #adds records lost if year is already created
            else:
                D[year] = records_lost    #makes dictionary with year and records lost
    for year, total in D.items():
        L.append((year,total))    #adds tuple to list
    L.sort(key=itemgetter(1), reverse = True)    #sorts list in descending lost records order
    return L

def top_methods_by_sector(dictionary):
    '''
    This function takes in the breach dictionary and returns a dictionary of dictionaries.
    sorts through the dictionary and adds the sector and method to as list. Then 
    sorts the list in alphabetical order of the sector. Then makes a dictionary 
    with the sector and the count of the method.
    '''
    L = []
    D = {}
    for key, value in dictionary.items():
        for index in value:    #for each value in list
            for Dict in index:    #for each dictionary at each index
                for key, values in Dict.items():
                    if str(key).isdigit() == True:    #if the key is a year
                        L.append(values)    #append sector/method to list
    L.sort(key=itemgetter(0))    #sorts list by sector
    for tup in L:
        sector = tup[0]
        method = tup[1]
        if sector not in D:    
            D[sector]= {}    #starts nested dictionary
            D[sector][method] = 1    #starts count of method
        elif sector in D:
            if method in D[sector]:
                D[sector][method] += 1    #adds to method count if in sector
            else:
                D[sector][method] = 1    #starts method count if not in sector
    return D

        
def top_rec_lost_plot(names,records):
    ''' Plots a bargraph pertaining to
        the cybersecurity breaches data '''
        
    y_pos = np.arange(len(names))

    plt.bar(y_pos, records, align='center', alpha=0.5,
            color='blue',edgecolor='black')
    plt.xticks(y_pos, names, rotation=90)
    plt.ylabel('#Records lost')
    plt.title('Cybersecurity Breaches',fontsize=20)
    plt.show()
    
def top_methods_by_sector_plot(methods_list):
    ''' Plots the top methods used to compromise
        the security of a sector '''
    methods = [] ; quantities = []
    for tup in methods_list:
        methods.append(tup[0])
        quantities.append(tup[1])
    labels = methods
    sizes = quantities
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors = colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    
    plt.axis('equal')
    plt.show()
    
def main():
    '''
    This function is the starting point of the program. It prompts the user with 
    the banner and menu then prompts the user for a choice 1-5. Thens prompts
    for a file. Displays the top 10 entities that lost records if option 1 is
    chosen. If option 2 is selected, the program calculates the records lost in 
    each year and displays the results in descending order. At the end of option 1/2
    the program asks user if they would like to plot on a bar graph. If option 3
    is selected, the program calculates the top methods being used for breaching
    for the sector inputed by the user. Then displays the methods in decreasing 
    order. Asks user to plot after. If option is 4, the program asks for an entity
    and returns and displays all stories for the desired entity. If option 5 is 
    selected, the program ends. If an invalid choice is inputed, an error message
    is displayed and user is asked to input another option.
    '''
    BANNER = '''
    
                 _,.-------.,_
             ,;~'             '~;, 
           ,;                     ;,
          ;                         ;
         ,'                         ',
        ,;                           ;,
        ; ;      .           .      ; ;
        | ;   ______       ______   ; | 
        |  `/~"     ~" . "~     "~\'  |
        |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
         |   |        }:{        |   | 
         |   l       / | \       !   |
         .~  (__,.--" .^. "--.,__)  ~. 
         |     ---;' / | \ `;---     |  
          \__.       \/^\/       .__/  
           V| \                 / |V  
            | |T~\___!___!___/~T| |  
            | |`IIII_I_I_I_IIII'| |  
            |  \,III I I I III,/  |  
             \   `~~~~~~~~~~'    /
               \   .       .   /
                 \.    ^    ./   
                   ^~~~^~~~^ 
                   
           
           ~~Cybersecurity Breaches~~        
                   @amirootyet    
                
    '''
    
    print(BANNER)
    
    MENU = '''  
[ 1 ] Most records lost by entities
[ 2 ] Records lost by year
[ 3 ] Top methods per sector
[ 4 ] Search stories
[ 5 ] Exit'''
    print(MENU)
    choice = input('[ ? ] Choice: ')    #prompts user for choice
    
    if choice in '1234':    #build dict for first time asking & choice is valid
        fp = open_file("[ ? ] Enter the file name: ")
        reader = csv.reader(fp)
        breach_dict = build_dict(reader)
    else:    #first time asking for choice and not valid choice
        while choice not in '12345':
            print('[ - ] Incorrect input. Try again.')
            print(MENU)
            choice = input('[ ? ] Choice: ')
        if choice in '1234':    #builds dict for program if choice is valid and not exiting
            fp = open_file("[ ? ] Enter the file name: ")
            reader = csv.reader(fp)
            breach_dict = build_dict(reader)
        
    while choice != '5':
        if choice == '1':
            print("[ + ] Most records lost by entities...")
            top_10 = top_rec_lost_by_entity(breach_dict)
            for values in top_10:    #displays top 10 entities with most records lost & ranking
                entity, records_lost = values[0], values[1]
                print("-"*45)
                print("[ {:2d} ] | {:15.10s} | {:10d}".format((top_10.index(values)+1) ,entity,records_lost))
                
            plot = input("[ ? ] Plot (y/n)? " )
            if plot == 'y':
                names = []
                records = []
                for value in top_10:
                    name,records_lost = value[0],value[1]
                    names.append(name)    #adds entity name to name list
                    records.append(records_lost)    #adds records lost to a records list
                top_rec_lost_plot(names,records)    #plots data in bar graph
                print(MENU)
                choice = input('[ ? ] Choice: ')
            else:
                print(MENU)
                choice = input('[ ? ] Choice: ')
                
        elif choice == '2':
            print("[ + ] Most records lost in a year...")
            year_list = records_lost_by_year(breach_dict)
            for tup in year_list:    #displays records lost per year in descending order w/ rank
                year, records_lost = str(tup[0]), tup[1]
                print("-"*45)
                print('[ {:2d} ] | {:15.10s} | {:10d}'.format((year_list.index(tup)+1) ,year,records_lost))
            plot = input("[ ? ] Plot (y/n)? " )
            if plot == 'y':
                years = []
                records = []
                for value in year_list:
                    year, records_lost = value[0], value[1]
                    years.append(year)    #adds year to a year list
                    records.append(records_lost)    #adds records lost to a records list
                top_rec_lost_plot(years,records)
                print(MENU)
                choice = input('[ ? ] Choice: ')
            else:
                print(MENU)
                choice = input('[ ? ] Choice: ')
                
        elif choice == '3':
            print("[ + ] Loaded sector data.")
            sectors_dict = top_methods_by_sector(breach_dict)    #builds sectors w/ methods dictionary
            sector_list = []
            methods_list = []
            for sector in sectors_dict:
                sector_list.append(sector)    #adds sectors to a list
            print(*sector_list, sep=' ')    #prints all sectors separated by a space
            sector_valid = False
            while sector_valid == False:    #makes sure user enters valid sector
                user_sector = input("[ ? ] Sector (case sensitive)? ")
                if user_sector in sector_list:
                    sector_valid = True
                else:
                    print("[ - ] Invalid sector name. Try again.")
                    sector_valid = False
            for method, count in sectors_dict[user_sector].items():
                methods_list.append((method, count))    #adds method/count to list
            methods_list.sort(key=itemgetter(1), reverse = True)   #sorts by count
            print("[ + ] Top methods in sector {}".format(user_sector))
            for tup in methods_list:    #diplays methods/counts w/ rank in descending order
                method, count = tup[0], tup[1]
                print("-"*45)
                print('[ {:2d} ] | {:15.10s} | {:10d}'.format((methods_list.index(tup)+1) ,method,count))
            plot = input("[ ? ] Plot (y/n)? " )    
            if plot == 'y':
                top_methods_by_sector_plot(methods_list)    #plots methods by sector
                print(MENU)
                choice = input('[ ? ] Choice: ')
            else:
                print(MENU)
                choice = input('[ ? ] Choice: ')
        
        elif choice == '4':
            story_list = []
            valid_entity = False
            while valid_entity == False:    #makes sure entity is valid
                user_entity = input("[ ? ] Name of the entity (case sensitive)? ")
                if user_entity in breach_dict:
                    valid_entity = True
                else:
                    print("[ - ] Entity not found. Try again.")
                    valid_entity = False
            for tup in breach_dict[user_entity]:
                story = tup[0][user_entity][2]
                story_list.append(story)    #adds each story to list
            print("[ + ] Found {} stories:".format(len(story_list)))
            for story in story_list:    #prints each story w/ order
                print("[ + ] Story {}: {:10s}".format(story_list.index(story)+1, story))
            print(MENU)
            choice = input('[ ? ] Choice: ')
        else:
            print('[ - ] Incorrect input. Try again.')
            choice = input('[ ? ] Choice: ')
    print("[ + ] Done. Exiting now...")
if __name__ == "__main__":
     main()