import os, sys, random
import pygame, pymunk
from CONST  import *
from ball   import *
from table  import *
from hole   import *
#from colision_handlers import *

class Game():

    def add_collision_handlers(self, pymunk_space):
        handler_yellow_full_hole    = pymunk_space.add_collision_handler(0, 1)
        handler_blue_full_hole      = pymunk_space.add_collision_handler(0, 2)
        handler_red_full_hole       = pymunk_space.add_collision_handler(0, 3)
        handler_purple_full_hole    = pymunk_space.add_collision_handler(0, 4)
        handler_orange_full_hole    = pymunk_space.add_collision_handler(0, 5)
        handler_green_full_hole     = pymunk_space.add_collision_handler(0, 6)
        handler_brown_full_hole     = pymunk_space.add_collision_handler(0, 7)
        handler_black_full_hole     = pymunk_space.add_collision_handler(0, 8)

        handler_yellow_stripes_hole = pymunk_space.add_collision_handler(0, 9)
        handler_blue_stripes_hole   = pymunk_space.add_collision_handler(0, 10)
        handler_red_stripes_hole    = pymunk_space.add_collision_handler(0, 11)
        handler_purple_stripes_hole = pymunk_space.add_collision_handler(0, 12)
        handler_orange_stripes_hole = pymunk_space.add_collision_handler(0, 13)
        handler_green_stripes_hole  = pymunk_space.add_collision_handler(0, 14)
        handler_brown_stripes_hole  = pymunk_space.add_collision_handler(0, 15)

        handler_white_full_hole     = pymunk_space.add_collision_handler(0, 16)

       

        all_handlers = [handler_yellow_full_hole, handler_blue_full_hole,
                        handler_red_full_hole, handler_purple_full_hole,
                        handler_orange_full_hole, handler_green_full_hole,
                        handler_brown_full_hole, handler_black_full_hole,
                        handler_yellow_stripes_hole, handler_blue_stripes_hole,
                        handler_red_stripes_hole, handler_purple_stripes_hole,
                        handler_orange_stripes_hole, handler_green_stripes_hole,
                        handler_brown_stripes_hole, handler_white_full_hole]

        for i in range(0,16):
            all_handlers[i].post_solve = all_balls[i].in_hole

    def moving(self, ball): # CHECKING IF BALLS ARE MOVING | TRUE IF BALLs ARE MOVING
        if ball.body.velocity[0] == 0 and ball.body.velocity[1] == 0:
            return False
        else:
            return True
    
    def friction_force(self, ball):    # SLOWING THE BALLS DOWN
        if  ball.body.velocity[0] > 0.2 or ball.body.velocity[1] > 0.2 or ball.body.velocity[0] < -0.2 or ball.body.velocity[1] < -0.2:
            ball.body.velocity -= ball.body.velocity * 0.0098
        else:
            ball.body.velocity = 0,0
                
    def mouse_pos(self):
            return pygame.mouse.get_pos() # pobieranie pozycji myszki

    def __init__(self):
        pygame.init()               # start pygame
        self.pymunk_space  = pymunk.Space()     # initialize pymunk physics
        self.pygame_screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        pygame.dt = 1
        
        self.game()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
            if event.type == pygame.MOUSEBUTTONUP:
                x = convert_coordinates(self.mouse_pos())
                #white_ball_full.body.apply_impulse_at_local_point(x-white_ball_full.body.position, (0,0)) # coś się psuje po uderzeniu białą w inną kulę
                white_ball_full.body.velocity =1/50 * (x-white_ball_full.body.position)
                

    def close(self):
        pygame.quit()
        sys.exit(0)

    def add_objects_to_pymunk(self, all_balls, table):
        table.add_to_pymunk_space(self.pymunk_space)

        for hole in all_holes:
            hole.add_to_pymunk_space(self.pymunk_space)
        
        for ball in all_balls:
            ball.add_to_pymunk_space(self.pymunk_space)

        self.add_collision_handlers(self.pymunk_space)

    def refresh_screen(self):
        pygame.display.update()
        self.dt = self.clock.tick(FRAMERATE) * FRAMERATE / 1000

    def draw(self):
        table.draw(self.pygame_screen)

        for hole in all_holes:
            hole.draw(self.pygame_screen)

        for ball in all_balls:
            ball.draw(self.pygame_screen)


    def game(self):

        self.add_objects_to_pymunk(all_balls, table)

        while True:
            self.pymunk_space.step(1)

            self.check_events()
            self.draw()
            self.refresh_screen()

            for ball in all_balls:
                if self.moving(ball):
                    self.friction_force(ball)

            
                    
    

  

Game()