"""
Andy Asher
01/31/2023
Project 3


"""

print("Tuples and More")
print("create tuples")

participant1 = ("black", "hispanic", "jewish", "heterosexual", "other")
participant2 = ("refuse", "refuse", "jewish", "bisexual", "woman")

#play with tuples
print(f"{participant1 = }")
print(f"{participant2 = }")

print(f"""
#create sets""")
set1 = set(participant1)
set2 = set(participant2)
print(f"""
{set1}
{set2}

Find set union and intersection
""")
setunion = set1 & set2
print(setunion)

setintersection = set1 | set2
print(setintersection)

#Use a dictionary to create key-value pairs of each word 
# and its count from a file. 
#I removed the punctuation for simplicity

print("""
Use python to count words in txt file

""")

with open("text_woodchuck.txt", "r") as wood:
    text = wood.read()
    list_words = text.split()  

countdict = {i:list_words.count(i) for i in list_words }
print(countdict)