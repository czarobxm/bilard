import os, sys, random
from pickle import FRAME
import pygame, pymunk
import pymunk.pygame_util
import numpy as np
from .CONST  import *
from .ball   import *
from .table  import *
from .hole   import *

class Pygame2D():
    def __init__(self): # DEFINING PYGAME, PYGAME SCREEN, PYMUNK SPACE, PYGAME CLOCK
        pygame.init()                           # start pygame
        self.pymunk_space  = pymunk.Space()     # initialize pymunk physics
        self.pygame_screen = pygame.display.set_mode(SCREEN_SIZE)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.pygame_screen)
        self.add_objects_to_pymunk()

        self.clock = pygame.time.Clock()
        #pygame.dt = 1
        #self.itt = 0
        #self.add_objects_to_pymunk()

        

    def close(self): # CLOSING PYGAME
        pygame.quit()
        #sys.exit(0)


    def draw(self): # DRAWING GANE ON SCREEN
        table.draw(self.pygame_screen)

        for hole in all_holes:
            hole.draw(self.pygame_screen)

        for ball in all_balls:
            ball.draw(self.pygame_screen)

    def refresh_screen(self):
        self.dt = self.clock.tick(FRAMERATE) #* FRAMERATE / 1000
        #pygame.display.update()
        pygame.display.flip()
        


    def mouse_pos(self): # GETTIN MOUSE POSITION
        return pygame.mouse.get_pos() # pobieranie pozycji myszki

    def stopped(self): # CHECKING IF BALLS ARE MOVING | FALSE IF BALLs ARE MOVING
        for ball in all_balls:
            if ball.body.velocity[0] != 0 or ball.body.velocity[1] != 0:
                return False
        print("stoją")
        return True

    def get_balls_pos(self):
        balls_pos = np.array([])
        
        for ball in all_balls:
            balls_pos = np.append(balls_pos, ball.body.position, axis=0)
        return balls_pos
    
    def get_balls_vel(self):
        for ball_string, ball in zip(all_balls_string, all_balls):
            print(f"{ball_string}: {ball.body.velocity}")

    def make_move(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x = convert_coordinates(self.mouse_pos())
                white_ball_full.body.velocity =1/50 * (x-white_ball_full.body.position)

    def make_action(self, action):
            if self.stopped():
                white_ball_full.body.velocity =1/50 * ((action[0],action[1])-white_ball_full.body.position)


    def friction_force(self, ball):    # SLOWING THE BALLS DOWN
        if  ball.body.velocity[0] > 0.2 or ball.body.velocity[1] > 0.2 or ball.body.velocity[0] < -0.2 or ball.body.velocity[1] < -0.2:
            ball.body.velocity -= ball.body.velocity * 0.0098
        else:
            ball.body.velocity = 0,0
                


    def add_objects_to_pymunk(self):
        table.add_to_pymunk_space(self.pymunk_space)

        for hole in all_holes:
            hole.add_to_pymunk_space(self.pymunk_space)
        
        

        for ball in all_balls:
            ball.body.position = ball.center
            ball.body.velocity = 0,0
            ball.add_to_pymunk_space(self.pymunk_space)

        for ball in all_balls_wo_white:
            ball.add_collision(self.pymunk_space)
        print(white_ball_full.body.position)

    def delete_objects_from_pymunk(self):
        table.remove_from_pymunk_space(self.pymunk_space)

        for hole in all_holes:
            hole.remove_from_pymunk_space(self.pymunk_space)
        
        for ball in all_balls:
            ball.remove_from_pymunk_space(self.pymunk_space)

    def action(self, action): 
        pygame.event.pump() # this makes pygame window work properly
        self.make_action(action)
        #self.get_balls_vel()
        for ball in all_balls:
            self.friction_force(ball)
        
    def evaluate(self):
        return 0

    def observe(self):
        #print(self.get_balls_pos())
        return self.get_balls_pos()
       

    def is_done(self):
        return False



