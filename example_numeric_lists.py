"""

Examples of numeric lists

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.


Uses only Python Standard Library module

"""

import statistics
import math

# define a variable with some univariant data
# (one varabile, many readings)
score_list = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]
print(score_list)

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xtimes_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues_list = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

# Descriptive: Averages and measures of central tendency
# Use statisttics module to get mean, median, mode
# for a values list

mean = statistics.mean(score_list)
median = statistics.median(score_list)
mode = statistics.mode(score_list)
print(mean, median, mode)
# Descriptive: Measures of spread
# Get standard deviation and variance for a values list

stdev = statistics.stdev(score_list)
variance = statistics.variance(score_list)
print(stdev, variance)
# Descriptive: Measures of correlation
# Use two numerical lists of the same size
# Use statisttics module to get correlation between list1 and list2

correlationxy = statistics.correlation(xtimes_list, yvalues_list)
print(correlationxy)

# Predictive: Machine Learning - Linear Regression
# If the corrlation is close to 1.0, then the data is linearly related
# If so, use statistics module to get linear regression for list1 and list2
# This is a form of supervised machine learning - it uses all known data
# Use the slope and intercept and an unknown (future) x to predict a y value
# Python functions can return multiple values

slope, intercept = statistics.linear_regression(xtimes_list, yvalues_list)
print(slope, intercept)
# Once we have learned the slope and intercept
# of the best-fit straight line through the data,
# we can use it to make predictions

# Predict the y value for a given x value outside the range of the data

x_max = max(xtimes_list)
newx = x_max * 1.5  # predict for a future x value
print(x_max)
print(newx)
# Use the slope and intercept to predict a y value for the future x value
# y = mx + b

newy = slope * newx + intercept
print(newy)

# BUILT-IN FUNCTIONS ......................................
# Many built-in functions work on lists
# try min(), max(), len(), sum(), sorted(), reversed()

# Using the score list provided above, do the following:
# Calcuate the max and min scores
max = max(score_list)
min = min(score_list)
print(max, min)
# Calculate the length of the list
len = len(score_list)
print(len)
# Calculate the sum of the list
sum = sum(score_list)
print(sum)
# Calculate the average of the list
avg = sum / len
print(avg)
# Return a new list soreted in ascending order
asc_scores = sorted(score_list)
print(asc_scores)
# Return a new list soreted in descending order
desc_scores = sorted(score_list, reverse=True)
print(desc_scores)

"""

LIST METHODS ............................................... 

Here are some common methods that operate on an instance of a list.

append(x): Add an item to the end of the list.
extend(iterable): Add all the items from an iterable (such as another list)
     to the end of the list.
insert(i, x): Insert an item at a given position.
remove(x): Remove the first occurrence of an item.
pop([i]): Remove the item at the given position in the list, 
    and return it. If no index is specified, 
    removes and returns the last item in the list.
clear(): Remove all items from the list.
index(x[, start[, end]]): Return the index of the first occurrence of
     an item.
count(x): Return the number of occurrences of an item.
sort(key=None, reverse=False): Sort the items in the list 
     in ascending order.
reverse(): Reverse the order of the items in the list.
copy(): Return a shallow copy of the list.

"""

# append an item to the end of the list
lst = [1, 2, 3]
lst.append(4)
print(lst)
# extend the list with another list
lst.extend([4, 5, 6])
print(lst)
# insert an item at a given position (0 = first item)
i = 0
newvalue = 42
lst.insert(i, newvalue)
print(lst)
# remove an item
item_to_remove = 42
lst.remove(item_to_remove)
print(item_to_remove)
print(lst)
print("!!!!!!!!!!!!!!!!!!!!")
# Count how many times 111 appears in the list
ct_of_111 = score_list.count(111)
print(ct_of_111)
# Sort the list in ascending order using the sort() method
asc_scores2 = score_list.sort()
print(asc_scores)
# Sort the list in descending order using the sort() method
desc_scores2 = score_list.sort(reverse=True)
print(desc_scores2)
# Copy the list to a new list
new_scores = score_list.copy()
print(new_scores)
# Remove the first item from the new list
# The first item in a list is at index 0
# Think of it as an offset from the beginning of the list
first = new_scores.pop(0)
print(first)
# Remove the last item from the new list
# The last item in a list is at index -1
last = new_scores.pop(-1)
print(last)
# Remove the item at index 3 from the new list
fourth = new_scores.pop(3)
print(new_scores)
print(fourth)
print(new_scores)


# TRANFORMATIONS ............................

# FILTER and MAP are critical in big data applications

# Use the built-in function filter() anywhere you need to filter a list
# Filter the new list to only include scores greater than 100
# You could pass in a named function, but honestly this is easier
# Say "keep x such that x > 100 is True" given new_scores
# Cast the result using square brackets to get a list
scores_over_100 = [filter(lambda x: x > 100, new_scores)]
print(scores_over_100)
# Use the built-in function map() anywhere you need to transfrom

# Map each element to its square
# Say "map x to x squared" given new_scores
# Cast the result using square brackets to get a list
doubled_scores = [map(lambda x: x * 2, new_scores)]
print(doubled_scores)
# Map each element to its square root
# Say "map x to the square root of x" and cast to a list
sqrt_scores = map(lambda x: math.sqrt(x), new_scores)
print(sqrt_scores)
# Map each element (radius) to its area
radius_list = [1, 2, 3, 4, 5]
# Say "map r to pi r squared" and cast to a list
area_list = [map(lambda r: math.pi * r * r, radius_list)]
print(radius_list)
print(area_list)
# TRANFORMATIONS - Using List Comprehensions
# List comprehensions are a concise way to create lists
# They work like map and filter, but are more concise
# They are the preferred "pythonic" way to do transformations

# With comprehensions, we start with what we WANT
# Filter the new list to only include scores greater than 100
# Say "keep x (for each x in new_scores) IF  x > 100"
scores_over_100 = [x for x in new_scores if x > 100]
print(scores_over_100)
# Try again "keep x (for each x in new_scores) IF  x < 42"
scores_under_42 = [x for x in new_scores if x < 42]
print(scores_under_42)
# Map each element to its square
# Say "give me x squared (for each x in new_scores)"
doubled_scores = [x * 2 for x in new_scores]
print(doubled_scores)
# Map each element to its square root
# Say "give me the square root of x (for each x in new_scores)"
# and cast it to a list using square brackets
sqrt_scores = [math.sqrt(x) for x in new_scores]
print(sqrt_scores)
# Map each element (radius) to its area
# Say "give me pi r squared (for each r in radius_list)"
# and cast it to a list using square brackets
area_list = [math.pi * r * r for r in radius_list]
print(area_list)
# Map each element (radius) to its circumference
# Say "give me 2 pi r (for each r in radius_list)"
# and cast it to a list using square brackets
circumference_list = [2 * math.pi * r for r in radius_list]
print(circumference_list)
# Mastering comprehesions is a key skill for data scientists
numbers = [1, 2, 3, 4]
squares = [x ** 2 for x in numbers]
print(numbers)
print(squares)
print()
print("Add print statements to the code to see what happens.")
print("Explore enough to understand.")
print("Then apply what you know to your own domain.")
print()
