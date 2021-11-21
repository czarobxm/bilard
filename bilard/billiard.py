import os, sys, random
import pygame, pymunk
from CONST  import *
from ball   import *
from table  import *
from hole   import *

class Game():
    def __init__(self): # DEFINING PYGAME, PYGAME SCREEN, PYMUNK SPACE, PYGAME CLOCK
        pygame.init()               # start pygame
        self.pymunk_space  = pymunk.Space()     # initialize pymunk physics
        self.pygame_screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        pygame.dt = 1
        
        self.game()

    def check_events(self): # CONTROL SETTINGS
        for event in pygame.event.get():
            # QUITTING PYGAME
            if event.type == pygame.QUIT:
                self.close()

            # MOVING WHITE BALL BY CHANGING ITS VELOCITY

            if event.type == pygame.MOUSEBUTTONUP:
                if self.stopped():
                    x = convert_coordinates(self.mouse_pos())
                    white_ball_full.body.velocity =1/50 * (x-white_ball_full.body.position)
            

    def close(self): # CLOSING PYGAME
        pygame.quit()
        sys.exit(0)


    def draw(self): # DRAWING GANE ON SCREEN
        table.draw(self.pygame_screen)

        for hole in all_holes:
            hole.draw(self.pygame_screen)

        for ball in all_balls:
            ball.draw(self.pygame_screen)

    def refresh_screen(self):
        pygame.display.update()
        self.dt = self.clock.tick(FRAMERATE) * FRAMERATE / 1000


    def mouse_pos(self): # GETTIN MOUSE POSITION
        return pygame.mouse.get_pos() # pobieranie pozycji myszki

    def stopped(self): # CHECKING IF BALLS ARE MOVING | FALSE IF BALLs ARE MOVING
        for ball in all_balls:
            if ball.body.velocity[0] != 0 or ball.body.velocity[1] != 0:
                return False
        print("stoją")
        return True

    def make_move(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x = convert_coordinates(self.mouse_pos())
                white_ball_full.body.velocity =1/50 * (x-white_ball_full.body.position)



    def friction_force(self, ball):    # SLOWING THE BALLS DOWN
        if  ball.body.velocity[0] > 0.2 or ball.body.velocity[1] > 0.2 or ball.body.velocity[0] < -0.2 or ball.body.velocity[1] < -0.2:
            ball.body.velocity -= ball.body.velocity * 0.0098
        else:
            ball.body.velocity = 0,0
                


    def add_objects_to_pymunk(self, all_balls, table):
        table.add_to_pymunk_space(self.pymunk_space)

        for hole in all_holes:
            hole.add_to_pymunk_space(self.pymunk_space)
        
        for ball in all_balls:
            ball.add_to_pymunk_space(self.pymunk_space)

        for ball in all_balls:
            ball.add_collision(self.pymunk_space)




    def game(self):

        self.add_objects_to_pymunk(all_balls, table)

        while True:
            self.pymunk_space.step(1)

            self.check_events()

            self.draw()
            self.refresh_screen()
            
            if not self.stopped():
                for ball in all_balls:
                    print(ball.body.velocity)
            
            for ball in all_balls:
                self.friction_force(ball)

            
                    
    

  

Game()