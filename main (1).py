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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Answer with the words in single quotation marks.") 

left_or_right = input("Would you like to go 'left' or 'right?' ").lower()
if left_or_right == "left":
  swim_or_wait = input("Would you like to 'swim' the river or 'wait?' ").lower()
  if swim_or_wait == "wait":
    door = input("'Yellow' door, 'Blue' door or 'Red' door? ").lower()
    if door == "red":
      print("Burned by fire. Game over!")
    elif door == "blue":
      print("Eaten by beasts. Game over!")
    elif door == "yellow":
      print("You win. Congrats!")
    else:
      print("Game over!")

  else:
    print("Attacked by trout. Game over!")
else:
  print("You jumped off a cliff. Game over!")
