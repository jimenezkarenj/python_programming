# Gaining efficiences
# Writing Efficient Python Code
# Skill track : Python Programming
# DataCamp
# Karen Jimenez

import numpy as np

#Read files
f_names = 'names.txt'
f_primary_types = 'primary_types.txt'
f_secondary_types = 'secondary_types.txt'

names = np.loadtxt(f_names, delimiter=',', dtype=str)
primary_types = np.loadtxt(f_primary_types, delimiter=',', dtype=str)
secondary_types = np.loadtxt(f_secondary_types, delimiter=',', dtype=str)


#######################################
## Combining Pokémon names and types ##
#######################################

# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')

####################################
## Counting Pokémon from a sample ##
####################################

#Import Counter from collections
from collections import Counter

#Read files
f_generations = 'generations.txt'
generations = np.loadtxt(f_generations, delimiter=',', dtype=str)

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [letter[0] for letter in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(letter[0] for letter in names)
print(starting_letters_count)

#############################
## Combinations of Pokémon ##
#############################


# Import combinations from itertools
from itertools import combinations
pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)

#List pokedex from pokémon trainers
ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle'] 
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']
brock_pokedex = ['Onix', 'Geodude', 'Zubat', 'Golem', 'Vulpix', 'Tauros', 'Kabutops', 'Omastar', 'Machop', 'Dugtrio']

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print("Pokémon in both pokedex:", '\n', both, '\n')

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print("Misty doesn't have those Pokémon:" '\n', ash_only, '\n')

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print("Pokémon that are in only one set (not both):" '\n', unique_to_set, '\n', )


###########################
## Searching for Pokémon ##
###########################

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex)


##############################
## Gathering unique Pokémon ##
##############################

#function was written to gather unique values from each list:
def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques

#Read files
f_sample_names = 'sample_names.txt'
sample_names = np.loadtxt(f_sample_names, delimiter=',', dtype=str)

# Use the provided function to collect unique Pokémon names
uniq_names_func = find_unique_items(sample_names)
print(len(uniq_names_func))

# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(sample_names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(sample_names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

#%timeit uniq_names_set = set(sample_names)
#%timeit uniq_names_func = find_unique_items(sample_names)

# Using a set to collect unique values is faster

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types) 
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n') 

######################################
## Gathering Pokémon without a loop ##
######################################

#Read files
f_poke_names = 'poke_names.txt'
poke_names = np.loadtxt(f_poke_names, delimiter=',', dtype=str)

f_poke_gens = 'poke_gens.txt'
poke_gens = np.loadtxt(f_poke_gens, delimiter=',', dtype=int)


gen1_gen2_name_lengths_loop = []

def loop(self):
    for name,gen in zip(poke_names, poke_gens):
        if gen < 3:
            name_length = len(name)
            poke_tuple = (name, name_length)
            gen1_gen2_name_lengths_loop.append(poke_tuple)

# %timeit loop('')

#Replace the entire for loop with one list comprehension        
[(name, len(name)) for name,gen in zip(poke_names, poke_gens) if gen < 3]
%timeit [(name, len(name)) for name,gen in zip(poke_names, poke_gens) if gen < 3]

# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]
%timeit gen1_gen2_pokemon

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)
%timeit name_lengths_map

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]
%timeit gen1_gen2_name_lengths

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

# Compared runtimes between the for loop and using list comprehension with a map() function, you'd see that the for loop took quite a bit longer.

###############################
## One-time calculation loop ##
###############################

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen,count in gen_counts.items():
    total_count = len(generations)
    gen_percent = round(count / total_count * 100, 2)
    print(
      'generation {}: count = {:3} percentage = {}'
      .format(gen, count, gen_percent)
    )

#Let's make this loop more efficient by moving a one-time calculation outside the loop.

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))

##############################
## Holistic conversion loop ##
##############################

pokemon_types = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting',
                 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice',
                 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']


# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerate_tuples = []

enumerated_pairs = []

for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_pair_list = list(enumerated_pair_tuple)
    enumerated_pairs.append(enumerated_pair_list)

#Let's make this loop more efficient using a holistic conversion.

# Add a line to append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerate_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerate_tuples)]
print(enumerated_pairs[:5])

#Used the map() function to convert tuples to lists all at once outside of a loop


################################################
## Bringing it all together: Pokémon z-scores ##
################################################

#Read files
f_hps = 'hps.txt'
hps = np.loadtxt(f_hps, delimiter=',', dtype=int)

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hp, zscore) for name,hp,zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')

#The total time for executing the updated solution using NumPy and list comprehension was faster.
