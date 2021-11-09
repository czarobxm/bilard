import os, sys, random
import pygame, pymunk


class ColisionHandler():
    def __init__(self, hole_colision_type, this_ball_number):
        self.white_ball_number = hole_colision_type
        self.this_ball_number  = this_ball_number

    #def add_colission_handler(self, pymunk_space):
    #    self = pymunk_space.add_collision_handler(self.hole_colision_type, self.this_ball_number)

        


handler_yellow_full_hole    = space.add_collision_handler(0, 1)
handler_blue_full_hole      = ColisionHandler(0, 2)
handler_red_full_hole       = ColisionHandler(0, 3)
handler_purple_full_hole    = ColisionHandler(0, 4)
handler_orange_full_hole    = ColisionHandler(0, 5)
handler_green_full_hole     = ColisionHandler(0, 6)
handler_brown_full_hole     = ColisionHandler(0, 7)
handler_black_full_hole     = ColisionHandler(0, 8)

handler_yellow_stripes_hole = ColisionHandler(0, 9)
handler_blue_stripes_hole   = ColisionHandler(0, 10)
handler_red_stripes_hole    = ColisionHandler(0, 11)
handler_purple_stripes_hole = ColisionHandler(0, 12)
handler_orange_stripes_hole = ColisionHandler(0, 13)
handler_green_stripes_hole  = ColisionHandler(0, 14)
handler_brown_stripes_hole  = ColisionHandler(0, 15)

handler_white_full_hole     = ColisionHandler(0, 16)

all_handlers = [handler_yellow_full_hole, handler_blue_full_hole, handler_red_full_hole, handler_purple_full_hole, handler_orange_full_hole, handler_green_full_hole, handler_brown_full_hole, handler_black_full_hole, handler_yellow_stripes_hole, handler_blue_stripes_hole, handler_red_stripes_hole, handler_purple_stripes_hole, handler_orange_stripes_hole, handler_green_stripes_hole, handler_brown_stripes_hole, handler_white_full_hole]

