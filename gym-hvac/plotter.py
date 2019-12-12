import numpy as n
import pandas as pd
import matplotlib.pyplot as plt 
import sys


filename = sys.argv[1]
# filename = '/home/rjohnson/school/machine_learning/Hvac/output/outpu_results.csv'
# df = pd.DataFrame.from_csv(filename
# rows = df.apply(lambda x: x.tolist(), axis=1
cols = ["episode","step", "time", "air_temperature","ground_temperature","hvac_temperature",	
        "basement_temperature",	'main_temperature', "attic_temperature", "heat_added",	
        "action",'reward','total_reward','terminal']

data = pd.read_csv(filename, names=cols, dtype=float, skiprows=1) 


episodes = data.episode.tolist()
basement = data.basement_temperature.tolist()
main = data.main_temperature.tolist()
attic = data.attic_temperature.tolist()
action = data.action.tolist()
individual_rewards = data.reward.tolist()
steps = data.step.tolist()
air_temps = data.air_temperature.tolist()
rewards = []
terminal = data.terminal.tolist()

plt.ion()
# ax = plt.gca()

# index = 128028
index = 0
reward = []
current_steps = []
actions = []
c_base = []
c_main = []
c_atic = []
c_airtemp = []
#fig, ax = plt.subplots(3, sharex=True, clear=True)
plt.rcParams["figure.figsize"] = [16,9]


if len(sys.argv) == 3 and sys.argv[2] == 'final':

        fig, ax = plt.subplots(3, sharex=True)
        ax[0].plot(episodes, main, 'c')
        ax[0].set_title("Main Floor Temperatures")
        ax[0].axhline(y=21)
        ax[0].axhline(y=23.5)
        ax[0].axhline(y=26)
        ax[0].grid()
        ax[0].set_ylabel("Celsius")

        ax[1].grid()
        ax[1].plot(episodes, basement, 'r')
        ax[1].set_title("Basement Floor Temperatures")
        ax[1].axhline(y=20)
        ax[1].axhline(y=21.5)
        ax[1].axhline(y=23)
        ax[1].annotate('Target Min', xy=(3700, 20), xytext=(3500, 16), arrowprops=dict(facecolor='black', shrink=0.05))
        ax[1].annotate('Target Mean', xy=(3500, 21.5), xytext=(3500, 25.5), arrowprops=dict(facecolor='black', shrink=0.05))
        ax[1].annotate('Target Max', xy=(3300, 23), xytext=(3000, 27), arrowprops=dict(facecolor='black', shrink=0.05))
        ax[1].set_ylabel("Celsius")



        ax[2].grid()
        ax[2].plot(episodes, attic, 'g')
        ax[2].set_title("Attic Floor Temperatures")
        ax[2].axhline(y=20.5)
        ax[2].axhline(y=19)
        ax[2].axhline(y=22)
        ax[2].annotate('Target Min', xy=(3700, 19), xytext=(3500, 15), arrowprops=dict(facecolor='black', shrink=0.05))
        ax[2].annotate('Target Mean', xy=(3500, 20.5), xytext=(3500, 24.5), arrowprops=dict(facecolor='black', shrink=0.05))
        ax[2].annotate('Target Max', xy=(3300, 22), xytext=(3000, 26), arrowprops=dict(facecolor='black', shrink=0.05))
        
        ax[2].set_xlabel("Epochs")
        ax[2].set_ylabel("Celsius")
        
        plt.savefig("output/all.png")
        plt.draw()
        plt.show()
        plt.pause(50)
