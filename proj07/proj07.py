# =============================================================================
# Computer Project 07 (List and Tuples and File Manipulation)
# 
# prompt user for a travel data file and a country code file
# display options that user can do with data
# can show data by year
# can show data by country  
# can show all country code names
# ends program with exit message
# =============================================================================

import matplotlib.pyplot as plt
import csv
from operator import itemgetter

MIN_YEAR = 2009
MAX_YEAR = 2017

def open_file(prompt_str):
    '''
    This function takes in a prompt string and returns a file pointer. 
    the prompt string is used to display the correct prompt for the correct file.
    it will keep asking until a valid file if given.
    '''
    valid = False
    while valid == False:
        file = input(prompt_str)
        try:
            fp = open(file, 'r', encoding = "utf-8")
            valid = True
        except FileNotFoundError:
            print("File not found! Try Again!")
            valid = False
    return fp
            
def read_travel_file(fp):
    '''
    This function takes a file pointer and returns a list of list of tuples, each
    corrisponding to a year.  each tupple contains the year, country, country code,
    # of departures/arrivals, expenditures, receipts, and average expenditure per
    departures and average receipt per arrival. 
    '''
    i = 0   
    data_list = [[],[],[],[],[],[],[],[],[]]
    reader = csv.reader(fp)
    next(reader)
    for line in reader:
        year = int(line[0])
        country = line[1][:20]
        country_code = line[2]
        num_departures = int(line[3])
        num_arrivals = int(line[4])
        expenditures = float(line[5])
        receipts = float(line[6]) 
        
        try:
            num_departures = num_departures / 1000    
            expenditures = expenditures / 1000000
            avrg_expenditures = (expenditures/ num_departures) * 1000
            avrg_expenditures = round(avrg_expenditures, 2)
        except ZeroDivisionError:
            avrg_expenditures = 0    #if 0 is in the denominator, the value is 0
            
        try:
            num_arrivals = num_arrivals / 1000
            receipts = receipts / 1000000
            avrg_receipts = (receipts / num_arrivals) * 1000
            avrg_receipts= round(avrg_receipts, 2)
        except ZeroDivisionError:
            avrg_receipts = 0    #if 0 is in the denominator, the value is 0
            #tuple containint all the desired information
        info = (year, country, country_code, num_arrivals, num_departures, \
                expenditures, receipts, avrg_expenditures, avrg_receipts)
        data_list[year - 2009].append(info)    #append the tuple to the specific year
                                               #index
    while i < len(data_list):
        data_list[i].sort(key = itemgetter(1))    #sorts each year of data by country
        i +=1
    return data_list    #returns the sorted list
        
def read_country_code_file(fp):
    '''
    This function takes in a file pointer for country codes and returns a list
    of tuples containg all the country codes and their corresponding countries
    '''
    country_code_list = []
    fp.readline()
    for line in fp:
        country_code, country =line.strip().split('/')    #splits at / and removes 
                                                        #white space
        country_code_list.append((country_code,country)) #adds the information to list
    country_code_list.sort(key=itemgetter(0))    #sorts list by country code
    return country_code_list

def get_country_code_data(country_code, data_list):
    '''
    This function takes in the country code and data list and returns a list of 
    each year of data for that country. 
    '''
    country_list = []    #specified country list
    for year in data_list:    
        for tup in year:  
            code = tup[2]
            if code == country_code:    
                country_list.append(tup)    #append the tuple if it has the same 
                                                #country code as requested
    if len(country_list) == 0:
        return None    #no inromation for the country, return None
    else:
        return country_list

