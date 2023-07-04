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
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
one = input('You are walking throught the jungle and you find two paths which one you chose "right" or "left"? \n')
one_lower = one.lower()
if one_lower == "left":
  two = input('You continue walking and arrive to the river, do you prefer to "swim" or "wait"? \n')
  two_lower = two.lower()
  if two_lower == "wait":
    three = input('Uju! You find a house in the middle of nowhere, but which door you are going to open? "Blue", "Yellow" or "Red"? \n')
    three_lower = three.lower()
    if three_lower == "blue":
      print(":(, you were eaten by beasts. Game Over.")
    elif three_lower == "red":
      print("Aush!, you were burn by fire. Game Over.")
    elif three_lower == "yellow":
      print("You Win! You find the treasure!")
    else:
      print("Game Over.")
  else:
    print("Rghhh!, You were attack by trout. Game Over.")
else:
  print("Ups! You fall into a hole. Game Over.")


