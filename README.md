# three_batter_rule
A Markov chain Monte Carlo simulation on the effects of MLB's three batter rule implemented for the 2020 season. Created by myself, Owen Ricketts, Adam Akbani, and Tory Farmer.

This repository was created to solve a problem posed to our group by the Cardinals' FO ahead of competing at the 2020 SABR Analytics Conference. THough we were ultimately unable to attend, you can find an expanded version of our methodology and results here. To further explain the files:

- __data_reader.py__ processes the .csv files used to create the scenarios that the simulation plays through including:
  - __pitcher_splits.csv__ has the average outcomes in 1B%, 2B%, 3B%, HR%, K%, etc. from taking the splits from the
most used LHP vs LHB and RHP vs RHB situational relievers over the 2017-2019 seasons.
  - __re_matrix.csv__ is the run expectancy matrix from 2019, courtesy of [Baseball Prospectus](https://legacy.baseballprospectus.com/sortable/index.php?cid=975409)
  - __sequences.csv__ contains every permutation of pitcher handendness and the handedness of the three batters due up
  - __we_matrix.csv__ is the win expectancy matrix, for innings 7-9, with the game within 1 run, from [Tom Tango](http://www.tangotiger.net/welist.html)
 
These are all processed into a single dataframe containing every relevant base/out/run/lineup scenario. These are where the pitching team is leading or tied, it's the 8th or 9th inning, and then accounting for each of these situations with each base/out and pitcher/hitter sequence. This dataframe is the basis of our simulation.

- __pa_outcomes.py__ contains the functions that drive the simulation, advancing to a different state based on the result of the prior plate appearance. These advance different variables like *VarState* (the runners on base), *RunState* (the number of runs conceded), and *OutState* (the number of outs), in line with the current state of these variables and the action (plate appearance result). This code is mostly from [Ben Clemens' article about Austin Hedges](https://blogs.fangraphs.com/some-fun-with-austin-hedges-a-baseball-extreme/), and tweaked slightly for our purposes here, and more in the core loop.

- __core_loop.py__ actually simulates the scenarios created by the data_reader.py script. Each scenario is represented by one row in the dataframe and is simulated 'n' number of times (default = 2000). If the inning ends, the number of runs allowed that inning is added to the running total of runs allowed. However, if the inning is still in progress, the matching scenario in the re_matrix dataframe is added to the running total (along with any runs that "crossed home"). The matching win expectancy for the end scenario is added to the running total of wins each simulation as well, and after completing *n* simulations, the average wins and runs allowed are calculated for each scenario and placed in the dataframe *output*.

- __results_to_csv.py__ processes this output dataframe and calculates the expected number of wins and runs gained by bringing in the pitcher of that specified handedness. This script then creates the file *we_results.csv* with this data.

Ultimately, the margins of runs gained are quite small, which is due in some part to our selection of relievers who lasted 3 seasons, but also due to the relatively small effects of these decisions in the long run. After our initial presentation, the feedback we received led to including the win expectancy in the revised version of this project. The boxplot below shows this effect and its few outliers in greater detail.


As per this simulation, the most extreme differences in wins are only in the range of approximately 0.05 WPA. One way this could understate the effects is if this difference is greater with two poorer relievers with more extreme splits, and looking at different statlines (instead of pitcher_splits.csv) is likely the next step of this project.

