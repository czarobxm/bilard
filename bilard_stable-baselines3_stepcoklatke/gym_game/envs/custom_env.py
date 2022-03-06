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
        
        self.observation_space = spaces.Box(low = np.array(16*[-1,-1]), high = np.array(16*[1,1]))
        self.action_space = spaces.Box(low = np.array([-1,-1]), high = np.array([1,1]))

        self.draw_options = pymunk.pygame_util.DrawOptions(self.pygame.pygame_screen)

    def reset(self):
        self.pygame.close()
        self.pygame.delete_objects_from_pymunk()
        self.pygame = Pygame2D()
        obs = self.pygame.observe()
        print("reset env\n")
        return obs

    def balls_stopped(self):
        return self.pygame.stopped()

    def step(self, action):
        self.pygame.make_action(action)
        print('ruch')
        while(True):
            self.pygame.pymunk_space.step(1)
            self.pygame.friction()
            self.render()
            #print(self.balls_stopped())
            if self.pygame.stopped():
                
                
                obs = self.pygame.observe()
                reward = self.pygame.evaluate()
                print(f"reward: {reward}")
                done = self.pygame.is_done()
                return obs, reward, done, {}
        
        
    def render(self, mode="human", close=False):
        self.pygame.draw()
        pygame.display.flip()
