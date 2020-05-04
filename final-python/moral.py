#  build game to demonstrate simple ai morality construct.
#  User will have a backend integer value representing their relative moral standing 
#  value will change depending on player's actions.
#  Will go up or down, and it will affect what actions/events the player
#  can engage in and how they are treated.
import pygame


class player:

    def __init__(self, name):
        self.name = name
        self.morality = 5 # five is neutral, 0-4 is "bad", 6-10 is "good"
    
    def print_info(self):
        print ("Player name " + self.name + "\nMorality " + str(self.morality))

    def change_morality(self, delta):
        print ("Morality changed by " + str(delta) + " points!")
        self.morality = self.morality + delta
        print ("New moral standing is " + str(self.morality))


###


class non_player:

    def __init__(self, name, morality):
        self.name = name
        self.morality = morality

    def print_info(self):
        print ("Name " + self.name + "\nMorality " + str(self.morality))

    def reaction(self, moral_value):
        if (self.morality <= moral_value):
            print("Hello friend! Come on through")
            return "friend"
        else:
            print("I'm sorry stranger, but we're closed")
            return "stranger"

FirstPlayer = player("John")
NonPlayerFirst = non_player("Larry", 7) #higher than average morality 

print (FirstPlayer.name + " is walking through the woods, you comes across a cat stuck in a tree.")
input_one = input("Take the time to help the cat?       [Y/N]: ")
if ((input_one == "Y") or(input_one == 'y')):
    print ("You saved the cat! Mr.fluffies scurries on home and you go on your way")
    FirstPlayer.change_morality(2)
else:
    print ("You pass by, ignoring the desperate meows of Mr.fluffies")


print("You continue walking, and come across a bar with a man standing in the doorway")
print("You approach the man, asking if you may enter")

reaction_one = NonPlayerFirst.reaction(FirstPlayer.morality)


    














#playerOne = Player('John')
#playerOne.example_fun()