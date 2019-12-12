import pandas as pd
import matplotlib.pyplot as plt

filename = 'D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/results.csv'

cols = ["episode","step", "time", "air_temperature","ground_temperature","hvac_temperature",
        "basement_temperature",	'main_temperature', "attic_temperature", "heat_added",
        "action",'reward','total_reward','terminal']

data = pd.read_csv(filename, names=cols, dtype=float, skiprows=1)


episodes = data.episode.tolist()
terminal=data.terminal.tolist()
basement = data.basement_temperature.tolist()
main = data.main_temperature.tolist()
attic = data.attic_temperature.tolist()
action = data.action.tolist()
individual_rewards = data.reward.tolist()
totalReward=data.total_reward.tolist()
newTR=[]
print(len(terminal))
for i in range(len(terminal)):
    if(terminal[i]==1.0):
        newTR.append(totalReward[i])
print(len(newTR))


#print(newTR)

t=0
tr=[]
ep=[]
tm=[]


j=1
tr1=[-0.07666666666666666, 68.92395092603361, 178.5852483483582, 376.6126789280439, 475.07047316289504, 684.8134959491406, 497.3610408785065, 791.4098635927784, 634.91755476446383, 1054.1396665687266, 601.8236740142657, 709.84364945612623, 646.3932871336236, 617.4051231981848, 963.2795105032891, 839.2568531407051, 663.1696464271613, 890.0326243605606,789,832,934, 1063.5950368893541,900,923,855, 1006.2675996854314,956, 978.7536264878142,1065,1029,938]

for r in newTR:
    t=t+r
    tm.append(t)
    if j%100==0 or j==1:
        t=t/100
        tr.append(t)
        ep.append(j)
        t=0
    j=j+1

print(len(tr))
print(tr)
e=[-3,-4,5]
y=[1,2,3]
plt.plot(ep,tr)
plt.grid(True)
plt.ylabel("Total Reward")
plt.xlabel("Episodes")
#plt.ylim([-4000,840000])
plt.show()