else:
        for i in terminal[index:]:
                if i == 1.0:
                        ax1 = plt.subplot(211)

                        ma, = ax1.plot(current_steps, c_main)
                        ba, = ax1.plot(current_steps, c_base)
                        at, = ax1.plot(current_steps, c_atic)
                        air, = ax1.plot(c_airtemp, color='c', ls='-')
                        no = ax1.axhline(y=25, color='g', ls='--')
                        low = ax1.axhline(y=38, color='r', ls='--')
                        high = ax1.axhline(y=9, color='r', ls='--')
                        done = ax1.axvline(x=96, color='b')
                        done.set_label("Full day")
                        air.set_label("Air Temperature")
                        low.set_label("Low Cut Off")
                        high.set_label("High Cut Off")
                        no.set_label("Target Temp")
                        ma.set_label("Main")
                        ba.set_label("Basement")
                        at.set_label("Attic")
                        ax1.set_title(f"Day: {int(episodes[index])}")
                        ax1.set_ylim([-20,50])
                        ax1.set_xlim([-5,120])
                        ax1.set_ylabel("Temperatures in Celsius")
                        
                        ax1.legend()
                        ax1.grid()

                        no_action = 1
                        ax3 = plt.subplot(212)

                        #ax3.plot(current_steps, actions)
                        ax3.step(current_steps, actions)
                        done = ax3.axvline(x=96, color='b')
                        done.set_label("Full day")
                        ax3.set_ylim([-.5,3])
                        ax3.set_xlim([-5,120])
                        no = ax3.axhline(y=1, color='g', ls='--')
                        heat = ax3.axhline(y=2.5, color='r', ls='--')
                        cool = ax3.axhline(y=0, color='b', ls='--')
                        no.set_label("No action")
                        heat.set_label("Hot Air")
                        cool.set_label("Cool Air")
                        ax3.set_ylabel("HVAC Action")
                        ax3.set_xlabel("Training Steps for each epoch, max = 96 (1 day)")
                        ax3.legend()
                        ax3.grid()

                        # if episodes[index] >= 2350: #or episodes[index] % 500 == 0:
                        #         plt.savefig(f'output/figs/changing/epoch_{int(episodes[index])}.png',bbox_inches='tight')
                        #         print(f'Saved: {episodes[index]}')
                        # print(f'At: {episodes[index]}')
                        plt.show()
                        plt.pause(.251)

                        c_atic.clear()
                        c_main.clear()
                        c_base.clear()
                        reward.clear()
                        c_airtemp.clear()
                        current_steps.clear()
                        actions.clear()
                        plt.clf()
                else:
                        reward.append(individual_rewards[index])
                        current_steps.append(steps[index])
                        actions.append(action[index])
                        c_base.append(basement[index])
                        c_main.append(main[index])
                        c_atic.append(attic[index])
                        c_airtemp.append(air_temps[index])

                index += 1



# Put these plots in subplots
  

# fig, ax = plt.subplots(3, sharex=True)
# ax[0].plot(episodes, main, 'c')
# # ax.plot(episodes, rewards)
# ax[0].set_title("Main Floor Temperatures")
# ax[0].axhline(y=21)
# ax[0].axhline(y=23.5)
# ax[0].axhline(y=26)
# ax[0].grid()
# # ax[0].annotate('Target Min', xy=(3700, 21), xytext=(3500, 17), arrowprops=dict(facecolor='black', shrink=0.05))
# # ax[0].annotate('Target Mean', xy=(3500, 23.5), xytext=(3500, 27.5), arrowprops=dict(facecolor='black', shrink=0.05))
# # ax[0].annotate('Target Max', xy=(3300, 26), xytext=(3000, 30), arrowprops=dict(facecolor='black', shrink=0.05))
# # ax.annotate('Overall Reward * .00001', xy=(episodes[-1], max_target), xytext=((episodes[-1] / 2 - 15), max_target - 12), arrowprops=dict(facecolor='black', shrink=0.05))

# ax[1].grid()
# ax[1].plot(episodes, basement, 'r')
# ax[1].set_title("Basement Floor Temperatures")
# ax[1].axhline(y=20)
# ax[1].axhline(y=21.5)
# ax[1].axhline(y=23)
# ax[1].annotate('Target Min', xy=(3700, 20), xytext=(3500, 16), arrowprops=dict(facecolor='black', shrink=0.05))
# ax[1].annotate('Target Mean', xy=(3500, 21.5), xytext=(3500, 25.5), arrowprops=dict(facecolor='black', shrink=0.05))
# ax[1].annotate('Target Max', xy=(3300, 23), xytext=(3000, 27), arrowprops=dict(facecolor='black', shrink=0.05))

# # _, attic_ax = plt.add_subplot(113)
# ax[2].grid()
# ax[2].plot(episodes, attic, 'r')
# ax[2].set_title("Attic Floor Temperatures")
# ax[2].axhline(y=20.5)
# ax[2].axhline(y=19)
# ax[2].axhline(y=22)
# ax[2].annotate('Target Min', xy=(3700, 19), xytext=(3500, 15), arrowprops=dict(facecolor='black', shrink=0.05))
# ax[2].annotate('Target Mean', xy=(3500, 20.5), xytext=(3500, 24.5), arrowprops=dict(facecolor='black', shrink=0.05))
# ax[2].annotate('Target Max', xy=(3300, 22), xytext=(3000, 26), arrowprops=dict(facecolor='black', shrink=0.05))



# # _, reward = plt.subplots(1)
# # reward.grid()
# # r_line, = reward.plot(episodes, individual_rewards, 'r')
# # r_line.set_label("Rewards")
# # reward.plot(episodes, action, 'c')
# # reward.set_title("Rewards vs Actions")
# # reward.legend()


# plt.show()
