##########
# Computer project 06 
#
# Lists & data analysis 
#
# basic analysis of web search data
# prompts user for .csv file
# user chooses from list of prompts what to do
# 1. displays top 20 sites by country with traffic rank and average daily page views
# 2. asks user for key word then finds all websites with keyword in it
# 3. shows the top 20 sites by average daily page views in descending order 
# end program
#
#########
import csv
from operator import itemgetter

PROMPT = '''
Choose
         (1) Top sites by country
         (2) Search by web site name
         (3) Top sites by views
         (q) Quit
'''

def open_file():
    '''
    this function ccontinuously prompts the user for a file name and returns the
    file.
    '''
    valid_file = False
    while valid_file == False:
        file = input("Input a filename: ")    #prompts for file name
        try:
            fp = open(file, encoding='ISO-8859-1')    #open file
            valid_file = True
        except FileNotFoundError:
            print("Error: file not found.")
            valid_file = False    #keeps loop going
    return fp

def read_file(fp):
    '''
    This function takes in a file and opens the reader for a csv file. It then 
    extracts each line, that has no missing data, of the csv file into a list 
    and then creates tuples for each row. Then takes that list and extracts the 
    country rank, website, global rank, average daily page views, and country
    into a tuple and returns a list of those tupples ranked by country rank and 
    country.
    '''
    reader = csv.reader(fp)    #reads through the csv file
    line_list = []    #list of every line from csv file stored as tuples
    info_list = []    #list of every valid line from csv file holding each line's
    i=0               # country rank, website, global rank, average daily page views, country
    next(reader)    #skips header
    for line in reader:
        line_list.append(line)    #adds every line of file to list
    while i < len(line_list):
        rank = int(line_list[i][0])    #country rank
        website = line_list[i][1]    #website url
        traffic = line_list[i][14].replace(' ','')    #global (traffic) rank
        page_views = line_list[i][5].replace(' ','')    #avrg daily page views
        country = line_list[i][30]    #country
        tup = (rank, website, traffic, page_views, country)
        if 'N/A' in tup:   #skips line if there is information missing
            i += 1
        else:
            tup = (rank, website, int(traffic), int(page_views), country)
            info_list.append(tup)    #adds tuple to info list
            i +=1
    info_list.sort(key=itemgetter(0, 4))    #sorts by country rank and country
    return info_list

def remove_duplicate_sites(L_of_L):
    '''
    This function takes a list of tuples and removes duplicate sites from the list
    and returns the list.
    '''
    master_list = []    #list holds first refrence of website
    names_list = []    #list of domain names 
    line = L_of_L
    i = 0
    while i < len(L_of_L):
        rank = line[i][0]
        traffic = line[i][2]
        page_views = line[i][3]
        country = line[i][4]
        website = line[i][1].split('.')    #splits website at . into list of 3/4 strings
        www = website[0]    #www of website url
        domain_name = website[1]    #domain name
        ending = website[2:]
        if domain_name in names_list:
            i += 1    #do nothing if domain is already in name list
        else:
            names_list.append(domain_name)    #add name to name list
            try:
                url = www +'.' + domain_name + '.' + ending[0] + '.'+ ending[1]    #if ending is 2 parts
            except:
                url = www +'.' + domain_name + '.' + ending[0]    #if ending it 1 part
            new_tup = (rank, url, traffic, page_views, country)
            master_list.append(new_tup)    #stores first instance of website
            i += 1
    master_list.sort(key=itemgetter(0, 1))    #sorts by country rank and website
    return master_list

def top_sites_per_country(L_of_L,country):
    '''
    This function takes in a list of tuples and a country and returns the top 20
    sites for that country.
    '''
    top_20_sites = []    #list of top 20 sites for country
    for tup in L_of_L:
        if len(top_20_sites) < 20:    #store first 20 values
            if tup[4] == country:
                top_20_sites.append(tup)    #adds tup to top 20 list
    return top_20_sites

def top_sites_per_views(L_of_L):
    '''
    This function take in a list of tuples and returns the top 20 sites ranked
    by page views in descending.
    '''
    total_list_sorted = L_of_L 
    total_list_sorted.sort(key=itemgetter(3), reverse = True)    #descending order of list sorted by average daily page views
    dup_free = remove_duplicate_sites(total_list_sorted)    #removes duplicate websites
    dup_free.sort(key=itemgetter(3), reverse = True)    
    top_20_views = dup_free[:20]    
    return top_20_views

def main():
    '''
    This function prompts the user to select from 3 options. It will ask for a
    file to open and then display a list of options to choose. it will loop asking 
    the user for a choice 1,2,3,'q'(case insensitive). q will end the program.
    1. displays top 20 sites by country with traffic rank and average daily page views
    2. asks user for key word then finds all websites with keyword in it
    3. shows the top 20 sites by average daily page views in descending order  
    '''
    print("----- Web Data -----")
    fp = open_file()  
    L_of_L = read_file(fp)
    print(PROMPT)
    choice = input('Choice: ').lower()    #choice is always a lower case q if q is entered
    while choice != 'q':
        if choice == '1':
            print("--------- Top 20 by Country -----------")
            country = input("Country: ")    #prompts for a country
            print('{:<30s} {:>16s}{:>30s}'.format("Website","Traffic Rank","Average Daily Page Views" ))
            i = 0
            top_20_sites = top_sites_per_country(L_of_L, country)
            while i < len(top_20_sites):
                print(" {:30s} {:>15d}{:>30,d}".format(top_20_sites[i][1],top_20_sites[i][2],top_20_sites[i][3]))
                i+=1    #prints the top 20 sites with their global rank and average daily page views
            print(PROMPT)
            choice = input('Choice: ').lower()
        elif choice == '2':
            keyword = input("Search: ").lower()    #always turnss keyword into lowercase
            print("{:^50s}".format("Websites Matching Query"))
            i = 0
            common = 0    #counter of websites with keyword in name
            while i < len(L_of_L):
                if keyword in L_of_L[i][1]:
                    print("{:<10s}" .format(L_of_L[i][1]))
                    common += 1
                    i += 1
                else:
                    i +=1    #skip tuple
            if common == 0:    #if nothing is found
                print("None found")
            print(PROMPT)
            choice = input('Choice: ').lower()
        elif choice == '3':
            top_20 = top_sites_per_views(L_of_L)
            print("--------- Top 20 by Page View -----------")
            print("{:30s} {:>20s}".format("Website", "Ave Daily Page Views"))
            for tup in top_20:
                print("{:30s} {:>20,d}".format(tup[1], tup[3]))
            print(PROMPT)
            choice = input('Choice: ').lower()
        else:    #if choice isnt 'q' or 1,2,3
            print("Incorrect input. Try again.")
            print(PROMPT)
            choice = input('Choice: ').lower()

if __name__ == "__main__":
     main()