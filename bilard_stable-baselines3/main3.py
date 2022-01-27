import gym
import gym_game

import pygame

from stable_baselines3 import PPO

env = gym.make("Pygame-v0")

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100)

obs = env.reset()
for i in range(10000):
    env.render()
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    
    if done:
      obs = env.reset()

env.close()