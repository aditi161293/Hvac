import csv
import random
import gym
import os

import gym_hvac
from gym_hvac import *
import matplotlib.pyplot as plt


import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

ENV_NAME = "HVAC-v0"

GAMMA = 0.95
LEARNING_RATE = 0.001

MEMORY_SIZE = 1000000
BATCH_SIZE = 20

EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995
checkpoint_fname = "checkpoint1.h5"



class DQNSolver:

    def __init__(self, observation_space, action_space):
        self.exploration_rate = EXPLORATION_MAX

        self.action_space = action_space
        self.memory = deque(maxlen=MEMORY_SIZE)

        self.model = Sequential()
        self.model.add(Dense(24, input_shape=(observation_space,), activation="relu"))
        self.model.add(Dense(24, activation="relu"))
        self.model.add(Dense(self.action_space, activation="linear"))
        self.model.compile(loss="mse", optimizer=Adam(lr=LEARNING_RATE))

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() < self.exploration_rate:
            return random.randrange(self.action_space)
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])

    def experience_replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        batch = random.sample(self.memory, BATCH_SIZE)
        for state, action, reward, state_next, terminal in batch:
            q_update = reward
            if not terminal:
                q_update = (reward + GAMMA * np.amax(self.model.predict(state_next)[0]))
            q_values = self.model.predict(state)
            q_values[0][action] = q_update
            self.model.fit(state, q_values, verbose=0)
        self.exploration_rate *= EXPLORATION_DECAY
        self.exploration_rate = max(EXPLORATION_MIN, self.exploration_rate)

def hvac():
    env = gym.make(ENV_NAME)
    observation_space = env.observation_space.shape[0]
    action_space = env.action_space.n
    dqn_solver = DQNSolver(observation_space, action_space)
    run = 0
    mainTemList=[]
    basementTempList=[]
    atticTempList=[]
    heaterTempList=[]
    timeList=[]


    with open('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/results.csv', 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['episode',
                             'step',
                             'time',
                             'air_temperature',
                             'ground_temperature',
                             'hvac_temperature',
                             'basement_temperature',
                             'main_temperature',
                             'attic_temperature',
                             'heat_added',
                             'action',
                             'reward',
                             'total_reward',
                             'terminal'])

    while run<1500:
        state = env.reset()
        state = np.reshape(state, [1, observation_space])
        step = 0
        while True:
            action = dqn_solver.act(state)
            state_next, reward, terminal, info = env.step(action)
            with open('D:/Study Material/Clean Energy/CleanEnergyHVACGroup-master/output/results.csv', 'a', newline='') as outfile:
                csv_writer = csv.writer(outfile)
                csv_writer.writerow([run, step, env.time] +
                                    state_next.tolist() +
                                    [env.total_heat_added, int(action), reward, env.total_reward, terminal])
            reward = reward if not terminal else -reward

            state_next = np.reshape(state_next, [1, observation_space])
            sn=state_next.tolist()

            dqn_solver.remember(state, action, reward, state_next, terminal)
            state = state_next

            if terminal:
                if(run%50==0):
                    mainTemList.append(sn[0][4])
                    atticTempList.append(sn[0][5])
                    basementTempList.append(sn[0][3])
                    heaterTempList.append(sn[0][2] + 20)
                    timeList.append(env.time / 60)

                print("Run: " + str(run) + ", exploration: " + str(dqn_solver.exploration_rate) + ", score: " + str(step) + ", Total_reward: "+str(env.total_reward))
                break
            dqn_solver.experience_replay()
            step += 1
        if run % 100 == 0:
            dqn_solver.model.save_weights(checkpoint_fname, overwrite=True)
            print("model saved")
            if os.path.exists(checkpoint_fname):
                dqn_solver.model.load_weights(checkpoint_fname)
                print("Restored")
            else:
                print("Training fresh model")

        run += 1
    return mainTemList,atticTempList,basementTempList,heaterTempList,timeList

# we will use this later to check our network is learning orr not
# if os.path.exists(checkpoint_fname):
#     dqn_solver.model.load_weights(checkpoint_fname)
#     print("Restored")
# else:
#     print("Training fresh model")




if __name__ == "__main__":
    mainTemp,atticTemp,basementTemp,heaterTemp,time=hvac()
    print(mainTemp)
    print(atticTemp)
    print(basementTemp)
    print(heaterTemp)
    print(time)

    plt.plot(time,mainTemp)
    plt.plot(time,atticTemp)
    plt.plot(time,basementTemp)
    plt.plot(time,heaterTemp)
    plt.show()
