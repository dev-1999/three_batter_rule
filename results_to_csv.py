#Processes the results and exports them to 'we_results.csv'
import pandas as pd
from core_loop import output
output['WPA'] = output['avg_wins'] - output['WE_0']
output.sort_values(by='WPA',inplace=True)
output.to_csv('we_results.csv')