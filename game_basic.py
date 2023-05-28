"""
started: 5/27/2023
Goal: Create a simple choice sub game
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
import random
import easygui

entityChoice = ['Ghoul', 'Angel', 'Demon', 'Human', 'Other']
deathCauses = ['Hit by a truck', 'Poisoned', 'Suicide', 'Murdered', 'Old age']
points = 0
totalPossible = 0

questions_answers = [
    {
        'question': "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        'answer': "An echo."
    },
    {
        'question': "What has keys but can't open locks?",
        'answer': "piano"
    },
    {
        'question': "Everyone has it but others use yours more than you do. What is it?",
        'answer': "Name"
    },
    {
        'question': "What can you catch but not throw?",
        'answer': "cold"
    },
    {
        'question': "I have cities, but no houses. I have forests, but no trees. I have rivers, but no water. What am I?",
        'answer': "map"
    },
    {
        'question': "What is the capital city of France?",
        'answer': "Paris"
    },
    {
        'question': "Who painted the Mona Lisa?",
        'answer': "Leonardo da Vinci"
    },
    {
        'question': "What is the largest planet in our solar system?",
        'answer': "Jupiter"
    },
    {
        'question': "What is the chemical symbol for gold?",
        'answer': "Au"
    },
    {
        'question': "Which country is known as the 'Land of the Rising Sun'?",
        'answer': "Japan"
    },
    {
        'question': "The more you take, the more you leave behind. What am I?",
        'answer': "Footsteps"
    },
    {
        'question': "This thing all things devours: birds, beasts, trees, flowers;\ngnaws iron, bites steel; grinds hard stones to meal; \nslays kings, ruins towns,and beats high mountains down. What is it?",
        'answer': "Time"
    },
    {
        'question': "What has a heart that doesn't beat?",
        'answer': "Deck of Cards"
    },
    {
        'question': "I am an odd number. Take away a letter, and I become even. What number am I?",
        'answer': "Seven"
    },
    {
        'question': " am the beginning of the end, and the end of time and space.\nI am essential to creation, and I surround every place.",
        'answer': "E"
    }
]


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

    def Quest_Branching_Initial(self):
        correct_answers = 0  # Track the number of correct answers

        #loops until user gets atleast two correct answer   
        while correct_answers < 2: 
            question_dict = random.choice(questions_answers)
            branching_question = question_dict['question']
            branching_User_answer = easygui.enterbox(question_dict['question'], title='Input')

            if branching_User_answer.lower() == question_dict['answer'].lower():
                easygui.msgbox("Your answer was correct!", title='Information')
                points += 2
                correct_answers += 1  # Increment the correct answers count
            else:
                easygui.msgbox("Your answer was incorrect! Good luck on the next question", title='Information')
                self.Quest_Branching_Initial()
                points +=1

            totalPossible+=2 #tally of correct answers' points - Smart path
            
        
        def Smart_Quest(self):
            pass


        def Mercenary_Quest(self):
            pass

        def Heroic_Quest(self):
            pass

        def Villain_Quest(self):
            pass




        if totalPossible == points:
            #all correct correct - Smart path
            pass
        elif points %2 == 0:
            #even numbers are possible full score - mercenary/villain
            pass
        elif points %2 != 0:
            #odd number possible incorrect answer -friend/hero
            pass
        
        
        

        


    

    def Quest(self):
        startAd =['Yes','No','Maybe']
        quest_choice = easygui.buttonbox("Would you like to start an adventure:", choices=startAd)
        
        match(quest_choice):
            case 'Maybe': 
                easygui.msgbox("Your second chance at life was ruthlessly revoked. In this realm, indecision finds no sanctuary.")
            case 'No': 
                easygui.msgbox("This realm has no place for cowards. You will start the quest or die ")
                self.Quest()
            case 'Yes':
                self.Quest_Branching_Initial()
                

                

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
