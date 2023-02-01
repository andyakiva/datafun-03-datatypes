"""
Andy Asher 
01/30/2023
PRoject 3
Examples of using string lists
"""

import random

# Define a string list
list_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]

# Define a list of outcomes
list_outcomes = ["win", "lose", "draw"]

# Define a list of calls
list_calls = ["heads", "tails"]

# Define a list for rock, paper, scissors
list_rps = ["rock", "paper", "scissors"]

# Define a list of colors
list_colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# Define a list of nouns
list_nouns = ["dog", "cat", "mouse", "bird", "fish", "snake"]

# Define a list of verbs
list_verbs = ["runs", "jumps", "swims", "flies", "crawls", "studies"]

# Define a list of adjectives
list_adjectives = ["happy", "sad", "angry", "scared", "confused", "bored"]

# Define a list of adverbs
list_adverbs = ["quickly", "slowly", "happily", "sadly", "angrily", "scaredly"]


# read in woodchuck to get a list of words
with open("text_woodchuck.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()  # split on whitespace
    unique_words = set(list_words)  # remove duplicates

# Print the count and list of words
word_ct = len(list_words)

# Print the count and list of unique words
unique_word_ct = len(unique_words)


# Create a random sentence
# e.g. "The angry dog runs quickly."

def sentence_get():
    sentence = (
    f"The {random.choice(list_adjectives)} {random.choice(list_nouns)} "
    f"{random.choice(list_verbs)} {random.choice(list_adverbs)}.")

    return sentence
    
playerchoice = input("Do you want to see a sentence? y|n ")
while playerchoice == "y":
    print(sentence_get())
    playerchoice = input("Do you want to see a sentence? y|n ")

if playerchoice == "n":
    print("Okay. Bye!")



# Game bot for rock, paper, scissors ................

# Define a function to get the winner message
# Use keyword arguments to be clear about the order of the arguments
def get_winner_message(userguess, botguess):
    if userguess == botguess:
        return "We tied!"
    elif userguess == "rock":
        if botguess == "paper":
            return "I win!"
        else:
            return "You win!"
    elif userguess == "paper":
        if botguess == "rock":
            return "I win!"
        else:
            return "You win!"
    elif userguess == "scissors":
        if botguess == "paper":
            return "I win!"
        else:
            return "You win!"


ready_for_continous_game = True  # change this when ready

while True:
    if not ready_for_continous_game:
        quit()  # don't get stuck in an infinite loop until ready

    print()
    user_choice = input("Say rock, paper, or scissors or q to quit:")
    if user_choice == "q":
        break  # break out of the loop
    # if still here, the bot makes a choice
    # don't indent unnecessarily
    bot_choice = random.choice(list_rps)
    print(f"You said {user_choice}.")
    print(f"I said {bot_choice}.")
    # When calling a function, the order of arguments matters!
    # We don't want to accidentally provide the guesses in the wrong order
    # So we'll use keyword arguments so the order doesn't matter
    msg1 = get_winner_message(userguess=user_choice, botguess=bot_choice)
    msg2 = get_winner_message(botguess=bot_choice, userguess=user_choice)
    if msg1 == msg2:
        print(msg1)
    print()
    print("This program will run forever unless you type q to quit.")
    print("or use Ctrl-C to stop the program.")
    print()

