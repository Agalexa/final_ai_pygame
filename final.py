import cmd
import sys
import os
import time
import random
import cutie

class player:

    def __init__(self):
        default_morality = 5
        self.name = 'default'
        self.morality = default_morality # five is neutral, 0-4 is "bad", 6-10 is "good"
        self.location ='start'
        self.attribute = 'default'
        self.attack = 0
        self.evasion = 0
        self.health = 100
        self.mana = 0
        self.tech = 0
        self.inventory = ['backpack ','contents:', 'water: ', 1, 'gold: ', 10]
        self.map_list = []

    def print_info(self):
        #print ("player name " + self.name + "\nhealth " + self.health "\nmorality " + str(self.morality) + '\nmana ' + str(self.mana) + '\ntech ' + str(self.tech))
        return 0
    def change_morality(self, delta):
        print ("Morality changed by " + str(delta) + " points!")
        self.morality = self.morality + delta
        print ("New moral standing is " + str(self.morality))
    def back_pack(self):
        num = 1
        scroll(self.inventory[0] + self.inventory[1])
        for x in range (len(self.inventory)- 3) :
            num = num + 1
            if ((num % 2) == 0):
                scroll('\n' + str(self.inventory[num]) + str(self.inventory[num + 1]))
        time.sleep(1.5)

def help_menu():
    print('####################')
    print('# welcome to the text rpg! #')
    print('####################')
    print ('good luck!')
    #title_screen_selections()


######## slowed text
def scroll(stringy):
    for character in stringy:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)        
    time.sleep(0.05)

def scroll_custom(stringy,numy):
    for character in stringy:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(numy)       
######## slowed text 

def get_input():
    player_input = input()
    return player_input

##########
def initialize_game():
    scroll('\n.............')
    scroll('\nInitializing program')
    scroll('\n...loading...')
    scroll('\n...loading...')
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#            -   want   -               #',0.02)
    scroll_custom('\n#            -    to   -                #',0.02)
    scroll_custom('\n#            -   play?   -              #',0.02)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)    
    return_variable = 0
    options = ['play','quit']
    cute_option = options[cutie.select(options)]
    if cute_option == 'play':
        return_variable = 1
    elif cute_option == 'quit':
        return_variable = 2
    return return_variable

def character_creation():
    scroll('\nyou awake in a dark cave, not quite sure where you are or what happened...\nyou hear a distant voice...')
    scroll_custom('\nwhat is your name young one? ',0.10)
    namey = input()
    playerOne = player()
    playerOne.name = namey
    scroll("well... " + playerOne.name + '\ndo you reside in the enchanted forest or the electric city? ')
    mana_or_tech = get_input()
    if mana_or_tech == 'enchanted forest':
        stringy1 = 'mana'
        playerOne.mana = 100
    elif mana_or_tech == 'electric city':
        stringy1 = 'tech'
        playerOne.tech = 100
    scroll('\nare you a fox or a bull? ')
    attac_or_def = get_input()
    if attac_or_def == 'bull':
        playerOne.attack = 100
        stringy = 'attack'
    elif attac_or_def == 'fox':
        playerOne.evasion = 100
        stringy = 'evasion'
    scroll('This is good to know ' + playerOne.name + ' this means you have a ' + stringy1 + ' of ' + str(playerOne.mana) + ' and an ' + stringy + ' of ' + str(playerOne.evasion))
    scroll('\nYou will need these attributes for whats to come...')
    time.sleep(.2)
    scroll_custom('\n...',0.08)
    time.sleep(.2)
    scroll_custom('\n...',0.08)
    os.system('cls')

    return playerOne

def first_encounter(playerChar):
    #results: 'trail', 'bird_friend', 'bird_damage'
    playerOne = playerChar
    end_encounter = ''
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)    
    scroll('\nyou feel the ground slip beneath you...\nand suddenly...')
    scroll('\nyou find yourself in a grassy field')
    scroll('\nthere\'s a trail ahead...\n\n')
    choices = ['do nothing','follow it']
    cute_choices = choices[cutie.select(choices)]
    if cute_choices == 'follow it':
        os.system('cls')
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)  
        scroll('\nyou continue on the path...')
        time.sleep(0.5)
        end_encounter = 'trail'

    elif cute_choices == 'do nothing':
        os.system('cls')
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)  
        scroll('\nyou lay down in the grass')
        scroll('\nyour eyelids feel heavy as you fall asleep...')
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)  
        scroll('\nsuddenly! you\'re shot awake by the sound of\n a giant bird landing at your feet')
        scroll('\nit towers over you, and as menacing as it looks\nit appears to be intelligent enough to speak...')
        time.sleep(1)
        scroll_custom('\nwhat do you do???',0.01)
        print('\n\n')
        bird_choice = [ 'insult the bird','compliment the bird']
        cutie_bird = bird_choice[cutie.select(bird_choice)]
        if cutie_bird == 'compliment the bird':
            os.system('cls')
            scroll('\nshockingly, the bird understood you...\nBIRD: \'SQUAWWWWWKKKKKKK thanks! I just got my feathers done\'\nBIRD: \'you look a little lost kid, need a lift?\'')
            scroll('\nthe bird gives you a ride into town...')
            scroll('\nas it lets you off and flies away, you notice you\'re wearing a backpack...\nwas it there the whole time?')
            end_encounter = 'bird_friend'
        elif cutie_bird == 'insult the bird':
            os.system('cls')
            scroll('\nsuprisingly, the bird understood you...\nBIRD: \'SQUAWWWWWKKKKKKK!!!!!\'')
            scroll('\ninsulted, the bird lunges to eat you!!!')
            if playerOne.evasion == 100:
                scroll('\nusing your evasive skills, you barely roll out of the way in time\nhaving taken a little damage you keep running down the trail and never look back!')
                playerOne.health = 80
                end_encounter = 'bird_damage'
            else:
                scroll_custom('\n#########################################',0.001)  
                scroll('\nGAME OVER: the mighty bird swallows you whole.')
                sys.exit('Thanks for playing!')
    return end_encounter

