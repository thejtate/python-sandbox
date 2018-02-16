import copy

toon = dict(
    name = 'Unkown',
    roll = 'Undead', 
    stats = {'hp':0,'mp':0,'sp':0}
    )

world = dict(
    user0 = {}
    )

def creation(name, roll):
    if roll.lower() == 'warrior':
        toon['name'] = name
        toon['roll'] = 'Mighty Warrior'
        toon['stats']['hp'] = 200
        toon['stats']['mp'] = 0
        toon['stats']['sp'] = 100
        return toon; 
    if roll.lower() == 'mage':
        toon['name'] = name
        toon['roll'] = 'Mythical Mage'
        toon['stats']['hp'] = 60
        toon['stats']['mp'] = 200
        toon['stats']['sp'] = 10
        return toon; 
    if roll.lower() == 'thief':
        toon['name'] = name
        toon['roll'] =  'Sneaky Thief'
        toon['stats']['hp'] = 75
        toon['stats']['mp'] = 40
        toon['stats']['sp'] = 140
        return toon; 
    else: 
        toon['name'] = name 
        toon['roll'] = 'Peasant'
        toon['stats']['hp'] = 20
        toon['stats']['mp'] = 0
        toon['stats']['sp'] = 0
        return toon; 

name = ''
roll = ''
key = 0

while True: 
    name = input('Enter your name: ')
    if name == '':
        print('Please enter a name, or type [quit] to stop.')
        continue
    elif name.lower() == 'quit':
        break   

    roll = input('Enter a class [Warrior, Mage, Thief] (if none, you will be a peasant): ')
    
    creation(name, roll)

    #Add new user to the Dictory 
    world['user'+str(key)] = copy.deepcopy(toon) #Deepcopy needed, else toon is duplicated
    key += 1

    # Print out results
    cleanp = '\nName: '+toon['name']+'\nClass: '+toon['roll']+'\n\nHP['+str(toon['stats']['hp'])+'] \nMP['+str(toon['stats']['mp'])+'] \nSP['+str(toon['stats']['sp'])+']'
    print(cleanp, end='\n\n')
    print('Total characters in world: ' + str(len(world)), end='\n\n')
 
    answer = input('Done adding users? ')
    if answer.lower() == 'yes':
        break
    else: 
        continue 

print('End of program...')