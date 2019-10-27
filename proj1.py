# File:    proj1.txt
# Author:  Steven Ryan
# Date:    10/16/18
# Section: 34
# E-mail:  sryan6@umbc.edu
# Description:
# Creates a text-based game that uses random numbers and user input

##################################
#### DO NOT TOUCH THESE LINES ####
from random import randint, seed #
seed(1000)                       #
##################################

#obligatory waffle constant
EGGO = 10
eggo = "Eggo"

#random number constants
RANDMIN = 1
RANDMAX = 10

#constants for player and monster health
MAX_HEALTH = 100
MIN_HEALTH = 0

DEM_MAX_HEALTH = 300
DEM_MIN_HEALTH = 0

DEM_DAMAGE = 20

#constants for survival
SURVIVE_DAYS = 7
SURVIVE_DIST = 150

#constant lists of food and items
FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]

ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys",
         "Walkman", "Laser Cannon", "Rubber Band"]

STARTING_ITEMS = ['Walkie Talkie', 'Flashlight']

#constant lists of menu options
DAY_OPTIONS = ["View Inventory", "View Current Stats", "Eat an Eggo Waffle",
               "Nothing else."]
ENCOUNTER_OPTIONS = ["Fight", "Flail", "Flee"]
EQUIP_OPTIONS = ["Equip", "Unequip", "I changed my mind"]
ACTION_OPTIONS = ["Pack up camp and go", "Stay where you are"]
EAT_OPTIONS = ["eat it", "put it back"]

# getUserChoice(choices) asks the user to select a choice from a list of choices
#                 continuously prompts the user until the choice is valid
#                 a valid choice is one that is a valid index in the list
# Input:          choices; a list of all the possible choices available
# Output:         choice; the validated choice that the user made (int)
def getUserChoice(choices):
    choice = int(input("Enter a choice: "))
    return choice

# displayMenu(choices) provides a template for the various menus throughout the
#               game.
# Input:        choices; one of the option lists; displays choices
# Output:       returns nothing, because it is a print function
def displayMenu(choices):
    index = 0
    print("")
    print("Choose your option:")
    while(index < len(choices)):
        print(index + 1, "-", choices[index])
        index += 1

# calcDamage(item) computes the amount of damage the passed variable will
#              inflict on something else 
# Input:       item; a string that deals damage
# Output:      an integer, the amount of damage that the item deals
def calcDamage(item):
    if(item == ITEMS[0]):
        return 50
    elif(item == ITEMS[5]):
        return 100
    elif(item == ITEMS[6]):
        return 20
    elif(item == STARTING_ITEMS[0]):
        return 10
    elif(item == STARTING_ITEMS[1]):
        return 5
    else:
        return 0

# nothingHappens() prints out how greatful you are nothing happened. It
#                  is Event # 5 under the "walking to civilization"
#                  branch of the action tree.
# Input:           None
# Output:          None, moves on to the next part of the program
def nothingHappens():
    print("\nWoot woot! Nothing happened!")
    
# eat(food, player_health) gives a boost to the player's health that does
#                          not make the health exceed 100.
# Input:  takes in a string and a number; food tells what is being eaten,
#         player_health is the amount of health before being healed
# Output: an integer that will be the new health of the player
def eat(food, player_health):
    if(food == eggo):
        newHealth = player_health + EGGO
        return newHealth
    elif(food == FOODS[0]):
        print("\nYou're allergic to peanut butter. -30")
        newHealth = player_health - 30
        return newHealth
    elif(food == FOODS[1]):
        print("\nYou popped some pop rocks into your mouth. Ouch. -5 ")
        newHealth = player_health - 5
        return newHealth
    elif(food == FOODS[2]):
        print("\nYou're in love with the cocoa. +15")
        newHealth = player_health + 15
        return newHealth
    elif(food == FOODS[3]):
        print("\nYou feel wonderful after eating that. +25")
        newHealth = player_health + 25
        return newHealth
    elif(food == FOODS[4]):
        print("\nPart of a nutritious breakfast. +30")
        newHealth = player_health + 30
        return newHealth

