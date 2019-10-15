###########################################################
    #  Computer Project #1
    #
    #    prompt for a number of rods
    #    input an integer for RODS
    #    turns rod int to float 
    #    convert rods to METERS and rounds to 3rd decimal 
    #    converts METERS to FEET, MIlES, FURLONGS to the 3rd decimal.
    #    convert MILES to hours and then MINUTES
    #    display values of RODS, METERS, FEET, MILES, and MINUTES to walk
    ###########################################################
RODS = input("Input rods: ")
RODS_FLOAT = float(RODS)
print("You input " + str(RODS_FLOAT) + " rods.")
print(' ')

print("Conversions")

METERS = RODS_FLOAT * 5.0292
METERS_ROUND = round(METERS,3)
print("Meters: " + str(METERS_ROUND))

FEET = (METERS/0.3048)
FEET = round(FEET,3)
print("Feet: " + str(FEET))

MILES = ( METERS/1609.34)
MILES_ROUND = round(MILES, 3)
print("Miles: " + str(MILES_ROUND))

FURLONGS = round((RODS_FLOAT/40.0),3)
print("Furlongs: " + str(FURLONGS))

MINUTES = ((MILES/3.1)*60)
MINUTES_ROUND = round(MINUTES,3)
print("Minutes to walk " + str(RODS_FLOAT) + " rods: " + str(MINUTES_ROUND))