import easygui
import requests


class SmartQuest:
    def Smart_Quest(self):
        smartQ_welcome = """
        Welcome, Knowledge-Seeker!\n
        Your responses to the initial questions have revealed your exceptional intellect and thirst for knowledge.\n
        As such, you are deemed worthy to embark on a quest to attain even greater wisdom that shall serve you well in your new life.\n
        Your insatiable curiosity and cultivated resilience will be invaluable assets in your endeavors.\n
        Prepare yourself, for the challenges that lie ahead will test your intellect, reasoning, and problem-solving abilities.\n
        May you emerge from this quest not only with knowledge but also with a profound understanding of the world around you.
        Let the pursuit of wisdom guide you as you step into the realm of endless possibilities!\n
        """

        easygui.msgbox(smartQ_welcome, "Story")

        # CONTINUE WITH THE QUEST CONTENT

        items = ["Puzzle Chambers", "Ancient Scrolls", "Library of Knowledge", "Memory Challenges", "Scientology", "Mind Games", "Historical Enigmas"]
        smart_Qchoice = easygui.choicebox("Select the type of quest you would like to embark on:", choices=items, title="Quest Option")
        if smart_Qchoice is None:
            print("User selected:", smart_Qchoice)
        else:
            match smart_Qchoice:
                case "Puzzle Chambers":
                    puzzleChamber_welcome = """
                    Welcome, Seeker of Knowledge, to the Enigma of Intellect!
                    As you step into the realm of Puzzle Chambers, a world of boundless curiosity unfolds before you.
                    Prepare to embark on a cerebral odyssey, where the very fabric of logic and reason weaves intricate webs of challenges.
                    Within these hallowed walls, mysteries await, demanding your astuteness, your ingenuity, and your insatiable thirst for knowledge.
                    Unleash the full potential of your mind as you confront mathematical enigmas, unravel cryptic codes, and decipher complex patterns.
                    Every puzzle is a stepping stone, a gateway to unparalleled enlightenment, and the key to unlocking the secrets of this labyrinthine chamber.
                    Venture forth with unwavering determination, for the rewards that lie ahead are not mere trinkets, but profound insights and intellectual growth.
                    Embrace the thrill of unraveling each enigma, for within their depths, you will discover the wisdom that shall shape your destiny.
                    Remember, it is not only the destination that matters, but the transformative journey of the mind.
                    """

                    easygui.msgbox(puzzleChamber_welcome, "Welcome to the Puzzle Chamber")

                    # Generate and solve puzzle questions
                    for _ in range(5):
                        question = generate_anagram_question()
                        solve_anagram_question(question)

                case "Ancient Scrolls":
                    pass  # Handle "Ancient Scrolls" quest

                case "Library of Knowledge":
                    pass  # Handle "Library of Knowledge" quest

                case "Memory Challenges":
                    pass  # Handle "Memory Challenges" quest

                case "Scientology":
                    pass  # Handle "Scientology" quest

                case "Mind Games":
                    pass  # Handle "Mind Games" quest

                case "Historical Enigmas":
                    pass  # Handle "Historical Enigmas" quest


def generate_anagram_question(): #API KEY PENDING
    url = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&includePartOfSpeech=noun&minLength=5&maxLength=10&api_key=YOUR_API_KEY"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        anagram = data["word"]
        word = anagram.upper()
        return word
    else:
        return None


def solve_anagram_question(question):
    if question:
        user_answer = easygui.enterbox(f"Unscramble the word: {question}", title="Puzzle Question")
        user_answer = user_answer.upper()

        if user_answer == question:
            easygui.msgbox("Congratulations! Your answer is correct.", title="Correct Answer")
        else:
            easygui.msgbox("Sorry, your answer is incorrect.", title="Incorrect Answer")
    else:
        easygui.msgbox("Failed to generate the question. Please try again later.", title="Error")