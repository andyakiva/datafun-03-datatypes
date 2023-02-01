"""
Andy Asher
Project 3
01/29/23
Domain: Social Inequality

"""

# import some modules first - how many can you make use of?
import statistics as stats
# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = length * width # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.




#define values of 20 homes in thousands
homes1 =[
    84,
    65,
    86,
    92,
    400,
    865,
    321,
    142,
    96,
    75,
    100,
    90,
    94,
    95,
    81,
    125,
    364,
    294,
    114,
    108
]
print("A list of 20 home values in thousands:")
print(homes1)

#years of home ownership
listx = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#value of avg increase per year in thousands
listy = list([11, 13, 12, 15, 12, 15, 16, 18, 17, 20])

#home value stats
meanhomes = stats.mean(homes1)
medianhomes = stats.median(homes1)
modehomes = stats.mode(homes1)
stdvhomes = stats.stdev(homes1)
varhomes = stats.variance(homes1)
print(f"""Here are some stats about our home values.
Mean: {meanhomes}
Median: {medianhomes}
Mode: {modehomes}
Standard Deviation of Values: {round(stdvhomes, 2)}
Variance of Values: {round(varhomes, 2)}
""")

#predict gain in year 15
correlationxy = stats.correlation(listx, listy)
slope, intercept = stats.linear_regression(listx, listy)
year15 = slope * 15 + intercept
print(f"""Let's predict how much value a home would gain in the 15th year of ownership.
How much a home gains in the first 10 years, by year, in thousands:
{listy}

How much a home value is predicted to increase in year 15:
{year15}

That's a lot!
""")


#more stats
minhomes1 = min(homes1)
maxhomes1 = max(homes1)
length = len(homes1)
total = sum(homes1)
average =  total / length
uniquehomes1 = set(homes1)
aschomes1 = sorted(homes1)
print(f"""Let's learn some more facts about these home values.
Lowest: {minhomes1}
Highest: {maxhomes1}
Average: {average}
All unique values:
{uniquehomes1}
All values, ascending:
{aschomes1}""")
print("All values, descending:")
dschomes1 = sorted(homes1, reverse = True)
print(dschomes1)


#demonstrating list methods
print("Let's look at some new homes!")
lst = [10, 25, 100, 25, 35, 45]
print(f"""New home values:
{lst}""")
print("Let's add one value.")
lst.append(54)
print("Let's add some more values!")
lst.extend([32, 41, 30])
print("Oops! We missed one! Let's add it")
lst.insert(3, 53)
print(lst)
print("Looks like there is one on here that shouldn't be. Let's remove it.")
lst.remove(10)
lstnew = lst
print(lstnew)
print("Let's see how many houses have a value of 25k")
count25 = lstnew.count(25)
print(count25)
print("This list is messy. Let's sort it.")
lstnew.sort()
print(lstnew)
print("Now in reverse!")
lstnew.sort(reverse = True)
print(lstnew)


lstcopy = lst.copy()
print("Let's remove the first and last houses.")
print(lstcopy.pop(0))
print(lstcopy.pop(-1))

#List transformations
print("Let's look at homes under 100k from our original list.")
lowvalues = list(filter(lambda x: x < 100, homes1))
print(lowvalues)
print("What would the values look like if the homes were 3x as valuable?")
triples = list(map(lambda x: x * 3, homes1))
print(triples)
print("What would the cube of a home value look like?")
cubeval = list(map(lambda x: x ** 3, homes1))
print(cubeval)

#List comprehensions
print("Let's look at homes above 100k from our original list.")
lowvalues = [x for x in homes1 if x > 100]
print(lowvalues)
print("What would the values look like if the homes were 5x as valuable?")
triples = [x * 5 for x in homes1]
print(triples)
print("What would the cube root of a home value look like?")
cubeval = [x ** (1/3) for x in homes1]
print(cubeval)





