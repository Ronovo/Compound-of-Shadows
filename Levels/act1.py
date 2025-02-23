from CommonScripts import hitCalculations
from Presets import weapons_preset
from Objects import enemy

#agent500 = {'health' : 10, 'primaryWeapon' : 'MP5', 'secondaryWeapon' : 'USP .45', 'luckyWeapon': '.38 Special'}

def scene1(secondaryWeapon):
    agent500 = {'health' : 10, 'weaponName' : 'M40A3'}
    agent1 = {'health' : 12}
    print("You arrive at sundown to the abandoned warehouse. It is a compound, and surveilled.")
    print("After a small planning session at the SUV before you go in, the game plan is decided.")
    print("Agent 500 will get a position on a building overlooking our entrance into the compound.")
    print("Agent 52 will join you in breaching and clearing.")
    print("500 will provide backup and overwatch when needed, as well and protect your initial advance.")
    input("Press any key if you agree to this plan...\n")
    print("Agent 500 enters a building, and start climbing to the top. The staircase is old, and worndown.")
    print("Press any key to see if he falls...\n")
    result = hitCalculations.roll(100)
    print("Agent 500's Athletics : 80")
    print("Roll result : " + str(result))
    if result < 80:
        print("He successfully gets to the top without issue")
    else:
        agent500['health'] -= 1
        print("DEBUG : Agent 500's Health is now " + str(agent500['health']))
        print("While walking upstairs, he trips on a step as it breaks below him.")
        print("He does not alert any guards, but he does take a nail in the foot that hurts.")
        print("He might need a Tetanus shot after this\n")
    print("He gets set up on the roof and radios the situation to you. 3 Guards walking between the buildings.")
    print("There is the abandoned warehouse, an old administration building, and some shipping containers.")
    print("Plenty of debris and cover to sneak in under the cover of night.")
    input("Press any key to begin the assault...\n")
    guard = enemy.Enemy(10,100,'m')
    print("There is a guard as you approach, watching the gap leading to the central courtyard of the \'compound\'")
    print("Do you want Agent 500 to take a sniper shot? or do you want to try and take them out?")
    print("Note : All weapons have silencers. Single shots will not draw attention. Sustained Shots will.")
    print("1.) Agent 500 Sniper Shot")
    print("2.) Take out with your " + secondaryWeapon.name)
    agentAnswer = input("Answer Below:\n")
    if int(agentAnswer) == 1:
        selectedWeapon = weapons_preset.getWeaponByName(agent500["weaponName"])
        guard.distance = 300
    elif int(agentAnswer) == 2:
        selectedWeapon = secondaryWeapon
    else:
        print("You incoherently babble, and Agent 500 decides to take the shot in your temporary insanity.")
        selectedWeapon = weapons_preset.getWeaponByName(agent500["weaponName"])
        guard.distance = 300
    print("DEBUG: Gun is set to : " + selectedWeapon.name)
    selectedWeapon.reload()

    # Guard Encounter
    selectedWeapon.currentAmmo -= 1
    result = hitCalculations.calculateHit(selectedWeapon, guard, 1, False)
    if selectedWeapon.name == "M9":
        secondaryWeapon = secondaryWeapon
    if result[0] == 1:
        guard.takeDamage(result[1])
        print("His head sprays a red mist as your bullet pierces it. He falls back with a new hole in his forehead")
    if result[0] == 0:
        print("The guard now sees you and is ready to take a shot back.")
        print("You back up for some cover as he takes a shot.")
        print("BANG!!!!\n")
        agent1Dummy = enemy.Enemy(12,200,'m')
        enemyWeapon = weapons_preset.getWeaponByName("G36")
        enemyResult = hitCalculations.calculateHit(enemyWeapon, agent1Dummy, 1, False)
        if enemyResult[0] == 1:
            agent1['health'] -= 4
            print("DEBUG: Agent 1 Health now at " + str(agent1['health']))
            print("You get hit as you try and get behind cover. You will survive, but you need first aid.")
        elif enemyResult[0] == 0:
            print("You successfully dodge the shot.")
        print("Agent 52 takes a shot as you duck behind cover. The guard falls to the ground.")
        print("A cold voice on the walkie-talkie. \"How have you survived this long by yourself?\"")
        print("It's clear 500 is doubting your abilities. You bandage yourself to stop the bleeding, and push on.")

    print("Agent 500 turns his attention to the rest of the courtyard. He notifies you that the warehouse side is clear.")
    print("2 guards by the administration building, not a concern right now. Provides overwatch as you and Agent 52")
    print("stack up on a door. You give a look. Just like old times. You see the confirmation in 52's eyes.")
    input("Press any button to kick in the door.....\n")
    scene1Result = {'agent1' : agent1, 'agent500' : agent500, 'secondaryWeapon' : secondaryWeapon}
    return scene1Result

