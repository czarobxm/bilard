from cgitb import reset
import gym
import bilard_gym

import pygame
import os

import tensorboard

from stable_baselines3 import SAC, PPO, A2C


# saving paths
models_dir = f"models/PPO"
log_dir = f"logs/PPO"
model_path = f"{models_dir}/296"


# creating directories for models and logs
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# making environment
env = gym.make('Bilard-v0')
env.reset()

# creating and loading model
model = PPO("MlpPolicy",
            env,
            verbose=2,
            tensorboard_log=log_dir,
            n_steps=1028,

            learning_rate=0.0001,
            #clip_range_vf=0.1,
            clip_range=0.1)

#model = model.load(model_path, env=env)

# Learning process
episodes = 250
TIMESTEPS = 2
tb_log_name = "PPO_two_rewards_reward2_1_if_ball_is_hit"

for i in range(1, episodes):
    print(f'{i} ' * 100)

    model.learn(total_timesteps=TIMESTEPS,
                reset_num_timesteps=False,
                tb_log_name=tb_log_name)
                #callback=TensorboardCallback())
    model.save(f"{models_dir}/{TIMESTEPS * i}")

obs = env.reset()

print("PREZENTACJA MODELU:")
for i in range(25):
    print(F"PREZENTACJA NR {i + 1}")
    env.render()
    action, _states = model.predict(obs, deterministic=False)
    print(action)
    obs, reward, done, info = env.step(action)
    if done:
        obs = env.reset()

env.close()

