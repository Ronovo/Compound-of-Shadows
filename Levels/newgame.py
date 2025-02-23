from CommonScripts import weaponType
from Presets import weapons_preset
from Levels import act1


def newGame():
    print("New game started!")
    print("No save functionality (More to come!)")
    print("-------------")
    print("New Game Menu")
    print("-------------")
    while 1:
        print("1.) Background Information")
        print("2.) Squad Information")
        print("3.) Armory")
        print("4.) Start game")
        print("5.) Quit")
        answer = input("Please provide an answer...\n")
        match int(answer):
            case 1:
                background()
            case 2:
                squad()
            case 3:
                armory()
            case 4:
                startGame()
                break
            case 5:
                print("Thank you for checking out my game!")
                input("Press any key to exit...\n")
                quit()
            case _:
                print("Invalid answer. Try again")

def background():
    # Agent Setup
    print("Your name is Agent 1. You are an experienced operator working for a secret government organization.")
    print("You have only seen it marked by a Green Triangle. Those that carry the sign just know.")
    print("However, there are some signs man should never know.")
    input("Press any key to continute...")
    # Setting Set Up
    print("You have been tasked with 2 other agents to clear out a local drug den. You each have experience")
    print("in law/drug enforcement. But those stories are ones for another time...")
    print("There is an abandoned warehouse by the docks that has been a hotspot for drug activity.")
    print("A new gang has set up shop in the buildings around this dilapidated building.")
    print("They have secured a nice security foothold, and local law enforcement can't handle it.")
    input("Press any key to continue...")
    print("Objectives")
    print("1.) Clear the facility (Deadly force authorized)")
    print("2.) Find documents detailing drug activity")
    print("3.) Eliminate the head drug manufacturer, Former Agent Beaker.")
    input("Press any key to accept your objectives...\n")

def squad():
    while 1:
        print("Which agent would you like information on?")
        print("1.) Agent 1")
        print("2.) Agent 52")
        print("3.) Agent 500")
        print("4.) Return to Menu")
        agentAnswer = input("Please select your answer...\n")
        match int(agentAnswer):
            case 1:
                print("This is your character. You are a veteran of urban combat situations.")
                print("You have seen the worst that humanity has to offered. Can't say you made")
                print("it back completely in one piece. You are quick to act in combat situations.")
                print("Weapon Proficiency: Pistol, Assault Rifle")
            case 2:
                print("Your battle buddy. You have been side by side with each other through a lot.")
                print("He gets his nickname from a deck of cards, a set of which he always keeps handy.")
                print("You can't think of a better man you would want with you during a breach.")
                print("Weapon Proficiency: SMG, Shotguns")
            case 3:
                print("Mysterious agent assigned to this mission with you. Handles overlook duties.")
                print("You have talked little, but you have picked up he is an expert assassin.")
                print("Named Agent 500 for his love of snipers. He is a crack shot with his M40A3.")
                print("Weapon Proficiency: Snipers")
            case 4:
                break
            case _:
                print("Invalid answer. Try again")

def armory():
    print("\n")
    print("Welcome to the Armory!")
    weaponList = weaponType.weaponTypeMenu()
    if len(weaponList) == 0:
        return
    # Begin Loop for Weapon Menu
    print("Here are all weapons for type. Select one for more info!")
    print("----------------------")
    flag = False
    while not flag:
        w = weaponType.selectWeaponMenu(weaponList)
        if w == 0:
            return
        wName = weaponList[w - 1]
        weapons_preset.armoryDisplay(wName)

def startGame():
    print("Let's select your weapons before you start.")
    weaponList = weapons_preset.getAllowedWeaponsList()

    print("Primary Weapon Selection:")
    print("1.) " + weaponList[0].name)
    print("2.) " + weaponList[1].name)
    primarySelect = input("Select a primary...\n")
    primaryWeapon = None
    if int(primarySelect) == 1:
        primaryWeapon = weapons_preset.getWeaponByName(weaponList[0].name)
    elif int(primarySelect) == 2:
        primaryWeapon = weapons_preset.getWeaponByName(weaponList[1].name)
    print("You have selected the " + primaryWeapon.name)
    primaryWeapon.reload()
    print("Primary weapon loaded\n")

    print("Secondary Weapon Selection:")
    print("1.) " + weaponList[2].name)
    print("2.) " + weaponList[3].name)
    secondarySelect = input("Select a primary...\n")
    secondaryWeapon = None
    if int(secondarySelect) == 1:
        secondaryWeapon = weapons_preset.getWeaponByName(weaponList[2].name)
    elif int(secondarySelect) == 2:
        secondaryWeapon = weapons_preset.getWeaponByName(weaponList[3].name)
    print("You have selected the " + secondaryWeapon.name)
    secondaryWeapon.reload()
    print("Secondary Weapon loaded.")

    print("You are locked and loaded")
    print("-------------------------")
    print("ACT 1 : Initial Assault")
    print("-----------------------")
    # Initial Approach and First Combat Encounter
    scene1Result = act1.scene1(secondaryWeapon)
    # Warehouse Search
    agent1 = scene1Result['agent1']
    agent1 = act1.scene2(primaryWeapon,agent1)
    # Sniper Attack
    act1.scene3()

