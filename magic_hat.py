# define dict of question IDs, question text, and bool for used Qs
# read in as CSV?
import csv 

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



####### RUN IT ##########

questions, unused_qids = populate_questions()
print(unused_qids)