def display_country_data(country_list):
    '''
    This function takes in the country list from the function above and displays 
    the information in that list. It also adds up all the departures/arrivals/expenditures/receipts
    and displays those as well. 
    '''
    total_departures=0
    total_arrivals=0
    total_expenditures=0
    total_receipts=0
    # Get the country name from the list
    country_name = country_list[0][1]
    
    # Print table title
    title = "Travel Data for {}".format(country_name)
    print("\n{:^80s}".format(title))
    
    # Table headers
    header = ['Year', 'Departures','Arrivals','Expenditures', 'Receipts']
    units = ['','(thousands)','(thousands)','(millions)','(millions)']
    #     header string formatting
    print('{:6s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(header[0],header[1],\
          header[2],header[3],header[4]))
    print('{:6s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(units[0],units[1],\
          units[2],units[3],units[4]))
    for year in country_list:
        year_value = year[0]     #extracts desired values value from tuple
        arrivals = year[3]
        departures = year[4]
        expenditures = year[5]
        receipts = year[6]
        total_departures += departures    #adds each desired value to a total counter
        total_arrivals += arrivals
        total_expenditures += expenditures
        total_receipts += receipts
        # Numeric values string formatting
        print('{:<6d}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format(year_value,\
              departures,arrivals,expenditures,receipts))    
    # Numeric values string formatting for total
    print(' ')
    print('{:<6s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format('Total', \
          total_departures,total_arrivals,total_expenditures,total_receipts))

def display_year_data(year_list):
    '''
    This function takes in the year list from the function above and displays 
    the information in that list. It also adds up all the departures/arrivals/expenditures/receipts
    and displays those as well.
    '''
    total_departures=0
    total_arrivals=0
    total_expenditures=0
    total_receipts=0
    # Get the year from the list
    year = year_list[0][0]
    
    # Print table title
    title = "Travel Data for {:d}".format(year)
    print("\n{:^80s}".format(title))
    
    # Table headers
    header = ['Country Name', 'Departures','Arrivals','Expenditures',\
              'Receipts']
    units = ['','(thousands)','(thousands)','(millions)','(millions)']
    
    # header string formatting
    print('{:25s}{:15s}{:15s}{:15s}{:15s}'.format(header[0],header[1],header[2]\
          ,header[3],header[4]))
    print('{:25s}{:15s}{:15s}{:15s}{:15s}'.format(units[0],units[1],units[2],\
          units[3],units[4]))
    for tup in year_list:
        country = tup[1]     #extracts desired values value from tuple    
        arrivals = tup[3]
        departures = tup[4]
        expenditures = tup[5]
        receipts = tup[6]
        total_departures += departures    #adds each desired value to a total counter
        total_arrivals += arrivals
        total_expenditures += expenditures
        total_receipts += receipts
    # Rows string formatting
        print( '{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format(country,\
              departures,arrivals,expenditures,receipts))
    # Numeric values string formatting for total
    print(' ')
    print('{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}'.format('Total',\
          total_departures,total_arrivals,total_expenditures,total_receipts))


def prepare_bar_plot(year_list):
    '''
     This function takes in the year list and returns the top 20  average expenditure/receipt
     countries. 
    '''
    expenditure_list = []
    receipt_list = []
    for tup in year_list:    #first loop to have just country and averge expenditure
                            #added to a list
        country = tup[1]
        average_expenditures = tup[7]
        tup = (country, average_expenditures)
        expenditure_list.append(tup)
    expenditure_list.sort(key=itemgetter(1), reverse = True)    #sorts list in reverse 
    top_20_expenditures = expenditure_list[:20]    #takes top 20 from list
    for tup in year_list:    #second loop to have country and average receipt added to list
        country = tup[1]
        average_receipt = tup[8]
        tup = (country, average_receipt)
        receipt_list.append(tup)
    receipt_list.sort(key=itemgetter(1), reverse = True)
    top_20_receipt = receipt_list[:20]
    return top_20_expenditures, top_20_receipt
    
def prepare_line_plot(country_list):
    '''
    This function takes in a country list and returns a list of the average expenditure
    and a list of the average receipt in the order presented.
    '''
    expenditure_list = []
    receipt_list = []
    for tup in country_list:
        average_expenditure = tup[7]
        expenditure_list.append(average_expenditure)
        average_receipt = tup[8]
        receipt_list.append(average_receipt)
    return expenditure_list, receipt_list

def plot_bar_data(expend_list, receipt_list, year):
    '''
        This function plots the the top 20 countries with the highest average
        expenditures and the top 20 countries with the highest receipts.
        
        Returns: None
    
    '''

    # prepare the columns
    countries_expend = [elem[0] for elem in expend_list]
    values_expend = [elem[1] for elem in expend_list]
    
    countries_receipt = [elem[0] for elem in receipt_list]
    values_receipt = [elem[1] for elem in receipt_list]
    
    # Average expenditures
    
    x = range(20) # top 20 countries are to be plotted.

    fig, axs = plt.subplots(2, 1,figsize=(7,10))
    title = "Top 20 countries with highest average expenditures {:4d}".format(year)
    axs[0].set_title(title)
    axs[0].bar(x, values_expend, width=0.4, color='b')
    axs[0].set_ylabel("Avg. Expenditures (US dollar)")
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(countries_expend , rotation='90')
    
    # Average receipt
    title = "Top 20 countries with highest average receipt  {:4d}".format(year)
    axs[1].set_title(title)
    axs[1].set_ylabel("Avg. Receipts (US dollar)")
    axs[1].bar(x, values_receipt, width=0.4, color='b')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(countries_receipt , rotation='90')
    fig.tight_layout()
#    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
    fig.savefig('avg_expense_receipts.png',dpi=100)
    fig.clf()


def plot_line_data(country_code, expend_list, receipt_list):
    '''
        Plot the line plot for the expenditures and receipts for the
        country between 2009 and 2017
        
        Returns: None
    '''
    
    
    title = "Average expenditures and receipts for {} between 2009 and 2017".format(country_code)
    years = range(MIN_YEAR, MAX_YEAR+1)
    fig, axs = plt.subplots(figsize=(7,5))
    axs.set_title(title)
    axs.set_ylabel("Cost (US dollar)")
    axs.plot(years, expend_list, years, receipt_list)
    axs.legend(['Expenditures','Receipt'])

#    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
    fig.savefig('line.png',dpi=100)
    fig.clf()

def main():
    '''
    This function is the starting point of the program. Its prompts the user to 
    open a travel data file and a country codes file and then displays a list of
    options the user can choose. Ends program when user tells it to and displays
    exit prompt.
    '''
    
    BANNER = "International Travel Data Viewer\
    \n\nThis program reads and displays departures, arrivals, expenditures,"\
    " and receipts for international travels made between 2009 and 2017."
    
    # Prompt for option
    OPTION = "Menu\
    \n\t1: Display data by year\
    \n\t2: Display data by country\
    \n\t3: Display country codes\
    \n\t4: Stop the Program"
#    \n\n\tEnter option number: "

    print(BANNER)
    travel_data_file = open_file('Enter the travel data file: ')
    data_list = read_travel_file(travel_data_file)    #ges data list for program
    
    country_code_file = open_file("Enter the country code file: ")
    country_code_list = read_country_code_file(country_code_file)    #gets country codes for the program
    codes_list = []
    for tup in country_code_list:
        codes_list.append(tup[0])    #adds country codes to codes list
    
    print(OPTION)
    
    option = input('\t\tEnter option number: ')
    while option != '4':
        if option == '1':
            valid = False
            while valid == False:    #loop to make sure year is a valid year
                year = int(input("Enter year: "))
                if year < MIN_YEAR:
                    print("Year needs to be between 2009 and 2017. Try Again!")
                    valid = False
                elif year > MAX_YEAR:
                    print("Year needs to be between 2009 and 2017. Try Again!")
                    valid = False
                else:
                    valid = True    #year is valid, break loop
            index = year - 2009    #finds index in data list
            year_list = data_list[index]    #list of all data for year
            display_year_data(year_list)
            plot = input("Do you want to plot (yes/no)? ").lower()
            if plot != 'yes':    #dont want to plot
                print(OPTION)
                option = input('\t\tEnter option number: ')
            else:
                expend_list, receipt_list = prepare_bar_plot(year_list)
                plot_bar_data(expend_list, receipt_list, year)
                print(OPTION)
                option = input('\t\tEnter option number: ')
                
        elif option == '2':
            valid_code = False
            while valid_code == False:    #makes sure user enters a valid country code
                user_country = input("Enter country code: ").upper()
                if user_country in codes_list:
                    valid_code = True    # if country code is valid, break loop
                else:
                    print("Country code is not found! Try Again!")
                    valid_code = False
            
            country_list = get_country_code_data(user_country, data_list)    #gets yearly data for country
            display_country_data(country_list)
            plot = input("Do you want to plot (yes/no)? ").lower()
            if plot != 'yes':
                print(OPTION)
                option = input('\t\tEnter option number: ')
            else:
                expend_list, receipt_list = prepare_line_plot(country_list)
                plot_line_data(user_country, expend_list, receipt_list)
                print(OPTION)
                option = input('\t\tEnter option number: ')
        elif option == '3':
            print('\nCountry Code Reference')
            print('{:15}{:25}'.format('Country Code', 'Country Name'))
            for tup in country_code_list:    #prints every country code and country
                print('{:15}{:25}'.format(tup[0],tup[1]))
            print(OPTION)
            option = input('\t\tEnter option number: ')
        else:    #if choice is not a number 1-4
            print("Invalid option. Try Again!")
            print(OPTION)
            option = input('\t\tEnter option number: ')
            
    print("\nThanks for using this program!")
        
if __name__ == "__main__":
    main()






