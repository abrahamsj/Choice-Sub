"""
started: 5/27/2023
Goal: Create a simple choice sub game
possible addition (seen when updating)
    - A function to tally and display points/status


quest
    - villain
        - doesn't see hero path 
    - heroic
        -doesn't see villan path
    - smart
        - see all path
    - Mercenary 
        - can see both villain of hero path

        -depends on answers to the previous questions
        - branch: for friend

Stretch Goal: Background music
EXTRA Stretch Goal : visuals
Longshot: make available online 

"""

# importing needed libraries
import random
import easygui
from QuestBranching import Quest_Branching

entityChoice = ['Ghoul', 'Angel', 'Demon', 'Human', 'Other']
deathCauses = ['Hit by a truck', 'Poisoned', 'Suicide', 'Murdered', 'Old age']

QBranchingObj = Quest_Branching()

class Player:
    def __init__(self):
        self.name = ""
        self.being = ""

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_being(self, being):
        self.being = being

    def get_being(self):
        return self.being

    def StartingBeing(self):
        self.being = random.choice(entityChoice)

    def Story(self):
        death_cause = random.choice(deathCauses)
        story = """Welcome, adventurer! Fate has dealt you a fatal blow, causing your untimely demise.\n Cause of Death:  {}.\n
                However, the universe has granted you a rare second chance at life. Brace yourself, for you will be reborn as a {}.

                Embark on a perilous quest, for you hold the key to unlocking a coveted treasure that awaits at the journey's end. But heed this warning: trust not too easily, for treachery lurks in the shadows. Yet, do not be overly guarded, for the path ahead is fraught with dangers only surmountable with the aid of steadfast companions. In this realm of uncertainty, camaraderie may prove to be your sole salvation.

                Prepare yourself, adventurer, as you step into this extraordinary world teeming with intrigue, challenges, and the promise of great reward. Your destiny awaits, and only through cunning, resilience, and alliances forged in the crucible of danger can you hope to emerge victorious.""".format(death_cause, self.being)

        easygui.msgbox(story, "Story")
        self.Quest()

    def Quest(self):
        startAd = ['Yes', 'No', 'Maybe']
        quest_choice = easygui.buttonbox("Would you like to start an adventure:", choices=startAd)

        if quest_choice == 'Maybe':
            easygui.msgbox("Your second chance at life was ruthlessly revoked. In this realm, indecision finds no sanctuary.")
        elif quest_choice == 'No':
            easygui.msgbox("This realm has no place for cowards. You will start the quest or die ")
            QBranchingObj.Quest_Branching_Initial()
        elif quest_choice == 'Yes':
            QBranchingObj.Quest_Branching_Initial()

    def gameSetup(self):
        self.name = easygui.enterbox("Enter your name:")
        self.StartingBeing()
        easygui.msgbox("Hello, {}. You will now start your new life as a {}".format(self.name, self.being))
        self.Story()


# Function to run the game as a whole
def main():
    player = Player()
    player.gameSetup()


# Code to run game
if __name__ == "__main__":
    main()