# fight(player_health, item, inventory) fights the monster until someone
#           dies or the player runs away. Can be boosted by items. Flail
#           is also an option.
# Input:    takes in an integer, string, and list. player_health is the
#           starting health. item is the equipped booster. inventory is
#           the list of available items
# Output:   returns an integer of the remaining health after the end of
#           the fight.
def fight(player_health, item, inventory):
    flee = False
    demDamage = DEM_DAMAGE
    demo_health = DEM_MAX_HEALTH
    print("The Demogorgon appears in front of you.")
    print("it snarls and flashes several rows of teeth.", end = "")
    print(" It looks like it wants to fight.")
    #Hi-C or Walkman come into effect here
    if(ITEMS[2] in inventory):
        demo_health *= .5
    elif(ITEMS[4] in inventory):
        demDamage *= .75
    
    while(player_health > 0 and flee == False and demo_health > 0):
        print("\nYour Health:", player_health)
        print("Monster Health:", demo_health)
        print("\nWhat do you do now?")
        displayMenu(ENCOUNTER_OPTIONS)
        encounterOption = getUserChoice(ENCOUNTER_OPTIONS)
        if(encounterOption == 1):
            damageDealt = calcDamage(item)
            demo_health -= damageDealt
            print("\nYou deal", damageDealt, "damage to the Demogorgon")
            player_health -= demDamage
            print("You take", demDamage,"damage.")
        elif(encounterOption == 2):
            print("\nYou decided to flail like an idiot. \nYou hit your", end = "")
            print(" head and are killed and eaten by the monster.")
            return 0
        elif(encounterOption == 3):
            fleeOrNot = randint(1,10)
            if(fleeOrNot >= 1 and fleeOrNot <= 3):
                print("\nYou managed to flee the beast.")
                flee = True
            elif(fleeOrNot >=4 and fleeOrNot <= 10):
                print("\nYou tried to escape, but you didn't. Run faster next time")
                player_health -= demDamage * .5
                print("You take", demDamage * .5,"damage.")
        if(demo_health <= 0):
            print("\nYou have defeated the beast!... for now...")
            flee = True
    return player_health
                
# viewInventory(inventory) prints out a list of
#                          items you have and are able to use
#
# Input:    inventory, a list of items in the inventory
# Output:   None, prints list of items in inventory
def viewInventory(inventory):
    print("")
    print("Inventory:")
    print(inventory)

# printStats(health, distance, item) prints out the health,distance 
#                                    traveled, and equipped item
#
# Input:    takes in health, distance, and itemList. an float, float, and List
#           with one string or boolean in it if it has no item
# Output:   None, but it prints out information about the player
def printStats(health, distance, itemList):
    print("")
    print("Health:", health)
    print("Distance traveled:", distance)
    if(itemList[0] == ""):
        print("There is no equipped item")
    else:
        print("Equipped item:", itemList[0])

# equip(item, equipList) Activates an item's boost skill and allows only
#                        one item to be equipped.
#
# Input:    takes in a string to equip and a list to put it in.
# Output:   returns a list that has your equipped item
# FUNCTION REMOVED AND PLACE IN MAIN. MAKES CODE OVERLY COMPLEX

# unequip(equipList) Takes away the equipped item from the list and
#                    deactivates the ability
#
# Input:    takes in a string to unequip and a list to take it out of.
# Output:   returns a list that has no item
# FUNCTION REMOVED AND PLACED IN MAIN. MAKES CODE OVERLY COMPLEX

