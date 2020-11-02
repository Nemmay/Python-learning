#A rock, paper, scissor imitator.
#0 = rock, 1 = paper, 2 = scissor.
import random #import random module
options = ['rock', 'paper', 'scissors'] #create a list and assign its values.
player = ' ' #set player to empty value so its is visible and accessible outside the loop
while True: #while loop set to true, so it runs till a condition makes it evaluate to False.
    player = input("Rock, Paper, Scissors: ") #player input.
    computer = random.choice(options) 
    if player.lower() ==  options[2] and computer == options[1]:
        print("You lose. computer chose {} and you chose {}".format(computer, player))
        break
    elif player.lower() == options[0] and computer == options[1]:
        print("You lose! Computer chose {}, You chose {}".format(computer, player))
        break
    elif player.lower() == options[0] and computer == options[2]:
        print("You win! {} beat {}.".format(player, computer))
        break
    elif player.lower() == options[1] and computer == options[0]:
        print("You win! Computer chose {} you chose {}".format(computer, player))
        break
    elif player.lower() == options[1] and computer ==options[2]:
        print("You lose! Computer chose {}, you chose {}".format(computer, player))
        break
    elif player.lower() == options[2] and computer == options[0]:
        print("You lose! computer chose {} and you chose {}.".format(computer, player))
        break
    else:
        print("it's a draw. computer chose {}, you chose {}".format(computer, player))
        break