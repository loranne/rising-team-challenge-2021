# Notes
My Magic Hat game uses an interactive command line interface to show the player a menu with gameplay options, along with the icebreaker questions that form the meat of the game. For ease of use and simplicity, I tried not to use too many extra dependencies or non-built-in modules (the one exception being termcolor). I chose this interface rather than building a webapp because it was faster for me, and given the data-light nature of the game, I felt a webapp would have heading into overkill territory. 

The primary data for my game&mdash;that being the questions themselves, and their ID numbers&mdash;is managed with three core data structures: a dictionary with the ID numbers as the keys, and the question texts as the values; a set of question IDs for all questions that have been encountered in this game session; and a list containing all the IDs for questions that have *not* been seen this session, which re-populates when the player has cycled through all available questions.

The data for the dictionary is read in from a CSV I created using data from the Conversation Starters website you pointed me to (https://conversationstartersworld.com/icebreaker-questions/). 

I chose a dictionary for its ease of use and the ability to associate the two most important values directly with one another: the questions and ID numbers. The set exists as an efficient way to keep tabs on all questions that the player has already seen. The list was chosen because Python deprecated the ability to select randomly from sets in 3.9, and that randomness is a core component of my pick question function. 

The bulk of the code is in one file, magic_hat.py. While I didn't have time to add integration or unit tests, the way I've blocked my code into these functions would make for easier testing in the future. Instead, I made sure to validate user input at every turn. 

I was able to add a couple of bonus features (users can view and add questions, either temporarily or permanently), and had ideas for more, but ran out of time. 

# Installation
- Clone this repo.
- Pip install from requirements.txt.

# How to Play
- In your terminal, run magic_hat.py.
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

# Task
Home coding exercise (4-8 hours)
- Magic hat is a game you can play with your team, where you pick a question out of a hat, as a team building exercise. Examples of questions would be “what was your childhood nickname?” Or “what is your favorite emoji and why?”.
- Can you build a game where the user can do the following:
    - Ask the hat to give you a question.
    - Ask the hat to ask questions every X seconds.
    - Ask the hat to turn off the periodic questions. 
    - The hat should not repeat questions that have been asked before (unless they've all been asked already)
- Please describe your architecture, instructions to run the code, use-cases, and link to code repo. Feel free to add any advanced features that you can think of. 
- List of icebreaker questions you can use
    - https://conversationstartersworld.com/icebreaker-questions/
- Your interface can be command line or browser.
- Your time is valuable, please stop at 8 hours, do not spend time making this perfect!
- Perfectly fine to stop between 4 and 8 hours, just let me know how much time you spent.
- Tips
    - Focus on functionality first, UI and bells and whistles can always be tweaked later
    - If you have a question, note the question, come up with your best guess, and keep going. Feel free to email me with questions but please don't wait for an answer if you are ready to start.

# Brainstorming
- starting with cmd line implementation
- challenges are:
    - how to get user input while loop is running (questions every x seconds)
    - dividing up program into the right functions. be careful they don't creep up in size as I think of other features/needs
    - right data structure for holding questions info
- store Qs and asked boolean in dict. structure like: questions = {1 : {text : "What was your childhood nickname?", asked : False}, 2 : {text : ...} }
    - consider storing values as dict, for easy indexing
- keep tabs on unasked questions in list, perhaps?
- web scraping? no, I don't remember it very well
- copy/paste into a CSV, read in from CSV. Could maybe scrape the website for Qs, but for such a small set, might not be worthwhile.

## Functions I need
- populate structure with question 
- user input to get single or multi-question mode
- pick question from unused list, use that id to index into the dict
    - mark question used (for dict), also removes from unused list
- get questions periodicially, based on time input by user
- play game (calls other functions within)

## Structure
- dict for questions
- Key is ID #, value is question text
- list for QIDs of unused questions
- set of QIDs for used questions
- write all other functions first, then play game function at end
- smaller helper functions can go within other function scope (like is_input)

## Extra features
- ~~user add question~~
- ~~user view questions~~
- ask X total questions at intervals of Y
- question packs (i.e. questions on a theme, for a specific type of team, etc.)
- user favorite questions
- user remove questions
- track frequency of each question

## Questions/thoughts
- What do they mean by describe use cases? 
    - Walkthrough all the features and how to use.
- Do I need to worry about user credentials/types of users?
    - No, too short a timeframe
- Think about if there's a better way to show "Press 'x'" message during continuous play. Currently pops up along with every question. Could add another sleep?
