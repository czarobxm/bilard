import os, sys, random
import pygame, pymunk
from CONST import *

class BallStripes():
    def __init__(self, center, color, collision_type):
        moment = pymunk.moment_for_circle(MASS, 0, SIZE_BALL)
        self.center = center
        self.color = color
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = center
        self.shape = pymunk.Circle(self.body, SIZE_BALL)
        self.shape.mass = MASS
        self.shape.elasticity = ELASTICITY
        self.shape.density = DENCITY
        self.shape.collision_type = collision_type

    def draw(self, screen):
        pygame.draw.circle( screen , self.color , convert_coordinates(self.body.position) , SIZE_BALL , True , False , False , False)
        pygame.draw.line( screen , self.color , convert_coordinates(self.body.position - (SIZE_BALL,0)) , convert_coordinates(self.body.position + (SIZE_BALL,0)))

    def in_hole(self, arbiter, space, data):
        self.body.position = ( 3 * SIZE_BALL, 2 * (SIZE_BALL + 2) * self.shape.collision_type + SIZE_BALL)
        self.body.velocity = (0,0)
        

    def add_to_pymunk_space(self,space):
        space.add(self.body, self.shape)

    def moving(self):
        if self.body.velocity[0] == 0 and self.body.velocity[1] == 0:
            return True
        return False

class BallFulls():
    def __init__(self, center, color, collision_type):
        mass=0
        self.center = center
        self.color = color
        self.body = pymunk.Body()
        self.body.position = center
        self.shape = pymunk.Circle(self.body, SIZE_BALL)
        self.shape.mass = MASS
        self.shape.elasticity = ELASTICITY
        self.shape.density = DENCITY
        self.shape.friction = 1
        self.shape.collision_type = collision_type

    def draw(self, screen):
        pygame.draw.circle( screen , self.color , convert_coordinates(self.body.position) , SIZE_BALL , True , False , False , False)

    def hit_ball(self, power):
        self.body.apply_force_at_local_point(power)

    def in_hole(self, arbiter, space, data):
        self.body.position = ( 3 * SIZE_BALL, 2 * (SIZE_BALL + 2) * self.shape.collision_type + SIZE_BALL)
        self.body.velocity = (0,0)

    def add_to_pymunk_space(self,pymunk_space):
        pymunk_space.add(self.body, self.shape)

    def moving(self):
        if self.body.velocity[0] == 0 and self.body.velocity[1] == 0:
            return True
        return False


#################### INITIALIZING BALLS
yellow_ball_full    = BallFulls(POS_1ST, YELLOW , 1)
blue_ball_full      = BallFulls(POS_2ND, BLUE   , 2)
red_ball_full       = BallFulls(POS_3RD, RED    , 3)
purple_ball_full    = BallFulls(POS_4TH, PURPLE , 4)
orange_ball_full    = BallFulls(POS_5TH, ORANGE , 5)
green_ball_full     = BallFulls(POS_6TH, GREEN  , 6)
brown_ball_full     = BallFulls(POS_7TH, BROWN  , 7)

black_ball_full = BallFulls(POS_8TH, BLACK, 8) 

yellow_ball_stripes = BallStripes(POS_9TH  , YELLOW , 9)
blue_ball_stripes   = BallStripes(POS_10TH , BLUE   , 10)
red_ball_stripes    = BallStripes(POS_11TH , RED    , 11)
purple_ball_stripes = BallStripes(POS_12TH , PURPLE , 12)
orange_ball_stripes = BallStripes(POS_13TH , ORANGE , 13)
green_ball_stripes  = BallStripes(POS_14TH , GREEN  , 14)
brown_ball_stripes  = BallStripes(POS_15TH , BROWN  , 15)

white_ball_full     = BallFulls(POS_16TH, WHITE, 16)

all_balls = (yellow_ball_full, blue_ball_full,
                red_ball_full, purple_ball_full, 
                orange_ball_full, green_ball_full,
                brown_ball_full , black_ball_full, 
                yellow_ball_stripes, blue_ball_stripes, 
                red_ball_stripes, purple_ball_stripes, 
                orange_ball_stripes, green_ball_stripes, 
                brown_ball_stripes, white_ball_full)