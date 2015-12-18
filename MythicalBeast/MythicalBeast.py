#12/18/15 - If Statements
# Have you already written a program to figure out what you would do if you come across a wild beast?
# If you haven't you should do so now, because it happens all the time, and you need to prepare yourself

from random import randint #Import our random function

print("\n\nMythical Beast Encounter Simulator") #Print Title

Beasts = ["Leprechaun", "Dragon", "Cyclops", "Hippogriff", "Minotaur", "Unicorn"] #Store the beasts
beastNumber = randint(0,5) # Get random beast

print("You come across a wild: " + Beasts[beastNumber])

if(beastNumber == 0): #We found a leprechaun! Thank you if statement
    print("Found Leprechaun")

if(beastNumber == 1):
    print("found Dragon")


#If staement cheat sheet
#    three components
#           * keyword 'if'
#           * condition inside paremthesis '(thing A == thing B)'
#           * code to be executed if true, in python this comes after a colon ':'
#             and needs to be indented one tab in from the if statement

#   example: if(A > B):
#                doThatThing()
#                doThisThing()
#            otherCodeAfterIfStatement()
