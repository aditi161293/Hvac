import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


episodes = []
attic=[]
main=[]
hvac=[]
basement=[]
with open('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/results2.csv') as f:
   reader = csv.DictReader(f)  # read rows into a dictionary format
   for row in reader:  # read a row as {column1: value1, column2: value2,...}
      for (k, v) in row.items():  # go over each column name and value
         if(k=='hvac_temperature'):
            hvac.append(v)  # append the value into the appropriate list
         if (k == 'basement_temperature'):
            basement.append(v)
         if (k == 'main_temperature'):
            main.append(v)
         if (k == 'attic_temperature'):
            attic.append(v)
         if (k == 'episode'):
            episodes.append(v)


print(episodes)
print(attic)
print(main)

newEp=[]
newMain=[]
newAttic=[]
newHvac=[]
newBase=[]

for v in range(len(episodes)):
   if (v + 1) % 500 == 0 and v!=0:
      fig, ax = plt.subplots()
      ax.plot(newEp, newAttic)
      ax.plot(newEp, newMain)
      ax.plot(newEp,newBase)
      ax.plot(newEp,newHvac)
      plt.autoscale()
      plt.ylabel('value')
      plt.xlabel('episodes')
      plt.show()
      newAttic = []
      newEp = []
      newMain = []
      newBase=[]
      newHvac=[]
   newBase.append(basement[v])
   newEp.append(episodes[v])
   newAttic.append(attic[v])
   newMain.append(main[v])
   newHvac.append(hvac[v])
















         # with open('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/results1.csv', 'a',
#                   newline='') as f:
#    csv_writer = csv.writer(f)
#    for i in  range(len(columns)):
#       csv_writer.writerow([columns[i][0],columns[i][1],columns[i][2],columns[i][3],columns[i][4],columns[i][5]])



