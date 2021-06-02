import time
import sys
import select

def is_data(): 
    # says if there's input on stdin, return true
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

while True:
    # not optimal because it won't stop for good until the sleep finishes. 
    # if the user only wants questions every 2 minutes, that could mean
    # waiting up to 1:59 for the program to finish this phase
    print("Running")
    time.sleep(5)

    if is_data():
        key_pressed = input()
        break