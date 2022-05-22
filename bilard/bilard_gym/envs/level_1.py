from .ball import *
from random import randint


def place_one_ball_random_full(pymunk_space, ball_to_place):
    for ball in all_balls_full:
        if ball == ball_to_place:
            ball.is_in_hole = 0
            ball.body.position = randint(LEFT_BOTTOM_CORNER[0] + SIZE_BALL + 10,
                                         RIGHT_BOTTOM_CORNER[0] - SIZE_BALL - 10), randint(
                LEFT_BOTTOM_CORNER[1] + SIZE_BALL + 10, LEFT_UPPER_CORNER[1] - SIZE_BALL - 10)
            ball.body.velocity = 0, 0
            ball.add_to_pymunk_space(pymunk_space)
        else:
            ball.is_in_hole = 1
            ball.body.position = (3500, 2 * (SIZE_BALL + 2) * ball.shape.collision_type + SIZE_BALL)
            ball.body.velocity = 0, 0
            ball.add_to_pymunk_space(pymunk_space)

    for ball in all_balls_stripes:
        ball.is_in_hole = 1
        ball.body.position = (3500, 2 * (SIZE_BALL + 2) * ball.shape.collision_type + SIZE_BALL)
        ball.body.velocity = 0, 0
        ball.add_to_pymunk_space(pymunk_space)

    white_ball_full.body.position = randint(LEFT_BOTTOM_CORNER[0] + SIZE_BALL,
                                            RIGHT_BOTTOM_CORNER[0] - SIZE_BALL), randint(
        LEFT_BOTTOM_CORNER[1] + SIZE_BALL, LEFT_UPPER_CORNER[1] - SIZE_BALL)
    white_ball_full.body.velocity = 0, 0
    white_ball_full.add_to_pymunk_space(pymunk_space)
    white_ball_full.is_in_hole = 0
