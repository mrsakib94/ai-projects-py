import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np


#  Function to select an action based on the action selection code
# 0: random action, 1: push to the right, 2: two rules, 3: four rules, 4: enhanced rule
def select_action(action_selection_code):
    if action_selection_code == 0:
        action = env.action_space.sample()  # random action
    elif action_selection_code == 1:
        action = 2  # push to the right
    elif action_selection_code == 2:
        # two rules
        if observation[0] > -0.53 and observation[1] > 0:
            action = 2
        elif observation[0] < -0.53 and observation[1] < 0:
            action = 0
        else:
            action = 1
    elif action_selection_code == 3:
        # four rules
        if observation[0] > -0.53 and observation[1] > 0:
            action = 2
        elif observation[0] < -0.53 and observation[1] < 0:
            action = 0
        elif observation[0] < -0.53 and observation[1] > 0:
            action = 2
        elif observation[0] > -0.53 and observation[1] < 0:
            action = 0
        else:
            action = 1
    elif action_selection_code == 4:
        # enhanced rule using velocity trend
        if observation[0] > -0.53 and observation[1] > 0:
            action = 2
        elif observation[0] < -0.53 and observation[1] < 0:
            action = 0
        elif observation[0] < -0.53 and observation[1] > 0:
            action = 2
        elif observation[0] > -0.53 and observation[1] < 0:
            action = 0
        elif observation[0] < 0 and observation[1] < prev_velocity:
            action = 0
        elif observation[0] > 0 and observation[1] > prev_velocity:
            action = 2
        else:
            action = 1
    else:
        action = 1

    return action


print("Starting Mountain Car")

env = gym.make("MountainCar-v0")
# env = gym.make("MountainCar-v0", render_mode="human")
observation, info = env.reset()
iter = 200
agents = 100
approaches = 5
prev_velocity = 0  # initialise previous velocity for enhanced rule

steps = np.zeros((agents, approaches))

# Run the simulation for different approaches
# 0: random action, 1: push to the right, 2: two rules, 3: four rules, 4: enhanced rule
for k in range(approaches):
    print("Running approach %i" % k)
    for j in range(agents):
        for i in range(iter):
            # 0: random action, 1: push to the right, 2: two rules, 3: four rules
            action = select_action(k)
            observation, reward, terminated, truncated, info = env.step(action)
            # print(observation)

            if terminated or truncated:
                observation, info = env.reset()
                break

        print("Finished in %i steps" % i)
        steps[j][k] = i

# Plot the results
bp = plt.boxplot(steps, showmeans=True)
plt.title("Number of steps needed")
plt.xlabel("Method")
plt.ylabel("Actions")
plt.xticks(np.arange(1, 6), ('Random', 'Always right',
           'Two rules', 'Four rules', 'Enhanced rule'))
plt.show()

print("Closing environment")
env.close()
