# define dict of question IDs, question text, and bool for used Qs
# read in as CSV?
import csv 
import random
import select
import sys
import time
import utils

# initialize empty dict, to be populated by reading in CSV
def populate_questions():
    """Populates dictionary of questions, IDs, and used values (default to false) 
    using data from CSV file"""
    
    questions = {}
    unused_qids = []

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
            questions[int(q_id)] = {"question" : q_txt, "used" : False}
            # add ID of each question to unused qids list
            unused_qids.append(int(q_id))

    # returns both the dict and the list of used_qids for further use in game
    return questions, unused_qids


def get_play_mode():
    """Prints user options for playing the game. Takes user input and returns 
    game mode"""

    print("Please type the letter corresponding to the options below, then press 'Return'.\n")
    print("(A) Get one question. (B) Get a new questions continuously, you choose how often. (Q) Quit.")

    play_mode = input("").lower()

    return play_mode


def pick_question(questions, unused_qids):
    """Chooses a random question for the team based on list of unused questions.
    Returns question text."""

    def are_unused(unused_qids):
        """Checks whether list of unused Qs is empty"""

        return len(unused_qids)

    # while len of unused_qids is 0 (meaning there are no unused Qs)
    while not are_unused(unused_qids):
        # loop over keys in questions to add them all back to unused list
        for key in questions:
            unused_qids.append(key)
            # update used status to False
            questions[key]["used"] = False

    # pick a random ID from list of unused qs
    q_id = random.choice(unused_qids)

    # find the question text using that ID
    ask_q = questions[q_id]["question"]

    # remove ID from list of unused qs
    unused_qids.remove(q_id)

    # change used state to True
    questions[q_id]["used"] = True

    # return question text
    return ask_q
    #DONE: handle what happens when unused_qids is empty


def get_periodic_questions(questions, unused_qids):
    """Takes in user input on how often (in minutes) the user would like to get 
    a new question. Prints questions to console based on time (user input)."""

    # user prompt
    interval = int(input("How often (in minutes) would you like to see a new question?\n"))

    # validate that user entered an int
    while type(interval) is not int:
        print("Please enter a number.")
        interval = input("")
    
    # convert time to seconds for use with sleep()
    # TODO: uncomment line 97
    # interval = interval * 60

    # helper function for validating user input during continuous questions
    def is_input():
        """Checks whether there is user input"""

        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    # loop for printing questions
    while True:
        utils.print_color(pick_question(questions, unused_qids) + "\n")
        print("Press 'X' and then 'Return' any time to stop getting questions.\n")
        # wait however long user said
        time.sleep(interval)

        # if there's user input, and it matches the stop command, break
        if is_input():
            if input("").lower() == "x":
                break
    
    # show_menu()


def play_game():
    """All together now. Core logic of gameplay loop using supporting functions"""

    # welcome message
    print("Welcome to Magic Hat, the icebreaker question game. Gather your team and get ready to play!\n")

    # set up dict of Qs and list of unused Qs
    questions, unused_qids = populate_questions()

    # get user input on what they'd like to do
    play_mode = get_play_mode()

    # while there is user input on play mode
    while play_mode:
        # single question mode
        if play_mode == "a":
            # print questions in yellow
            utils.print_color(pick_question(questions, unused_qids) + "\n")
            # prompt user for input again and update play mode
            play_mode = get_play_mode()
        # periodic question mode
        elif play_mode == "b":
            get_periodic_questions(questions, unused_qids)
            play_mode = get_play_mode()
        # quit the game
        elif play_mode == "q":
            print("Thanks for playing. Goodbye!")
            quit()


####### RUN IT ##########

game = play_game()
