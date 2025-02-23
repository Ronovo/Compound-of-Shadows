from Levels import newgame

print("Welcome to Ronovo's first Delta Green Adventure")
print("-----------------------------------------------")
print("Compound of Shadows!!!")
print("-----------------------------------------------")
print("Built using Standalonegunsystem v1.5")
print("-----------------------------------------------")
print("Main Menu")
print("---------")
while 1:
    print("1.) New Game")
    print("2.) Quit")
    answer = input("Please provide an answer...\n")
    if answer == str(1):
        newgame.newGame()
    print("Thank you for checking out my game!")
    input("Press any key to exit...\n")
    quit()
