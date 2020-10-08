#Basic Pandas Optimizations
#Writing Efficient Python Code
#Skill track : Python Programming
#DataCamp
#Karen Jimenez


import numpy as np
import pandas as pd

filename = "baseball_stats.csv"
baseball_stats = pd.read_csv(filename)

#copy rows from PIT
is_pit = baseball_stats.loc[:, 'Team'] == 'PIT'
pit_df = baseball_stats.loc[is_pit].copy()

baseball_stats.head(3)

################################
## Iterating with .iterrows() ##
################################

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)

# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)

"""
Since .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs, you can either split 
this tuple and use the index and row-values separately (as you did with for i,row in pit_df.iterrows()), or you 
can keep the result of .iterrows() in the tuple form (as you did with for row_tuple in pit_df.iterrows()).
If using i,row, you can access things from the row using square brackets (i.e., row['Team']). If using row_tuple,
you would have to specify which element of the tuple you'd like to access before grabbing the team name 
(i.e., row_tuple[1]['Team']).
With either approach, using .iterrows() will still be substantially faster than using .iloc"""

######################################
##Run differentials with .iterrows()##
######################################

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff


#copy rows from SFG
is_giants = baseball_stats.loc[:, 'Team'] == 'SFG'
giants_df = baseball_stats.loc[is_giants].copy()

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs

print(giants_df)

##################################
## Iterating with .itertuples() ##
##################################

#copy rows from TEX
is_rangers = baseball_stats.loc[:, 'Team'] == 'TEX'
rangers_df = baseball_stats.loc[is_rangers].copy()

# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)

for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W
    print(i, year, wins, sep=' / ')
        
    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.Playoffs == 1:
        print(f'Playoffs: {i} / {year} / {wins}')

##########################################
## Run differentials with .itertuples() ##
##########################################

#copy rows from NYY
is_yankees = baseball_stats.loc[:, 'Team'] == 'NYY'
yankees_df = baseball_stats.loc[is_yankees].copy()

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df.head())

############################################
## Analyzing baseball stats with .apply() ##
############################################

#copy rows from Tampa Bay Rays
is_rays = baseball_stats.loc[:, 'Team'] == 'TBR'
rays_d = baseball_stats.loc[is_rays].copy()
rays_df = rays_d.set_index('Year')
rays_df

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

############################################
## Analyzing baseball stats with .apply() ##
############################################

#copy rows from ARI
is_dbacks = baseball_stats.loc[:, 'Team'] == 'ARI'
dbacks_df = baseball_stats.loc[is_dbacks].copy()

#Let's use the below function and the .apply() method to see which manager is correct.
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])


######################################################
## Bringing it all together: Predict win percentage ##
######################################################

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head(10))

