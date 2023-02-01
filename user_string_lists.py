"""
Andy Asher
01/30/2023
Project 3
Domain: Social Inequality

"""
print(f"""


!!!!!!!!!!!!!!!!!
Here for part 1
!!!!!!!!!!!!!!!!!!!!!


""")

#def lists
race = ["black", "white", "asian", "native", "other", "refuse"]
ethnicity = ["hispanic", "non-hispanic", "other", "refuse"]
religion = ["jewish", "christian", "muslim", "hindu", "pagan", "atheist", "other", "refuse"]
gender = ["man", "woman", "nonbinary", "other", "refuse"]
orientation = ["hetersexual", "homosexual", "bisexual", "asexual", "queer", "other", "refuse"]

print(f"""
Race: {race}
Ethnicity: {ethnicity}
Religion: {religion}
Gender: {gender}
Orientation: {orientation}
""")

print("How many race options are there?")
print(f"This program recognizes {len(race)} races for demographic statistics.")
print("What all options for identity does this program recognize?")
identities = race + ethnicity + religion + gender + orientation
uniqueid = set(identities)
print(uniqueid)
print()
print(f"This program offers {len(uniqueid)} identity options. You select 5.")
print("You can select other and refuse multiple times")
print()
print("Race and ethnicity data for three people could look like this:")
participantrace = ["black", "black", "white"]
participanteth = ["hispanic", "refuse", "refuse"]
print(f"""
Races: {participantrace}
Ethnicities: {participanteth}

We can combine these into matched data as a tuple.
{tuple(zip(participantrace, participanteth))}
""")

print(f"""


!!!!!!!!!!!!!!!!!
Here for part 2
!!!!!!!!!!!!!!!!!!!!!


""")

#  imports first
import random

# reusable functions next
def sentence_get():
    senrace = random.choice(race)
    seneth = random.choice(ethnicity)
    senrel = random.choice(religion)
    sengen = random.choice(gender)
    senori = random.choice(orientation)

    #ensure not assaigned "other" or "refuse"
    while senrace == "other" or senrace == "refuse":
        senrace = random.choice(race)

    while seneth == "other" or seneth == "refuse":
        seneth = random.choice(ethnicity)

    while senrel == "other" or senrel == "refuse":
        senrel = random.choice(religion)
    
    while sengen == "other" or sengen == "refuse":
        sengen = random.choice(gender)
    
    while senori == "other" or senori == "refuse":
        senori = random.choice(orientation)
    
    #use those variables
    sentence = str(f"""Congratulations! \n\nYou are now a {senrace} {senori} {seneth} {senrel} {sengen}!""")
    return sentence

# call functions and execute code
# use if __name__ == "__main__":
if __name__ == "__main__":
    print(f"""Let's learn about demographic data.

    This program is going to assaign you random demographics.
    These graphics are not in any way tied to your real life.
    They are nothing more than coincidence if they overlap.

    Enjoy your new identity!
    
    """)

    print(sentence_get())




print(f"""


!!!!!!!!!!!!!!!!!
Here for part 3
!!!!!!!!!!!!!!!!!!!!!


""")

with open("gendersa.txt", "r") as genders:
    text = genders.read()
    list_words = text.split()  
    unique_words = set(list_words)  

print(f"""With new and ever expanding understandings of gender, it ist important
to not let demographic data sets miss people. This is why it's a good idea
to always include an option for other.

As an example, let's see how many genders starting with the letter A we can find.

{list_words}


That's a lot of genders! {len(unique_words)} in fact!

""")


    

