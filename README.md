## Task
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


## Notes
- starting with cmd line implementation
- challenges are:
    - how to get user input while loop is running (questions every x seconds)
        - need this to get back out to menu
- store Qs and asked boolean in dict. structure like: questions = {1 : {text : "What was your childhood nickname?", asked : False}, 2 : {text : ...} }
    - consider storing values as list instead, for easy indexing
- keep tabs on unasked questions in list, perhaps?
- web scraping? no, I don't remember it very well
- copy/paste into a CSV, read in from CSV
- at one point I thought to make a function to populate the questions dict, but then I can't access the whole dict outside the scope of that function

### Functions I need
- user input to get question
- pick question from unused list, use that id to index into the dict
- mark question used (for dict), also removes from unused list
- 

### Structure
- dict for questions
- Key is ID #, value is another dict containing key of "question" and "used", corresponding to question text and boolean of whether or not question has been used this game or not
- list for QIDs of unused questions

## Questions
- What do they mean by describe use cases? 
    - Walkthrough all the features and how to use.
