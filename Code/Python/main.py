import random

# Dice Rolling Functions
def roll(rollIntro):
    rolling = True
    print("You have selected: roll", "\n")
    while rolling:
        if rollIntro: 
            rollIntro = False
            print("To roll your dice, you are just going to type the number of dice you are rolling and the number of sides the dice have")
            print("Separate these 2 or 3 things by a space, like: 1 12 or 2 20")
            print("Do not type: 1,6 (use space, not comma) or 2 twenty (only use numbers)")

        while True:
            user_input = input("Enter your dice roll or type help: ")
            
            if user_input.lower() == "help":
                rollIntro = True
                break

            try:
                dNum, dType = user_input.split()
                dNum = int(dNum)
                dType = int(dType)
                
                if dType not in [4, 6, 8, 10, 12, 20, 100]:
                    print("Please enter a valid dice type (4, 6, 8, 10, 12, 20, or 100).")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number of dice and a valid dice type, separated by a space.")
                continue
        if rollIntro:
            continue
        print("Rolling", dNum, "d", dType, "\n")
        if dNum == 1:
            if dType == 100:
                value = roll100()
            elif dType == 20:
                value = roll20()
                if value == 20:
                    print("You rolled a nat 20! Woohoo Critical Success!","\n")
                    return
                elif value == 1:
                    print("You rolled a nat 1! Boohoo Critical Failure!","\n")
                    return
            elif dType == 12:
                value = roll12()
            elif dType == 10:
                value = roll10()
            elif dType == 8:
                value = roll8()
            elif dType == 6:
                value = roll6()
            elif dType == 4:
                value = roll4()

            print("You rolled a:", value, "\n")
            rolling = False
        
        elif 1 < dNum < 100:
            rollX(dNum, dType)
            rolling = False
        
        else:
            print("Please enter a valid number of dice between 1 and 100.")


def rollX (x, dType):
    for i in range(1,x+1):
        if (dType == 100):
            value = roll100()
        elif (dType == 20):
            value = roll20()
            if(value == 20):
                print("Die", i, "rolled a nat 20! Woohoo Critical Success!","\n")
                continue
            elif(value == 1):
                print("Die", i, "rolled a nat 1! Boohoo Critical Failure!","\n")
                continue
        elif (dType == 12):
            value = roll12()
        elif (dType == 10):
            value = roll10()
        elif (dType == 8):
            value = roll8()
        elif (dType == 6):
            value = roll6()
        elif (dType == 4):
            value = roll4()
        
        print("Die", i, "rolled a:", value, "\n")

def roll100 ():
    return random.randint(1,100)

def roll20 ():
    return random.randint(1,20)

def roll12 ():
    return random.randint(1,12)

def roll10 ():
    return random.randint(1,10)

def roll8 ():
    return random.randint(1,8)

def roll6 ():
    return random.randint(1,6)

def roll4 ():
    return random.randint(1,4)

def main ():
    rollIntro = True
    isPlaying = True
   
    while True:
        user_input = input("Have you been here before: ")
    
        if user_input.lower() == "yes":
            rollIntro = False
            break
        
        elif user_input.lower() == "no":
            rollIntro = True
            break
        
        else:  
            print("Invalid input. Please answer yes or no.")
            continue

    while(isPlaying == True):

        print("What would you like to do?")
        action = input("Type your action or help to see a list of all actions: ").lower()
        
        if (action == "roll"):
            roll(rollIntro)
            rollIntro = False
    
        elif (action == "help"):
            print("You have selected: help","\n")
            print("Here are the possible actions:","\n") 
            print("Roll: Specify how many dice you're rolling and what type of dice you're rolling to receive results","\n")
            print("Help: Recieve a list of all commands","\n")
            print("Exit: Quit the session","\n")
        
        elif (action == "exit"):
            print("Thank you for playing!")
            isPlaying = False
        
        else:
            print("Please input a valid command or type help to view the valid commands")
            
    return 0  

main()
