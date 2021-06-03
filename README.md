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


# Notes
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
- Key is ID #, value is another dict containing key of "question" and "used", corresponding to question text and boolean of whether or not question has been used this game or not
- list for QIDs of unused questions
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

## Questions
- What do they mean by describe use cases? 
    - Walkthrough all the features and how to use.
- Do I need to worry about user credentials/types of users?
    - No, too short a timeframe
- Think about if there's a better way to show "Press 'x'" message during continuous play. Currently pops up along with every question. Could add another sleep?