def scene2(primaryWeapon, agent1):
    print("The warehouse is dimly lit, filled with abandoned crates, graffiti, and the faint echo of distant urban decay.")
    print("Drug paraphernalia lies scattered across the floor and crates, remnants of the last party.")
    print("Speaking of dregs, two junkies are lying passed out in a corner of the room. What do you do?")
    print("1.) Apprehend the Junkies")
    print("2.) Shoot to Kill")
    print("Note : Agent 52 will not approve of noncombatant deaths.")
    junkieAnswer = input("Please make a decision...\n")
    junkieInitative = False
    agentInitative = False
    innocentCheck = True
    if int(junkieAnswer) == 1:
        innocentCheck = False
        print("You approach the junkies, trying to call to them. \"Hands where I can see them\"")
        input("Press any button to do an Alertness Roll...")
        alertCheck = hitCalculations.roll(100)
        print("Agent 1's Alertness : 60")
        print("Alertness Roll : " + str(alertCheck))
        if alertCheck < 60:
            agentInitative = True
            print("As you approach, you see the junkie twitching nervously. He may be dangerous.")
            print("As he leaps up, you have the first shot with your drawn " + primaryWeapon.name)
        else:
            junkieInitative = True
            print("You do not notice the junkie twitching as you approach.")
            print("He leaps up, surprising you, with a gun in hand. He shoots his M1911.")
    elif int(junkieAnswer) == 2:
        agentInitative = True
    else:
        junkieInitative = True
        print("The junkie leaps up as you decide on a plan forward, and gets the first attack on you.")

    #Set Gun for Fight
    selectedWeapon = None
    if agentInitative:
        selectedWeapon = primaryWeapon
    elif junkieInitative:
        selectedWeapon = weapons_preset.getWeaponByName('M1911')

    #Reload weapon if it is the Junkies gun
    if selectedWeapon.currentAmmo == 0:
        selectedWeapon.reload()

    #Do the hit calculation
    junkie = enemy.Enemy(10,100,'s')
    agent1Dummy = enemy.Enemy(12, 200, 'm')
    if agentInitative:
        result = hitCalculations.calculateHit(selectedWeapon,junkie,1,False)
        if result[0] == 1:
            print("You take a shot at the Junkie, and it hits.")
            print("He crumples down to the mattress, red stains joining other ones on the spotted mattress.")
        if result[0] == 0:
            print("You miss your shot at the Junkie. Now he is going to take a shot at you.")
            print("There is no immediate cover here.")
            selectedWeapon = weapons_preset.getWeaponByName('M1911')
            if selectedWeapon.currentAmmo == 0:
                selectedWeapon.reload()
            junkieResult = hitCalculations.calculateHit(selectedWeapon, agent1Dummy, 1, False)
            if junkieResult[0] == 1:
                agent1['health'] -= 2
                print("You feel a pain as the bullet hits your arm. That's going to hurt in the morning.")
                if agent1['health'] < 10:
                    print("You aren't looking too good. If you keep this up, you might not make it out.")
            elif junkieResult[0] == 0:
                print("Luckily, his aim is not good, and the bullet whizzes by your ear.")
            print("As the Junkie takes the shot, Agent 52 turns with his MP5 and lands a 3-round burst to his chest.")
            print("Unlike 500, he doesn't scold you. \"I got your back, buddy.\"")
    elif junkieInitative:
        junkieResult = hitCalculations.calculateHit(selectedWeapon,agent1Dummy,1,False)
        if junkieResult[0] == 1:
            agent1['health'] -= 2
            print("You feel a pain as the bullet hits your arm. That's going to hurt in the morning.")
            if agent1['health'] < 10:
                print("You aren't looking too good. If you keep this up, you might not make it out.")
        elif junkieResult[0] == 0:
            print("Luckily, his aim is not good, and the bullet whizzes by your ear.")
            print("As the Junkie takes the shot, Agent 52 turns with his MP5 and lands a 3-round burst to his chest.")
            print("Unlike 500, he doesn't scold you. \"I got your back, buddy.\"")

    input("Press any key to continue...\n")

    if innocentCheck:
        print("52's face gets severe as the situation resolves itself.")
        print("\"I don't like how you handled that. We aren't executioners.\"")
        print("You explain that it isn't like this is the first time you as a group had done this.")
        print("\"Let's make this mission the last time we are this ruthless, please?\"")
        print("You have something to consider when you go home.")
        input("Press any key to continue...\n")
    print("The other Junkie puts his hands on his head when he hears the gun go off.")
    print("\"He said you were coming\" he says in a matter of fact voice")
    print("As you handcuff him, he starts to utter gibberish to you.")
    print("You pistol whip him to shut him up. As you stand up, you notice the symbols on the wall.")
    print("The art makes you uneasy. It is not normal graffiti. The symbols seem to draw you to them.")
    print("You shake it off, and do a sweep of the warehouse with 52 for any more threats\n")
    input("Press any key to continue...\n")
    return agent1

