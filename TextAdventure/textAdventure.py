
#-------------------Setup (This is where all of my definitions are)'


def getCharacterInfo(): #this function gets all the info for our character
    global name
    name = raw_input("Howdy, What's your name partner? ")
    print("\n\n\n\n You have 100 credits to spend on supplies. It might be wise to save some for the road.\n")

    donzo = False
    while(credits > 0 and donzo == False):
        print("You have " + str(credits) + " credits left, what will you buy next? ")
        choice = int(raw_input("Enter: \n 1) Food \n 2) Armor \n 3) Ammunition \n 4) I'm done buying things "))
        donzo = handleInfoChoice(choice)



def handleInfoChoice(choice): # this function handles our choices
    if(choice == 1):
        global credits #get a reference to our variables
        global food
        global armor
        global ammunition

        quantity = int(raw_input("How Much? ")) # get user input

        food = food + quantity # add to our food counter

        credits = credits - quantity # take away from our credits

        print("You purchased " + str(quantity) + " Units of food \n\n\n") # Tell us what is going on
        return False #Let the loop know we arent done yet

    elif(choice == 2):
        quantity = int(raw_input("How Much? "))
        armor = armor + quantity
        credits = credits - quantity
        print("You purchased " + str(quantity) + " Units of Armor \n\n\n")
        return False

    elif(choice == 3):
        quantity = int(raw_input("How Much? "))
        ammunition = ammunition + quantity
        credits = credits - quantity
        print("You purchased " + str(quantity) + " Units of Ammunition \n\n\n")
        return False
    else:
        print("It's been great knowing you. Good luck with your journey ")
        return True


def game():
    print "\n\n\n\n\nThis is the game loop"
    answer = int(raw_input("\nWhat'll it be? \n 1) Print Stats \n 2) Do a cool thing \n" ))
    handleGameChoice(answer)

def handleGameChoice(num):
    global credits, name, food, armor, ammunition

    if(num == 1):
        print "Name: " + str(name) + " | Credits: " + str(credits) + " | Food: " + str(food) + " | Armor: " + \
         str(armor) + " | Ammunition: " + str(ammunition)
    else:
        print "Sorry, Havent figured out that thing yet"

        
#----------------Main (this is where my program runs)


credits = 100
name = ""
food = 0
armor = 0
ammunition = 0

getCharacterInfo()
game()
