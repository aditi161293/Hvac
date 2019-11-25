import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


episodes = []
actions=[]
rewards=[]
with open('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/results2.csv') as f:
   reader = csv.DictReader(f)  # read rows into a dictionary format
   for row in reader:  # read a row as {column1: value1, column2: value2,...}
      for (k, v) in row.items():  # go over each column name and value
         if(k=='episode'):
            episodes.append(v)  # append the value into the appropriate list
         if (k == 'action'):
            actions.append(v)
         if (k == 'reward'):
            rewards.append(v)

print(episodes)
print(actions)
print(rewards)

newEp=[]
newRe=[]
newAc=[]

for v in range(len(episodes)):
   if (v + 1) % 100 == 0 and v!=0:
      fig, ax = plt.subplots()
      ax.plot(newEp, newAc)
      ax.plot(newEp, newRe)
      plt.autoscale()
      plt.ylabel('value')
      plt.xlabel('episodes')
      plt.show()
      newAc = []
      newEp = []
      newRe = []
   newRe.append(rewards[v])
   newEp.append(episodes[v])
   newAc.append(actions[v])
















         # with open('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/results1.csv', 'a',
#                   newline='') as f:
#    csv_writer = csv.writer(f)
#    for i in  range(len(columns)):
#       csv_writer.writerow([columns[i][0],columns[i][1],columns[i][2],columns[i][3],columns[i][4],columns[i][5]])