def main():
    #Variable initialization
    health = MAX_HEALTH
    demHealth = DEM_MAX_HEALTH
    aliveFlag = True
    multiplier = 1
    distance = 0
    choice = 0
    dayCounter = 1
    inventory = STARTING_ITEMS
    equippedItemFlag = False
    eggoFlag = False
    equipList = [""]
    equippedItem = ""
    attackPower = 0
    walked = ((health / 4) + 5)
    
    #Introduction: Beginning narration.
    print("After miles and miles of hiking", end = "")
    print(" in the woods, you finally setup your camp.")
    print("You decided to go camping on the wrong weekend.")
    print("Your phone buzzes:")
    print("\t\t\tTHE DEMOGORGON HAS ESCAPED.\t\tRUN.")
    print("")

    #Is true unless the player dies or makes the distance requirement
    while(aliveFlag == True and distance < SURVIVE_DIST):
        #Is true unless the player dies, makes the distance
        #requirement, or survives
        while(dayCounter <= SURVIVE_DAYS and aliveFlag == True
              and distance < SURVIVE_DIST):
            print("The sun rises on Day", dayCounter, "in the forest.")
            print("")
            print("What would you like to do this morning?")
            
            #Keeps prompting the user about daily tasks until
            #they don't want to do them.
            while(choice != 4):
                displayMenu(DAY_OPTIONS)
                choice = getUserChoice(DAY_OPTIONS)
                #Views inventory and asks to equip and unequip
                if(choice == 1):
                    #views inventory
                    viewInventory(inventory)
                    print("")
                    print("Do you want to equip an item?")
                    displayMenu(EQUIP_OPTIONS)
                    equipChoice = getUserChoice(EQUIP_OPTIONS)
                    #Validates whether the person can equip or unequip something
                    while(equipChoice == 1 and equippedItemFlag == True):
                        print("\nYou can't equip more than", end = "")
                        print(" one item. Try unequipping.")
                        displayMenu(EQUIP_OPTIONS)
                        equipChoice = getUserChoice(EQUIP_OPTIONS)
                    while(equipChoice == 2 and equippedItemFlag == False):
                        print("\nYou can't unequip items", end = "")
                        print(" when you have nothing equipped")
                        displayMenu(EQUIP_OPTIONS)
                        equipChoice = getUserChoice(EQUIP_OPTIONS)
                    #equips the item and activates the ability.
                    if(equipChoice == 1 and equippedItemFlag == False):
                        displayMenu(inventory)
                        equippedItem = getUserChoice(inventory)
                        print("You have equipped", inventory[equippedItem - 1])
                        equipList[0] = inventory[equippedItem - 1]
                        equippedItemFlag = True
                        if("Flashlight" in equipList):
                            attackPower = 5
                        elif("Walkie Talkie" in equipList):
                            attackPower = 10
                        elif("Rubber Band" in equipList):
                            attackPower = 25
                        elif("Sword" in equipList):
                            attackPower = 50
                        elif("Laser Cannon" in equipList):
                            attackPower = 100
                    #Where the unequip function would be if I didn't take it out
                    #because of its redundancy.
                    elif(equipChoice == 2 and equippedItemFlag == True):
                        equippedItem = equipList[0]
                        equipList.remove(equippedItem)
                        equipList.append("")
                        attackPower = 0
                        equippedItemFlag = False
                        print("You have unequipped", equippedItem)
    
                #prints stats
                elif(choice == 2):
                    printStats(health, distance, equipList)        
                #eats an eggo
                elif(choice == 3):
                    if(eggoFlag == False):
                        if(eat(eggo, health) <= MAX_HEALTH):
                            health = eat(eggo, health)
                            print("\nThat waffle stood no chance ", end = "")
                            print("against your voracious appetite. +10")
                        elif(eat(eggo, health) > MAX_HEALTH):
                            health = 100
                            print("\nYou were healed to full!")
                        eggoFlag = True
                    else:
                        print("")
                        print("Slow down there tubby,", end = "")
                        print(" that's enough waffle for today")
                #prompts the user if the loop hasn't ended
                if(choice != 4):
                    print("")
                    print("What else do you want to try this morning?")

            #moves on past daily tasks to daytime actions
            displayMenu(ACTION_OPTIONS)
            leaveOrStay = getUserChoice(ACTION_OPTIONS)
            #If you leave
            if(leaveOrStay == 1):
                eventChance = randint(1, 10)
                # EVENT 1: 20% chance you find a food backpack
                if(eventChance >= 1 and eventChance <= 2):
                    foodAppears = randint(1, len(FOODS))
                    backPackFood = FOODS[foodAppears]
                    print("\nYou stumble upon a backpack with a food item in it")
                    print("You open the backpack and find", backPackFood)
                    eatChoice = input("Do you want to eat it? (y/n) ")
                    if(eatChoice == "y"):
                        health = eat(backPackFood, health)
                    elif(eatChoice == "n"):
                        print("Alright, you weren't hungry anyway... right?")
                # EVENT 2: 20% chance you find an old shed with items in it
                if(eventChance >= 3 and eventChance <= 4):
                    shedItem = randint(0, len(ITEMS)-1)
                    #for duplicate items
                    if(ITEMS[shedItem] in inventory):
                        print("You stumble upon a", shedItem,"in a nearby shed.")
                        print("Unfortunately, you already have it.")
                    #You add the shed item to your inventory
                    else:
                        inventory.append(ITEMS[shedItem])
                        print("\nYou stumble upon an old shed and take a look")
                        print("You see something on the shelf, it's a", ITEMS[shedItem])
                        print("The", ITEMS[shedItem].upper(), "has been ", end = "")
                        print("added to your inventory.")
                        if(shedItem == ITEMS[1] or shedItem == ITEMS[3]):
                            print("You feel that you can travel faster now")
                        elif(shedItem == ITEMS[0] or shedItem == ITEMS[5] or
                             shedItem == ITEMS[6]):
                            print("You feel like you could wack ", end = "")
                            print("a monster with ", end = "")
                            print("a little more power now")
                        elif(shedItem == ITEMS[2] or shedItem == ITEMS[4]):
                            print("You feel like the Monster might", end = "")
                            print("have weakened a little")

                    #if you get a Hi-C or Walkman, the effects take place in
                    #the fight function. the effects of the equippable items only
                    #come into play when you equip them
                    #Otherwise, take into account the travel items:

                    #if bicycle is acquired, add distance multiplier
                    if(ITEMS[1] in inventory):
                        multiplier = 1.5
                    #if Heeleys are acquired, add distance multiplier
                    elif(ITEMS[3] in inventory):
                        multiplier = 1.25

                # EVENT 3: 20% chance that you fall into a trench
                if(eventChance >= 5 and eventChance <= 6):
                    dayCounter += 1
                    print("You fall into a trench. OUCH!")
                    print("You spend a whole day recovering")
                    print("You also were only able to go about half", end = "")
                    print(" the distance you would have gone.")
                    multiplier *= .5
                    
                # EVENT 4: 30% chance that you fight the monster
                if(eventChance >= 7 and eventChance <= 9):
                    health = fight(health, equipList[0], inventory)
                    
                # EVENT 5: 10% chance that nothing happens
                if(eventChance == 10):
                    nothingHappens()
                    
            #If you stay
            elif(leaveOrStay == 2):
                demoEncounter = randint(1, 10)
                #70% chance of fighting the monster
                if(demoEncounter >= 1 and demoEncounter <= 7):
                    health = fight(health, equipList[0], inventory)
                #30% chance of being healed to full
                elif(demoEncounter > 7 and demoEncounter <= 10):
                    print("\nThe monster got confused and ran past your camp")
                    print("You then rest up to full health")
                    health = MAX_HEALTH
            #print out stuff for the end of the day
            if(health <= 0):
                print("You have died.")
                aliveFlag = False
            if(aliveFlag == True):
                walked = ((health / 4) + 5)
                distance = distance + walked * multiplier
                print("\nYou have walked", distance,"\n")
                          
            #reset variables
            choice = 0
            eggoFlag = False
            dayCounter += 1
            if(ITEMS[1] in inventory):
                multiplier = 1.5
            elif(ITEMS[3] in inventory):
                multiplier = 1.25
            else:
                multiplier = 1
    if(dayCounter > SURVIVE_DAYS):
        print("You survived 7 days and therefore win\n")
    elif(distance >= SURVIVE_DIST):
        print("You made it to the nearest city and survived\n")
    else:
        print("ENDGAME\n")
main()
