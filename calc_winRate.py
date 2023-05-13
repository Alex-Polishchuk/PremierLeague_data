#to calculate the win rate of teams (overall, per season, against certain teams)
import pandas as pd

df = pd.read_csv('results.csv', parse_dates=True)

home_value = df.value_counts('HomeTeam')
away_value = df.value_counts('AwayTeam')

#convertings values to a dataframe
home_df = pd.DataFrame(home_value)
away_df = pd.DataFrame(away_value)

#renaming columns for clarity
home_df = home_df.rename(columns={0:'Games Played Home'})
away_df = away_df.rename(columns={0:'Games Played Away'})

#resetting index
home_df.reset_index(inplace=True)
away_df.reset_index(inplace=True)

#renaming columns
home_df = home_df.rename(columns={'HomeTeam':'Team'})
away_df = away_df.rename(columns={'AwayTeam':'Team'})

#merging two dataframes together
total_df = pd.merge(home_df, away_df, on='Team')
print(home_df.shape, total_df.shape, away_df.shape)

total_df['Total Played'] = ''
#total_df.set_index('Team' , inplace=True)

for index, team in total_df.iterrows():

    #call the index of the home and away game values for a certain team
    home_played = total_df.loc[index, 'Games Played Home']
    away_played = total_df.loc[index, 'Games Played Away']

    #changed it to integers
    away_played = int(away_played)
    home_played = int(home_played)

    #sum home and away games
    total_played = home_played + away_played

    #changes the value of the team to the correct value
    total_df.loc[index, 'Total Played'] = total_played
    #print(type(total_played))

total_df['Home Wins'] = ''
total_df['Away Wins'] = ''
total_df['Total Wins'] = ''

total_df['Home Draw Percentage'] = ''
total_df['Away Draw Percentage'] = ''
total_df['Total Draw Percentage'] = ''

total_df['Home Loss Percentage'] = ''
total_df['Away Loss Percentage'] = ''
total_df['Total Loss Percentage'] = ''


total_df['Home Win Percentage'] = ''
total_df['Away Win Percentage'] = ''
total_df['Total Win Percentage'] = ''


for index, team in total_df.iterrows():
    total_played = total_df.loc[index, 'Total Played']
    home_wins = df[(df['HomeTeam'] == team) & (df['Result'] == 'HomeTeam')].shape[0]
    away_wins = df[(df['AwayTeam'] == team) & (df['Result'] == 'AwayTeam')].shape[0]
    total_wins = home_wins + away_wins
    win_rate = total_wins / total_played
    total_df.loc[index, 'Win Rate'] = win_rate