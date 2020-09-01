# Foundations for efficiencies
# Writing Efficient Python Code
# Skill track : Python Programming
# DataCamp
# Karen Jimenez


###############################
## A taste of things to come ##
###############################

# Print the list created using the Non-Pythonic approach
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)

################################
## Built-in practice: range() ##
################################

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(type(nums_list2))
print(nums_list2)

"""You can convert the range object into a list by using the list() function or by unpacking it into a list using the star character (*)."""

####################################
## Built-in practice: enumerate() ##
####################################

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

##############################
## Built-in practice: map() ##
##############################

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [* names_map]

# Print the list created above
print(names_uppercase)

##################################
## Practice with NumPy arrays() ##
##################################

import numpy as np

nums = np.array([[ 1,  2,  3,  4,  5], [ 6,  7,  8,  9, 10]])

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:, 2] = nums[:, 2] + 1
print(nums)

"""Using numpy arrays allows you to take advantage of an array's memory efficient nature and easily perform mathematical operations on your data."""


##############################
## Bringing it all together ##
##############################

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3


# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i, time in enumerate(new_times)]

def welcome_guest(self):
    welcome = str(f"Welcome to Festivus {self[0]}... You're {self[1]} min late.")
    return welcome

#Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')