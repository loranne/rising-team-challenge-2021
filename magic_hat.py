# Magic Hat icebreaker questions game
import csv 
import random
import select
import sys
import time
# my own module to convert print statements to color
import utils


def populate_questions():
    """Populates dictionary of questions, IDs, and used values (default to false) 
    using data from CSV file"""
    
    # empty dict. question text and ids will live here
    questions = {}
    # list of IDs for Qs not used in current pass through list
    # need to be able to select randomly, which is why it's a list, not set
    not_used_qids = []
    # set of Q IDs that have been seen this whole game
    used_qids = set()

    # use csv module to read in data
    with open("questions.csv", "r") as csvfile:
        # skip first row, which is only labels
        next(csvfile)
        # separate rows on | character
        reader = csv.reader(csvfile, delimiter = "|")

        # unpack row values
        for row in reader:
            q_id, q_txt = row
            # q_id was a string, coming in from csv, so call int while populating dict
            # all used values set to false at beginning
            questions[int(q_id)] = q_txt
            # add ID of each question to unused qids list
            not_used_qids.append(int(q_id))

    # returns both the dict and the list of used_qids for further use in game
    return questions, not_used_qids, used_qids


def get_play_mode():
    """Prints user options for playing the game. Takes user input and returns 
    game mode"""
    
    #TODO: If time, split into play and settings modes (latter for adding, deleting, viewing Qs)

    print("\nPlease type the letter corresponding to an option below, then press 'Return'.\n")
    print("(A) Get one question. (B) Get new questions continuously, you choose how often. (C) Add your own question. (D) View questions. (Q) Quit.")

    options = ("a", "b", "c", "d", "q")

    play_mode = input().lower()

    # in case user inputs invalid menu option
    while play_mode not in options:
        print("No such option. Please choose 'A', 'B', 'C', 'D', or 'Q'.")
        play_mode = input().lower()

    return play_mode


def pick_question(questions, not_used_qids, used_qids):
    """Chooses a random question for the team based on list of unused questions.
    Returns question text."""

    def are_unused(not_used_qids):
        """Checks whether list of unused Qs is empty"""

        return len(not_used_qids) > 0

    # while len of not_used_qids is 0 (meaning there are no unused Qs)
    if not are_unused(not_used_qids):
        # loop over keys in questions to add them all back to unused list
        for key in questions:
            not_used_qids.append(key)

    # pick a random ID from list of unused qs
    q_id = random.choice(not_used_qids)

    # find the question text using that ID
    ask_q = questions[q_id]

    # remove ID from set of unused qs. discard avoids error if element isn't in set
    not_used_qids.remove(q_id)

    # add used question to set of used Q IDs
    used_qids.add(q_id)

    # return question text
    return ask_q


def get_periodic_questions(questions, not_used_qids, used_qids):
    """Takes in user input on how often (in seconds) the user would like to get 
    a new question. Prints questions to console based on time (user input)."""

    # user prompt
    print("How often (in seconds, up to 1,800) would you like to see a new question?")
    interval = input()

    # validate that user entered an int
    while not interval.isdigit():
        print("Please enter a number.")
        interval = input()
    # change type to int after validating it's digits
    interval = int(interval)
    # sets a max on amount of time between questions of 30 min
    if interval > 1800: 
        interval = 1800
    
    # helper function for validating user input during continuous questions
    def is_input():
        """Checks whether there is user input"""

        # found on stackoverflow: https://stackoverflow.com/questions/2408560/non-blocking-console-input

        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    # loop for printing questions
    while True:
        # if there's user input, and it matches the stop command, break
        if is_input():
            if input().lower() == "x":
                break

        # call pick question to get a question        
        utils.print_color(pick_question(questions, not_used_qids, used_qids) + "\n")
        print("Press 'X' and then 'Return' any time to stop getting questions.\n")
        # wait however long user said
        time.sleep(interval)
    
    return


def view_questions(questions, not_used_qids, used_qids):
    """Lets user view all questions"""

    print("Which questions would you like to view?")
    view_mode = input("(A) All. (B) Questions seen this game. (C) Questions not seen this game.\n").lower()
    options = ("a", "b", "c")

    # validate input
    while view_mode not in options:
        print("No such option. Please choose 'A', 'B', or 'C'.")
        view_mode = input()

    if view_mode == "a":
        # loop over items in questions dict
        for key, value in questions.items():
            # print each question text along with its ID
            print(str(key) + ") " + value)
    elif view_mode == "b":
        for id in used_qids:
            print(str(id) + ") " + questions[id])
    elif view_mode == "c":
        for id in not_used_qids:
            print(str(id) + ") " + questions[id])

    return


def write_question_csv(user_q, new_id):
        """Allows user to save their input question to csv for future use"""
        
        # open csv. use with for cleanup and automatic closing. "a" option for 
        # adding to existing file
        with open("questions.csv", "a") as csvfile:
            # fields in order for writing
            fields = [new_id, user_q]
            writer = csv.writer(csvfile, delimiter="|")
            writer.writerow(fields)

        return 


def add_question(questions, not_used_qids):
    """Takes user input to add new question to game. Writes new question to csv
    on user request."""

    # get user question
    print("Please type your question, then press 'Return'.")
    user_q = input().capitalize()
    # find the end of the questions dict to get the id for new question
    # +1 because csv containing ids starts at 1, not 0
    new_id = len(questions) + 1
    
    # add to questions dict at new id 
    questions[new_id] = user_q
    # add new id to not_used_qids list for immediate use
    not_used_qids.append(new_id)
    
    # ask if user wants to save the question to game permanently
    print("Would you like to save your question for future use? (Y) / (N)")
    save_q = input().lower()
    options = ("y", "n")

    #check for valid input
    while save_q not in options:
        print("Invalid input. Would you like to save your question for future use? (Y) / (N)")
        save_q = input()

    # if yes, call on write function
    if save_q == "y":
        write_question_csv(user_q, new_id)
        print("Question saved!")
    # if no, pass
    elif save_q == "n":
        pass

    return


def play_game():
    """All together now. Core logic of gameplay loop using supporting functions"""

    # welcome message
    print("\nWelcome to Magic Hat, the icebreaker question game. Gather your team and get ready to play!")

    # set up dict of Qs and list of unused Qs
    questions, not_used_qids, used_qids = populate_questions()

    # get user input on what they'd like to do
    play_mode = get_play_mode()

    # while game is running
    while True:
        # single question mode
        if play_mode == "a":
            # print questions in yellow
            utils.print_color(pick_question(questions, not_used_qids, used_qids))
        # periodic question mode
        elif play_mode == "b":
            get_periodic_questions(questions, not_used_qids, used_qids)
        # add new question
        elif play_mode == "c":
            add_question(questions, not_used_qids)
        elif play_mode == "d":
            view_questions(questions, not_used_qids, used_qids)
        # quit the game
        elif play_mode == "q":
            print("Thanks for playing. Goodbye!")
            quit()
        play_mode = get_play_mode()

    return

####### RUN IT ##########

game = play_game()
