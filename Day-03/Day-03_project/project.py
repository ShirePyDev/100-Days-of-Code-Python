print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the Treasure")
first = input("Your're the cross road. Where do you want to go? Type right or Type left: ")
first = first.capitalize()

if first == "right":
    print("You've come a lake. There is an Island in the middle of the lake.")
    type2 = input("Type wait to wait for boat. Type swim to swim across.")
    type2 = type2.capitalize()
    if type2 == "wait":
        type3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
              "One red, One yellow and One green?")
        type3 = type3.capitalize()
        
        if type3 == "green":
            print("You get success!")
            
        elif type3 == "red":
            print("It's a room of fire. Game over.")
            
        elif type3 == "yellow":
            print("You get a shack. Game over.")
            
    else:
        print("There is crocodile catch you and dead!")
        
else:
    print("You fell a hall. Game over")