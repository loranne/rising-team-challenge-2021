# Notes
My Magic Hat game uses an interactive command line interface to show the player a menu with gameplay options, along with the icebreaker questions that form the meat of the game. For ease of use and simplicity, I tried not to use too many extra dependencies or non-built-in modules (the one exception being termcolor, which I use in a utility that colorizes print statements). I chose this interface rather than building a webapp because it was faster for me, and given the data-light nature of the game, I felt a webapp would have heading into overkill territory. 

The primary data for my game&mdash;that being the questions themselves, and their ID numbers&mdash;is managed with three core data structures: a dictionary with the ID numbers as the keys, and the question texts as the values; a set of question IDs for all questions that have been encountered in this game session; and a list containing all the IDs for questions that have *not* been seen this session, which re-populates when the player has cycled through all available questions.

The data for the dictionary is read in from a CSV I created using data from the Conversation Starters website you pointed me to (https://conversationstartersworld.com/icebreaker-questions/). 

I chose a dictionary for its ease of use and the ability to associate the two most important values directly with one another: the questions and ID numbers. The set exists as an efficient way to keep tabs on all questions that the player has already seen. The list was chosen because Python deprecated the ability to select randomly from sets in 3.9, and that randomness is a core component of my pick question function. 

The bulk of the code is in one file, magic_hat.py. While I didn't have time to add integration or unit tests, the way I've blocked my code into these functions would make for easier testing in the future. Instead, I made sure to validate user input at every turn. 

I was able to add a couple of bonus features (users can view and add questions, either temporarily or permanently), and had ideas for more, but ran out of time. 

# Installation
- Clone this repo.
    `git clone https://github.com/loranne/rising-team-challenge-2021.git`
- Pip install from requirements.txt.
    `pip install -r requirements.txt`

# How to Play
- In your terminal, navigate to the directory where you cloned the repo.
- Run magic_hat.py
    `python3 magic_hat.py`
- A welcome message, followed by menu options, will be displayed in the output.
- To make your selection, type the corresponding letter, then press "Return"
- Each option is described within the menu, but to elaborate:
    - A) Print one question to the console.
    - B) Continuous question mode. If you select this option, you will then be prompted to indicate how often (in seconds) you'd like to receive a new question. You can enter any positive integer up to 1,800 (half an hour). 
        - To exit this mode once activated, type "x", then press "Return". It will take a full time cycle (based on how often you chose to see a new question) to exit continuous mode, so you may need to be patient!
    - C) Add a question of your own. You'll be prompted to type in a question, then press "Return". 
        - After you've entered your question, you will be asked whether you'd like to save your question for future use. Choosing "yes" will write this question into the CSV that populates the dictionary for future game sessions. Choosing "no" will allow you to use your question during *your current* game session only.
    - D) View questions. You'll be prompted to choose which set of questions you'd like to view: all questions, just the ones you've seen at some point in this game session, or just the questions you *haven't* yet seen in this game session.
    - Q) Quit. This ends your game and closes the program.
- If you get stuck, you can always press Ctrl + C to force quit the program. 