import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#You
rps = [rock, paper, scissors]
you_chose = int(input("Type 0 for rock, 1 for paper and 2 for scissors. "))
your_choice = rps[you_chose]
printed_your_choice = print(f"You chose: {your_choice}")

#Comp
random_rps = random.randint(0, 2)
comp_choice = rps[random_rps]
printed_comp_choice = print(f"Computer chose: {comp_choice}")

if your_choice == comp_choice:
  print("Draw!")
elif your_choice == 0 and comp_choice == 1:
  print("Computer wins!")
elif your_choice == 0 and comp_choice == 2:
  print("You win!")
elif your_choice == 1 and comp_choice == 0:
  print("You wins!")
elif your_choice == 1 and comp_choice == 2:
  print("Computer wins!")
elif your_choice == 2 and comp_choice == 0:
  print("Computer wins!")
else:
  print("You win!")








