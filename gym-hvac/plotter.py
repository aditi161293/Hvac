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
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import os
import sys


def plotter(episode, results_filename, output_dir, ylim):
    df = pd.read_csv('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/resultsSpecial.csv')
    #df = df[df['episode'] == episode]
    x = ['episode']
    y=['total_reward']

    # y = ['hvac_temperature',
    #      'basement_temperature',
    #      'main_temperature',
    #       'attic_temperature',
    #      'reward']
        # 'total_reward',
         #'reward']
    selected_df = df[x + y]
    melted_df = pd.melt(selected_df, id_vars=x, value_vars=y)
    sns.set(style="darkgrid")
    plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
    ax = sns.lineplot(x='episode', y='value', hue='variable', data=melted_df)
    ax.set(ylim= (0,30))
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #plt.title('Episode '+str(episode))
    plt.savefig(os.path.join('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output', '{:0>3}.png'.format(episode)), bbox_inches='tight')
    plt.show()
    # x = ['episode']
    # y = ['reward','action']
    # y = ['ground_temperature',
    #      'air_temperature',
    #      'hvac_temperature',
    #      'heat_added',
    #      'basement_temperature',
    #      'main_temperature',
    #      'attic_temperature']#,
    # 'total_reward',
    # 'reward']
    # selected_df = df[x + y]
    # melted_df = pd.melt(selected_df, id_vars=x, value_vars=y)
    # sns.set(style="darkgrid")
    # plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
    # ax = sns.lineplot(x='episode', y='value', hue='variable', data=melted_df)
    # ax.set(ylim=ylim)
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.savefig(
    #     os.path.join('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output', '{:0>3}.png'.format(episode)),
    #     bbox_inches='tight')
    # plt.show()
def __main__(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('output_dir')
    parser.add_argument('episode_upper', type=int)
    parser.add_argument('--episode_lower', type=int, default=0)
    parser.add_argument('--ylim_lower', type=float, default=-5)
    parser.add_argument('--ylim_upper', type=float, default=40)
    args = parser.parse_args(argv)
    vargs = vars(args)
    for episode in range(vargs['episode_lower'], vargs['episode_upper'] + 1):
        plotter(episode,
                os.path.join(vargs['output_dir'], 'D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output'),
                'D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/results.csv',
                (vargs['ylim_lower'], vargs['ylim_upper']))


if __name__ == '__main__':
    __main__(sys.argv)

# filename = '/home/rjohnson/school/machine_learning/Hvac/output/results_test.csv'
# # df = pd.DataFrame.from_csv(filename
# # rows = df.apply(lambda x: x.tolist(), axis=1
# cols = ["episode","step", "time", "air_temperature","ground_temperature","hvac_temperature",
#         "basement_temperature",	'main_temperature', "attic_temperature", "heat_added",
#         "action",'reward','total_reward','terminal']
#
# data = pd.read_csv(filename, names=cols, dtype=float, skiprows=1)
#
#
# episodes = data.episode.tolist()
# basement = data.basement_temperature.tolist()
# main = data.main_temperature.tolist()
# attic = data.attic_temperature.tolist()
# action = data.action.tolist()
# individual_rewards = data.reward.tolist()
# rewards = []
# for i in data.total_reward.tolist():
#         rewards.append(float(i) * .00001)
# max_target = rewards[-1]
#
#
#
# fig, ax = plt.subplots(1)
# ax.plot(episodes, main, 'c.')
# ax.plot(episodes, rewards)
# ax.set_title("Main Floor Temperatures")
# ax.axhline(y=21)
# ax.axhline(y=23.5)
# ax.axhline(y=26)
# ax.grid()
# ax.annotate('Target Min', xy=(3700, 21), xytext=(3500, 17), arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('Target Mean', xy=(3500, 23.5), xytext=(3500, 27.5), arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('Target Max', xy=(3300, 26), xytext=(3000, 30), arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('Overall Reward * .00001', xy=(episodes[-1], max_target), xytext=((episodes[-1] - 1000), max_target - 12), arrowprops=dict(facecolor='black', shrink=0.05))
#
# main, main_ax = plt.subplots(1)
# main_ax.grid()
# main_ax.plot(episodes, basement, 'r.')
# main_ax.plot(episodes, rewards)
# main_ax.set_title("Basement Floor Temperatures")
# main_ax.axhline(y=20)
# main_ax.axhline(y=21.5)
# main_ax.axhline(y=23)
#
# main_ax.annotate('Target Min', xy=(3700, 20), xytext=(3500, 16), arrowprops=dict(facecolor='black', shrink=0.05))
# main_ax.annotate('Target Mean', xy=(3500, 21.5), xytext=(3500, 25.5), arrowprops=dict(facecolor='black', shrink=0.05))
# main_ax.annotate('Target Max', xy=(3300, 23), xytext=(3000, 27), arrowprops=dict(facecolor='black', shrink=0.05))
# main_ax.annotate('Overall Reward * .00001', xy=(episodes[-1], max_target), xytext=((episodes[-1] - 1000), max_target - 12), arrowprops=dict(facecolor='black', shrink=0.05))
#
# _, attic_ax = plt.subplots(1)
# attic_ax.grid()
# attic_ax.plot(episodes, attic, 'r.')
# attic_ax.plot(episodes, rewards)
# attic_ax.set_title("Attic Floor Temperatures")
# attic_ax.axhline(y=20.5)
# attic_ax.axhline(y=19)
# attic_ax.axhline(y=22)
# attic_ax.annotate('Target Min', xy=(3700, 19), xytext=(3500, 15), arrowprops=dict(facecolor='black', shrink=0.05))
# attic_ax.annotate('Target Mean', xy=(3500, 20.5), xytext=(3500, 24.5), arrowprops=dict(facecolor='black', shrink=0.05))
# attic_ax.annotate('Target Max', xy=(3300, 22), xytext=(3000, 26), arrowprops=dict(facecolor='black', shrink=0.05))
# attic_ax.annotate('Overall Reward * .00001', xy=(episodes[-1], max_target), xytext=((episodes[-1] - 1000), max_target - 12), arrowprops=dict(facecolor='black', shrink=0.05))
#
#
#
# _, reward = plt.subplots(1)
# reward.grid()
# r_line, = reward.plot(episodes, individual_rewards, 'r.')
# r_line.set_label("Rewards")
# reward.plot(episodes, action, 'c.')
# reward.set_title("Rewards vs Actions")
# reward.legend()
#
#
# plt.show()
