import gym
import gym_game

import pygame

from stable_baselines3 import SAC, PPO

env = gym.make("Pygame-v0")

model = SAC("MlpPolicy", env, verbose=1)

#model = model.load("model_zapis1")


model.learn(total_timesteps=5)
model.save("model_zapis2")

obs = env.reset()


print("PREZENTACJA MODELU:")
for i in range(2):
    print(F"PREZENTACJA NR {i+1}")
    env.render()
    action, _states = model.predict(obs, deterministic=False)
    obs, reward, done, info = env.step(action)
    if done:
      obs = env.reset()

env.close()