def convert_coordinates(points):                     # CHANGES PYGAME COORDINATES TO PYMUNK CARTESIAN COORDINATES // DOES SAME FROM PYMUNK TO PYGAME
    return (int(points[0]), SCREEN_LENGTH - int(points[1]))

###############################################
# SCREEN
SCREEN_WIDTH = 1700
SCREEN_LENGTH = 1000
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_LENGTH)

###############################################
# TABLE
LENGTH_TABLE = 700
WIDTH_TABLE = 1400
SIZE_TABLE = (WIDTH_TABLE, LENGTH_TABLE)

###############################################
# DISTANCE BETWEEN SCREEN AND TABLE
OFFSET_SCREEN_WIDTH  = (SCREEN_WIDTH  - WIDTH_TABLE)/2                            
OFFSET_SCREEN_LENGTH = (SCREEN_LENGTH - LENGTH_TABLE)/2

################################################
# TICKING
MAX_FPS = 220
FRAMERATE = 100

################################################
# BALL
SIZE_BALL = 23
OFFSET = SIZE_BALL + 1

################################################
# COLORS
COLOR_BOARD = (70,130,80)
COLOR_EDGE  = (70,100,50)

WHITE       = (250,250,250)
BLACK       = (0,0,0)

YELLOW      = (255,255,0)
BLUE        = (0,0,255)
RED         = (255,0,0)
PURPLE      = (128,0,128)
ORANGE      = (233,107,57)
GREEN       = (0,255,0)
BROWN       = (139,69,19)

################################################
# PYMUNK PHYSICS
ELASTICITY_TABLE = 0.9
ELASTICITY = 1
DENCITY = 0.1
MASS = 10

###############################################
# POSITIONING BALLS
POS_5TH = (OFFSET_SCREEN_WIDTH + 3 * WIDTH_TABLE/4), (OFFSET_SCREEN_LENGTH + LENGTH_TABLE/2 )

######## ROW 1
POS_1ST = (POS_5TH[0] - 86 ), (POS_5TH[1])

######## ROW 2
POS_2ND = (POS_5TH[0] - 43 ), (POS_5TH[1] - 25)
POS_3RD = (POS_5TH[0] - 43 ), (POS_5TH[1] + 25)

######## ROW 3
POS_4TH = (POS_5TH[0]), (POS_5TH[1] - 50)
#POS_5TH
POS_6TH = (POS_5TH[0]), (POS_5TH[1] + 50)

######## ROW 4
POS_7TH = (POS_5TH[0] + 43 ), (POS_5TH[1] - 75)
POS_8TH = (POS_5TH[0] + 43 ), (POS_5TH[1] - 25)
POS_9TH = (POS_5TH[0] + 43 ), (POS_5TH[1] + 25)
POS_10TH = (POS_5TH[0] + 43 ), (POS_5TH[1] + 75)

######## ROW 5
POS_11TH = (POS_5TH[0] + 86 ), (POS_5TH[1] - 100)
POS_12TH = (POS_5TH[0] + 86 ), (POS_5TH[1] - 50)
POS_13TH = (POS_5TH[0] + 86 ), (POS_5TH[1] )
POS_14TH = (POS_5TH[0] + 86 ), (POS_5TH[1] + 50)
POS_15TH = (POS_5TH[0] + 86 ), (POS_5TH[1] + 100)

POS_16TH = convert_coordinates(((OFFSET_SCREEN_WIDTH + WIDTH_TABLE/4), (OFFSET_SCREEN_LENGTH + LENGTH_TABLE/2)))


###############################################
# TABLE'S CORNERS COORDINATES
LEFT_BOTTOM_CORNER  = [OFFSET_SCREEN_WIDTH                , OFFSET_SCREEN_LENGTH]            
LEFT_UPPER_CORNER   = [OFFSET_SCREEN_WIDTH                , SCREEN_LENGTH - OFFSET_SCREEN_LENGTH]
RIGHT_BOTTOM_CORNER = [SCREEN_WIDTH - OFFSET_SCREEN_WIDTH , OFFSET_SCREEN_LENGTH]
RIGHT_UPPER_CORNER  = [SCREEN_WIDTH - OFFSET_SCREEN_WIDTH , SCREEN_LENGTH - OFFSET_SCREEN_LENGTH]

###############################################
# PARTS OF TABLE (STARTING POINT, ENDING POINT)
TABLE_BOTTOM_LEFT_WALL     = (LEFT_BOTTOM_CORNER[0] + 53                  , LEFT_BOTTOM_CORNER[1])          , (LEFT_BOTTOM_CORNER[0] + WIDTH_TABLE/2 - 38   , LEFT_BOTTOM_CORNER[1])
TABLE_BOTTOM_RIGHT_WALL    = (RIGHT_BOTTOM_CORNER[0] - WIDTH_TABLE/2 + 38 , RIGHT_BOTTOM_CORNER[1])         , (RIGHT_BOTTOM_CORNER[0] - 53                  , RIGHT_BOTTOM_CORNER[1])

