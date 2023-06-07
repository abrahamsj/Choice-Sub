import easygui
import random
from SmartQuest import SmartQuest

questions_answers = [
    {
        'question': "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        'answer': "echo."
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
        'question': "What is the last name of the person who painted the Mona Lisa?",
        'answer': "DaVinci"
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
        'answer': "Cards"
    },
    {
        'question': "I am an odd number. Take away a letter, and I become even. What number am I?",
        'answer': "Seven"
    },
    {
        'question': "I am the beginning of the end, and the end of time and space.\nI am essential to creation, and I surround every place.",
        'answer': "E"
    }
]


class Quest_Branching:
    def Quest_Branching_Initial(self):
        quest = SmartQuest()
        
        correct_answers = 0  # Track the number of correct answers
        total_questions = 2  # Set the total number of questions

        for _ in range(total_questions):
            question_dict = random.choice(questions_answers)
            branching_question = question_dict['question']
            branching_User_answer = easygui.enterbox(question_dict['question'], title='Input')

            if branching_User_answer.lower() == question_dict['answer'].lower():
                easygui.msgbox("Your answer was correct!", title='Information')
                correct_answers += 1  # Increment the correct answers count
            else:
                easygui.msgbox("Your answer was incorrect! Good luck on the next question", title='Information')

        totalPossible = 2 * total_questions  # Total possible points for all questions
        points = 2 * correct_answers  # Points earned based on correct answers

        if totalPossible == points:
            # All answers are correct - Smart path
            quest.Smart_Quest()
        elif points % 2 == 0:
            # Even number of correct answers - Mercenary/Villain path
            pass  # Handle Mercenary/Villain quest
        elif points % 2 != 0:
            # Odd number of correct answers - Friend/Hero path
            pass  # Handle Friend/Hero quest

        return totalPossible, points
