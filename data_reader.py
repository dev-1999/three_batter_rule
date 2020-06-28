"""
This script iterates over the .csv data that the script uses to calculate the expeected runs and wins gained from
the decisions made. pitcher_splits.csv is a generalized range of outcomes created from taking the splits from the
most used LHP vs LHB and RHP vs RHB situational relievers over the 2017-2019 seasons. re_matrix.csv is the run
expectancy matrix from 2019, courtesy of Baseball Prospectus: (https://legacy.baseballprospectus.com/sortable/index.php?cid=975409).
sequences.csv is every permutation of pitcher and three batters' handedness. we_matrix.csv is the win expectancy matrix,
for innings 7-9, with the game within 1 run (from Tom Tango: http://www.tangotiger.net/welist.html).

This is all distilled into the master dataframe 'master', which takes all relevant scenarios - pitching team leading/tied,
8+ inning, with each base/out and pitcher/hitter sequence.
"""
import pandas as pd
from pandasql import sqldf
dfRE24 = pd.read_csv('re_matrix.csv')
pitcherSplits = pd.read_csv('pitcher_splits.csv')
sequences = pd.read_csv('sequences.csv')
dfWE = pd.read_csv('we_matrix.csv')

#Creating lists to build the master dataframe
inn = []
t_b = []
_1b = []
_2b = []
_3b = []
sco = []
out = []
pit = []
b1 = []
b2 = []
b3 = []
we0 = []

#Populating the lists row by row
for j in range(len(sequences)):
    for k in range(len(dfWE)):
        inn.append(dfWE.loc[k,'Inning'])
        t_b.append(dfWE.loc[k,'TopBottom'])
        _1b.append(dfWE.loc[k,'1B'])
        _2b.append(dfWE.loc[k,'2B'])
        _3b.append(dfWE.loc[k,'3B'])
        sco.append(dfWE.loc[k,'Score'])
        pit.append(sequences.loc[j,'p'])
        b1.append(sequences.loc[j,'b1'])
        b2.append(sequences.loc[j,'b2'])
        b3.append(sequences.loc[j,'b3'])
        we0.append(dfWE.loc[k,'WE'])
        out.append(dfWE.loc[k,'Outs'])

#Zipping into the dataframe
master = pd.DataFrame({'Inning':inn,'TopBottom':t_b,'1B':_1b,'2B':_2b,'3B':_3b,'Score':sco,'Outs':out,'P':pit,'b1':b1,'b2':b2,'b3':b3,'WE_0':we0})

#Selecting a smaller subset of data as outlined above
#Uses SQL syntax to easily be pared down to only more relevant data for faster runtime
master = sqldf("SELECT * FROM master WHERE TopBottom = 'Top' AND Score >= 0")

#Dropping any duplicates
master.drop_duplicates(inplace=True)