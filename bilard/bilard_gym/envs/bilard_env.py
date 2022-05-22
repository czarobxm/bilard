import gym
from gym import spaces
import numpy as np
import pygame, pymunk
import pymunk.pygame_util
from .pygame_2d import *
from .CONST import *


class BilardEnv(gym.Env):
    def __init__(self):
        self.bilard = Pygame2D()
        self.observation_space = spaces.Box(low=np.array(16 * [0, 0, 0]), high=np.array(16 * [1, 1, 1]))
        self.action_space = spaces.Box(low=np.array([0, 0, 0]), high=np.array([1, 1, 1]))

    def reset(self):
        if self.bilard.show_game:
            close()
        self.bilard.delete_objects_from_pymunk()
        self.bilard = Pygame2D()
        obs = self.bilard.observe()
        print("reset env\n")
        return obs

    def balls_stopped(self):
        return stopped()

    def step(self, action):
        """
        1. Make a move
        2. Change is_hit to False for every ball at the beginning of the move
        3. Save scaled action and save ball the model chose
        4. Calculate REWARD_1 on chosen action
        5. Calculate REWARD_2's starting distance between white ball and chosen ball
        6. For loop with game - rendering ball movements
        7. All balls have stopped.
        7. Calculate REWARD_2's ending distance between white ball and chosen ball (1 if the ball was hit)
        8. OBS, REWARD AND CHECKING IF GAME HAS ENDED
        :param action:
        :return:
        """
        print("\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        # stop balls if they were generated on each other
        if not stopped():
            while stopped():
                self.bilard.pymunk_space.step(1)
                friction()

        make_action(action)
        reset_balls()

        # SCALE ACTION, CHOOSE BALL AT THE BEGINNING OF THE STEP
        scaled_action = (action[0] * SCREEN_WIDTH, action[1] * SCREEN_LENGTH)
        self.bilard.closest_ball = choose_closest_ball(all_balls_wo_white, scaled_action)

        # REWARD 1
        d_rew_1 = self.bilard.d_rew_1(scaled_action)
        rew_1 = min(1, 50 / d_rew_1) * 1.5 - 1

        # REWARD 2 - calculate starting distance
        d_start_rew_2 = self.bilard.d_rew_2()

        # REWARD 3
         

        for i in range(500):
            # self.pygame.pymunk_space.step(1)
            self.render(action)

        print(f'action: {action}')
        print('ruch\n')
        while True:
            self.bilard.pymunk_space.step(1)
            friction()
            self.render(action)

            """
            for i in range(2):
                # self.pygame.pymunk_space.step(1)
                self.render(action)
            """
            # self.pygame.check_balls_pos()

            if stopped():
                # CALCULATE REWARD 2 - if ball was hit - give max rew value (1)
                print(self.bilard.closest_ball.is_hit)
                if self.bilard.closest_ball.is_hit:
                    print("bila trafiona")
                    rew_2 = 1
                else:
                    d_end_rew_2 = self.bilard.d_rew_2()
                    rew_2 = self.bilard.calculate_rew_2(d_start_rew_2, d_end_rew_2)

                # CALCULATE REWARD 3 FROM SAVED_VELOCITY OF CHOSEN BALL

                # add reward to final score
                self.bilard.finish_score += rew_1
                self.bilard.finish_score += rew_1 * rew_2
                print(f'rew_1: {rew_1}')
                print(f'rew_2: {rew_2}')

                # OBS, REWARD AND CHECKING IF GAME HAS ENDED
                obs = self.bilard.observe()
                reward = self.bilard.evaluate(action, obs)
                print(f"\nreward: {reward}\n")
                done = self.bilard.is_done(1)

                return obs, reward, done, {}

    def render(self, action, mode="human", close=False):
        if self.bilard.show_game:
            pygame.event.pump()  # this makes pygame window work properly
            self.bilard.draw()
            pygame.draw.circle(self.bilard.pygame_screen, (24, 254, 0),
                               convert_coordinates((action[0] * SCREEN_WIDTH, action[1] * SCREEN_LENGTH)), 10, True,
                               False, False, False)

            pygame.display.flip()
