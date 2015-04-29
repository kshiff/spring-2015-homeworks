import numpy as np 
import csv
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

datadir = "./data/"

with open(datadir + 'tourney_detailed_results.csv', 'rb') as infile:
	stats = csv.reader(infile)
	for stat in stats:
		print stat

stat = 'wscore'
s = 'lscore'
data = pd.io.parsers.read_csv(datadir+'regular_season_detailed_results.csv')

stats = data.columns.values

# for stat in stats:
	# if stat == "wloc":
	# 	pass
	# else:
print stats
for stat in stats:
	if stat == "wloc":
		pass
	else:
		print stat, np.mean(data[stat])

print "------------------------"
for stat in stats:
	if stat == "wloc":
		pass
	else:
		print stat, np.std(data[stat])

# d = data[stat].value_counts()
# x = data[s].value_counts()
# plt.bar(d.index, d.values, align='edge')
# plt.bar(x.index, x.values, color='red', width=.5, align='center')
# plt.show()