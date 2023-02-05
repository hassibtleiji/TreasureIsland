print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")

answer1 = input(
    "Your outside in the woods and run into the base of a mountain. Would you like to go left or right?").lower()
if answer1 == "left":
    answer2 = input(
        "You ran to a dead end, only thing there is a river. Are you going to swim or wait? ").lower()
    if answer2 == "wait":
        answer3 = input(
            "Your at the end and there are 3 doors, which do you open? Red, Blue, or Yellow?").lower()
        if answer3 == "red":
            print("It's a room full of fire, Game Over!")
        elif answer3 == "yellow":
            print("You found the trasure, you win!")
        elif answer3 == "blue":
            print("You enter a room full of beasts, Game Over.")
        else:
            ("You chose a door that doesnt exist, Game Over.")
    else:
        print("You get attacked by angry beavers, Game Over")
else:
    print("You fell into a hole, Game Over")
