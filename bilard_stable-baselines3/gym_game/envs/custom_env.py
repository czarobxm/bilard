import gym
from gym import spaces
import numpy as np
import pygame, pymunk
import pymunk.pygame_util
from .CONST import LEFT_BOTTOM_CORNER, LEFT_UPPER_CORNER, LENGTH_TABLE, RIGHT_BOTTOM_CORNER, WIDTH_TABLE
from .pygame_2d import Pygame2D


class CustomEnv(gym.Env):
    #metadata = {'render.modes' : ['human']}
    def __init__(self):
        self.pygame = Pygame2D()
        
        self.observation_space = spaces.Box(low = np.array(16*[0,0]), high = np.array(16*[LENGTH_TABLE,WIDTH_TABLE]))
        self.action_space = spaces.Box(low = np.array([10,10]), high = np.array([1000,700]))

        self.draw_options = pymunk.pygame_util.DrawOptions(self.pygame.pygame_screen)

    def reset(self):
        self.pygame.close()
        self.pygame.delete_objects_from_pymunk()
        self.pygame = Pygame2D()
        obs = self.pygame.observe()
        return obs

    def step(self, action):
        self.pygame.action(action)
        obs = self.pygame.observe()
        reward = self.pygame.evaluate()
        done = self.pygame.is_done()
        self.pygame.pymunk_space.step(1)
        return obs, reward, done, {}

    def render(self, mode="human", close=False):
        self.pygame.draw()
        pygame.display.flip()
