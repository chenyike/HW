import random

def print_intro():
    print '''Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term of office. Your duties are to distribute food, direct farming, and buy and sell land as needed to support your people. Watch out for rat infestations and the resultant plague! Grain is the general currency, measured in bushels. The following will help you in your decisions:\n
    * Each person needs at least 20 bushels of grain per year to survive. \n
    * Each person can farm at most 10 acres of land.\n
    * It takes 2 bushels of grain to farm an acre of land.\n
    * The market price for land fluctuates yearly.\n
    Rule wisely and you will be showered with appreciation at the end of your term. Rule poorly and you will be kicked out of office!'''

def Hammurabi():
    year=1
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000              #total bushels harvested
    bushels_per_acre = 3   #amount harvested for each acre planted
    rats_ate = 200               #bushels destroyed by rats
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19      # each acre costs this many bushels
    plague_deaths = 0

    print_intro()

    while year<11:
        print'''O great Hammurabi!\n
        You are in year''', year, '''of your ten year rule.\n
        In the previous year''', starved,'''people starved to death.\n
        In the previous year''',immigrants,'''people entered the kingdom.\n
        The population is now''',population,'''.\n
        We harvested''',harvest, '''bushels at''',bushels_per_acre,'''bushels per acre.\n
        Rats destroyed''',rats_ate,'''bushels, leaving''',bushels_in_storage,'''bushels in storage. \n
        The city owns''',acres_owned,'''acres of land.\n
        Land is currently worth''',cost_per_acre,'''bushels per acre.\n
        There were''',plague_deaths,'''deaths from the plague.\n'''

        #Ask user to choose sell or buy land, calculate 8.acres owned
        buy_or_sell=raw_input('Please type \'B\' if you want to buy land, and input \'S\' if you wish to sell land.')

        while buy_or_sell not in 'BbSs':
            buy_or_sell=raw_input('Please type \'B\' if you want to buy land, and input \'S\' if you wish to sell land.')
        if buy_or_sell in 'Bb':
            added_land=ask_to_buy_land(bushels_in_storage,cost_per_acre)
            acres_owned+=added_land
            bushels_in_storage-=cost_per_acre*added_land
        elif buy_or_sell in 'Ss':
            decreased_land=ask_to_sell_land(acres_owned)
            acres_owned-=decreased_land
            bushels_in_storage+=cost_per_acre*decreased_land
            
        
        #Ask user to feed people, calculate 7.bushels_in_storage
        decreased_bushels=ask_to_feed(bushels_in_storage)
        bushels_in_storage-=decreased_bushels

        #Ask user to cultivate land
        seed_acres=ask_to_cultivate(acres_owned, population, bushels_in_storage)
        bushels_in_storage-=seed_acres * 2

        #Calculate 10. plague death
        if isPlague()==True:
            plague_deaths=population/2
        else:
            plague_deaths=0

        #Calculate number of 1.people starving
        starved=numStarving(population, decreased_bushels)
        #Judge whether Hammurabi is fired or not
        if starved>0.45*population:
            print '''Oh... great Hammurabi, way too many people starved to death. You are fired!'''
            break

        #Calculate 2.immigrants population
        immigrants=numImmigrants(acres_owned,bushels_in_storage,population,starved)
        
        #Calculate 4.harvest and 5. bushels_per_acre
        bushels_per_acre=getHarvest()
        harvest=seed_acres * bushels_per_acre

        #Calculate 6.rats impact
        infest_percent=effectOfRats()
        rat_probability=random.randint(0,100)
        if rat_probability<40:
            rats_ate=abs((bushels_in_storage * infest_percent)/100)
        else:
            rats_ate=0
        

        #Calculate 7.bushels_in_storage
        bushels_in_storage=bushels_in_storage+harvest-rats_ate
        
        #Calculate 9.price of land
        cost_per_acre=priceOfLand()

        #Calculate the population
        population=population-starved+immigrants-plague_deaths
        
        year+=1  #Complete the while loop

        print

    if year==11 and population>80 and acres_owned>600:
        print '''O great Hammurabi, thank you for leading us into prosperity!'''
    elif year==11 and population>50 and acres_owned>300:
        print '''O great Hammurabi, we appreciate your wise ruling!'''
    elif year==11 and population>0 and acres_owned>0:
        print '''O great Hammurabi, thank you for bringing us back from near distinction!'''
        

def ask_to_buy_land(bushels,cost):
    '''Ask user how many bushels to spend buying land.'''
    acres = input("How many acres will you buy? ")
    while acres * cost > bushels:
        print "O great Hammurabi, we have but", bushels, "bushels of grain!"
        acres = input("How many acres will you buy? ")
    return acres

def ask_to_sell_land(acres):
    '''Ask user how much land they want to sell'''
    acres_to_sell=input('How many acres will you sell?')
    while acres_to_sell>acres:
        print '''O great Hammurabi, we only have''',acres,'''of land!'''
        acres_to_sell=input('How many acres will you sell?')
    return acres_to_sell

def ask_to_feed(bushels):
    '''Ask user how many bushels they want to use for feeding.'''
    bushels_to_feed=input('How many bushels will you feed your people?')
    while bushels_to_feed>bushels:
        print '''O great Hammurabi, we only have''',bushels,'''bushels'''
        bushels_to_feed=input('How many bushels will you feed your people?')
    return bushels_to_feed


def ask_to_cultivate(acres, population, bushels):
    '''Ask user how much land they want to plant seed in'''
    seeding_acres=input('How many acres of land do you want to plant seed in?')
    while seeding_acres>acres or seeding_acres>population*10 or bushels<seeding_acres*2:
        print '''O great Hammurabi, we only have''',acres,'''acres of land, we only have''',bushels,'''bushels of grain, and we only have''',population, '''people'''
        seeding_acres=input('How many acres of land do you want to plant seed in?')
    return seeding_acres
    
def isPlague():
    if random.randint(0,100)<=15:
        return True
    else:
        return False

def numStarving(population, bushels):
    if population<(bushels/20):
        starved_people=0
    else:
         starved_people=population-bushels/20
    return starved_people
    
def numImmigrants(land,grainInStorage,population,numStarving):
    immigrant=(20*land+grainInStorage)/(100*population+1)
    return immigrant

def getHarvest():
    acre_yield=random.randint(1,8)
    return acre_yield

def effectOfRats():
    percent_destroyed=random.randint(10,30)
    return percent_destroyed

def priceOfLand():
    price_of_land=random.randint(16,22)
    return price_of_land

    

        
