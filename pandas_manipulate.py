import pandas as pd
import seaborn as sns
import sqlite3 as sql
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

df = pd.read_csv('results.csv', parse_dates=True)

# totalHG = df['FTHG'].value_counts()
# totalAG = df['FTAG'].value_counts()

# print(totalHG, totalAG)

# sns.lineplot(data=totalAG)
# sns.lineplot(data=totalHG)

# plt.xlabel('Number of goals in a game')
# plt.ylabel('Total Goals')
# plt.title('Home vs Away Goals')
# plt.legend(title='Team', loc='upper right', labels=['Home Goal', 'Away Goal'])
# plt.show()

# tot_HomeTeam = df['HomeTeam'].value_counts()
# tot_AwayTeam = df['AwayTeam'].value_counts()
# print(tot_HomeTeam, tot_AwayTeam)

# total_Season = df['Season'].value_counts()
# print(total_Season)

total_Season = df.groupby(['Season'])
#print(total_Season)

list_Season = df['Season'].tolist()
list_Season = list(set(list_Season))
list_Season.sort()
#print(list_Season)

# ZeroS = total_Season.get_group('2001-11')
# HG = ZeroS['FTHG'].sum()
# AG = ZeroS['FTAG'].sum()
# print(HG + AG)
season_list = {}
for season in list_Season:
    ZeroS = total_Season.get_group(season)
    HG = ZeroS['FTHG'].sum()
    AG = ZeroS['FTAG'].sum()
    season_list[season] = HG + AG
    #print(season, HG + AG)

print(season_list)