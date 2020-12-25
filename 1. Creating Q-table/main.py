import gym
import numpy as np

env = gym.make("MountainCar-v0")   # selecting an envirnment
env.reset()

# For creating Q-table
print(env.observation_space)  
print(env.observation_space.high)   #[0.6  0.07]
print(env.observation_space.low)  #[-1.2  -0.07]
print(env.action_space.n)  #3

DISCRETE_OS_SIZE= [20] * len(env.observation_space.high) #[20,20]
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE  #[0.09  0.007]

print(env.observation_space.high - env.observation_space.low)
print(discrete_os_win_size)


q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

print(q_table.shape)  # (20, 20, 3)
print(q_table)

###  This is env
done = False

while not done:
    action = 2
    new_state, reward, done, info = env.step(action)
    print(new_state,reward)
    env.render()

env.close()