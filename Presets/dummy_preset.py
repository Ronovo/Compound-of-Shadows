from CommonScripts import hitCalculations
from Objects.dummy import Dummy

small = Dummy(125, 0, 's')
medium = Dummy(200, 0, 'm')
large = Dummy(275, 0, 'l')

sizes = ['Small','Medium','Large']
ranges = [50,100,150,200,300,400,500]

def getSizes():
    return sizes

def getRanges():
    return ranges


def getNewDummy(debug):
    print("Dummy Size:")
    print("s = small, m = medium, l = large")
    size = input("Select your Size of Dummy\n")
    size = str.lower(size)
    match size:
        case 's':
            newDummy = small
        case 'm':
            newDummy = medium
        case 'l':
            newDummy = large
        case _:
            print("Invalid Option, Dummy set to Medium")
            newDummy = medium
    newDummy.setDummyRange(debug)
    return newDummy

def getNewDummyBalanceReport(size):
    match size:
        case 'Small':
            newDummy = small
        case 'Medium':
            newDummy = medium
        case 'Large':
            newDummy = large
        case _:
            newDummy = medium
    return newDummy

def shootDummy(newDummy, selectedWeapon, fireMode):
    triggerPulls = 1
    shots = 0
    if selectedWeapon.currentAmmo == 0:
        print("Out of Ammo! Try Reloading")
        return newDummy
    if fireMode == 'Fully Automatic':
        y = input("How many shots do you want to fire?\n")
        if int(y) > selectedWeapon.maxAmmo:
            triggerPulls = selectedWeapon.maxAmmo - selectedWeapon.currentAmmo
        else:
            triggerPulls = int(y)
    if fireMode == '3 Round Burst':
        triggerPulls = 3
    waitVariable = input("Press any key to shoot")
    while triggerPulls != 0:
        selectedWeapon.fireShot(True)
        triggerPulls -= 1
        if fireMode != "Fully Automatic":
            if fireMode == "3 Round Burst":
                if shots == 3:
                    shots = 0
            else:
                shots = 0
        shots += 1
        result = hitCalculations.calculateHit(selectedWeapon, newDummy, shots, True)
        if result[0] == 1:
            newDummy.takeDamage(result[1])
            print("Dummy health is now " + str(newDummy.health) + "\n")
        else:
            print("\n")
        if newDummy.health <= 0:
            print("Dummy destroyed!")
            break