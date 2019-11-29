###############################################################################################
#   gatterbzinfo.py v 0.7 (random number lol)
#   author: Federico E. Benelli aka Ruther
#   
#   This is a work in progress program, that will gatter all the data from different
#   ODF files form Battlezone and then generate json and xlsx files with the gattered data
#
#   As for now, the gatter of data for ordinances and guns is fully automated, but still 
#   some polish needs to be done since the result file is kinda messy.
#
#   Since it's better standarized, vehicle data is easier to gatter and right now
#
#   I'm not familiar with BZ2/BZCC ODF files,
#   but I guess they have similar format so it could be used there, too
###############################################################################################

import os
import json
import pandas as pd

ordinances = {}

guns = {}

vehicles = {}

# List of guns characteristics to gatter
# right now the script will consider as a
# gun file any odf that has any of this 
# characteristics, more desired characteristics
# to be gattered can be added to the list 
# non-desired data can be substracted from the list
gunsCharacteristics = ["wpnName",
                       "ordName",
                       "fireSound",
                       "wpnReticle",
                       "wpnPriority",
                       "wpnCategory",
                       "shotDelay"]

# List of ordinance characteristics to gatter
# right now the script will consider as a
# ordinance file any odf that has any of this 
# characteristics, more desired characteristics
# to be gattered can be added to the list 
# non-desired data can be substracted from the list
ordinancesCharacteristics = ['ammoCost',
                             'lifeSpan',
                             'shotSpeed',
                             'damageRadius',
                             'damageBallistic',
                             'damageConcussion',
                             'damageFlame',
                             'damageImpact',
                             'xplGround',
                             'xplVehicle',
                             'xplBuilding']


# List of vehicle characteristic to gatter, 
# if left with only 'unitName' it will gatter all of them
# Right now the script considers as a vehicle any ODF that has
# the letter 'v' as the second character on the filename
vehicleCharacteristics = [
    'unitName'
]

for filename in os.listdir('./Files'):
    print('Looking through: ',filename)
    # Looks through the files on the ./Files folder

    with open(f'./Files/{filename}') as f:

        # Opens the file on readmode and makes auxiliar variables
        # boolean variable is redefined as True in the case the case it passed through some  of the possible type of ODF to analyze, so after the data is added to the corresponding diccionary
        # isVehicle is another auxiliary boolean that turns True when the filename has the letter 'v' on the second position, I didn't made it like that in the weapons and ordinances since they don't have a clear naming
        # Both auxiliar booleans will turn False again each time a new file is opened

        boolean = False
        isVehicle = False
        isOrdinance = False
        isGun = False

        # Definition of auxiliar dictionaries that are later added to the main ones

        tempVeh = {}
        tempOrdi = {}
        tempGuns = {}

        # Addition of the elements to the auxiliar dictionaries

        for element in vehicleCharacteristics:
            tempVeh[element] = ''

        for element in ordinancesCharacteristics:
            tempOrdi[element] = ''  

        for element in ordinancesCharacteristics:
            tempOrdi[element] = '' 

        # Scanning through each line of the file

        for line in f:

            # If the seccond letter on the filename is 'v' isVehicle will turn True, since it's a vehicle file
            if filename[1] == 'v':
                isVehicle = True

            try:

                # Splits each line to a list, based on spaces, so if the line is, for example, ammocost = 1 the list will be ['ammo', '=', 'cost']
                lineSplited = line.split()
                element = lineSplited[0]


                # If the first element on the list is one of the ordinance characteristics I want to get
                # this becomes True so I add the third element on the list to the auxiliar ordinance dictionary
                # I also turn the boolean variable to True to add this dictionary element to the main dictionary later
                # All of the next 'if' statements are equivalent to this one
                if element in ordinancesCharacteristics:
                    tempOrdi[element] = lineSplited[2]
                    isOrdinance = True
                    boolean = True
                
                if element in gunsCharacteristics:
                    tempGuns[element] = lineSplited[2]
                    isGun = True
                    boolean = True

                if isVehicle and len(vehicleCharacteristics)==1:
                    try:
                        lineSplited[2] = float(lineSplited[2])
                    except:
                        None
                    tempVeh[element] = lineSplited[2]
                    boolean = True

                elif isVehicle and element in vehicleCharacteristics:
                    try:
                        lineSplited[2] = float(lineSplited[2])
                    except:
                        None
                    tempVeh[element] = lineSplited[2]
                    boolean = True


            except:
                None
        
        # If the boolean is true the dictionary element will be added to the main dictionary
        if boolean:
            if isOrdinance:
                ordinances[filename] = tempOrdi
            if isGun:
                guns[filename] = tempGuns
            if isVehicle:
                vehicles[filename] = tempVeh
            
print('__________\n')

# I dump the dictionaries to json files
print('Saving json files')

with open('vehicles.json', 'w') as w:
    json.dump(vehicles, w)
with open('guns.json', 'w') as w:
    json.dump(guns, w)
with open('ordinances.json', 'w') as w:
    json.dump(ordinances, w)



# Transforms the dictionaries to pandas DataFrames and saves them to Excel Files
print('Saving xlsx files')

df = pd.DataFrame(data=guns)
df = (df.T)
df.to_excel('weapons.xlsx')

df = pd.DataFrame(data=ordinances)
df = (df.T)
df.to_excel('ordinances.xlsx')

df = pd.DataFrame(data=vehicles)
df = (df.T)
df.to_excel('vehicles.xlsx')

print('Done!')
