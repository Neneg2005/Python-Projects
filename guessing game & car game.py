
"""Guessing Game and Car Game

Guessing: You guess 3 numbers. If you are right the program tells you that you have won otherwise you fail after 3 tries.
"""

secret = 13
initial = 0
limit = 3

while initial < limit:
    game = int(input("Guess a number:  "))
    initial += 1
    if game == secret:
        print("Congrats, you won! ")
        break
else:
   print("You lost:( ")

"""Car: When you enter commands like: start,stop, help and quit, the program works. Also, if a command is repeated, the code tells you so."""

started = False
stopped = False

while True:
  command = input("> ").lower()
  if command == "start":
    if started:
      print("Car is already started!")
    else:
      started = True
      print("Car started....ready to go")
  elif command == "stop":
    if stopped:
      print("Car is already stopped!")
    else:
      stopped = True
      print("Car stopped")
  elif command == "help":
    print("""
start - to start the car
stop - to stop the car
quit - to exit
    """)
  elif command == "quit":
      break
  else:
    print("Hey, I don't understand that....")
