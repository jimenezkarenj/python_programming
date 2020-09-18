# Timing and profiling code
# Writing Efficient Python Code
# Skill track : Python Programming
# DataCamp
# Karen Jimenez

import time
import csv
import numpy as np

###################
## Using %timeit ##
###################

# Create a list of integers (0-50) using list comprehension


nums_list_comp = [num for num in range(51)]

print(nums_list_comp)

print(time.thread_time())


# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)
print(time.thread_time())


########################################################
## Using %timeit: specifying number of runs and loops ##
########################################################

#Read heroes file


with open("heroes.csv", "r") as csv_file:
    heroes_csv = csv.reader(csv_file, delimiter=',')
    for line in heroes_csv:
        heroes_list = line[0]

print(time.thread_time())


##################################################
## Using %timeit: formal name or literal syntax ##
##################################################

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Print out the type of formal_list
print(type(formal_list))

print(time.thread_time())


# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of literal_list
print(type(literal_list))

print(time.thread_time())