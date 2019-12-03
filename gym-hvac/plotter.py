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
rewards = []
terminal = data.terminal.tolist()

for i in data.total_reward.tolist():
        rewards.append(float(i) * .00001)
max_target = rewards[-1]


plt.ion()
# ax = plt.gca()

index = 179970
reward = []
current_steps = []
actions = []
c_base = []
c_main = []
c_atic = []
#fig, ax = plt.subplots(3, sharex=True, clear=True)
plt.rcParams["figure.figsize"] = [16,9]
for i in terminal[index:]:
        if i == 1.0:
                """
                # # rew, = plt.plot(current_steps, reward)
                # # act, = plt.plot(current_steps, actions)
                # # rew.set_label('Reward')
                # # act.set_label('Action')
                # # plt.text(5, 150, f'Epoch: {epoch}')
                # # plt.plot(current_steps, reward)
                # # plt.plot(current_steps, actions)
                
                # at, = plt.plot(current_steps, c_atic)
                # m, = plt.plot(current_steps, c_main)
                # b, = plt.plot(current_steps, c_base)

                # at.set_label('Attic')
                # m.set_label('Main')
                # b.set_label('Basement')
                # # rew.set_label('Rewards')
                # # act.set_label('Action')
                # plt.ylim(top=30)
                # plt.ylim(bottom=10)
                # plt.xlim(right=110)
                # plt.xlim(left=0)
                # plt.xlabel(f'Number of Steps to Terminal | Epoch: {epoch}')
                # plt.ylabel('Epoch Reward')
                # plt.legend()
                # plt.draw()
                # # plt.show()
                # plt.pause(.001)
                
                # reward.clear()
                # actions.clear()
                # current_steps.clear()

                # c_atic.clear()
                # c_main.clear()
                # c_base.clear()
                # epoch += 1
                """
                ax1 = plt.subplot(311)

                #ax[0].set_ylim(right=110)
                #ax[0].xlim(right=110)
                #ax[0].xlim(left=0)
                ma, = ax1.plot(current_steps, c_main)
                ba, = ax1.plot(current_steps, c_base)
                at, = ax1.plot(current_steps, c_atic)
                no = ax1.axhline(y=25, color='g', ls='--')
                low = ax1.axhline(y=38, color='r', ls='--')
                high = ax1.axhline(y=12, color='r', ls='--')
                low.set_label("Low Cut Off")
                high.set_label("High Cut Off")
                no.set_label("Target Temp")
                ma.set_label("Main")
                ba.set_label("Basement")
                at.set_label("Attic")
                ax1.set_title(f"Temperatures | Epoch: {int(episodes[index])}")
                ax1.set_ylim([10,40])
                ax1.set_xlim([-5,110])
                ax1.legend()
                ax1.grid()

                ax2 = plt.subplot(312)

                ax2.plot(current_steps, reward)
                ax2.set_title("Rewards")
                ax2.set_ylim([-30,30])
                ax2.set_xlim([-5,110])
                ax2.grid()


                no_action = 1
                ax3 = plt.subplot(313)

                ax3.plot(current_steps, actions)
                ax3.set_title("HVAC Action")
                ax3.set_ylim([-.5,3])
                ax3.set_xlim([-5,110])
                no = ax3.axhline(y=1, color='g', ls='--')
                heat = ax3.axhline(y=2, color='r', ls='--')
                cool = ax3.axhline(y=0, color='b', ls='--')
                no.set_label("No action")
                heat.set_label("Hot Air")
                cool.set_label("Cool Air")
                ax3.legend()
                ax3.grid()

                if episodes[index] == 0 or episodes[index] == 50 or episodes[index] % 100 == 0:
                        plt.savefig(f'output/figs/epoch_{int(episodes[index])}.png',bbox_inches='tight')
                        # exit(0)
                # plt.show()
                # plt.pause(.001)

                c_atic.clear()
                c_main.clear()
                c_base.clear()
                reward.clear()
                current_steps.clear()
                actions.clear()
                plt.clf()
                print(f'Epoch: {episodes[index]}')
        else:
                reward.append(individual_rewards[index])
                current_steps.append(steps[index])
                actions.append(action[index])
                c_base.append(basement[index])
                c_main.append(main[index])
                c_atic.append(attic[index])


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