def scene3():
    print("As you and Agent 52 deal with the Junkies inside, your sounds alert some guards.")
    print("The ones that were around the administrative building have started to move towards the warehouse.")
    print("There are 2 of them. Agent 500 has 3-4 shots before they make it to the warehouse door.")
    print("He hardens his stare as he touches the microphone on his ear. \"Additional Guards Alerted.\"")
    print("\"I am going to try and take them out myself.\"")
    print("He puts his cheek against the pad of his trusty rifle, and dials in his first shot.")
    guard1 = enemy.Enemy(10,400,'m')
    guard2 = enemy.Enemy(10,450,'l')
    selectedWeapon = weapons_preset.getWeaponByName('M40A3')
    if selectedWeapon.currentAmmo == 0:
        selectedWeapon.reload()
    shootAtGuardsResult = []
    guard1Standing = 1
    guard2Standing = 1
    for x in range(1,4):
        match x:
            case 1:
                if guard1Standing == 1 or guard2Standing == 1:
                    shootAtGuardsResult = shootAtGuards(selectedWeapon,400,450,guard1Standing,guard2Standing)
            case 2:
                if guard1Standing == 1 or guard2Standing == 1:
                    shootAtGuardsResult = shootAtGuards(selectedWeapon, 350, 400, guard1Standing, guard2Standing)
            case 3:
                if guard1Standing == 1 or guard2Standing == 1:
                    shootAtGuardsResult = shootAtGuards(selectedWeapon, 300, 350, guard1Standing, guard2Standing)
            case 4:
                if guard1Standing == 1 or guard2Standing == 1:
                    shootAtGuardsResult = shootAtGuards(selectedWeapon, 250, 300, guard1Standing, guard2Standing)
        if shootAtGuardsResult['Guard 1'] == 0:
            guard1Standing = 0
        if shootAtGuardsResult['Guard 2'] == 0:
            guard2Standing = 0
        if guard1Standing == 0 and guard2Standing == 0:
            print("Both guards died before they get to the warehouse.")
            break



def shootAtGuards(selectedWeapon,distance1,distance2,guard1Standing,guard2Standing):
    guardShootResult = {'Guard 1' : guard1Standing, 'Guard 2' : guard2Standing}
    print("Which one do you want to shoot at?")
    if guard1Standing == 1:
        print("1.) Guard 1 (" + str(distance1)+ "M)")
    if guard2Standing == 1:
        print("2.) Guard 2 (" + str(distance2) + "M)")
    guardAnswer = input("Select your target...\n")
    guardResult = []
    selectedGuard = 0
    guard1Dummy = enemy.Enemy(10, distance1, 'm')
    guard2Dummy = enemy.Enemy(10, distance2, 'm')
    match int(guardAnswer):
        case 1:
            input("Press any key to take a shot...\n")
            selectedWeapon.fireShot(False)
            guardResult = hitCalculations.calculateHit(selectedWeapon, guard1Dummy, 1, False)
            selectedGuard = 1
        case 2:
            input("Press any key to take a shot...\n")
            selectedWeapon.fireShot(False)
            guardResult = hitCalculations.calculateHit(selectedWeapon, guard2Dummy, 1, False)
            selectedGuard = 2
        case _:
            if guard1Standing == 1:
                print("Invalid answer. Guard 1 set as target.")
                selectedGuard = 1
                input("Press any key to take a shot...\n")
                selectedWeapon.fireShot(False)
                guardResult = hitCalculations.calculateHit(selectedWeapon, guard1Dummy, 1, False)
            elif guard2Standing == 1:
                print("Invalid answer. Guard 2 set as target ")
                selectedGuard = 2
                input("Press any key to take a shot...\n")
                selectedWeapon.fireShot(False)
                guardResult = hitCalculations.calculateHit(selectedWeapon, guard2Dummy, 1, False)

    if guardResult[0] == 1:
        if selectedGuard == 1:
            print("You have killed Guard 1")
            guardShootResult['Guard 1'] = 0
        if selectedGuard == 2:
            print("You have killed Guard 2")
            guardShootResult['Guard 2'] = 0
    else:
        print("You missed that shot!")
    return guardShootResult






