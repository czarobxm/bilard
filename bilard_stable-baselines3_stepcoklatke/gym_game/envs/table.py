import os, sys, random
import pygame, pymunk
from .CONST import *


class Table():
    def __init__(self):
        # WALLS
        self.body_floor_left    = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_floor_left   = pymunk.Segment(self.body_floor_left,TABLE_BOTTOM_LEFT_WALL[0], TABLE_BOTTOM_LEFT_WALL[1] , 1)
        
        self.body_floor_right   = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_floor_right  = pymunk.Segment(self.body_floor_right, TABLE_BOTTOM_RIGHT_WALL[0], TABLE_BOTTOM_RIGHT_WALL[1], 1)

        self.body_left_wall     = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_left_wall    = pymunk.Segment(self.body_left_wall,TABLE_SIDE_LEFT_WALL[0], TABLE_SIDE_LEFT_WALL[1] , 1)

        self.body_right_wall    = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_right_wall   = pymunk.Segment(self.body_right_wall,TABLE_SIDE_RIGHT_WALL[0], TABLE_SIDE_RIGHT_WALL[1] , 1)

        self.body_ceiling_left  = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_ceiling_left = pymunk.Segment(self.body_ceiling_left, TABLE_UPPER_LEFT_WALL[0], TABLE_UPPER_LEFT_WALL[1] , 1)

        self.body_ceiling_right = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_ceiling_right= pymunk.Segment(self.body_ceiling_right,TABLE_UPPER_RIGHT_WALL[0], TABLE_UPPER_RIGHT_WALL[1] , 1)

        # HOLES bottom
        self.body_hole_bottom_left_one    = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_bottom_left_one   = pymunk.Segment(self.body_hole_bottom_left_one, HOLE_BOTTOM_LEFT_WALL_ONE[0], HOLE_BOTTOM_LEFT_WALL_ONE[1], 1)

        self.body_hole_bottom_left_two    = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_bottom_left_two   = pymunk.Segment(self.body_hole_bottom_left_two, HOLE_BOTTOM_LEFT_WALL_TWO[0], HOLE_BOTTOM_LEFT_WALL_TWO[1], 1)
        
        self.body_hole_bottom_center_one  = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_bottom_center_one = pymunk.Segment(self.body_hole_bottom_center_one, HOLE_BOTTOM_CENTER_WALL_ONE[0], HOLE_BOTTOM_CENTER_WALL_ONE[1], 1)

        self.body_hole_bottom_center_two  = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_bottom_center_two = pymunk.Segment(self.body_hole_bottom_center_two, HOLE_BOTTOM_CENTER_WALL_TWO[0], HOLE_BOTTOM_CENTER_WALL_TWO[1], 1)
        
        self.body_hole_bottom_right_one   = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_bottom_right_one  = pymunk.Segment(self.body_hole_bottom_right_one, HOLE_BOTTOM_RIGHT_WALL_ONE[0], HOLE_BOTTOM_RIGHT_WALL_ONE[1], 1)

        self.body_hole_bottom_right_two   = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_bottom_right_two  = pymunk.Segment(self.body_hole_bottom_right_two, HOLE_BOTTOM_RIGHT_WALL_TWO[0], HOLE_BOTTOM_RIGHT_WALL_TWO[1], 1)

        # HOLES upper
        self.body_hole_upper_left_one    = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_upper_left_one   = pymunk.Segment(self.body_hole_upper_left_one, HOLE_UPPER_LEFT_WALL_ONE[0], HOLE_UPPER_LEFT_WALL_ONE[1], 1)

        self.body_hole_upper_left_two    = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_upper_left_two   = pymunk.Segment(self.body_hole_upper_left_two, HOLE_UPPER_LEFT_WALL_TWO[0], HOLE_UPPER_LEFT_WALL_TWO[1], 1)

        self.body_hole_upper_center_one  = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_upper_center_one = pymunk.Segment(self.body_hole_upper_center_one, HOLE_UPPER_CENTER_WALL_ONE[0], HOLE_UPPER_CENTER_WALL_ONE[1], 1)

        self.body_hole_upper_center_two  = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_upper_center_two = pymunk.Segment(self.body_hole_upper_center_two, HOLE_UPPER_CENTER_WALL_TWO[0], HOLE_UPPER_CENTER_WALL_TWO[1], 1)

        self.body_hole_upper_right_one   = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_upper_right_one  = pymunk.Segment(self.body_hole_upper_right_one, HOLE_UPPER_RIGHT_WALL_ONE[0], HOLE_UPPER_RIGHT_WALL_ONE[1], 1)

        self.body_hole_upper_right_two   = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape_hole_upper_right_two  = pymunk.Segment(self.body_hole_upper_right_two, HOLE_UPPER_RIGHT_WALL_TWO[0], HOLE_UPPER_RIGHT_WALL_TWO[1], 1)



        # COLLISION TYPE
        # walls
        self.shape_floor_left.collision_type = 50
        self.shape_floor_right.collision_type = 50
        self.shape_left_wall.collision_type = 50
        self.shape_right_wall.collision_type = 50
        self.shape_ceiling_left.collision_type = 50
        self.shape_ceiling_right.collision_type = 50
        # bottom holes
        self.shape_hole_bottom_left_one.collision_type = 50
        self.shape_hole_bottom_left_two.collision_type = 50
        self.shape_hole_bottom_center_one.collision_type = 50
        self.shape_hole_bottom_center_two.collision_type = 50
        self.shape_hole_bottom_right_one.collision_type = 50
        self.shape_hole_bottom_right_two.collision_type = 50
        # upper holes
        self.shape_hole_upper_left_one.collision_type = 50
        self.shape_hole_upper_left_two.collision_type = 50
        self.shape_hole_upper_center_one.collision_type = 50
        self.shape_hole_upper_center_two.collision_type = 50
        self.shape_hole_upper_right_one.collision_type = 50
        self.shape_hole_upper_right_two.collision_type = 50
        

        # ELASTICITY
        # walls
        self.shape_floor_left.elasticity = ELASTICITY_TABLE
        self.shape_floor_right.elasticity = ELASTICITY_TABLE
        self.shape_left_wall.elasticity = ELASTICITY_TABLE
        self.shape_right_wall.elasticity = ELASTICITY_TABLE
        self.shape_ceiling_left.elasticity = ELASTICITY_TABLE
        self.shape_ceiling_right.elasticity = ELASTICITY_TABLE
        # bottom holes
        self.shape_hole_bottom_left_one.elasticity = ELASTICITY_TABLE
        self.shape_hole_bottom_left_two.elasticity = ELASTICITY_TABLE
        self.shape_hole_bottom_center_one.elasticity = ELASTICITY_TABLE
        self.shape_hole_bottom_center_two.elasticity = ELASTICITY_TABLE
        self.shape_hole_bottom_right_one.elasticity = ELASTICITY_TABLE
        self.shape_hole_bottom_right_two.elasticity = ELASTICITY_TABLE
        # upper holes
        self.shape_hole_upper_left_one.elasticity = ELASTICITY_TABLE
        self.shape_hole_upper_left_two.elasticity = ELASTICITY_TABLE
        self.shape_hole_upper_center_one.elasticity = ELASTICITY_TABLE
        self.shape_hole_upper_center_two.elasticity = ELASTICITY_TABLE
        self.shape_hole_upper_right_one.elasticity = ELASTICITY_TABLE
        self.shape_hole_upper_right_two.elasticity = ELASTICITY_TABLE

    def add_to_pymunk_space(self,pymunk_space):
        
        # ADDING TO PYMUNK SPACE
        # walls
        pymunk_space.add(self.body_ceiling_left, self.shape_ceiling_left)
        pymunk_space.add(self.body_ceiling_right, self.shape_ceiling_right)
        pymunk_space.add(self.body_floor_left, self.shape_floor_left)
        pymunk_space.add(self.body_floor_right, self.shape_floor_right)
        pymunk_space.add(self.body_left_wall, self.shape_left_wall)
        pymunk_space.add(self.body_right_wall, self.shape_right_wall)
        # bottom holes
        pymunk_space.add(self.shape_hole_bottom_left_one, self.body_hole_bottom_left_one)
        pymunk_space.add(self.shape_hole_bottom_left_two, self.body_hole_bottom_left_two)
        pymunk_space.add(self.shape_hole_bottom_center_one, self.body_hole_bottom_center_one)
        pymunk_space.add(self.shape_hole_bottom_center_two, self.body_hole_bottom_center_two)
        pymunk_space.add(self.shape_hole_bottom_right_one, self.body_hole_bottom_right_one)
        pymunk_space.add(self.shape_hole_bottom_right_two, self.body_hole_bottom_right_two)
        # upper holes
        pymunk_space.add(self.shape_hole_upper_left_one, self.body_hole_upper_left_one)
        pymunk_space.add(self.shape_hole_upper_left_two, self.body_hole_upper_left_two)
        pymunk_space.add(self.shape_hole_upper_center_one, self.body_hole_upper_center_one)
        pymunk_space.add(self.shape_hole_upper_center_two, self.body_hole_upper_center_two)
        pymunk_space.add(self.shape_hole_upper_right_one, self.body_hole_upper_right_one)
        pymunk_space.add(self.shape_hole_upper_right_two, self.body_hole_upper_right_two)

    def remove_from_pymunk_space(self,pymunk_space):
        
        # REMOVING TABLE FROM PYMUNK SPACE
        # walls
        pymunk_space.remove(self.body_ceiling_left, self.shape_ceiling_left)
        pymunk_space.remove(self.body_ceiling_right, self.shape_ceiling_right)
        pymunk_space.remove(self.body_floor_left, self.shape_floor_left)
        pymunk_space.remove(self.body_floor_right, self.shape_floor_right)
        pymunk_space.remove(self.body_left_wall, self.shape_left_wall)
        pymunk_space.remove(self.body_right_wall, self.shape_right_wall)
        # bottom holes
        pymunk_space.remove(self.shape_hole_bottom_left_one, self.body_hole_bottom_left_one)
        pymunk_space.remove(self.shape_hole_bottom_left_two, self.body_hole_bottom_left_two)
        pymunk_space.remove(self.shape_hole_bottom_center_one, self.body_hole_bottom_center_one)
        pymunk_space.remove(self.shape_hole_bottom_center_two, self.body_hole_bottom_center_two)
        pymunk_space.remove(self.shape_hole_bottom_right_one, self.body_hole_bottom_right_one)
        pymunk_space.remove(self.shape_hole_bottom_right_two, self.body_hole_bottom_right_two)
        # upper holes
        pymunk_space.remove(self.shape_hole_upper_left_one, self.body_hole_upper_left_one)
        pymunk_space.remove(self.shape_hole_upper_left_two, self.body_hole_upper_left_two)
        pymunk_space.remove(self.shape_hole_upper_center_one, self.body_hole_upper_center_one)
        pymunk_space.remove(self.shape_hole_upper_center_two, self.body_hole_upper_center_two)
        pymunk_space.remove(self.shape_hole_upper_right_one, self.body_hole_upper_right_one)
        pymunk_space.remove(self.shape_hole_upper_right_two, self.body_hole_upper_right_two)

    def draw(self, screen):
        pygame.draw.rect(screen, COLOR_EDGE, (OFFSET_SCREEN_WIDTH-30, OFFSET_SCREEN_LENGTH-30, WIDTH_TABLE + 60, LENGTH_TABLE + 60), 0 )
        pygame.draw.rect(screen, COLOR_BOARD, (OFFSET_SCREEN_WIDTH, OFFSET_SCREEN_LENGTH, WIDTH_TABLE, LENGTH_TABLE), 0 )

        pygame.draw.line(screen, BLACK, TABLE_BOTTOM_LEFT_WALL[0]    , TABLE_BOTTOM_LEFT_WALL[1] , 1)
        pygame.draw.line(screen, BLACK, TABLE_BOTTOM_RIGHT_WALL[0]   , TABLE_BOTTOM_RIGHT_WALL[1], 1)
        pygame.draw.line(screen, BLACK, TABLE_UPPER_LEFT_WALL[0]     , TABLE_UPPER_LEFT_WALL[1]  , 1)
        pygame.draw.line(screen, BLACK, TABLE_UPPER_RIGHT_WALL[0]    , TABLE_UPPER_RIGHT_WALL[1] , 1)
        pygame.draw.line(screen, BLACK, TABLE_SIDE_LEFT_WALL[0]      , TABLE_SIDE_LEFT_WALL[1]   , 1)
        pygame.draw.line(screen, BLACK, TABLE_SIDE_RIGHT_WALL[0]     , TABLE_SIDE_RIGHT_WALL[1]  , 1)

        pygame.draw.line(screen, BLACK, HOLE_BOTTOM_LEFT_WALL_ONE[0] , HOLE_BOTTOM_LEFT_WALL_ONE[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_BOTTOM_LEFT_WALL_TWO[0] , HOLE_BOTTOM_LEFT_WALL_TWO[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_BOTTOM_CENTER_WALL_ONE[0],HOLE_BOTTOM_CENTER_WALL_ONE[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_BOTTOM_CENTER_WALL_TWO[0],HOLE_BOTTOM_CENTER_WALL_TWO[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_BOTTOM_RIGHT_WALL_ONE[0], HOLE_BOTTOM_RIGHT_WALL_ONE[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_BOTTOM_RIGHT_WALL_TWO[0], HOLE_BOTTOM_RIGHT_WALL_TWO[1], 1)

        pygame.draw.line(screen, BLACK, HOLE_UPPER_LEFT_WALL_ONE[0]  , HOLE_UPPER_LEFT_WALL_ONE[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_UPPER_LEFT_WALL_TWO[0]  , HOLE_UPPER_LEFT_WALL_TWO[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_UPPER_CENTER_WALL_ONE[0], HOLE_UPPER_CENTER_WALL_ONE[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_UPPER_CENTER_WALL_TWO[0], HOLE_UPPER_CENTER_WALL_TWO[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_UPPER_RIGHT_WALL_ONE[0] , HOLE_UPPER_RIGHT_WALL_ONE[1], 1)
        pygame.draw.line(screen, BLACK, HOLE_UPPER_RIGHT_WALL_TWO[0] , HOLE_UPPER_RIGHT_WALL_TWO[1], 1)


table = Table()