def second_encounter(first_result, thePlayer):
    playerOne = thePlayer
    firstResult = first_result
    second_result = ''
    if firstResult == 'trail':
        scroll('\nyou wander down the trail until you find a town...')
        scroll('\noddly, you just notice you\'ve been wearing a backpack...\nwas it on this whole time?')
        scroll('\nyou check its contents...\n')
        time.sleep(0.3)
        playerOne.back_pack()
        os.system('cls')
        scroll_custom('\n#########################################',0.001)  
        scroll('\nwithin this town you come across a man who is dying of thirst')
        scroll('\ngive him some of your water?')
        print('\n')
        water_choice = ['give him some','drink your water in front of him']
        cutie_water = water_choice[cutie.select(water_choice)]
        if cutie_water == 'give him some':
            scroll('\nyou give the dying man some water and he springs back to life!')
            scroll('\nMAN: thank you so much!')
            scroll('\nthe old man runs off into the sunset\nand you rest easy knowing you did a good deed\n')
            playerOne.change_morality(3)
            second_result = 'saved'
            print('\nmorality : ' + str(playerOne.morality))

        else: 
            #cutie_water == 'drink your water in front of him'
            second_result = 'dyed'
            scroll('\nwow you\'re a terrible person')
            scroll('\nthe old man gasping for water sees you... and in his last moment...\ncurses you.\n')
            time.sleep(1)
            playerOne.change_morality(-3)
            print('\nmorality : ' + str(playerOne.morality))
            time.sleep(1)

    else:
        scroll_custom('\n#########################################',0.001)  
        scroll('\nwithin this town you come across a man who is dying of thirst')
        scroll('\ngive him some of your water?')
        print('\n')
        water_choice = ['give him some','drink your water in front of him']
        cutie_water = water_choice[cutie.select(water_choice)]
        if cutie_water == 'give him some':
            scroll('\nyou give the dying man some water and he springs back to life!')
            scroll('\nMAN: thank you so much!')
            scroll('\nthe old man runs off into the sunset\nand you rest easy knowing you did a good deed\n')
            playerOne.change_morality(3)
            second_result = 'saved'
            print('\nmorality : ' + str(playerOne.morality))
            time.sleep(1)

        else: 
            #cutie_water == 'drink your water in front of him'
            second_result = 'dyed'
            scroll('\nwow you\'re a terrible person')
            scroll('\nthe old man gasping for water sees you... and in his last moment...\ncurses you.\n')
            time.sleep(1)
            playerOne.change_morality(-3)
            print('\nmorality : ' + str(playerOne.morality))
            time.sleep(1)

def third_encounter(thePlayer):
    playerOne = thePlayer
    os.system('cls')
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll_custom('\n#########################################',0.001)
    scroll('\nif you wish to beat this game\nyou must go to the mountain and face the monster!')
    scroll('\nhowever, you feel famished...\nyou decide to stop by the local tavern and get some food')
    if playerOne.morality > 6:
        scroll('\nTAVERN MASTER: welcome friend!\nwe saw what you did for that old man and we appreciate your kind around here')
        scroll('\nTAVERN MASTER: I\'ve heard your trying to face the dragon at the top of the mountain...\nyou\'ll need this if you want to survive')
        playerOne.inventory.append('Special item: ')
        playerOne.inventory.append(1)
        scroll('\nuse this item at the right time and you will be able to deal with the monster!')
        scroll('\nwith a full belly and the special item you head to the mountain...')
    else:
        scroll('\nTAVERN MASTER: I\'m sorry but we saw the way you treated that old man\nwe don\'t want people like you around here')
        scroll('\nwith nothing else to do you head of to the mountain to face the dragon')

def last_encounter(thePlayer):
    playerOne = thePlayer
    if playerOne.morality > 6:
        os.system('cls')
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)
        scroll('\nyou approach the dragon\'s layer and you hear a voice!')
        scroll('\nDRAGON: what do you want?')
        scroll('\nwith fear in your heart you reach into your backpack\nand produce the special item')
        scroll('\nthe dragon upon seeing the item reels back in delight...')
        scroll('\nDRAGON: finally! my delivery is here... usually grubhub has better service on weeekends\nI hope you know this means I\'m not tipping you.')
        time.sleep(1)
        scroll('\ncongrats! you beat the game by not being a jerk!')
        time.sleep(1)
        sys.exit('have a good one!')

    else:
        os.system('cls')
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)
        scroll_custom('\n#########################################',0.001)
        scroll('\nyou approach the dragon\'s layer and you hear a voice!')
        scroll('\nDRAGON: what do you want?')
        scroll('\nwith fear in your heart you mutter something\nabout coming to face the dragon')
        scroll('\nwithout letting you get through your sentence the dragon swallows you whole')
        scroll('\ngame over! next time don\'t  be a jerk!')
        time.sleep(1)
        sys.exit('game over!')

def main():
    playerOne = player()
    start_variable = initialize_game()
    if (start_variable == 1):
        print('very good then')
        time.sleep(1)
        os.system('cls')
        playerOne = character_creation()
    else:
        sys.exit('Have a good one!')
    
    encounterFirst = first_encounter(playerOne)
    encounterSecond = second_encounter(encounterFirst, playerOne)
    third_encounter(playerOne)
    last_encounter(playerOne)

main()