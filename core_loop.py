"""
This core loop simulates the outcomes imported in from the master spreadsheet 'n' number of times.
Each row will then have the average runs allowed and win expectancy added, and the difference vs expected can be calculated.
"""
from data_reader import master, pitcherSplits, dfRE24, dfWE as df
from pa_outcomes import Walk, Strikeout, TwoBaseSingle, OneBaseSingle, Double, GIDP, Groundout, Flyout, Triple, Lineout, HomeRun
import numpy as np
import pandas as pd

#Number of simulations per row to run
n = 2000
#List to be populated by the average outcomes for each row
avgRuns = []
avgWins = []

for i in range(len(master)):
    #A simle progress percent tracker, this can take a long time.
    if i % 20 == 0:
        print(str(round(i/len(master)*100),3) + "%")
    #The running total of wins/runs, to be divided by n later.
    totalRuns = 0
    totalWins = 0
    #Populating the sequence
    sequence = []
    pitcher = master.loc[i, 'P']
    sequence.append(master.loc[i, 'b1'])
    sequence.append(master.loc[i, 'b2'])
    sequence.append(master.loc[i, 'b3'])
    #Creating the initial base/out state
    basestate = []
    basestate.append(master.loc[i, '1B'])
    basestate.append(master.loc[i, '2B'])
    basestate.append(master.loc[i, '3B'])
    o = master.loc[i, 'Outs']
    #Simulating until three outs or three batters reached
    for j in range(n):
        netRuns = 0
        netWins = 0
        Hitter = 0
        Runs = 0
        Outs = o
        Bases = basestate
        while Hitter < 3 and Outs < 3:
            if pitcher == "R":
                if sequence[Hitter] == "L":
                    row = 0
                if sequence[Hitter] == "R":
                    row = 1
            if pitcher == "L":
                if sequence[Hitter] == "L":
                    row = 2
                if sequence[Hitter] == "R":
                    row = 3
            Action = np.random.random()
            if Action < pitcherSplits.loc[row, "BB%"]:
                Dummy = Walk(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action < pitcherSplits.loc[row, "BB%"] + pitcherSplits.loc[row, "K%"]:
                Dummy = Strikeout(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action < pitcherSplits.loc[row, "BB%"] + pitcherSplits.loc[row, "K%"] + pitcherSplits.loc[
                row, "1B%"] / 2:
                Dummy = TwoBaseSingle(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action < pitcherSplits.loc[row, "BB%"] + pitcherSplits.loc[row, "K%"] + pitcherSplits.loc[row, "1B%"]:
                if Outs == 2:
                    Dummy = TwoBaseSingle(Bases, Runs, Outs)
                    Bases = Dummy[0]
                    Runs = Dummy[1]
                    Outs = Dummy[2]
                else:
                    Dummy = OneBaseSingle(Bases, Runs, Outs)
                    Bases = Dummy[0]
                    Runs = Dummy[1]
                    Outs = Dummy[2]
            elif Action < pitcherSplits.loc[row, "BB%"] + pitcherSplits.loc[row, "K%"] + pitcherSplits.loc[row, "1B%"] + \
                    pitcherSplits.loc[row, "2B%"]:
                Dummy = Double(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action < pitcherSplits.loc[row, "BB%"] + pitcherSplits.loc[row, "K%"] + pitcherSplits.loc[row, "1B%"] + \
                    pitcherSplits.loc[row, "2B%"] + pitcherSplits.loc[row, "3B%"]:
                Dummy = Triple(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action < pitcherSplits.loc[row, "BB%"] + pitcherSplits.loc[row, "K%"] + pitcherSplits.loc[row, "1B%"] + \
                    pitcherSplits.loc[row, "2B%"] + pitcherSplits.loc[row, "3B%"] + pitcherSplits.loc[row, "HR%"]:
                Dummy = HomeRun(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action < pitcherSplits.loc[row, "GBO%"] / 2 + pitcherSplits.loc[row, "BB%"] + pitcherSplits.loc[
                row, "K%"] + pitcherSplits.loc[row, "1B%"] + pitcherSplits.loc[row, "2B%"] + pitcherSplits.loc[
                row, "3B%"] + pitcherSplits.loc[row, "HR%"]:
                Dummy = GIDP(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action < pitcherSplits.loc[row, "GBO%"] + pitcherSplits.loc[row, "BB%"] + pitcherSplits.loc[
                row, "K%"] + pitcherSplits.loc[row, "1B%"] + pitcherSplits.loc[row, "2B%"] + pitcherSplits.loc[
                row, "3B%"] + pitcherSplits.loc[row, "HR%"]:
                Dummy = Groundout(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            else:
                Dummy = Flyout(Bases, Runs, Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            Hitter += 1
        #Adding runs scored to runvalue for this simulated inning.
        netRuns += Dummy[1]
        #If the inning isn't over, this adds the remaining expected run value according to the base/out state.
        if Dummy[2] < 3:
            outState = (str(Dummy[2]) + "_out")
            baseState = Dummy[0]
            baseCol = 0
            for i in range(len(dfRE24)):
                if dfRE24.loc[i, "1B"] == baseState[0] and dfRE24.loc[i, "2B"] == baseState[1] and dfRE24.loc[
                    i, "3B"] == baseState[2]:
                    baseCol = i
            netRuns += dfRE24.loc[baseCol, outState]

        score_check = master.loc[i, 'Score'] - Dummy[1]
        #This block of identifies the relevant win expectancy at the end of the sequence.
        if Dummy[2] == 3:
            top_check = 'Top'
            inn_check = 0
            if master.loc[i, 'TopBottom'] == 'Top':
                top_check = 'Bottom'
                inn_check = master.loc[i, 'Inning']
            else:
                top_check = 'Top'
                inn_check = master.loc[i, 'Inning'] + 1
            row_crit = -1
            for r in range(len(df)):
                if df.loc[r, 'Inning'] == inn_check and df.loc[r, 'TopBottom'] == top_check and df.loc[
                    r, 'Score'] == score_check and df.loc[r, 'Outs'] == 0 and df.loc[r, '1B'] == 0 and df.loc[
                    r, '2B'] == 0 and df.loc[r, '3B'] == 0:
                    row_crit = r
            if row_crit >= 0:
                netWins += df.loc[row_crit, 'WE']
        else:
            row_crit = -1
            for r in range(len(df)):
                baseState = Dummy[0]
                if df.loc[r, 'Inning'] == master.loc[i, 'Inning'] and df.loc[r, 'TopBottom'] == master.loc[
                    i, 'TopBottom'] and df.loc[r, 'Score'] == score_check and df.loc[r, 'Outs'] == Dummy[2] and df.loc[
                    r, '1B'] == baseState[0] and df.loc[r, '2B'] == baseState[1] and df.loc[r, '3B'] == baseState[2]:
                    row_crit = r
            if row_crit >= 0:
                netWins += df.loc[row_crit, 'WE']
        #After simulating, this adds the runs allowed and wins earned to the running total.
        totalRuns += netRuns
        totalWins += netWins
    #After n simluations, this calculates the average runs allowed and wins gained.
    avgRuns.append(totalRuns / n)
    avgWins.append(totalWins / n)

#Creating a final dataframe with the run and win outcomes for each scenario incorporated.
output = master
output['avg_runs'] = avgRuns
output['avg_wins'] = avgWins