TABLE_SIDE_LEFT_WALL       = (LEFT_BOTTOM_CORNER[0]                       , LEFT_BOTTOM_CORNER[1] + 53)     , (LEFT_UPPER_CORNER[0]                         , LEFT_UPPER_CORNER[1] - 53 )
TABLE_SIDE_RIGHT_WALL      = (RIGHT_BOTTOM_CORNER[0]                      , RIGHT_BOTTOM_CORNER[1] + 53)    , (RIGHT_UPPER_CORNER[0]                        , RIGHT_UPPER_CORNER[1] - 53)

TABLE_UPPER_LEFT_WALL      = (LEFT_UPPER_CORNER[0] + 53                   , LEFT_UPPER_CORNER[1])           , (LEFT_UPPER_CORNER[0] + WIDTH_TABLE/2 - 38    , LEFT_UPPER_CORNER[1])
TABLE_UPPER_RIGHT_WALL     = (RIGHT_UPPER_CORNER[0] - WIDTH_TABLE/2 + 38  , RIGHT_UPPER_CORNER[1])          , (RIGHT_UPPER_CORNER[0] - 53                   , RIGHT_UPPER_CORNER[1])

# SMALL WALLS BY HOLES
HOLE_BOTTOM_LEFT_WALL_ONE  = (LEFT_BOTTOM_CORNER[0] + 53                  , LEFT_BOTTOM_CORNER[1])          , (LEFT_BOTTOM_CORNER[0] + 53 - 100             , LEFT_BOTTOM_CORNER[1] - 100)
HOLE_BOTTOM_LEFT_WALL_TWO  = (LEFT_BOTTOM_CORNER[0]                       , LEFT_BOTTOM_CORNER[1] + 53)     , (LEFT_BOTTOM_CORNER[0] - 100                  , LEFT_BOTTOM_CORNER[1] + 53 - 100) 

HOLE_BOTTOM_CENTER_WALL_ONE= (LEFT_BOTTOM_CORNER[0] + WIDTH_TABLE/2 - 38  , LEFT_BOTTOM_CORNER[1])          , (LEFT_BOTTOM_CORNER[0] + WIDTH_TABLE/2 -38+25 , LEFT_BOTTOM_CORNER[1] - 75) 
HOLE_BOTTOM_CENTER_WALL_TWO= (RIGHT_BOTTOM_CORNER[0] - WIDTH_TABLE/2 + 38 , RIGHT_BOTTOM_CORNER[1])         , (RIGHT_BOTTOM_CORNER[0] -WIDTH_TABLE/2 +38-25 , RIGHT_BOTTOM_CORNER[1] - 75)

HOLE_BOTTOM_RIGHT_WALL_ONE = (RIGHT_BOTTOM_CORNER[0] - 53                 , RIGHT_BOTTOM_CORNER[1])         , (RIGHT_BOTTOM_CORNER[0] - 53 + 100            , RIGHT_BOTTOM_CORNER[1] - 100)
HOLE_BOTTOM_RIGHT_WALL_TWO = (RIGHT_BOTTOM_CORNER[0]                      , RIGHT_BOTTOM_CORNER[1] + 53)    , (RIGHT_BOTTOM_CORNER[0] + 100                 , RIGHT_BOTTOM_CORNER[1] + 53 - 100)

HOLE_UPPER_LEFT_WALL_ONE   = (LEFT_UPPER_CORNER[0]                        , LEFT_UPPER_CORNER[1] - 53)      , (LEFT_UPPER_CORNER[0] - 100                   , LEFT_UPPER_CORNER[1] - 53 + 100) 
HOLE_UPPER_LEFT_WALL_TWO   = (LEFT_UPPER_CORNER[0] + 53                   , LEFT_UPPER_CORNER[1])           , (LEFT_UPPER_CORNER[0] + 53 - 100              , LEFT_UPPER_CORNER[1] + 100)

HOLE_UPPER_CENTER_WALL_ONE= (LEFT_UPPER_CORNER[0] + WIDTH_TABLE/2 - 38    , LEFT_UPPER_CORNER[1])           , (LEFT_UPPER_CORNER[0] + WIDTH_TABLE/2 -38+25  , LEFT_UPPER_CORNER[1] + 75) 
HOLE_UPPER_CENTER_WALL_TWO= (RIGHT_UPPER_CORNER[0] - WIDTH_TABLE/2 + 38   , RIGHT_UPPER_CORNER[1])          , (RIGHT_UPPER_CORNER[0] -WIDTH_TABLE/2 +38-25  , RIGHT_UPPER_CORNER[1] + 75)

HOLE_UPPER_RIGHT_WALL_ONE = (RIGHT_UPPER_CORNER[0] - 53                   , RIGHT_UPPER_CORNER[1])          , (RIGHT_UPPER_CORNER[0] - 53 + 100             , RIGHT_UPPER_CORNER[1] + 100)
HOLE_UPPER_RIGHT_WALL_TWO = (RIGHT_UPPER_CORNER[0]                        , RIGHT_UPPER_CORNER[1] - 53)     , (RIGHT_UPPER_CORNER[0] + 100                  , RIGHT_UPPER_CORNER[1] - 53 + 100)

