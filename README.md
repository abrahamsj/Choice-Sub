# Choice-Sub


### If you want to replicate the game you should request you api key from the site below

REQUEST KEY FROM `https://www.wordnik.com/`

    `url = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&includePartOfSpeech=noun&minLength=5&maxLength=10&api_key=YOUR_API_KEY"`

    Above you see where you'll need the api key for the Smart quest Puzzle Chamber


This project is an attempt at Choice-Sub adventure game.


It starts by collect user info then randomly generates the character as well as their backstory.
The desired game play is outlined below:

Answer initial questions to be branched off to a quest
quest
    - villain
        - doesn't see hero path 
        - low score on intial questions
    - heroic
        - doesn't see villan path
        - half or more of total possible scores from initial questions
    - smart
        - see all path
        - all possible scores from intial questions 
    - Mercenary 
        - can see both villain of hero path
        - Randomselection

        -depends on answers to the previous questions
        - branch: for friend

Stretch Goal: 
- Background music
- show stats...leader board
- allow for sub quest to be limited depending on points
- EXTRA Stretch Goal : visuals
- Longshot: make available online 
